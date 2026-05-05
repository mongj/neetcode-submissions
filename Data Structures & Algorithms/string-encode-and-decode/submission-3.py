class Solution:

    def encode(self, strs: List[str]) -> str:
        enc_str = ""
        for s in strs:
            enc_str += str(len(s)) + "-" + s
        return enc_str


    def decode(self, s: str) -> List[str]:
        print(s)
        decoded_strs = []
        length_buffer = ""
        p = 0
        while p < len(s):
            if s[p] != "-":
                length_buffer += s[p]
                p += 1
            elif s[p] == "-":
                curr_str_length = int(length_buffer)
                decoded_strs.append(s[p + 1:p + 1 + curr_str_length])
                length_buffer = ""
                p = p + 1 + curr_str_length
        return decoded_strs

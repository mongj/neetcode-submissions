class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        DIRS = [(1,0),(0,1),(-1,0),(0,-1)]
        nr = len(board)
        nc = len(board[0])

        def check(r: int, c: int, word_index: int) -> bool:
            if r < 0 or c < 0 or r >= nr or c >= nc:
                return False
            
            if board[r][c] != word[word_index]:
                return False

            # check if this is the last letter
            if word_index == len(word) - 1:
                return True

            # mark the cell as seen
            board[r][c] += "_SEEN"

            if any([check(r + dr, c + dc, word_index + 1) for dr, dc in DIRS]):
                return True
            else:
                # unmark the cell
                board[r][c] = board[r][c][:-5]
                return False
        
        for r in range(nr):
            for c in range(nc):
                if check(r, c, 0):
                    return True
        
        return False
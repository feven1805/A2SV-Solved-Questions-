class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        rows = [set() for _ in range(9)]
        cols = [set() for _ in range(9)]
        boxes = [set() for _ in range(9)]
        empty = []

        for i in range(9):
            for j in range(9):
                if board[i][j] == '.':
                    empty.append((i, j))
                else:
                    val = board[i][j]
                    rows[i].add(val)
                    cols[j].add(val)
                    boxes[(i // 3) * 3 + (j // 3)].add(val)

        def backtrack(k):
            if k == len(empty):
                return True

            r, c = empty[k]
            b = (r // 3) * 3 + (c // 3)

            for ch in '123456789':
                if ch not in rows[r] and ch not in cols[c] and ch not in boxes[b]:
                    board[r][c] = ch
                    rows[r].add(ch)
                    cols[c].add(ch)
                    boxes[b].add(ch)

                    if backtrack(k + 1):
                        return True

                    board[r][c] = '.'
                    rows[r].remove(ch)
                    cols[c].remove(ch)
                    boxes[b].remove(ch)

            return False

        backtrack(0)
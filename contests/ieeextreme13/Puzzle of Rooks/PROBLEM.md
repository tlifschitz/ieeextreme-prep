# Puzzle of Rooks

**IEEEXtreme 13.0** · Time limit: 1000 ms · Memory limit: 256 MB

**CS Academy:** <https://csacademy.com/ieeextreme-practice/task/puzzle-of-rooks/>

Some predict that by the year $2050$ AI will be able to solve most of the challenges we face today. You are a fan of the prediction, but your friend Lenny is not yet convinced. You therefore have to prove to her the power of AI by solving the /Puzzle of Rooks/!

There is a chessboard of infinite size. Each cell is identified based on its horizontal and vertical coordinates using an integer pair $(x, y)$. There are $n$ rooks located at $n$ initial cells on the chessboard. There are additionally $n$ target cells. To solve the puzzle, one must move the $n$ rooks, so that each of the target cells contains exactly one rook, and no two rooks attack each other at any time. Two rooks attack each other if they share a same row or column, i.e. their cells have a same $x$ or a same $y$ coordinate. The following operations may be performed:

- Move a rook on the chessboard to one of its horizontally or vertically adjacent cell. That is, moving a rook at cell $(x, y)$ left, right, up, or down changes its cell to $(x-1, y), (x+1, y), (x, y+1), (x, y-1)$ respectively.
- Record the position of a rook and temporarily remove it from the chessboard. The cell of the rook becomes empty. At most one rook can be temporarily removed at a time. In other words, the chessboard always has at least $n - 1$ rooks on it.
- Put the removed rook back to its recorded position on the chessboard. A new rook can be removed after a previously removed rook is put back.

You are to create an AI that will solve the Puzzle of Rooks. The AI shall find a sequence of operations that will move the $n$ rooks to the $n$ target positions without letting the rooks attack each other during the whole process.  Lenny is also very picky. She will only be convinced if your AI is efficient enough. More specifically, your AI shall solve the puzzle with no more than $2050$ operations!

## Standard input

The input has one integer $n$ on the first line.

Each of the next $n$ lines has two integers describing the initial cell of a rook.

Each of the next $n$ lines has two integers describing a target cell.

## Standard output

Output a single integer $k$ ($k \leq 2050$) on the first line, the number of operations your AI needs. Then print $k$ lines, each line is in the format `x y op`. `op` is a single character describing the type of operation performed on cell $(x, y)$:

- `L`,  `R`, `U`, `D`: Move the rook currently at cell $(x, y)$ left, right, up, or down.
- `T`: Temporarily remove the rook at cell $(x, y)$.
- `P`: Put the temporarily removed rook back to its recorded position $(x, y)$.

Note that as the chessboard is infinitely large, it is allowed that a rook is moved to a cell with negative coordinates.

If the output sequence contains more than $2050$ operations, or any of the operation provided is invalid (e.g. an operation results in two rooks attacking each other; attempting to move a rook at $(x, y)$ but the cell $(x, y)$ is empty; putting a removed rook back to a position different from what was recorded), your solution will receive /Wrong Answer/.

## Constraints and notes

- $1 \leq n \leq 10$
- All coordinates of the initial and target cells are between $1$ and $99$ inclusive.
- No two initial cells share a row or column.
- No two target cells share a row or column.
- At least one target cell is not among the initial cells.
- It can be proved that for any initial and target cells satisfying the given constraints a sequence of no more than $2050$ operations exists to solve the puzzle.

## Examples

### Example 1

Input:
```
2
1 1
2 2
1 2
2 1
```

Output:
```
6
2 2 T
1 1 R
2 1 R
2 2 P
2 2 L
3 1 L
```

### Example 2

Input:
```
3
1 2
2 3
3 1
3 2
2 1
1 3
```

Output:
```
18
2 3 U
1 2 L
2 4 T
3 1 L
2 1 L
2 4 P
0 2 T
1 1 U
1 2 U
0 2 P
1 3 T
0 2 D
2 4 D
2 3 R
3 3 D
0 1 R
1 1 R
1 3 P
```

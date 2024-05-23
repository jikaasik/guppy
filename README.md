<p align="center">
<img src="guppy.png" alt="Guppy" width="300"/>
</p>

# guppy
### A first attempt at programming a chess engine
This repo is a __work in progress__. It is primarily a fun side project that I am using to learn about chess programming. There are some well-developed libraries that would simplify this process, by my goal here is to learn, so this project is entirely built with the Python standard library. The only external library actively used is Pytest. In any case, a chess engine written in Python is unlikely to take on Stockfish or Leela anytime soon. We'll leave that to a future iteration in a faster language ("GOppy", perhaps :smirk:).

#### Board Representation
The board and pieces are represented as a set of 12 64-bit integers. While representing the board as a two-dimensional array is intuitive and works perfectly well for programming a chess game, an engine's search process is computationally too intensive for that. Luckily, the binary representation of a 64-bit integer maps conveniently to the 64 squares on a chess board, allowing the entire board to be represented by 12 integers (one for each piece type and color). Movement can then be represented by shifting bits in the binary representation of the integer representing any given piece.

```

  56 57 58 59 60 61 62 63    =>    8 a8 b8 c8 d8 e8 f8 g8 h8
  48 49 50 51 52 53 54 55    =>    7 a7 b7 c7 d7 e7 f7 g7 h7
  40 41 42 43 44 45 46 47    =>    6 a6 b6 c6 d6 e6 f6 g6 h6
  32 33 34 35 36 37 38 39    =>    5 a5 b5 c5 d5 e5 f5 g5 h5
  24 25 26 27 28 29 30 31    =>    4 a4 b4 c4 d4 e4 f4 g4 h4
  16 17 18 19 20 21 22 23    =>    3 a3 b3 c3 d3 e3 f3 g3 h3
  08 09 10 11 12 13 14 15    =>    2 a2 b2 c2 d2 e2 f2 g2 h2
  00 01 02 03 04 05 06 07    =>    1 a1 b1 c1 d1 e1 f1 g1 h1
                                     a  b  c  d  e  f  g  h
```

For example, for white pawns, the starting position is represented simply by the integer 65280, which, when expressed in its 64-bit binary form (and visualized as an 8 by 8 grid), looks like the table below. So, a single integer represents the positions of all of the white pawns in the game! Amazingly, the black pawns, represented by the integer `71776119061217280` still only use about half of the memory required by an empty string `""`. I have visualized the binary versions of the integers representing the white and black pawns below.

```
White pawns = 65280             = `0000000000000000000000000000000000000000000000001111111100000000`
Black pawns = 71776119061217280 = `0000000011111111000000000000000000000000000000000000000000000000`

White pawns: 65280                              Black pawns: 71776119061217280

0 0 0 0 0 0 0 0                                 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0       ♙ ♙ ♙ ♙ ♙ ♙ ♙ ♙   <=  1 1 1 1 1 1 1 1
0 0 0 0 0 0 0 0                                 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0                                 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0                                 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0                                 0 0 0 0 0 0 0 0
1 1 1 1 1 1 1 1   =>  ♟︎ ♟︎ ♟︎ ♟︎ ♟︎ ♟︎ ♟︎ ♟︎       0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0                                 0 0 0 0 0 0 0 0
```

#### Move Generation
... In progress ...

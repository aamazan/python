#### [The Almost Impossible Chessboard Puzzle [intermediate] — 6/XX/21](https://www.reddit.com/r/dailyprogrammer/comments/hrujc5/20200715_challenge_385_intermediate_the_almost/)


Prompt:
>"First, assume that there exists a function flip that takes a series of 64 bits (0 or 1) and a number from 0 to 63. This function returns the same series of bits with the corresponding bit flipped. Now, you need to write two functions. Function prisoner1 takes two inputs: a series S of 64 bits, and a number X from 0 to 63 (inclusive). It returns a number Y from 0 to 63.
Function prisoner2 takes one input: a series T of 64 bits. It returns a number from 0 to 63.
Now, you must make it so that if you flip S using the output of prisoner1 and pass the result to prisoner2, you get back the number X. Put another way, the following function must return True for every possible valid input S and X.""

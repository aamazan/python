#### [The Almost Impossible Chessboard Puzzle [intermediate] — 6/29/21](https://www.reddit.com/r/dailyprogrammer/comments/hrujc5/20200715_challenge_385_intermediate_the_almost/)


Prompt:
>"First, assume that there exists a function flip that takes a series of 64 bits (0 or 1) and a number from 0 to 63. This function returns the same series of bits with the corresponding bit flipped. Now, you need to write two functions. Function prisoner1 takes two inputs: a series S of 64 bits, and a number X from 0 to 63 (inclusive). It returns a number Y from 0 to 63.
Function prisoner2 takes one input: a series T of 64 bits. It returns a number from 0 to 63.
Now, you must make it so that if you flip S using the output of prisoner1 and pass the result to prisoner2, you get back the number X. Put another way, the following function must return True for every possible valid input S and X.""

I'm ashamed to admit I was unable to figure out the puzzle myself and instead had to rely on the solutions provided. Regardless, let's go into how the [solution](https://www.youtube.com/watch?v=as7Gkm7Y7h4&t=0s) works and my experience adapting it for Python code.

This project took a surprisingly long time. In the end, the biggest issue with my code was due to having tabbed for prisoner1's conditional statements instead of using the python-standard four spaces. While the compiler would throw errors when I made this mistake outside of the conditional statements, they weren't triggering the error for some reason. As a result, I had to test each function I'd finished up until that point to see which one was incorrectly implemented.

As a result of this bug, I learned a handy trick: the ctrl+f function differentiates between a tab and four spaces, so it can be useful to highlight the code's indentation to make sure everything's consistent. I definitely don't plan on making that mistake again.

As the solution is provided both [here](https://www.youtube.com/watch?v=as7Gkm7Y7h4&t=0s) and in a preceding paragraph, I'm only going to discuss the implementation. The primary functions to understand for this problem are prisoner1 and check_board.

check_board iterates through the string of bits representing the board and only counts the "heads" values of specific sets of columns (identified using the modulo operator) and rows (using a counter that iterated every time the current square completed a ring of integer values), assigning a bit based on whether or not the number of "heads" was odd. I'm sure there's a cleaner, more efficient implementation of check_board which probably involves nesting the for loops into a small loop that acts as an enumerator instead of doing individual passes and calculating column/row sums all at once instead of using individual loops for each pass.

prisoner1 follows the logic of the solution by taking the encoded board state from check_board, taking the exclusive-or of the board state and the "magic square" target, reconverting it back to an integer (to represent prisoner 1 choosing a square to flip).

Below is the aforementioned code:

    # the flip function takes a series s of 64 bits and
    # a number x s.t. 0 <= x <= 63
    # input: 64-bit string, integer
    # output: 64-bit string
    def flip(s, flipnum):
        if s[flipnum] == "0":
            temp = list(s)
            temp[flipnum] = "1"
            s = "".join(temp)
        elif s[flipnum] == "1":
            temp = list(s)
            temp[flipnum] = "0"
            s = "".join(temp)
        return s


    # check_board takes the current board and determines the encoded binary
    # input: 64-bit string
    # output: 6-bit string
    def check_board(s):
        result = "000000"
        check = 0 # for determining number of heads per section
        resbit = 5 # current bit of result being checked for
        # columns: designated by %8 (e.g. 8%8 == 0%8 = 0, so same column)
        # every other  (1,3,5,7) ((0-7))
        for i in range(0,64):
            if i%8 == 1 or i%8 == 3 or i%8 == 5 or i%8 == 7:
                if s[i] == "1":
                    check += 1
        checkres = str(check%2)
        temp = list(result)
        temp[resbit] = checkres
        result = "".join(temp)
        check = 0 # reinitialize
        resbit -= 1


        # skip two, check two (2,3,6,7)
        for i in range(0,64):
            if i%8 == 2 or i%8 == 3 or i%8 == 6 or i%8 == 7:
                if s[i] == "1":
                    check += 1
        checkres = str(check%2)
        temp = list(result)
        temp[resbit] = checkres
        result = "".join(temp)
        check = 0
        resbit -= 1


        # check latter half (4,5,6,7)
        for i in range(0,64):
            if i%8 == 4 or i%8 == 5 or i%8 == 6 or i%8 == 7:
                if s[i] == "1":
                    check += 1
        checkres = str(check%2)
        temp = list(result)
        temp[resbit] = checkres
        result = "".join(temp)
        check = 0
        resbit -= 1
        row = 0


        # rows:
        # every other  (1,3,5,7) ((0-7))
        for i in range(0,64):
            if row == 1 or row == 3 or row == 5 or row == 7:
                if s[i] == "1":
                    check += 1
            if (i%8 == 7):
                row += 1
        checkres = str(check%2)
        temp = list(result)
        temp[resbit] = checkres
        result = "".join(temp)
        check = 0
        resbit -= 1
        row = 0


        # skip two, check two (2,3,6,7)
        for i in range(0,64):
            if row == 2 or row == 3 or row == 6 or row == 7:
                if s[i] == "1":
                    check += 1
            if i%8 == 7:
                row += 1
        checkres = str(check%2)
        temp = list(result)
        temp[resbit] = checkres
        result = "".join(temp)
        check = 0
        resbit -= 1
        row = 0


        # check latter half (4,5,6,7)
        for i in range(0,64):
            if row == 4 or row == 5 or row == 6 or row == 7:
                if s[i] == "1":
                    check += 1
            if i%8 == 7:
                row += 1
        checkres = str(check%2)
        temp = list(result)
        temp[resbit] = checkres
        result = "".join(temp)

        return result


    # "Function prisoner1 takes two inputs: a series S of 64 bits,
    # and a number X from 0 to 63 (inclusive).
    # It returns a number Y from 0 to 63."
    # input: 64-bit string, integer
    # output: integer
    def prisoner1(s,x):
        bits = '{0:06b}'.format(x) # get binary for x, outputs bitstring
        board = check_board(s) # board = current state bitstr
        tempbits = list(bits)
        tempboard = list(board)
        result = ""
        for i in range(0,6): # lazy xor implementation
            if tempbits[i] == tempboard[i]:
                result = result + "0"
            else:
                result = result + "1"
        result = int(result,2) # convert bitstr to int
        return result #square to be flipped


    # "Function prisoner2 takes one input: a series T of 64 bits.
    # It returns a number from 0 to 63."
    # input: 64-bit string
    # output: integer
    def prisoner2(t):
        bits = check_board(t) # bitstr to decode
        result = int(bits,2) # convert bitstr to int
        return result


    # Function solve provided with the prompt
    def solve(S, X):
        Y = prisoner1(S, X)
        T = flip(S, Y)
        return prisoner2(T) == X

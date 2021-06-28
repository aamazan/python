#### [Pancake Sort Challenge [intermediate] — 6/15/21](https://www.reddit.com/r/dailyprogrammer/comments/np3sio/20210531_challenge_392_intermediate_pancake_sort/)


Prompt:
>"Implement the flipfront function. Given an array of integers and a number n between 2 and the length of the array (inclusive), return the array with the order of the first n elements reversed. ...Given an array of integers, sort the array (smallest to largest) using the flipfront function on the entire array.
...Make sure you correctly handle elements that appear more than once in the array!
You may not modify the array by any other means, but you may examine it however you want."

The flipfront portion of the prompt was fairly simple and took little time, but the second part was surprisingly tricky, not because the theory behind the algorithm wasn't understood, but because of a lack of familiarity with some of Python's specific quirks (in this case, slicing arrays and what happens when a subarray is passed as an argument).

Pancake Sort is a fun algorithm. Although you may already understand it, I feel obliged to explain how it works (at the very least, to show that I understand it myself).
The function starts by taking a set and finding the largest value. This value is then flipped to the 0 index and out to the end of the array (which then becomes a "sorted" subset). The process then continues on the subset of items that does not include the largest item from the previous subset until the end of the array. This conveniently also allows for duplicates in the sorting process without messing things up for other indices.


Below is the code for all functions used in the exercise:

    # returns index of largest element of an array
    def largest(array):
        index = 0
        lgst = 0
        for i in range(0,len(array)):
            if array[i] > lgst:
                index = i
                lgst = array[i]
        return index

    # returns the set with the subset indices up to the nth reversed
    def flip_front(array, n):
        for i in range(0,math.floor(n/2)):
            temp = array[i]
            array[i] = array[(n-1)-i]
            array[(n-1)-i] = temp
        return array

    # returns the set sorted from least to greatest (duplicate-inclusive)
    def pancake_sort(array):
        for i in range(0, len(array)):
            l = largest(array[0:len(array)-i]) #largest in current subset
            flip_front(array, l+1)
            flip_front(array, len(array)-i)
        return array

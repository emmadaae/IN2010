from countswaps import CountSwaps

def sort(A:CountSwaps)-> CountSwaps:
    # Do insertion sort here. Use the Sorter's comparison- and swap
    # methods for automatically counting the swaps and comparisons.
    for i in range (1, len(A)):
        j = i
        while j > 0 and A[j-1] > A[j]:
            A.swap((j-1), j)
            j = j-1
    return A

    # Use A.""swap(i, j) to swap the values at two indices i and j. The swap is
    # counted, when using this method. Comparisons are counted automatically.

from countswaps import CountSwaps

import numpy as np
from typing import List, Optional
import statistics


def ChoosePivot(A: CountSwaps, low: int, high: int) -> int:
    n = len(A)
    return statistics.median([(A[low], low), (A[n//2],n//2), (A[high],high)])[1]

def Partition(A: CountSwaps, low:int , high:int) -> int :
    # Do quicksort here. Use the Sorter's comparison- and swap
    # methods for automatically counting the swaps and comparisons.

    # Use A.swap(i, j) to swap the values at two indices i and j. The swap is
    # counted, when using this method. Comparisons are counted automatically.

    n = len(A)
    p = ChoosePivot(A, low, high)
    A.swap(p, high)
    #A[p], A[high] = A[high], A[p]
    pivot = A[high]
    left = low
    right = high - 1

    while left <= right:
        while left <= right and A[left] <= pivot:
            left = left + 1

        while right >= left and A[right] >= pivot:
            right = right - 1

        if left < right:
            A.swap(left, right)

    A.swap(left, right)

    return left

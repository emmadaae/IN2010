from countswaps import CountSwaps
#Bubblesort med kompleksitet O(n^2)

def sort(A:CountSwaps)-> CountSwaps:
    for i in range(0, len(A) - 2):
        for j in range(0, len(A) - i - 2):
            if A[j] > A[j + 1]:
                #A[j], A[j + 1] = A[j + 1], A[j]
                A.swap(j, (j+1))
    return A

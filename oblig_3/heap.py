from countswaps import CountSwaps

def BubbleDown(A, i, n):
    largest = i
    left = 2*i + 1
    right = 2*i + 2

    if left < n and A[largest] < A[left]:
        left, largest = largest, left
        #A.swap(left, largest)

    if right < n and A[largest] < A[right]:
        right, largest = largest, right
        #A.swap(right, largest)

    if i != largest:
        #A[largest], A[i] = A[i], A[largest]
        A.swap(largest, i)
        BubbleDown(A, largest, n)

def BuildMaxHeap(A, n):
    n = len(A)
    i = n//2
    for j in range(i, 0, -1):
        BubbleDown(A, j, n)

#Heapsort med kompleksitet O(log(n))
def sort(A:CountSwaps)-> CountSwaps:
    n = len(A)
    BuildMaxHeap(A, n)
    for i in range(n - 1, 0,-1):
        #A[0], A[i] = A[i], A[0]
        A.swap(i,0)
        BubbleDown(A, 0, i)
    return A

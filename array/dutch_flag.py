#Reorder the array so the result is [smaller elements, pivot elements, larger elements]
def dutchFlag(pivot, A):
    pivElem = A[pivot]
    #bottomGroup - A[:smaler]
    #middleGroup - A[smaller:equal]
    #topGroup - A[larger:]
    smaller, equal, larger = 0, 0, len(A)
    while equal < larger:
        #A[equal] is unclassified element
        if A[equal] < pivElem:
            A[smaller], A[equal] = A[equal], A[smaller]
            smaller, equal = smaller + 1, equal + 1
        elif A[equal] == pivElem:
            equal += 1
        else:
            larger -=1
            A[equal], A[larger] = A[larger], A[equal]
    return A

if __name__ == "__main__":
    A = [1,2,4,5,3,6,7,8,4,5,6,10,33,22]
    print(dutchFlag(3, A))
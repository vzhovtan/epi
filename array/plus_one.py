#Add 1 to the digital nnon-negative number represented by array, i.e 101 is represented by [1,0,1]
def plusOne(A):
    A[-1] += 1
    for i in reversed(range(1, len(A))):
        if A[i] != 10:
            break
        A[i] = 0
        A[i-1] += 1

    if A[0] == 10:
        A[0] = 1
        A.append(0)

    return A

if __name__ == "__main__":
    print(plusOne([1,9 ,9]))

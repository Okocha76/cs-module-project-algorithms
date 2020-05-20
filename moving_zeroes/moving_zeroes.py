'''
Input: a List of integers
Returns: a List of integers
'''
def moving_zeroes(arr):
    # create zeroes array with len(arr)
    moved_zeroes = [0] * len(arr)

    i = 0

    # loop through array
    for k in range(len(arr)):
        # if element is non-zero, overwrite from left
        if arr[k] != 0:
            moved_zeroes[i] = arr[k]
            i += 1

    return moved_zeroes


if __name__ == '__main__':
    # Use the main function here to test out your implementation
    arr = [0, 3, 1, 0, -2]

    print(f"The resulting of moving_zeroes is: {moving_zeroes(arr)}")
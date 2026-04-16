def merge(left_half, right_half):
        global ops
        if left_half[-1] > right_half[0]:
            ops += 1
            return right_half + left_half
        else:
            return left_half + right_half



    def divide(left, right, arr):
        if left == right:
            return [arr[left]]

        mid = left + (right - left) // 2
        left_half = divide(left, mid, arr)
        right_half = divide(mid + 1, right, arr)

        return merge(left_half, right_half)

    if divide(0, m - 1, arr) != sorted(arr):
        print(-1)
    else:
        print(ops)
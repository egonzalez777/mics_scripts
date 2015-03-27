def pairSumV1(arr, k):
    """ O(NLogN) """

    if len(arr) < 2:
        return
    arr.sort()
    left, right = (0, len(arr) - 1)

    while left < right:
        current_sum = arr[left] + arr[right]
        if current_sum == k:
            print arr[left] + arr[right], (arr[left], arr[right],)
            left += 1
        elif current_sum < k:
            left += 1
        else:
            right -= 1


def pairSumV2(arr, k):
    """ O(N) """

    if len(arr) < 2:
        return
    seen = set()
    output = set()
    for num in arr:
        target = k - num
        print 'target:', target
        if target not in seen:
            seen.add(num)
        else:
            output.add((min(num, target), max(num, target)))

    print '\n'.join(map(str, list(output)))

pairSumV1([1, 2, 3, 4], 6)
pairSumV2([1, 2, 3, 4], 6)

# -*- coding: utf-8 -*-


def ten_sum_exists(matrix):
    """Calculate if the numbers provided can sum to 10.
    :Parameter:
        matrix: list
    :Returns:
        boolean, dict
    """

    if not isinstance(matrix, list):
        return

    length = len(matrix)
    count = 0
    pointer = 0
    ten_sum_count = 0
    # Capture all the sets that calculate to 10.
    calculated_sums = set()

    while True:
        if count <= length:
            if matrix[pointer] + matrix[count] == 10:
                calculated_sums.add((matrix[pointer], matrix[count]))
                ten_sum_count = ten_sum_count + 1
            count = count + 1
            if count == length:
                count = 0
                pointer = pointer + 1
            if pointer == length:
                break
    return ten_sum_count > 0, dict(sums=calculated_sums,
                                   total_sum=ten_sum_count)


if __name__ == '__main__':
    works = [9, 29, 8, 9, 28, 1, 9, 4, 5, 20]
    wont_work = [1, -5, 8, 0]
    custom = [-100, -4, 14, 12, 9, 4, 0]

    print(ten_sum_exists(works))
    print(ten_sum_exists(wont_work))
    print(ten_sum_exists(custom))

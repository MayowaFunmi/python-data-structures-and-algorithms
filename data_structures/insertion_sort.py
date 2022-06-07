def insertion_sort(elements):
    for i in range(1, len(elements)):
        anchor = elements[i]
        j = i - 1
        while j >= 0 and anchor < elements[j]:
            elements[j+1] = elements[j]
            j = j - 1
        elements[j+1] = anchor


def normal_sort(elements):
    x = sorted(elements)
    return x


if __name__ == '__main__':
    elements = [11, 9, 29, 7, 2, 15, 28]
    insertion_sort(elements)
    print(elements)
    print('normal sort = ', normal_sort(elements))

    tests = [
        [5, 9, 2, 1, 67, 34, 88, 34],
        [3, 7, 11, 9],
        [25, 22, 21, 10],
        [29, 15, 10],
        [],
        [6]
    ]

    for elements in tests:
        insertion_sort(elements)
        print(f'sorted array: {elements}')
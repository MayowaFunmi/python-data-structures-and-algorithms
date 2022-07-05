# find sum of list normally


def list_sum(num_list):
    the_sum = 0
    for i in num_list:
        the_sum += i
    return the_sum

print(list_sum([1, 3, 5, 7, 9]))


# using recursion
def sum_list(num_arr):
    if len(num_arr) == 1:
        return num_arr[0]
    return num_arr[0] + sum_list(num_arr[1:])

print(sum_list([1, 3, 5, 7, 9,10]))
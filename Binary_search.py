print('Binary search execute on a sorted list!!!')
print('Binary search === O(log n)')
import time

range_list = 100000000
my_list = [x for x in range(range_list)]
my_number = 99999999


def naive_search(arr, num):
    start = time.time()
    for i in arr:
        if i == num:
            end = time.time()
            return f'Searching for number: {num} in a range of: {range_list}\nFound ' \
                   f'the number in efficient time: {round(end-start,3)}'

print('\nNaive search')
print(naive_search(my_list, my_number))



def binary_search(arr, the_number):
    start = time.time()
    start_index = 0
    middle_index = len(arr)//2
    end_index = len(arr)

    while arr[middle_index] != the_number:

        if arr[middle_index] > the_number:
            end_index = middle_index
            middle_index -= int((middle_index - start_index)/2)

        else:
            start_index = middle_index
            middle_index += int((end_index-middle_index)/2)
    end = time.time()
    return f'Searching for number: {the_number} in a range of: {range_list}\nFound ' \
           f'the number in efficient time: {round(end - start, 3)}'


print('\nBinary search')
print(binary_search(my_list, my_number))

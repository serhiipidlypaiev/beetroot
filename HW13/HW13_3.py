
def choose_func(list, func1, func2):

    if all(x > 0 for x in list)==True:
        return square(list)
    else:
        return remove(list)

def square_nums(nums):
    return [num ** 2 for num in nums]


square = square_nums


def remove_negatives(nums):
    return [num for num in nums if num > 0]


remove = remove_negatives

nums1 = [1, 2, 3, 4, 5]
nums2 = [1, -2, 3, -4, 5]



print(choose_func(nums2, square, remove))
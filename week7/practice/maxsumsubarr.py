#The maximum sum subarray problem consists in finding the maximum sum of a contiguous subsequence in an array or list of integers:

# max_sequence([-2, 1, -3, 4, -1, 2, 1, -5, 4])
# # should be 6: [4, -1, 2, 1]

# Easy case is when the list is made up of only positive numbers and the maximum sum is the sum of the whole array. 
#If the list is made up of only negative numbers, return 0 instead.

# Empty list is considered to have zero greatest sum. Note that the empty list or array is also a valid sublist/subarray.

def max_sequence(arr):
    max_sum = 0
    current_sum = 0
    for i in arr:
        current_sum = max(0, current_sum + i)
        max_sum = max(max_sum, current_sum)
    return max_sum

print(max_sequence([-2, 1, -3, 4, -1, 2, 1, -5, 4])) # 6
print(max_sequence([])) # 0
print(max_sequence([-2, -1, -3, -4, -1, -2, -1, -5, -4])) # 0
print(max_sequence([1, 2, 3, 4, 5, 6, 7, 8, 9])) # 45
print(max_sequence([-1, -2, -3, -4, -5, -6, -7, -8, -9])) # 0


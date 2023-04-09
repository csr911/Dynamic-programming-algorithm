def max_subarray_sum(arr):
    max_so_far = float('-inf')
    max_ending_here = float('-inf')
    starting_index = 0
    ending_index = 0
    for i in range(len(arr)):
        change_starting_index = False
        if arr[i] < (max_ending_here + arr[i]):
            max_ending_here = max_ending_here + arr[i]
        else:
            max_ending_here = arr[i]
            change_starting_index = True
        if max_ending_here > max_so_far:
            max_so_far = max_ending_here
            if change_starting_index:
                starting_index = i
            ending_index = i
    print(f"\n     input array:   {arr}")
    print(f"\n    max subarray:   {arr[starting_index:ending_index+1]}")
    print(f"max subarray sum:   {max_so_far}")
    print(f"\n  starting index:   {starting_index}")
    print(f"    ending index:   {ending_index}\n")


input_array = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
max_subarray_sum(input_array)
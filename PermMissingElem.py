def solution(A):
    # write your code in Python 3.6
    sorted_array = sorted(A)
    array_len = len(A)
    # check if the array is empty or first element is 1
    if array_len == 0 or sorted_array[0] != 1:
        missing_num = 1
        return(missing_num)
    # iterate through each element
    else:
        for i in range(array_len-1): 
            # if the current element subtracted from the next element is not equal 1
            if sorted_array[i+1] - sorted_array[i] != 1:
                # calculate for the missing element as the current element + 1
                missing_num = sorted_array[i] + 1
                return(missing_num) 
        # if iteration is completed, calculate for the missing element as the last element + 1
        missing_num = sorted_array[array_len-1] + 1
        return(missing_num)
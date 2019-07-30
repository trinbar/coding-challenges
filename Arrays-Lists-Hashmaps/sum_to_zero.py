"""
Brute force approach.
O(n***3) runtime
O(1) space
"""

def brute_sum_to_zero(arr):
    """Checks if three integers in arr sum to zero. True/False."""

    #Return false if length of arr is less than 3
    if len(arr) < 3:
        return False

    #Iterate through the array with 3 pointers
    #First pointer at arr[0], can go up to third to last item in arr
    for i in range(0, len(arr)-2):
        #Second pointer at arr[1], can go up to second to last item in arr
        for j in range(1, len(arr)-1):
            #Third pointer at arr[2], can go up to last item in arr
            for k in range(2, len(arr)):
                #Check if sum to 0
                if (arr[i] + arr[j] + arr[k]) == 0:
                    return True

    return False

"""
Hashmap approach
O(n**2 runtime)
O(n) space
"""


def hash_sum_to_zero(arr):
    """Checks if three integers in arr sum to zero. True/False."""

    #Return false if length of arr is less than 3
    if len(arr) < 3:
        return False

    #Create a dictionary of the arr where key is the int and value is index
    arrdict = {x: arr.index(x) for x in arr2}

    #Iterate through the array with 2 pointers
    #First pointer at arr[0], can go up to second to last item in arr
    for i in range(0, len(arr) - 1):
        #Second pointer at arr[1], can go up to second to last item in arr
        for j in range(1, len(arr)):
            #Assign a temporary varisable for the negative value of arr[i] + arr[j]
            y = -(arr[i] + arr[j])
            #Check if y matches any key in arrdict
            if y in arrdict:
                return True
    
    return False



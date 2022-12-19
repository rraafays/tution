def find_minimum(array):  # define a function called find_minimum
    minimum = array[0]  # assume minimum is the first value of the array
    for i in range(len(array)):  # for i in the range of the array provided
        if minimum > array[i]:  # if minimum is greater than the current item
            minimum = array[i]  # replace minimum with the current item
    print(minimum)  # print the minimum value


find_minimum([3, 2, 3, 1])  # call method with array as the parameter

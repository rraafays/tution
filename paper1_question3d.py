val = 43  # set val to 43
arr = [3, 5, 13, 43, 655, 872]  # setting an array to a bunch of numbers
left = 1  # minimum (most left value) of the list
right = len(arr)  # maximum (rightmost value) length of the list (5)

while left != right:  # while left is not equal to right
    mid = int((left + right) / 2)  # set mid to the integer of left + right divided by 2 (midpoint)
    if val <= arr[mid]:  # if value is not equal to the value in the middle of the array
        right = mid  # half the array
    else:  # if value is not less than or equal to the middle value
        left = mid + 1  # moving the left most value by 1

for i in range(len(arr)):  # while i is less than the length of the array (5)
    if val == arr[i]:  # if value is equal to the value at array[i]
        print("true")  # print true
    else:  # if the value is not equal to the value at array[i]
        print("false")  # print false

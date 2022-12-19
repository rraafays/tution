hours = int(input("enter the hours 0-23 "))  # get the integer of the user's input

if hours < 12 and hours > 0:  # if hours is within 12 to 0
    print("it is " + str(hours) + "am now")  # tell them the time with am
elif hours > 12 and hours < 24:  # if hours is greater than 12 and less than 24
    print("it is " + str(hours - 12) + "pm now")  # tell them the time with pm
elif hours == 0:  # if hours is equal to 0
    print("it is 12am now")  # tell them that it is 12am
elif hours == 12:  # if hours is equal to 12
    print("it is 12pm now")  # tell them that it is 12pm

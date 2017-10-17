largest = None
smallest = None
while True:
    num = raw_input("Enter a number: ")
    if num == "done" : break
    try:
        num = int(num)
    except: 
        print num, "not a number, try again"
        continue
    
    else:
        if largest is None:
            largest = num
        elif smallest is None:
            if largest > num:
                smallest = num
            elif largest < num:
                smallest = largest
                largest = num
        elif num > largest:
            largest = num
        elif num < smallest:
            smallest = num
    print num

print "Maximum", largest
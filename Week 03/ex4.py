#get marks as integer input
marks = int(input("enter your marks(0-100): "))

#check if marks are within 0 - 100
if 0 <= marks <= 100:
    #check if the marks is greater or equal to 50
    if marks >= 50:
        #if true print pass
        print('pass')
    else:
        #if false print fail
        print('fail')
else:
    #if false print 'invalid marks'
    print('invalid mark')
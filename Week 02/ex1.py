#get the marks from the user
marks = float(input('enter marks (0 - 100) :'))

if marks < 0 or marks > 100: #check if the marks is within the range
    print('marks should be within 0 to 100')
    
elif marks >= 50: #check if the marks is grater than 50
    print('pass')
    
else:
    print('fail')

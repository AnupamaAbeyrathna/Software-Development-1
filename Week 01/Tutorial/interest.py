principle_balance = int(input("enter the initial principle balance :"))
interest_rate = int(input("enter the interest rate :"))
time = int(input("enter the time(in years) :"))

interest = principle_balance * interest_rate / 100 * time
final_amount = principle_balance + interest
print('final amount is ', final_amount)

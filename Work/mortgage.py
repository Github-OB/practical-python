# mortgage.py
#
# Exercise 1.7

extra_payment_start_month = int(input('Enter start month of extra payments:'))
extra_payment_end_month = int(input('Enter end month of extra payments:'))
extra_payment = int(input('Enter amount of extra payments:'))
#extra_payment = 1000
principal = 500000.0
rate = 0.05
payment = 2684.11
total_paid = 0.0
number_months = 0  


while principal > 0:
    number_months += 1 
    #print(number_months)
    principal = principal * (1+rate/12) - payment
    #print(principal)
    total_paid += payment
    #print(total_paid) 
    if  principal >  0:
        print(number_months, total_paid, principal)
    else:
        print(number_months, total_paid, 0)
    while (number_months >= extra_payment_start_month) and (number_months <= extra_payment_end_month):
        number_months += 1
        print("Now in extra payments")
        #print(number_months)
        principal = principal * (1+rate/12) - (payment + extra_payment) 
        #print(principal)
        total_paid += (payment + extra_payment)
        #print(total_paid)
        if principal > 0:
             print(number_months, total_paid, principal)
        else:
             print(number_months, total_paid, 0)
print ('Total paid', total_paid) 
print ('Total Months', number_months)


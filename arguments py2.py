def total_calculate(bill_amount,donation_amount):
    donation=(donation_amount/100)*bill_amount
    total_inc_tax = bill_amount + donation
    total = round(total_inc_tax,2)
    print(f"~~  please pay  ~~ {total_inc_tax}$")

total_calculate(25000,35)

def factorial(n):          # recursion - the number calls itself again from its body  
    if n == 1 or n == 0 :
        return 1
    else :
        return n * factorial (n - 1)

num = 5
print(f"wnter number of person ",num,"is",factorial(num))


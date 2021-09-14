income = int(input("\n>Please provide monthly income: "))



cat_one_tax=0
cat_two_tax=0
cat_three_tax=0

if 0<income<38000:
    cat_one_tax = 0.3*income

elif 38000<=income<=50000:
    cat_one_tax = 0.30*38000
    cat_two_tax = 0.35*(income-38000)

elif 50000 < income:
    cat_one_tax = 0.30*38000
    cat_two_tax = 0.35*(50000-38000)
    cat_three_tax = 0.40*(income-50000)

tax = cat_one_tax+cat_two_tax+cat_three_tax

print(f"\n> Corresponding income tax: {int(tax)} \n")


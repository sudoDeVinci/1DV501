price = float(input("\n> Price: "))
payment = float(input("\n> Payment: "))

change = round(payment-price)

print(f"\n> Change: {change} kr \n")

notes = [1000,500,200,100,50,20,10,5,2,1]
min = []


for note in notes:
    current_min = change//note
    min.append(current_min)
    change = change - (note*current_min)



out = f"1000kr bills: {min[0]}\n500kr bills: {min[1]}\n200kr bills: {min[2]}\n100kr bills: {min[3]}\n50kr bills: {min[4]}\n20kr bills: {min[5]}\n10kr coins: {min[6]}\n5kr coins: {min[7]}\n2kr coins: {min[8]}\n1kr coins: {min[9]}\n"

print(out)
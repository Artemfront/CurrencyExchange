dollar = 400
euro = 401
num = int(input("dollar 400, euro - 401: "))

if num == dollar:
    print("You chose dollar")
    sum = int(input("Enter the amount:"))
    if sum > 0:
        print("change: {0}".format(round(sum / 75, 1)))
    elif sum < 0:
        print("The amount must be greater than zero")
elif num == euro:
    print("You chose euro")
    sum = int(input("Enter the amount:"))
    if sum > 0:
        print("Обмен: {0}".format(round(sum / 90, 1)))
    elif sum < 0:
        print("The amount must be bigger than zero ")

input()

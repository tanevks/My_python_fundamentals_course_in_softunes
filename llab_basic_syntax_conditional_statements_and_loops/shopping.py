budget = int(input())
sum_product = 0
while True:
    command = (input())
    if command == "End":
        print("You bought everything needed.")
        break
    product_price = int(command)
    sum_product += product_price
    if sum_product > budget:
        print("You went in overdraft!")
        break

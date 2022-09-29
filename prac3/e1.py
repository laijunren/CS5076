def cal_total(total_on_receipt, items_num):
    if items_num < 10:
        discount = 0
    elif 10 <= items_num < 20:
        discount = 0.2
    elif 20 <= items_num < 30:
        discount = 0.3
    else:
        discount = 0.5

    total = total_on_receipt - (total_on_receipt * discount)
    return total

total_receipt = float(input("Enter total amount on the receipt?: "))
item_num = float(input("Enter number of items?: "))

final_amnt = cal_total(total_receipt,item_num)
print(f"Final amount to pay: {final_amnt}")



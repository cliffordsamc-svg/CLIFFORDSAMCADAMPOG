def display_menu(menu):
    print("\n===== FAST FOOD MENU =====")

    number = 1
    for item, price in menu.items():
        print(number, ".", item, "- P", price)
        number += 1


def print_receipt(receipt, total):
    print("\n========== RECEIPT ==========")
    print("Item\t\tQty\tPrice\tTotal")

    for order in receipt:
        print(order[0], "\t\t", order[1], "\tP", order[2], "\tP", order[3])

    print("-----------------------------")
    print("TOTAL: P", total)
    print("=============================")
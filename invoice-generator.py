print("=======================================================================")
print("\t\t\t\tINVOICE")
print("=======================================================================")

end = False

item_no = 0
total = 0.0

while (not end):
    msg = "Enter amount for item #" + str(item_no + 1) + ": Rs "
    price = float(input(msg))
    if (price == 0):
        end = True
    else:
        total += price
        item_no += 1
        print("\tprice entered: Rs {:.2f}".format(price))


print("=======================================================================")
print("TOTAL ITEMS purchased: {:d}".format(item_no))
print("TOTAL: Rs {:.2f}".format(total))

print("----------------------------------------------------------------------")
print ("\t\tThank You! Visit the Store Again")
print("-----------------------------------------------------------------------")

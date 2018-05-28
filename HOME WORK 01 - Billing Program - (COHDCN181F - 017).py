item_list=[]
price_list=[]
quantity_list=[]
c=0
total=0
print("Billing Program\n")


input("Press Enter to Start")

while True:
    Item_Name= input("Enter Item Name")
    if not Item_Name:
        break
    item_list.append(Item_Name)
    print(Item_Name)
    Item_Price= input("Enter Item Price")
    price_list.append(Item_Price)
    print(Item_Price)
    Item_Quantity= input("Enter Item Quantity")
    quantity_list.append(Item_Quantity)
    print(Item_Quantity)
    total+=int(Item_Price)*int(Item_Quantity)
    print(total)


if total >= 5000:
   discount=total*0.12
   total=total-discount
   print("Discount Value is :Rs %d" % discount)
   print("Discount Price is :Rs %d" % total)

elif total>= 3000:
    discount=total*0.1
    total=total-discount
    print("Discount Value is :Rs %d" % discount)
    print("Discount Price is :Rs %d" % total)

elif total>= 1000:
    y=total*0.05
    total=total-y 
    print("Discount Value is :Rs %d" % discount)
    print("Discount Price is :Rs %d" % total)

input("Press Enter to Save Text File")
f = open('output.txt','a')

for c in range(0, len(item_list)):
    f.write(item_list[int(c)] + "\t" + str(price_list[int(c)]) + "\n")

f.close()

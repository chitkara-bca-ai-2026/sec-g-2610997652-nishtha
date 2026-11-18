item=input("Enter Item Name:")
price=float(input("Enter Price Per Unit:"))
quantity=float(input("Enter Quantity:"))

final_amt=(price * quantity)

print("        TAX INVOICE         ")
print("Product Name: ",item)
print("Price Per Unit: ",price)
print("Quantity: ",quantity)
print("----------------------------")
print("Invoice Total:", final_amt)

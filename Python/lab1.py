x=int(input("enter tuition fee:"))
y=int(input("enter library fee:"))
z=int(input("enter lab fee:"))
a=int(input("enter exam fee:"))
discount=2500

total_fee_before_dis = x+y+z+a
total_fee_after_dis = total_fee_before_dis - discount
annual_fee = total_fee_after_dis * 2
mon_fee = annual_fee / 12

print("Tuition Fee: ",x)
print("Tuition Fee: ",y)
print("Tuition Fee: ",z)
print("Tuition Fee: ",a)
print("Total Fee: ",total_fee_before_dis)
print("Discount: ", discount)
print("Fee After Discount:", total_fee_after_dis)
print("Annual Fee:", annual_fee)
print("Monthly installment:", mon_fee)
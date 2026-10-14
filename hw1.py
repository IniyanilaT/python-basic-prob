product1 = int(input("price1"))
product2 = int(input("price2"))
total_bill = product1 + product2
print(total_bill)
if product1 > product2:
    print("higher price",product1)
else:
    print("higher price",product2)    
if product1 < product2:
    print("lower price",product1)
else:
    print("lower price",product2)        
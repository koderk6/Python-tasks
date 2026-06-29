# Discount program

print(" Welcome to our store! ".center(60,"#"))
totalValue = float(input("Please enter the total value of your items: "))
if totalValue < 100 :
    discount = 0
elif totalValue >= 100 and totalValue < 500:
    discount = 10
else:
    discount = 20
discountedTotal = totalValue * (1-discount/100)
print("-".center(60, "-"))
print(f"Available discount for you is {discount}%.")
print(f"Total Value after discount = {discountedTotal:.2f} L.E.")
print("-".center(60, "-"))

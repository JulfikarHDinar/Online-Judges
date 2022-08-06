noOfShoes = input()
shoeSize = input().split()
noOfCustomer = int(input())

totalPrice=0
for i in range(noOfCustomer):
  desiredShoeSize, price = input().split()
  if desiredShoeSize in shoeSize:
    totalPrice = totalPrice + int(price)
    shoeSize.remove(desiredShoeSize)


print(totalPrice)

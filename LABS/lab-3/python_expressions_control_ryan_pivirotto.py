#boolean
print(f"is 20 > 10? {20>10}")
print(f"is 5 < 2?{5<2}")
print(f"a: {10==7}")
print(f"b: 1==1")

#python Boolean
print("one is equal to 2:",int(1==2))
print("one is equal to 1",int(1==1))

#literals and variables
name = "Bob"
myAge = 34
print(f"a {63}") #numeric literal
print(f"B: {'Bonjour'}") #string literal
print(f"c: {False}")#constant literal
print(f"d: {name}")#string variable
print(f"e: {myAge}")#numeric variable

#precedence
print((1-5+9),(4-57+1))
print((10*2+34),(-3*2+60))

#relational operators
print(f"is 'briar'=='briar tuck'? {'briar'=='briar tuck'}")

#Equality operator
myName = "Piv"
print("assignment: ",myName)
print("equality: ",myName == 'Piv')

#comparison operator
print("comparison: ","ddd" < "b")
print("comparison: ", 5<6)

a = 34
b = 65
print(f"comparison: {a} is greater than {b}" if a > b else '')
print(f"comparison: {a} is less than {b}" if a < b else '')
print(f"comparison: {a} is greater than or equal to {b}" if a >= b else '')
print(f"comparison: {a} is less than or equal to {b}" if a <= b else '')

#If statements
bankBalance = 24
if bankBalance < 100:
  money = 1000
  bankBalance += money
  print(bankBalance)

#else statement
bankBalance = 23
if bankBalance > 100:
  money = 1000
  bankBalance += money
else:
    print("balance is less than or equal to 100. you are broke.")

#elif statement
bankBalance = 575
savings = 1000
if bankBalance < 100:
  money = 1000
  bankBalance += money
elif bankBalance> 200:
  savings += 100
  bankBalance -= 100
else:
  savings =+ 50
  bankBalance -= 50
print("Bank Balance is: ",bankBalance)
print("Your savings are: ", savings)

#ternary
fuel = 0.5
print("Fill tank now" if fuel <= 1 else "There's enough fuel")

#looping
fuel = 9
while fuel > 1:
  print("There's Enough Fuel")
  fuel -=1

#for loop
books = ['harry potter', 'book title #3', 'book title # 57']
for book in books:
  print(f"book: {book}")

for count in range(13):
  print(f"{count} times 111 is {count * 111}")
  if count == 7 :
    break

for count in range(13):
  if count==7:
      continue
  print(f"{count} times 111 is {count * 111}") 
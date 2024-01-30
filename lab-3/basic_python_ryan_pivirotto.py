#comments
#This is a single line comment

#Literals
print('Anakin') # this is an object of type string.
print(68.901) # this is a number. Technically a float.

#variable names
a=15
b=20
print(a+b)

a=10
A=20
print(a,A)

student_gpa = 2.8
print(type(student_gpa))

#lVariables
user_name = 'Horizon'
gpa = 13
print(user_name,gpa)

#Strings and varibales, + and f strings
name = 'Ryan'
print('My name is ' + name + ' not RICK')
print(f'My name is {name} not RICK')

#converting between types and substring
name = "Wookie"
name = 12345
number = 151 * 10984
print(str(number)[0:3]) #Converting number to a string and getting first 3 characters

#a,b function
def add_numbers(a,b):
  output = a+b
  return output
  print(b)

print(add_numbers(50,2)) #positional arguments
print(add_numbers(b=9,a=1)) #named arguments

#say hello function
name = 'Tiem'
def say_hello():
  name = 'Riane'
  print(name)
say_hello()


 What is Python? How does it works? Who developed it? why is it highly recommended today? and what are it's application?
 -  Python is a high-level, versatile, and interpreted programming language known for its simplicity and readability which is Created by 
Guido van Rossum and first released in 1991, which was named as 'Python' as inspired by the then popular show 
"Monty Python ", Python has become one of the most popular programming languages in the world.
  Why Learn Python?
- Beginner-friendly and widely used in the industry.
- High demand in job markets for roles like data scientists, software developers, and AI specialists.
- Extensive learning resources and an active support community.
  

  Note : Make sure to follow the indentation rule in python, Indentation rule is highly sensative in python.

  

# Program to print the message "Hello future developers".
print("Hello future developers")

#program to input the value and then display it.
  num = int(input("Enter number: "))
  print(f"The number you entered is {num}")

#program to display the the following message.
      Hello <your_name>,
                Congratulation, you finally learn the basic python.
                
Code:
    name = input("Enter the name: ")
    print(f"Hello {name},\n Congratulation, you finally learn the basic python."

#Program in python to input the name and display it
 Code:
 name = input("Enter the name: ")
 print(f"The name you entered was {name}")

#program to input any two numbers and calcualte it's addition.

Code:
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

print(f"The addition of {num1} and {num2} is ",num1+num2)

#Program to input number and find it's factorial.

Code:
num = int(input("Enter number: ")
fact = 1
for x in range(1 , num + 1):
    fact = fact*i

print(f"The factorial of {num} is {fact}")

#program to input any number and display the multiplication table.

Code:
num = int(input("Enter the number: "))
print(f"Multiplication table for {num}")
for i in range(1,10):
    print(f"{num} X {i}={num*i}")

#Program in python to check whether the number is odd or even

Code:
num = int(input("Enter the number: "))
if num%2==0:
    print(f"The number {num} is even.")
else:
    print(f"The number {num} is odd")

#Program to check the message is spam msg or not
Code:

p1 = "Make money with this"
p2 = "Click here"
p3 = "Follow me"
p4 = "Download now"

msg = input("Enter the message: ")

print(f"Message entered: {msg}")

if((p1.lower() in msg.lower()) or (p2.lower() in msg.lower()) or (p3.lower() in msg.lower()) or (p4.lower() in msg.lower())):
    print("This message is spam")
else:
    print("This message is not spam")


#program to access the password until it is satisfied !

Code:
password = input("Enter the password ")
while password != "password123":
    password = input("Enter the password: ")

print("Access granted ")

#program to input the name until it is satisfied. 

Code:
name = input("Enter your good name: ")

while name =="":
    print("Message cannot be empty, !")
    name = input("Enter your good name: ")

print(f"The message you entered was {name}")


#program to make a payment receipt transaction

Code:
product_name = input("What do you want to purchase?\n: ")
product_price = int(input(f"What's the cost of {product_name}?\n"))
product_qty = int(input(f"How much  {product_name}?\n"))

total_cost = product_price * product_qty

print(f"The total transaction cost for {product_qty} {product_name} is + {total_cost}")

#Program to input principal, time and rate and find the simple interest.

Code:
p = int(input("Enter the principal: "))
t = float(input("Enter the time: "))
r = float(input("Enter the rate: "))

si = (p*t*r)/100
print(f"The simple interest is {si}") 

#program to input any three numbers and find the greatest number among them.

Code:
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
num3 = int(input("Enter third number: "))

if(num1 >= num2 and num1 >= num3):
     max = num1;
elif(num2 >= num1 and num2 >= num3):
    max = num2;
else:
    max = num3;

print(f"The greatest number is {max}")


            Contents in progress ...
    

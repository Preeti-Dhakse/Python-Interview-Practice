Day-01

Q1.Reverse a String
text = "Python"
output: nohtyP

code : 

approch 1. text = "Python"
           rev = text[::-1]
           print(rev)

approch 2.text = "Python"
          rev = ""
          for ch in text :
            rev = ch + rev
          print(rev)


Q2.Even or Odd
num = 17

approch 1. def num_even_odd(num):
           if num % 2==0 :
             return "even"
           return "odd"
print(num_even_odd(6))


approch 2. num = int (input("enter a number :"))
          if num % 2 == 0:
            print("even number")
          else:
           print("odd number")

Q3. Swap Two Numbers
input : a = 10,b = 20
output :a = 20,b = 10

approch 1 .
a = int (input("enter a number :"))
b = int (input("enter b number :"))

a = a^b
b = a^b
a = a^b

print("a = " , a)
print("b = " , b)

approch 2. 
a = int (input("enter a number :"))
b = int (input("enter b number :"))

a = a+b
b = a-b
a = a-b

print("a = " , a)
print("b = " , b)

approch 3.
a = int (input("enter a number :"))
b = int (input("enter b number :"))

temp = a
a = b
b = temp

print("a = " , a)
print("b = " , b)

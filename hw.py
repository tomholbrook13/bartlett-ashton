print("     Hello, World!  ".split(","))

x = 5
print(x)

y = 6
print(y)

z = x + y
print(z)

if x < y:
 print("5 is less than 6")
else:
 print("6 is less than 5")
 
 
teststr = str(3)
testint = int(3)
testfloat = float(3)

print(teststr)
print(testint)
print(testfloat)

X, Y, Z = "Orange", "Banana", "Cherry"
print(X)
print(Y)
print(Z)

cars = ["Clio", "Scenic", "C4", "Mondeo"]

b = 1

def myfunc():
 b = 0
 print(b)
#while loop test
 while b < 4:
  a = cars[b]
  print(a)
  b = b + 1
  
myfunc()

print(b)

#for loop test
b = 0
for b in [0,1,2,3]:
 a = cars[b]
 print(a)
 
b = 0
[print(b) for b in cars]

newlist = []
for b in cars:
 if "e" in b:
  newlist.append(b)
  
print(newlist)

r = range(10)
newr = [x for x in r]
print(newr)

def myfunc2(n):
 return abs(n - 50)
 
thislist = [100,23,32,60,50]
thislist.sort(key = myfunc2)
print(thislist)

def reversestring():
    #input string
    stringtoflip = input()
    print(stringtoflip)
    #turn string into an iterable
    listtoflip = list(stringtoflip)
    print(listtoflip)
    #reverse iterable
    listtoflip.reverse()
    print(listtoflip)
    #reform a string
    reversestring = ""
    for letter in listtoflip:
     reversestring = reversestring + letter
     
    print(reversestring)

def biggestnumber():
 f = 0
 numbers = []
 while f < 5:
  numbers.append(input())
  f = f + 1
 
 numbers.sort(reverse = True)

 print("Biggest number is " + str(numbers[0]))

#biggestnumber()

def fahrenheitToCelc():
 fahr = int(input())
 celc = (fahr - 30)/2
 print("Celsius is " + str(celc) + " degrees")
 
#fahrenheitToCelc()

def fizzbuzz():
 for fb in range(1,100):
  if(fb % 3 == 0):
   if(fb % 5 == 0):
    print("FizzBuzz")
   else:
    print("Fizz")
  else:
   if(fb % 5 == 0):
    print("Buzz")
   else:
    print(fb)
    
def betterfizzbuzz():
 string = ""
 for fb in range(1,100):
  if(fb % 3 == 0):
   string = string + "Fizz"
  if(fb % 5 == 0):
   string = string + "Buzz"
  if(fb % 3 != 0 and fb % 5 != 0):
   string = str(fb)
  print(string)
  string = ""
    
betterfizzbuzz()

 


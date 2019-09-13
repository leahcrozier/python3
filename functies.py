
print("=========================1===========================")
def helloworld():
    for i in range(10):
        print("Hello World!");

helloworld()

print("=========================2===========================")

def tafelvanvijf():
    print(str(1*5))
    print(str(2*5))
    print(str(3*5))
    print(str(4*5))
    print(str(5*5))
    print(str(6*5))



tafelvanvijf()

print("=========================3===========================")

def helloworldagain(x):
    for i in range(x):
        print("Hello again, world!")
  
helloworldagain(4)

print("=========================4============================")

def yeehaw():
    zt = int(input("vul een getal in: "))
    for i in range(zt):
        print("yeehaw")

yeehaw()
  
print("=========================5============================")

def kerstboom(x):
    for i in range(len(x)):
            l = slice (i+1)
            print(x[l])


kerstboom("merry christmas")
     
print("=========================6============================")

def max_van_3(x,y,z):
    print (max(x,y,z))

max_van_3(6,9,0)

print("=========================7============================")

def reverse_string(x):
    x = x[::-1]
    print(x)


reverse_string("ok, this is epic.")

print("=========================8============================")
    
def is_priemgetal(x):
    if x >1:
        for i in range(2,x):
            if (x % i) == 0:
                print ("False")
                break
            else:
                print("True")
                break

    else:
        print("False")
        
    
is_priemgetal(3)

print("=========================9============================")

def is_palindrome(x):
    L = x[::-1]
    if x == L:
        print("True")

    else:
        print("False")
    
is_palindrome("racecar")

print("=========================10============================")

def reverse(x):
    x = x[::-1]
    print(x)

reverse([2,4,5,6])

print("=========================11============================")




    
    
    
    

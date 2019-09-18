
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

def yeehaw(x):
    for i in range(x):
        print("yeehaw")

yeehaw(3)
  
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
    return x

print(reverse([2,4,5,6]))

print("=========================11============================")

def length(x):
    z = len(x)
    print(z)


length([2,6,8,9,4,6])
    
print("=========================12============================")    
def addthing(array, string):
    array.append(string)
    return array

print (addthing( ["a","potato","flew","around","my", "room"], "before"))
    
print("=========================13============================")
def secondthing(array, string):
     array.insert(1, string)
     return array

print (secondthing( ["you're","good","duck",", ","you're", "just","like","your","father"] ,"no"))
     
print("=========================14============================")

def deletething(array):
    array.remove("the")
    return array

print(deletething( ["somebody","once","told","me","the"]))

print("=========================14============================")

def yeetusdeletus(array, string):
    if string in array:
        array.remove(string)
        return array
    else:
        return array

print(yeetusdeletus( ["it's", "epic", "gamer", "time", "!"] , "!"))

print("=========================15============================")

def createdict(n):
    dict = {}
    for i in range(n):
        dict[i+1] = (i+1)*(i+1)
    return dict

print(createdict(5))

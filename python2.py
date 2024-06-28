def greet(name):
    print(f'hello,{name}')
greet('binu')

# function
def addition(a, b):
    sum = a+b
    print(f'the sum is {sum}')
    print('the sum is:',sum)
addition(2,3)

# return
def add_numbers(num1,num2):
    return num1+num2

result=add_numbers(5,7)
print('the sum is:', result)

# lambda
add = lambda a,b : a+b
multiply = lambda x, y : x*y 

print(add(3,4))
print(multiply(1,2))

def test(*args):
    print(args)
test(1,2,3)

def lis(num): 
    for i in num: 
        print(i)

lis([1,2,4])
lis((1,2,3))

def cube(num):
    for i in num: 
        result= i**3
        print(f'cube of {i} is {result}')
cube([1,2,3,4,5,6])

# oop
class calculation:
    def add(self,a,b):
        return a+b
    def sub(self,a,b):
        return a-b 
    def mul(self,a,b):
        return a*b
    
calculator= calculation()
result2=calculator.add(2,3)
result3=calculator.sub(9,5)
result4=calculator.mul(5,7)
print(result2)
print(result3)
print(result4)

class meth:
    def cube(self,num):
        for i in num: 
            result= i**3
            print(f'cube of {i} is {result}')
    def lis(self,num): 
        for i in num: 
            print(i)

meth1=meth()
out1=meth1.cube([1,2,4])
out2=meth1.lis([1,2,3,4,5])
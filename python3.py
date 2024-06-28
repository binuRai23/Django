#  ( __name = name ) private attribute 
# 1
class animal: 
    def __init__(self,name):
        print('constructor is invoked')
        self.name = name 
    def eat(self): 
        # print(self.name)
        print("i can eat")
    def sleep(self):
        print("i can sleep")

# inheritance
class Dog(animal): 
    def bark(self):
        print('i can bark')

dog1 = Dog("saint bernard")
print(dog1.name)
dog1.eat()
dog1.sleep()

# 2
# _name = name (protected)
class BankAccount: 
    def __init__(self,account_number,balance) : 
        self._account_number = account_number
        self._balance = balance 
        
    def deposit(self,amount):
        self._balance += amount
        print(f'deposit successful.New balance: ${self._balance}')
    
    def check_balance(self):
        print(f'current balance: {self._balance}')
    
    def withdraw(self,amount):
        self._balance -=amount 
        print(f'withdraw successful. New balance : ${self._balance}')
    
account = BankAccount('1234', 20000)
account.deposit(200)
account.withdraw(50)
account.check_balance()

print(account._account_number)

# 3
class employee:
    def __init__(self,name,emp_id,salary):
        self._name = name 
        self._emp_id = emp_id
        self._salary = salary
        
    def calculate_bonus(self):
        return self._salary * 0.1 
    
    def display_info(self):
        print(f'name: {self._name}')
        print(f'Employee id : {self._emp_id}')
        print (f'salary : {self._salary}')
        
        
employee1 = employee('bob',1, 1000)
employee1.display_info()
bonus = employee1.calculate_bonus()

print(bonus)

# 4
class Father:
    def __init__(self, child):
        # print('constructor')
        self.child = child 
    def talk(self):
        print('i can talk')

class Ram(Father):
    def walk(self):
        print('i can walk')

class Hari(Father):
    def eat(self):
        print('i can eat')


child1 = Ram("Ram")
print(child1.child)
child1.talk()

child2 = Hari("Hari")
print(child2.child)
child2.talk()

# 5
class Employee:
    def __init__(self,name,emp_id):
        self._name = name 
        self._emp_id = emp_id
    
    def display_info(self):
        print(f'name: {self._name}')
        print(f'Employee id : {self._emp_id}')
        
class Manager(Employee):
    def __init__(self,name, emp_id,department):
        super().__init__(name,emp_id)
        self.department = department
        
    def display_info(self):
        super().display_info()
        print(f'department: {self.department}')

class Developer(Employee):
    def __init__(self,name,emp_id,programming_lang):
        super().__init__(name, emp_id)
        self.programming_lang = programming_lang
        
    def display_info(self):
        super().display_info()
        print(f'programming language: {self.programming_lang}')
        
        
manager = Manager('Bob',1, 'engineering')
manager.display_info()

developer = Developer('pranjal',2, 'html')
developer.display_info()

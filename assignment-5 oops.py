#!/usr/bin/env python
# coding: utf-8

# In[4]:


class point:
    def __init__(self,x,y,z):
        self.x=x
        self.y=y
        self.z=z
    def sqsum(self):
        a=self.x*self.x
        b=self.y*self.y
        c=self.z*self.z
        return a+b+c
output=point(1,3,5)


# In[5]:


class Calculator:
    def __init__(self,num1,num2):
        self.num1=float(num1)
        self.num2=float(num2)
    def add(self):
        self.num1+self.num2
        return self.num1+self.num2
    def subtract(self):
        self.num2-self.num1
        return self.num2-self.num1
    def multiply(self):
        self.num1*self.num2
        return self.num1*self.num2
    def divide(self):
        self.num2/self.num1
        return self.num2/self.num1
obj =Calculator(10, 94)
obj.add()


# In[6]:


class student:
    def __init__(self):
        self.name=None
        self.rollnumber=None
    def setName(self,newname):
        self.name=newname
    def getName(self):
        return self.name
    def setRollNumber(self,newnumber):
        if newnumber>0:
            self.rollnumber=newnumber
        else:
            return 'Enter valid rollnumber'
    def getRollNumber(self):
        return self.rollnumber


# In[7]:


obj=student()
obj.setName('Edyoda')
print(obj.getName())
obj.setRollNumber(240623)
print(obj.getRollNumber())


# In[8]:


class account:
    def __init__(self, title=None, balance=0):
        self.title = title
        self.balance = balance
    def print_detail(self):
        return self.title,self.balance

class SavingsAccount(account):
    def __init__(self, title, balance, interestRate):
        super().__init__(title, balance)
        self.interestRate = interestRate
    def print_detail(self):
        return self.title,self.balance,self.interestRate


# In[9]:


obj1=account("Ashish",5000)
obj1.print_detail()
obj2=SavingsAccount('Ashish',5000,5)
obj2.print_detail()


# In[10]:


class Account:
    def __init__(self,title="none",balance=0):
        self.title=title
        self.balance=balance
    def getBalance(self,balance):
        self.balance=balance
    def deposit(self,amount):
        self.balance=amount+self.balance
    def withdrawal(self,amount):
        self.balance=self.balance-amount
class SavingsAccount(Account):
    def __init__(self,title=None,balance=0,interestRate=0):
        super().__init__(title,balance)
        self.interestRate = interestRate
    def interestAmount(self):
        self.interestAmount=(self.interestRate*self.balance)/100
obj2=Account("Ashish",5000)
obj1=SavingsAccount("Ashish",5000,5)


# In[11]:


obj1.interestAmount()


# In[12]:


obj1.interestAmount


# In[ ]:





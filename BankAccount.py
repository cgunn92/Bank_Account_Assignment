import sys
import math
import datetime as dt

class Customer():
    def __init__(self, name, cellPhone="", addLine1="", addLine2=None, city="", prov="", postCode="", acct=None, workPhone=None, homePhone=None):
        self._name = self.set_name(name)[1]
        self._acct = self.set_acct(acct)[1]
        self._workPhone = self.set_workPhone(workPhone)[1]
        self._homePhone = self.set_homePhone(homePhone)[1]
        self._cellPhone = self.set_cellPhone(cellPhone)[1]
        self._addLine1 = self.set_addLine1(addLine1)[1]
        self._addLine2 = self.set_addLine2(addLine2)[1]
        self._city = self.set_city(city)[1]
        self._prov = self.set_prov(prov)[1]
        self._postCode = self.set_postCode(postCode)[1]

    def get_name(self):
        return self._name

    def set_name(self, name):
        if len(name) == 0:
            sys.stderr.write("Must have at least one character in name")
            return False
        self._name = name
        return True, self._name

    def get_acct(self):
        return self._acct

    def set_acct(self, acct):
        if acct == None:
            return True
        elif len(acct) == 0:
            sys.stderr.write('Must enter a valid account number')
            return False
        self._acct = acct
        return True, self._acct
        
    def get_cellPhone(self):
        return self._cellPhone
    
    def set_cellPhone(self, cellPhone):
        if not cellPhone:
            sys.stderr.write("Must have a 10 digit cell phone number")
            return False
        if not (len(cellPhone) == 10):
            sys.stderr.write("Must have a 10 digit phone number")
            return False
        self._cellPhone = cellPhone
        return True, self._cellPhone

    def get_workPhone(self):
        return self._workphone

    def set_workPhone(self, workPhone):
        if workPhone == None:
            return True, None
        elif (len(workPhone) != 10):
            sys.stderr.write("Must have a 10 digit phone number")
            return False
        self._workPhone = workPhone
        return True, self._workPhone

    def get_homePhone(self):
        return self._homePhone

    def set_homePhone(self, homePhone):
        if homePhone == None:
            return True, None
        elif not (len(homePhone) == 10):
            sys.stderr.write("Must have a 10 digit phone number")
            return False
        self._homePhone = homePhone
        return True, self._homePhone

    def get_addLine1(self):
        return self._addLine1

    def set_addLine1(self, addLine1):
        if not addLine1:
            sys.stderr.write("Must enter an address")
            return False
        elif len(addLine1) == 0:
            sys.stderr.write("Must enter a valid address")
            return False
        self._addLine1 = addLine1
        return True, self._addLine1

    def get_addLine2(self):
        return self._addLine2

    def set_addLine2(self, addLine2):
        if addLine2 == None:
            return True, None
        elif len(addLine2) == 0:
            sys.stderr.write("Please enter a valid line 2 address ")
        self._addLine2 = addLine2
        return True, self._addLine2

    def get_city(self):
        return self._city

    def set_city(self, city):
        if not city:
            sys.stderr.write("Must enter a city")
            return False
        elif len(city) == 0:
            sys.stderr.write("Must enter a valid city")
            return False
        self._city = city
        return True, self._city

    def get_prov(self):
        return self._prov

    def set_prov(self, prov):
        if not prov:
            sys.stderr.write("Must enter a province")
            return False
        elif len(prov) == 0:
            sys.stderr.write("Must enter a valid province")
            return False
        self._prov = prov
        return True, self._prov

    def get_postCode(self):
        return self._postCode

    def set_postCode(self, postCode):
        if not postCode:
            sys.stderr.write('Must enter a postal code')
            return False
        if (len(postCode) < 6) or (len(postCode) > 7):
            sys.stderr.write("Must enter a valid postal code")
            return False
        self._postCode = postCode
        return True, self._postCode

class Account():
    def __init__(self, balance, status, acctNum='1', branchNum='1', subAccts=[]):
        self._acctNum = self.set_acctNum(acctNum)[1]
        self._branchNum = branchNum
        self._status = self.set_status(status)[1]
        self._dateOpened = dt.datetime.today()
        self._subAccts = subAccts
        self._balance = balance

    def get_acctNum(self):          #Account number setter is ommitted because it should not change
        return self._acctNum
    
    def set_acctNum(self, acctNum):
        if len(acctNum) != "1":
            sys.stderr.write("Enter a valid acct number")
            return False
        elif 
        

    @property
    def branchNum(self):
        return self._branchNum

    @branchNum.setter
    def branchNum(self, branchNum):
        self._branchNum = branchNum

    def get_status(self):
        return self._status

    def set_status(self, status):
        self._status = status

    def get_dateOpened(self):    #I chose to omit a setter function for dateOpened
        return self._dateOpened  #because that is immutable

    def get_subAccts(self):
        return self._subAccts

    def set_subAccts(self):
        self._subAccts = SubAccount()

class SubAccount():
    def __init__(self):
        pass
    
    
newC = Customer("Caleb", "1234567890", "1234", None, "Carlton", "Oregon", "v2r 5c7", "1", None, None)
print(newC.get_name())

newA = Account(32, "open", '1', '1', [])
print(newA._status)
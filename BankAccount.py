import sys
import math
import datetime as dt

class Customer():
    def __init__(self, name, cellPhone="", addLine1="", addLine2=None, city="", prov="", postCode="", acct=None, workPhone=None, homePhone=None):
        self.name = name
        self.acct = acct
        self.workphone = workPhone
        self.homePhone = homePhone
        self.cellPhone = cellPhone
        self.addLine1 = addLine1
        self.addLine2 = addLine2
        self.city = city
        self.prov = prov
        self.postCode = postCode

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        if len(name) == 0:
            sys.stderr.write("Must have at least one character in name")
            return False
        self._name = name
        return True

    @property
    def acct(self):
        return self._acct
    
    @acct.setter
    def acct(self, acct):
        if acct == None:
            return True
        elif len(acct) == 0:
            sys.stderr.write('Must enter a valid account number')
            return False
        self._acct = acct
        return True
        
    @property
    def cellPhone(self):
        return self._cellPhone

    @cellPhone.setter
    def cellPhone(self, cellPhone):
        if not cellPhone:
            sys.stderr.write("Must have a 10 digit cell phone number")
            return False
        if not (len(cellPhone) == 10):
            sys.stderr.write("Must have a 10 digit phone number")
            return False
        self._cellPhone = cellPhone
        return True

    def get_workPhone(self):
        return self._workphone

    def set_workPhone(self, workPhone):
        if not (len(workPhone) == 10):
            sys.stderr.write("Must have a 10 digit phone number")
            return False
        self._workphone = workPhone
        return True

    def get_homePhone(self):
        return self._homePhone

    def set_homePhone(self, homePhone):
        if not (len(homePhone) == 10):
            sys.stderr.write("Must have a 10 digit phone number")
            return False
        self._homePhone = homePhone
        return True

    @property
    def addLine1(self):
        return self._addLine1

    @addLine1.setter
    def addLine1(self, addLine1):
        if not addLine1:
            sys.stderr.write("Must enter an address")
            return False
        elif len(addLine1) == 0:
            sys.stderr.write("Must enter a valid address")
            return False
        self._addLine1 = addLine1
        print(True, file=sys.stderr)

    def get_addLine2(self):
        return self._addLine2

    def set_addLine2(self, addLine2):
        self._addLine2 = addLine2

    @property
    def city(self):
        return self._city

    @city.setter
    def city(self, city):
        if not city:
            sys.stderr.write("Must enter a city")
            return False
        elif len(city) == 0:
            sys.stderr.write("Must enter a valid city")
            return False
        self._city = city
        return True

    @property
    def prov(self):
        return self._prov

    @prov.setter
    def prov(self, prov):
        if not prov:
            sys.stderr.write("Must enter a province")
            return False
        elif len(prov) == 0:
            sys.stderr.write("Must enter a valid province")
            return False
        self._prov = prov
        return True

    @property
    def postCode(self):
        return self._postCode

    @postCode.setter
    def postCode(self, postCode):
        if not postCode:
            sys.stderr.write('Must enter a postal code')
            return False
        if (len(postCode) < 6) or (len(postCode) > 7):
            sys.stderr.write("Must enter a valid postal code")
            return False
        self._postCode = postCode
        return True

class Account():
    def __init__(self, acctNum='1', branchNum='1', status='open', dateOpened=dt.datetime.today(), subAccts=[]):
        self.acctNum = acctNum
        self.branchNum = branchNum
        self.status = status
        self.dateOpened = dt.datetime.today()
        self.subAccts = subAccts

    @property
    def acctNum(self):          #Account number setter is ommitted because it should not change
        return self._acctNum
    
    @acctNum.setter
    def acctNum(self, acctNum):
        if len(acctNum) != "1":
            sys.stderr.write("Enter a valid acct number")
        

    @property
    def branchNum(self):
        return self._branchNum

    @branchNum.setter
    def branchNum(self, branchNum):
        self._branchNum = branchNum

    @property
    def status(self):
        return self._status

    @status.setter
    def status(self, status):
        self._status = status

    def get_dateOpened(self):    #I chose to omit a setter function for dateOpened
        return self._dateOpened  #because that is immutable

    def get_subAccts(self):
        return self._subAccts

    def set_subAccts(self, SubAccount):
        self._subAccts = SubAccount()

class SubAccount():
    def __init__(self):
        pass


# Customer("", "1234567890", "", None, "", "", "123456", None, None, None)

newAccount = Account("1", '1', 'open', '', [])

print(newAccount.branchNum)

newAccount.branchNum('2')

print(newAccount.branchNum)
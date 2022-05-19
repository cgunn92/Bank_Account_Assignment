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
            print(False, file=sys.stderr)
            raise Exception("Must have at least one character in name")
        self._name = name
        print(True, file=sys.stderr)

    @property
    def acct(self):
        return self._acct
    
    @acct.setter
    def acct(self, acct):
        self._acct = acct
        
    @property
    def cellPhone(self):
        return self._cellPhone

    @cellPhone.setter
    def cellPhone(self, cellPhone):
        if not cellPhone: raise Exception("Must have a 10 digit cell phone number")
        if not (len(cellPhone) == 10): raise Exception("Must have a 10 digit phone number")
        self._cellPhone = cellPhone

    def get_workPhone(self):
        return self._workphone

    def set_workPhone(self, workPhone):
        if not (len(workPhone) == 10): raise Exception("Must have a 10 digit phone number")
        self._workphone = workPhone

    def get_homePhone(self):
        return self._homePhone

    def set_homePhone(self, homePhone):
        if not (len(homePhone) == 10): raise Exception("Must have a 10 digit phone number")
        self._homePhone = homePhone

    @property
    def addLine1(self):
        return self._addLine1

    @addLine1.setter
    def addLine1(self, addLine1):
        if not addLine1:
            print(False, file=sys.stderr)
            raise Exception("Must enter an address")
        elif len(addLine1) == 0:
            print(False, file=sys.stderr)
            raise Exception("Must enter a valid address")
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
            print(False, file=sys.stderr)
            raise Exception("Must enter a city")
        elif len(city) == 0:
            print(False, file=sys.stderr)
            raise Exception("Must enter a valid city")
        self._city = city
        print(True, file=sys.stderr)

    @property
    def prov(self):
        return self._prov

    @prov.setter
    def prov(self, prov):
        if not prov:
            print(False, file=sys.stderr)
            raise Exception("Must enter a province")
        elif len(prov) == 0:
            print(False, file=sys.stderr)
            raise Exception("Must enter a valid province")
        self._prov = prov

    @property
    def postCode(self):
        return self._postCode

    @postCode.setter
    def postCode(self, postCode):
        if not postCode:
            print(False, file=sys.stderr)
            raise Exception("Must enter a postal code")
        if (len(postCode) < 6) or (len(postCode) > 7):
            print(False, file=sys.stderr)
            raise Exception("Must enter a valid postal code")
        self._postCode = postCode
        print(True, file=sys.stderr)

class Account():
    def __init__(self, acctNum='1', branchNum='1', status='open', dateOpened=dt.datetime.today(), subAccts=[]):
        self.acctNum = acctNum
        self.branchNum = branchNum
        self.status = status
        self.dateOpened = dateOpened
        self.subAccts = subAccts

    @property
    def acctNum(self):
        return self._acctNum

    @acctNum.setter
    def acctNum(self, acctNum):
        self._acctNum = acctNum

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


Customer("", "1234567890", "", None, "", "", "123456", None, None, None)
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
        if not (len(cellPhone) == 10): raise Exception("Must have a 10 digit cell phone number")
        self._cellPhone = cellPhone

    def get_workPhone(self):
        return self._workphone

    def set_workPhone(self, workPhone):
        self._workphone = workPhone

    def get_homePhone(self):
        return self._homePhone

    def set_homePhone(self, homePhone):
        self._homePhone = homePhone

    @property
    def addLine1(self):
        return self._addLine1

    @addLine1.setter
    def addLine1(self, addLine1):
        self._addLine1 = addLine1

    def get_addLine2(self):
        return self._addLine2

    def set_addLine2(self, addLine2):
        self._addLine2 = addLine2

    @property
    def city(self):
        return self._city

    @city.setter
    def city(self, city):
        self._city = city

    @property
    def prov(self):
        return self._prov

    @prov.setter
    def prov(self, prov):
        self._prov = prov

    @property
    def postCode(self):
        return self._postCode

    @postCode.setter
    def postCode(self, postCode):
        if not postCode: raise Exception("Must enter a postal code")
        if (len(postCode) < 6) or (len(postCode) > 7): raise Exception("Must enter a valid postal code")
        self._postCode = postCode

class Account():
    def __init__(self, acctNum, branchNum, status='open', dateOpened=dt.datetime.today(), subAccts=[]):
        self._acctNum = acctNum
        self._branchNum = branchNum
        self._status = status
        self._dateOpened = dateOpened
        self._subAccts = subAccts

    def get_acctNum(self):
        return self._acctNum

    def set_acctNum(self, acctNum):
        self._acctNum = acctNum

    def get_branchNum(self):
        return self._branchNum

    def set_branchNum(self, branchNum):
        self._branchNum = branchNum

    def get_status(self):
        return self._status

    def set_status(self, status):
        self._status = status

    def get_dateOpened(self):
        return self._dateOpened

    def set_dateOpened(self, dateOpened):
        self._dateOpened = dateOpened

    def get_subAccts(self):
        return self._subAccts

    def set_subAccts(self, subAccts):
        self._subAccts = subAccts

class SubAccount():
    pass


Customer("", "1234567890", "", None, "", "", "123456", None, None, None)
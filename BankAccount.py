import math
import datetime as dt

class Customer():
    def __init__(self, name, cellPhone="", addLine1="", addLine2=None, city="", prov="", postCode="", acct=None, workPhone=None, homePhone=None):
        self._name = name
        self._acct = acct
        self._workphone = workPhone
        self._homePhone = homePhone
        self._cellPhone = cellPhone
        self._addLine1 = addLine1
        self._addLine2 = addLine2
        self._city = city
        self._prov = prov
        self._postCode = postCode

    def get_name(self):
        return self._name

    def set_name(self, name):
        self._name = name

    def get_cellPhone(self):
        return self._cellPhone

    def set_cellPhone(self, cellPhone):
        self._cellPhone = cellPhone

    def get_workPhone(self):
        return self._workphone

    def set_workPhone(self, workPhone):
        self._workphone = workPhone

    def get_homePhone(self):
        return self._homePhone

    def set_homePhone(self, homePhone):
        self._homePhone = homePhone

    def get_addLine1(self):
        return self._addLine1

    def set_addLine1(self, addLine1):
        self._addLine1 = addLine1

    def get_addLine2(self):
        return self._addLine2

    def set_addLine2(self, addLine2):
        self._addLine2 = addLine2

    def get_city(self):
        return self._city

    def set_city(self, city):
        self._city = city

    def get_province(self):
        return self._prov

    def set_province(self, prov):
        self._prov = prov

    def get_postCode(self):
        return self._postCode

    def set_postCode(self, postCode):
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


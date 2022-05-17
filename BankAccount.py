import math
import datetime as dt

class Customer():
    def __init__(self, name, cellPhone, addLine1="", addLine2=None, city="", prov="", postCode="", acct=None, workPhone=None, homePhone=None):
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


class Account():
    def __init__(self, acctNum, branchNum, status='open', dateOpened=dt.datetime.today(), subAccts=[]):
        self._acctNum = acctNum
        self._branchNum = branchNum
        self._status = status
        self._dateOpened = dateOpened
        self._subAccts = subAccts

class SubAccount():
    pass


print(dt.datetime.today())
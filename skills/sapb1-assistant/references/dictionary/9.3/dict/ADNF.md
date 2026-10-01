<!-- source: erpref.com (schema IP: SAP) | version: SAP Business One 9.3 | verified: 2026-10-01 -->
# ADNF - DNF Code
Module: Inventory and Production | 8 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: LogInstanc, AbsEntry
  NCM_DNF U: LogInstanc, DNFCode, NCMEntry
Fields (name type(len) description [values] ->parent table):
  AbsEntry Int(11) Internal Key
  NCMEntry Int(11) NCM Code ->ONCM
  DNFCode nVarChar(5) DNF Code
  DNFUoM nVarChar(10) DNF UoM
  DNFFactor Num(19,6) DNF Factor
  LogInstanc Int(11) Log Instance default=0
  UserSign2 Int(6) Updating User ->OUSR
  UpdateDate Date(8) Update Date

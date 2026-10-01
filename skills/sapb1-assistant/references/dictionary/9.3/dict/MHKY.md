<!-- source: erpref.com (schema IP: SAP) | version: SAP Business One 9.3 | verified: 2026-10-01 -->
# MHKY - MetaData Tables HKeys
Module: General | 11 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: RevCode, ResCode, HKeyIndex, TableName
Fields (name type(len) description [values] ->parent table):
  TableName nVarChar(5) Table Name
  HKeyIndex Int(6) HKey Index
  Name nVarChar(10) Key Name
  ViewOrder Int(6) View Order
  UniqueKey VarChar(1) Unique Key default=Y [Y=Yes, N=No]
  Ascend VarChar(1) Ascending default=Y [Y=Yes, N=No]
  UpdateDate Date(8) Update Date
  UpdateTime Int(11) Update Time default=0
  UsrSgnAttr Int(11) User Sign For Attribs Change default=-1
  ResCode Int(11) Resource Code from RSBD default=-1
  RevCode Int(11) Revision Code default=-1

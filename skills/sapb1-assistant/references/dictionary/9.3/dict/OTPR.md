<!-- source: erpref.com (schema IP: SAP) | version: SAP Business One 9.3 | verified: 2026-10-01 -->
# OTPR - Tax Return Values
Module: Administration | 7 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: AbsId
  CODE U: Code
Fields (name type(len) description [values] ->parent table):
  AbsId Int(11) Internal Number
  Code nVarChar(7) Return Value Code
  Descr nVarChar(30) Description
  Display VarChar(1) Display default=Y [Y=Yes, N=No]
  FieldID Int(11) Field ID in CUFD ->CUFD
  Locked VarChar(1) Locked default=N [Y=Yes, N=Changeable]
  DataType VarChar(1) Data Type default=S [T=Tax Amounts, S=Amounts, P=Prices, Q=Quantities, %=Percents, I=Integer, A=String, M=Measures]

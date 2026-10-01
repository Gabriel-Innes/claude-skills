<!-- source: erpref.com (schema IP: SAP) | version: SAP Business One 9.3 | verified: 2026-10-01 -->
# OTPA - Tax Parameter Attributes
Module: Administration | 6 columns
Indexes (name: columns; first = primary key; U = unique) - WARNING: multi-column key order here is reversed vs SAP's 10.0 reference (read as a set; see references/dictionary/INDEX.md):
  PRIMARY U: AbsId
  CODE U: Code
Fields (name type(len) description [values] ->parent table):
  AbsId Int(11) Internal Number
  Code nVarChar(8) Attribute Code
  Descr nVarChar(30) Description
  DataType VarChar(1) Data Type default=S [S=Amounts, P=Prices, Q=Quantities, %=Percents, I=Integer, A=String, M=Measures]
  FieldId Int(11) Field ID in CUFD ->CUFD
  Locked VarChar(1) Locked default=N [Y=Yes, N=Changeable]

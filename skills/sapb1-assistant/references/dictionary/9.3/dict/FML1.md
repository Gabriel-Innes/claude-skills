<!-- source: erpref.com (schema IP: SAP) | version: SAP Business One 9.3 | verified: 2026-10-01 -->
# FML1 - Tax Formula Parameter Declaration
Module: Administration | 7 columns
Indexes (name: columns; first = primary key; U = unique) - WARNING: multi-column key order here is reversed vs SAP's 10.0 reference (read as a set; see references/dictionary/INDEX.md):
  PRIMARY U: DispOrder, FmlId
Fields (name type(len) description [values] ->parent table):
  FmlId Int(11) Formula ID ->OFML
  DispOrder Int(11) Display Order
  VarName nVarChar(64) Variable Name
  Category VarChar(1) Category default=1 [1=Input, 2=Output, 3=In Out]
  Parameter Text(16) Parameter
  DataType VarChar(1) Data Type default=S [T=Tax Amounts, S=Amounts, P=Prices, Q=Quantities, %=Percents, I=Integer, A=String, B=Boolean, M=Measures, W=WTax]
  LogInstanc Int(11) Log Instance default=0

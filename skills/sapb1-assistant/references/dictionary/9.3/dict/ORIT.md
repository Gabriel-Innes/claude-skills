<!-- source: erpref.com (schema IP: SAP) | version: SAP Business One 9.3 | verified: 2026-10-01 -->
# ORIT - Dunning Interest Rate
Module: Administration | 5 columns | ObjType: 149
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: Code
Fields (name type(len) description [values] ->parent table):
  Code nVarChar(20) Interest Code
  Name nVarChar(50) Interest Name
  IncPartPay VarChar(1) Include Partially Paid Inv. default=Y [Y=Yes, N=No]
  DayInMonth Int(11) Number of Days in Month
  OrigRate VarChar(1) Use Original Exchange Rate default=Y [Y=Yes, N=No]

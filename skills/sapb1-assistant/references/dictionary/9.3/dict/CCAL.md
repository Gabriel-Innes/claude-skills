<!-- source: erpref.com (schema IP: SAP) | version: SAP Business One 9.3 | verified: 2026-10-01 -->
# CCAL - Chinese Chart of Account Level Definition
Module: Finance | 3 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: lvlIAccLe
Fields (name type(len) description [values] ->parent table):
  lvlIAccLe Int(6) Length First Level Accounts default=4 [4=]
  accLvlSet VarChar(1) Account Level Set default=N [N=, Y=]
  balIndSet VarChar(1) Balance Dir Indicator Set default=N [N=, Y=]

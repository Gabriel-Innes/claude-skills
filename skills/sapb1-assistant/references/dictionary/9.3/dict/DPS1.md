<!-- source: erpref.com (schema IP: SAP) | version: SAP Business One 9.3 | verified: 2026-10-01 -->
# DPS1 - Deposit - Rows
Module: Banking | 3 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: CheckKey, DepositId
Fields (name type(len) description [values] ->parent table):
  DepositId Int(11) Deposit Key ->ODPS
  CheckKey Int(11) Check Key
  DepCancel VarChar(1) Canceled default=N [Y=Yes, N=No]

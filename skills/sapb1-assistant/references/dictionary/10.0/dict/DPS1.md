<!-- source: REFDB.chm (SAP Business One SDK 10.0 - Database Tables Reference) | version: SAP Business One 10.0 | verified: 2026-10-01 -->
# DPS1 - Deposit - Rows
Module: Banking | 3 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: DepositId, CheckKey
Fields (name type(len) description [values] ->parent table):
  DepositId Int(11) Deposit Key ->ODPS
  CheckKey Int(11) Check Key
  DepCancel VarChar(1) Canceled default=N [Y=Yes, N=No]

<!-- source: erpref.com (schema IP: SAP) | version: SAP Business One 9.3 | verified: 2026-10-01 -->
# DPS1 - Deposit - Rows
Module: Banking | 3 columns
Indexes (name: columns; first = primary key; U = unique) - WARNING: multi-column key order here is reversed vs SAP's 10.0 reference (read as a set; see references/dictionary/INDEX.md):
  PRIMARY U: CheckKey, DepositId
Fields (name type(len) description [values] ->parent table):
  DepositId Int(11) Deposit Key ->ODPS
  CheckKey Int(11) Check Key
  DepCancel VarChar(1) Canceled default=N [Y=Yes, N=No]

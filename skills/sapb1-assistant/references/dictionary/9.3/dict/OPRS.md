<!-- source: erpref.com (schema IP: SAP) | version: SAP Business One 9.3 | verified: 2026-10-01 -->
# OPRS - Tax Payer Status
Module: Banking | 3 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: Code
Fields (name type(len) description [values] ->parent table):
  Code nVarChar(2) Code
  Descriptio nVarChar(254) Description
  Default VarChar(1) Default default=N [Y=Yes, N=No]

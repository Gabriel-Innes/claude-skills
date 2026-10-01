<!-- source: erpref.com (schema IP: SAP) | version: SAP Business One 9.3 | verified: 2026-10-01 -->
# OPFT - Portfolio Definitions
Module: Banking | 3 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: Code
Fields (name type(len) description [values] ->parent table):
  Code nVarChar(8) Code
  Name nVarChar(50) Name
  Type VarChar(1) Type default=C [C=Cheque, B=Bill of Exchange]

<!-- source: erpref.com (schema IP: SAP) | version: SAP Business One 9.3 | verified: 2026-10-01 -->
# PYD1 - Payment Terms Allowed in Payment Run
Module: Banking | 2 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: PYMCode, PYDCode
Fields (name type(len) description [values] ->parent table):
  PYDCode nVarChar(20) Payment Run Code ->OPYD
  PYMCode nVarChar(15) Payment Method ->OPYM

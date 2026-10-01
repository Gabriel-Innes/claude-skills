<!-- source: REFDB.chm (SAP Business One SDK 10.0 - Database Tables Reference) | version: SAP Business One 10.0 | verified: 2026-10-01 -->
# PYD1 - Payment Terms Allowed in Payment Run
Module: Banking | 2 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: PYDCode, PYMCode
Fields (name type(len) description [values] ->parent table):
  PYDCode nVarChar(20) Payment Run Code ->OPYD
  PYMCode nVarChar(15) Payment Method ->OPYM

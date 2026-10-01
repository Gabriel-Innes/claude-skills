<!-- source: erpref.com (schema IP: SAP) | version: SAP Business One 9.3 | verified: 2026-10-01 -->
# UDG2 - User Defaults - Credit Cards
Module: Administration | 3 columns
Indexes (name: columns; first = primary key; U = unique) - WARNING: multi-column key order here is reversed vs SAP's 10.0 reference (read as a set; see references/dictionary/INDEX.md):
  PRIMARY U: CreditCard, Code
Fields (name type(len) description [values] ->parent table):
  Code nVarChar(8) Code
  CreditCard Int(6) Credit Card Code ->OCRC
  AcctCode nVarChar(15) Credit Amount Code ->OACT

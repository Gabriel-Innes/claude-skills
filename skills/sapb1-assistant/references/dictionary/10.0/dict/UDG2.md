<!-- source: REFDB.chm (SAP Business One SDK 10.0 - Database Tables Reference) | version: SAP Business One 10.0 | verified: 2026-10-01 -->
# UDG2 - User Defaults - Credit Cards
Module: Administration | 3 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: Code, CreditCard
Fields (name type(len) description [values] ->parent table):
  Code nVarChar(8) Code
  CreditCard Int(6) Credit Card Code ->OCRC
  AcctCode nVarChar(15) Credit Amount Code ->OACT

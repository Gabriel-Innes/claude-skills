<!-- source: REFDB.chm (SAP Business One SDK 10.0 - Database Tables Reference) | version: SAP Business One 10.0 | verified: 2026-10-01 -->
# WHL3 - Register of VAT Payers - BPs Compared with OWHL
Module: General | 4 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: CardCode, NIP, BankAcc
Fields (name type(len) description [values] ->parent table):
  LastDate Date(8) Last Date
  CardCode nVarChar(15) BP Code
  NIP nVarChar(32) Federal Tax ID
  BankAcc nVarChar(50) Bank Account

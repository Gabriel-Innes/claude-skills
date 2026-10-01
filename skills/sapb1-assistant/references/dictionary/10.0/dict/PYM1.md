<!-- source: REFDB.chm (SAP Business One SDK 10.0 - Database Tables Reference) | version: SAP Business One 10.0 | verified: 2026-10-01 -->
# PYM1 - Currency Selection
Module: Banking | 4 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: PymCode, CurrCode
Fields (name type(len) description [values] ->parent table):
  PymCode nVarChar(15) Payment Method Code ->OPYM
  CurrCode nVarChar(3) Currency Code ->OCRN
  CurrName nVarChar(20) Currency Name
  Choose VarChar(1) Choose default=N [Y=Yes, N=No]

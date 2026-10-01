<!-- source: REFDB.chm (SAP Business One SDK 10.0 - Database Tables Reference) | version: SAP Business One 10.0 | verified: 2026-10-01 -->
# SVR1 - Saved Reconciliations - Transaction List
Module: Banking | 3 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: acctCode, transID, transLine
Fields (name type(len) description [values] ->parent table):
  acctCode nVarChar(15) Account Code
  transID Int(11) Transaction ID ->OJDT
  transLine Int(11) Transaction Row

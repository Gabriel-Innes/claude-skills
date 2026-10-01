<!-- source: erpref.com (schema IP: SAP) | version: SAP Business One 9.3 | verified: 2026-10-01 -->
# SVR1 - Saved Reconciliations - Transaction List
Module: Banking | 3 columns
Indexes (name: columns; first = primary key; U = unique) - WARNING: multi-column key order here is reversed vs SAP's 10.0 reference (read as a set; see references/dictionary/INDEX.md):
  PRIMARY U: transLine, transID, acctCode
Fields (name type(len) description [values] ->parent table):
  acctCode nVarChar(15) Account Code
  transID Int(11) Transaction ID ->OJDT
  transLine Int(11) Transaction Row

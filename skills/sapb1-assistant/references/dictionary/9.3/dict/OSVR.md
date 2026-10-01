<!-- source: erpref.com (schema IP: SAP) | version: SAP Business One 9.3 | verified: 2026-10-01 -->
# OSVR - Saved Reconciliations
Module: Banking | 6 columns | ObjType: 230
Indexes (name: columns; first = primary key; U = unique) - WARNING: multi-column key order here is reversed vs SAP's 10.0 reference (read as a set; see references/dictionary/INDEX.md):
  PRIMARY U: acctCode
Fields (name type(len) description [values] ->parent table):
  acctCode nVarChar(15) Account Code
  endBalanc Num(19,6) Bank Statement Ending Balance
  endDate Date(8) Bank Statement Ending Date
  statemntNo Int(11) Bank Statement Number
  userSign Int(6) Creating User ->OUSR
  createDate Date(8) Creation Date

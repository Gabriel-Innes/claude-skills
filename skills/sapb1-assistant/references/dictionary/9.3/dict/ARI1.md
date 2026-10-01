<!-- source: erpref.com (schema IP: SAP) | version: SAP Business One 9.3 | verified: 2026-10-01 -->
# ARI1 - Add-On
Module: Administration | 4 columns
Indexes (name: columns; first = primary key; U = unique) - WARNING: multi-column key order here is reversed vs SAP's 10.0 reference (read as a set; see references/dictionary/INDEX.md):
  PRIMARY U: AddOnID, USER_CODE
Fields (name type(len) description [values] ->parent table):
  USER_CODE nVarChar(25) User Code ->OUSR
  AddOnID Int(11) Add-On ID
  AddOnType VarChar(1) Add-On Type [M=Manual, C=Critical, A=Automatic, D=Disabled]
  EnableFlag VarChar(1) Add-On Enable Flag default=Y [Y=Yes, N=No]

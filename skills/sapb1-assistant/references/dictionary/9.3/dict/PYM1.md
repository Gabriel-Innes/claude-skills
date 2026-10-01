<!-- source: erpref.com (schema IP: SAP) | version: SAP Business One 9.3 | verified: 2026-10-01 -->
# PYM1 - Currency Selection
Module: Banking | 4 columns
Indexes (name: columns; first = primary key; U = unique) - WARNING: multi-column key order here is reversed vs SAP's 10.0 reference (read as a set; see references/dictionary/INDEX.md):
  PRIMARY U: CurrCode, PymCode
Fields (name type(len) description [values] ->parent table):
  PymCode nVarChar(15) Payment Method Code ->OPYM
  CurrCode nVarChar(3) Currency Code ->OCRN
  CurrName nVarChar(20) Currency Name
  Choose VarChar(1) Choose default=N [Y=Yes, N=No]

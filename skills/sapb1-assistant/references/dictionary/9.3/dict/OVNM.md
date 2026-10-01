<!-- source: erpref.com (schema IP: SAP) | version: SAP Business One 9.3 | verified: 2026-10-01 -->
# OVNM - VAT Report Numbering
Module: Administration | 7 columns
Indexes (name: columns; first = primary key; U = unique) - WARNING: multi-column key order here is reversed vs SAP's 10.0 reference (read as a set; see references/dictionary/INDEX.md):
  PRIMARY U: NumId
Fields (name type(len) description [values] ->parent table):
  NumId Int(11) Numbering ID
  NumName nVarChar(10) Numbering Name
  First nVarChar(9) First Number
  Next nVarChar(9) Next Number
  Last nVarChar(9) Last Number
  YrDepend VarChar(1) Year-Dependent default=N [Y=Year-Dependent, N=Year-Indepedent]
  DefaultNum VarChar(1) Default Numbering default=N [Y=Default Numbering, N=No Default Numbering]

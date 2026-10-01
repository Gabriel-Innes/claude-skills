<!-- source: erpref.com (schema IP: SAP) | version: SAP Business One 9.3 | verified: 2026-10-01 -->
# ONFM - Nota Fiscal Model
Module: Finance | 8 columns | ObjType: 540000056
Indexes (name: columns; first = primary key; U = unique) - WARNING: multi-column key order here is reversed vs SAP's 10.0 reference (read as a set; see references/dictionary/INDEX.md):
  PRIMARY U: AbsEntry
Fields (name type(len) description [values] ->parent table):
  AbsEntry nVarChar(6) NF Model ID
  NfmName nVarChar(20) NF Model Name
  NfmDescrip nVarChar(100) NF Model Description
  UserSign Int(6) User Signature - Create ->OUSR
  UserSign2 Int(6) Updating User ->OUSR
  UpdateDate Date(8) Date of Update
  NfmCode nVarChar(10) NF Model Code
  NfmTW VarChar(1) Tax Wizard Relevant default=Y [Y=Yes, N=No]

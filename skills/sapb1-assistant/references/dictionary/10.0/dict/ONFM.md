<!-- source: REFDB.chm (SAP Business One SDK 10.0 - Database Tables Reference) | version: SAP Business One 10.0 | verified: 2026-10-01 -->
# ONFM - Nota Fiscal Model
Module: Finance | 8 columns | ObjType: 540000056
Indexes (name: columns; first = primary key; U = unique):
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

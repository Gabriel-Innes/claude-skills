<!-- source: erpref.com (schema IP: SAP) | version: SAP Business One 9.3 | verified: 2026-10-01 -->
# OPJT - Project Plan
Module: Administration | 9 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: DocEntry
  NAME: TempName
Fields (name type(len) description [values] ->parent table):
  DocEntry Int(11) Internal Number
  TempType VarChar(1) Template Type default=N [S=System Template, N=Nonsystem Template]
  TempName nVarChar(254) Template Name
  LogInstanc Int(11) Log Instance
  UserSign Int(11) User Signature ->OUSR
  UserSign2 Int(11) Updating User ->OUSR
  CreateDate Date(8) Production Date
  UpdateDate Date(8) Date of Update
  TempDesc nVarChar(254) Template Description

<!-- source: REFDB.chm (SAP Business One SDK 10.0 - Database Tables Reference) | version: SAP Business One 10.0 | verified: 2026-10-01 -->
# ASUC - Single User Setup - History
Module: Administration | 8 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: StpCode, LogInstanc
Fields (name type(len) description [values] ->parent table):
  StpCode Int(6) Setup Code
  StpDes nVarChar(100) Setup Description
  Action VarChar(1) Action default=B [B=Block Update, W=Warning]
  LogInstanc Int(11) Log Instance default=0
  UpdateDate Date(8) Date of Update
  CreateDate Date(8) Creation Date
  UserSign Int(6) User Signature ->OUSR
  UserSign2 Int(6) Updating User ->OUSR

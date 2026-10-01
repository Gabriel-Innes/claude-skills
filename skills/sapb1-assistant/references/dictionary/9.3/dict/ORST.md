<!-- source: erpref.com (schema IP: SAP) | version: SAP Business One 9.3 | verified: 2026-10-01 -->
# ORST - Route Stages
Module: Administration | 9 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: AbsEntry
  SECONDARY U: Code
Fields (name type(len) description [values] ->parent table):
  AbsEntry Int(11) Internal Number
  Code nVarChar(50) Code
  Desc nVarChar(100) Description
  UserSign Int(6) User Signature
  UserSign2 Int(6) Updating User
  CreateDate Date(8) Creation Date
  CreateTime Int(6) Generation Time
  UpdateDate Date(8) Date of Update
  LogInstanc Int(11) Log Instance default=0

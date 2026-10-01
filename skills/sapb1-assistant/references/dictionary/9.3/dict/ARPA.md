<!-- source: erpref.com (schema IP: SAP) | version: SAP Business One 9.3 | verified: 2026-10-01 -->
# ARPA - Routing Permission Areas
Module: General | 7 columns
Indexes (name: columns; first = primary key; U = unique) - WARNING: multi-column key order here is reversed vs SAP's 10.0 reference (read as a set; see references/dictionary/INDEX.md):
  PRIMARY U: LogInstanc, AbsEntry
  SECONDARY U: LogInstanc, RPAreaCode
Fields (name type(len) description [values] ->parent table):
  AbsEntry Int(11) Routing Permission Area Internal Number
  RPAreaCode nVarChar(40) Routing Permission Area Code
  RPAreaDesc nVarChar(120) Routing Permission Area Description
  UserSign Int(6) User Signature
  UpdateDate Date(8) Date of Update
  UserSign2 Int(6) Updating User
  LogInstanc Int(11) Log Instance default=0

<!-- source: erpref.com (schema IP: SAP) | version: SAP Business One 9.3 | verified: 2026-10-01 -->
# ARPR - Routing Permissions
Module: General | 7 columns
Indexes (name: columns; first = primary key; U = unique) - WARNING: multi-column key order here is reversed vs SAP's 10.0 reference (read as a set; see references/dictionary/INDEX.md):
  PRIMARY U: LogInstanc, AbsEntry
  SECONDARY U: LogInstanc, RPAreaId, RStageId
Fields (name type(len) description [values] ->parent table):
  AbsEntry Int(11) Routing Permission Internal Number
  RStageId Int(11) Route Stage ID ->ORST
  RPAreaId Int(11) Routing Permission Area ID ->ORPA
  UserSign Int(6) User Signature
  UpdateDate Date(8) Date of Update
  UserSign2 Int(6) Updating User
  LogInstanc Int(11) Log Instance default=0

<!-- source: erpref.com (schema IP: SAP) | version: SAP Business One 9.3 | verified: 2026-10-01 -->
# ANCM - NCM Code
Module: Administration | 8 columns
Indexes (name: columns; first = primary key; U = unique) - WARNING: multi-column key order here is reversed vs SAP's 10.0 reference (read as a set; see references/dictionary/INDEX.md):
  PRIMARY U: LogInstanc, AbsEntry
  CODE U: LogInstanc, GroupCode, NcmCode
Fields (name type(len) description [values] ->parent table):
  AbsEntry Int(11) ID
  NcmCode nVarChar(15) NCM Code
  Descrip nVarChar(254) Description
  LogInstanc Int(11) Log Instance default=0
  UserSign2 Int(6) Updating User ->OUSR
  UpdateDate Date(8) Update Date
  GroupCode VarChar(1) Group Code default=0
  Group Int(6) NCM Group ->ONCG

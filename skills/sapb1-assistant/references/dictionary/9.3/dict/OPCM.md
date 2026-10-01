<!-- source: erpref.com (schema IP: SAP) | version: SAP Business One 9.3 | verified: 2026-10-01 -->
# OPCM - POS/Cash Register
Module: General | 7 columns
Indexes (name: columns; first = primary key; U = unique) - WARNING: multi-column key order here is reversed vs SAP's 10.0 reference (read as a set; see references/dictionary/INDEX.md):
  PRIMARY U: AbsEntry
  ID_CODE U: IdCode
  POC_CR U: CrCode, PosCode
Fields (name type(len) description [values] ->parent table):
  AbsEntry Int(11) Internal Number
  IdCode nVarChar(50) Identification Code
  PosCode nVarChar(6) Point of Service Code
  PosDesc nVarChar(100) Point of Service Description
  CrCode nVarChar(20) Cash Register Code
  CrDesc nVarChar(100) Cash Register Description
  Remarks nVarChar(250) Remarks

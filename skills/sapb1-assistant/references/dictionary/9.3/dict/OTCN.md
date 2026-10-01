<!-- source: erpref.com (schema IP: SAP) | version: SAP Business One 9.3 | verified: 2026-10-01 -->
# OTCN - Tracking Note
Module: General | 7 columns
Indexes (name: columns; first = primary key; U = unique) - WARNING: multi-column key order here is reversed vs SAP's 10.0 reference (read as a set; see references/dictionary/INDEX.md):
  PRIMARY U: AbsEntry
  CCD U: DirectImp, CCDNum
Fields (name type(len) description [values] ->parent table):
  AbsEntry Int(11) Abs. Entry
  CCDNum nVarChar(40) CCD Number
  Date Date(8) Date
  CustTerm nVarChar(15) Customs Terminal
  CntrOrigin nVarChar(3) Country of Origin
  DirectImp VarChar(1) Direct Import default=N [Y=Yes, N=No]
  CardCode nVarChar(15) BP Code

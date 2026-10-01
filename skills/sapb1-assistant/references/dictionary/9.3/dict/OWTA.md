<!-- source: erpref.com (schema IP: SAP) | version: SAP Business One 9.3 | verified: 2026-10-01 -->
# OWTA - Withholding Tax Accumulation
Module: Finance | 8 columns
Indexes (name: columns; first = primary key; U = unique) - WARNING: multi-column key order here is reversed vs SAP's 10.0 reference (read as a set; see references/dictionary/INDEX.md):
  PRIMARY U: AbsEntry
  SECONDARY U: BPLId, WTTypeId, PmntDate, CardCode
Fields (name type(len) description [values] ->parent table):
  AbsEntry Int(11) Internal Number
  CardCode nVarChar(15) BP Code ->OCRD
  PmntDate Date(8) Payment Date
  WTTypeId Int(11) WT Type Id
  AccmAmnt Num(19,6) WT Accumulated Amount
  AccmAmntFC Num(19,6) WT Accumulated Amount FC
  AccmAmntSC Num(19,6) WT Accumulated Amount SC
  BPLId Int(11) Branch default=0

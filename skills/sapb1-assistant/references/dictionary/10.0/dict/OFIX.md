<!-- source: REFDB.chm (SAP Business One SDK 10.0 - Database Tables Reference) | version: SAP Business One 10.0 | verified: 2026-10-01 -->
# OFIX - Fixed Asset Transactions
Module: Finance | 5 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: AbsEntry
  SECONDARY: SrcObjType, SrcObjAbs
Fields (name type(len) description [values] ->parent table):
  AbsEntry Int(11) Internal Number
  SrcObjType nVarChar(20) Source Object Type
  SrcObjAbs Int(11) Source Object Internal ID
  Canceled VarChar(1) Canceled default=N [Y=Yes, N=No]
  CancelDate Date(8) Cancellation Date

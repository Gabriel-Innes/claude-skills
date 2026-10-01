<!-- source: erpref.com (schema IP: SAP) | version: SAP Business One 9.3 | verified: 2026-10-01 -->
# OFIX - Fixed Asset Transactions
Module: Finance | 5 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: AbsEntry
  SECONDARY: SrcObjAbs, SrcObjType
Fields (name type(len) description [values] ->parent table):
  AbsEntry Int(11) Internal Number
  SrcObjType nVarChar(20) Source Object Type
  SrcObjAbs Int(11) Source Object Internal ID
  Canceled VarChar(1) Canceled default=N [Y=Yes, N=No]
  CancelDate Date(8) Cancellation Date

<!-- source: REFDB.chm (SAP Business One SDK 10.0 - Database Tables Reference) | version: SAP Business One 10.0 | verified: 2026-10-01 -->
# IVRU - Inventory Valuation Utility
Module: Inventory and Production | 18 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: AbsEntry
Fields (name type(len) description [values] ->parent table):
  AbsEntry Int(11) Successive No.
  SourceDB nVarChar(128) Source Database
  UtilityDB nVarChar(128) Utility DB
  IVLGEntry Int(11) IVLG Entry ->IVLG
  UpdDate Date(8) Update Date and Time
  TblHINM nVarChar(30) HINM Name
  TblHITM nVarChar(30) HITM Name
  TblHITW nVarChar(30) HITW Name
  TblFINM nVarChar(30) FINM Name
  TblFITM nVarChar(30) FITM Name
  TblFITW nVarChar(30) FITW Name
  TrSeqHINM Int(11) Last HINM Trans. Seq. No.
  TrSeqOINM Int(11) Last OINM Trans. Seq. No.
  TrIdUtil Int(11) Last OJDT Trans. No. Utility
  TrIdProd Int(11) Last OJDT Trans. No. Productiv
  Comment nVarChar(100) Comment
  StrFld nVarChar(50) General String Field
  NumFld Int(11) General Number Field

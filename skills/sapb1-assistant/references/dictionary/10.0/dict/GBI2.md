<!-- source: REFDB.chm (SAP Business One SDK 10.0 - Database Tables Reference) | version: SAP Business One 10.0 | verified: 2026-10-01 -->
# GBI2 - GBI Row 2 - G/L Account Master Records
Module: Finance | 10 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: HistoryId, RowId
Fields (name type(len) description [values] ->parent table):
  HistoryId Int(11) History Key ->OGBI
  RowId Int(11) Row Number
  AcctCode nVarChar(15) Account Code
  AcctName nVarChar(100) Account Name
  StrucLevel Int(11) Account Structure Level
  EvalSign VarChar(1) Evaluation Sign
  AddField nVarChar(60) Possible Additional Fields
  AcctType nVarChar(20) Account Type
  MesurUnit nVarChar(10) Measurement Unit
  BlDirect nVarChar(4) Direction of Balance

<!-- source: erpref.com (schema IP: SAP) | version: SAP Business One 9.3 | verified: 2026-10-01 -->
# GBI2 - GBI Row 2 - G/L Account Master Records
Module: Finance | 10 columns
Indexes (name: columns; first = primary key; U = unique) - WARNING: multi-column key order here is reversed vs SAP's 10.0 reference (read as a set; see references/dictionary/INDEX.md):
  PRIMARY U: RowId, HistoryId
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

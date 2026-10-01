<!-- source: erpref.com (schema IP: SAP) | version: SAP Business One 9.3 | verified: 2026-10-01 -->
# VLG1 - Validation of Recalc. From To
Module: Inventory and Production | 13 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: RecNum, AbsEntry
Fields (name type(len) description [values] ->parent table):
  AbsEntry Int(11) Internal Unique Key ->IVLG
  RecNum Int(11) Record Number
  FromSysDat Date(8) From System Date
  FromDocNum Int(11) From Document Number
  FromDocTyp Int(6) From Document Type
  ToSysDate Date(8) To System Date
  ToDocNum Int(11) To Document Number
  ToDocType Int(6) To Document Type
  CalRecOINM Int(11) Calculated Record in OINM
  LastCalcTS Int(11) Last Calculated Trans. Seq.
  SumTranVal Num(19,6) Sum of Transaction Value
  StrFld nVarChar(50) General String Field
  NumFld Int(11) General Number Field

<!-- source: erpref.com (schema IP: SAP) | version: SAP Business One 9.3 | verified: 2026-10-01 -->
# TRN1 - Subtable of OTRN
Module: Administration | 8 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: LineNum, TrnAbsEntr
  UniqueIdx U: LineNum, ItemCode, ItemType, TrnAbsEntr
Fields (name type(len) description [values] ->parent table):
  TrnAbsEntr Int(11) OTRN Abs Entry
  LineNum Int(11) Line Number of Table
  ItemCode nVarChar(254) Item Code
  ItemType nVarChar(8) Item Type
  SlimType nVarChar(8) Slim Type
  MaxLength Int(11) Max. Length
  SourceText Text(16) Source Text
  Memo Text(16) Memo

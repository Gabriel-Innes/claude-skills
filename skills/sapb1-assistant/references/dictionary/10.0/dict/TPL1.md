<!-- source: REFDB.chm (SAP Business One SDK 10.0 - Database Tables Reference) | version: SAP Business One 10.0 | verified: 2026-10-01 -->
# TPL1 - Template - Records
Module: Administration | 5 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: TplNum, LineNum
Fields (name type(len) description [values] ->parent table):
  TplNum Int(11) Template Code ->OTPL
  LineNum Int(11) Line No.
  FieldPos Int(11) Field Pos.
  SrcArrType Int(11) Source Array Type default=1 [-1=None, 1=Main, 12=Array 1, 13=Array 2, 14=Array 3, 15=Array 4, 16=Array 5, 17=Array 6, 18=Array 7, 19=Array 8, 20=Array 9, 21=Array 10, 22=Array 11]
  SrcObjType Int(11) Source Object Type default=-1

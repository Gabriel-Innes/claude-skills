<!-- source: REFDB.chm (SAP Business One SDK 10.0 - Database Tables Reference) | version: SAP Business One 10.0 | verified: 2026-10-01 -->
# TXD2 - Tax Invoice Draft Operation Codes
Module: Marketing Documents | 5 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: BaseEntry, LineNum, OpCode
Fields (name type(len) description [values] ->parent table):
  BaseEntry Int(11) Abs. Entry ->OTSI
  LineNum Int(11) Base Doc. Abs. Entry ->TSI1
  OpCode Int(11) Operation Code ->OBSI
  ObjType Int(11) Object Type ->ADP1
  LogInstanc Int(11) Log Instance default=0

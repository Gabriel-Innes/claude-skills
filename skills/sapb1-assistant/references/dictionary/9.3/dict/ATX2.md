<!-- source: erpref.com (schema IP: SAP) | version: SAP Business One 9.3 | verified: 2026-10-01 -->
# ATX2 - Tax Invoice Operation Codes
Module: Marketing Documents | 5 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: ObjType, LogInstanc, OpCode, LineNum, BaseEntry
Fields (name type(len) description [values] ->parent table):
  BaseEntry Int(11) Abs. Entry ->OTSI
  LineNum Int(11) Base Doc. Abs. Entry ->TSI1
  OpCode Int(11) Operation Code ->OBSI
  ObjType Int(11) Object Type ->ADP1
  LogInstanc Int(11) Log Instance default=0

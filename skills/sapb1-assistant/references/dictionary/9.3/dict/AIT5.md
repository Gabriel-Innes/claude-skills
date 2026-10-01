<!-- source: erpref.com (schema IP: SAP) | version: SAP Business One 9.3 | verified: 2026-10-01 -->
# AIT5 - Asset Item Projects - History
Module: Inventory and Production | 7 columns
Indexes (name: columns; first = primary key; U = unique) - WARNING: multi-column key order here is reversed vs SAP's 10.0 reference (read as a set; see references/dictionary/INDEX.md):
  PRIMARY U: LogInstanc, LineNum, ItemCode
Fields (name type(len) description [values] ->parent table):
  ItemCode nVarChar(50) Item No. ->OITM
  LineNum Int(11) Line Number
  ValidFrom Date(8) Valid From
  ValidTo Date(8) Valid To
  Project nVarChar(20) Project ->OPRJ
  LogInstanc Int(11) Log Instance default=0
  ObjType nVarChar(20) Object default=4 ->ADP1

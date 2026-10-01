<!-- source: erpref.com (schema IP: SAP) | version: SAP Business One 9.3 | verified: 2026-10-01 -->
# LIVI - IVI Log File
Module: Inventory and Production | 9 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: LogEntry
Fields (name type(len) description [values] ->parent table):
  LogEntry Int(11) Internal Number
  Version Int(11) B1 Main Version
  PatchLevel nVarChar(50) B1 PL Version
  Comment nVarChar(100) Recalculation Comment
  LoadCustom VarChar(1) Load customs from OIPF default=Y [N=No, Y=Yes]
  LastMsgID Int(11) Last OILM Message ID
  UpdateDate Date(8) Date of Update
  InitMap VarChar(1) Initialize MAP Items
  InitStd VarChar(1) Initialize STD Items

<!-- source: erpref.com (schema IP: SAP) | version: SAP Business One 9.3 | verified: 2026-10-01 -->
# CIVI - IVI Config File
Module: Inventory and Production | 16 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: AbsEntry
Fields (name type(len) description [values] ->parent table):
  AbsEntry Int(11) Internal Number
  EnableRun VarChar(1) Enable Run default=N [Y=Yes, N=No]
  EnblRunDt Date(8) Enable Run Date
  MsgSource Int(11) Object ID of Message Source
  IsOILMUpd VarChar(1) Is OILM Updated default=N [N=No, Y=Yes]
  EnblDays Int(11) Enable Valid In Days default=30
  LstChkMsg Int(11) Last Checked OILM Message
  LstMsgDate Date(8) Last Build Message Date
  LstHndlMsg Int(11) Last Handled OILM Message
  EnableUpd VarChar(1) Enable Update default=Y [Y=Yes, N=No]
  IgnPreUpd VarChar(1) Ignore Previous Update default=N [Y=Yes, N=No]
  ForceRSP VarChar(1) Force RSP Precheck default=N [Y=Yes, N=No]
  ReorderFrm Date(8) Reorder 8.8 Messages: From Date
  ReorderTo Date(8) Reorder 8.8 Messages: To Date
  InitMap VarChar(1) Initialize MAP Items
  InitStd VarChar(1) Initialize STD Items

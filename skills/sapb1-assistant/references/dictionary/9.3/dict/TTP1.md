<!-- source: erpref.com (schema IP: SAP) | version: SAP Business One 9.3 | verified: 2026-10-01 -->
# TTP1 - ToolTip Preview - Rows
Module: General | 5 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: DataKey, ObjectId, UserSign
Fields (name type(len) description [values] ->parent table):
  UserSign Int(6) User Signature ->OUSR
  ObjectId Int(11) Object ID
  DataKey nVarChar(50) Data Key
  VisOrder Int(11) Visual Order
  IsVisible VarChar(1) Visible default=Y [Y=Yes, N=No]

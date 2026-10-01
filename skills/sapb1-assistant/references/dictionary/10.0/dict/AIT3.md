<!-- source: REFDB.chm (SAP Business One SDK 10.0 - Database Tables Reference) | version: SAP Business One 10.0 | verified: 2026-10-01 -->
# AIT3 - Items - Localization Fields - History
Module: Inventory and Production | 4 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: ItemCode, LogInstanc
Fields (name type(len) description [values] ->parent table):
  ItemCode nVarChar(50) Item No. ->OITM
  IncNature nVarChar(10) Income Nature ->OBMI
  LogInstanc Int(11) IPI Class Code
  ObjType nVarChar(20) Log Instance default=0

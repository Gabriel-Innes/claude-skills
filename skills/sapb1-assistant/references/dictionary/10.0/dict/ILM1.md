<!-- source: REFDB.chm (SAP Business One SDK 10.0 - Database Tables Reference) | version: SAP Business One 10.0 | verified: 2026-10-01 -->
# ILM1 - Srl & Batch Det of Inv Log Msg
Module: Inventory and Production | 5 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: MessageID, ItemCode, SysNumber
Fields (name type(len) description [values] ->parent table):
  MessageID Int(11) Message ID ->OILM
  ItemCode nVarChar(50) Item Code ->OITM
  SysNumber Int(11) System Number
  Quantity Num(19,6) Quantity
  MdAbsEntry Int(11) MD Abs Entry

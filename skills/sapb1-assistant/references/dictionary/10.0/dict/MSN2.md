<!-- source: REFDB.chm (SAP Business One SDK 10.0 - Database Tables Reference) | version: SAP Business One 10.0 | verified: 2026-10-01 -->
# MSN2 - MRP Run Results
Module: MRP | 10 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: AbsEntry, PeriodID, ItemCode
Fields (name type(len) description [values] ->parent table):
  AbsEntry Int(11) Internal Number
  ItemCode nVarChar(50) Item No. ->OITM
  PeriodID Int(11) Period ID
  Initial Num(19,6) Initial Quantity
  InitialOrg Num(19,6) Original Initial Quantity
  InStock Num(19,6) Incoming Stock
  OutStock Num(19,6) Outgoing Stock
  Final Num(19,6) Final Quantity
  FinalOrg Num(19,6) Original Final Quantity
  Requests Num(19,6) Requests

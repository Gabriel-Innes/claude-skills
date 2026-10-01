<!-- source: REFDB.chm (SAP Business One SDK 10.0 - Database Tables Reference) | version: SAP Business One 10.0 | verified: 2026-10-01 -->
# BAL1 - Opening Balance Instances
Module: Marketing Documents | 14 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: AbsEntry, Instance
Fields (name type(len) description [values] ->parent table):
  AbsEntry Int(11) Internal Number
  Instance Int(11) Instance
  OBDate Date(8) Date of Opening Balance (first day of next fiscal period)
  InAmount Num(19,6) Total Received Value
  InQty Num(19,6) Total Received Quantity
  OutQty Num(19,6) Total Issued Quantity
  InAmntLWA Num(19,6) Last Non-zero Total Received Value
  InQtyLWA Num(19,6) Last Non-zero Total Received Quantity
  LastTrnsID Int(11) Last Transaction ID
  WasPrevOB VarChar(1) OB from Start of Fiscal Year default=N [Y=Yes, N=No]
  CreateDate Date(8) Create Date
  UpdateDate Date(8) Update Date
  CrossPRev Num(19,6) Cross Period Revaluation from Next Period
  WasUpdPrCB VarChar(1) Update previous Closing Balance with cross period revaluations default=N [Y=Yes, N=No]

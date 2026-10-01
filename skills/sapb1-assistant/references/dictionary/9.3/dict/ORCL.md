<!-- source: erpref.com (schema IP: SAP) | version: SAP Business One 9.3 | verified: 2026-10-01 -->
# ORCL - Recurring Transaction Instances
Module: Marketing Documents | 7 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: AbsEntry
Fields (name type(len) description [values] ->parent table):
  AbsEntry Int(11) Internal Number
  RcpEntry Int(11) Template Entry ->ORCP
  Instance Int(11) Recurrence Instance default=0
  PlanDate Date(8) Scheduled Date
  Status VarChar(1) Recurrence Status default=N [N=Not Executed, E=Executed, R=Removed]
  DocObjType nVarChar(20) Document Object Type [13=Invoice, 112=Draft]
  DocEntry Int(11) Created Doc Entry

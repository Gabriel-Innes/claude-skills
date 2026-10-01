<!-- source: erpref.com (schema IP: SAP) | version: SAP Business One 9.3 | verified: 2026-10-01 -->
# MSN4 - MRP Scenarios - Items Array
Module: MRP | 14 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: ItemCode, AbsEntry
  ItemCode: ItemCode
Fields (name type(len) description [values] ->parent table):
  AbsEntry Int(11) Internal Number ->OMSN
  ItemCode nVarChar(50) Item Code
  Selected VarChar(1) Selected default=Y [Y=Yes, N=No]
  TmpForMrp VarChar(1) Is Temporary for MRP default=N
  WorDueDate Date(8) Production Order Due Date
  DsmDueDate Date(8) Disassembly Order Due Date
  NorDueDate Date(8) Non Prd Order Doc. Due Date
  Interval Int(6) Order Intervals
  Multiple Num(19,6) Order Multiple
  MinORdrQty Num(19,6) Minimum Order Quantity
  LeadTime Int(11) Lead Time
  prcrmntMtd VarChar(1) Procurement Method default=B [B=Buy, M=Make]
  ToleranDay Int(11) Tolerance Day
  CompoWH VarChar(1) Component Warehouse default=B [B=From Bill of Materials Line, P=From Parent Item Document Line]

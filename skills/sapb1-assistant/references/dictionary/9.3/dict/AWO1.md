<!-- source: erpref.com (schema IP: SAP) | version: SAP Business One 9.3 | verified: 2026-10-01 -->
# AWO1 - Production Order (Rows) - History
Module: Inventory and Production | 37 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: LogInstanc, LineNum, DocEntry
  VISORDER U: LogInstanc, VisOrder, DocEntry
  ITEM_CODE: ItemCode
Fields (name type(len) description [values] ->parent table):
  DocEntry Int(11) Document Internal Number ->OWOR
  LineNum Int(11) Row Number
  ItemCode nVarChar(50) Item No.
  BaseQty Num(19,6) Base Quantity
  PlannedQty Num(19,6) Planned Quantity - Rows
  IssuedQty Num(19,6) Issued Quantity
  IssueType VarChar(1) Production Order Issue Type [M=Manual, B=Backflush]
  wareHouse nVarChar(8) Warehouse ->OWHS
  VisOrder Int(11) Visual Order
  WipActCode nVarChar(15) WIP Account Code ->OACT
  CompTotal Num(19,6) Total Completed Sum
  OcrCode nVarChar(8) Distribution Rule ->OOCR
  OcrCode2 nVarChar(8) Distribution Rule2 ->OOCR
  OcrCode3 nVarChar(8) Distribution Rule3 ->OOCR
  OcrCode4 nVarChar(8) Distribution Rule4 ->OOCR
  OcrCode5 nVarChar(8) Distribution Rule5 ->OOCR
  LocCode Int(11) Location Code ->OLCT
  LogInstanc Int(11) Log Instance default=0
  Project nVarChar(20) Project Code ->OPRJ
  UomEntry Int(11) UoM Entry default=0 ->OUOM
  UomCode nVarChar(20) UoM Code
  ItemType Int(11) Item Type default=4 [4=Item, 290=Resource, -18=Text]
  AdditQty Num(19,6) Additional Quantity
  LineText Text(16) Row Text
  PickStatus VarChar(1) Pick Status default=N [Y=Picked, N=Not Picked, R=Release for Picking, P=Partially Picked]
  PickQty Num(19,6) Pick Quantity
  PickIdNo Int(11) Pick List ID Number
  ReleaseQty Num(19,6) Released Quantity
  ResAlloc VarChar(1) Resource Allocation [S=On Start Date, D=On End Date, F=Start Date Forwards, B=End Date Backwards]
  StartDate Date(8) Start Date
  EndDate Date(8) End Date
  StageId Int(11) Stage ID
  BaseQtyNum Num(19,6) Base Quantity Numerator
  BaseQtyDen Num(19,6) Base Quantity Denominator
  ReqDays Num(19,6) Required Days default=0
  RtCalcProp Num(19,6) Routing Calculation Proportion default=100
  Status VarChar(1) Stage Status default=P [P=Planned, I=In Progress, C=Complete]

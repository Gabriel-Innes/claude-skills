<!-- source: erpref.com (schema IP: SAP) | version: SAP Business One 9.3 | verified: 2026-10-01 -->
# UBTN - Batch Numbers Master Data
Module: Inventory and Production | 32 columns
Indexes (name: columns; first = primary key; U = unique) - WARNING: multi-column key order here is reversed vs SAP's 10.0 reference (read as a set; see references/dictionary/INDEX.md):
  PRIMARY U: AbsEntry
  SYSTEM_KEY U: SysNumber, ItemCode
  DIST_KEY: DistNumber, ItemCode
Fields (name type(len) description [values] ->parent table):
  ItemCode nVarChar(50) Item No. ->OITM
  SysNumber Int(11) System Number
  DistNumber nVarChar(36) Batch Number
  MnfSerial nVarChar(36) Batch Attribute 1
  LotNumber nVarChar(36) Batch Attribute 2
  ExpDate Date(8) Expiration Date
  MnfDate Date(8) Manufacturing Date
  InDate Date(8) Admission Date
  GrntStart Date(8) Warranty Start Date
  GrntExp Date(8) Warranty End Date
  CreateDate Date(8) Creation Date
  Location nVarChar(100) Location
  Status VarChar(1) Status default=0 [0=Released, 1=Not Accessible, 2=Locked]
  Notes Text(16) Details
  DataSource VarChar(1) Data Source default=N [N=Unknown, I=Interface, U=Update, M=Import, O=DI API, A=Doc. Generation Wizard, D=Restore Wizard, P=Partner Implementation, T=Year Transfer]
  UserSign Int(6) User Signature ->OUSR
  Transfered VarChar(1) Transferred default=N [Y=Yes, N=No]
  Instance Int(6) Instance default=0
  AbsEntry Int(11) Abs. Entry
  ObjType nVarChar(20) Object Type
  itemName nVarChar(100) Item Description
  LogInstanc Int(11) Log Instance
  UserSign2 Int(6) Updating User ->OUSR
  UpdateDate Date(8) Update Date
  CostTotal Num(19,6) Total Cost of Batches
  Quantity Num(19,6) Quantity
  QuantOut Num(19,6) Output Quantity
  PriceDiff Num(19,6) Price Difference
  Balance Num(19,6) Batch Balance
  TrackingNt Int(11) CCD Tracking Note ->OTCN
  TrackiNtLn Int(11) CCD Tracking Note Line ->TCN1
  SumDec Int(6) Totals Accuracy for SnB

<!-- source: erpref.com (schema IP: SAP) | version: SAP Business One 9.3 | verified: 2026-10-01 -->
# OSRN - Serial Numbers Master Data
Module: Inventory and Production | 32 columns | ObjType: 10000045
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: AbsEntry
  SYSTEM_KEY U: SysNumber, ItemCode
  DIST_KEY: DistNumber, ItemCode
  LOT_KEY: LotNumber, ItemCode
Fields (name type(len) description [values] ->parent table):
  ItemCode nVarChar(50) Item No. ->OITM
  SysNumber Int(11) System Number
  DistNumber nVarChar(36) Serial Number
  MnfSerial nVarChar(36) Manufacturer Serial No.
  LotNumber nVarChar(36) Lot Number
  ExpDate Date(8) Expiration Date
  MnfDate Date(8) Manufacturing Date
  InDate Date(8) Admission Date
  GrntStart Date(8) Mfr Warranty Start Date
  GrntExp Date(8) Mfr Warranty End Date
  CreateDate Date(8) Creation Date
  Location nVarChar(100) Location
  Status VarChar(1) Status [0=Available, 1=Unavailable, 2=Allocated]
  Notes Text(16) Details
  DataSource VarChar(1) Data Source default=N [N=Unknown, I=Interface, U=Update, M=Import, O=DI API, A=Doc. Generation Wizard, D=Restore Wizard, P=Partner Implementation, T=Year Transfer]
  UserSign Int(6) User Signature ->OUSR
  Transfered VarChar(1) Transferred default=N [Y=Yes, N=No]
  Instance Int(6) Instance default=0
  AbsEntry Int(11) abs entry
  ObjType nVarChar(20) object type
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

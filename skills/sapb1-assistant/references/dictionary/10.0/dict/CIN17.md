<!-- source: REFDB.chm (SAP Business One SDK 10.0 - Database Tables Reference) | version: SAP Business One 10.0 | verified: 2026-10-01 -->
# CIN17 - Correction Invoice - Bin Allocation Data
Module: Marketing Documents | 16 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: DocEntry, LineNum
Fields (name type(len) description [values] ->parent table):
  DocEntry Int(11) Internal Number ->OCIN
  LineNum Int(11) Bin Allocation Sequence
  LogInstanc Int(11) Line Number default=0
  ObjectType nVarChar(20) Subline Number default=132 ->ADP1
  ImpDocType VarChar(1) SnB Type ->OBSI
  ImpDocNum nVarChar(10) SnB Master Data Internal Number
  DateOfReg Date(8) Bin Internal Number
  CustClrDat Date(8) Quantity
  ConcActNum nVarChar(30) Item Code
  AdditNum nVarChar(30) Warehouse Code
  AddItmDV Num(19,6) Object Type
  tpVTransp Int(6) Overland Transport Route [1=Maritime, 2=Waterway, 3=Lakeside, 4=Air, 5=Post, 6=Train, 7=Road, 8=Network Transmission, 9=Own Means, 10=Input/Output Fictitious, 11=Courier, 12=Hand Carry]
  DrawSReg nVarChar(11) Drawback - Suspension Regime
  AddFrNavyA Num(19,6) Additional Freight to Navy Authority
  TypeOfImp VarChar(1) Type of Import
  nSeqAdic Int(6) Additional Item Sequential Number

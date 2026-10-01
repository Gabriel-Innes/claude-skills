<!-- source: erpref.com (schema IP: SAP) | version: SAP Business One 9.3 | verified: 2026-10-01 -->
# CSV17 - A/R Correction Invoice Reversal - Bin Allocation Data
Module: Marketing Documents | 12 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: LineNum, DocEntry
Fields (name type(len) description [values] ->parent table):
  DocEntry Int(11) Internal Number ->OCSV
  LineNum Int(11) Bin Allocation Sequence
  LogInstanc Int(11) Line Number default=0
  ObjectType nVarChar(20) Subline Number default=166 ->ADP1
  ImpDocType VarChar(1) SnB Type ->OBSI
  ImpDocNum nVarChar(10) SnB Master Data Internal Number
  DateOfReg Date(8) Bin Internal Number
  CustClrDat Date(8) Quantity
  ConcActNum nVarChar(30) Item Code
  AdditNum nVarChar(30) Warehouse Code
  AddItmDV Num(19,6) Object Type
  tpVTransp Int(6) Overland Transport Route [1=Maritime, 2=Waterway, 3=Lakeside, 4=Air, 5=Post, 6=Train, 7=Road, 8=Network Transmission, 9=Own Means, 10=Input/Output Fictitious]

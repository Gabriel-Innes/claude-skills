<!-- source: erpref.com (schema IP: SAP) | version: SAP Business One 9.3 | verified: 2026-10-01 -->
# OBIN - Bin Location
Module: Inventory and Production | 64 columns | ObjType: 10000206
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: AbsEntry
  BIN_CODE U: BinCode
  WHS_CODE: SysBin, WhsCode
  BUSINESS_K: SL4Code, SL3Code, SL2Code, SL1Code, WhsCode
Fields (name type(len) description [values] ->parent table):
  AbsEntry Int(11) Internal Number
  BinCode nVarChar(228) Bin Location Code
  WhsCode nVarChar(8) Warehouse Code ->OWHS
  SysBin VarChar(1) System Bin default=N [Y=Yes, N=No]
  SL1Abs Int(11) Sublevel-1 Internal Number ->OBSL
  SL1Code nVarChar(50) Sublevel-1 Code
  SL2Abs Int(11) Sublevel-2 Internal Number ->OBSL
  SL2Code nVarChar(50) Sublevel-2 Code
  SL3Abs Int(11) Sublevel-3 Internal Number ->OBSL
  SL3Code nVarChar(50) Sublevel-3 Code
  SL4Abs Int(11) Sublevel-4 Internal Number ->OBSL
  SL4Code nVarChar(50) Sublevel-4 Code
  Attr1Abs Int(11) Attribute-1 Internal Number ->OBAT
  Attr1Val nVarChar(20) Attribute-1 Value
  Attr2Abs Int(11) Attribute-2 Internal Number ->OBAT
  Attr2Val nVarChar(20) Attribute-2 Value
  Attr3Abs Int(11) Attribute-3 Internal Number ->OBAT
  Attr3Val nVarChar(20) Attribute-3 Value
  Attr4Abs Int(11) Attribute-4 Internal Number ->OBAT
  Attr4Val nVarChar(20) Attribute-4 Value
  Attr5Abs Int(11) Attribute-5 Internal Number ->OBAT
  Attr5Val nVarChar(20) Attribute-5 Value
  Attr6Abs Int(11) Attribute-6 Internal Number ->OBAT
  Attr6Val nVarChar(20) Attribute-6 Value
  Attr7Abs Int(11) Attribute-7 Internal Number ->OBAT
  Attr7Val nVarChar(20) Attribute-7 Value
  Attr8Abs Int(11) Attribute-8 Internal Number ->OBAT
  Attr8Val nVarChar(20) Attribute-8 Value
  Attr9Abs Int(11) Attribute-9 Internal Number ->OBAT
  Attr9Val nVarChar(20) Attribute-9 Value
  Attr10Abs Int(11) Attribute-10 Internal Number ->OBAT
  Attr10Val nVarChar(20) Attribute-10 Value
  Disabled VarChar(1) Inactive default=N [Y=Yes, N=No]
  Descr nVarChar(50) Description
  BarCode nVarChar(100) Bar Code
  AltSortCod nVarChar(50) Alternative Sort Code
  ItmRtrictT Int(6) Item Restriction Type default=0 [0=None, 1=Specific Item, 2=Single Item Only, 3=Specific Item Group, 4=Single Item Group Only]
  SpcItmCode nVarChar(50) Specific Item Code ->OITM
  SpcItmGrpC Int(6) Specific Item Group Code ->OITB
  SngBatch VarChar(1) Batch Restriction default=N [N=None, Y=Single Batch]
  RtrictType Int(6) Restricted Transactions Type default=0 [0=None, 1=All Transactions, 2=Inbound Transactions, 3=Outbound Transactions, 4=All Except Inventory Transfer and Counting Transactions]
  RtrictResn nVarChar(254) Reason for Restriction
  RtrictDate Date(8) Last Updated On
  DataSource VarChar(1) Data Source default=N
  UserSign Int(6) User Signature ->OUSR
  Transfered VarChar(1) Year Transfer [Y/N] default=N
  Instance Int(6) Instance default=0
  LogInstanc Int(11) Log Instance default=0
  CreateDate Date(8) Create Date
  UserSign2 Int(6) Updating User ->OUSR
  UpdateDate Date(8) Date of Update
  Deleted VarChar(1) Deleted default=N
  MinLevel Num(19,6) Minimum Qty
  MaxLevel Num(19,6) Maximum Qty
  ReceiveBin VarChar(1) Receiving Bin Location default=N [Y=Yes, N=No]
  NoAutoAllc VarChar(1) Excl. fr. Auto Alloc. on Issue default=N [Y=Yes, N=No]
  MaxWeight1 Num(19,6) Maximum Weight 1
  Wght1Unit Int(6) Unit of Maximum Weight 1 ->OWGT
  MaxWeight2 Num(19,6) Maximum Weight 2
  Wght2Unit Int(6) Unit of Maximum Weight 2 ->OWGT
  UoMRtrict Int(6) UoM Restriction default=0 [0=None, 1=Specific UoM, 2=Single UoM Only, 3=Specific UoM Group, 4=Single UoM Group Only]
  SpcUoMCode Int(11) Specified UoM Code ->OUOM
  SpcUGPCode Int(11) Specified UoM Group Code ->OUGP
  SngUoMCode Int(11) Single UoM Code ->OUOM

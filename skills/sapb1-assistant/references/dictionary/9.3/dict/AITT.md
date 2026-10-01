<!-- source: erpref.com (schema IP: SAP) | version: SAP Business One 9.3 | verified: 2026-10-01 -->
# AITT - Product Tree - History
Module: Inventory and Production | 27 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: LogInstac, Code
Fields (name type(len) description [values] ->parent table):
  Code nVarChar(50) Parent Item ->OITM
  TreeType VarChar(1) BOM Type default=P [A=Assembly, S=Sales, P=Production, T=Template]
  PriceList Int(6) Price List default=0 ->OPLN
  Qauntity Num(19,6) No. of Units
  CreateDate Date(8) Creation Date
  UpdateDate Date(8) Date of Update
  Transfered VarChar(1) Postponed to Next Year default=N [Y=Yes, N=No]
  DataSource VarChar(1) Data source default=N [N=Unknown, I=Interface, U=Update, M=Import, O=DI API, A=Doc. Generation Wizard, D=Restore Wizard, P=Partner Implementation, T=Year Transfer]
  UserSign Int(6) User Signature ->OUSR
  SCNCounter Int(6) SCN Counter
  DispCurr nVarChar(3) Display Currency
  ToWH nVarChar(8) Whse for Finished Product
  Object nVarChar(20) Object Type default=66
  LogInstac Int(11) Log Instance - History
  UserSign2 Int(11) Updating User ->OUSR
  OcrCode nVarChar(8) Distribution Rule ->OOCR
  HideComp VarChar(1) Hide Components in Printing default=N [Y=Yes, N=No]
  OcrCode2 nVarChar(8) Distribution Rule2 ->OOCR
  OcrCode3 nVarChar(8) Distribution Rule3 ->OOCR
  OcrCode4 nVarChar(8) Distribution Rule4 ->OOCR
  OcrCode5 nVarChar(8) Distribution Rule5 ->OOCR
  UpdateTime Int(11) Time of Update
  Project nVarChar(20) Project Code ->OPRJ
  PlAvgSize Num(19,6) Planned Average Production Size default=1
  Name nVarChar(100) Product Description
  CreateTS Int(11) Create Time - Incl. Secs
  UpdateTS Int(11) Update Full Time

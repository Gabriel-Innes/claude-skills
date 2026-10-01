<!-- source: REFDB.chm (SAP Business One SDK 10.0 - Database Tables Reference) | version: SAP Business One 10.0 | verified: 2026-10-01 -->
# SCL4 - Expense Documents
Module: Service | 17 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: SrcvCallID, Line, PartType, DocAbs, Object
Fields (name type(len) description [values] ->parent table):
  SrcvCallID Int(11) Service Call No. ->OSCL
  Line Int(6) Row default=-1
  PartType VarChar(1) Part Type default=I [I=Inventory, N=Travel/Labor]
  DocAbs Int(11) Document Internal Number
  Object nVarChar(20) Document Type default=13 [13=A/R Invoice, 15=Delivery, 16=Returns, 67=Inventory Transfer, 14=A/R Credit Memo, 165=A/R Correction Invoice, 0=, 17=Sales Order, 23=Sales Quotation, 540000006=Purchase Quotation, 22=Purchase Order, 20=Goods Receipt PO, 18=A/P Invoice, 19=A/P Credit Memo, 21=Goods Return, 234000032=Goods Return Request, 234000031=Return Request]
  DocPstDate Date(8) Document Posting Date
  ObjectType nVarChar(20) Object Type default=191
  LogInstanc Int(11) Log Instance
  UserSign Int(6) User Signature ->OUSR
  CreateDate Date(8) Creation Date
  UserSign2 Int(6) User Signature 2 ->OUSR
  UpdateDate Date(8) Date of Update
  DocNumber Int(11) Document No.
  Transfered VarChar(1) Transfered default=Y [Y=Yes, N=No]
  VisOrder Int(11) Visual Order
  StckTrnDir VarChar(1) Inventory Transaction Direction [T=Transfer to Technician, N=Transfer from Technician]
  Instance Int(6) Instance default=0

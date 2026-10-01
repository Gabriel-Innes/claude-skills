<!-- source: erpref.com (schema IP: SAP) | version: SAP Business One 9.3 | verified: 2026-10-01 -->
# ORCJ - Resource Capacity Log
Module: General | 24 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: Id
  RWDT: CapType, CapDate, WhsCode, ResCode
  BASE_DOC: BaseLine, BaseAbsEnt, BaseObjTyp
  OWNING_DOC: OwnLine, OwnAbsEnt, OwnObjTyp
Fields (name type(len) description [values] ->parent table):
  Id Int(11) Primary Key
  ResCode nVarChar(50) Internal Resource ID ->ORSC
  WhsCode nVarChar(8) Warehouse Code ->OWHS
  CapDate Date(8) Capacity Date
  CapType VarChar(1) Type of Capacity Entry default=I [I=Internal, O=Ordered, C=Committed, U=Consumed]
  Capacity Num(19,6) Capacity
  SrcObjType Int(11) Source Object Type default=-1 [-1=, 202=Production Order, 60=Issue for Production, 59=Receipt from Production, 17=Sales Order, 15=Delivery, 13=A/R Invoice, -13=A/R Reserve Invoice, 14=A/R Credit Memo, 165=A/R Correction Invoice, 166=A/R Correction Invoice Reversal, 16=Returns, 22=Purchase Order, 20=Goods Receipt PO, 18=A/P Invoice, -18=A/P Reserve Invoice, 19=A/P Credit Memo, 163=A/P Correction Invoice, 164=A/P Correction Invoice Reversal, 21=Goods Return]
  SrcAbsEnt Int(11) Source Absolute Entry
  SrcLine Int(11) Source Line Number
  BaseObjTyp Int(11) Base Object Type default=-1 [-1=, 202=Production Order]
  BaseAbsEnt Int(11) Base Absolute Entry
  BaseLine Int(11) Base Line Number
  ActionType Int(6) Action Type default=-1 [-1=, 1=Production Order - Create, 2=Production Order - Close, 3=Production Order - Reschedule, 4=Production Order - Add Line, 5=Production Order - Delete Line, 6=Production Order - Update Line, 7=Issue for Production - Create, 8=Receipt from Production - Create, 9=Sales Order - Create, 10=Sales Order - Close, 11=Sales Order - Cancel, 12=Sales Order - Add Line, 13=Sales Order - Delete Line, 14=Sales Order - Update Line, 15=Delivery - Create, 16=Delivery - Close, 17=Delivery - Cancel, 18=A/R Invoice - Create, 19=A/R Invoice - Cancel, 20=A/R Credit Memo - Create, 21=A/R Credit Memo - Cancel, 22=Correction A/R Invoice - Create, 23=Correction A/R Invoice Reversal - Create, 24=Returns - Create, 25=Returns - Cancel, 26=Returns - Close, 27=Purchase Order - Create, 28=Purchase Order - Close, 29=Purchase Order - Cancel, 30=Purchase Order - Add Line, 31=Purchase Order - Delete Line, 32=Purchase Order - Update Line, 33=Goods Receipt PO - Create, 34=Goods Receipt PO - Close, 35=Goods Receipt PO - Cancel, 36=A/P Invoice - Create, 37=A/P Invoice - Cancel, 38=A/P Credit Memo - Create, 39=A/P Credit Memo - Cancel, 40=Correction A/P Invoice - Create, 41=Correction A/P Invoice Reversal - Create, 42=Goods Return - Create, 43=Goods Return - Cancel, 44=Goods Return - Close, 45=A/R Invoice - Update, 46=A/P Invoice - Update, 47=A/R Reserve Invoice - Create, 48=A/R Reserve Invoice - Update, 49=A/R Reserve Invoice - Cancel, 50=A/P Reserve Invoice - Create, 51=A/P Reserve Invoice - Update, 52=A/P Reserve Invoice - Cancel]
  OwnObjTyp Int(11) Owning Doc. Object Type default=-1 [-1=, 202=Production Order, 60=Issue for Production, 59=Receipt from Production, 17=Sales Order, 15=Delivery, 13=A/R Invoice, -13=A/R Reserve Invoice, 14=A/R Credit Memo, 165=A/R Correction Invoice, 166=A/R Correction Invoice Reversal, 16=Returns, 22=Purchase Order, 20=Goods Receipt PO, 18=A/P Invoice, -18=A/P Reserve Invoice, 19=A/P Credit Memo, 163=A/P Correction Invoice, 164=A/P Correction Invoice Reversal, 21=Goods Return]
  OwnAbsEnt Int(11) Owning Doc. Absolute Entry
  OwnLine Int(11) Owning Doc. Line Number
  RevdObjTyp Int(11) Reverted Object Type default=-1 [-1=, 60=Issue for Production]
  RevdAbsEnt Int(11) Reverted Absolute Entry
  RevdLine Int(11) Reverted Line Number
  MemoSrc VarChar(1) Memo Source default=- [-=, C=Resource Capacity Form, S=Set Daily Internal Capacities Form]
  Memo Text(16) Memo
  SngRunCap Num(19,6) Single Run Capacity
  MemoSrcSng VarChar(1) Memo Source of Single Run Capacity default=- [-=, C=Resource Capacity Form, S=Set Daily Internal Capacities Form]
  MemoSng Text(16) Memo of Single Run Capacity

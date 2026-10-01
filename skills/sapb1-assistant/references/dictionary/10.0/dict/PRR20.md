<!-- source: REFDB.chm (SAP Business One SDK 10.0 - Database Tables Reference) | version: SAP Business One 10.0 | verified: 2026-10-01 -->
# PRR20 - Intrastat Expenses
Module: Marketing Documents | 20 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: DocEntry, LineNum
Fields (name type(len) description [values] ->parent table):
  DocEntry Int(11) Document Internal ID ->OPRR
  ExpnsCode Int(11) Freight Code ->OEXD
  TotalLC Num(19,6) Total
  TotalFC Num(19,6) Total (FC)
  TotalSC Num(19,6) Total (SC)
  DistribM VarChar(1) Distribution Method default=T [Q=Quantity, V=Volume, W=Weight, E=Equally, T=Row Total]
  DrawnLC Num(19,6) Drawn Total
  DrawnFC Num(19,6) Drawn Total (FC)
  DrawnSC Num(19,6) Drawn Total (SC)
  LineNum Int(11) Line Number default=-1
  BaseAbsEnt Int(11) Base Abs. Entry default=-1
  BaseType Int(11) Base Document Type default=-1 [23=Sales Quotation, 17=Sales Order, 15=Delivery Notes, 16=Return, 13=A/R Invoice, 203=Down Payment Incoming, 204=Down Payment Outgoing, 22=Purchase Order, 20=Goods Receipt PO, 21=Goods Return, 18=A/P Invoice, 540000006=Purchase Quotation, 0=, -1=]
  BaseRef Int(11) Base Document Reference
  BaseLnNum Int(11) Base Document Row No. default=-1
  LogInstanc Int(11) Log Instance default=0
  ObjectType nVarChar(20) Object Type default=234000032 ->ADP1
  FixCurr nVarChar(3) Fixation Currency ->OCRN
  AppliedLC Num(19,6) Applied
  AppliedFC Num(19,6) Applied (FC)
  AppliedSC Num(19,6) Applied (SC)

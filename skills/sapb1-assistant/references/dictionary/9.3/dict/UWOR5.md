<!-- source: erpref.com (schema IP: SAP) | version: SAP Business One 9.3 | verified: 2026-10-01 -->
# UWOR5 - Production Order - Document Reference Information
Module: Inventory and Production | 10 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: LineNum, DocEntry
  DOC_ENTRY: DocEntry
Fields (name type(len) description [values] ->parent table):
  DocEntry Int(11) Document Internal Number
  ObjType nVarChar(20) Object Type default=202
  LogInstanc Int(11) Log Instance default=0
  LineNum Int(11) Line Number
  RefDocEntr Int(11) Referenced Internal Number
  RefDocNum Int(11) Referenced Document Number
  ExtDocNum nVarChar(100) External Referenced Document Number
  RefObjType nVarChar(20) Referenced Object Type [-1=External Document, 23=Sales Quotation, 17=Sales Order, 15=Delivery Notes, 234000031=Return Request, 16=Return, 203=Down Payment Incoming, 13=A/R Invoice, 14=A/R Credit Memo, 165=A/R Correction Invoice, 280=A/R Tax Invoice, 540000006=Purchase Quotation, 22=Purchase Order, 20=Goods Receipt PO, 234000032=Goods Return Request, 21=Goods Return, 204=Down Payment Outgoing, 18=A/P Invoice, 19=A/P Credit Memo, 163=A/P Correction Invoice, 281=A/P Tax Invoice, 69=Landed Costs, 24=Incoming Payments, 30=Journal Entry, 202=Production Order]
  IssueDate Date(8) Date of Issue
  Remark nVarChar(254) Remarks

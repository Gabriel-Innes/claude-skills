<!-- source: REFDB.chm (SAP Business One SDK 10.0 - Database Tables Reference) | version: SAP Business One 10.0 | verified: 2026-10-01 -->
# AIN12 - Inventory Counting - Document Reference Information - History
Module: Inventory and Production | 10 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: DocEntry, LineNum, ObjType, LogInstanc
  DOC_ENTRY: DocEntry
Fields (name type(len) description [values] ->parent table):
  DocEntry Int(11) Internal Number
  ObjType Int(11) Object Type
  LogInstanc Int(11) Log Instance default=0
  LineNum Int(11) Line Number
  RefDocEntr Int(11) Referenced Internal Number
  RefDocNum Int(11) Referenced Document Number
  ExtDocNum nVarChar(100) External Referenced Document Number
  RefObjType nVarChar(20) Referenced Object Type [23=Sales Quotation, 17=Sales Order, 15=Delivery Notes, 234000031=Return Request, 16=Return, 203=A/R Down Payment, 13=A/R Invoice, 14=A/R Credit Memo, 165=A/R Correction Invoice, 280=A/R Tax Invoice, 1470000113=Purchase Request, 540000006=Purchase Quotation, 22=Purchase Order, 20=Goods Receipt PO, 234000032=Goods Return Request, 21=Goods Return, 204=A/P Down Payment, 18=A/P Invoice, 19=A/P Credit Memo, 163=A/P Correction Invoice, 281=A/P Tax Invoice, 69=Landed Costs, 24=Incoming Payments, 46=Outgoing Payments, 57=Checks for Payment, 321=Internal Reconciliation, 34=Recurring Posting, 30=Journal Entry, 59=Goods Receipt, 60=Goods Issue, 162=Inventory Revaluation, 1470000065=Inventory Counting, 10000071=Inventory Posting, 1250000001=Inventory Transfer Request, 67=Inventory Transfer, 202=Production Order, 13001=Original Invoice, -1=External Document]
  IssueDate Date(8) Date of Issue
  Remark nVarChar(254) Remarks

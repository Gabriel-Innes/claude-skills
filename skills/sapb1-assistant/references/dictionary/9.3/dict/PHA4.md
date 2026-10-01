<!-- source: erpref.com (schema IP: SAP) | version: SAP Business One 9.3 | verified: 2026-10-01 -->
# PHA4 - Project Management - Stages - Documents
Module: General | 18 columns
Indexes (name: columns; first = primary key; U = unique) - WARNING: multi-column key order here is reversed vs SAP's 10.0 reference (read as a set; see references/dictionary/INDEX.md):
  PRIMARY U: LineID, AbsEntry
Fields (name type(len) description [values] ->parent table):
  AbsEntry Int(11) Internal Key ->PHA1
  LineID Int(11) Row No.
  StageID Int(11) Stage ID ->PHA1
  TYP Int(11) Document Type default=-1 [-1=Please select, 112=Document Draft, 30=Manual Journal Entry, 23=Sales Quotation, 17=Sales Order, 15=Delivery, 16=Return, 203002=A/R Down Payment Request, 203=A/R Down Payment Invoice, 13=A/R Invoice, 14=A/R Credit Memo, 13002=A/R Reserve Invoice, 540000006=Purchase Quotation, 22=Purchase Order, 20=Goods Receipt PO, 21=Goods Return, 204002=A/P Down Payment Request, 204=A/P Down Payment Invoice, 18=A/P Invoice, 19=A/P Credit Memo, 18002=A/P Reserve Invoice, 191=Service Call, 59=Goods Receipt, 60=Goods Issue, 165=A/R Correction Invoice, 166=A/R Correction Invoice Reversal, 163=A/P Correction Invoice, 164=A/P Correction Invoice Reversal, 1470000113=Purchase Request, 234000032=Goods Return Request, 234000031=Return Request]
  DOCNUM Int(11) Document Number
  DocEntry Int(11) Document Abs. Entry
  DocDate Date(8) Document Date
  Total Num(19,6) Total
  LineNum Int(11) Line Number
  Status VarChar(1) Line status default=O [O=Open, C=Closed]
  LogInstanc Int(11) Log Instance default=0
  AmountCat VarChar(1) Category to which we will apply the amount from Total [I=Invoiced, O=Open]
  Categorize nVarChar(2) Category Open Amount/Invoiced A/R, A/P to which we will apply the amount from journal entry [OP=Open Amount (A/P), OR=Open Amount (A/R), IP=Invoiced (A/P), IR=Invoiced (A/R)]
  Operation VarChar(1) Operation which we will apply to the amount from the total [A=Add, S=Subtract]
  Chargeable VarChar(1) Chargeable [Yes/No] default=N [Y=Yes, N=No]
  Charged Num(19,6) Charged
  ChargedQty Num(19,6) Charged Quantity
  DocType VarChar(1) Document Type default=I [I=Item, S=Service]

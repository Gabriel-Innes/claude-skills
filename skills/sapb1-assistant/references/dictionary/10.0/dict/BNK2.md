<!-- source: REFDB.chm (SAP Business One SDK 10.0 - Database Tables Reference) | version: SAP Business One 10.0 | verified: 2026-10-01 -->
# BNK2 - Bank Statement - Recommendation List
Module: Banking | 29 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: IdNumber, BSLine, ListLineID
Fields (name type(len) description [values] ->parent table):
  IdNumber Int(11) Bank Statement ID
  BSLine Int(11) Bank Statement Line ID
  ListLineID Int(6) List Line ID
  DocID nVarChar(27) Document Identifier
  DocType Int(6) Document Type [15=Delivery, 16=Returns, 203=A/R Down Payment, 13=A/R Invoice, 14=A/R Credit Memo, 132=Correction Invoice, 20=Goods Receipt PO, 21=Goods Returns, 204=A/P Down Payment, 18=A/P Invoice, 19=A/P Credit Memo, 24=Incoming Payment, 25=Deposit, 46=Payment Advice, 57=Checks for Payment, 76=Postdated Deposit, -2=Opening Balance, -3=Closing Balance, 30=Journal Entry, 58=Whse Reconciliation, 59=Goods Receipt, 60=Goods Issue, 67=Inventory Transfers, -1=All transactions]
  AmntLC Num(19,6) Applied Amount (LC)
  AmntFC Num(19,6) Applied Amount (FC)
  IsDebit VarChar(1) Debit [Yes/No] default=Y [Y=Yes, N=No]
  GLAct nVarChar(15) G/L Account or BP Code ->OACT
  PrftCenter nVarChar(8) Distribution Rule ->OOCR
  Project nVarChar(20) Project ->OPRJ
  VatCode nVarChar(8) VAT Code ->OVTG
  Selected VarChar(1) Selected [Y=Yes, N=No]
  VatLC Num(19,6) VAT or Discount Amount (LC)
  VatFC Num(19,6) VAT or Discount Amount (FC)
  Installmnt Int(11) Installment
  InterimAct nVarChar(15) Interim Account ->OACT
  JdtLine Int(11) Journal Entry ->OJDT
  DocNum Int(11) Document Number
  PrftCent2 nVarChar(8) Distribution Rule2 ->OOCR
  PrftCent3 nVarChar(8) Distribution Rule3 ->OOCR
  PrftCent4 nVarChar(8) Distribution Rule4 ->OOCR
  PrftCent5 nVarChar(8) Distribution Rule5 ->OOCR
  MatchLog nVarChar(254) Matching Criteria Log
  DueBal Num(19,6) Balance Due
  DueBalFC Num(19,6) Balance Due (FC)
  AmntSC Num(19,6) Applied Amount (SC)
  BPLId Int(11) Branch ID ->OBPL
  BPLName nVarChar(100) Branch Name

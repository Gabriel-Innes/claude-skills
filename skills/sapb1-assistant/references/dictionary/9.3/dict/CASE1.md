<!-- source: erpref.com (schema IP: SAP) | version: SAP Business One 9.3 | verified: 2026-10-01 -->
# CASE1 - Internal Recon. Upgrade 2007A
Module: Finance | 36 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: LineId, AbsEntry
Fields (name type(len) description [values] ->parent table):
  AbsEntry Int(11) Header Internal ID ->CASE
  LineId Int(11) Inconsistent Amt Number default=0
  ShortName nVarChar(15) BP Code
  Account nVarChar(15) Account Code ->OACT
  OrigAbsEnt Int(11) Original Doc. Internal ID
  OrigObjTyp Int(11) Original Doc. Type default=0 [0=All, 13=A/R Invoice, 14=A/R Credit Memo, 18=A/P Invoice, 19=A/P Credit Memo, 24=Incoming Payment, 30=Journal Entry, 46=Outgoing Payment, 163=A/P Correction Invoice, 165=A/R Correction Invoice, 203=A/R Down Payment, 204=A/P Down Payment]
  OrigDocNum Int(11) Original Document Number
  OrigInsNum Int(11) Original Installment Number
  OrigTrnsId Int(11) Original JE Trans. No. ->OJDT
  OrigTrnsLn Int(11) Original JE Row No.
  LnkRecnAbs Int(11) Linked Recon. Doc. Internal ID
  LnkRecnObj Int(11) Destination Object Type
  LnkRecnNum Int(11) Destination Document Number
  LnkRecnIns Int(11) Destination Installment Number
  LnkRecnTrn Int(11) Linked and Recon. JE Trans No. ->OJDT
  LnkRecnLn Int(11) Linked and Recon. JE Row No.
  InconsType nVarChar(2) Type of Inconsistency [1=Invoice Linked to Reconciled Payment, 2=Credit Memo Linked to Reconciled Payment, 3=Canceled Reconciliation, 4=Partial Exchange Rate Difference Recognition, 5=Payment Linked to Reconciled Transaction, 6=Journal Entry Linked to Reconciled Payment, 7=Unbalanced Reconciliation, 8=Invoice/Credit Linked to Credit/Invoice, 9=Balancing Upgrade Journal Transaction, 10=Canceled Payment or Journal Entry, 11=Cancellation of Payment/JE within Payment, 12=Unreconciled Balance Rows in Multiple BPs Reconciliation, 13=Missing Exchange Rate Difference behind Multiple BPs Reconciliation, 14=Double Application of Payments of Down Payment Request, 15=Exchange Difference Recognition of Payments of DPM Requests, 16=Reconciliation of Payments Associated with DPM Request, 17=Unbalanced Multiple BP Reconciliation, 18=Amount Differences, 19=Double application of invoice after linking of down payment, 20=Canceled payment of down payment request, 21=Credit Memo based on a Year Transfered invoice, 22=Payment of a year transfer document, 23=Processing of Payment Linked to Transactions, 24=Consolidating Business Partner, 25=Multiple Control Accounts, 26=Different Control Accounts in a Canceled Payment, 0=None]
  ReconNum Int(11) Reconciliation Number
  NewRcnNum Int(11) New Reconciliation No. ->OITR
  CredDeb VarChar(1) Credit or Debit
  Amount Num(19,6) Inconsistent Amount
  AmountFC Num(19,6) Inconsistent Amount (FC)
  AmountSC Num(19,6) Inconsistent Amount (SC)
  TransId Int(11) Balancing Trans. Internal ID ->OJDT
  TransLine Int(11) Balancing Transaction Row No.
  X Num(19,6) x
  Y Num(19,6) Y
  Z Num(19,6) Z
  LnkObjAbsE Int(11) Linked Doc. Internal ID
  LinkObjTyp Int(11) Linked Document Type
  LinkDocNum Int(11) Linked Document Number
  LinkInsNum Int(11) Linked Doc. Installment Number
  LinkTrnsId Int(11) Linked Doc. JE Trans. No. ->OJDT
  LinkTrnsLn Int(11) Linked Doc. JE Row No.
  TrnsTtlAmt Num(19,6) Balancing Trans. Total Amount
  TrnsTtlFc Num(19,6) Balancing Trans. Total Amt FC

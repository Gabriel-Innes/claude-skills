<!-- source: erpref.com (schema IP: SAP) | version: SAP Business One 9.3 | verified: 2026-10-01 -->
# ITR1 - Internal Reconciliation - Rows
Module: Banking | 25 columns
Indexes (name: columns; first = primary key; U = unique) - WARNING: multi-column key order here is reversed vs SAP's 10.0 reference (read as a set; see references/dictionary/INDEX.md):
  PRIMARY U: LineSeq, ReconNum
  Journal: TransRowId, TransId
  Object: SrcObjAbs, SrcObjTyp
Fields (name type(len) description [values] ->parent table):
  ReconNum Int(11) Reconciliation Number ->OITR
  LineSeq Int(11) Row Number
  ShortName nVarChar(15) BP/Account Code
  TransId Int(11) Transaction Internal ID ->OJDT
  TransRowId Int(11) Transaction Row Number
  SrcObjTyp nVarChar(20) Source Object Type [30=Journal Transactions, 13=Invoices, 18=Purchases, 24=Receipts, 46=Outgoing Payments, 14=Revert Invoices, 19=Revert Purchases, 203=Down Payment Incoming, 204=Down Payment Outgoing, 163=Correction A/P Invoice, 164=Correction A/P Invoice Reversals, 165=Correction A/R Invoice, 166=Correction A/R Invoice Reversals]
  SrcObjAbs Int(11) Source Object Internal ID
  ReconSum Num(19,6) Reconciliation Amount
  ReconSumFC Num(19,6) Reconciliation Amount (FC)
  ReconSumSC Num(19,6) Reconciliation Amount (SC)
  FrgnCurr nVarChar(3) Foreign Currency ->OCRN
  SumMthCurr Num(19,6) Amt in Reconciliation Currency
  IsCredit VarChar(1) Credit or Debit [C=Credit, D=Debit]
  Account nVarChar(15) Account Code ->OACT
  CashDisSum Num(19,6) Cash Discount Amount
  WTSum Num(19,6) Withholding Tax Amount
  WTSumFC Num(19,6) Withholding Tax Amount (FC)
  WTSumSC Num(19,6) Withholding Tax Amount (SC)
  ExpSum Num(19,6) Freight Amount
  ExpSumFC Num(19,6) Freight Amount (FC)
  ExpSumSC Num(19,6) Freight Amount (SC)
  netBefDisc Num(19,6) Net Before Discount Sum
  MIEntry Int(11) MI Entry Include this Recon. default=0
  MIType nVarChar(20) MI Type Include this Recon. [270=A/R Monthly Invoice, 140000014=A/P Monthly Invoice]
  InstID Int(11) Installment ID default=0

<!-- source: erpref.com (schema IP: SAP) | version: SAP Business One 9.3 | verified: 2026-10-01 -->
# OTAX - VAT Transactions
Module: Finance | 5 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: AbsEntry
  SECONDARY U: OrdinLNum, SrcObjAbs, SrcObjType
Fields (name type(len) description [values] ->parent table):
  AbsEntry Int(11) Internal Number
  SrcObjType nVarChar(20) Source Object Type default=-1 [-1=, 13=A/R Invoice, 14=A/R Credit Memo, 165=Correction A/R Invoice, 166=Correction A/R Invoice Reversals, 18=A/P Invoice, 19=A/P Credit Memo, 163=Correction A/P Invoice, 164=Correction A/P Invoice Reversals, 46=Outgoing Payment, 24=Incoming Payment, 57=Check for Payment, 30=Journal Transaction, 67=Warehouse Transfer, 25=Deposit, 321=Internal Reconciliation, 76=Deposit Temporary, 140000010=Incoming Excise Invoice, 140000009=Outgoing Excise Invoice, 69=Import file]
  SrcObjAbs Int(11) Source Object Internal ID default=-1
  OrdinLNum Int(11) Ordial Num (BTF & Canceled) default=-1
  Cancelled VarChar(1) Canceled default=N [N=No, Y=Yes]

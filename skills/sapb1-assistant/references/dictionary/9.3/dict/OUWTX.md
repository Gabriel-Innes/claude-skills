<!-- source: erpref.com (schema IP: SAP) | version: SAP Business One 9.3 | verified: 2026-10-01 -->
# OUWTX - Unreported WTax Transactions
Module: Finance | 5 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: AbsEntry
  SECONDARY U: SrcObjAbs, SrcObjType
Fields (name type(len) description [values] ->parent table):
  AbsEntry Int(11) Internal Number
  SrcObjType nVarChar(20) Source Object Type default=-1 [-1=, 13=A/R Invoice, 14=A/R Credit Memo, 18=A/P Invoice, 19=A/P Credit Memo, 46=Outgoing Payment, 24=Incoming Payment]
  SrcObjAbs Int(11) Source Object Internal ID default=-1
  Cancelled VarChar(1) Canceled default=N [N=No, Y=Yes]
  FullCopied VarChar(1) Fully Copied default=N [N=No, Y=Yes]

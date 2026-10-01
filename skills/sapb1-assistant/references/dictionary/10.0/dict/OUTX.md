<!-- source: REFDB.chm (SAP Business One SDK 10.0 - Database Tables Reference) | version: SAP Business One 10.0 | verified: 2026-10-01 -->
# OUTX - Unreported VAT Transactions
Module: Finance | 5 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: AbsEntry
  SECONDARY U: SrcObjType, SrcObjAbs, OrdinLNum
Fields (name type(len) description [values] ->parent table):
  AbsEntry Int(11) Internal Number
  SrcObjType nVarChar(20) Source Object Type default=-1 [-1=, 15=Delivery notes, 16=Revert Delivery Notes, 17=Sales Order, 20=Goods Receipt, 21=Goods Return, 22=Purchase order, 23=Sales Quotation, 112=Document Draft, 59=Goods Receipt, 60=Goods Issue, 28=Journal Batches, 140=Payment Draft, 123=Checks for Payment Drafts, 540000006=Purchase Quotation]
  SrcObjAbs Int(11) Source Object Internal ID default=-1
  OrdinLNum Int(11) Ordial Num (BTF & Canceled) default=-1
  Cancelled VarChar(1) Canceled default=N [N=No, Y=Yes]

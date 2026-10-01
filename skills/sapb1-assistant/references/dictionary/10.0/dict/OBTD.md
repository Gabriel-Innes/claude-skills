<!-- source: REFDB.chm (SAP Business One SDK 10.0 - Database Tables Reference) | version: SAP Business One 10.0 | verified: 2026-10-01 -->
# OBTD - Journal Vouchers List
Module: Finance | 10 columns | ObjType: 29
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: BatchNum
  STATUS: Status
Fields (name type(len) description [values] ->parent table):
  BatchNum Int(11) Journal Voucher No.
  Status VarChar(1) Open/Closed Document default=O [O=Open, C=Closed]
  NumOfTrans Int(6) No. of Transactions
  DateID Date(8) Posting Date
  LocTotal Num(19,6) Total (LC)
  FcTotal Num(19,6) Total (FC)
  SysTotal Num(19,6) Total (SC)
  MemoID nVarChar(50) Details
  UserSign Int(6) User Signature ->OUSR
  Remarks nVarChar(50) Journal Voucher Remarks Field

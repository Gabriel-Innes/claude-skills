<!-- source: REFDB.chm (SAP Business One SDK 10.0 - Database Tables Reference) | version: SAP Business One 10.0 | verified: 2026-10-01 -->
# VRT1 - Tax Invoice Report - Rows
Module: Marketing Documents | 10 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: TxInvRptNo, SeqNo
Fields (name type(len) description [values] ->parent table):
  TxInvRptNo nVarChar(10) Tax Invoice Report No. ->OVRT
  SeqNo Int(11) Sequence No.
  MD Date(8) Original Date of Line Item
  ItemDesc nVarChar(200) Description of Line Item
  Unit nVarChar(100) Unit of Line Item
  Quantity Num(19,6) Quantity
  UnitPrice Num(19,6) Unit Price
  BaseAmt Num(19,6) Base Amount
  TaxAmt Num(19,6) Tax Amount
  Remark nVarChar(100) Remarks

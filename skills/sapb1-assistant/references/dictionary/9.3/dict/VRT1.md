<!-- source: erpref.com (schema IP: SAP) | version: SAP Business One 9.3 | verified: 2026-10-01 -->
# VRT1 - Tax Invoice Report - Rows
Module: Marketing Documents | 10 columns
Indexes (name: columns; first = primary key; U = unique) - WARNING: multi-column key order here is reversed vs SAP's 10.0 reference (read as a set; see references/dictionary/INDEX.md):
  PRIMARY U: SeqNo, TxInvRptNo
Fields (name type(len) description [values] ->parent table):
  TxInvRptNo nVarChar(10) Tax Invoice Report No. ->OVRT
  SeqNo Int(11) Sequence No.
  MD Date(8) Original Date of Line Item
  ItemDesc nVarChar(100) Description of Line Item
  Unit nVarChar(100) Unit of Line Item
  Quantity Num(19,6) Quantity
  UnitPrice Num(19,6) Unit Price
  BaseAmt Num(19,6) Base Amount
  TaxAmt Num(19,6) Tax Amount
  Remark nVarChar(100) Remarks

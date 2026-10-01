<!-- source: erpref.com (schema IP: SAP) | version: SAP Business One 9.3 | verified: 2026-10-01 -->
# VRT2 - Tax Invoice Report Grid Info
Module: Marketing Documents | 21 columns
Indexes (name: columns; first = primary key; U = unique) - WARNING: multi-column key order here is reversed vs SAP's 10.0 reference (read as a set; see references/dictionary/INDEX.md):
  PRIMARY U: GridRow, TxInvRptNo
Fields (name type(len) description [values] ->parent table):
  TxInvRptNo nVarChar(10) Tax Invoice Report No. ->OVRT
  GridRow Int(11) Grid Row Number
  BPLId Int(11) Business Place ID
  BPCode nVarChar(15) BP Code
  BPName nVarChar(100) BP Name
  DocDate Date(8) Doc. Date
  ItemNo nVarChar(50) Item Number
  ItemDes nVarChar(100) Item Description
  TaxCode nVarChar(8) Tax Code
  ItemQty Num(19,6) Item Quantity
  ItemPrice Num(19,6) Item Price
  BaseAmt Num(19,6) Base Amount
  TaxAmt Num(19,6) Tax Amount
  LineType Int(11) Row Type
  DocEntry Int(11) Unique Document ID
  DocType Int(11) Document Type [0=, 13=A/R Invoice, 14=A/R Credit Memo, 203=A/R Down Payment]
  LineNum Int(11) Item Row Number
  Currency nVarChar(3) Currency
  Remark nVarChar(100) Remarks
  LegacyData VarChar(1) Legacy Data default=N [Y=Yes, N=No]
  Quantity Num(19,6) Quantity

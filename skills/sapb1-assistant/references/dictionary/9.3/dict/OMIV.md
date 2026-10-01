<!-- source: erpref.com (schema IP: SAP) | version: SAP Business One 9.3 | verified: 2026-10-01 -->
# OMIV - A/P Monthly Invoice
Module: Marketing Documents | 17 columns
Indexes (name: columns; first = primary key; U = unique) - WARNING: multi-column key order here is reversed vs SAP's 10.0 reference (read as a set; see references/dictionary/INDEX.md):
  PRIMARY U: Entry
  Number U: Number
Fields (name type(len) description [values] ->parent table):
  Entry Int(11) Internal Key
  Number Int(11) Monthly Invoice Number
  Date Date(8) Issued Date
  BPCode nVarChar(15) Vendor Code
  BPName nVarChar(100) Vendor Name
  Currency nVarChar(3) Currency
  LastBilled Num(19,6) Last Billed
  Paid Num(19,6) Paid in the Period
  CarryForw Num(19,6) Carry Forward
  CurAmount Num(19,6) Current Amount
  BillAmount Num(19,6) Billing Amount
  OBPaid Num(19,6) OB Paid in this Period
  OBLstJENum Int(11) OB Last JE Num in the Period
  Predeces Int(11) The Former MI Num
  Successor Int(11) The Latter MI Num
  Series Int(11) Series
  Cancelled VarChar(1) Is Canceled default=N [N=, Y=]

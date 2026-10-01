<!-- source: REFDB.chm (SAP Business One SDK 10.0 - Database Tables Reference) | version: SAP Business One 10.0 | verified: 2026-10-01 -->
# OMIN - A/R Monthly Invoice
Module: Marketing Documents | 19 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: Entry
Fields (name type(len) description [values] ->parent table):
  Entry Int(11) Internal Number
  Number Int(11) Monthly Invoice Number
  Date Date(8) Monthly Invoice Issue Date
  BPCode nVarChar(15) BP Code of Monthly Invoice
  BPName nVarChar(100) BP Name of Monthly Invoice
  Currency nVarChar(3) Currency of Monthly Invoice
  LastBilled Num(19,6) Last Billed
  Paid Num(19,6) Paid in the Period
  CarryForw Num(19,6) Carry Balance Forward
  CurAmount Num(19,6) Current Amount
  BillAmount Num(19,6) Billing Amount
  OBPaid Num(19,6) OB Paid in This Period
  OBLstJENum Int(11) Last JE # for OB at Currnt Dte
  Predeces Int(11) Former Monthly Invoice Number
  Successor Int(11) Latter Monthly Invoice Number
  Series Int(11) Series
  Cancelled VarChar(1) is Canceled default=N [N=, Y=]
  Address nVarChar(254) Bill To
  BPLId Int(11) Branch

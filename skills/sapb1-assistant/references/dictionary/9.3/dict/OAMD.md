<!-- source: erpref.com (schema IP: SAP) | version: SAP Business One 9.3 | verified: 2026-10-01 -->
# OAMD - Amount Differences Report
Module: Reports | 9 columns
Indexes (name: columns; first = primary key; U = unique) - WARNING: multi-column key order here is reversed vs SAP's 10.0 reference (read as a set; see references/dictionary/INDEX.md):
  PRIMARY U: LineNum
Fields (name type(len) description [values] ->parent table):
  LineNum Int(11) Internal ID
  DateFrom Date(8) Date From
  DateTo Date(8) Date To
  CardCode nVarChar(15) BP Code ->OCRD
  Approved VarChar(1) Confirmed default=N [Y=Yes, N=No]
  AmountDiff Num(19,6) Amount Difference (LC)
  TaxAmtDiff Num(19,6) Tax Difference (LC)
  RpCurrency nVarChar(3) Currency Chosen for the Report ->OCRN
  VendOffAct nVarChar(15) Vendor Offset Account ->OACT

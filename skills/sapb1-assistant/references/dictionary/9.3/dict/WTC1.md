<!-- source: erpref.com (schema IP: SAP) | version: SAP Business One 9.3 | verified: 2026-10-01 -->
# WTC1 - WTax Certificates - WT Groups in Certificates
Module: Inventory and Production | 9 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: LineId, AbsEntry
Fields (name type(len) description [values] ->parent table):
  AbsEntry Int(11) Internal Number
  LineId Int(11) Row Number
  WtAbsEntry Int(11) Internal Number
  WTPercent Num(19,6) WTax Rate
  SumVatAmnt Num(19,6) Sum of VAT Amount
  SumDocTot Num(19,6) Sum of Doc. Total Amount
  SumBaseAmn Num(19,6) Sum of Base Amount
  SumAccumAm Num(19,6) Sum of Accumulated Amount
  SumPercpAm Num(19,6) Sum of Perception Amount

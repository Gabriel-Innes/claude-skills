<!-- source: erpref.com (schema IP: SAP) | version: SAP Business One 9.3 | verified: 2026-10-01 -->
# WTC2 - WTax Certificates - Docs in WT Groups
Module: Inventory and Production | 11 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: LineId, BaseLineId, AbsEntry
Fields (name type(len) description [values] ->parent table):
  AbsEntry Int(11) Internal Number
  BaseLineId Int(11) Base Line Number
  LineId Int(11) Line Number
  DocEntry Int(11) Internal Number
  DocObjType nVarChar(20) Doc. Object Type
  VatAmnt Num(19,6) VAT Amount
  DocTot Num(19,6) Doc. Total Amount
  WTBaseAmnt Num(19,6) WTax Base Amount
  WTAccAmnt Num(19,6) Accumulated Amount
  WTPercpAm Num(19,6) WTax Perception Amount
  WTPercent Num(19,6) WTax Rate

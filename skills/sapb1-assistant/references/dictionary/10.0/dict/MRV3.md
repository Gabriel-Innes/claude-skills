<!-- source: REFDB.chm (SAP Business One SDK 10.0 - Database Tables Reference) | version: SAP Business One 10.0 | verified: 2026-10-01 -->
# MRV3 - Inventory Revaluation SNB
Module: General | 17 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: DocEntry, BaseLine, LineNum
Fields (name type(len) description [values] ->parent table):
  DocEntry Int(11) Document Internal ID
  BaseLine Int(11) Base Row Number
  LineNum Int(11) Row Number
  SNBNum nVarChar(36) Serial and Batch Number
  AdmisDate Date(8) Admission Date
  ExpiryDate Date(8) Expiration Date
  CurrCost Num(19,6) Current Cost
  NewCost Num(19,6) New Cost
  DebCred Num(19,6) Debit Credit Value
  SNBOpenQty Num(19,6) SNB Open Quantity
  RToStock Num(19,6) Reval. Amount Posted to Stock
  SnbSysNum Int(11) SNB System Number
  SnbAbsEnt Int(11) SNB Abs. Entry
  SnbQty Num(19,6) SNB Quantity
  SnbCostT Num(19,6) SNB Cost Total
  SnbLotNum nVarChar(36) SNB Lot Number
  SnbMfn nVarChar(36) SNB Manufacture Attribute

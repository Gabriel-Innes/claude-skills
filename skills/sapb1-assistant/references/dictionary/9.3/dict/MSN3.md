<!-- source: erpref.com (schema IP: SAP) | version: SAP Business One 9.3 | verified: 2026-10-01 -->
# MSN3 - MRP Pegging Information
Module: MRP | 15 columns
Indexes (name: columns; first = primary key; U = unique) - WARNING: multi-column key order here is reversed vs SAP's 10.0 reference (read as a set; see references/dictionary/INDEX.md):
  PRIMARY U: LineID, AbsEntry
Fields (name type(len) description [values] ->parent table):
  AbsEntry Int(11) Internal Number
  ItemCode nVarChar(50) Item No. ->OITM
  PeriodID Int(11) Period ID
  Quantity Num(19,6) Quantity
  BaseEntry Int(11) Base Document Internal ID
  BaseLine Int(11) Base Row
  BaseObj nVarChar(20) Base Object Type
  BaseDocNum nVarChar(16) Base Document Number
  BaseDue Date(8) Base Due Date
  StockType VarChar(1) Stock Operation Type default=I [I=Stock Issue, R=Stock Receipt]
  LineID Int(11) Row Number
  ParentCode nVarChar(50) Parent Item No. ->OITM
  StartDate Date(8) Period Start Date
  EndDate Date(8) Period End Date
  WhsCode nVarChar(8) Warehouse Code ->OWHS

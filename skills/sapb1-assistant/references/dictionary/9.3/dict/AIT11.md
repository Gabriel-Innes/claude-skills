<!-- source: erpref.com (schema IP: SAP) | version: SAP Business One 9.3 | verified: 2026-10-01 -->
# AIT11 - Asset Item Period Control
Module: Inventory and Production | 8 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: LogInstanc, VisOrder, DprArea, PeriodCat, ItemCode
Fields (name type(len) description [values] ->parent table):
  ItemCode nVarChar(50) Item No. ->OITM
  PeriodCat nVarChar(10) Period Category
  DprArea nVarChar(15) Depreciation Area ->ODPA
  VisOrder Int(11) Visual Order
  DprSt VarChar(1) Depreciation Status default=Y [Y=Yes, N=No]
  factor Num(19,6) Factor
  LogInstanc Int(11) Log Instance default=0
  ActualUnit Int(11) Actual Units

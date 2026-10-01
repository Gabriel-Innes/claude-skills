<!-- source: erpref.com (schema IP: SAP) | version: SAP Business One 9.3 | verified: 2026-10-01 -->
# ITM7 - Asset Item Depreciation Params
Module: Inventory and Production | 17 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: DprArea, PeriodCat, ItemCode
Fields (name type(len) description [values] ->parent table):
  ItemCode nVarChar(50) Item No. ->OITM
  PeriodCat nVarChar(10) Period Category
  DprArea nVarChar(15) Depreciation Area ->ODPA
  VisOrder Int(11) Visual Order
  DprStart Date(8) Depreciation Start Date
  DprEnd Date(8) Depreciation End Date
  UsefulLife Int(11) Useful Life
  RemainLife Num(19,6) Remaining Life
  DprType nVarChar(15) Depreciation Type ->ODTP
  DprTypeC nVarChar(15) Depr. Type Calculation ->ODTP
  UsefulLfeC Int(11) Useful Life Calculation
  LogInstanc Int(11) Log Instance default=0
  ObjType nVarChar(20) Object default=4 ->ADP1
  RemainDays Num(19,6) Remaining Life in Days
  TotalUnits Int(11) Total Units in Life
  RemainUnit Int(11) Remaining Units
  StanUnit Int(11) Standard Units

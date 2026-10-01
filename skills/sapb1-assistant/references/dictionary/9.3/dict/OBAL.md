<!-- source: erpref.com (schema IP: SAP) | version: SAP Business One 9.3 | verified: 2026-10-01 -->
# OBAL - Opening Balances
Module: Marketing Documents | 8 columns
Indexes (name: columns; first = primary key; U = unique) - WARNING: multi-column key order here is reversed vs SAP's 10.0 reference (read as a set; see references/dictionary/INDEX.md):
  PRIMARY U: AbsEntry
  SECONDARY U: LayerID, DtSorting, EvalSystem, PeriodID, WhsCode, ItemCode
Fields (name type(len) description [values] ->parent table):
  AbsEntry Int(11) Internal Number
  ItemCode nVarChar(50) Item No. ->OITM
  WhsCode nVarChar(8) Warehouse Code ->OWHS
  PeriodID Int(11) Period Indicator ->BAL2
  EvalSystem VarChar(1) Valuation Method default=W [A=Moving Average, F=FIFO, W=Weighted Average]
  DtSorting VarChar(1) Date Sorting Method default=P [S=System Date, P=Posting Date, E=Effective Posting Date]
  LayerID Int(11) Layer ID default=-1
  CreateDate Date(8) Create Date

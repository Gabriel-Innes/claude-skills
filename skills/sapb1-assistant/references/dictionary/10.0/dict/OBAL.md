<!-- source: REFDB.chm (SAP Business One SDK 10.0 - Database Tables Reference) | version: SAP Business One 10.0 | verified: 2026-10-01 -->
# OBAL - Opening Balances
Module: Marketing Documents | 8 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: AbsEntry
  SECONDARY U: ItemCode, WhsCode, PeriodID, EvalSystem, DtSorting, LayerID
Fields (name type(len) description [values] ->parent table):
  AbsEntry Int(11) Internal Number
  ItemCode nVarChar(50) Item No. ->OITM
  WhsCode nVarChar(8) Warehouse Code ->OWHS
  PeriodID Int(11) Period Indicator ->BAL2
  EvalSystem VarChar(1) Valuation Method default=W [A=Moving Average, F=FIFO, W=Weighted Average]
  DtSorting VarChar(1) Date Sorting Method default=P [S=System Date, P=Posting Date, E=Effective Posting Date]
  LayerID Int(11) Layer ID default=-1
  CreateDate Date(8) Create Date

<!-- source: REFDB.chm (SAP Business One SDK 10.0 - Database Tables Reference) | version: SAP Business One 10.0 | verified: 2026-10-01 -->
# ODPV - Fixed Assets Depreciation Value
Module: Finance | 17 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: AbsEntry
  SECONDARY U: ItemCode, DprArea, PeriodCat, SubPeriod
Fields (name type(len) description [values] ->parent table):
  AbsEntry Int(11) Internal Number
  ItemCode nVarChar(50) Item Code ->OITM
  DprArea nVarChar(15) Depreciation Area ID ->ODPA
  PeriodCat nVarChar(10) Period Category
  FromDate Date(8) Period Start Date
  ToDate Date(8) Period To Date
  OrdDprPlan Num(19,6) Ordinary Depreciation Plan
  OrdDprPost Num(19,6) Ordinary Depreciation Posted
  OrdDprAct Num(19,6) Ordinary Depreciation Actual
  SpDprKey nVarChar(2) Special Depreciation Key ->ODPP
  SpDprPlan Num(19,6) Special Depreciation Plan
  SpDprPost Num(19,6) Special Depreciation Posted
  SpDprAct Num(19,6) Special Depreciation Actual
  SubPeriod Int(11) Sub-period
  OrdDprPln1 Num(19,6) Ordinary Depreciation Plan 1
  OrdDprPst1 Num(19,6) Ordinary Depreciation Posted 1
  OrdDprAct1 Num(19,6) Ordinary Depreciation Actual 1

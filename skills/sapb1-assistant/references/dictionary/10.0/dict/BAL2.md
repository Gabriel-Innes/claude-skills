<!-- source: REFDB.chm (SAP Business One SDK 10.0 - Database Tables Reference) | version: SAP Business One 10.0 | verified: 2026-10-01 -->
# BAL2 - Period indicators for opening Balance
Module: Marketing Documents | 5 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: PeriodID
  SECONDARY U: DateFrom, DateTo
Fields (name type(len) description [values] ->parent table):
  PeriodID Int(11) Period Indicator
  DateFrom Date(8) Date From
  DateTo Date(8) Date To
  FiscalYear Int(11) Fiscal Year
  CreateDate Date(8) Create Date

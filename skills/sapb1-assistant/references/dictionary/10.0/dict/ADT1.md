<!-- source: REFDB.chm (SAP Business One SDK 10.0 - Database Tables Reference) | version: SAP Business One 10.0 | verified: 2026-10-01 -->
# ADT1 - Depreciation Types - Rows - History
Module: Finance | 8 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: Code, Level, LogInstanc
Fields (name type(len) description [values] ->parent table):
  Code nVarChar(15) Code ->ODTP
  Level Int(11) Level
  Base nVarChar(3) Base default=APC [APC=Acquisition Value, NBV=Net Book Value]
  Years Int(11) Number of Years
  Percentage Num(19,6) Percentage
  LogInstanc Int(11) Log Instance default=0
  Amount Num(19,6) Amount
  SnapshotId Int(11) Snapshot ID default=0

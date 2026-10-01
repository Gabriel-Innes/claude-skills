<!-- source: erpref.com (schema IP: SAP) | version: SAP Business One 9.3 | verified: 2026-10-01 -->
# DTP1 - Depreciation Types - Rows
Module: Finance | 8 columns
Indexes (name: columns; first = primary key; U = unique) - WARNING: multi-column key order here is reversed vs SAP's 10.0 reference (read as a set; see references/dictionary/INDEX.md):
  PRIMARY U: Level, Code
Fields (name type(len) description [values] ->parent table):
  Code nVarChar(15) Code ->ODTP
  Level Int(11) Level
  Base nVarChar(3) Base default=APC [APC=Acquisition Value, NBV=Net Book Value]
  Years Int(11) Number of Years
  Percentage Num(19,6) Percentage
  LogInstanc Int(11) Log Instance default=0
  Amount Num(19,6) Amount
  SnapshotId Int(11) Snapshot ID default=0

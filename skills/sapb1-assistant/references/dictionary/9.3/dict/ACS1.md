<!-- source: erpref.com (schema IP: SAP) | version: SAP Business One 9.3 | verified: 2026-10-01 -->
# ACS1 - Asset Classes - Depreciation Areas
Module: Finance | 9 columns
Indexes (name: columns; first = primary key; U = unique) - WARNING: multi-column key order here is reversed vs SAP's 10.0 reference (read as a set; see references/dictionary/INDEX.md):
  PRIMARY U: LineNum, Code
  UNIQUE U: DprAreaID, Code
Fields (name type(len) description [values] ->parent table):
  Code nVarChar(20) Code ->OACS
  LineNum Int(11) Line Number
  DprAreaID nVarChar(15) Depreciation Area ID ->ODPA
  Active VarChar(1) Active default=Y [Y=Yes, N=No]
  AcctDtn nVarChar(15) Account Determination ->OADT
  DprTypID nVarChar(15) Depreciation Type ID ->ODTP
  UseLife Int(11) Useful Life
  LogInstanc Int(11) Log Instance default=0
  SnapshotId Int(11) Snapshot ID default=0

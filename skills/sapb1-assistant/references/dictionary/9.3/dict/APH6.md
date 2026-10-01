<!-- source: erpref.com (schema IP: SAP) | version: SAP Business One 9.3 | verified: 2026-10-01 -->
# APH6 - Project Management - Stages - Activities - History
Module: General | 7 columns
Indexes (name: columns; first = primary key; U = unique) - WARNING: multi-column key order here is reversed vs SAP's 10.0 reference (read as a set; see references/dictionary/INDEX.md):
  PRIMARY U: LogInstanc, LineID, AbsEntry
Fields (name type(len) description [values] ->parent table):
  AbsEntry Int(11) Internal Key ->PHA1
  LineID Int(11) Row No.
  StageID Int(11) Stage ID ->PHA1
  ACTIVITYID Int(11) Activity Number ->OCLG
  LogInstanc Int(11) Log Instance default=0
  Charged Num(19,6) Charged
  Chargeable VarChar(1) Chargeable [Yes/No] default=Y [Y=Yes, N=No]

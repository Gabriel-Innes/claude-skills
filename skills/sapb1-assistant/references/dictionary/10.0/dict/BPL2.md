<!-- source: REFDB.chm (SAP Business One SDK 10.0 - Database Tables Reference) | version: SAP Business One 10.0 | verified: 2026-10-01 -->
# BPL2 - Branch Tributary Info.
Module: Administration | 10 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: BPLId, TributID
Fields (name type(len) description [values] ->parent table):
  BPLId Int(11) BPL ID ->OBPL
  TributID Int(11) Tributary Info. ID
  TributType Int(11) Tributary Type default=-1 ->OBNI
  TTStartDat Date(8) Tributary Type Start Date
  TTEndDate Date(8) Tributary Type End Date
  TribRegCod Int(11) Tributary Regime Code default=-1 ->OBNI
  TRCStartD Date(8) Tributary Reg. Code Start Date
  TRCEndDate Date(8) Tributary Regime Code End Date
  LogInstanc Int(11) Log Instance default=0
  ObjType nVarChar(20) Object Type default=247 ->ADP1

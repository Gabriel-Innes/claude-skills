<!-- source: erpref.com (schema IP: SAP) | version: SAP Business One 9.3 | verified: 2026-10-01 -->
# ABP2 - Branch Tributary Info. Log
Module: Administration | 10 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: LogInstanc, TributID, BPLId
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

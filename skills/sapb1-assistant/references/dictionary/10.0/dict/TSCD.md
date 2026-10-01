<!-- source: REFDB.chm (SAP Business One SDK 10.0 - Database Tables Reference) | version: SAP Business One 10.0 | verified: 2026-10-01 -->
# TSCD - Schedules
Module: General | 7 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: SrvcName
  NAME_SCHED U: SrvcName, LastExDate
Fields (name type(len) description [values] ->parent table):
  SrvcName nVarChar(20) Service application name
  SchedType VarChar(1) Type of schedule default=P [P=Suspended / Paused, O=Once, S=Every X seconds, M=Every X minutes, D=Daily, W=Weekly, T=Monthly]
  SchedDate Date(8) Scheduled date
  SchedDay nVarChar(2) Scheduled day default=1
  Interval Int(11) Interval
  LastExDate Date(8) Last execution date
  AutoStart VarChar(1) Auto run when OS starts default=Y [Y=Yes, N=NO]

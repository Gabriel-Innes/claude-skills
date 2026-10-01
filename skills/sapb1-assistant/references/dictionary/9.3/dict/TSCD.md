<!-- source: erpref.com (schema IP: SAP) | version: SAP Business One 9.3 | verified: 2026-10-01 -->
# TSCD - Schedules
Module: General | 7 columns
Indexes (name: columns; first = primary key; U = unique) - WARNING: multi-column key order here is reversed vs SAP's 10.0 reference (read as a set; see references/dictionary/INDEX.md):
  PRIMARY U: SrvcName
  NAME_SCHED U: LastExDate, SrvcName
Fields (name type(len) description [values] ->parent table):
  SrvcName nVarChar(20) Service application name
  SchedType VarChar(1) Type of schedule default=P [P=Suspended / Paused, O=Once, S=Every X seconds, M=Every X minutes, D=Daily, W=Weekly, T=Monthly]
  SchedDate Date(8) Scheduled date
  SchedDay nVarChar(2) Scheduled day default=1
  Interval Int(11) Interval
  LastExDate Date(8) Last execution date
  AutoStart VarChar(1) Auto run when OS starts default=Y [Y=Yes, N=NO]

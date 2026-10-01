<!-- source: erpref.com (schema IP: SAP) | version: SAP Business One 9.3 | verified: 2026-10-01 -->
# SLOGR - SLOGR
Module: General | 8 columns
Indexes (name: columns; first = primary key; U = unique) - WARNING: multi-column key order here is reversed vs SAP's 10.0 reference (read as a set; see references/dictionary/INDEX.md):
  PRIMARY U: LogKey
Fields (name type(len) description [values] ->parent table):
  LogKey Identity(11) Table key
  CompName nVarChar(100) Computer Name
  LoginName nVarChar(100) Login Name
  ProcessID Int(11) Process ID
  LogDate Date(8) Log file date
  LogFile Text(16) Log file blob
  Archive Int(11) Archive type default=0 [1=AuditArchive, 0=NotArchive]
  CrashTime nVarChar(14) Time of the crash

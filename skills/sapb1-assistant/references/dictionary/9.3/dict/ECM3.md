<!-- source: erpref.com (schema IP: SAP) | version: SAP Business One 9.3 | verified: 2026-10-01 -->
# ECM3 - Statuses and Logs for Actions in Electronic Communication
Module: Reports | 15 columns
Indexes (name: columns; first = primary key; U = unique) - WARNING: multi-column key order here is reversed vs SAP's 10.0 reference (read as a set; see references/dictionary/INDEX.md):
  PRIMARY U: LogNum, AbsEntry
Fields (name type(len) description [values] ->parent table):
  AbsEntry Int(11) Internal ID ->ECM2
  LogNum Int(11) Log Number
  LogType VarChar(1) Log Type default=R [S=Send, R=Receive, I=Import, N=Note, W=Warning, E=Error]
  LogMessage Text(16) Log Message
  LogData Text(16) Log Data
  LogOpDate Date(8) Log Operation Date
  LogOpTS Int(11) Log Operation Time - Incl. Secs
  ExportFmt Int(11) Export Format ->OLLF
  UserSign Int(6) User Signature ->OUSR
  CreateDate Date(8) Creation Date
  CreateTS Int(11) Create Time - Incl. Secs
  UserSign2 Int(6) Updating User ->OUSR
  UpdateDate Date(8) Update Date
  UpdateTS Int(11) Update Time - Incl. Secs
  LogInstanc Int(6) Log Instance

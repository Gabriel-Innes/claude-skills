<!-- source: erpref.com (schema IP: SAP) | version: SAP Business One 9.3 | verified: 2026-10-01 -->
# SOUT - [SOUT]
Module: General | 12 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: LogNum
  STATUS: Status
Fields (name type(len) description [values] ->parent table):
  LogNum Int(11) ??' ?????
  Company nVarChar(128) Company
  USER_CODE nVarChar(8) User code
  Object Int(11) Object
  ObjectAbs Int(11) ObjectAbs
  SubDate Date(8) Submission date
  SubTime Int(6) Submission time
  ActDate Date(8) Action date
  ActTime Int(6) Action time
  Status VarChar(1) Status default=C [C=Check in, P=In process, E=Error, S=Success, I=Success with info]
  ErrCode Int(11) Error code
  ErrMessage Text(16) Error message

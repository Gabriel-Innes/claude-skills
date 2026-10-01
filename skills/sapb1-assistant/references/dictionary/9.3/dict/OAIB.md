<!-- source: erpref.com (schema IP: SAP) | version: SAP Business One 9.3 | verified: 2026-10-01 -->
# OAIB - Received Alerts
Module: Administration | 8 columns | ObjType: 82
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: UserSign, AlertCode
  USER: UserSign
  READ: WasRead
  DELETED: Deleted
Fields (name type(len) description [values] ->parent table):
  AlertCode Int(11) Alert Code ->OALR
  UserSign Int(6) User Signature ->OUSR
  Opened VarChar(1) Opened default=N [Y=Yes, N=No]
  RecDate Date(8) Receipt Date
  RecTime Int(6) Time Received
  WasRead VarChar(1) Read default=N [Y=Yes, N=No]
  Deleted VarChar(1) Deleted default=N [Y=Yes, N=No]
  Failed VarChar(1) Failed default=N [Y=Yes, N=No]

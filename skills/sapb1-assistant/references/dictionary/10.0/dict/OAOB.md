<!-- source: REFDB.chm (SAP Business One SDK 10.0 - Database Tables Reference) | version: SAP Business One 10.0 | verified: 2026-10-01 -->
# OAOB - Message Sent
Module: Administration | 5 columns | ObjType: 83
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: AlertCode, UserSign
  USER: UserSign
Fields (name type(len) description [values] ->parent table):
  AlertCode Int(11) Alert Code ->OALR
  SendDate Date(8) Date
  SendTime Int(6) Time
  WasSent VarChar(1) Sent default=N [Y=Yes, N=No]
  UserSign Int(6) User Signature ->OUSR

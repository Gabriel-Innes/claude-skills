<!-- source: erpref.com (schema IP: SAP) | version: SAP Business One 9.3 | verified: 2026-10-01 -->
# OAOB - Message Sent
Module: Administration | 5 columns | ObjType: 83
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: UserSign, AlertCode
  USER: UserSign
Fields (name type(len) description [values] ->parent table):
  AlertCode Int(11) Alert Code ->OALR
  SendDate Date(8) Date
  SendTime Int(6) Time
  WasSent VarChar(1) Sent default=N [Y=Yes, N=No]
  UserSign Int(6) User Signature ->OUSR

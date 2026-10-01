<!-- source: erpref.com (schema IP: SAP) | version: SAP Business One 9.3 | verified: 2026-10-01 -->
# RMSG - EditMode Messages
Module: General | 8 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: abs
  TO_WHO: toWho
  WHO_READ: msgRead, toWho
Fields (name type(len) description [values] ->parent table):
  abs Int(11) abs
  fromWho Int(11) from Who
  toWho Int(11) to Who
  date Date(8) date
  time Int(11) time
  loggedOnly VarChar(1) msg valid only f logged default=Y
  message nVarChar(250) message
  msgRead VarChar(1) was message read default=N

<!-- source: erpref.com (schema IP: SAP) | version: SAP Business One 9.3 | verified: 2026-10-01 -->
# OAT4 - Blanket Agreement - Recurring Transactions
Module: Business Partners | 3 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: RcpEntry, AgrNo
Fields (name type(len) description [values] ->parent table):
  AgrNo Int(11) Agreement No. ->OOAT
  RcpEntry Int(11) Recurring Template Entry ->ORCP
  LogInstanc Int(11) Log Instance default=0

<!-- source: erpref.com (schema IP: SAP) | version: SAP Business One 9.3 | verified: 2026-10-01 -->
# ACT2 - Service Contract - Recurring Transactions
Module: Service | 3 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: LogInstanc, RcpEntry, ContractID
Fields (name type(len) description [values] ->parent table):
  ContractID Int(11) Contract No. ->OCTR
  RcpEntry Int(11) Recurring Template Entry ->ORCP
  LogInstanc Int(11) Log Instance - History

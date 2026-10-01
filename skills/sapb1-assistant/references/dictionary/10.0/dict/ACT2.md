<!-- source: REFDB.chm (SAP Business One SDK 10.0 - Database Tables Reference) | version: SAP Business One 10.0 | verified: 2026-10-01 -->
# ACT2 - Service Contract - Recurring Transactions
Module: Service | 4 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: ContractID, RcpEntry, LogInstanc
Fields (name type(len) description [values] ->parent table):
  ContractID Int(11) Contract No. ->OCTR
  RcpEntry Int(11) Recurring Template Entry ->ORCP
  LogInstanc Int(11) Log Instance - History
  EncryptIV nVarChar(100) Encrypt IV

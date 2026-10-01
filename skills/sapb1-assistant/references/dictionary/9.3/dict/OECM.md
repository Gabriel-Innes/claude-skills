<!-- source: erpref.com (schema IP: SAP) | version: SAP Business One 9.3 | verified: 2026-10-01 -->
# OECM - Electronic Communication Types or Protocols
Module: Reports | 6 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: Code
Fields (name type(len) description [values] ->parent table):
  Code nVarChar(8) Communication Type or Protocol
  Descr nVarChar(200) Description
  LogInstanc Int(6) Log Instance
  UIOrder Int(6) UI Order
  StrIndex Int(6) String Index
  IsActive VarChar(1) Activation of Communication Type or Protocol default=N [Y=Yes, N=No]

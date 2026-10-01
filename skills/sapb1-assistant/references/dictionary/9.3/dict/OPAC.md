<!-- source: erpref.com (schema IP: SAP) | version: SAP Business One 9.3 | verified: 2026-10-01 -->
# OPAC - PAC Companies
Module: General | 5 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: PACCode
Fields (name type(len) description [values] ->parent table):
  PACCode nVarChar(16) PAC Code
  PACName nVarChar(100) PAC Name
  PublicKey Text(16) PAC Public Key
  UserSign Int(6) User Signature ->OUSR
  LogInstanc Int(11) Log Instance

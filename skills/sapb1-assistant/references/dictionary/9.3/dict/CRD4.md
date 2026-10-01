<!-- source: erpref.com (schema IP: SAP) | version: SAP Business One 9.3 | verified: 2026-10-01 -->
# CRD4 - Allowed WTax Codes for BP
Module: Business Partners | 3 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: WTCode, CardCode
Fields (name type(len) description [values] ->parent table):
  CardCode nVarChar(15) BP Code
  WTCode nVarChar(4) WTax Code
  LogInstanc Int(11) Log Instance default=0

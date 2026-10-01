<!-- source: erpref.com (schema IP: SAP) | version: SAP Business One 9.3 | verified: 2026-10-01 -->
# ACR4 - Allowed WTax Codes for BP - History
Module: Business Partners | 3 columns
Indexes (name: columns; first = primary key; U = unique) - WARNING: multi-column key order here is reversed vs SAP's 10.0 reference (read as a set; see references/dictionary/INDEX.md):
  PRIMARY U: LogInstanc, WTCode, CardCode
Fields (name type(len) description [values] ->parent table):
  CardCode nVarChar(15) BP Code
  WTCode nVarChar(4) WTax Code
  LogInstanc Int(11) Log Instance default=0

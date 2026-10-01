<!-- source: erpref.com (schema IP: SAP) | version: SAP Business One 9.3 | verified: 2026-10-01 -->
# CRD5 - BP Payment Dates
Module: Business Partners | 3 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: PmntDate, CardCode
Fields (name type(len) description [values] ->parent table):
  CardCode nVarChar(15) BP Code ->OCRD
  PmntDate nVarChar(2) Payment Date
  LogInstanc Int(11) Log Instance default=0

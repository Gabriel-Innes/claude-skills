<!-- source: erpref.com (schema IP: SAP) | version: SAP Business One 9.3 | verified: 2026-10-01 -->
# CRDC - BP - Communication Means
Module: General | 3 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: CommMeanId, CardCode
Fields (name type(len) description [values] ->parent table):
  CardCode nVarChar(15) BP Code ->OCRD
  CommMeanId Int(11) Communication Mean ID ->OCMM
  Select VarChar(1) Select [Y=Yes, N=No]

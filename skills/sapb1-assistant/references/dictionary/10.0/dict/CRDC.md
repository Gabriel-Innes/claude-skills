<!-- source: REFDB.chm (SAP Business One SDK 10.0 - Database Tables Reference) | version: SAP Business One 10.0 | verified: 2026-10-01 -->
# CRDC - BP - Communication Means
Module: General | 3 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: CardCode, CommMeanId
Fields (name type(len) description [values] ->parent table):
  CardCode nVarChar(15) BP Code ->OCRD
  CommMeanId Int(11) Communication Mean ID ->OCMM
  Select VarChar(1) Select [Y=Yes, N=No]

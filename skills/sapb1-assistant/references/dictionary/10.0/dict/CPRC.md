<!-- source: REFDB.chm (SAP Business One SDK 10.0 - Database Tables Reference) | version: SAP Business One 10.0 | verified: 2026-10-01 -->
# CPRC - Contact Persons - Communication Mean
Module: General | 5 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: CntctCode, CommMeanID
Fields (name type(len) description [values] ->parent table):
  CntctCode Int(11) Internal Number ->OCPR
  CommMeanID Int(11) Communication Mean ID ->OCMM
  Select VarChar(1) Select [Y=Yes, N=No]
  CardCode nVarChar(15) BP Code ->OCRD
  CntctName nVarChar(50) Contact Person Name ->OCPR

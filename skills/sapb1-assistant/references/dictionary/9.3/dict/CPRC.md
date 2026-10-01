<!-- source: erpref.com (schema IP: SAP) | version: SAP Business One 9.3 | verified: 2026-10-01 -->
# CPRC - Contact Persons - Communication Mean
Module: General | 3 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: CommMeanID, CntctCode
Fields (name type(len) description [values] ->parent table):
  CntctCode Int(11) Internal Number ->OCPR
  CommMeanID Int(11) Communication Mean ID ->OCMM
  Select VarChar(1) Select [Y=Yes, N=No]

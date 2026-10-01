<!-- source: REFDB.chm (SAP Business One SDK 10.0 - Database Tables Reference) | version: SAP Business One 10.0 | verified: 2026-10-01 -->
# OAT3 - Item Details: Activity
Module: Business Partners | 5 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: AgrNo, AgrLnNum, AgrEfctNum, ActivityID
Fields (name type(len) description [values] ->parent table):
  AgrNo Int(11) Agreement No. ->OOAT
  AgrLnNum Int(11) Agreement Line Number
  AgrEfctNum Int(11) Line Number
  ActivityID Int(11) Activity ID ->OCLG
  LogInstanc Int(11) Log Instance default=0

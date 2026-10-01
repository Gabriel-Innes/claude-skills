<!-- source: REFDB.chm (SAP Business One SDK 10.0 - Database Tables Reference) | version: SAP Business One 10.0 | verified: 2026-10-01 -->
# AOA3 - Item Details: Activity
Module: Business Partners | 5 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: AgrNo, AgrLnNum, AgrEfctNum, ActivityID, LogInstanc
Fields (name type(len) description [values] ->parent table):
  AgrNo Int(11) Agreement No. ->AOAT
  AgrLnNum Int(11) Agreement Item Row Number
  AgrEfctNum Int(11) Agreement Effective: Row No.
  ActivityID Int(11) Activity ID ->OCLG
  LogInstanc Int(11) Log Instance default=0

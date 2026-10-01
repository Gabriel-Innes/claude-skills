<!-- source: erpref.com (schema IP: SAP) | version: SAP Business One 9.3 | verified: 2026-10-01 -->
# AOA3 - Item Details: Activity
Module: Business Partners | 5 columns
Indexes (name: columns; first = primary key; U = unique) - WARNING: multi-column key order here is reversed vs SAP's 10.0 reference (read as a set; see references/dictionary/INDEX.md):
  PRIMARY U: LogInstanc, ActivityID, AgrEfctNum, AgrLnNum, AgrNo
Fields (name type(len) description [values] ->parent table):
  AgrNo Int(11) Agreement No. ->AOAT
  AgrLnNum Int(11) Agreement Item Row Number
  AgrEfctNum Int(11) Agreement Effective: Row No.
  ActivityID Int(11) Activity ID ->OCLG
  LogInstanc Int(11) Log Instance default=0

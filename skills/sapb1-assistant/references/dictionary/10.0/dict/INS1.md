<!-- source: REFDB.chm (SAP Business One SDK 10.0 - Database Tables Reference) | version: SAP Business One 10.0 | verified: 2026-10-01 -->
# INS1 - Customer Equipment Card - Multiple Business Partners
Module: Service | 3 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: InsID, BpCode
Fields (name type(len) description [values] ->parent table):
  InsID Int(11) Equipment Card No. ->OINS
  BpCode nVarChar(15) BP Code ->OCRD
  LogInstanc Int(11) Log Instance default=0

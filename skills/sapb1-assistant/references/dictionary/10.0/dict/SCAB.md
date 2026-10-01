<!-- source: REFDB.chm (SAP Business One SDK 10.0 - Database Tables Reference) | version: SAP Business One 10.0 | verified: 2026-10-01 -->
# SCAB - Appl CABs
Module: General | 8 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: Version
Fields (name type(len) description [values] ->parent table):
  Version Int(11) Version
  Flags nVarChar(50) Flags default=NNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN
  ApplCab Text(16) Appl. CAB
  DbCab Text(16) Metadata CAB
  ComOBSCab Text(16) Com OBS CAB
  ComUICab Text(16) Com UI CAB
  ApplCab64 Text(16) Appl. CAB (64bit)
  DbCab64 Text(16) Metadata CAB (64bit)

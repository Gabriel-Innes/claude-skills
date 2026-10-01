<!-- source: REFDB.chm (SAP Business One SDK 10.0 - Database Tables Reference) | version: SAP Business One 10.0 | verified: 2026-10-01 -->
# CSPI - Solution Packager Information
Module: Administration | 7 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: AbsEntry
Fields (name type(len) description [values] ->parent table):
  AbsEntry Int(11) absEntry
  Name nVarChar(50) Parameter Name
  Type nVarChar(20) Parameter Type
  Value Text(16) Parameter Value
  LstUpdDate Date(8) Last Update Date
  LstUpdTime Int(11) Last Update Time
  CheckSum nVarChar(50) Row Checksum

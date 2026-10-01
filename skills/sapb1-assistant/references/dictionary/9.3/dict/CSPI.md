<!-- source: erpref.com (schema IP: SAP) | version: SAP Business One 9.3 | verified: 2026-10-01 -->
# CSPI - Solution Packager Information
Module: Administration | 7 columns
Indexes (name: columns; first = primary key; U = unique) - WARNING: multi-column key order here is reversed vs SAP's 10.0 reference (read as a set; see references/dictionary/INDEX.md):
  PRIMARY U: AbsEntry
Fields (name type(len) description [values] ->parent table):
  AbsEntry Int(11) absEntry
  Name nVarChar(50) Parameter Name
  Type nVarChar(20) Parameter Type
  Value Text(16) Parameter Value
  LstUpdDate Date(8) Last Update Date
  LstUpdTime Int(11) Last Update Time
  CheckSum nVarChar(50) Row Checksum

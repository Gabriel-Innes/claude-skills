<!-- source: REFDB.chm (SAP Business One SDK 10.0 - Database Tables Reference) | version: SAP Business One 10.0 | verified: 2026-10-01 -->
# OCIP - Configuration of Integration Packages
Module: General | 5 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: AbsEntry
  CODE U: Code
Fields (name type(len) description [values] ->parent table):
  AbsEntry Int(11) Internal Number
  Code nVarChar(10) Package Code
  Name nVarChar(254) Package Name
  DsplID Int(11) Display Description ID
  IsEnable VarChar(1) Is Enabled

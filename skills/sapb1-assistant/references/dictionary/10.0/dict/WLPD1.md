<!-- source: REFDB.chm (SAP Business One SDK 10.0 - Database Tables Reference) | version: SAP Business One 10.0 | verified: 2026-10-01 -->
# WLPD1 - Fiori Launchpad Groups
Module: General | 6 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: ParentId, Guid
Fields (name type(len) description [values] ->parent table):
  ParentId nVarChar(40) Parent Id
  Guid nVarChar(40) Guid
  Order Int(11) Order
  GroupId nVarChar(40) Group Id
  GroupName nVarChar(100) Group Name
  Visible VarChar(1) Visible default=Y [Y=Yes, N=No]

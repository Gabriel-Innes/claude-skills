<!-- source: REFDB.chm (SAP Business One SDK 10.0 - Database Tables Reference) | version: SAP Business One 10.0 | verified: 2026-10-01 -->
# SWRS - 
Module: General | 5 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: ResourceID
Fields (name type(len) description [values] ->parent table):
  ResourceID Identity(11) Workflow Resource ID
  Name nVarChar(254) Workflow Resouce Name
  Version nVarChar(13) Resource Version
  DeploymtID Int(11) Deployment ID ->SWDP
  Bytes Text(16) Resource Library

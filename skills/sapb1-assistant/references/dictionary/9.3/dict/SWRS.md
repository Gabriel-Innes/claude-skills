<!-- source: erpref.com (schema IP: SAP) | version: SAP Business One 9.3 | verified: 2026-10-01 -->
# SWRS - SWRS
Module: General | 5 columns
Indexes (name: columns; first = primary key; U = unique) - WARNING: multi-column key order here is reversed vs SAP's 10.0 reference (read as a set; see references/dictionary/INDEX.md):
  PRIMARY U: ResourceID
Fields (name type(len) description [values] ->parent table):
  ResourceID Identity(11) Workflow Resource ID
  Name nVarChar(254) Workflow Resouce Name
  Version nVarChar(13) Resource Version
  DeploymtID Int(11) Deployment ID ->SWDP
  Bytes Text(16) Resource Library

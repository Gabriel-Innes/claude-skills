<!-- source: REFDB.chm (SAP Business One SDK 10.0 - Database Tables Reference) | version: SAP Business One 10.0 | verified: 2026-10-01 -->
# WSV1 - Web Client Smart View Filter
Module: General | 5 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: ParentId, Guid
Fields (name type(len) description [values] ->parent table):
  Guid nVarChar(40) GUID
  ParentId nVarChar(40) Parent Id ->OWSV
  FlterFld nVarChar(254) Filter Name
  BindField nVarChar(254) Bind Field
  CardId nVarChar(40) Card Id

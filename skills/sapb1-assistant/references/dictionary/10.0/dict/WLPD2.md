<!-- source: REFDB.chm (SAP Business One SDK 10.0 - Database Tables Reference) | version: SAP Business One 10.0 | verified: 2026-10-01 -->
# WLPD2 - Fiori Launchpad Tiles
Module: General | 5 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: RootId, ParentId, Guid
Fields (name type(len) description [values] ->parent table):
  RootId nVarChar(40) Root Guid
  ParentId nVarChar(40) Parent Id
  Guid nVarChar(40) Guid
  Order Int(11) Order
  TileId nVarChar(40) Tile Id

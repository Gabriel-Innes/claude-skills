<!-- source: erpref.com (schema IP: SAP) | version: SAP Business One 9.3 | verified: 2026-10-01 -->
# SFMD - SFMD
Module: General | 4 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: Version
Fields (name type(len) description [values] ->parent table):
  Version Int(11) Version
  Metadefs Text(16) Metadefs.bin
  ClusterID nVarChar(3) Cluster Identification
  PatchLevel nVarChar(50) Application Patch Level

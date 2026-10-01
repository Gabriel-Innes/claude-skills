<!-- source: erpref.com (schema IP: SAP) | version: SAP Business One 9.3 | verified: 2026-10-01 -->
# SINF - Server Info
Module: General | 11 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: Version
Fields (name type(len) description [values] ->parent table):
  Version Int(11) Version
  Flags nVarChar(100) Flags
  UpgCab Text(16) Upg CAB
  AppDate Date(8) Application Date
  ClusterID nVarChar(3) Cluster Identification
  AppTime Int(6) Application Time
  ShrPath Text(16) Shared folder path
  Algo Int(6) Encryption Algorithm.
  PatchLevel nVarChar(50) Application Patch Level
  BuildDesc nVarChar(50) Build Descriptor
  IsPALInit VarChar(1) Is PAL Initialize or Not default=N

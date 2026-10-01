<!-- source: erpref.com (schema IP: SAP) | version: SAP Business One 9.3 | verified: 2026-10-01 -->
# SEWH1 - SEWH1
Module: General | 8 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: ID, CompDbNam, MachineNam
Fields (name type(len) description [values] ->parent table):
  MachineNam nVarChar(254) Machine Name
  CompDbNam nVarChar(100) Company Db Name
  ID Int(11) AddOn ID
  Name nVarChar(40) AddOn Name
  Version nVarChar(13) AddOn Version
  Status nVarChar(50) AddOn Status
  InstStatus VarChar(1) AddOn Installation Status default=P [I=Installed, P=Pending]
  EwaSentDat nVarChar(10) EWA Sent Date

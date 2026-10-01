<!-- source: erpref.com (schema IP: SAP) | version: SAP Business One 9.3 | verified: 2026-10-01 -->
# OVTP - Vendor Type
Module: Business Partners | 4 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: ABSEntry
  TYPE: VendorType
Fields (name type(len) description [values] ->parent table):
  ABSEntry Int(11) Primary Key
  VendorType nVarChar(32) Vendor Type
  Descript nVarChar(120) Description
  Locked VarChar(1) Locked default=N

<!-- source: erpref.com (schema IP: SAP) | version: SAP Business One 9.3 | verified: 2026-10-01 -->
# OCFX - Cash Flow Forecast Object Types
Module: Administration | 4 columns
Indexes (name: columns; first = primary key; U = unique) - WARNING: multi-column key order here is reversed vs SAP's 10.0 reference (read as a set; see references/dictionary/INDEX.md):
  PRIMARY U: ObjType
Fields (name type(len) description [values] ->parent table):
  ObjType nVarChar(20) Object Type
  Level Int(11) Level
  ObjName nVarChar(100) Object Name
  Group nVarChar(2) Group

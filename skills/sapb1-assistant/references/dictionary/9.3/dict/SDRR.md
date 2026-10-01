<!-- source: erpref.com (schema IP: SAP) | version: SAP Business One 9.3 | verified: 2026-10-01 -->
# SDRR - Drag&Relate - Reports
Module: General | 3 columns
Indexes (name: columns; first = primary key; U = unique) - WARNING: multi-column key order here is reversed vs SAP's 10.0 reference (read as a set; see references/dictionary/INDEX.md):
  PRIMARY U: ServerType, ObjId
Fields (name type(len) description [values] ->parent table):
  ObjId nVarChar(4) Object ID
  ReportStr Text(16) Report String
  ServerType Int(11) Server Type default=0

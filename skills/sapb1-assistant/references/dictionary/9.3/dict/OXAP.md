<!-- source: erpref.com (schema IP: SAP) | version: SAP Business One 9.3 | verified: 2026-10-01 -->
# OXAP - XAPP Master Data
Module: General | 3 columns
Indexes (name: columns; first = primary key; U = unique) - WARNING: multi-column key order here is reversed vs SAP's 10.0 reference (read as a set; see references/dictionary/INDEX.md):
  PRIMARY U: AbsEntry
  NAME U: Name
Fields (name type(len) description [values] ->parent table):
  AbsEntry Int(11) Key of XAPP
  Name nVarChar(250) Name of XAPP
  Default VarChar(1) Is default default=N

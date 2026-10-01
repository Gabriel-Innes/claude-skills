<!-- source: erpref.com (schema IP: SAP) | version: SAP Business One 9.3 | verified: 2026-10-01 -->
# SWID - SWID
Module: General | 4 columns
Indexes (name: columns; first = primary key; U = unique) - WARNING: multi-column key order here is reversed vs SAP's 10.0 reference (read as a set; see references/dictionary/INDEX.md):
  PRIMARY U: Name
Fields (name type(len) description [values] ->parent table):
  Name nVarChar(200) Name
  Value Int(11) Value
  Rev Int(11) Revision
  LastUpdate nVarChar(50) Last update date and time

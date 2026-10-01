<!-- source: erpref.com (schema IP: SAP) | version: SAP Business One 9.3 | verified: 2026-10-01 -->
# OBOD - BIOD Master Data
Module: General | 6 columns
Indexes (name: columns; first = primary key; U = unique) - WARNING: multi-column key order here is reversed vs SAP's 10.0 reference (read as a set; see references/dictionary/INDEX.md):
  PRIMARY U: BIOD_ENTRY
  USERID: BIOD_UID
Fields (name type(len) description [values] ->parent table):
  BIOD_ENTRY Int(11) BIOD Key
  BIOD_UID Int(6) User ID
  BIOD_QID Int(11) Query Internal Key
  BIOD_QN nVarChar(100) Query Name
  BIOD_QLD Date(8) Last Upload Date
  BIOD_QLT Int(6) Last Upload Time

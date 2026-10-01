<!-- source: erpref.com (schema IP: SAP) | version: SAP Business One 9.3 | verified: 2026-10-01 -->
# QAG1 - Query Authorization Group Assignment
Module: General | 2 columns
Indexes (name: columns; first = primary key; U = unique) - WARNING: multi-column key order here is reversed vs SAP's 10.0 reference (read as a set; see references/dictionary/INDEX.md):
  PRIMARY U: CATEGORYID, AUTHGRPID
Fields (name type(len) description [values] ->parent table):
  AUTHGRPID Int(11) Query Authorization Group ID ->OQAG
  CATEGORYID Int(11) Category ID ->OQCN

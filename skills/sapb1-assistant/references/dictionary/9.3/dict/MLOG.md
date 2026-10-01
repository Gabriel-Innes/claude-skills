<!-- source: erpref.com (schema IP: SAP) | version: SAP Business One 9.3 | verified: 2026-10-01 -->
# MLOG - MLOG
Module: General | 7 columns
Indexes (name: columns; first = primary key; U = unique) - WARNING: multi-column key order here is reversed vs SAP's 10.0 reference (read as a set; see references/dictionary/INDEX.md):
  PRIMARY U: absId
Fields (name type(len) description [values] ->parent table):
  absId Int(11)
  userCode nVarChar(20)
  ipAddress nVarChar(20)
  updateDate Date(8)
  tableName nVarChar(10)
  operation VarChar(1) [C=Create, U=Update, D=Remove]
  objGuid nVarChar(36)

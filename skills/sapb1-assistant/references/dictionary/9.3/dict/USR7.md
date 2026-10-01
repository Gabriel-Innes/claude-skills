<!-- source: erpref.com (schema IP: SAP) | version: SAP Business One 9.3 | verified: 2026-10-01 -->
# USR7 - Group User Association
Module: General | 5 columns
Indexes (name: columns; first = primary key; U = unique) - WARNING: multi-column key order here is reversed vs SAP's 10.0 reference (read as a set; see references/dictionary/INDEX.md):
  PRIMARY U: GroupId, UserId
Fields (name type(len) description [values] ->parent table):
  UserId Int(6) User ID ->OUSR
  GroupId Int(6) Group ID ->OUGR
  Category nVarChar(155) Group Category
  StartDate Date(8) Start Date
  DueDate Date(8) Due Date

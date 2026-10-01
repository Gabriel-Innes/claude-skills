<!-- source: erpref.com (schema IP: SAP) | version: SAP Business One 9.3 | verified: 2026-10-01 -->
# UIC3 - Template User Customization
Module: General | 3 columns
Indexes (name: columns; first = primary key; U = unique) - WARNING: multi-column key order here is reversed vs SAP's 10.0 reference (read as a set; see references/dictionary/INDEX.md):
  PRIMARY U: UserID, TPLId
Fields (name type(len) description [values] ->parent table):
  TPLId Int(6) Template ID ->UICU
  UserID Int(6) User ID ->OUSR
  IsTemplate VarChar(1) Is Template

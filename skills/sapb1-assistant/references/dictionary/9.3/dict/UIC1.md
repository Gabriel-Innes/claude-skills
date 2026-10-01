<!-- source: erpref.com (schema IP: SAP) | version: SAP Business One 9.3 | verified: 2026-10-01 -->
# UIC1 - Customized Forms in Templates
Module: General | 5 columns
Indexes (name: columns; first = primary key; U = unique) - WARNING: multi-column key order here is reversed vs SAP's 10.0 reference (read as a set; see references/dictionary/INDEX.md):
  PRIMARY U: FormId, TPLId
Fields (name type(len) description [values] ->parent table):
  TPLId Int(6) Template ID ->UICU
  FormId nVarChar(20) Form ID
  Width Int(6) Form Width
  Height Int(6) Form Height
  MenuId nVarChar(20) Menu ID

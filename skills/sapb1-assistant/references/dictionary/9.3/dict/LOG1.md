<!-- source: erpref.com (schema IP: SAP) | version: SAP Business One 9.3 | verified: 2026-10-01 -->
# LOG1 - LOG1
Module: General | 4 columns
Indexes (name: columns; first = primary key; U = unique) - WARNING: multi-column key order here is reversed vs SAP's 10.0 reference (read as a set; see references/dictionary/INDEX.md):
  PRIMARY U: fldName, absId
Fields (name type(len) description [values] ->parent table):
  absId Int(11)
  fldName nVarChar(10)
  valFrom nVarChar(254)
  valTo nVarChar(254)

<!-- source: erpref.com (schema IP: SAP) | version: SAP Business One 9.3 | verified: 2026-10-01 -->
# SXRTE - XLR Terms
Module: General | 4 columns
Indexes (name: columns; first = primary key; U = unique) - WARNING: multi-column key order here is reversed vs SAP's 10.0 reference (read as a set; see references/dictionary/INDEX.md):
  PRIMARY U: Language, TermId
Fields (name type(len) description [values] ->parent table):
  TermId nVarChar(50) TermId
  Language Int(11) Language
  Type Int(11) Type
  Term Text(16) Term

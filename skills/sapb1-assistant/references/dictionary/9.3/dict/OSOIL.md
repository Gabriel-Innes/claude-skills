<!-- source: erpref.com (schema IP: SAP) | version: SAP Business One 9.3 | verified: 2026-10-01 -->
# OSOIL - Statement of Import Wizard Run
Module: Reports | 4 columns
Indexes (name: columns; first = primary key; U = unique) - WARNING: multi-column key order here is reversed vs SAP's 10.0 reference (read as a set; see references/dictionary/INDEX.md):
  PRIMARY U: SOIWNum
  SECONDARY U: AbsEntry
Fields (name type(len) description [values] ->parent table):
  SOIWNum nVarChar(100) Statement No.
  WizardId Int(11) Wizard ID
  SOINum Int(11) SOI
  AbsEntry Int(11) Abs Entry

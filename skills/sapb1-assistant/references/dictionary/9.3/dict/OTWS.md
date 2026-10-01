<!-- source: erpref.com (schema IP: SAP) | version: SAP Business One 9.3 | verified: 2026-10-01 -->
# OTWS - E-Tax Web Site
Module: Reports | 6 columns
Indexes (name: columns; first = primary key; U = unique) - WARNING: multi-column key order here is reversed vs SAP's 10.0 reference (read as a set; see references/dictionary/INDEX.md):
  PRIMARY U: AbsEntry
  TWSNAME: TwsName
Fields (name type(len) description [values] ->parent table):
  AbsEntry Int(6) E-Tax Internal ID
  TwsName nVarChar(64) E-Tax Web Site Name
  TwsURL Text(16) E-Tax Web Site URL
  TwsDescrip nVarChar(200) E-Tax Web Site Description
  UserSign Int(6) User Signature - Create ->OUSR
  UserSign2 Int(6) Updating User ->OUSR

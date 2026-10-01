<!-- source: REFDB.chm (SAP Business One SDK 10.0 - Database Tables Reference) | version: SAP Business One 10.0 | verified: 2026-10-01 -->
# OTWS - E-Tax Web Site
Module: Reports | 6 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: AbsEntry
  TWSNAME: TwsName
Fields (name type(len) description [values] ->parent table):
  AbsEntry Int(6) E-Tax Internal ID
  TwsName nVarChar(64) E-Tax Web Site Name
  TwsURL Text(16) E-Tax Web Site URL
  TwsDescrip nVarChar(200) E-Tax Web Site Description
  UserSign Int(6) User Signature - Create ->OUSR
  UserSign2 Int(6) Updating User ->OUSR

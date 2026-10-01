<!-- source: erpref.com (schema IP: SAP) | version: SAP Business One 9.3 | verified: 2026-10-01 -->
# LOCL - Localizations Table
Module: General | 7 columns
Indexes (name: columns; first = primary key; U = unique) - WARNING: multi-column key order here is reversed vs SAP's 10.0 reference (read as a set; see references/dictionary/INDEX.md):
  PRIMARY U: LocCode
  ABS_KEY U: AbsKey
Fields (name type(len) description [values] ->parent table):
  AbsKey Int(11) Abs Key
  LocCode nVarChar(2) Localization Code
  Name nVarChar(32) Name
  DfltLang Int(11) Default Language
  B5IColctn nVarChar(20) B5I Collection Name
  IncldInExp VarChar(1) Include In export default=N [Y=Yes, N=No]
  IncEnInExp VarChar(1) Include English In Export default=Y [Y=Yes, N=No]

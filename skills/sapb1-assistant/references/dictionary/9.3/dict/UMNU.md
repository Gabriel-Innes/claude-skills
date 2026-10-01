<!-- source: erpref.com (schema IP: SAP) | version: SAP Business One 9.3 | verified: 2026-10-01 -->
# UMNU - UMNU
Module: General | 10 columns
Indexes (name: columns; first = primary key; U = unique) - WARNING: multi-column key order here is reversed vs SAP's 10.0 reference (read as a set; see references/dictionary/INDEX.md):
  PRIMARY U: guid
  FATHER_ID: fatherId
Fields (name type(len) description [values] ->parent table):
  guid nVarChar(36) Guid
  fatherId nVarChar(36) Fathter Id
  lineNum Int(11) Line Num
  menuName nVarChar(254) Menu Name
  linkType VarChar(1) Link Type
  linkTo nVarChar(36) LinkTo
  icon Int(11) Icon
  locale nVarChar(254) Localization Flag
  mnuNameSid Int(11) Menu String Id
  linkChart nVarChar(36) Linked Chart Id

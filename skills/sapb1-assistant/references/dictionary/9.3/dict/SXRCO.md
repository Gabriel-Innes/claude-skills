<!-- source: erpref.com (schema IP: SAP) | version: SAP Business One 9.3 | verified: 2026-10-01 -->
# SXRCO - XLR Context
Module: General | 12 columns
Indexes (name: columns; first = primary key; U = unique) - WARNING: multi-column key order here is reversed vs SAP's 10.0 reference (read as a set; see references/dictionary/INDEX.md):
  PRIMARY U: ContextId
Fields (name type(len) description [values] ->parent table):
  ContextId Int(11) ContextId
  B1User nVarChar(50) B1User
  Password nVarChar(50) Password
  Language Int(11) Language
  Applicatio Int(11) ApplicationId
  LogonDate Date(8) LogonDate
  ExpiryDate Date(8) ExpiryDate
  Constrain nVarChar(250) Constraint
  DB nVarChar(250) DB
  ForceCust Int(11) ForceCustomConnect default=0
  Roles nVarChar(250) Roles
  InvalidTer Text(16) InvalidTerms

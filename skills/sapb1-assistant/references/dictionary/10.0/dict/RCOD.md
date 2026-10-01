<!-- source: REFDB.chm (SAP Business One SDK 10.0 - Database Tables Reference) | version: SAP Business One 10.0 | verified: 2026-10-01 -->
# RCOD - 
Module: General | 6 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: DocCode
Fields (name type(len) description [values] ->parent table):
  DocCode nVarChar(8) Base Doc Code
  TrnsDocCod nVarChar(8) Translation Doc Code
  ClntDocCod nVarChar(8) Client Doc Code
  LocMask nVarChar(100) Localization Mask
  LangMask nVarChar(100) Language Mask
  TranRequir VarChar(1) Translation Required

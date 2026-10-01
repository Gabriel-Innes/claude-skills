<!-- source: REFDB.chm (SAP Business One SDK 10.0 - Database Tables Reference) | version: SAP Business One 10.0 | verified: 2026-10-01 -->
# SEULA - 
Module: General | 5 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: Locale, EULAType
Fields (name type(len) description [values] ->parent table):
  Locale nVarChar(100) Localization
  EULAType VarChar(1) EULA type default=P [P=Productive, E=Evaluation]
  EULADoc Text(16) EULA doc
  Format nVarChar(50) format default=TXT [TXT=Text Format, PDF=PDF Format]
  CheckSum nVarChar(50) checksum

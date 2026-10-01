<!-- source: erpref.com (schema IP: SAP) | version: SAP Business One 9.3 | verified: 2026-10-01 -->
# SEULA - SEULA
Module: General | 5 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: EULAType, Locale
Fields (name type(len) description [values] ->parent table):
  Locale nVarChar(100) Localization
  EULAType VarChar(1) EULA type default=P [P=Productive, E=Evaluation]
  EULADoc Text(16) EULA doc
  Format nVarChar(50) format default=TXT [TXT=Text Format, PDF=PDF Format]
  CheckSum nVarChar(50) checksum

<!-- source: erpref.com (schema IP: SAP) | version: SAP Business One 9.3 | verified: 2026-10-01 -->
# SHLP - Server Help
Module: General | 4 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: LangCode
Fields (name type(len) description [values] ->parent table):
  LangCode nVarChar(5) Language Code
  HelpImage Text(16) Help Image
  Version Int(11) Help Version
  helpPath Text(16) Help Path

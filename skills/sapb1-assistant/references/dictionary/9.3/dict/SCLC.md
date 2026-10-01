<!-- source: erpref.com (schema IP: SAP) | version: SAP Business One 9.3 | verified: 2026-10-01 -->
# SCLC - SCLC
Module: General | 9 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: LangCode
Fields (name type(len) description [values] ->parent table):
  LangCode Int(11) Language Code
  BaseID Int(11) Base language ID
  HotKeyID Int(11) Hotkey language ID
  Updated Date(8) Date of update
  File Text(16) Localization Resource File
  FileName nVarChar(64) Localization file name
  UpdTime Int(11) Time of update
  Version nVarChar(32) B1 version
  PatchLevel nVarChar(16) Special build string

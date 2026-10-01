<!-- source: REFDB.chm (SAP Business One SDK 10.0 - Database Tables Reference) | version: SAP Business One 10.0 | verified: 2026-10-01 -->
# SXRSS - XLR Security Settings
Module: General | 6 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: SecuritySe
  second U: AppId, DatabaseId, ModuleId, Label
Fields (name type(len) description [values] ->parent table):
  SecuritySe Identity(11) SecuritySettingId
  AppId nVarChar(218) AppId
  DatabaseId nVarChar(218) DatabaseId
  ModuleId nVarChar(20) ModuleId default='' [''=]
  Label nVarChar(50) Label
  Value Text(16) Value

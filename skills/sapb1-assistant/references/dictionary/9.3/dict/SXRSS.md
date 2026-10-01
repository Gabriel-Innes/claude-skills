<!-- source: erpref.com (schema IP: SAP) | version: SAP Business One 9.3 | verified: 2026-10-01 -->
# SXRSS - XLR Security Settings
Module: General | 6 columns
Indexes (name: columns; first = primary key; U = unique) - WARNING: multi-column key order here is reversed vs SAP's 10.0 reference (read as a set; see references/dictionary/INDEX.md):
  PRIMARY U: SecuritySe
  second U: Label, ModuleId, DatabaseId, AppId
Fields (name type(len) description [values] ->parent table):
  SecuritySe Identity(11) SecuritySettingId
  AppId nVarChar(218) AppId
  DatabaseId nVarChar(218) DatabaseId
  ModuleId nVarChar(20) ModuleId default=' ['=]
  Label nVarChar(50) Label
  Value Text(16) Value

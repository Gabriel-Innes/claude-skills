<!-- source: erpref.com (schema IP: SAP) | version: SAP Business One 9.3 | verified: 2026-10-01 -->
# OCMN - Customized Menu
Module: Administration | 10 columns
Indexes (name: columns; first = primary key; U = unique) - WARNING: multi-column key order here is reversed vs SAP's 10.0 reference (read as a set; see references/dictionary/INDEX.md):
  PRIMARY U: GUID
  UID_KEY: MenuUID
Fields (name type(len) description [values] ->parent table):
  GUID nVarChar(32) GUID
  Name nVarChar(100) Menu Item Name
  Father nVarChar(32) Menu Parent GUID
  Type VarChar(1) Menu Type default=C [S=, A=, C=]
  SubMenu VarChar(1) Submenu Flag default=N [Y=, N=]
  MenuUID nVarChar(50) Menu UID
  ObjectType Int(11) Target Object Type
  ObjectKey nVarChar(200) Target Object ID
  PermFolder Int(11) Permission Folder ID
  SortOrder Int(11) Sort Order

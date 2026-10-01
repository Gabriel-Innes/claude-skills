<!-- source: erpref.com (schema IP: SAP) | version: SAP Business One 9.3 | verified: 2026-10-01 -->
# MABV - Menu Abbreviation
Module: Administration | 5 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: absEntry
  PKG_NAME U: pkgName
Fields (name type(len) description [values] ->parent table):
  absEntry Int(11) Internal Key
  pkgName nVarChar(200) Package Name
  fileName nVarChar(200) FileName
  imprtDate Date(8) Import Date
  pkgPath nVarChar(200) Package Path

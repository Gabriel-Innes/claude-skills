<!-- source: erpref.com (schema IP: SAP) | version: SAP Business One 9.3 | verified: 2026-10-01 -->
# OWPK - Dashboard Packages
Module: General | 19 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: AbsEntry
  CODE U: PackagCode
Fields (name type(len) description [values] ->parent table):
  AbsEntry Int(11) Internal Key
  PackagCode nVarChar(32) Package Code
  PackagName nVarChar(100) Package Name
  Note Text(16) Package Description
  Content Text(16) Package Content
  Author nVarChar(32) Creator
  Version nVarChar(13) Version
  CreateDate Date(8) Create Date
  CreateTime Int(6) Create Time
  IsSystem VarChar(1) Is System default=N [N=No, Y=Yes]
  PackagType VarChar(1) Package Type default=D [D=Dashboard, M=Mobile, P=Pervasive]
  ISIMDB VarChar(1) IS IMDB default=N [N=No, Y=Yes]
  StraType nVarChar(254) Strategy Type default=none
  StraPara nVarChar(254) Strategy Parameters
  SourceType nVarChar(20) Query Source Type default=normal
  ViewName nVarChar(250) View's Name
  ViewCtg nVarChar(250) View's Catalog
  ViewSyn nVarChar(250) View's Synonym
  Viewid Int(11) Query Number

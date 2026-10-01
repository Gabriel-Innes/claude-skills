<!-- source: REFDB.chm (SAP Business One SDK 10.0 - Database Tables Reference) | version: SAP Business One 10.0 | verified: 2026-10-01 -->
# OTRN - Multilingual Service Table
Module: Administration | 7 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: AbsEntry
  CATCODE U: Category, PriCode, SecCode
Fields (name type(len) description [values] ->parent table):
  AbsEntry Int(11) Doc. Entry
  Category nVarChar(6) Category [CRRpt=CR Report, Menu=Menu Item, EFM=EFM Item]
  PriCode nVarChar(128) Primary Code
  SecCode nVarChar(128) Secondary Code
  SourceLang Int(11) Source Language
  CreateDate Date(8) Create Date
  UpdateDate Date(8) Update Date

<!-- source: REFDB.chm (SAP Business One SDK 10.0 - Database Tables Reference) | version: SAP Business One 10.0 | verified: 2026-10-01 -->
# OSVT - Define Summary VAT Report Type
Module: Finance | 4 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: AbsEntry
  NAME U: Name
Fields (name type(len) description [values] ->parent table):
  AbsEntry Int(11) VAT Report Type ID
  Name nVarChar(254) Summary VAT Report Type
  Descript nVarChar(254) Description
  NameDesc nVarChar(254) Name & Desc

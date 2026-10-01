<!-- source: REFDB.chm (SAP Business One SDK 10.0 - Database Tables Reference) | version: SAP Business One 10.0 | verified: 2026-10-01 -->
# OCIF - Configuration of Intrastat Fields
Module: Administration | 6 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: AbsEntry
Fields (name type(len) description [values] ->parent table):
  AbsEntry Int(11) Internal Key
  ISTable nVarChar(4) Intrastat Wizard Table
  ISField nVarChar(10) Intrastat Wizard Field Alias
  FieldDesc nVarChar(200) Field Description
  FlLocation nVarChar(200) Field Location
  FldSource nVarChar(200) Source of the Field Value

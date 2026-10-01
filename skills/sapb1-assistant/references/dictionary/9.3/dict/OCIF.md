<!-- source: erpref.com (schema IP: SAP) | version: SAP Business One 9.3 | verified: 2026-10-01 -->
# OCIF - Configuration of Intrastat Fields
Module: Administration | 6 columns
Indexes (name: columns; first = primary key; U = unique) - WARNING: multi-column key order here is reversed vs SAP's 10.0 reference (read as a set; see references/dictionary/INDEX.md):
  PRIMARY U: AbsEntry
Fields (name type(len) description [values] ->parent table):
  AbsEntry Int(11) Internal Key
  ISTable nVarChar(4) Intrastat Wizard Table
  ISField nVarChar(10) Intrastat Wizard Field Alias
  FieldDesc nVarChar(200) Field Description
  FlLocation nVarChar(200) Field Location
  FldSource nVarChar(200) Source of the Field Value

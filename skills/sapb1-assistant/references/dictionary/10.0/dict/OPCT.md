<!-- source: REFDB.chm (SAP Business One SDK 10.0 - Database Tables Reference) | version: SAP Business One 10.0 | verified: 2026-10-01 -->
# OPCT - Process Checklist Template
Module: Administration | 4 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: DocEntry
  TMPLCODE U: TmplCode
Fields (name type(len) description [values] ->parent table):
  DocEntry Int(11) Internal Number
  TmplCode nVarChar(15) Template Primary Key
  TmplName nVarChar(100) Template Name
  XMLFile Text(16) XML File Contents

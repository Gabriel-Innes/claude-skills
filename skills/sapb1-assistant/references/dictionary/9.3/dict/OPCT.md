<!-- source: erpref.com (schema IP: SAP) | version: SAP Business One 9.3 | verified: 2026-10-01 -->
# OPCT - Process Checklist Template
Module: Administration | 4 columns
Indexes (name: columns; first = primary key; U = unique) - WARNING: multi-column key order here is reversed vs SAP's 10.0 reference (read as a set; see references/dictionary/INDEX.md):
  PRIMARY U: DocEntry
  TMPLCODE U: TmplCode
Fields (name type(len) description [values] ->parent table):
  DocEntry Int(11) Internal Number
  TmplCode nVarChar(15) Template Primary Key
  TmplName nVarChar(100) Template Name
  XMLFile Text(16) XML File Contents

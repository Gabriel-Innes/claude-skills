<!-- source: erpref.com (schema IP: SAP) | version: SAP Business One 9.3 | verified: 2026-10-01 -->
# OTPL - Import Template
Module: Administration | 4 columns
Indexes (name: columns; first = primary key; U = unique) - WARNING: multi-column key order here is reversed vs SAP's 10.0 reference (read as a set; see references/dictionary/INDEX.md):
  PRIMARY U: TplNum
  CODE U: TplType, TplCode
Fields (name type(len) description [values] ->parent table):
  TplNum Int(11) Template Number
  TplName nVarChar(100) Template Name
  TplType nVarChar(3) Template Type [T=Target BPs, B=BP, I=Items, F=Fixed Asset]
  TplCode nVarChar(20) Template Code

<!-- source: erpref.com (schema IP: SAP) | version: SAP Business One 9.3 | verified: 2026-10-01 -->
# STA1 - Valid Period
Module: Administration | 5 columns
Indexes (name: columns; first = primary key; U = unique) - WARNING: multi-column key order here is reversed vs SAP's 10.0 reference (read as a set; see references/dictionary/INDEX.md):
  PRIMARY U: EfctDate, SttType, StaCode
Fields (name type(len) description [values] ->parent table):
  StaCode nVarChar(8) Tax Parameter Code ->OSTA
  SttType Int(11) Tax Type ->OSTT
  EfctDate Date(8) Effective From
  Rate Num(19,6) Rate
  TaaSUpdate Date(8) Last Update By TaaS

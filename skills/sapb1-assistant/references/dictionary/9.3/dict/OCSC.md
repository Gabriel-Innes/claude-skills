<!-- source: erpref.com (schema IP: SAP) | version: SAP Business One 9.3 | verified: 2026-10-01 -->
# OCSC - Crystal Server Configuration
Module: Administration | 7 columns
Indexes (name: columns; first = primary key; U = unique) - WARNING: multi-column key order here is reversed vs SAP's 10.0 reference (read as a set; see references/dictionary/INDEX.md):
  PRIMARY U: DocEntry
Fields (name type(len) description [values] ->parent table):
  DocEntry Int(11) CSC Abs. Entry
  Name nVarChar(100) Server Name
  User nVarChar(30) Logon User Code
  Password nVarChar(254) Logon User Password
  URL nVarChar(200) URL
  IsDefault VarChar(1) Is Default default=N [Y=Yes, N=No]
  Port nVarChar(20) Port default=8080

<!-- source: erpref.com (schema IP: SAP) | version: SAP Business One 9.3 | verified: 2026-10-01 -->
# SEWSY - SEWSY
Module: General | 6 columns
Indexes (name: columns; first = primary key; U = unique) - WARNING: multi-column key order here is reversed vs SAP's 10.0 reference (read as a set; see references/dictionary/INDEX.md):
  PRIMARY U: S_USER
Fields (name type(len) description [values] ->parent table):
  S_USER nVarChar(16) Absolute Key
  SmpSendAdd nVarChar(254) Smp Server URL
  SmpInboAdd nVarChar(254) Smp user Inbox URL
  CollecData VarChar(1) Communication and trigger flag default=N [Y=CollectData, N=DontCollectData]
  FindSolAdd nVarChar(254) Find Solution URL
  FeedOptAdd nVarChar(254) Feedback Option URL

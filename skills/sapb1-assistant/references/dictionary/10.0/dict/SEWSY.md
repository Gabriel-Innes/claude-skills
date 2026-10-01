<!-- source: REFDB.chm (SAP Business One SDK 10.0 - Database Tables Reference) | version: SAP Business One 10.0 | verified: 2026-10-01 -->
# SEWSY - 
Module: General | 6 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: S_USER
Fields (name type(len) description [values] ->parent table):
  S_USER nVarChar(16) Absolute Key
  SmpSendAdd nVarChar(254) Smp Server URL
  SmpInboAdd nVarChar(254) Smp user Inbox URL
  CollecData VarChar(1) Communication and trigger flag default=N [Y=CollectData, N=DontCollectData]
  FindSolAdd nVarChar(254) Find Solution URL
  FeedOptAdd nVarChar(254) Feedback Option URL

<!-- source: REFDB.chm (SAP Business One SDK 10.0 - Database Tables Reference) | version: SAP Business One 10.0 | verified: 2026-10-01 -->
# OFAT - Office 365 Authorization Token
Module: General | 5 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: ID
Fields (name type(len) description [values] ->parent table):
  ID nVarChar(254) ID
  USER_ID nVarChar(254) User ID
  OFUSERNAME nVarChar(254) Office User Name
  AUTH_TOKEN Text(16) Authorization Token
  ID_TOKEN Text(16) ID Token

<!-- source: REFDB.chm (SAP Business One SDK 10.0 - Database Tables Reference) | version: SAP Business One 10.0 | verified: 2026-10-01 -->
# RGRP - users groups
Module: General | 3 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: GroupCode
  NAME U: GroupName
Fields (name type(len) description [values] ->parent table):
  GroupCode Int(11) Group Code
  GroupName nVarChar(20) Group Name
  Perms nVarChar(250) Permissions

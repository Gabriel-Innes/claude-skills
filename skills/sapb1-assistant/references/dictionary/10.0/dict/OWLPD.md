<!-- source: REFDB.chm (SAP Business One SDK 10.0 - Database Tables Reference) | version: SAP Business One 10.0 | verified: 2026-10-01 -->
# OWLPD - Launchpad
Module: General | 5 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: Guid
Fields (name type(len) description [values] ->parent table):
  Guid nVarChar(40) Guid
  UserId Int(11) User Id
  ThemeId nVarChar(254) Theme Id
  DisQikView VarChar(1) Display Quick View or not default=N [Y=Yes, N=No]
  NtfShowDay Int(11) Notification Show Days Setting

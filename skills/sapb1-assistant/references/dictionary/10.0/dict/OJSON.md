<!-- source: REFDB.chm (SAP Business One SDK 10.0 - Database Tables Reference) | version: SAP Business One 10.0 | verified: 2026-10-01 -->
# OJSON - JSON Content Repository
Module: General | 5 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: Guid
  INDEX1 U: Type, Index1
Fields (name type(len) description [values] ->parent table):
  Guid nVarChar(40) Guid
  Type VarChar(1) Type [F=Form Preference]
  Index1 nVarChar(254) User-Defined Indexes
  Content Text(16) JSON Content
  UserSign Int(6) User Signature ->OUSR

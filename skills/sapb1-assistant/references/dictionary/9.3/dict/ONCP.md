<!-- source: erpref.com (schema IP: SAP) | version: SAP Business One 9.3 | verified: 2026-10-01 -->
# ONCP - New Cockpit Table
Module: General | 14 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: AbsEntry
  NAME U: Owner, Name
Fields (name type(len) description [values] ->parent table):
  AbsEntry Int(11) Internal Number
  Name nVarChar(100) Name
  Owner Int(11) Owner ->OUSR
  GroupId Int(11) Group ID
  CreateDate Date(8) Create Date
  UpdateDate Date(8) Update Date
  IsPublic VarChar(1) Public default=N [Y=, N=]
  Pubby nVarChar(30) Published By
  PubDate Date(8) Publication Date
  Type VarChar(1) Type default=T [U=User, T=Template]
  Descr nVarChar(100) Description
  Date Date(8) Publication Date
  Time Int(6) Publication Time
  Mnfacturer nVarChar(50) Provider

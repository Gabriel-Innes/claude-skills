<!-- source: erpref.com (schema IP: SAP) | version: SAP Business One 9.3 | verified: 2026-10-01 -->
# OCPT - Cockpit Main Table
Module: General | 18 columns | ObjType: 1210000000
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: AbsEntry
  CODE U: UserSign, Code
  NAME U: UserSign, Name
Fields (name type(len) description [values] ->parent table):
  AbsEntry Int(11) Internal Number
  Code Int(6) Cockpit Code
  Name nVarChar(20) Name
  Descr nVarChar(100) Description
  IsDefault VarChar(1) Is Default default=N [Y=, N=]
  UserSign Int(6) User ID ->OUSR
  IsPublic VarChar(1) Public default=N [Y=, N=]
  Strategy nVarChar(20) Layout Strategy
  _Top Int(11) Client Top
  _Left Int(11) Client Left
  _Width Int(11) Client Width
  _Height Int(11) Client Height
  Date Date(8) Publication Date
  Time Int(6) Publication Time
  Mnfacturer nVarChar(50) Provider
  Pubby nVarChar(30) Published By
  Disabled VarChar(1) Disabled default=N [Y=, N=]
  Type VarChar(1) Type default=U [U=User, T=Template]

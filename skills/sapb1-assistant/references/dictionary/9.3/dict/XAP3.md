<!-- source: erpref.com (schema IP: SAP) | version: SAP Business One 9.3 | verified: 2026-10-01 -->
# XAP3 - XAP Filter
Module: General | 6 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: AbsEntry
Fields (name type(len) description [values] ->parent table):
  AbsEntry Int(11) Key of XAPP filter
  XAPEntry Int(11) Foreign key of XAPP
  Name nVarChar(250) Name of filter
  Type nVarChar(250) Type of filter
  Method nVarChar(250) Filter method
  MultiValue VarChar(1) Allow multiple value

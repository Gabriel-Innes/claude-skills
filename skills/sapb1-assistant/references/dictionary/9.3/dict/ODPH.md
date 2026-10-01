<!-- source: erpref.com (schema IP: SAP) | version: SAP Business One 9.3 | verified: 2026-10-01 -->
# ODPH - Template for Demand Planning
Module: MRP | 5 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: AbsEntry
Fields (name type(len) description [values] ->parent table):
  AbsEntry Int(11) Template Internal Number
  UserSign nVarChar(50) User Signature
  TmpltName nVarChar(100) Template Name
  TmpltCnt Text(16) Template Content
  CrtDate Date(8) Create Date

<!-- source: erpref.com (schema IP: SAP) | version: SAP Business One 9.3 | verified: 2026-10-01 -->
# OIRC - Interactive Report Category
Module: Reports | 10 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: CategoryId
Fields (name type(len) description [values] ->parent table):
  CategoryId Int(11) Category Id
  ParentId Int(11) Parent Category Id default=-1
  Name nVarChar(254) Category Name
  ResKey nVarChar(128) Resource Key
  Comment nVarChar(254) Comment
  System VarChar(1) System default=N
  CreateBy nVarChar(25) Created By
  CreateDate Date(8) Creation Timestamp
  ModifyBy nVarChar(25) Modified By
  ModifyDate Date(8) Modification Timestamp

<!-- source: REFDB.chm (SAP Business One SDK 10.0 - Database Tables Reference) | version: SAP Business One 10.0 | verified: 2026-10-01 -->
# RLCK - resource locks table
Module: General | 7 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: resType, masterKey
Fields (name type(len) description [values] ->parent table):
  resType Int(11) Resource Type default=1 [1=form resource, 3=Grid resource, 5=String list resource, 18=Report]
  masterKey nVarChar(64) Master Key
  wrkstation nVarChar(250) Work Station
  userSign Int(11) User Sign
  date Date(8) Date
  time Int(11) Time
  count Int(11) Locks Count default=1

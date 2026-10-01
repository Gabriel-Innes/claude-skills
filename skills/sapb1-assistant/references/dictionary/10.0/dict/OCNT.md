<!-- source: REFDB.chm (SAP Business One SDK 10.0 - Database Tables Reference) | version: SAP Business One 10.0 | verified: 2026-10-01 -->
# OCNT - Counties
Module: Administration | 8 columns | ObjType: 265
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: AbsId
  UNIQUE U: Code, Country, State
Fields (name type(len) description [values] ->parent table):
  AbsId Int(11) Auto Key
  Code nVarChar(7) County Code
  Country nVarChar(3) Country/Region ->OCST
  State nVarChar(3) State ->OCST
  Name nVarChar(100) County Name
  TaxZone VarChar(1) Tax Free Zone default=N [Y=Yes, N=No]
  IbgeCode nVarChar(10) IBGE Code
  GiaCode nVarChar(10) GIA Code

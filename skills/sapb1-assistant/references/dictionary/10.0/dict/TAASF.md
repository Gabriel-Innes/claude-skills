<!-- source: REFDB.chm (SAP Business One SDK 10.0 - Database Tables Reference) | version: SAP Business One 10.0 | verified: 2026-10-01 -->
# TAASF - Result of TaaS Tax Code Fix
Module: Reports | 11 columns
Indexes (name: columns; first = primary key; U = unique):
  DUMMY U: LogInstanc, Internal
Fields (name type(len) description [values] ->parent table):
  LogInstanc Int(11) Log Instance
  Internal Int(11) Internal Number
  TaxCode nVarChar(8) Tax Code
  DocDate Date(8) Doc. Date
  StaCode nVarChar(8) Tax Authorities Code
  StaType Int(11) Tax Authorities Type
  OldRate Num(19,6) Old Rate
  NewRate Num(19,6) New Rate
  FixType VarChar(1) Fix Type
  IsOK VarChar(1) Is OK
  Descr nVarChar(254) Description

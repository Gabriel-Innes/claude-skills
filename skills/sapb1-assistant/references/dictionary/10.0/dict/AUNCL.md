<!-- source: REFDB.chm (SAP Business One SDK 10.0 - Database Tables Reference) | version: SAP Business One 10.0 | verified: 2026-10-01 -->
# AUNCL - PEPPOL BIS Code Lists - Log
Module: Reports | 11 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: AbsEntry, LogInstanc
  IsDefault: IsDefault
Fields (name type(len) description [values] ->parent table):
  AbsEntry Int(11) Internal Number
  Codelist Int(11) Code List [1=Order Type Code, 2=Delivery Type Code, 3=Invoice Type Code, 4=Credit Note Type Code, 5=Standard Item Type Identification Code, 6=Item Commodity Classification Code]
  Code nVarChar(20) Code
  Descrip nVarChar(254) Description
  SchemaCode nVarChar(20) Schema Code
  SchemaDesc nVarChar(254) Schema Description
  LogInstanc Int(11) Log Instance default=0
  UpdateDate Date(8) Date of Update
  UserSign Int(6) User Signature ->OUSR
  UserSign2 Int(6) Updating User ->OUSR
  IsDefault VarChar(1) Is Default default=N [Y=Yes, N=No]

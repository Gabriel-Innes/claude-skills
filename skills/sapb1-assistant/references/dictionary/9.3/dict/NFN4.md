<!-- source: erpref.com (schema IP: SAP) | version: SAP Business One 9.3 | verified: 2026-10-01 -->
# NFN4 - Manual Nota Fiscal Number
Module: Administration | 12 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: CardCode, SeqCode, Model, SubStr, SeriesStr, Serial, ObjectCode
Fields (name type(len) description [values] ->parent table):
  ObjectCode nVarChar(20) Document ->ONFN
  SeqCode Int(6) Sequence Code
  SeqName nVarChar(8) Seq Name
  Serial Int(11) Serial Number
  SeriesStr nVarChar(3) Series String
  SubStr nVarChar(3) Subseries String
  DocSubType nVarChar(2) Document Sub-Type default=--
  Model nVarChar(6) Nota Fiscal Model ->ONFM
  CardCode nVarChar(15) Customer/Vendor Code default=- ->OCRD
  DocEntry Int(11) Document Abs. Entry
  DocNumber Int(11) Document Number
  IsReusable VarChar(1) Is Reusable default=N [Y=Yes, N=No]

<!-- source: REFDB.chm (SAP Business One SDK 10.0 - Database Tables Reference) | version: SAP Business One 10.0 | verified: 2026-10-01 -->
# OTCN - Tracking Note
Module: General | 7 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: AbsEntry
  CCD U: CCDNum, DirectImp
Fields (name type(len) description [values] ->parent table):
  AbsEntry Int(11) Abs. Entry
  CCDNum nVarChar(40) CCD Number
  Date Date(8) Date
  CustTerm nVarChar(15) Customs Terminal
  CntrOrigin nVarChar(3) Country/Region of Origin
  DirectImp VarChar(1) Direct Import default=N [Y=Yes, N=No]
  CardCode nVarChar(15) BP Code

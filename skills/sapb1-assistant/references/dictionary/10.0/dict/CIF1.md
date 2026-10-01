<!-- source: REFDB.chm (SAP Business One SDK 10.0 - Database Tables Reference) | version: SAP Business One 10.0 | verified: 2026-10-01 -->
# CIF1 - Country Specific Information
Module: Administration | 7 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: FldAbsEnt, Country, TransCRY
Fields (name type(len) description [values] ->parent table):
  FldAbsEnt Int(11) Field ID ->OCIF
  Country nVarChar(3) Country/Region Code ->OCRY
  TransCRY nVarChar(3) Transaction Country/Region default=XX
  IsMandImp VarChar(1) Field is mandatory for import [Y=Yes, N=No]
  IsMandExp VarChar(1) Field is mandatory for export [Y=Yes, N=No]
  IsReqAllIm VarChar(1) Field is required for import default=N [Y=Yes, N=No]
  IsReqAllEx VarChar(1) Field is required for export default=N [Y=Yes, N=No]

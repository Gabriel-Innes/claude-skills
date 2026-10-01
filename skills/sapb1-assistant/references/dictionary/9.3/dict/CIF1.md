<!-- source: erpref.com (schema IP: SAP) | version: SAP Business One 9.3 | verified: 2026-10-01 -->
# CIF1 - Country Specific Information
Module: Administration | 7 columns
Indexes (name: columns; first = primary key; U = unique) - WARNING: multi-column key order here is reversed vs SAP's 10.0 reference (read as a set; see references/dictionary/INDEX.md):
  PRIMARY U: TransCRY, Country, FldAbsEnt
Fields (name type(len) description [values] ->parent table):
  FldAbsEnt Int(11) Field ID ->OCIF
  Country nVarChar(3) Country Code ->OCRY
  TransCRY nVarChar(3) Transaction Country default=XX
  IsMandImp VarChar(1) Field is mandatory for import [Y=Yes, N=No]
  IsMandExp VarChar(1) Field is mandatory for export [Y=Yes, N=No]
  IsReqAllIm VarChar(1) Field is required for import default=N [Y=Yes, N=No]
  IsReqAllEx VarChar(1) Field is required for export default=N [Y=Yes, N=No]

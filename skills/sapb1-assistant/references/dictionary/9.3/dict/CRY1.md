<!-- source: erpref.com (schema IP: SAP) | version: SAP Business One 9.3 | verified: 2026-10-01 -->
# CRY1 - Country Combination Settings
Module: Administration | 3 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: TransCRY, Country
Fields (name type(len) description [values] ->parent table):
  Country nVarChar(3) Country Code ->OCRY
  TransCRY nVarChar(3) Transaction Country ->OCRY
  EnableIST VarChar(1) Enable Intrastat Transactions [Y=Yes, N=No]

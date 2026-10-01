<!-- source: REFDB.chm (SAP Business One SDK 10.0 - Database Tables Reference) | version: SAP Business One 10.0 | verified: 2026-10-01 -->
# CRY1 - Country Combination Settings
Module: Administration | 3 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: Country, TransCRY
Fields (name type(len) description [values] ->parent table):
  Country nVarChar(3) Country/Region Code ->OCRY
  TransCRY nVarChar(3) Transaction Country/Region ->OCRY
  EnableIST VarChar(1) Enable Intrastat Transactions [Y=Yes, N=No]

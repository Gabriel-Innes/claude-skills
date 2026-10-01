<!-- source: REFDB.chm (SAP Business One SDK 10.0 - Database Tables Reference) | version: SAP Business One 10.0 | verified: 2026-10-01 -->
# OKPF - KPI Factor
Module: Finance | 5 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: FactorId
Fields (name type(len) description [values] ->parent table):
  FactorId nVarChar(3) KPI Factor No.
  FactorName nVarChar(100) KPI Factor Name
  CatId Int(6) Numerator
  TemplateId Int(11) Template
  IsSys VarChar(1) Is System [Y=Yes, N=No]

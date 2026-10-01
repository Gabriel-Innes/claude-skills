<!-- source: erpref.com (schema IP: SAP) | version: SAP Business One 9.3 | verified: 2026-10-01 -->
# ODIM - Cost Accounting Dimension
Module: Finance | 4 columns | ObjType: 251
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: DimCode
  DIM_KEY: DimName
Fields (name type(len) description [values] ->parent table):
  DimCode Int(6) Dimension Code
  DimName nVarChar(15) Dimension Name
  DimActive VarChar(1) Activated? [Y/N] default=N [Y=Yes, N=No]
  DimDesc nVarChar(50) Dimension Description

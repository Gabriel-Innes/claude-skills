<!-- source: REFDB.chm (SAP Business One SDK 10.0 - Database Tables Reference) | version: SAP Business One 10.0 | verified: 2026-10-01 -->
# OSTQ - Inventory Valuation Utility Queries
Module: Inventory and Production | 5 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: AbsEntry
Fields (name type(len) description [values] ->parent table):
  AbsEntry Int(11) Internal Number
  QueryNAme nVarChar(100) Query Name
  QueryStr Text(16) Query String
  Severity VarChar(1) Inventory Valuation Query Seve default=E [W=Warning if fails, E=Error if fails]
  QueryGroup VarChar(1) Query Group default=B [B=Before Recalculation, A=After Recalculation, T=Year Transfer]

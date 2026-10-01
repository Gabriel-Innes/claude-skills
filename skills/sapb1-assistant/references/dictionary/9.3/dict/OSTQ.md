<!-- source: erpref.com (schema IP: SAP) | version: SAP Business One 9.3 | verified: 2026-10-01 -->
# OSTQ - Inventory Valuation Utility Queries
Module: Inventory and Production | 5 columns
Indexes (name: columns; first = primary key; U = unique) - WARNING: multi-column key order here is reversed vs SAP's 10.0 reference (read as a set; see references/dictionary/INDEX.md):
  PRIMARY U: AbsEntry
Fields (name type(len) description [values] ->parent table):
  AbsEntry Int(11) Internal Number
  QueryNAme nVarChar(100) Query Name
  QueryStr Text(16) Query String
  Severity VarChar(1) Inventory Valuation Query Seve default=E [W=Warning if fails, E=Error if fails]
  QueryGroup VarChar(1) Query Group default=B [B=Before Recalculation, A=After Recalculation, T=Year Transfer]

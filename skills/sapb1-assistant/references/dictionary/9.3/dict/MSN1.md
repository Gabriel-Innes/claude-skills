<!-- source: erpref.com (schema IP: SAP) | version: SAP Business One 9.3 | verified: 2026-10-01 -->
# MSN1 - MRP Scenarios - Warehouses Array
Module: MRP | 5 columns
Indexes (name: columns; first = primary key; U = unique) - WARNING: multi-column key order here is reversed vs SAP's 10.0 reference (read as a set; see references/dictionary/INDEX.md):
  PRIMARY U: WhsCode, AbsEntry
Fields (name type(len) description [values] ->parent table):
  AbsEntry Int(11) Internal Number ->OMSN
  WhsCode nVarChar(8) Warehouse Code ->OWHS
  ReqSel VarChar(1) Requirement Selection default=Y [Y=Yes, N=No]
  InvtSel VarChar(1) Inventory Selection default=Y [Y=Yes, N=No]
  ExtIvntSel VarChar(1) Existing Inventory Selection default=Y [Y=Yes, N=No]

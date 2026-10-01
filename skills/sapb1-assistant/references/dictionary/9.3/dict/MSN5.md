<!-- source: erpref.com (schema IP: SAP) | version: SAP Business One 9.3 | verified: 2026-10-01 -->
# MSN5 - MRP-Specific Document
Module: MRP | 5 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: DocSubType, DocEntry, DocType, AbsEntry
Fields (name type(len) description [values] ->parent table):
  AbsEntry Int(11) Internal Number
  DocType nVarChar(20) Document Type
  DocEntry Int(11) Document Entry
  Selected VarChar(1) Selected default=Y [Y=Yes, N=No]
  DocSubType nVarChar(2) Document Sub-Type default=--

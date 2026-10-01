<!-- source: erpref.com (schema IP: SAP) | version: SAP Business One 9.3 | verified: 2026-10-01 -->
# TRS1 - Tax Report Saving Object - Approved Documents
Module: Reports | 11 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: LineID, AbsEntry
  SECONDARY U: PayDocEntr, PayDocType, PayLineID, MeansType, ApDocOrdNo, ApDocEntry, ApDocType, AbsEntry
Fields (name type(len) description [values] ->parent table):
  AbsEntry Int(11) Internal Number ->OTRS
  ObjType nVarChar(20) Object Type
  LineID Int(11) Internal Row Number
  ApDocType nVarChar(20) Approved Document Type
  ApDocEntry Int(11) Approved Document Key
  ApDocOrdNo Int(11) Appr. Doc. Ordinal Number default=-1
  ApDocAdRef Int(11) Appr. Doc. Additional Reference default=-1
  MeansType Int(11) Payment Means Type default=-1
  PayLineID Int(11) Payment Means Line ID default=-1
  PayDocType Int(11) Payment Document Type default=-1
  PayDocEntr Int(11) Payment Document Entry default=-1

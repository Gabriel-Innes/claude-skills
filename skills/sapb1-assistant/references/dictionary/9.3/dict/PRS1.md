<!-- source: erpref.com (schema IP: SAP) | version: SAP Business One 9.3 | verified: 2026-10-01 -->
# PRS1 - Detail Lines of Print Sequence Definition
Module: Reports | 10 columns
Indexes (name: columns; first = primary key; U = unique) - WARNING: multi-column key order here is reversed vs SAP's 10.0 reference (read as a set; see references/dictionary/INDEX.md):
  PRIMARY U: LineNum, SeqID
Fields (name type(len) description [values] ->parent table):
  SeqID Int(11) Internal Number
  LineNum Int(6) Row Number
  ObjectID Int(11) Document Object ID
  LaytCode nVarChar(8) Report Code
  NumCopy Int(6) Number of Copies
  UsrQuery Int(11) User Query to Customize
  SubDocType Int(6) Document Subtype
  Printer nVarChar(100) Printer
  Prtr1st nVarChar(100) Printer for First Page
  Use1stPrtr VarChar(1) Use 1st Page Printer default=N [Y=Yes, N=No]

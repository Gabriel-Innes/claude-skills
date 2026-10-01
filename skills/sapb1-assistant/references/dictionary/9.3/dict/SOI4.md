<!-- source: erpref.com (schema IP: SAP) | version: SAP Business One 9.3 | verified: 2026-10-01 -->
# SOI4 - Statement of Import - Invoices
Module: Reports | 9 columns
Indexes (name: columns; first = primary key; U = unique) - WARNING: multi-column key order here is reversed vs SAP's 10.0 reference (read as a set; see references/dictionary/INDEX.md):
  PRIMARY U: DocEntry, DocType, SOINum, WizardId
Fields (name type(len) description [values] ->parent table):
  WizardId Int(11) Wizard ID
  SOINum Int(11) Statement No.
  DocType Int(11) Document Type
  DocEntry Int(11) Document Abs Entry
  DocNum Int(11) Doc. No.
  DocDate Date(8) Posting Date
  TaxDate Date(8) Document Date
  NumAtCard nVarChar(100) BP Reference No.
  InvEntry Int(11) Invoice Abs Entry ->OINV

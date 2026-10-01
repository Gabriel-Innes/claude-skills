<!-- source: erpref.com (schema IP: SAP) | version: SAP Business One 9.3 | verified: 2026-10-01 -->
# TRB4 - Tax Report Wizard - Selected Tax Entries
Module: Reports | 4 columns
Indexes (name: columns; first = primary key; U = unique) - WARNING: multi-column key order here is reversed vs SAP's 10.0 reference (read as a set; see references/dictionary/INDEX.md):
  PRIMARY U: TaxLine, TaxEntry, TaxSrcType, AbsEntry
Fields (name type(len) description [values] ->parent table):
  AbsEntry Int(11) Internal Number ->OTRB
  TaxSrcType Int(11) Tax Source Object TYpe default=10000011 [10000011=VAT Transactions, 243000003=Brazil - Tax Adjustment]
  TaxEntry Int(11) Tax Entry
  TaxLine Int(11) Tax Line

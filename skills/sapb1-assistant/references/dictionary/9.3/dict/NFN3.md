<!-- source: erpref.com (schema IP: SAP) | version: SAP Business One 9.3 | verified: 2026-10-01 -->
# NFN3 - Assigned Nota Fiscal Series
Module: Administration | 3 columns
Indexes (name: columns; first = primary key; U = unique) - WARNING: multi-column key order here is reversed vs SAP's 10.0 reference (read as a set; see references/dictionary/INDEX.md):
  PRIMARY U: SeqCode, DocSubType, ObjectCode
  SEQ: SeqCode
Fields (name type(len) description [values] ->parent table):
  ObjectCode nVarChar(20) Document ->ONFN
  SeqCode Int(6) Sequence Code default=0
  DocSubType nVarChar(2) VAT Code for Tax Invoice Rpt default=--

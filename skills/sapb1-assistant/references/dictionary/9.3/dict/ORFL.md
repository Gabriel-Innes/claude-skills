<!-- source: erpref.com (schema IP: SAP) | version: SAP Business One 9.3 | verified: 2026-10-01 -->
# ORFL - Already Displayed 347, 349 and WTax Reports
Module: Reports | 6 columns | ObjType: 179
Indexes (name: columns; first = primary key; U = unique) - WARNING: multi-column key order here is reversed vs SAP's 10.0 reference (read as a set; see references/dictionary/INDEX.md):
  PRIMARY U: OrdinalNum, TaxCode, LineNum, DocType, ReportType, DocEntry
Fields (name type(len) description [values] ->parent table):
  ReportType Int(11) Report Type [1=347, 2=349, 3=WT, 4=O & P, 5=Annual List, 6=Tax Report]
  DocType nVarChar(20) Document Type [13=Invoice, 14=Revert Invoice, 18=Purchase, 19=Revert purchase, 203=A/R Down Payment, 204=A/P Down Payment]
  DocEntry Int(11) Document Internal ID
  LineNum Int(11) Row No.
  TaxCode nVarChar(8) Tax Code
  OrdinalNum Int(11) Ordinal Num (BTF & Cancelled) default=-1

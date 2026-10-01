<!-- source: erpref.com (schema IP: SAP) | version: SAP Business One 9.3 | verified: 2026-10-01 -->
# AWH1 - Tax Definition
Module: Finance | 15 columns
Indexes (name: columns; first = primary key; U = unique) - WARNING: multi-column key order here is reversed vs SAP's 10.0 reference (read as a set; see references/dictionary/INDEX.md):
  PRIMARY U: LogInstanc, LineNum, WTCode
Fields (name type(len) description [values] ->parent table):
  WTCode nVarChar(4) WTax Code ->OWHT
  EffecDate Date(8) Effective from
  Rate Num(19,6) Rate
  LogInstanc Int(11) Log Instance default=0
  TdsRate Num(19,6) TDS Rate
  SurRate Num(19,6) Surcharge Rate
  CessRate Num(19,6) Cess Rate
  HscRate Num(19,6) HSC Rate
  PmntTerms Int(6) Payment Terms ->OCTG
  LineNum Int(11) Row Number
  IgstRate Num(19,6) IGST Rate
  CgstRate Num(19,6) CGST Rate
  SgstRate Num(19,6) SGST Rate
  UtgstRate Num(19,6) UTGST Rate
  CsgstRate Num(19,6) Cess GST Rate

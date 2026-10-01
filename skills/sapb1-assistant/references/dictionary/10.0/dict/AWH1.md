<!-- source: REFDB.chm (SAP Business One SDK 10.0 - Database Tables Reference) | version: SAP Business One 10.0 | verified: 2026-10-01 -->
# AWH1 - Tax Definition
Module: Finance | 21 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: WTCode, LineNum, LogInstanc
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
  UomEntry Int(11) UoM Entry ->OUOM
  UoMCode nVarChar(20) UoM Code
  FixedAmnt Num(19,6) Fixed Amount
  Currency nVarChar(3) Fixed Amount Currency ->OCRN
  ItrNCRate Num(19,6) TDS ITR Noncompliance Rate
  PanNCRate Num(19,6) TDS PAN Noncompliance Rate

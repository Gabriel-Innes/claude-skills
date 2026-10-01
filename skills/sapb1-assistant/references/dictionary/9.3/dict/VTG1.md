<!-- source: erpref.com (schema IP: SAP) | version: SAP Business One 9.3 | verified: 2026-10-01 -->
# VTG1 - Tax Definition
Module: Finance | 9 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: EffecDate, Code
Fields (name type(len) description [values] ->parent table):
  Code nVarChar(8) Group Code
  EffecDate Date(8) Effective From
  Rate Num(19,6) Rate
  EquVatPr Num(19,6) Equalization Tax %
  MinAmount Num(19,6) Minimum Stamp Tax Amount
  FixedAmout Num(19,6) Fixed Stamp Tax Amount
  TaxType VarChar(1) Tax Type (VAT or Stamp) default=V [V=VAT, S=Stamp]
  LogInstanc Int(11) Log Instance default=0
  DatevCode Int(6) DATEV Code

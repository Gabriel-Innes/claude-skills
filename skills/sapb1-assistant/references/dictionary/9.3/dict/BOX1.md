<!-- source: erpref.com (schema IP: SAP) | version: SAP Business One 9.3 | verified: 2026-10-01 -->
# BOX1 - Box Definition - Rows
Module: Finance | 9 columns
Indexes (name: columns; first = primary key; U = unique) - WARNING: multi-column key order here is reversed vs SAP's 10.0 reference (read as a set; see references/dictionary/INDEX.md):
  PRIMARY U: BosCode, SeqNum, ReportType, BoxCode
Fields (name type(len) description [values] ->parent table):
  BoxCode nVarChar(30) Group Code
  BoxMember nVarChar(30) Box Code ->OBOX
  VATMember nVarChar(8) VAT Group ->OVTG
  SeqNum Int(11) Sequence Number
  FormulSign VarChar(1) Formula Sign default=P [P=+, M=-]
  ReportType VarChar(1) Report Type default=B [B=Box Declaration, S=BAS Reporting]
  EffecDate Date(8) Effective From
  TaxType VarChar(1) Acquisition / Reverse Tax Type default=B [I=Input Tax, O=Output Tax, B=Input Tax and Output Tax]
  BosCode Int(11) Box Set Code ->OBOS

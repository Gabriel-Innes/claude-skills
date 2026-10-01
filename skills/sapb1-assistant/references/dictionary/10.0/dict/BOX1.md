<!-- source: REFDB.chm (SAP Business One SDK 10.0 - Database Tables Reference) | version: SAP Business One 10.0 | verified: 2026-10-01 -->
# BOX1 - Box Definition - Rows
Module: Finance | 9 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: BoxCode, ReportType, SeqNum, BosCode
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

<!-- source: erpref.com (schema IP: SAP) | version: SAP Business One 9.3 | verified: 2026-10-01 -->
# BGT2 - Budget - Cost Accounting
Module: Finance | 9 columns
Indexes (name: columns; first = primary key; U = unique) - WARNING: multi-column key order here is reversed vs SAP's 10.0 reference (read as a set; see references/dictionary/INDEX.md):
  PRIMARY U: DimCode, OcrCode, BudgId
Fields (name type(len) description [values] ->parent table):
  BudgId Int(11) Budget Key ->OBGT
  OcrCode nVarChar(8) Factor Code ->OOCR
  DimCode Int(6) In Which Dimension ->ODIM
  Instance Int(11) Instance default=1 ->OBGS
  DebLTotal Num(19,6) Tot. Annu. Budgt Debit (LC)
  CredLTotal Num(19,6) Tot. Annu. Budgt Credit (LC)
  DebSTotal Num(19,6) Tot. Annu. Budgt Debit (SC)
  CredSTotal Num(19,6) Tot. Annu. Budgt Credit (SC)
  UserSign Int(6) User Signature ->OUSR

<!-- source: REFDB.chm (SAP Business One SDK 10.0 - Database Tables Reference) | version: SAP Business One 10.0 | verified: 2026-10-01 -->
# OCDC - Cash Discount
Module: Finance | 7 columns | ObjType: 133
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: Code
Fields (name type(len) description [values] ->parent table):
  Code nVarChar(20) Cash Discount Code
  TableDesc nVarChar(100) Cash Discount Name
  ByDate VarChar(1) By Date default=N [Y=Yes, N=No]
  Freight VarChar(1) Freight default=N [Y=Yes, N=]
  Tax VarChar(1) Tax default=N [Y=Yes, N=No]
  VatCrctn VarChar(1) VAT Correction default=N [Y=Yes, N=No]
  BaseDate VarChar(1) Base Date default=P [P=Posting Date, S=System Date, T=Document Date, C=Closing Date]

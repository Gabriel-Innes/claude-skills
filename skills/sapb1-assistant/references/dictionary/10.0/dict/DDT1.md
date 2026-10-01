<!-- source: REFDB.chm (SAP Business One SDK 10.0 - Database Tables Reference) | version: SAP Business One 10.0 | verified: 2026-10-01 -->
# DDT1 - Withholding Tax Deduction Hierarchy - Rows
Module: Business Partners | 6 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: DdtKey, LineNum
Fields (name type(len) description [values] ->parent table):
  DdtKey Int(11) Hierarchy Key ->ODDT
  LineNum Int(11) Row Number
  DdctPrcnt Num(19,6) Deduction %
  MaxSum Num(19,6) Maximum Total
  DataSource VarChar(1) Data Source default=N [N=Unknown, I=Interface, U=Update, M=Import, O=DI API, S=Service Layer, W=Web Client, A=Doc. Generation Wizard, D=Data Doc., P=Partner Implementation, T=Year Transfer]
  UserSign Int(6) User Signature ->OUSR

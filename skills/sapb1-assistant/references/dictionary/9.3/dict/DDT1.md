<!-- source: erpref.com (schema IP: SAP) | version: SAP Business One 9.3 | verified: 2026-10-01 -->
# DDT1 - Withholding Tax Deduction Hierarchy - Rows
Module: Business Partners | 6 columns
Indexes (name: columns; first = primary key; U = unique) - WARNING: multi-column key order here is reversed vs SAP's 10.0 reference (read as a set; see references/dictionary/INDEX.md):
  PRIMARY U: LineNum, DdtKey
Fields (name type(len) description [values] ->parent table):
  DdtKey Int(11) Hierarchy Key ->ODDT
  LineNum Int(11) Row Number
  DdctPrcnt Num(19,6) Deduction %
  MaxSum Num(19,6) Maximum Total
  DataSource VarChar(1) Data Source default=N [N=Unknown, I=Interface, U=Update, M=Import, O=DI API, A=Doc. Generation Wizard, D=Data Doc., P=Partner Implementation, T=Year Transfer]
  UserSign Int(6) User Signature ->OUSR

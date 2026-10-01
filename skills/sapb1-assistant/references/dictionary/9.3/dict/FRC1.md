<!-- source: erpref.com (schema IP: SAP) | version: SAP Business One 9.3 | verified: 2026-10-01 -->
# FRC1 - Extend Cat. f. Financial Rep.
Module: Finance | 12 columns
Indexes (name: columns; first = primary key; U = unique) - WARNING: multi-column key order here is reversed vs SAP's 10.0 reference (read as a set; see references/dictionary/INDEX.md):
  PRIMARY U: VisOrder, AcctCode, CatId, TemplateId
  ACCNT_CODE: AcctCode
Fields (name type(len) description [values] ->parent table):
  CatId Int(6) Numerator
  TemplateId Int(11) Template ->OFRT
  AcctCode nVarChar(15) Account Code ->OACT
  VisOrder Int(6) Display Order
  CFWId Int(11) Cash Flow Line Item ID ->OCFW
  CalcMethod nVarChar(30) Calculation Method [BOP=Beginning of Period, EOP=End of Period, CPID=Current Period In Debit, CPIC=Current Period In Credit, CPIB=Current Period In Both]
  SlpCode Int(11) Sales Unit Code ->OSLP
  PrcCode nVarChar(8) Cost Center Code ->OPRC
  CalMethod2 nVarChar(30) Calculation Method 2
  CalMethod3 nVarChar(30) Calculation Method 3
  Linked VarChar(1) Linked default=B [B=Balance, D=Debit, C=Credit]
  Sign VarChar(1) Sign default=E [E=, P=Positive, N=Negative]

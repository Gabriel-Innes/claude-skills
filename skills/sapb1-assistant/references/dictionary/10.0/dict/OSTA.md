<!-- source: REFDB.chm (SAP Business One SDK 10.0 - Database Tables Reference) | version: SAP Business One 10.0 | verified: 2026-10-01 -->
# OSTA - Sales Tax Authorities
Module: Administration | 36 columns | ObjType: 126
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: Code, Type
Fields (name type(len) description [values] ->parent table):
  Code nVarChar(8) Code
  Name nVarChar(100) Name
  Rate Num(19,6) Rate
  SalesTax nVarChar(15) Sales Tax Account ->OACT
  UseTax nVarChar(15) Use Tax Account ->OACT
  Type Int(11) Type ->OSTT
  UserSign Int(6) User Signature ->OUSR
  PurchTax nVarChar(15) Purchasing Tax Account ->OACT
  deferrAcct nVarChar(15) Deferred Tax Account ->OACT
  NonDdctPrc Num(19,6) Non Deductible %
  NonDdctAct nVarChar(15) Non Deductible Account ->OACT
  TaxInPrice VarChar(1) Included in Price default=N [Y=Yes, N=No]
  Exempt VarChar(1) Exempt default=N [Y=Yes, N=No]
  APExpAct nVarChar(15) Purchasing Tax Expense Account ->OACT
  ARExpAct nVarChar(15) Sales Tax Expense Account ->OACT
  CredBala Num(19,6) Credit Balance: Raw Material
  CredFG Num(19,6) Credit for Finished Goods
  CredCG Num(19,6) Credit for Capital Goods
  InGrossRev VarChar(1) Included in Gross Revenue default=N [Y=Yes, N=No]
  EfctDate Date(8) Effective From
  SvcTaxCr Num(19,6) Credit for Service Tax
  MinAmount Num(19,6) Min. Taxable Amount
  MaxAmount Num(19,6) Max. Taxable Amount
  FlatAmount Num(19,6) Flat Tax Amount
  TextCode Int(6) Text Code
  UnencumTax VarChar(1) Unencumbered Tax default=N [Y=Yes, N=No]
  TaxOnRI VarChar(1) Tax On Reserve Invoice default=N [Y=Yes, N=No]
  DIOTRptTyp VarChar(1) DIOT Report Type [A=15% or 16% VAT, B=15% or 16% VAT on Import, C=Exempt on Import, D=0% VAT, E=Exempt, F=VAT on Returns, Discounts, and Rebates, G=Stimulus for Northern Border Region]
  IsSystem VarChar(1) Is System Tax Jurisdiction default=N [Y=Yes, N=No]
  RvsCrgPrc Num(19,6) Reverse Charge %
  InFirstIns VarChar(1) Included in First Installment default=N [Y=Yes, N=No]
  SaleTaxRCM nVarChar(15) Sales Tax RCM Account ->OACT
  SaleRCMClr nVarChar(15) Sales Tax RCM Clearing Account ->OACT
  VatExempt VarChar(1) Apply VAT Exemption default=N [Y=Yes, N=No]
  VatExmPrc Num(19,6) VAT Exemption %
  VatExmBase Num(19,6) Base VAT %

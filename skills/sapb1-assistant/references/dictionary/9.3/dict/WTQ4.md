<!-- source: erpref.com (schema IP: SAP) | version: SAP Business One 9.3 | verified: 2026-10-01 -->
# WTQ4 - Inventory Transfer Request - Tax Amount per Document
Module: Inventory and Production | 55 columns
Indexes (name: columns; first = primary key; U = unique) - WARNING: multi-column key order here is reversed vs SAP's 10.0 reference (read as a set; see references/dictionary/INDEX.md):
  PRIMARY U: LogInstanc, ObjectType, LineSeq, DocEntry
  SCONDARY: staType, StaCode, StcCode, ExpnsCode, GroupNum, LineNum, DocEntry
Fields (name type(len) description [values] ->parent table):
  DocEntry Int(11) Internal Document ID ->OWTQ
  LineNum Int(11) Row Number default=-1
  GroupNum Int(11) Group No. default=-1
  ExpnsCode Int(11) Expense Code default=-1 ->OEXD
  RelateType Int(11) Relation Type default=1 [1=Row, 2=Row Freight Charges, 3=Document Expenses, 13=Distributed Freights]
  StcCode nVarChar(8) Tax Code ->OSTC
  StaCode nVarChar(8) Tax Code ->OSTA
  staType Int(11) Authority Type ->OSTT
  TaxRate Num(19,6) Authority Type ->OSTT
  TaxAcct nVarChar(15) Authority Code
  TaxSum Num(19,6) Tax % ->OACT
  TaxSumFrgn Num(19,6) Tax Account
  TaxSumSys Num(19,6) Tax Amount
  BaseSum Num(19,6) Tax Amount (FC)
  BaseSumFrg Num(19,6) Base Amount
  BaseSumSys Num(19,6) Base Amount (FC)
  ObjectType nVarChar(20) Base Amount (SC)
  LogInstanc Int(11) Tax Amount (SC) default=0 ->ADP1
  TaxStatus VarChar(1) Base Amount default=Y [Y=Regular Tax, N=No Tax, U=Use Tax]
  VatApplied Num(19,6) VAT Applied
  VatAppldFC Num(19,6) Applied Tax (FC)
  VatAppldSC Num(19,6) Applied Tax (SC)
  LineSeq Int(11) Line Sequence
  DeferrAcct nVarChar(15) Deferred Tax Account ->OACT
  BaseType Int(11) Base Document Type default=-1
  BaseAbs Int(11) Base Doc Abs Entry default=-1
  BaseSeq Int(11) Base Doc. Line Sequence
  DeductTax Num(19,6) Deductible Tax Amount
  DdctTaxFrg Num(19,6) Deductible Tax Amount (FC)
  DdctTaxSys Num(19,6) Deductible Tax Amount (SC)
  BaseAppld Num(19,6) Applied Base Amount
  BaseApldFC Num(19,6) Applied Base Amount (FC)
  BaseApldSC Num(19,6) Applied Base Amount (SC)
  NonDdctPrc Num(19,6) Non Deductible %
  NonDdctAct nVarChar(15) Non Deductible Account ->OACT
  TaxInPrice VarChar(1) Tax Included in Price? default=N [Y=Yes, N=No]
  Exempt VarChar(1) Exempt? default=N [Y=Yes, N=No]
  TaxExpAct nVarChar(15) Expense Account for Tax ->OACT
  OnHoldTax Num(19,6) On Hold Tax Amount
  OnHoldTaxF Num(19,6) On Hold Tax Amount (FC)
  OnHoldTaxS Num(19,6) On Hold Tax Amount (SC)
  InGrossRev VarChar(1) Included in Gross Revenue default=N [Y=Yes, N=No]
  TaxSumOrg Num(19,6) Tax Amount Original
  TaxSumOrgF Num(19,6) Tax Amount Original (FC)
  TaxSumOrgS Num(19,6) Tax Amount Original (SC)
  OpenTax Num(19,6) Open Service Tax
  OpenTaxFC Num(19,6) Open Service Tax (FC)
  OpenTaxSC Num(19,6) Open Service Tax (SC)
  Unencumbrd VarChar(1) Unencumbered default=N [Y=Yes, N=No]
  TaxOnRI VarChar(1) Tax On Reserve Invoice default=N [Y=Yes, N=No]
  RvsChrgPrc Num(19,6) Reverse Charge %
  RvsChrgTax Num(19,6) Reverse Charge Tax Amount
  RvsChrgSC Num(19,6) Reverse Charge Tax Amount (SC)
  RvsChrgFC Num(19,6) Reverse Charge Tax Amount (FC)
  InFirstIns VarChar(1) Included in First Installment default=N [Y=Yes, N=No]

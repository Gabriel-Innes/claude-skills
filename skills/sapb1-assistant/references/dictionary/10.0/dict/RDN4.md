<!-- source: REFDB.chm (SAP Business One SDK 10.0 - Database Tables Reference) | version: SAP Business One 10.0 | verified: 2026-10-01 -->
# RDN4 - Returns - Tax Amount per Document
Module: Marketing Documents | 61 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: DocEntry, LineSeq
  SCONDARY: DocEntry, LineNum, GroupNum, ExpnsCode, StcCode, StaCode, staType
Fields (name type(len) description [values] ->parent table):
  DocEntry Int(11) Document Internal ID ->ORDN
  LineNum Int(11) Row Number default=-1
  GroupNum Int(11) Group Number default=-1
  ExpnsCode Int(11) Expense Code default=-1 ->OEXD
  RelateType Int(11) Relation Type default=1 [1=Row, 2=Row Freight Charges, 3=Document Expenses, 13=Distributed Freights]
  StcCode nVarChar(8) Tax Code ->OSTC
  StaCode nVarChar(8) Authority Code ->OSTA
  staType Int(11) Authority Type ->OSTT
  TaxRate Num(19,6) Tax Rate
  TaxAcct nVarChar(15) Tax Account ->OACT
  TaxSum Num(19,6) Tax Amount
  TaxSumFrgn Num(19,6) Tax Amount (FC)
  TaxSumSys Num(19,6) Tax Amount (SC)
  BaseSum Num(19,6) Base Amount
  BaseSumFrg Num(19,6) Base Amount (FC)
  BaseSumSys Num(19,6) Base Amount (SC)
  ObjectType nVarChar(20) Object Type default=16 ->ADP1
  LogInstanc Int(11) Log Instance default=0
  TaxStatus VarChar(1) Tax Status default=Y [Y=Regular Tax, N=No Tax, U=Use Tax]
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
  ExtTaxRate Num(19,6) External Tax Rate
  ExtTaxSum Num(19,6) External Tax Amount
  TaxAmtSrc VarChar(1) Tax Amount Source default=S [S=Internal System Calculation, E=External Calculation]
  ExtTaxSumF Num(19,6) External Tax Amount (FC)
  ExtTaxSumS Num(19,6) External Tax Amount (SC)
  CESTrel VarChar(1) CEST Relevant default=N [Y=, N=]

<!-- source: erpref.com (schema IP: SAP) | version: SAP Business One 9.3 | verified: 2026-10-01 -->
# AVTG - Tax Definition
Module: Finance | 62 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: LogInstanc, Code
  GROUP_NAME: LogInstanc, Name
Fields (name type(len) description [values] ->parent table):
  Code nVarChar(8) Code
  Name nVarChar(50) Name
  Rate Num(19,6) Rate %
  EffecDate Date(8) Effective from
  Category VarChar(1) Category default=O [O=Output Tax, I=Input Tax]
  Account nVarChar(15) Tax Account ->OACT
  Locked VarChar(1) Locked default=N [Y=Yes, N=No]
  DataSource VarChar(1) Data Source default=N [N=Unknown, I=Interface, U=Update, M=Import, O=DI API, A=Doc. Generation Wizard, D=Restore Wizard, P=Partner Implementation, T=Year Transfer]
  UserSign Int(6) User Signature ->OUSR
  IsEC VarChar(1) EU default=N [Y=Yes, N=No]
  Indicator VarChar(1) Triangular Deal ->OIND
  AcqstnRvrs VarChar(1) Acquisition/Reverse default=N [Y=Yes, N=No]
  NonDedct Num(19,6) Non-Deductible %
  AcqsTax nVarChar(15) Acquisition Tax Account ->OACT
  GoddsShip VarChar(1) Goods Shipment ->OGSP
  NonDedAcc nVarChar(15) Non-Deductible Acct ->OACT
  DeferrAcc nVarChar(15) Deferred Tax Account ->OACT
  EquVatPr Num(19,6) Equalization Tax %
  ReportCode nVarChar(100) Group Description
  FixdAssts VarChar(1) Fixed Assets Flag default=N [Y=Yes, N=No]
  CalcMethod VarChar(1) Calculation Method default=R [R=Rate, F=Fixed]
  TaxType VarChar(1) Tax Type (VAT or Stamp) default=V [V=VAT, S=Stamp]
  FixedAmnt Num(19,6) Fixed Amount (LC)
  ExtCode nVarChar(10) External Code
  Correction VarChar(1) Correction default=N [Y=Yes, N=No]
  VatCrctn nVarChar(8) VAT Correction ->OVTG
  RetVatCode nVarChar(8) Returning VAT Code
  RepType Int(11) Report Type ->OKRT
  LogInstanc Int(11) Log Instance default=0
  UpdateDate Date(8) Date of Update
  TaxCtgr VarChar(1) Tax Type (Annual List) default=E [E=Excluded, T=Taxable, X=Exempt, N=Not Taxable, G=Gross Profit, R=Reverse Charge, U=Tourism, A=Taxable - Article 162, B=Taxable - Article 173 point 5, C=Taxable - Construction, D=Taxable - Expected Confirmation, F=Taxable - Gross, I=Taxable - Import, Y=Taxable - Import from EAEU, L=Taxable - Late Export, O=Taxable - Not Confirmed, S=Taxable - Real Estate, W=Taxable - Sale of Company, M=Taxable - Article 151 point 1, P=Taxable - Article 170 point 3, V=Taxable - Fixed Assets]
  EquAccount nVarChar(15) Equalization Tax Account ->OACT
  UserSign2 Int(6) Updating User ->OUSR
  IsIGIC VarChar(1) IGIC default=N [Y=Yes, N=No]
  ServSupply VarChar(1) Service Supply ->OSSP
  Inactive VarChar(1) Inactive default=N [Y=Yes, N=No]
  TaxCtgrBL VarChar(1) Tax Type (Black List) default=E [E=Excluded, T=Taxable, X=Exempt, N=Not Taxable, S=Non-Subject]
  R349Code Int(11) Report 349 Code default=0 [0=, 1=E, 2=A, 3=T, 4=S, 5=I, 6=M, 7=H]
  VatRevAcc nVarChar(15) VAT in Revenue Account ->OACT
  CashDisAcc nVarChar(15) Cash Discount Account ->OACT
  DpmTaxOAcc nVarChar(15) Down Paymnt Tax Offset Account ->OACT
  VatDedAcc nVarChar(15) VAT Deductible Account ->OACT
  CstmExpAcc nVarChar(15) Customs VAT Expense Account
  CstmAlcAcc nVarChar(15) Customs VAT Allocation Account
  TaxRegion nVarChar(5) Tax Country Region default=PT [PT=Continental Portugal, PT-AC=Azores Islands, PT-MA=Madeira Islands]
  ExemReason nVarChar(3) Tax Exemption Reason [M01=Article 16th No. 6 of CIVA, M02=Article 6th Law 198/90 June 19th, M03=Cash Liabilities, M04=Exempt Article 13th of CIVA, M05=Exempt Article 14th of CIVA, M06=Exempt Article 15th of CIVA, M07=Exempt Article 9th of CIVA, M08=VAT - Self-Liquidation, M09=VAT - Non-Deductible, M10=VAT - Exempted Company, M11=VAT - Exempted (Tobacco), M12=VAT - Exempted (Travel Agencies), M13=VAT - Exempt (Second Hand Goods), M14=VAT - Exempted (Objects of Art), M15=VAT - Exempted (Collectibles and Antiques), M16=VAT - Exempted (Article 14th of RITI), M99=Not Subject to VAT]
  Agent VarChar(1) Agent default=N [Y=Yes, N=No]
  OpCode nVarChar(7) Tax Operation Code
  Export VarChar(1) Export default=N [Y=Yes, N=No]
  Section nVarChar(3) VAT Section
  SplitPaymt VarChar(1) Split Payment default=N [Y=Yes, N=No]
  SplitPayAc nVarChar(15) Split Payment Account
  TaxAgent VarChar(1) Tax Agent (Section 3) default=N [Y=Yes, N=No]
  SectionLim nVarChar(3) VAT Section (under limit)
  VatSubjCod nVarChar(10) VAT Subject Code
  VatType Int(11) Type of VAT default=-1
  VatCategor Int(11) VAT Category default=-1
  Parag44 VarChar(1) Paragraph 44 default=N [Y=Yes, N=No]
  ProrataDed VarChar(1) Pro-rata deductible default=N [Y=Yes, N=No]
  ExcFrmTaxS VarChar(1) Exclude from Tax Summary Report Total A/R or A/P Net Amounts default=N [Y=Yes, N=No]
  CstmActing VarChar(1) Customer Accounting default=N [Y=Yes, N=No]
  CstmActOut nVarChar(8) Corresponding Tax Code

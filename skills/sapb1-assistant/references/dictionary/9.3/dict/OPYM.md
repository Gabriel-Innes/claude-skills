<!-- source: erpref.com (schema IP: SAP) | version: SAP Business One 9.3 | verified: 2026-10-01 -->
# OPYM - Payment Methods for Payment Wizard
Module: Banking | 63 columns | ObjType: 147
Indexes (name: columns; first = primary key; U = unique) - WARNING: multi-column key order here is reversed vs SAP's 10.0 reference (read as a set; see references/dictionary/INDEX.md):
  PRIMARY U: PayMethCod
Fields (name type(len) description [values] ->parent table):
  PayMethCod nVarChar(15) Payment Method Code
  Descript nVarChar(100) Description
  Type VarChar(1) Type [O=Outgoing, I=Incoming]
  BankTransf VarChar(1) Payment Means [C=Check, T=Bank Transfer, B=Bill of Exchange]
  Address VarChar(1) Check Address default=N [Y=Yes, N=No]
  BankDet VarChar(1) Check Bank Details default=N [Y=Yes, N=No]
  CllctAutor VarChar(1) Check Collection Authorization default=N [Y=Yes, N=No]
  FrgnPmntBl VarChar(1) Block Foreign Payment default=N [Y=Yes, N=No]
  FrgnBnkBl VarChar(1) Block Foreign Bank default=N [Y=Yes, N=No]
  CurrRestr VarChar(1) Currency Restriction default=N [Y=Yes, N=No]
  PostOffBnk VarChar(1) Post Office Bank default=N [Y=Yes, N=No]
  MinAmount Num(19,6) Minimum Amount
  MaxAmount Num(19,6) Maximum Amount
  BnkDflt nVarChar(30) Default Bank
  UserSign Int(6) User Signature ->OUSR
  DataSource VarChar(1) Data Source default=N [N=Unknown, I=Interface, U=Update, M=Import, O=DI API, A=Doc. Generation Wizard, D=Restore Wizard, P=Partner Implementation, T=Year Transfer]
  CreateDate Date(8) Creation Date
  BankCountr nVarChar(3) Bank Country ->OCRY
  DflAccount nVarChar(50) Default Bank Account
  GLAccount nVarChar(15) G/L Account ->OACT
  Branch nVarChar(50) Bank Branch
  KeyCode nVarChar(6) Key Code
  TrnsType nVarChar(2) Transaction Type
  Format nVarChar(11) File Format ->OFRM
  AgtCollect VarChar(1) Agent Collection default=N [Y=Yes, N=No]
  SendAccept VarChar(1) Send for Acceptance default=N [Y=Yes, N=No]
  GrpByDate VarChar(1) Group By Date default=N [Y=Yes, N=No]
  DepNorm nVarChar(8) Deposit Norm
  DebitMemo VarChar(1) Debit Memo default=N [N=No, Y=Yes]
  GroupPmRef VarChar(1) Group by Payment Reference No. default=N [Y=Yes, N=No]
  GroupInv VarChar(1) Group Invoices by Pay default=N [N=No, Y=Yes]
  ValDateSel VarChar(1) Due Date Selection default=P [P=Date of Payment Run, I=Due Date of Invoice, T=Payment Terms]
  PaymTerms Int(6) Payment Terms Code ->OCTG
  IntrimAcct VarChar(1) Post to G/L Interim Account default=N [N=No, Y=Yes]
  BnkActKey Int(11) Bank Account Key ->DSC1
  DocType nVarChar(2) BoE Document Type
  Accepted VarChar(1) BoE Status - Accepted
  PtfID nVarChar(3) BoE Internal Portfolio ID
  PtfCode nVarChar(2) BoE Portfolio Code
  PtfNum nVarChar(4) BoE Portfolio Number
  CurCode nVarChar(2) BoE Currency Code
  Instruct1 nVarChar(2) BoE Instruction 1
  Instruct2 nVarChar(2) BoE Instruction 2
  PaymntPlc nVarChar(128) BoE Payment Place
  BoeDll nVarChar(50) Bar Code DLL
  BankCtlKey nVarChar(2) Bank Control No.
  Active VarChar(1) Status of the Payment Method default=Y [Y=Active, N=Inactive]
  BcgPcnt Num(19,6) Bank Charge Rate (%)
  GrpByCur VarChar(1) Group Invoices by Currency default=N [N=No, Y=Yes]
  GrpByBank VarChar(1) Group Invoices by Pay-To Bank default=N [Y=Yes, N=No]
  DflIBAN nVarChar(50) Bank IBAN
  DflSwift nVarChar(50) Bank BIC/SWIFT
  BoeReport nVarChar(8) BoE Report Code
  CancInstr nVarChar(2) Cancellation Instruction
  OccurCode nVarChar(2) Occurrence Code
  MovmntCode nVarChar(10) Movement Code
  NegPymCode nVarChar(15) Negative Payment Method Code ->OPYM
  DirectDbt nVarChar(5) Direct Debit [CORE=, B2B=, COR1=]
  IssueIndic VarChar(1) Issue Indicator default=R [3=, R=]
  PrintSEPA VarChar(1) Print SEPA Prenotification default=N [Y=Yes, N=No]
  PmntType nVarChar(50) Payment Type default=01 [01=Efectivo, 02=Cheque nominativo, 03=Transferencia electrónica de fondos, 04=Tarjeta de crédito, 05=Monedero electrónico, 06=Dinero electrónico, 08=Vales de despensa, 12=Dación en pago, 13=Pago por subrogación, 14=Pago por consignación, 15=Condonación, 17=Compensación, 23=Novación, 24=Confusión, 25=Remisión de deuda, 26=Prescripción o caducidad, 27=A satisfacción del acreedor, 28=Tarjeta de débito, 29=Tarjeta de servicios, 30=Aplicación de anticipos, 99=Por definir]
  GrpByAgrNo VarChar(1) Group Blanket Agreement default=N [Y=Yes, N=No]
  SpltPmtVAT VarChar(1) Split Payments for VAT default=N [Y=Yes, N=No]

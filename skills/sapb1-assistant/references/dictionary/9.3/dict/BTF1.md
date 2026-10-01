<!-- source: erpref.com (schema IP: SAP) | version: SAP Business One 9.3 | verified: 2026-10-01 -->
# BTF1 - Journal Voucher - Rows
Module: Finance | 136 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: Line_ID, TransId, BatchNum
  SHORT_NAME: ShortName
  ACCOUNT: Account
  BATCH_IDX: BatchNum
  CURRENCY: FCCurrency
  INTRNMATCH: IntrnMatch, Account, ShortName
Fields (name type(len) description [values] ->parent table):
  TransId Int(11) Transaction Key ->OJDT
  Line_ID Int(11) Row Number default=0
  Account nVarChar(15) Account Code ->OACT
  Debit Num(19,6) Debit Amount
  Credit Num(19,6) Credit Amount
  SYSCred Num(19,6) System Credit Amount
  SYSDeb Num(19,6) System Debit Amount
  FCDebit Num(19,6) FC Debit Amount
  FCCredit Num(19,6) FC Credit Amount
  FCCurrency nVarChar(3) Foreign Currency
  DueDate Date(8) Due Date
  SourceID Int(11) Source Key
  SourceLine Int(6) Source Row Number
  ShortName nVarChar(15) Card/Account Code
  IntrnMatch Int(11) Internal Reconciliation No. default=0
  ExtrMatch Int(11) External Reconciliation No. default=0
  ContraAct nVarChar(15) Offset Account
  LineMemo nVarChar(50) Row Details
  Ref3Line nVarChar(27) Reference 3
  TransType nVarChar(20) Original Journal default=-1 [-1=]
  RefDate Date(8) Posting Date
  Ref2Date Date(8) Posting Date 2
  Ref1 nVarChar(100) Reference 1
  Ref2 nVarChar(100) Reference 2
  CreatedBy Int(11) Origin
  BaseRef nVarChar(11) Base Reference
  Project nVarChar(20) Project Code ->OPRJ
  TransCode nVarChar(4) Transaction Code ->OTRC
  ProfitCode nVarChar(8) Distribution Rule ->OOCR
  TaxDate Date(8) Document Date
  SystemRate Num(19,6) System Price
  MthDate Date(8) Reconciliation Date
  ToMthSum Num(19,6) Reconciliation Total
  UserSign Int(6) User Signature ->OUSR
  BatchNum Int(11) Journal Voucher No. ->OBTD
  FinncPriod Int(11) Posting Period ->OFPR
  RelTransId Int(11) Linked Transaction Key default=-1
  RelLineID Int(11) Linked Row No. default=-1
  RelType VarChar(1) Link Type default=N [N=Without Link, D=WTax Deduction - Correction]
  LogInstanc Int(11) Log Instance default=0
  VatGroup nVarChar(8) Tax Group ->OVTG
  BaseSum Num(19,6) Base Amount
  VatRate Num(19,6) Tax %
  Indicator nVarChar(2) Indicator Code ->OIDC
  AdjTran VarChar(1) Adjusting Trans. (Period 13) default=N [Y=Yes, N=No]
  RevSource VarChar(1) Revaluation Source default=N [F=FC, S=System, N=No]
  ObjType nVarChar(20) Object Type default=30 ->ADP1
  VatDate Date(8) Document Date
  PaymentRef nVarChar(27) Payment Reference
  SYSBaseSum Num(19,6) System Base Amount
  MultMatch Int(11) Multiple BP Reconciliation No. default=0
  VatLine VarChar(1) VAT Row default=N [Y=Yes, N=No]
  VatAmount Num(19,6) VAT Amount
  SYSVatSum Num(19,6) System VAT Amount
  Closed VarChar(1) Closed default=N
  GrossValue Num(19,6) Gross Value
  CheckAbs Int(11) Internal Check No.
  LineType Int(11) LineType default=0
  DebCred VarChar(1) Debit Credit Line Indicator [D=Debit, C=Credit]
  SequenceNr Int(11) Assigned Sequence No. default=0
  StornoAcc nVarChar(15) Storno Account Code ->OACT
  BalDueDeb Num(19,6) Balance Due - Debit
  BalDueCred Num(19,6) Balance Due - Credit
  BalFcDeb Num(19,6) Balance Due FC - Debit
  BalFcCred Num(19,6) Balance Due FC - Credit
  BalScDeb Num(19,6) Balance Due SC - Debit
  BalScCred Num(19,6) Balance Due SC - Credit
  IsNet VarChar(1) Is Net default=Y [Y=Yes, N=No]
  DunWizBlck VarChar(1) Wizard Dunning Block default=N [N=No, Y=Yes, =]
  DunnLevel Int(11) Dunning Level default=0 ->ODUN
  DunDate Date(8) Last Dunning Date
  TaxType Int(6) Tax Type default=0
  TaxPostAcc VarChar(1) Tax Posting Account default=N [N=, R=Sales Tax Account, P=Purchasing Tax Account]
  StaCode nVarChar(8) Authority Code ->OSTA
  StaType Int(11) Authority Type ->OSTT
  TaxCode nVarChar(8) Tax Code ->OSTC
  ValidFrom Date(8) Valid From default=19000101
  GrossValFc Num(19,6) Gross Value (FC)
  LvlUpdDate Date(8) Dunning Level Update Date
  OcrCode2 nVarChar(8) Costing Code 2 ->OOCR
  OcrCode3 nVarChar(8) Costing Code 3 ->OOCR
  OcrCode4 nVarChar(8) Costing Code 4 ->OOCR
  OcrCode5 nVarChar(8) Costing Code 5 ->OOCR
  MIEntry Int(11) MI Entry when include this OB default=0
  MIVEntry Int(11) A/P Monthly Invoice default=0
  ClsInTP Int(11) Tax Payment Wizard default=0
  CenVatCom Int(11) CENVAT Component default=-1
  MatType Int(11) Material Type default=-1
  PstngType Int(11) Posting Type default=0
  ValidFrom2 Date(8) Valid from2 default=19000101
  ValidFrom3 Date(8) Valid from3 default=19000101
  ValidFrom4 Date(8) Valid from4 default=19000101
  ValidFrom5 Date(8) Valid from5 default=19000101
  Location Int(11) Loc. ->OLCT
  WTaxCode nVarChar(4) Withholding Tax Code ->OWHT
  EquVatRate Num(19,6) Equalization Tax %
  EquVatSum Num(19,6) Equalization Tax Amount
  SYSEquSum Num(19,6) System Equalization Tax Amount
  TotalVat Num(19,6) Total Tax
  SYSTVat Num(19,6) System Total Tax
  WTLiable VarChar(1) WTax-Liable default=N [Y=Yes, N=No]
  WTLine VarChar(1) WTax Row default=N [Y=Yes, N=No]
  WTApplied Num(19,6) Applied WTax
  WTAppliedS Num(19,6) Applied WTax (SC)
  WTAppliedF Num(19,6) Applied WTax (FC)
  WTSum Num(19,6) WTax Amount
  WTSumFC Num(19,6) WTax Amount (FC)
  WTSumSC Num(19,6) WTax Amount (SC)
  PayBlock VarChar(1) Payment Block default=N [Y=Yes, N=No]
  PayBlckRef Int(11) Payment Block Abs Entry ->OPYB
  LicTradNum nVarChar(32) Federal Tax ID
  InterimTyp Int(11) Interim Account Type default=0
  DprId Int(11) Down Payment Request Key
  MatchRef nVarChar(20) Reconciliation Reference
  Ordered VarChar(1) Payment Ordered default=N [Y=Yes, N=No]
  CUP Int(11) Unique Code of Project ->OCUP
  CIG Int(11) Contract Code Identification ->OCIG
  BPLId Int(11) Branch ->OBPL
  BPLName nVarChar(100) Branch Name
  VatRegNum nVarChar(32) VAT Reg. Number
  SLEDGERF VarChar(1) Subledger Flag
  InitRef2 nVarChar(100) Initial Reference 2
  InitRef3Ln nVarChar(27) Initial Reference 3
  ExpUUID nVarChar(50) Expense UUID
  ExpOPType VarChar(1) Expense Operation Type [P=Professional Services, R=Renting Assets, O=Others, =]
  ExTransId Int(11) Exposed Transaction ID
  DocArr Int(6) Source of Posting
  DocLine Int(11) Source Line Internal ID
  MYFtype nVarChar(2) MYF type [S1=MYF sales, S2=Retail sales, P1=MYF purchase, P3=Other expense]
  DocEntry Int(11) Source Document Entry
  DocNum Int(11) Source Document Number
  DocType nVarChar(20) Source Document Type
  DocSubType nVarChar(2) Document Subtype
  RmrkTmpt Int(11) Remark Text Template ->OTTR
  CemCode nVarChar(20) Cost Element Code
  CAOutCode nVarChar(8) Customer Accounting Output Tax Code

<!-- source: erpref.com (schema IP: SAP) | version: SAP Business One 9.3 | verified: 2026-10-01 -->
# PWZ3 - Payment Wizard - Rows 3
Module: Banking | 160 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: PymNum, IdEntry
Fields (name type(len) description [values] ->parent table):
  IdEntry Int(11) ID Entry ->OPWZ
  PymNum Int(11) Payment Number ->OCRN
  CardCode nVarChar(15) Vendor Code ->OCRD
  CardName nVarChar(100) Vendor Name
  PymMeth nVarChar(15) Payment Method ->OPYM
  GLAccCode nVarChar(15) G/L Account Code ->OACT
  GLAccName nVarChar(100) G/L Account Name
  PymAmount Num(19,6) Total Payment
  PymAmntFC Num(19,6) Total Payment (FC)
  PymAmnSyst Num(19,6) Total Payment (SC)
  InvKey Int(11) Invoice Key
  DocNum Int(11) Document Number
  PostDate Date(8) Posting Date
  ValDate Date(8) Due Date
  TotalLoc Num(19,6) Total (LC)
  TotalFC Num(19,6) Total (FC)
  TotalSys Num(19,6) Total (SC)
  DueBal Num(19,6) Balance Due
  DueBalFC Num(19,6) Balance Due (FC)
  DueBalSys Num(19,6) Balance Due (SC)
  DiscPrcnt Num(19,6) Discount %
  DiscSum Num(19,6) Total Discount
  DiscSumFC Num(19,6) Total Discount (FC)
  DiscSumSy Num(19,6) Total Discount (SC)
  PayAmount Num(19,6) Payment Amount
  PayAmntFC Num(19,6) Payment Amount (FC)
  PayAmntSys Num(19,6) Payment Amount (SC)
  InvPayAmnt Num(19,6) Total Invoice for Payment
  InvPayAmFC Num(19,6) Total Invoice for Payment (FC)
  InvPayAmSy Num(19,6) Total Invoice for Payment (SC)
  CardType VarChar(1) BP Type default=C [C=Customer, S=Vendor, L=Lead]
  Country nVarChar(3) Bank Country ->OCRY
  ObjType nVarChar(20) Object Type default=13 ->ADP1
  PymBnkTrns VarChar(1) Payment Means default=C [C=Check, T=Bank Transfer, B=Bill Of Exchange]
  ActFrmtCod nVarChar(210) Account Format Code
  Checked VarChar(1) Checked
  FatherLine VarChar(1) Father Line default=N
  InvCurr nVarChar(3) Document Currency
  LineRate Num(19,6) Row Rate
  BfDcntSum Num(19,6) Amount Before Discount
  BfNetDcnt Num(19,6) Net Amount Before Discount
  vatApplied Num(19,6) VAT Applied
  IsTax VarChar(1) Is Tax default=Y
  IsFreight VarChar(1) Is Freight default=Y
  IsOrigMeth VarChar(1) Original Payment Method default=N
  FreightSum Num(19,6) Freight Sum
  IsrRef nVarChar(27) ISR Ref. No.
  RoundSum Num(19,6) Rounding Amount
  Agent nVarChar(32) Agent Code ->OAGP
  InstId Int(6) Installment ID default=1
  WtSum Num(19,6) Withholding Tax Amount
  BoeNum Int(11) Bill of Exchange No.
  NumAtCard nVarChar(100) BP Reference No.
  DeductPer Num(19,6) Deduction Percent
  DpmPosted VarChar(1) Down Payment Posted
  Status VarChar(1) Inv Status
  NumOfCheck Int(11) Number of Checks default=1
  SumFrstChk Num(19,6) Sum of First Check
  SumNxtChk Num(19,6) Sum of Next Check
  PayToCode nVarChar(50) Pay to
  PayToCntr nVarChar(3) Pay to Bank Country ->OCRY
  PayToBank nVarChar(30) Pay to Bank Code
  PayToAct nVarChar(50) Pay to Bank Account No.
  PymCurr nVarChar(3) Payment Currency
  TaxOnExpSu Num(19,6) Tax on Freight Amount
  TransId Int(11) Transaction Internal ID ->OJDT
  OcrCode nVarChar(8) Distribution Rule ->OOCR
  Line_ID Int(11) JE Row Number default=0
  OcrCode2 nVarChar(8) Distribution Rule2 ->OOCR
  OcrCode3 nVarChar(8) Distribution Rule3 ->OOCR
  OcrCode4 nVarChar(8) Distribution Rule4 ->OOCR
  OcrCode5 nVarChar(8) Distribution Rule5 ->OOCR
  PymDate Date(8) Payment Date
  BcgSum Num(19,6) Bank Charges Amount
  BcgSumFC Num(19,6) Bank Charges Amount (FC)
  BcgSumSy Num(19,6) Bank Charges Amount (SC)
  BcgTaxSum Num(19,6) Bank Charge Tax Amount
  BcgTaxSumF Num(19,6) Bank Charge Tax Amount (FC)
  BcgTaxSumS Num(19,6) Bank Charge Tax Amount (SC)
  PrjCode nVarChar(20) Project ->OPRJ
  BcgVatGrp nVarChar(8) Bank Charge Tax Group ->OVTG
  LinePrjCod nVarChar(20) Line Project ->OPRJ
  BcgPmnt Num(19,6) Payment Amount (BCG)
  BcgPmntFc Num(19,6) Payment Amount FC (BCG)
  BcgPmntSc Num(19,6) Payment Amount SC (BCG)
  PayOrderNo Int(11) Payment Order Number ->OIPO
  LineType VarChar(1) Line Type default=G [G=General, O=Pay on Account, T=Pay to Account]
  ManualNum Int(11) Manual Entry No. default=0
  Ref1 nVarChar(100) Reference 1
  Ref2 nVarChar(100) Reference 2
  Ref3 nVarChar(100) Reference 3
  OrdrStatus VarChar(1) Payment Order Status
  BnkCode nVarChar(30) Bank Code
  BnkAccNo nVarChar(50) Bank Account Number
  Branch nVarChar(50) Branch
  BnkCountr nVarChar(3) Manual Line Bank Country
  TBankCode nVarChar(30) Target Default Bank default=-1
  TDflAccoun nVarChar(50) Target Default Account
  TBankCount nVarChar(3) Target Bank Country ->OCRY
  TargetBran nVarChar(50) Target Bank Branch
  DscDueDate Date(8) Discount Due Date
  CIG Int(11) Contract Code Identification ->OCIG
  CUP Int(11) Unique Code of Project ->OCUP
  BoeCurrSta VarChar(1) BoE Current Status
  BoeKey Int(11) Bill of Exchange Key ->OBOE
  BoeDate Date(8) BoE Date
  BoeDueDate Date(8) Bill of Exchange Due Date
  Instruct1 nVarChar(2) BoE Instruction 1
  Instruct2 nVarChar(2) BoE Instruction 2
  BoeCancIns nVarChar(2) BoE Cancel Instruction
  BoeOccCode nVarChar(2) BoE Occurrence Code
  BoePtfID nVarChar(3) BoE Internal Portfolio ID
  BoeOurNum Int(11) Our Number in Next BoE
  BoeIntrAm Num(19,6) BoE Interest Amount
  BoeDiscD Date(8) BoE Discount Date
  BoeDisAmnt Num(19,6) BoE Discount Amount
  BoeFineD Date(8) BoE Fine Date
  BoeFineAmt Num(19,6) BoE Fine Amount
  BoeIntrstD Date(8) BoE Interest Date
  BoeIOFAmt Num(19,6) BoE IOF Amount
  BoeMovCode nVarChar(10) BoE Movement Code
  BarcodeRep nVarChar(100) Barcode Representation
  BPLId Int(11) Branch ->OBPL
  PONumber Int(11) External Payment Order Number
  POSeries Int(11) External Payment Order Series
  PaPriority VarChar(1) Payment Priority default=6 [1=, 2=, 3=, 4=, 5=, 6=]
  PaymType VarChar(1) Payment Type default=N [N=, E=Electronic, P=Mail, T=Telegraph, X=Express]
  OriPymMeth nVarChar(15) Original Payment Method Code
  PymMethTyp VarChar(1) Payment Method Type [I=Incoming, O=Outgoing]
  SinglePym VarChar(1) Single Payment default=N [N=No, Y=Yes]
  MandateID nVarChar(35) Mandate ID
  SeqType nVarChar(4) Sequence Type [OOFF=OOFF, FRST=FRST, RCUR=RCUR, FNAL=FNAL]
  BaseDocDat Date(8) Base Document Date
  OKATO nVarChar(11) OKATO
  PostPeriod nVarChar(10) Posting Period Code
  RecipStatu nVarChar(2) Recipient Status
  BudgetId nVarChar(100) VAT Budget Classification Code
  PymReason nVarChar(2) Payment Reason
  BaseDocTyp nVarChar(2) Base Document Type
  TaxPymType nVarChar(2) Tax Payment Type
  OKTMO nVarChar(12) OKTMO
  PymIsUpdat nVarChar(30) Payment method is updated
  OriPymCode nVarChar(15) Original Payment Method Code
  OriPymType VarChar(1) Original Payment Method Type
  ReasonCode Int(11) Reason Code
  OriActCode nVarChar(15) Original Account Code
  OriActName nVarChar(100) Original Account Name
  ReasonLine Int(11) Reason Line
  OriFormat nVarChar(210) Original Format Code
  WtIsPym VarChar(1) Withholding Tax is Payment Type default=N [N=No, Y=Yes]
  IBAN nVarChar(50) IBAN
  SwiftNum nVarChar(50) BIC/SWIFT Code
  UIPCode nVarChar(25) UIP Code
  AgrNo Int(11) Agreement No. ->OOAT
  ExeByServ VarChar(1) Executed by Server
  SpltPmtVAT VarChar(1) Split Payment default=N [Y=Yes, N=No]
  VatAmount Num(19,6) VAT Amount
  EnPayToAct Text(16) Encryption of Pay to Bank Acct
  EncryptIV nVarChar(100) Encrypt IV
  DPPStatus VarChar(1) Data Protection Status default=N [N=None, D=Erased]

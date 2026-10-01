<!-- source: REFDB.chm (SAP Business One SDK 10.0 - Database Tables Reference) | version: SAP Business One 10.0 | verified: 2026-10-01 -->
# OPEX - Payment Results Table
Module: Banking | 139 columns | ObjType: 158
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: AbsEntry
Fields (name type(len) description [values] ->parent table):
  AbsEntry Int(11) Internal Number
  PayRunDate Date(8) Date of Payment Run
  VendorNum nVarChar(15) Vendor Code
  CustNum nVarChar(15) Customer Code
  PaymMethod nVarChar(15) Payment Means
  PaymDocNum Int(11) Payment Document No.
  FiscalYear Date(8) Fiscal Year
  Country nVarChar(3) Company Country/Region
  CompTaxNum nVarChar(32) Company Tax Number
  PayeeName nVarChar(100) Payee Name
  PayeeZip nVarChar(20) Payee Zip Code
  PayeeCity nVarChar(100) Payee City
  PayeeStree nVarChar(100) Payee Street
  PayCountry nVarChar(3) Payee Country/Region
  PayeeState nVarChar(3) Payee State
  PayBnkName nVarChar(250) Payee Bank Name
  PayBankZip nVarChar(20) Payee Bank Zip Code
  PayBnkCity nVarChar(100) Payee Bank City
  PayBnkStr nVarChar(100) Payee Bank Street
  PayBnkCntr nVarChar(3) Payee Bank Country/Region
  PayBankAct nVarChar(50) Payee Bank Account
  PayBnkCode nVarChar(30) Payee Bank Code
  PayBnkCtrl nVarChar(2) Payee Bank Control Number
  PayBnkSwif nVarChar(50) Payee Bank BIC/SWIFT Code
  PayBnkIBAN nVarChar(50) Payee Bank IBAN
  PymPostDat Date(8) Payment Posting Date
  PymBnkAcct nVarChar(50) Payment Bank Account
  PymBnkCntr nVarChar(3) Payment Bank Country/Region
  PymBnkCode nVarChar(30) Payment Bank Code
  PymBnkIBAN nVarChar(50) Payment Bank IBAN
  PymGLAcct nVarChar(15) Payment G/L Account
  Currency nVarChar(3) Main Currency
  PymDocAmnt Num(19,6) Payment Document Amount (LC)
  PymDocCurr nVarChar(3) Payment Document Currency
  PymDcAmtFC Num(19,6) Payment Document Amount (FC)
  PymCshDsct Num(19,6) Cash Discount in Payment Doc
  PyCshDscFC Num(19,6) Cash Discount in Payment Doc
  PymNumOfPa Int(11) Number of Items Paid
  PymDocRate Num(19,6) Payment Document Exchange Rate
  Status VarChar(1) Status default=O [O=Open, C=Closed]
  PaymWizCod Int(11) Payment Wizard Code ->OPWZ
  InstrucKey nVarChar(30) Instruction Key
  CllctAutho VarChar(1) Collection Authorization
  PayBnkPost VarChar(1) Payee Bank Post Office
  PayBnkChNo Int(11) Payee Bank Next Check No.
  PayBnkHsBk VarChar(1) Payee Bank House Bank default=N [N=No, Y=Yes]
  PayBnkBlck nVarChar(100) Payee Bank Block
  PayBnkCnty nVarChar(100) Payee Bank County
  PayBnkStat nVarChar(3) Payee Bank State
  PayBnkBISR VarChar(1) Payee Bank BISR default=N [N=No, Y=Yes]
  PayBnkUsr1 nVarChar(25) Payee Bank User No. 1
  PayBnkUsr2 nVarChar(25) Payee Bank User No. 2
  PayBnkUsr3 nVarChar(25) Payee Bank User No. 3
  PayBnkUsr4 nVarChar(25) Payee Bank User No. 4
  PaymFormat nVarChar(20) Payment Format
  CompName nVarChar(100) Company Name
  CompAddres nVarChar(254) Company Address
  CompISRBil nVarChar(9) Company ISR Biller ID
  VendISRBil nVarChar(9) Vendor ISR Biller ID
  AddIdNum nVarChar(32) Additional ID No.
  CompOrgNum nVarChar(50) Company Organization No.
  PayBnkBrnc nVarChar(50) Payee Bank Branch
  PymBnkBrnc nVarChar(50) Payment Bank Branch
  UserName nVarChar(155) User Name
  UserEmail nVarChar(100) User E-Mail
  UserPortNo nVarChar(50) User Mobile Phone No.
  UserFax nVarChar(50) User Fax No.
  Department Int(6) User Department
  DebitMemo VarChar(1) Debit Memo default=N [N=No, Y=Yes]
  EuInTrnsfr VarChar(1) EU Internal Transfer default=N [N=No, Y=Yes]
  FilePath Text(16) File Path
  OrderParty nVarChar(30) Ordering Party
  PymCtrlKey nVarChar(2) Payment Bank Control Number
  PayeeTaxNo nVarChar(32) Payee Tax Number
  PymKeyCode nVarChar(6) Payment Key Code
  PayRefDtls nVarChar(20) Payee Reference Details
  FormatName nVarChar(100) Format Name
  CheckPmnt VarChar(1) Payment Done with Check default=N [N=No, Y=Yes]
  PymBnkUsr1 nVarChar(25) Payment Bank User No. 1
  PymBnkUsr2 nVarChar(25) Payment Bank User No. 2
  PymBnkUsr3 nVarChar(25) Payment Bank User No. 3
  PymBnkUsr4 nVarChar(25) Payment Bank User No. 4
  CompStreet nVarChar(100) Company Street
  CompBlock nVarChar(100) Company Block
  CompCity nVarChar(100) Company City
  CompZip nVarChar(20) Company Zip Code
  CompCounty nVarChar(100) Company County
  CompState nVarChar(3) Company State ->OCST
  PymBCACode nVarChar(3) Payment Bank Charges ->OBCA
  PaymDocTyp nVarChar(20) Payment Document Object Type
  PayOrderNo Int(11) Payment Order Number ->OIPO
  FreeText1 nVarChar(254) Free Text 1
  FreeText2 nVarChar(254) Free Text 2
  FreeText3 nVarChar(254) Free Text 3
  PymBnkSwif nVarChar(50) Payment Bank Swift Code
  PayBnkUIC nVarChar(3) Payee Bank UIC Code
  LineType VarChar(1) Line Type default=G [G=General, O=Pay on Account, T=Pay to Account]
  BoeKey Int(11) Bill of Exchange Key ->OBOE
  BoeCurrSta VarChar(1) BoE Current Status
  BoeDate Date(8) Bill of Exchange Date
  BoeDueDate Date(8) BoE Due Date
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
  PONumber Int(11) External Payment Order Number
  POSeries Int(11) External Payment Order Series
  PaPriority VarChar(1) Payment Priority default=6 [1=, 2=, 3=, 4=, 5=, 6=]
  PaymType VarChar(1) Payment Type default=N [N=, E=Electronic, P=Mail, T=Telegraph, X=Express]
  RecipStatu nVarChar(2) Recipient Status
  BudegetId nVarChar(100) VAT Budget Classification Code
  OKATO nVarChar(11) OKATO
  PymReason nVarChar(2) Payment Reason
  PostPeriod nVarChar(10) Posting Period Code
  BaseDocTyp nVarChar(2) Base Document Type
  BaseDocDat Date(8) Base Document Date
  TaxPymType nVarChar(2) Tax Payment Type
  OKTMO nVarChar(12) OKTMO
  SeqType nVarChar(4) Sequence Type [OOFF=OOFF, FRST=FRST, RCUR=RCUR, FNAL=FNAL]
  PymDate Date(8) Payment Date
  PymBnkName nVarChar(250) Payment Bank Name
  UIPCode nVarChar(25) UIP Code
  UserId Int(6) User ID ->OUSR
  SpltPmtVAT VarChar(1) Split Payment default=N [Y=Yes, N=No]
  EnBnkAct Text(16) Encryption of Payee Bank Acct
  EnBnkIBan Text(16) Encryption of Payee Bank IBAN
  EncryptIV nVarChar(100) Encrypt IV
  DPPStatus VarChar(1) Data Protection Status default=N [N=None, D=Erased]

<!-- source: erpref.com (schema IP: SAP) | version: SAP Business One 9.3 | verified: 2026-10-01 -->
# RTW1 - Boleto Retorno Wizard: Import Table
Module: Banking | 44 columns
Indexes (name: columns; first = primary key; U = unique) - WARNING: multi-column key order here is reversed vs SAP's 10.0 reference (read as a set; see references/dictionary/INDEX.md):
  PRIMARY U: AbsEntry
Fields (name type(len) description [values] ->parent table):
  AbsEntry Int(11) Internal Number
  BoeMatch nVarChar(10) BoE Match
  BoeNo nVarChar(10) BoE Number
  BoeDate Date(8) BoE Date
  BoeDueDate Date(8) BoE Due Date
  CreditDate Date(8) Credit Date
  CurrBoeSt VarChar(1) Current BoE Status [G=Generated, S=Sent, D=Deposited, P=Paid, C=Canceled, L=Closed, F=Failed, V=BoE to Vendor]
  ReqBoeSt VarChar(1) Requested BoE Status [G=Generated, S=Sent, D=Deposited, P=Paid, C=Canceled, L=Closed, F=Failed, V=BoE to Vendor]
  Instruct1 nVarChar(2) BoE Instruction 1
  Instruct2 nVarChar(2) BoE Instruction 2
  CancelCode nVarChar(4) Cancellation Code
  MovmntCode Int(6) Movement Code
  OccurCode Int(6) Occurrence Code
  OccurDate Date(8) Occurrence Date
  Portfolio VarChar(1) Portfolio
  OurNum Int(11) Our Number
  ValueOfT Num(19,6) Value of Title
  NetAmnt Num(19,6) Net Amount
  PaidAmnt Num(19,6) Paid Amount
  FineAmnt Num(19,6) Fine Amount
  IntAmnt Num(19,6) Interest Amount
  Discounts Num(19,6) Discount Amount
  ServiceFee Num(19,6) Service Fee
  IOFTax Num(19,6) IOF Tax
  OtherCred Num(19,6) Other Credits
  OtherExp Num(19,6) Other Expenses
  OtherInc Num(19,6) Other Incomes
  Errors nVarChar(8) Errors
  RefNum nVarChar(254) Reference No.
  Ref2 nVarChar(254) Reference 2
  CardName nVarChar(100) BP Name
  BoEBPName nVarChar(100) BoE BP Name
  MatchCode VarChar(1) Match Code default=N [A=Automatic, M=Manual, N=Not Identified]
  Selected VarChar(1) Selected default=N
  BoeRec Int(11) BoE Record Number
  RetIndex Int(11) RET File Record Index
  Filtered VarChar(1) Filtered default=Y
  Executed VarChar(1) Executed default=N
  Failed VarChar(1) Failed default=N
  LastRun VarChar(1) Last Run default=N
  ErrorMsg nVarChar(254) Error Message
  JETransId nVarChar(10) JE Trans. ID
  CardCode nVarChar(15) BoE BP Code
  PostType VarChar(1) Transaction Type default=C [C=Collection, D=Discounted]

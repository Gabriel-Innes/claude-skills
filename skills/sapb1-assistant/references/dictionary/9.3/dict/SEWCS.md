<!-- source: erpref.com (schema IP: SAP) | version: SAP Business One 9.3 | verified: 2026-10-01 -->
# SEWCS - SEWCS
Module: General | 42 columns
Indexes (name: columns; first = primary key; U = unique) - WARNING: multi-column key order here is reversed vs SAP's 10.0 reference (read as a set; see references/dictionary/INDEX.md):
  PRIMARY U: CompDbNam
Fields (name type(len) description [values] ->parent table):
  CompDbNam nVarChar(100) Company Db Name
  SmpTableId nVarChar(3) Smp Table ID
  COAtemplat VarChar(1) COA Template
  LocalCurr nVarChar(3) Local Currency
  SystemCurr nVarChar(3) System Currenct
  UseSegAcc VarChar(1) Use Segment Accounts
  StkValuat VarChar(1) Stock Valuation
  PricSysPWh VarChar(1) Price System Per Warehouse
  AllowRelSt VarChar(1) Stock Release w/o Cost Price
  CostPrcLst VarChar(1) Gross profit Base Price Origi
  GrossBySal VarChar(1) Calculate % GP as
  BlkNegQuan VarChar(1) Block Negative Quantity
  RoundMeth VarChar(1) Rounding Method
  RoundVAT VarChar(1) Round Tax Amount in Rows
  EnblExpns VarChar(1) Manage Expenses in Documents
  DirectRate VarChar(1) Exchange Rate Posting
  SumDec Int(11) Decimal - Amounts
  PriceDec Int(11) Decimal - Prices
  RateDec Int(11) Decimal - Rates
  QtyDec Int(11) Decimal - Quantities
  PercentDec Int(11) Decimal - Percent
  MeasureDec Int(11) Decimal - Units
  DecSep VarChar(1) Decimal - Separator
  DpmSalAct nVarChar(15) Sal-DownPayment Clearing Acct
  DfltIncom nVarChar(15) Sales -Revenues Account
  ForgnIncm nVarChar(15) Sales -Revenues Foreign
  ECIncome nVarChar(15) Sales -Revenue EU
  SHandleWT VarChar(1) Sales -enable WT
  SDfltWT nVarChar(4) Sales -Default WT Code
  NINum nVarChar(20) Ni No
  ExpireDate Date(8) Sales - Expiration Date
  CrtfcateNO nVarChar(20) Sales - Certificate Number
  SaleVatOff nVarChar(15) Sales - Tax Offsetting account
  DfltExpn nVarChar(15) Purchase - Expense Account
  ForgnExpn nVarChar(15) Purchase-Foreign Expense Acct
  ECExepnses nVarChar(15) Purchase - EU Expense account
  DpmPurAct nVarChar(15) Pur-DownPayment Clearing Acct
  ExpVarAct nVarChar(15) Purchase - Variance accont
  PHandleWT VarChar(1) Purchase - WT enabled
  PDfltWT nVarChar(4) Purchase - Default WT code
  PurcVatOff nVarChar(15) Pur - Tax Offsetting account
  ComissAct nVarChar(15) Gen - Credit Card Deposit fee

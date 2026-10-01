<!-- source: erpref.com (schema IP: SAP) | version: SAP Business One 9.3 | verified: 2026-10-01 -->
# RCT3 - Incoming Pmt - Credit Vouchers
Module: Banking | 26 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: LineID, DocNum
Fields (name type(len) description [values] ->parent table):
  DocNum Int(11) Document No. ->ORCT
  LineID Int(11) Row No.
  CreditCard Int(6) Credit Card default=-1 ->OCRC
  CreditAcct nVarChar(15) Credit Amount ->OACT
  CrCardNum nVarChar(64) Credit Card No.
  CardValid Date(8) Credit Card Valid Until
  VoucherNum nVarChar(20) Credit Voucher No.
  OwnerIdNum nVarChar(15) ID Number
  OwnerPhone nVarChar(20) Telephone
  CrTypeCode Int(6) Payment Method Code default=-1 ->OCRP
  NumOfPmnts Int(6) No. of Payments default=1
  FirstDue Date(8) 1st Payment Date
  FirstSum Num(19,6) 1st Partial Payment
  AddPmntSum Num(19,6) Each Additional Payment
  CreditSum Num(19,6) Credit Amount
  CreditCur nVarChar(3) Credit Currency ->OCRN
  CreditRate Num(19,6) Credit Rate
  ConfNum nVarChar(20) Confirmation No.
  CreditType VarChar(1) Credit Transaction Type default=S [U=Telephone Transaction, S=Regular, I=Internet Transaction]
  CredPmnts Int(6) No. of Credit Payments default=1
  PlCrdStat nVarChar(4) Pelecard Debit Status default=-1
  MagnetStr nVarChar(40) Magnetic Stripe Content
  SpiltCred VarChar(1) Split Credit Voucher Payment default=N [Y=Yes, N=No]
  ConsolNum Int(11) Vendor Credit Code default=-1 ->OPVL
  ObjType nVarChar(20) Object Type default=24 ->ADP1
  LogInstanc Int(11) Log Instance default=0

<!-- source: erpref.com (schema IP: SAP) | version: SAP Business One 9.3 | verified: 2026-10-01 -->
# RCC4 - Incoming Payment - Credit Vouchers
Module: Banking | 35 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: LineId, DocNum
Fields (name type(len) description [values] ->parent table):
  DocNum Int(11) Document Number ->ORCT
  LineId Int(11) Row Number
  AcctCode nVarChar(15) Credit Card default=-1 ->OCRC
  SumApplied Num(19,6) Credit Amount
  AppliedFC Num(19,6) Credit Card Number
  AppliedSys Num(19,6) Credit Card Validity
  Descrip nVarChar(250) Voucher Number
  VatGroup nVarChar(8) ID Number ->OVTG
  VatPrcnt Num(19,6) Telephone
  AcctName nVarChar(100) Payment Method Code default=-1
  ObjType nVarChar(20) Number of Payments default=1 ->ADP1
  LogInstanc Int(11) First Payment Date
  OcrCode nVarChar(8) Distribution Rule ->OOCR
  Project nVarChar(20) Project Code ->OPRJ
  GrossAmnt Num(19,6) Gross Amount
  GrssAmntFC Num(19,6) Gross Amount (FC)
  GrssAmntSC Num(19,6) Gross Amount (SC)
  AmntBase VarChar(1) Base Amount [E=Exclude Tax, I=Include Tax]
  VatAmnt Num(19,6) VAT Amount
  VatAmntFC Num(19,6) VAT Amount (FC)
  VatAmntSC Num(19,6) VAT Amount (SC)
  UserChaVat VarChar(1) User Changed VAT default=N [N=No, Y=Yes]
  TaxTypeID Int(11) Tax Type Component ID ->OSTT
  OcrCode2 nVarChar(8) Distribution Rule2 ->OOCR
  OcrCode3 nVarChar(8) Distribution Rule3 ->OOCR
  OcrCode4 nVarChar(8) Distribution Rule4 ->OOCR
  OcrCode5 nVarChar(8) Distribution Rule5 ->OOCR
  Section Int(11) Section ->OSEC
  AsseType VarChar(1) Assessee Type [C=Company, P=Others]
  LocCode Int(11) Location Code ->OLCT
  MatType Int(11) Material Type default=0
  EquVatPer Num(19,6) Equalization Tax Rate
  EquVatSum Num(19,6) Equalization VAT Amount
  EquVatSumF Num(19,6) Equalization VAT Amount (FC)
  EquVatSumS Num(19,6) Equalization VAT Amount (SC)

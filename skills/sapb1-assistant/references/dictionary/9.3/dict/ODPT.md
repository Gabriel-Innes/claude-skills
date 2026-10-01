<!-- source: erpref.com (schema IP: SAP) | version: SAP Business One 9.3 | verified: 2026-10-01 -->
# ODPT - Postdated Deposit
Module: Banking | 36 columns | ObjType: 76
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: DeposId
Fields (name type(len) description [values] ->parent table):
  DeposId Int(11) Payment Internal ID default=0
  DeposType VarChar(1) Payment Type default=K [K=Check Deposit, V=Credit Deposit]
  DeposDate Date(8) Payment Date
  DeposCurr nVarChar(3) Currency for Payments
  BanckAcct nVarChar(15) SAP Business One Acct Code f.
  Memo nVarChar(250) Details
  LocTotal Num(19,6) Total (LC)
  FcTotal Num(19,6) Total (FC)
  SysTotal Num(19,6) Total (SC)
  TransAbs Int(11) Journal Entry Key ->OJDT
  Ref1 nVarChar(11) Reference 1
  Ref2 nVarChar(11) Reference 2
  DocRate Num(19,6) Payment Rate
  Splited VarChar(1) Split default=N [Y=Yes, N=No]
  VatAct nVarChar(15) Tax Account
  ComissAct nVarChar(15) Commissions Account
  VatTotal Num(19,6) Total Tax
  Comission Num(19,6) Commission
  ComissDate Date(8) Commission Date
  TaxDate Date(8) Document Date
  DataSource VarChar(1) Data Source default=N [N=Unknown, I=Interface, U=Update, M=Import, O=DI API, A=Doc. Generation Wizard, D=Restore Wizard, P=Partner Implementation, T=Year Transfer]
  ObjType nVarChar(20) Object Type ->ADP1
  FinncPriod Int(11) Posting Period ->OFPR
  VatTotlSys Num(19,6) Total Tax on Input (SC)
  ComissnSys Num(19,6) Total Commission (SC)
  UserSign Int(6) User Signature ->OUSR
  CommisVat nVarChar(8) Commission VAT Group ->OVTG
  Project nVarChar(20) Project Code ->OPRJ
  OcrCode nVarChar(8) Distribution Rule ->OOCR
  OcrCode2 nVarChar(8) Distribution Rule 2 ->OOCR
  OcrCode3 nVarChar(8) Distribution Rule 3 ->OOCR
  OcrCode4 nVarChar(8) Distribution Rule 4 ->OOCR
  OcrCode5 nVarChar(8) Distribution Rule 5 ->OOCR
  ComisFC Num(19,6) Total Commission (FC)
  VatTotlFC Num(19,6) Total Tax on Input (FC)
  ComisCurr nVarChar(3) Commission Currency

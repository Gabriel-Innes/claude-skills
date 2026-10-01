<!-- source: erpref.com (schema IP: SAP) | version: SAP Business One 9.3 | verified: 2026-10-01 -->
# ARC5 - Reciept log vat adjustment-History
Module: Banking | 26 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: LogInstanc, ObjType, LineSeq, DocNum
Fields (name type(len) description [values] ->parent table):
  DocNum Int(11) Document No. - History ->ORCT
  InvEntry Int(11) Invoice Key - History ->OINV
  LineNum Int(11) Row Number - History
  ObjType nVarChar(20) Object Type - History ->ADP1
  LogInstanc Int(11) Log Instance - History default=0
  VatGroup nVarChar(8) Tax Group - History ->OVTG
  VatPrcnt Num(19,6) Tax % - History
  VatSum Num(19,6) Tax Amount - History
  BaseSum Num(19,6) Base Amount - History
  NoDedSum Num(19,6) Non-Deductible Amount
  BaseSumFc Num(19,6) Base Amount (FC)
  VatSumFc Num(19,6) Tax Amount (FC)
  NoDedSumFc Num(19,6) Non-Deductible Amount (FC)
  BaseSumSc Num(19,6) Base Amount (SC)
  NoDedSumSc Num(19,6) Non-Deductible Amount (SC)
  VatSumSc Num(19,6) VAT Amount (SC)
  CashDiscAc nVarChar(15) Cash Discount Account
  BaseObjArr Int(6) Base Object Array Number default=1
  BaseObj Int(11) Base Object default=13
  InstlmntId Int(6) Installment ID default=0
  GroupNum Int(11) Group Number default=0
  LineSeq Int(11) Row Sequence default=-1
  EquVatPer Num(19,6) Equalization Tax %
  EquVatSum Num(19,6) Total Equalization Tax
  EquVatSumF Num(19,6) Total Equalization Tax (FC)
  EquVatSumS Num(19,6) Total Equalization Tax (SC)

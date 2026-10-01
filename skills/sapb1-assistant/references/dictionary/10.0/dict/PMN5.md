<!-- source: REFDB.chm (SAP Business One SDK 10.0 - Database Tables Reference) | version: SAP Business One 10.0 | verified: 2026-10-01 -->
# PMN5 - Payment - VAT Adjustment
Module: Banking | 26 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: DocNum, LineSeq
Fields (name type(len) description [values] ->parent table):
  DocNum Int(11) Document Number ->OPMN
  InvEntry Int(11) Invoice No.
  LineNum Int(11) Row Number
  ObjType nVarChar(20) Object Type default=24 ->ADP1
  LogInstanc Int(11) Log Instance default=0
  VatGroup nVarChar(8) Tax Group ->OVTG
  VatPrcnt Num(19,6) Tax %
  VatSum Num(19,6) Tax Amount
  BaseSum Num(19,6) Base Amount
  NoDedSum Num(19,6) Nondeductible Amount
  BaseSumFc Num(19,6) Base Amount (FC)
  VatSumFc Num(19,6) Tax Amount (FC)
  NoDedSumFc Num(19,6) Nondeductible Amount (FC)
  BaseSumSc Num(19,6) Base Amount (SC)
  NoDedSumSc Num(19,6) Nondeductible Amount (SC)
  VatSumSc Num(19,6) VAT Amount (SC)
  CashDiscAc nVarChar(15) Cash Discount Account
  BaseObjArr Int(6) Base Object Array Number default=1
  BaseObj Int(11) Base Object default=13
  InstlmntId Int(6) Installment ID default=0
  GroupNum Int(11) Group Number default=0
  LineSeq Int(11) Row Sequence
  EquVatPer Num(19,6) Equalization Tax %
  EquVatSum Num(19,6) Total Equalization Tax
  EquVatSumF Num(19,6) Total Equalization Tax (FC)
  EquVatSumS Num(19,6) Total Equalization Tax (SC)

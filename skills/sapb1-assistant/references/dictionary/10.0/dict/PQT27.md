<!-- source: REFDB.chm (SAP Business One SDK 10.0 - Database Tables Reference) | version: SAP Business One 10.0 | verified: 2026-10-01 -->
# PQT27 - Purchase Quotation - E-Books(GR) Rows
Module: Marketing Documents | 29 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: DocEntry, LineNum
  RELATE_ROW: DocEntry, RelateType, RelateLine, GroupNum
Fields (name type(len) description [values] ->parent table):
  DocEntry Int(11) Document Internal ID ->OPQT
  LineNum Int(11) Row Number
  RelateType Int(11) Relation Type default=-1 [1=Row, 2=Row Expenses, 3=Document Expenses, 13=Distributed Freights, -1=Manual]
  RelateLine Int(11) Relation Row Number default=-1
  GroupNum Int(11) Group Number default=-1
  LineTotal Num(19,6) Line Total
  LineTotalF Num(19,6) Line Total (FC)
  LineTotalS Num(19,6) Line Total (SC)
  InClassTyp Int(11) Income Classification Type ->OICP
  InClassCat Int(11) Income Classification Category ->OICC
  ExClassTyp Int(11) Expense Classification Type ->OECP
  ExClassCat Int(11) Expense Classification Cat. ->OECC
  VatCate Int(11) VAT Category
  NetValue Num(19,6) Net Value
  NetValueFC Num(19,6) Net Value (FC)
  NetValueSC Num(19,6) Net Value (SC)
  VatAmount Num(19,6) VAT Amount
  VatAmFC Num(19,6) VAT Amount (FC)
  VatAmSC Num(19,6) VAT Amount (SC)
  WtPercCat Int(11) Withheld Percentage Category
  WtAmount Num(19,6) Withheld Amount
  WtAmountFC Num(19,6) Withheld Amount (FC)
  WtAmountSC Num(19,6) Withheld Amount (SC)
  ObjectType nVarChar(20) Object Type default=13 ->ADP1
  LogInstanc Int(11) Log Instance default=0
  WtCategory VarChar(1) Withheld Category [I=Invoice, P=Payment]
  VATClassTy Int(11) VAT Classification Type ->OECP
  VATClassCa Int(11) VAT Classification Category ->OECC
  EBVatExCau Int(11) VAT Exemption Cause ->OVEC

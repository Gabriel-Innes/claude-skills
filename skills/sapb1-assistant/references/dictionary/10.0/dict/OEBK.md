<!-- source: REFDB.chm (SAP Business One SDK 10.0 - Database Tables Reference) | version: SAP Business One 10.0 | verified: 2026-10-01 -->
# OEBK - E-Books
Module: General | 27 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: AbsEntry
  UID U: UID
  MARK U: MARK
Fields (name type(len) description [values] ->parent table):
  AbsEntry Int(11) E-Books Abs. Entry
  MARK nVarChar(40) MARK
  CancelMARK nVarChar(40) Cancel MARK
  UID nVarChar(50) UID
  IssueVATID nVarChar(64) Issuer VAT Number
  CPVATID nVarChar(64) Counterpart VAT Number
  Series nVarChar(16) Series
  AA nVarChar(200) AA
  IssueDate Date(8) Issue Date
  InvoiceTyp nVarChar(100) Invoice Type
  Currency nVarChar(200) Currency
  TlNetVal Num(19,6) Total Net Value
  TlVatAmn Num(19,6) Total VAT Amount
  TlWheldAmn Num(19,6) Total Withheld Amount
  TlGrossVal Num(19,6) Total Gross Value
  LinkDocTyp Int(11) Linked Doc. Type [18=A/P Invoices, 19=A/P Credit Memos, 30=Journal Entries, 0=, -1=]
  LinkDocEnt Int(11) Linked Doc. Entry
  IsNegMark VarChar(1) Is Negative MARK default=N [N=No, Y=Yes]
  LogInstanc Int(11) Log Instance default=0
  UserSign Int(6) User Signature ->OUSR
  CreateDate Date(8) Creation Date
  CreateTS Int(11) Create Time - Incl. Secs
  UpdateDate Date(8) Date of Update
  UpdateTS Int(11) Update Full Time
  SourceECM8 Int(11) LogNum of Source ECM8
  ObjType nVarChar(20) Object Type default=234003013 [234003013=E-Books Expense] ->ADP1
  UserSign2 Int(6) Updating User ->OUSR

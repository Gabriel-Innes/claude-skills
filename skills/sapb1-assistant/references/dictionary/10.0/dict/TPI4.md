<!-- source: REFDB.chm (SAP Business One SDK 10.0 - Database Tables Reference) | version: SAP Business One 10.0 | verified: 2026-10-01 -->
# TPI4 - Purchase Tax Invoice - Linked Down Payments
Module: Marketing Documents | 23 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: DocEntry, LineNum
  DOC_ENTRY: DocEntry
Fields (name type(len) description [values] ->parent table):
  DocEntry Int(11) Internal Number
  ObjType Int(11) Object Type
  LogInstanc Int(11) Log Instance default=0
  LineNum Int(11) Line Number
  DpmObjType Int(11) Down Payment Type
  DpmDocEntr Int(11) Down Payment Entry
  DpmDocNum Int(11) Down Payment No.
  PmnObjType Int(11) Payment Type
  PmnDocEntr Int(11) Payment Entry
  PmnDocNum Int(11) Payment Number
  PmnTaxDate Date(8) Payment Date
  TrsfrDate Date(8) Transfer Date
  TrsfrRef nVarChar(27) Intended Purpose
  DrawnSum Num(19,6) Drawn Amount
  DrawnSumFc Num(19,6) Drawn Amount (FC)
  DrawnSumSc Num(19,6) Drawn Amount (SC)
  DocCur nVarChar(3) Document Currency
  Vat Num(19,6) Tax Amount
  VatFc Num(19,6) Tax Amount (FC)
  VatSc Num(19,6) Tax Amount (SC)
  Gross Num(19,6) Gross Amount
  GrossFc Num(19,6) Gross Amount (FC)
  GrossSc Num(19,6) Gross Amount (SC)

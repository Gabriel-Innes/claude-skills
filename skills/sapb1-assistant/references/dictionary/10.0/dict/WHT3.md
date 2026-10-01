<!-- source: REFDB.chm (SAP Business One SDK 10.0 - Database Tables Reference) | version: SAP Business One 10.0 | verified: 2026-10-01 -->
# WHT3 - Value Range
Module: Finance | 10 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: WTCode, LineNum, SeqNum
Fields (name type(len) description [values] ->parent table):
  AbsId Int(11) Internal Number
  WTCode nVarChar(4) WTax Code ->OWHT
  EfctFrom Date(8) Effective From
  ValueFrom Num(19,6) Value From
  Deduct Num(19,6) WTax to Be Deductible
  Rate Num(19,6) Rate
  WTCur nVarChar(3) Currency
  LogInstanc Int(11) Log Instance default=0
  LineNum Int(11) Row Number
  SeqNum Int(11) Sequence Number

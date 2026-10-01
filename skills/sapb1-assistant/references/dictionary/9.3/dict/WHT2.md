<!-- source: erpref.com (schema IP: SAP) | version: SAP Business One 9.3 | verified: 2026-10-01 -->
# WHT2 - Withholding Tax Definition - Rows2
Module: Finance | 10 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: SeqNum, LineNum, Code
Fields (name type(len) description [values] ->parent table):
  AbsEntry Int(11) Numerator
  Code nVarChar(4) Tax Code ->OWHT
  EffectDate Date(8) Date Effective
  Rate Num(19,6) Tax Rate
  MinAmount Num(19,6) Min. Amount
  MaxAmount Num(19,6) Max. Amount
  WTCUR nVarChar(3) Progressive Tax Currency ->OCRN
  LogInstanc Int(11) Log Instance default=0
  LineNum Int(11) Row Number
  SeqNum Int(11) Sequence Number

<!-- source: REFDB.chm (SAP Business One SDK 10.0 - Database Tables Reference) | version: SAP Business One 10.0 | verified: 2026-10-01 -->
# CTG1 - Installment Layout
Module: Banking | 6 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: CTGCode, IntsNo
  ABS_ENTRY U: CTGCode, InstMonth, InstDays
Fields (name type(len) description [values] ->parent table):
  CTGCode Int(6) Payment Method Code ->OCTG
  IntsNo Int(6) Installment No.
  InstMonth Int(6) Installment Month default=0
  InstDays Int(6) Installment Days default=0
  InstPrcnt Num(19,6) Installment %
  LogInstanc Int(11) Log Instance default=0

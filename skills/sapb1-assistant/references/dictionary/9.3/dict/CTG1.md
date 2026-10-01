<!-- source: erpref.com (schema IP: SAP) | version: SAP Business One 9.3 | verified: 2026-10-01 -->
# CTG1 - Installment Layout
Module: Banking | 5 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: IntsNo, CTGCode
  ABS_ENTRY U: InstDays, InstMonth, CTGCode
Fields (name type(len) description [values] ->parent table):
  CTGCode Int(6) Payment Method Code ->OCTG
  IntsNo Int(6) Installment No.
  InstMonth Int(6) Installment Month default=0
  InstDays Int(6) Installment Days default=0
  InstPrcnt Num(19,6) Installment %

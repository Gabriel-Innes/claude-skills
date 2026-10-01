<!-- source: erpref.com (schema IP: SAP) | version: SAP Business One 9.3 | verified: 2026-10-01 -->
# IRR1 - Input Service Distribution - Recipient Credit Memo
Module: Marketing Documents | 6 columns
Indexes (name: columns; first = primary key; U = unique) - WARNING: multi-column key order here is reversed vs SAP's 10.0 reference (read as a set; see references/dictionary/INDEX.md):
  PRIMARY U: LineNum, DocEntry
Fields (name type(len) description [values] ->parent table):
  DocEntry Int(11) Document Internal ID ->OIRI
  LineNum Int(11) Row Number
  StaType Int(11) GST Tax Type [-100=CGST, -110=SGST, -120=IGST, -130=Cess GST, -150=UTGST]
  TaxAcct nVarChar(15) Tax Account
  RecAmnt Num(19,6) Received Amount
  ElgAmnt Num(19,6) Eligible Amount

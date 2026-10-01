<!-- source: REFDB.chm (SAP Business One SDK 10.0 - Database Tables Reference) | version: SAP Business One 10.0 | verified: 2026-10-01 -->
# IRI1 - ISD Recipient Invoice Lines
Module: Marketing Documents | 6 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: DocEntry, LineNum
Fields (name type(len) description [values] ->parent table):
  DocEntry Int(11) Document Internal ID ->OIRI
  LineNum Int(11) Row Number
  StaType Int(11) GST Tax Type [-100=CGST, -110=SGST, -120=IGST, -130=Cess GST, -150=UTGST]
  TaxAcct nVarChar(15) Tax Account
  RecAmnt Num(19,6) Received Amount
  ElgAmnt Num(19,6) Eligible Amount

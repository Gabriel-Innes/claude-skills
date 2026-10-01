<!-- source: REFDB.chm (SAP Business One SDK 10.0 - Database Tables Reference) | version: SAP Business One 10.0 | verified: 2026-10-01 -->
# AIS2 - Input Service Distribution - Row Detail
Module: Marketing Documents | 8 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: DocEntry, LineNum, TargetLoc, TarTaxAcct, TarStaType
Fields (name type(len) description [values] ->parent table):
  DocEntry Int(11) Document Internal ID ->OISD
  LineNum Int(11) Row Number
  TargetLoc Int(11) Target Location Code
  TarLocName nVarChar(100) Target Location Name
  TarStaType Int(11) Target GST Tax Type [-100=CGST, -110=SGST, -120=IGST, -130=Cess GST, -150=UTGST]
  TarTaxAcct nVarChar(15) Target Tax Account Code ->OACT
  AllocAmnt Num(19,6) Allocated Amount
  ITCType VarChar(1) ITC Type default=E [E=Eligible, I=Ineligible]

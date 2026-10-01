<!-- source: erpref.com (schema IP: SAP) | version: SAP Business One 9.3 | verified: 2026-10-01 -->
# ISD2 - ISD - Target Lines
Module: Marketing Documents | 8 columns
Indexes (name: columns; first = primary key; U = unique) - WARNING: multi-column key order here is reversed vs SAP's 10.0 reference (read as a set; see references/dictionary/INDEX.md):
  PRIMARY U: TarTaxAcct, TarStaType, TargetLoc, LineNum, DocEntry
Fields (name type(len) description [values] ->parent table):
  DocEntry Int(11) Document Internal ID ->OISD
  LineNum Int(11) Row Number
  TargetLoc Int(11) Target Location Code
  TarLocName nVarChar(100) Target Location Name
  TarStaType Int(11) Target GST Tax Type [-100=CGST, -110=SGST, -120=IGST, -130=Cess GST, -150=UTGST]
  TarTaxAcct nVarChar(15) Target Tax Account Code ->OACT
  AllocAmnt Num(19,6) Allocated Amount
  ITCType VarChar(1) ITC Type default=E [E=Eligible, I=Ineligible]

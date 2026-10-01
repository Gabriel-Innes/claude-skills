<!-- source: erpref.com (schema IP: SAP) | version: SAP Business One 9.3 | verified: 2026-10-01 -->
# ISC1 - Input Service Distribution - Credit Memo Lines
Module: Marketing Documents | 13 columns
Indexes (name: columns; first = primary key; U = unique) - WARNING: multi-column key order here is reversed vs SAP's 10.0 reference (read as a set; see references/dictionary/INDEX.md):
  PRIMARY U: LineNum, DocEntry
Fields (name type(len) description [values] ->parent table):
  DocEntry Int(11) Document Internal ID ->OISI
  LineNum Int(11) Row Number
  SourceType Int(11) Source Document Type [18=GST Tax Invoice, 19=GST Credit Memo, -18=GST Debit Memo]
  SourceNo Int(11) Source Document No.
  SrcEntry Int(11) Source Document Entry
  SrcStaType Int(11) Source GST Tax Type [-100=CGST, -110=SGST, -120=IGST, -130=Cess GST, -150=UTGST]
  SrcTaxAcct nVarChar(15) Source Tax Account
  SACEntry Int(11) SAC Entry
  TarStaType Int(11) Target GST Tax Type [-100=CGST, -110=SGST, -120=IGST, -130=Cess GST, -150=UTGST]
  TarTaxAcct nVarChar(15) Target Tax Account
  DistAmnt Num(19,6) Credit Amount to Distribute
  SrcSubType nVarChar(2) Source Document Subtype
  ITCType VarChar(1) ITC Type default=E [E=Eligible, I=Ineligible]

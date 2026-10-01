<!-- source: REFDB.chm (SAP Business One SDK 10.0 - Database Tables Reference) | version: SAP Business One 10.0 | verified: 2026-10-01 -->
# ISD1 - ISD - Source Lines
Module: Marketing Documents | 14 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: DocEntry, LineNum
Fields (name type(len) description [values] ->parent table):
  DocEntry Int(11) Document Internal ID ->OISD
  LineNum Int(11) Row Number
  SourceType Int(11) Source Document Type [18=GST Tax Invoice, 19=GST Credit Memo, -18=GST Debit Memo]
  SourceNo Int(11) Source Document No.
  SrcEntry Int(11) Source Document Entry
  SrcLocCode Int(11) Source Location Code ->OLCT
  SrcLocName nVarChar(100) Source Location Name
  SrcStaType Int(11) Source GST Tax Type [-100=CGST, -110=SGST, -120=IGST, -130=Cess GST, -150=UTGST]
  SrcTaxAcct nVarChar(15) Source Tax Account
  SACEntry Int(11) SAC Entry
  CrdtAmnt Num(19,6) Total Credit Amount
  DistAmnt Num(19,6) Credit Amount to Distribute
  SrcSubType nVarChar(2) Source Document Subtype
  ITCType VarChar(1) ITC Type default=E [E=Eligible, I=Ineligible]

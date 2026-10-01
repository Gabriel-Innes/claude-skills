<!-- source: REFDB.chm (SAP Business One SDK 10.0 - Database Tables Reference) | version: SAP Business One 10.0 | verified: 2026-10-01 -->
# TPW5 - Challan Information
Module: Banking | 5 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: AbsEntry
Fields (name type(len) description [values] ->parent table):
  AbsEntry Int(11) Absolute Entry No ->OTPW
  ChlnDate Date(8) Challan Date
  ChlnNo nVarChar(50) Challan No
  ChlnBank nVarChar(100) Challan Bank
  ChlnMemo nVarChar(100) Challan Memo

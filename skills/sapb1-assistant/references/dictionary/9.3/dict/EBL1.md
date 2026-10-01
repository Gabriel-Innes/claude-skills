<!-- source: erpref.com (schema IP: SAP) | version: SAP Business One 9.3 | verified: 2026-10-01 -->
# EBL1 - E-Balance Report Data
Module: Reports | 7 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: LineNum, AbsEntry
Fields (name type(len) description [values] ->parent table):
  AbsEntry Int(11) Internal Key
  LineNum Int(11) Line Number
  ReportType Int(11) Report Type default=0 [0=, 1=E-General Information GCD (Global Common Document), 2=e-Balance Sheet, 3=e-Profit and Loss, 4=E-Taxable Profit and Loss, 5=E-Income Usage, 6=E-Assets History Sheet, 7=Shareholder, 8=Account Verification, -1=Global Common Data, -2=Global Common Report Data]
  Selected VarChar(1) Selected default=Y [Y=Yes, N=No]
  Mandatory VarChar(1) Mandatory
  DocType VarChar(1) Document Type [0=XBRL]
  DocContent Text(16) Document Content

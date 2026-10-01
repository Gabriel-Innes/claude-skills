<!-- source: erpref.com (schema IP: SAP) | version: SAP Business One 9.3 | verified: 2026-10-01 -->
# UDG1 - User Defaults - Documents
Module: Administration | 15 columns
Indexes (name: columns; first = primary key; U = unique) - WARNING: multi-column key order here is reversed vs SAP's 10.0 reference (read as a set; see references/dictionary/INDEX.md):
  PRIMARY U: ObjType, Code
Fields (name type(len) description [values] ->parent table):
  Code nVarChar(8) Code
  ObjType nVarChar(20) Object Type
  Copies Int(6) No. of Copies default=1
  PrintOnAdd VarChar(1) Add & Print default=N [Y=Yes, N=No]
  ExprtOnAdd VarChar(1) Add & Export default=N [Y=Yes, N=No]
  RoundSums VarChar(1) Totals Rounding default=N [Y=Yes, N=No]
  Remark Text(16) Permanent Remark
  PrintSums VarChar(1) Print Totals default=Y [Y=Yes, N=No]
  VndrNum VarChar(1) Print Mfr Catalog No. default=N [Y=Yes, N=No]
  PrnDscnt VarChar(1) Print Discount Data default=Y [Y=Yes, N=No]
  HandCopies Int(6) No. of Copies for Manual Doc. default=1
  EngKBItem VarChar(1) English Keyboard Entering Item No. default=N [Y=Yes, N=No]
  EngKBCard VarChar(1) English Keyboard Entering BP Code default=N [Y=Yes, N=No]
  EmailOnAdd VarChar(1) Add & E-Mail default=N [Y=Yes, N=No]
  PDFOnAdd VarChar(1) Add & Export to PDF default=N [Y=Yes, N=No]

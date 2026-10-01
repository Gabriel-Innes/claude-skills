<!-- source: REFDB.chm (SAP Business One SDK 10.0 - Database Tables Reference) | version: SAP Business One 10.0 | verified: 2026-10-01 -->
# AEC5 - List of Canceled Reconciliations for Actions in Electronic Communication
Module: Reports | 14 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: AbsEntry, LogNum, LogInstanc
Fields (name type(len) description [values] ->parent table):
  AbsEntry Int(11) Internal ID ->ECM2
  LogNum Int(11) Log Number
  DocType Int(11) Document Type
  DocAbs Int(11) Document Abs. Entry
  DocNum Int(11) Document Number
  UUID nVarChar(50) UUID
  UserSign Int(6) User Signature ->OUSR
  CreateDate Date(8) Creation Date
  CreateTS Int(11) Create Time - Incl. Sec.
  UserSign2 Int(6) Updating User ->OUSR
  UpdateDate Date(8) Update Date
  UpdateTS Int(11) Update Time - Incl. Sec.
  LogInstanc Int(6) Log Instance
  Code Int(11) Communication Type or Protocol [0=Invalid, 1=GEN, 2=EET, 3=CFDI, 4=FPA, 5=MTD, 6=EWB, 7=PEPPOL, 8=HOI, 9=MYF, 10=EIS, 11=IIS, 12=IIS_ANNUAL, 13=DIGIPOORT, 14=E-Books, 17=E-Billing]

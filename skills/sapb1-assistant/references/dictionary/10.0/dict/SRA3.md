<!-- source: REFDB.chm (SAP Business One SDK 10.0 - Database Tables Reference) | version: SAP Business One 10.0 | verified: 2026-10-01 -->
# SRA3 - Scheduled Report Recipients
Module: Reports | 15 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: ActionCode, RecipCode
  USER: Name
Fields (name type(len) description [values] ->parent table):
  ActionCode Int(11) Action Code ->OSRA
  RecipCode Int(11) Recipient Code
  ObjType nVarChar(20) Object Type
  ObjCode nVarChar(50) Object Code
  Name nVarChar(155) Name
  SendInter VarChar(1) Send Internally default=N [Y=Yes, N=No]
  SendEmail VarChar(1) Send as E-Mail default=N [Y=Yes, N=No]
  SendSMS VarChar(1) Send as SMS default=N [Y=Yes, N=No]
  Email nVarChar(100) E-Mail Address
  Number nVarChar(100) Telephone Number
  AttachDAG VarChar(1) Attach DAG default=N [Y=Yes, N=No]
  AttachPDF VarChar(1) Attach PDF default=N [Y=Yes, N=No]
  AttachHTML VarChar(1) Attach HTML default=N
  AttachXML VarChar(1) Attach XML default=N [Y=Yes, N=No]
  ShowResult VarChar(1) Results Visible to User default=Y [Y=Yes, N=No]

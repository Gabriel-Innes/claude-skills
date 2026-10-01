<!-- source: REFDB.chm (SAP Business One SDK 10.0 - Database Tables Reference) | version: SAP Business One 10.0 | verified: 2026-10-01 -->
# EJB1 - ERV-JAb Wizard Signing Persons
Module: Reports | 10 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: WizardID, LineNum
Fields (name type(len) description [values] ->parent table):
  WizardID Int(11) Wizard ID ->OEJB
  LineNum Int(11) Row Number
  Title nVarChar(20) Title
  FirstName nVarChar(38) First Name
  Surname nVarChar(38) Surname
  CommID nVarChar(3) Commercial ID
  DateOfBrth Date(8) Date of Birth
  DateOfSign Date(8) Date of Signing
  AbsEntry Int(11) Internal Number ->OEJD
  LineNumEJD Int(11) Row Number EJD1 ->EJD1

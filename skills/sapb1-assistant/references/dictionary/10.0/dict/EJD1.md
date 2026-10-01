<!-- source: REFDB.chm (SAP Business One SDK 10.0 - Database Tables Reference) | version: SAP Business One 10.0 | verified: 2026-10-01 -->
# EJD1 - ERV-JAb Signing Persons List
Module: Reports | 8 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: AbsEntry, LineNum
Fields (name type(len) description [values] ->parent table):
  AbsEntry Int(11) Internal Number ->OEJD
  LineNum Int(11) Row Number
  Title nVarChar(20) Title
  FirstName nVarChar(38) First Name
  Surname nVarChar(38) Surname
  CommID nVarChar(3) Commercial ID
  DateOfBrth Date(8) Date of Birth
  Active VarChar(1) Active default=N [Y=Yes, N=No]

<!-- source: REFDB.chm (SAP Business One SDK 10.0 - Database Tables Reference) | version: SAP Business One 10.0 | verified: 2026-10-01 -->
# UDO1 - User-Defined Objects - Child
Module: Administration | 5 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: Code, SonNum
Fields (name type(len) description [values] ->parent table):
  Code nVarChar(20) Code
  SonNum Int(11) Child No.
  TableName nVarChar(19) Table Name ->OUTB
  LogName nVarChar(20) Log Table Name
  SonName nVarChar(100) Child Name default=' '

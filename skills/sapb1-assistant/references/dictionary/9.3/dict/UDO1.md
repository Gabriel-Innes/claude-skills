<!-- source: erpref.com (schema IP: SAP) | version: SAP Business One 9.3 | verified: 2026-10-01 -->
# UDO1 - User-Defined Objects - Child
Module: Administration | 5 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: SonNum, Code
Fields (name type(len) description [values] ->parent table):
  Code nVarChar(20) Code
  SonNum Int(11) Child No.
  TableName nVarChar(19) Table Name ->OUTB
  LogName nVarChar(20) Log Table Name
  SonName nVarChar(100) Child Name

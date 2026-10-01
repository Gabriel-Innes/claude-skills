<!-- source: REFDB.chm (SAP Business One SDK 10.0 - Database Tables Reference) | version: SAP Business One 10.0 | verified: 2026-10-01 -->
# OUTB - User Tables
Module: Administration | 9 columns | ObjType: 153
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: TableName
Fields (name type(len) description [values] ->parent table):
  TableName nVarChar(20) Table Name
  Descr nVarChar(30) Description
  TblNum Int(11) Table number
  ObjectType nVarChar(20) Object Type default=0 [0=No Object, 1=Master Data, 2=Master Data Rows, 3=Document, 4=Document Rows, 5=No Object with Auto. Increment]
  UsedInObj nVarChar(20) Used in Object
  LogTable nVarChar(20) Log Table
  Archivable VarChar(1) Archivable default=N [Y=Yes, N=No]
  ArchivDate nVarChar(18) Archive Date
  DisplyMenu VarChar(1) Display Menu default=Y [Y=Yes, N=No]

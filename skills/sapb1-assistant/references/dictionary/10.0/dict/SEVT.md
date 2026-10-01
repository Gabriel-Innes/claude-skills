<!-- source: REFDB.chm (SAP Business One SDK 10.0 - Database Tables Reference) | version: SAP Business One 10.0 | verified: 2026-10-01 -->
# SEVT - 
Module: General | 13 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: SequenceID
  SOURCE_DB: SourceDB, ObjectType, FieldValue
Fields (name type(len) description [values] ->parent table):
  SequenceID Identity(11) Sequence ID
  SourceDB nVarChar(100) Event source database
  Timestamp nVarChar(20) Event timestamp
  Status nVarChar(50) Event status
  Retry Int(11) Sending event retries
  ObjectType nVarChar(30) Object type
  TransType VarChar(1) Transaction type
  FieldsInKe Int(11) Number of fields in key
  FieldNames nVarChar(254) Names of key fields
  FieldValue nVarChar(254) Values of key fields
  UserID nVarChar(155) Modified by user
  USER_CODE nVarChar(25) User code
  SAPPassprt Text(16) Extended SAP Passport

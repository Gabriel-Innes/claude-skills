<!-- source: erpref.com (schema IP: SAP) | version: SAP Business One 9.3 | verified: 2026-10-01 -->
# SEVT - SEVT
Module: General | 13 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: SequenceID
  SOURCE_DB: FieldValue, ObjectType, SourceDB
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
  USER_CODE nVarChar(8) User code
  SAPPassprt Text(16) Extended SAP Passport

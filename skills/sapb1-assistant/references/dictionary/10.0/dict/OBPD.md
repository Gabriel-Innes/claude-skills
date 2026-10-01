<!-- source: REFDB.chm (SAP Business One SDK 10.0 - Database Tables Reference) | version: SAP Business One 10.0 | verified: 2026-10-01 -->
# OBPD - Blocked Personal Data
Module: Administration | 15 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: AbsEntry
  DATA_SUBJ: DatSubType, DatSubKey, DatSubKey2
  TABL_FIELD: TableName, KeyValue1, KeyValue2, KeyValue3, KeyValue4, KeyValue5, FieldName
Fields (name type(len) description [values] ->parent table):
  AbsEntry Int(11) Internal Number
  DatSubType nVarChar(4) Data Subject Type [OCRD=Business Partner, OCPR=Contact Person, OHEM=Employee, OUSR=User, CPN1=Campaign - BP]
  DatSubKey nVarChar(15) Data Subject Key No.1
  DatSubKey2 nVarChar(50) Data Subject Key No.2
  TableName nVarChar(20) Table Name
  KeyValue1 nVarChar(50) Key Value No.1
  KeyValue2 nVarChar(50) Key Value No.2
  KeyValue3 nVarChar(50) Key Value No.3
  KeyValue4 nVarChar(50) Key Value No.4
  KeyValue5 nVarChar(50) Key Value No.5
  FieldName nVarChar(50) Field Name
  EncryptVal Text(16) Encryption Value
  EncryptIV nVarChar(100) Encryption Initialization Vector
  CreateDate Date(8) Creation Date
  CreateTime Int(11) Creation Time

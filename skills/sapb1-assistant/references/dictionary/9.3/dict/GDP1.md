<!-- source: erpref.com (schema IP: SAP) | version: SAP Business One 9.3 | verified: 2026-10-01 -->
# GDP1 - General Data Protection Wizard - Personal Fields Setup
Module: Reports | 9 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: PfsAbs, AbsEntry
Fields (name type(len) description [values] ->parent table):
  AbsEntry Int(11) Internal Number
  PfsAbs Int(11) Internal Number
  TableName nVarChar(20) Table Name
  FieldName nVarChar(50) Field Name
  RefObjType nVarChar(20) Referenced Object Type
  Category VarChar(1) Category default=N [N=, R=Sales A/R, P=Purchase A/P]
  OrigType VarChar(1) Original Type default=U [U=User Defined, S=Sensitive, P=Personal]
  Type VarChar(1) Type default=N [N=Not Relevant, S=Sensitive, P=Personal]
  Descr nVarChar(254) Description

<!-- source: REFDB.chm (SAP Business One SDK 10.0 - Database Tables Reference) | version: SAP Business One 10.0 | verified: 2026-10-01 -->
# OPFS - Personal Fields Setup
Module: Administration | 16 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: AbsEntry
  SECONDARY U: TableName, FieldName, Category
Fields (name type(len) description [values] ->parent table):
  AbsEntry Int(11) Internal Number
  TableName nVarChar(20) Data Subtype
  FieldName nVarChar(50) Field Name
  RefObjType nVarChar(20) Data Type
  Category VarChar(1) Category default=N [N=, R=Sales A/R, P=Purchase A/P, Q=Purchase Request, A=Inventory Transfers and Requests Sales A/R, B=Inventory Transfers and Requests Purchase A/P, C=Opportunity - Business Partner, D=Opportunity - Business Partner Channel, E=Customer Equipment Card - Business Partner, F=Customer Equipment Card - Direct Partner, L=Landed Cost - Vendor, G=Landed Cost - Broker, X=Payment Results - Business Partner, U=Payment Results - User, H=Incoming Payments, I=Outgoing Payments, J=Sales A/R, K=Purchase A/P, M=Bill of Exchange for Incoming Payments]
  OrigType VarChar(1) Default Data Classification default=U [U=User Defined, S=Sensitive Personal, P=Personal, N=Not Personal]
  UserSign Int(6) User Signature
  UserSign2 Int(6) Updating User
  CreateDate Date(8) Creation Date
  CreateTS Int(11) Create Time - Incl. Secs
  UpdateDate Date(8) Date of Update
  UpdateTS Int(11) Update Full Time
  LogInstanc Int(11) Log Instance default=0
  Type VarChar(1) Data Classification default=N [N=Not Personal, S=Sensitive Personal, P=Personal]
  Descr nVarChar(254) Description
  MaxType VarChar(1) Max. Data Classification default=U [U=User Defined, S=Sensitive Personal, P=Personal]

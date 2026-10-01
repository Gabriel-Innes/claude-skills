<!-- source: erpref.com (schema IP: SAP) | version: SAP Business One 9.3 | verified: 2026-10-01 -->
# APFS - Personal Fields Setup - History
Module: Administration | 15 columns
Indexes (name: columns; first = primary key; U = unique) - WARNING: multi-column key order here is reversed vs SAP's 10.0 reference (read as a set; see references/dictionary/INDEX.md):
  PRIMARY U: LogInstanc, AbsEntry
  SECONDARY U: LogInstanc, Category, FieldName, TableName
Fields (name type(len) description [values] ->parent table):
  AbsEntry Int(11) Internal Number
  TableName nVarChar(20) Data Subtype
  FieldName nVarChar(50) Field Name
  RefObjType nVarChar(20) Data Type
  Category VarChar(1) Category default=N [N=, R=Sales A/R, P=Purchase A/P, Q=Purchase Request, A=Inventory Transfers and Requests Sales A/R, B=Inventory Transfers and Requests Purchase A/P, C=Opportunity - Business Partner, D=Opportunity - Business Partner Channel, E=Customer Equipment Card - Business Partner, F=Customer Equipment Card - Direct Partner, L=Landed Cost - Vendor, G=Landed Cost - Broker, X=Payment Results - Business Partner, U=Payment Results - User, H=Incoming Payments, I=Outgoing Payments, J=Sales A/R, K=Purchase A/P, M=Bill of Exchange for Incoming Payments]
  OrigType VarChar(1) Default Data Classification default=U [U=User Defined, S=Sensitive Personal, P=Personal]
  UserSign Int(6) User Signature
  UserSign2 Int(6) Updating User
  CreateDate Date(8) Creation Date
  CreateTS Int(11) Create Time - Incl. Secs
  UpdateDate Date(8) Date of Update
  UpdateTS Int(11) Update Full Time
  LogInstanc Int(11) Log Instance default=0
  Type VarChar(1) Data Classification default=N [N=Not Personal, S=Sensitive Personal, P=Personal]
  Descr nVarChar(254) Description

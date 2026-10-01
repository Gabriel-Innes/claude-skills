<!-- source: erpref.com (schema IP: SAP) | version: SAP Business One 9.3 | verified: 2026-10-01 -->
# OLLF - Legal List Format
Module: Administration | 15 columns | ObjType: 410000005
Indexes (name: columns; first = primary key; U = unique) - WARNING: multi-column key order here is reversed vs SAP's 10.0 reference (read as a set; see references/dictionary/INDEX.md):
  PRIMARY U: AbsEntry
  NAME U: Name
Fields (name type(len) description [values] ->parent table):
  AbsEntry Int(11) Internal Number
  Name nVarChar(100) Electronic File Name
  Descr nVarChar(250) Electronic File Description
  MenuGuid nVarChar(32) GUID of Menu Entry
  Version nVarChar(5) Electronic File Version
  SchVersion nVarChar(5) Electronic File Schema Version
  OutPath Text(16) Output Path
  FrmId Int(11) OFRM Internal ID ->OFRM
  UpdateNum Int(11) Update Count default=0
  MenuName nVarChar(100) Menu Name
  MenuPath nVarChar(250) Menu Path
  Assigned nVarChar(10) Format Status default=N [A=Assigned, N=Not Assigned, D=Deleted]
  SboVersion nVarChar(11) Compatible Release Version
  Type nVarChar(5) Format Type default=L [AR=Electronic Document, L=Generic Electronic File, ARA=Electronic Authority Report, INTER=Internally Used, IM=Electronic Document - Input Message, GD=General Electronic Document, GWS=General Mapping for Web Service, GI=General Mapping for Document Import, NFeD=NF-e Invoice Document, NFeC=NF-e Cancelation Document, NFeS=NF-e Number Skipping Request, NFeWS=Web Service Mapping, CFDD=CFDi Electronic Document, CFDP=CFDi Electronic Payment & Reconciliation Document, CFDT=CFDI Electronic Transfer Document, CFDIM=CFDI Electronic Input Message Document, CFDWS=CFDi Electronic Mapping for Web Service, EETD=EET Electronic Document, EETWS=EET Electronic Mapping for Web Service, FPAD=FatturaPA Electronic Document, FPAI=FatturaPA Electronic Document for Import, FPAWS=FatturaPA Electronic Mapping for Web Service]
  SubType nVarChar(6) Format Subtype [I=Intrastat, N=Normal Generic File Format]

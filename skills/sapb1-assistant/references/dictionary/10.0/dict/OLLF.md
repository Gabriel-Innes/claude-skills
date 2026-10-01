<!-- source: REFDB.chm (SAP Business One SDK 10.0 - Database Tables Reference) | version: SAP Business One 10.0 | verified: 2026-10-01 -->
# OLLF - Legal List Format
Module: Administration | 15 columns | ObjType: 410000005
Indexes (name: columns; first = primary key; U = unique):
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
  SboVersion nVarChar(13) Compatible Release Version
  Type nVarChar(5) Format Type default=L [AR=Electronic Document, L=Generic Electronic File, LI=Generic Electronic File for Intrastat, ARA=Electronic Authority Report, INTER=Internally Used, IM=Electronic Document - Input Message, GD=General Electronic Document, GWS=General Mapping for Web Service, GI=General Mapping for Document Import, NFeD=NF-e Invoice Document, NFeC=NF-e Cancelation Document, NFeS=NF-e Number Skipping Request, NFeWS=Web Service Mapping, CFDD=CFDi Electronic Document, CFDP=CFDi Electronic Payment & Reconciliation Document, CFDT=CFDI Electronic Transfer Document, CFDIM=CFDI Electronic Input Message Document, CFDWS=CFDi Electronic Mapping for Web Service, EETD=EET Electronic Document, EETWS=EET Electronic Mapping for Web Service, FPAD=FatturaPA Electronic Document, FPAPD="FatturaPA" Electronic Purchasing Document, FPAI=FatturaPA Electronic Document for Import, FPAWS=FatturaPA Electronic Mapping for Web Service, MTDR=Making Tax Digital Report Submission, MTDWS=Making Tax Digital Mapping for Web Service, EISD=Electronic Document, EISWS=Electronic Document Web Service, IISD1=Electronic Document for IIS INV, IISD2=Electronic Document for IIS PCH, IISD3=Electronic Document for IIS Deferred, IISD4=Electronic Document for IIS JE, IISD5=Electronic Document for IIS JE Received, IISWS=Electronic Document for IIS Web Service, ANND1=Electronic Document for IIS Annual, ANND2=Electronic Document for IIS Annual Cancel, ANNWS=Electronic Document for IIS Annual Web Service, PPLD=Electronic Document for PEPPOL Invoice, PPLWS=Electronic Document for PEPPOL Web Service, PPLCM=Electronic Document for PEPPOL Credit Note, PPLI=Electronic Document for PEPPOL Import, EBKD=Electronic Document for E-Books, EBKI=Electronic Document for E-Books Income Classification, EBKE=Electronic Document for E-Books Expense Classification, EBKR=Electronic Document for E-Books Request Documents, EBKRS=Electronic Document for E-Books Request Submitted Documents, EBKC=Electronic Document for Cancellation, EBKW=Electronic Document for E-Books Web Service, DOXD=Electronic Document for Document Information Extraction, DOXI=Electronic Document for Document Information Extraction Import, EWBD=Electronic Document for E-Way Bill, EINVD=Electronic Document for E-Billing, RTIED=Electronic Document for RTIE, RCTED=Electronic Correction Document for RTIE, RTIWS=Electronic Document for RTIE Web Service]
  SubType nVarChar(6) Format Subtype [=None, I=Intrastat, N=Normal Generic File Format]

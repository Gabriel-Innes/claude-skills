<!-- source: REFDB.chm (SAP Business One SDK 10.0 - Database Tables Reference) | version: SAP Business One 10.0 | verified: 2026-10-01 -->
# CRD12 - BP eDoc Settings
Module: Business Partners | 8 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: CardCode, ProtCode
Fields (name type(len) description [values] ->parent table):
  CardCode nVarChar(15) BP Code ->OCRD
  ProtCode Int(11) Communication Type or Protocol [0=Invalid, 1=GEN, 2=EET, 3=CFDI, 4=FPA, 5=MTD, 6=EWB, 7=PEPPOL, 8=HOI, 10=EIS, 11=IIS, 12=IIS_ANNUAL, 16=RTIE] ->OECM
  GenType VarChar(1) Generation Type [N=Not Relevant, G=Generate, L=Generate Later]
  MapID Int(11) Electronic Document Format Mapping
  LogInstanc Int(11) Log Instance default=0
  VatStruct nVarChar(64) VAT Structure
  ParticipID nVarChar(128) Participant ID
  ElecUID nVarChar(46) Electronic UID

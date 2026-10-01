<!-- source: erpref.com (schema IP: SAP) | version: SAP Business One 9.3 | verified: 2026-10-01 -->
# CRD12 - BP eDoc Settings
Module: Business Partners | 5 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: ProtCode, CardCode
Fields (name type(len) description [values] ->parent table):
  CardCode nVarChar(15) BP Code ->OCRD
  ProtCode Int(11) Communication Type or Protocol [0=Invalid, 1=GEN, 2=EET, 3=CFDI] ->OECM
  GenType VarChar(1) Generation Type default=N [N=Not Relevant, G=Generate, L=Generate Later]
  MapID Int(11) Electronic Document Format Mapping
  LogInstanc Int(11) Log Instance default=0

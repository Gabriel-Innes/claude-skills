<!-- source: REFDB.chm (SAP Business One SDK 10.0 - Database Tables Reference) | version: SAP Business One 10.0 | verified: 2026-10-01 -->
# OPAC - PAC Companies
Module: General | 6 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: PACCode
Fields (name type(len) description [values] ->parent table):
  PACCode nVarChar(16) PAC Code
  PACName nVarChar(100) PAC Name
  PublicKey Text(16) PAC Public Key
  UserSign Int(6) User Signature ->OUSR
  LogInstanc Int(11) Log Instance
  EDFCode Int(11) Communication Type or Protocol [0=Invalid, 1=GEN, 2=EET, 3=CFDI, 4=FPA, 5=MTD, 6=EWB, 7=PEPPOL, 8=HOI, 9=MYF, 10=EIS, 11=IIS, 12=IIS_ANNUAL]

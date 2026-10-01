<!-- source: REFDB.chm (SAP Business One SDK 10.0 - Database Tables Reference) | version: SAP Business One 10.0 | verified: 2026-10-01 -->
# AEC1 - Parameters for Various Types of Electronic Communication
Module: Reports | 16 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: Code, BPLId, LineNum, LogInstanc
Fields (name type(len) description [values] ->parent table):
  Code nVarChar(8) Code ->OECM
  LineNum Int(11) Row Number
  StrIndex Int(6) String Index
  BPLId Int(11) Branch ID default=-1 ->OBPL
  ParamType nVarChar(2) Parameter Type default=TX [TX=General Text, TT=Title, EM=E-Mail, UR=URI Address, SA=Server Address, PT=Path, FN=File Name, LG=Logic Value - Yes/No, NI=Number - Integer, NR=Number - Real, PW=Password, OT=Other, MP=Mapping, GT=Generation Type, CT=Certificate, UQ=User Queries Category, CB=Combo Box, SP=Separator, EF=External Function, IU=B1i Server URL, NM=Money, LT=Long General Text]
  ParamVisib VarChar(1) Parameter is Visible default=Y [Y=Yes, N=No]
  ParamName nVarChar(100) Parameter Name
  ParamValue Text(16) Parameter Value
  UserSign Int(6) User Signature ->OUSR
  CreateDate Date(8) Creation Date
  UserSign2 Int(6) Updating User ->OUSR
  UpdateDate Date(8) Update Date
  LogInstanc Int(6) Log Instance
  ParamPrms nVarChar(254) Parameter Parameters
  UIorder Int(6) UI Order
  Type Int(6) UI Type

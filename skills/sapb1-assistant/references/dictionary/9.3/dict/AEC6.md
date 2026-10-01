<!-- source: erpref.com (schema IP: SAP) | version: SAP Business One 9.3 | verified: 2026-10-01 -->
# AEC6 - Electronic Protocol DI API Properties
Module: Reports | 15 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: LogInstanc, Code
Fields (name type(len) description [values] ->parent table):
  Code Int(11) Communication Type or Protocol [0=Invalid, 1=GEN, 2=EET, 3=CFDI, 4=FPA, 5=MTD] ->OECM
  GenType VarChar(1) Generation Type default=N [N=Not Relevant, G=Generate, L=Generate - Later]
  MapID Int(11) Electronic Document Format Mapping ->OLLF
  MapID_WS Int(11) eDoc Web Service Format Mapping ->OLLF
  TestMode VarChar(1) Testing Mode Flag default=N [Y=Yes, N=No]
  LogInstanc Int(6) Log Instance
  ParamLogic VarChar(1) Logic Value Parameter default=N [Y=Yes, N=No]
  ParamStr nVarChar(254) String Value Parameter
  ParamLText Text(16) Long Text Parameter
  ActStatus VarChar(1) Action Status default=N [N=New, P=Pending, E=Error, O=OK, S=Sent, R=Document Error, W=Waiting, A=Authorized, I=In Process, J=Rejected, D=Denied, C=Canceled, B=Aborted, Q=Queued, M=Imported, G=Warning]
  ParamUqc Int(11) User Query Category ->OQCN
  ParamInt Int(11) Integer Number
  ParamPAC nVarChar(16) Authority Code ->OPAC
  ParamTgl VarChar(1) Toggle Value Parameter
  ParamMon Num(19,6) Money Value Parameter

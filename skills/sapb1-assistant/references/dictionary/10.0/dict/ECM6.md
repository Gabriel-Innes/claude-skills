<!-- source: REFDB.chm (SAP Business One SDK 10.0 - Database Tables Reference) | version: SAP Business One 10.0 | verified: 2026-10-01 -->
# ECM6 - Electronic Protocol DI API Properties
Module: Reports | 73 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: Code
Fields (name type(len) description [values] ->parent table):
  Code Int(11) Communication Type or Protocol [0=Invalid, 1=GEN, 2=EET, 3=CFDI, 4=FPA, 5=MTD, 6=EWB, 7=PEPPOL, 8=HOI, 9=MYF, 10=EIS, 11=IIS, 12=IIS_ANNUAL, 13=DIGIPOORT, 14=E-Books, 16=RTIE, 17=E-Billing] ->OECM
  GenType VarChar(1) Generation Type [N=Not Relevant, G=Generate, L=Generate - Later]
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
  ParamMon nVarChar(254) Money Value Parameter (Including Currency)
  ParamLink Text(16) Hyperlink Parameter
  Frequency Int(11) Frequency default=1 [1=Daily, 7=Weekly, 14=Fortnightly, 30=Monthly, 90=Quarterly]
  Source VarChar(1) Document Source default=B [B=Business Logic, I=Import]
  ReportID nVarChar(50) Report ID
  AssignedID nVarChar(50) Assigned ID
  Confirm nVarChar(5) Confirmation
  PayMethod nVarChar(50) Payment Method default=01 [01=Efectivo, 02=Cheque nominativo, 03=Transferencia electr�nica de fondos, 04=Tarjeta de cr�dito, 05=Monedero electr�nico, 06=Dinero electr�nico, 08=Vales de despensa, 12=Daci�n en pago, 13=Pago por subrogaci�n, 14=Pago por consignaci�n, 15=Condonaci�n, 17=Compensaci�n, 23=Novaci�n, 24=Confusi�n, 25=Remisi�n de deuda, 26=Prescripci�n o caducidad, 27=A satisfacci�n del acreedor, 28=Tarjeta de d�bito, 29=Tarjeta de servicios, 30=Aplicaci�n de anticipos, 31=Intermediario pagos, 99=Por definir]
  CancStatus VarChar(1) Cancelation Status default=T [T=, N=New Request, S=Request Sent, A=Approved, R=Rejected, E=Error, C=Canceled, I=In Process, U=Sent To Authorities]
  CancRecons nVarChar(30) Canceled Reconciliations
  EntryTypes nVarChar(30) Filter Entry Types
  EntryStats nVarChar(30) Filter Entry Statuses
  EntryCncSt nVarChar(30) Filter Entries by Cancellation Status
  MaxLines Int(6) Filter Max Lines default=0
  BPLId Int(11) Filter Branch ID default=-1
  DateFrom Date(8) Filter Date From
  TimeFrom Int(11) Filter Time From
  DateTo Date(8) Filter Date To
  TimeTo Int(11) Filter Time To
  FromEntry Int(11) Filter From Entry
  Ascending VarChar(1) Order Ascending default=Y [Y=Yes, N=No]
  CodeStr nVarChar(8) Code as a string
  GUID nVarChar(100) Filter GUID
  LogType VarChar(1) Filter Log Type default=R [=INVALID, S=Send, R=Receive, I=Import, N=Note, W=Warning, E=Error, D=WS Data]
  LogMessage Text(16) Log Message
  LogData Text(16) Log Data
  EDocType Int(11) E-Doc Type ->OUNCL
  EDocNum nVarChar(100) E-Doc Number
  ROText1 nVarChar(254) Read Only Text 1
  ProcTarget nVarChar(40) Processing Target
  ParticipID nVarChar(128) E-Doc Number
  PositMARK nVarChar(100) MARK of Positive Value Invoice
  NegatMARK nVarChar(100) MARK of Negative Value Invoice
  EbookRelvt VarChar(1) Is E-Books Relevant
  PInvType Int(11) Type Abs of Pos. Value Invoice ->OEIT
  PInvCode nVarChar(254) Type of Pos. Value Invoice
  NInvType Int(11) Type Abs of Neg. Value Invoice ->OEIT
  NInvCode nVarChar(254) Type of Neg. Value Invoice
  BlobCntTyp Int(11) Blob Content Type default=-1 [-1=, 0=XML, 1=Zipped XML, 2=JSON, 3=Zipped JSON, 4=Text]
  ZipUnzip VarChar(1) Zip or Unzip Blob Content default=N [Y=Yes, N=No]
  KeepPrefix VarChar(1) Keep Prefix in Blob Content default=N [Y=Yes, N=No]
  DocFunc VarChar(1) Document Function default=0 [0=, 1=??? - ????-???????, 2=?????? - ????-??????? ? o???????, 3=??? - o???????, 4=???? - ???????????????? ????-???????, 5=??????? - ???????????????? ????-??????? ? o???????, 6=??? - o???????]
  EIRN nVarChar(254) IRN of E-Billing
  PKP Text(16)
  BKP Text(16)
  SignMsg Text(16)
  SignDigest Text(16)
  FechaTimbr nVarChar(30)
  SelloSAT Text(16)
  RFCofPAC nVarChar(100)
  PACSATCert nVarChar(100)
  SeqNum Int(11)
  SndDateSDI Date(8)
  Progressiv nVarChar(20)
  ExportFile Text(16)
  Descriptn nVarChar(200) Protocol Description
  CFDiExport nVarChar(2) default=01 [01=No aplica, 02=Definitiva, 03=Temporal]
  CancReason nVarChar(2) Cancellation Reason
  CancResp nVarChar(3) Cancellation Response

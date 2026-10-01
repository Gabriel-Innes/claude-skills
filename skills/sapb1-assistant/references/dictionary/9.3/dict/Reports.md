<!-- source: erpref.com (schema IP: SAP) | version: SAP Business One 9.3 | verified: 2026-10-01 -->

# AEC1 - Parameters for Various Types of Electronic Communication
Module: Reports | 16 columns
Indexes (name: columns; first = primary key; U = unique) - WARNING: multi-column key order here is reversed vs SAP's 10.0 reference (read as a set; see references/dictionary/INDEX.md):
  PRIMARY U: LogInstanc, LineNum, BPLId, Code
Fields (name type(len) description [values] ->parent table):
  Code nVarChar(8) Code ->OECM
  LineNum Int(11) Row Number
  StrIndex Int(6) String Index
  BPLId Int(11) Branch ID default=-1 ->OBPL
  ParamType nVarChar(2) Parameter Type default=TX [TX=General Text, TT=Title, EM=E-Mail, UR=URI Address, SA=Server Address, PT=Path, FN=File Name, LG=Logic Value - Yes/No, NI=Number - Integer, NR=Number - Real, PW=Password, OT=Other, MP=Mapping, GT=Generation Type, CT=Certificate, UQ=User Queries Category, CB=Combo Box, SP=Separator, EF=External Function]
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

# AEC2 - Electronic Transactions
Module: Reports | 36 columns
Indexes (name: columns; first = primary key; U = unique) - WARNING: multi-column key order here is reversed vs SAP's 10.0 reference (read as a set; see references/dictionary/INDEX.md):
  PRIMARY U: LogInstanc, AbsEntry
Fields (name type(len) description [values] ->parent table):
  AbsEntry Int(11) Internal ID
  Code nVarChar(8) Code ->OECM
  ParentID Int(11) Parent ID ->ECM2
  ActType VarChar(1) Action Type [S=Setup, R=Report, D=Document A/R, P=Document A/P, F=A/R Draft Document, E=A/P Draft Document, O=Other, K=Skip, C=Contingency, B=BP Check, I=Payment - Incoming, U=Payment - Outgoing, A=Internal Reconciliation, T=Transportation Document, W=Inventory Transfer]
  ActDesc nVarChar(100) Action Description
  ActStatus VarChar(1) Action Status default=N [N=New, P=Pending, E=Error, T=Temporary Error, O=OK, S=Sent, R=Document Error, W=Waiting, A=Authorized, I=In Process, J=Rejected, D=Denied, C=Canceled, B=Aborted, Q=Queued, M=Imported, G=Warning, V=Approved]
  IsRemoved VarChar(1) Is Removed default=N [Y=Yes, N=No]
  ActMessage nVarChar(254) Action Message
  ActEnv Int(11) Action Environment Type default=-1 ->OBNI
  BPLId Int(11) Branch ID default=-1 ->OBPL
  Submits Int(6) Report - Number of Submissions
  ObjectID nVarChar(50) Object ID
  ReportID nVarChar(50) Report ID
  SrcObjType nVarChar(20) Source Object Type
  SrcObjAbs Int(11) Source Object Internal ID
  Cancel VarChar(1) Cancelation default=N [Y=Yes, N=No]
  AssignedID nVarChar(50) Assigned ID
  DocBtch nVarChar(50) Document Batch
  DocBtchLn Int(6) Document Batch Line
  GenType VarChar(1) Generation Type default=N [N=Not Relevant, G=Generate, L=Generate - Later, S=Send, R=Send - Later]
  TestMode VarChar(1) Test Mode default=N [N=No, Y=Yes]
  PeriodType VarChar(1) Report Period Type [Y=Year, Q=Quarter, M=Month, P=Period]
  PeriodNum Int(11) Report Period Number
  Year Int(6) Report Year
  DateFrom Date(8) Report - Date From
  DateTo Date(8) Report - Date To
  UserSign Int(6) User Signature ->OUSR
  CreateDate Date(8) Creation Date
  CreateTS Int(11) Creation Time - Incl. Secs
  UserSign2 Int(6) Updating User ->OUSR
  UpdateDate Date(8) Update Date
  UpdateTS Int(11) Update Time - Incl. Secs
  LogInstanc Int(6) Log Instance
  SchedJobID Int(11) Scheduled Job ID ->OBSJ
  GUID nVarChar(100) GUID
  Authority nVarChar(16) Authority Code ->OPAC

# AEC3 - Statuses and Logs for Actions in Electronic Communication
Module: Reports | 15 columns
Indexes (name: columns; first = primary key; U = unique) - WARNING: multi-column key order here is reversed vs SAP's 10.0 reference (read as a set; see references/dictionary/INDEX.md):
  PRIMARY U: LogInstanc, LogNum, AbsEntry
Fields (name type(len) description [values] ->parent table):
  AbsEntry Int(11) Internal ID ->ECM2
  LogNum Int(11) Log Number
  LogType VarChar(1) Log Type default=R [S=Send, R=Receive, I=Import, N=Note, W=Warning, E=Error]
  LogMessage Text(16) Log Message
  LogData Text(16) Log Data
  LogOpDate Date(8) Log Operation Date
  LogOpTS Int(11) Log Operation Time - Incl. Secs
  ExportFmt Int(11) Export Format ->OLLF
  UserSign Int(6) User Signature ->OUSR
  CreateDate Date(8) Creation Date
  CreateTS Int(11) Create Time - Incl. Secs
  UserSign2 Int(6) Updating User ->OUSR
  UpdateDate Date(8) Update Date
  UpdateTS Int(11) Update Time - Incl. Secs
  LogInstanc Int(6) Log Instance

# AEC4 - Import Mapping Determination
Module: Reports | 13 columns
Indexes (name: columns; first = primary key; U = unique) - WARNING: multi-column key order here is reversed vs SAP's 10.0 reference (read as a set; see references/dictionary/INDEX.md):
  PRIMARY U: LogInstanc, AbsEntry
Fields (name type(len) description [values] ->parent table):
  AbsEntry Int(11) Internal ID
  Code nVarChar(8) Code ->OECM
  LineNum Int(11) Row Number
  ObjType nVarChar(20) Object Type default=-1 [18=A/P Invoice, 19=A/P Credit Memo, 204=A/P Down Payment, 163=A/P Correction Invoice, 164=A/P Correction Invoice Reversal, 20=Goods Receipt PO, 21=Goods Return, 24=Incoming Payment, 46=Outgoing Payment]
  ObjXPath nVarChar(254) Object Type XPath
  FieldType VarChar(1) Field Type default=T [T=Federal Tax ID, A=Additional ID, U=Unified Federal Tax ID, C=CNPJ, L=Alias Name, I=IBAN, N=BP Name]
  FieldXPath nVarChar(254) Field XPath
  ImportFmt Int(11) Import Format ->OLLF
  UserSign Int(6) User Signature ->OUSR
  CreateDate Date(8) Creation Date
  UserSign2 Int(6) Updating User ->OUSR
  UpdateDate Date(8) Update Date
  LogInstanc Int(6) Log Instance

# AEC5 - List of Canceled Reconciliations for Actions in Electronic Communication
Module: Reports | 13 columns
Indexes (name: columns; first = primary key; U = unique) - WARNING: multi-column key order here is reversed vs SAP's 10.0 reference (read as a set; see references/dictionary/INDEX.md):
  PRIMARY U: LogInstanc, LogNum, AbsEntry
Fields (name type(len) description [values] ->parent table):
  AbsEntry Int(11) Internal ID ->ECM2
  LogNum Int(11) Log Number
  DocType Int(11) Document Type
  DocAbs Int(11) Document Abs. Entry
  DocNum Int(11) Document Number
  UUID nVarChar(50) UUID
  UserSign Int(6) User Signature ->OUSR
  CreateDate Date(8) Creation Date
  CreateTS Int(11) Create Time - Incl. Sec.
  UserSign2 Int(6) Updating User ->OUSR
  UpdateDate Date(8) Update Date
  UpdateTS Int(11) Update Time - Incl. Sec.
  LogInstanc Int(6) Log Instance

# AEC6 - Electronic Protocol DI API Properties
Module: Reports | 15 columns
Indexes (name: columns; first = primary key; U = unique) - WARNING: multi-column key order here is reversed vs SAP's 10.0 reference (read as a set; see references/dictionary/INDEX.md):
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

# AECM - Electronic Communication Types or Protocols
Module: Reports | 6 columns
Indexes (name: columns; first = primary key; U = unique) - WARNING: multi-column key order here is reversed vs SAP's 10.0 reference (read as a set; see references/dictionary/INDEX.md):
  PRIMARY U: LogInstanc, Code
Fields (name type(len) description [values] ->parent table):
  Code nVarChar(8) Communication Type or Protocol
  Descr nVarChar(200) Description
  LogInstanc Int(6) Log Instance
  UIOrder Int(6) UI Order
  StrIndex Int(6) String Index
  IsActive VarChar(1) Activation of Communication Type or Protocol default=N [Y=Yes, N=No]

# AMD1 - Amout Differences Report Lines
Module: Reports | 16 columns
Indexes (name: columns; first = primary key; U = unique) - WARNING: multi-column key order here is reversed vs SAP's 10.0 reference (read as a set; see references/dictionary/INDEX.md):
  PRIMARY U: PmnInvID, PmnNum, LineNum
Fields (name type(len) description [values] ->parent table):
  LineNum Int(11) Internal ID
  PmnNum Int(11) Payment Number ->ORCT
  PmnInvID Int(11) Invoice Seq. No. in Payment
  PmnDate Date(8) Payment Date
  CardCode nVarChar(15) BP Code ->OCRD
  InvType nVarChar(20) Invoice Category default=13 [13=Sales Invoice]
  InvEntry Int(11) Invoice Key ->OINV
  InstId Int(6) Installment ID
  InvTransID Int(11) Invoice Transaction Number ->OJDT
  FCCurrency nVarChar(3) Foreign Currency ->OCRN
  InvRate Num(19,6) Rate, Invoice
  PmnRate Num(19,6) Rate, Payment
  Approved VarChar(1) Confirmed default=Y [Y=Yes, N=No]
  AmountDiff Num(19,6) Amount Difference (LC)
  TaxAmtDiff Num(19,6) Tax Difference (LC)
  TMP_JE nVarChar(50) Temporary Transaction ID

# AQAG - Query Authorization Groups - Log
Module: Reports | 10 columns
Indexes (name: columns; first = primary key; U = unique) - WARNING: multi-column key order here is reversed vs SAP's 10.0 reference (read as a set; see references/dictionary/INDEX.md):
  PRIMARY U: LogInstanc, AUTHGRPID
Fields (name type(len) description [values] ->parent table):
  AUTHGRPID Int(11) Query Authorization Group ID
  AUTHGRPCD nVarChar(50) Group Code
  AUTHGRPN nVarChar(254) Group Description
  LogInstanc Int(11) Log Instance default=0
  UserSign Int(6) Item Created By ->OUSR
  UserSign2 Int(6) Item Updated By ->OUSR
  UpdateDate Date(8) Date of Update
  CreateDate Date(8) Date of Create
  Deleted VarChar(1) Deleted Field default=N
  SnapShotID Int(11) Snapshot ID default=0

# ATHL - Thresholds
Module: Reports | 12 columns
Indexes (name: columns; first = primary key; U = unique) - WARNING: multi-column key order here is reversed vs SAP's 10.0 reference (read as a set; see references/dictionary/INDEX.md):
  PRIMARY U: LogInstanc, AbsEntry
Fields (name type(len) description [values] ->parent table):
  AbsEntry Int(11) Internal Number
  RecType VarChar(1) Report Type default=A [A=Annual Invoice Declaration, B=Blacklist Country]
  EffecFrom Date(8) Effective From
  Company nVarChar(20) Company
  PrivInv nVarChar(20) Private - Invoice
  PrivJE nVarChar(20) Private - Journal Entry
  LogInstanc Int(11) Log Instance
  UserSign Int(6) User Signature ->OUSR
  CreateDate Date(8) Creation Date
  UserSign2 Int(6) Updating User ->OUSR
  UpdateDate Date(8) Date of Update
  Tourism nVarChar(20) Tourism

# BTA1 - Brazil - Tax Adjustment - Tax Types
Module: Reports | 2 columns
Indexes (name: columns; first = primary key; U = unique) - WARNING: multi-column key order here is reversed vs SAP's 10.0 reference (read as a set; see references/dictionary/INDEX.md):
  PRIMARY U: StaType, AbsEntry
Fields (name type(len) description [values] ->parent table):
  AbsEntry Int(11) Internal Number ->OBTA
  StaType Int(11) Tax Authority Type ->OSTT

# BTA2 - Brazil Tax Adujstment - Taxes Paid in Advance
Module: Reports | 4 columns
Indexes (name: columns; first = primary key; U = unique) - WARNING: multi-column key order here is reversed vs SAP's 10.0 reference (read as a set; see references/dictionary/INDEX.md):
  PRIMARY U: LineNum, AbsEntry
  TAX U: TaxLine, TaxEntry, AbsEntry
Fields (name type(len) description [values] ->parent table):
  AbsEntry Int(11) Internal Number ->OBTA
  LineNum Int(11) Row Number
  TaxEntry Int(11) Tax Entry ->TAX1
  TaxLine Int(11) Tax Line ->TAX1

# EBL1 - E-Balance Report Data
Module: Reports | 7 columns
Indexes (name: columns; first = primary key; U = unique) - WARNING: multi-column key order here is reversed vs SAP's 10.0 reference (read as a set; see references/dictionary/INDEX.md):
  PRIMARY U: LineNum, AbsEntry
Fields (name type(len) description [values] ->parent table):
  AbsEntry Int(11) Internal Key
  LineNum Int(11) Line Number
  ReportType Int(11) Report Type default=0 [0=, 1=E-General Information GCD (Global Common Document), 2=e-Balance Sheet, 3=e-Profit and Loss, 4=E-Taxable Profit and Loss, 5=E-Income Usage, 6=E-Assets History Sheet, 7=Shareholder, 8=Account Verification, -1=Global Common Data, -2=Global Common Report Data]
  Selected VarChar(1) Selected default=Y [Y=Yes, N=No]
  Mandatory VarChar(1) Mandatory
  DocType VarChar(1) Document Type [0=XBRL]
  DocContent Text(16) Document Content

# ECDW1 - ECD Wizard - Rows 1
Module: Reports | 8 columns
Indexes (name: columns; first = primary key; U = unique) - WARNING: multi-column key order here is reversed vs SAP's 10.0 reference (read as a set; see references/dictionary/INDEX.md):
  PRIMARY U: ExNumData2, ExNumData1, DocType, AbsEntry
Fields (name type(len) description [values] ->parent table):
  AbsEntry Int(11) Internal Number
  DocType VarChar(1) Template Type [B=Balance Sheet, P=Profit and Loss]
  ExNumData1 Int(11) Extra Numeric Data 1
  ExNumData2 Int(11) Extra Numeric Data 2
  ExNumData3 Int(11) Extra Numeric Data 3
  ExStrData1 nVarChar(254) Extra String Data 1
  ExStrData2 nVarChar(254) Extra String Data 2
  ExStrData3 nVarChar(254) Extra String Data 3

# ECM1 - Parameters for Various Types of Electronic Communication
Module: Reports | 16 columns
Indexes (name: columns; first = primary key; U = unique) - WARNING: multi-column key order here is reversed vs SAP's 10.0 reference (read as a set; see references/dictionary/INDEX.md):
  PRIMARY U: LineNum, BPLId, Code
  PARAM_NAME U: ParamName, BPLId, Code
Fields (name type(len) description [values] ->parent table):
  Code nVarChar(8) Code ->OECM
  LineNum Int(11) Row Number
  StrIndex Int(6) String Index
  BPLId Int(11) Branch ID default=-1 ->OBPL
  ParamType nVarChar(2) Parameter Type default=TX [TX=General Text, TT=Title, EM=E-Mail, UR=URI Address, SA=Server Address, PT=Path, FN=File Name, LG=Logic Value - Yes/No, NI=Number - Integer, NR=Number - Real, PW=Password, OT=Other, MP=Mapping, GT=Generation Type, CT=Certificate, UQ=User Queries Category, CB=Combo Box, SP=Separator, EF=External Function]
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

# ECM2 - Electronic Transactions
Module: Reports | 36 columns
Indexes (name: columns; first = primary key; U = unique) - WARNING: multi-column key order here is reversed vs SAP's 10.0 reference (read as a set; see references/dictionary/INDEX.md):
  PRIMARY U: AbsEntry
  ACTION U: AbsEntry, Code
  DOCREF: Code, SrcObjAbs, SrcObjType
Fields (name type(len) description [values] ->parent table):
  AbsEntry Int(11) Internal ID
  Code nVarChar(8) Code ->OECM
  ParentID Int(11) Parent ID ->ECM2
  ActType VarChar(1) Action Type [S=Setup, R=Report, D=Document A/R, P=Document A/P, F=A/R Draft Document, E=A/P Draft Document, O=Other, K=Skip, C=Contingency, B=BP Check, I=Payment - Incoming, U=Payment - Outgoing, A=Internal Reconciliation, T=Transportation Document, W=Inventory Transfer, V=VAT Obligations, N=VAT Declarations, L=VAT Liabilities, Y=VAT Payments]
  ActDesc nVarChar(100) Action Description
  ActStatus VarChar(1) Action Status default=N [N=New, P=Pending, E=Error, T=Temporary Error, O=OK, S=Sent, R=Document Error, W=Waiting, A=Authorized, I=In Process, J=Rejected, D=Denied, C=Canceled, B=Aborted, Q=Queued, M=Imported, G=Warning, V=Approved]
  IsRemoved VarChar(1) Is Removed default=N [Y=Yes, N=No]
  ActMessage nVarChar(254) Action Message
  ActEnv Int(11) Action Environment Type default=-1 ->OBNI
  BPLId Int(11) Branch ID default=-1 ->OBPL
  Submits Int(6) Report - Number of Submissions
  ObjectID nVarChar(50) Object ID
  ReportID nVarChar(50) Report ID
  SrcObjType nVarChar(20) Source Object Type
  SrcObjAbs Int(11) Source Object Internal ID
  Cancel VarChar(1) Cancelation default=N [Y=Yes, N=No]
  AssignedID nVarChar(50) Assigned ID
  DocBtch nVarChar(50) Document Batch
  DocBtchLn Int(6) Document Batch Line
  GenType VarChar(1) Generation Type default=N [N=Not Relevant, G=Generate, L=Generate - Later, S=Send, R=Send - Later]
  TestMode VarChar(1) Test Mode default=N [N=No, Y=Yes]
  PeriodType VarChar(1) Report Period Type [Y=Year, Q=Quarter, M=Month, P=Period]
  PeriodNum Int(11) Report Period Number
  Year Int(6) Report Year
  DateFrom Date(8) Report - Date From
  DateTo Date(8) Report - Date To
  UserSign Int(6) User Signature ->OUSR
  CreateDate Date(8) Creation Date
  CreateTS Int(11) Creation Time - Incl. Secs
  UserSign2 Int(6) Updating User ->OUSR
  UpdateDate Date(8) Update Date
  UpdateTS Int(11) Update Time - Incl. Secs
  LogInstanc Int(6) Log Instance
  SchedJobID Int(11) Scheduled Job ID ->OBSJ
  GUID nVarChar(100) GUID
  Authority nVarChar(16) Authority Code ->OPAC

# ECM3 - Statuses and Logs for Actions in Electronic Communication
Module: Reports | 15 columns
Indexes (name: columns; first = primary key; U = unique) - WARNING: multi-column key order here is reversed vs SAP's 10.0 reference (read as a set; see references/dictionary/INDEX.md):
  PRIMARY U: LogNum, AbsEntry
Fields (name type(len) description [values] ->parent table):
  AbsEntry Int(11) Internal ID ->ECM2
  LogNum Int(11) Log Number
  LogType VarChar(1) Log Type default=R [S=Send, R=Receive, I=Import, N=Note, W=Warning, E=Error]
  LogMessage Text(16) Log Message
  LogData Text(16) Log Data
  LogOpDate Date(8) Log Operation Date
  LogOpTS Int(11) Log Operation Time - Incl. Secs
  ExportFmt Int(11) Export Format ->OLLF
  UserSign Int(6) User Signature ->OUSR
  CreateDate Date(8) Creation Date
  CreateTS Int(11) Create Time - Incl. Secs
  UserSign2 Int(6) Updating User ->OUSR
  UpdateDate Date(8) Update Date
  UpdateTS Int(11) Update Time - Incl. Secs
  LogInstanc Int(6) Log Instance

# ECM4 - Import Mapping Determination
Module: Reports | 13 columns
Indexes (name: columns; first = primary key; U = unique) - WARNING: multi-column key order here is reversed vs SAP's 10.0 reference (read as a set; see references/dictionary/INDEX.md):
  PRIMARY U: AbsEntry
  DOC_IMPORT U: AbsEntry, ObjType, Code
Fields (name type(len) description [values] ->parent table):
  AbsEntry Int(11) Internal ID
  Code nVarChar(8) Code ->OECM
  LineNum Int(11) Row Number
  ObjType nVarChar(20) Object Type default=-1 [18=A/P Invoice, 19=A/P Credit Memo, 204=A/P Down Payment, 163=A/P Correction Invoice, 164=A/P Correction Invoice Reversal, 20=Goods Receipt PO, 21=Goods Return, 24=Incoming Payment, 46=Outgoing Payment]
  ObjXPath nVarChar(254) Object Type XPath
  FieldType VarChar(1) Field Type default=T [T=Federal Tax ID, A=Additional ID, U=Unified Federal Tax ID, C=CNPJ, L=Alias Name, I=IBAN, N=BP Name]
  FieldXPath nVarChar(254) Field XPath
  ImportFmt Int(11) Import Format ->OLLF
  UserSign Int(6) User Signature ->OUSR
  CreateDate Date(8) Creation Date
  UserSign2 Int(6) Updating User ->OUSR
  UpdateDate Date(8) Update Date
  LogInstanc Int(6) Log Instance

# ECM5 - List of Related Documents for Actions in Electronic Communication
Module: Reports | 13 columns
Indexes (name: columns; first = primary key; U = unique) - WARNING: multi-column key order here is reversed vs SAP's 10.0 reference (read as a set; see references/dictionary/INDEX.md):
  PRIMARY U: LogNum, AbsEntry
Fields (name type(len) description [values] ->parent table):
  AbsEntry Int(11) Internal ID ->ECM2
  LogNum Int(11) Log Number
  DocType Int(11) Document Type
  DocAbs Int(11) Document Abs. Entry
  DocNum Int(11) Document Number
  UUID nVarChar(50) UUID
  UserSign Int(6) User Signature ->OUSR
  CreateDate Date(8) Creation Date
  CreateTS Int(11) Create Time - Incl. Sec.
  UserSign2 Int(6) Updating User ->OUSR
  UpdateDate Date(8) Update Date
  UpdateTS Int(11) Update Time - Incl. Sec.
  LogInstanc Int(6) Log Instance

# ECM6 - Electronic Protocol DI API Properties
Module: Reports | 15 columns
Indexes (name: columns; first = primary key; U = unique) - WARNING: multi-column key order here is reversed vs SAP's 10.0 reference (read as a set; see references/dictionary/INDEX.md):
  PRIMARY U: Code
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

# EFDW1 - EFD Wizard - Rows 1
Module: Reports | 2 columns
Indexes (name: columns; first = primary key; U = unique) - WARNING: multi-column key order here is reversed vs SAP's 10.0 reference (read as a set; see references/dictionary/INDEX.md):
  PRIMARY U: WhCode, AbsEntry
Fields (name type(len) description [values] ->parent table):
  AbsEntry Int(11) Internal Number
  WhCode nVarChar(8) Warehouse Code ->OWHS

# EJB1 - ERV-JAb Wizard Signing Persons
Module: Reports | 10 columns
Indexes (name: columns; first = primary key; U = unique) - WARNING: multi-column key order here is reversed vs SAP's 10.0 reference (read as a set; see references/dictionary/INDEX.md):
  PRIMARY U: LineNum, WizardID
Fields (name type(len) description [values] ->parent table):
  WizardID Int(11) Wizard ID ->OEJB
  LineNum Int(11) Row Number
  Title nVarChar(20) Title
  FirstName nVarChar(38) First Name
  Surname nVarChar(38) Surname
  CommID nVarChar(3) Commercial ID
  DateOfBrth Date(8) Date of Birth
  DateOfSign Date(8) Date of Signing
  AbsEntry Int(11) Internal Number ->OEJD
  LineNumEJD Int(11) Row Number EJD1 ->EJD1

# EJB2 - Docs List for ERV-JAb Wizard
Module: Reports | 9 columns
Indexes (name: columns; first = primary key; U = unique) - WARNING: multi-column key order here is reversed vs SAP's 10.0 reference (read as a set; see references/dictionary/INDEX.md):
  PRIMARY U: DocID, WizardID
Fields (name type(len) description [values] ->parent table):
  WizardID Int(11) Wizard ID ->OEJB
  DocID Int(11) Document ID
  Selected VarChar(1) Selected default=Y [Y=Yes, N=No]
  Mandatory VarChar(1) Mandatory default=N [Y=Yes, N=No]
  Type nVarChar(3) Type [XML=XML, PDF=PDF]
  RptSec Int(11) Report Section default=0 [0=, 1=General Information for ERV-JAb, 2=Names of Signatories:, 3=Legal Size Classification, 4=Extract from Balance Sheet (UGB Form 2), 5=Balance Sheet, 6=P&L Statement, 7=Annex To Be Published (UGB Form 3), 8=General and Other Explanations, 9=Annex to Balance Sheet Entry, 10=Annex to P&L Statement, 11=Annual Report, 12=Suggestion for Financial Statement Usage, 13=Decision About Financial Statement Usage, 14=Note of Confirmation, 15=Supervisory Board Report, 16=External Auditor Report Acc. to Art. 44 Para. 3 EStG (Income Tax Act), 17=Finance-Specific Annex, 18=Assets History Sheet, 19=Liabilities History Sheet]
  FilePath nVarChar(254) File Path
  FileStorag Text(16) File Storage
  VisOrder Int(11) Visual Order

# EJD1 - ERV-JAb Signing Persons List
Module: Reports | 8 columns
Indexes (name: columns; first = primary key; U = unique) - WARNING: multi-column key order here is reversed vs SAP's 10.0 reference (read as a set; see references/dictionary/INDEX.md):
  PRIMARY U: LineNum, AbsEntry
Fields (name type(len) description [values] ->parent table):
  AbsEntry Int(11) Internal Number ->OEJD
  LineNum Int(11) Row Number
  Title nVarChar(20) Title
  FirstName nVarChar(38) First Name
  Surname nVarChar(38) Surname
  CommID nVarChar(3) Commercial ID
  DateOfBrth Date(8) Date of Birth
  Active VarChar(1) Active default=N [Y=Yes, N=No]

# EML1 - E-mail Log - Rows
Module: Reports | 5 columns
Indexes (name: columns; first = primary key; U = unique) - WARNING: multi-column key order here is reversed vs SAP's 10.0 reference (read as a set; see references/dictionary/INDEX.md):
  PRIMARY U: Line, AbsEntry
Fields (name type(len) description [values] ->parent table):
  AbsEntry Int(11) Absolute entry
  Line Int(11) Row Number
  ObjectID Int(11) Document Object ID
  DocDate Date(8) Posting Date
  DocEntry Int(11) Doc Internal Number

# FLT1 - 856 Report - Selection Criteria
Module: Reports | 10 columns
Indexes (name: columns; first = primary key; U = unique) - WARNING: multi-column key order here is reversed vs SAP's 10.0 reference (read as a set; see references/dictionary/INDEX.md):
  PRIMARY U: FilterName, Code, UserSign, FormNo
Fields (name type(len) description [values] ->parent table):
  FormNo nVarChar(20) Form No.
  Code nVarChar(50) Code
  UserSign Int(6) User Signature ->OUSR
  ExNumData1 Int(11) Extra Numeric Data 1
  ExNumData2 Int(11) Extra Numeric Data 2
  ExNumData3 Int(11) Extra Numeric Data 3
  ExStrData1 nVarChar(254) Extra String Data 1
  ExStrData2 nVarChar(254) Extra String Data 2
  ExStrData3 nVarChar(254) Extra String Data 3
  FilterName nVarChar(30) Filter Name default=_

# GDP1 - General Data Protection Wizard - Personal Fields Setup
Module: Reports | 9 columns
Indexes (name: columns; first = primary key; U = unique) - WARNING: multi-column key order here is reversed vs SAP's 10.0 reference (read as a set; see references/dictionary/INDEX.md):
  PRIMARY U: PfsAbs, AbsEntry
Fields (name type(len) description [values] ->parent table):
  AbsEntry Int(11) Internal Number
  PfsAbs Int(11) Internal Number
  TableName nVarChar(20) Table Name
  FieldName nVarChar(50) Field Name
  RefObjType nVarChar(20) Referenced Object Type
  Category VarChar(1) Category default=N [N=, R=Sales A/R, P=Purchase A/P]
  OrigType VarChar(1) Original Type default=U [U=User Defined, S=Sensitive, P=Personal]
  Type VarChar(1) Type default=N [N=Not Relevant, S=Sensitive, P=Personal]
  Descr nVarChar(254) Description

# GDP2 - General Data Protection Wizard - Natural Persons
Module: Reports | 8 columns
Indexes (name: columns; first = primary key; U = unique) - WARNING: multi-column key order here is reversed vs SAP's 10.0 reference (read as a set; see references/dictionary/INDEX.md):
  PRIMARY U: LineNum, AbsEntry
  NATOBJ_KEY U: NatObjKey2, NatObjKey1, NatObjArr, NatObjType, AbsEntry
Fields (name type(len) description [values] ->parent table):
  AbsEntry Int(11) Internal Number ->OGDP
  LineNum Int(6) Line
  NatObjType nVarChar(20) Natural Person Object Type
  NatObjArr Int(11) Natural Person Object Array
  NatObjKey1 nVarChar(20) Natural Person Object Key
  NatObjKey2 nVarChar(20) Natural Person Object Subkey
  Result Int(11) Result
  ErrorStr nVarChar(254) Error String

# GDP3 - General Data Protection Wizard - Processed Documents
Module: Reports | 5 columns
Indexes (name: columns; first = primary key; U = unique) - WARNING: multi-column key order here is reversed vs SAP's 10.0 reference (read as a set; see references/dictionary/INDEX.md):
  PRIMARY U: LineNum, AbsEntry
  NATOBJ_KEY U: RefObjKey2, RefObjKey1, RefObjType, AbsEntry
Fields (name type(len) description [values] ->parent table):
  AbsEntry Int(11) Internal Number ->OGDP
  LineNum Int(6) Line
  RefObjType nVarChar(20) Referenced Object Type
  RefObjKey1 nVarChar(20) Referenced Object Key
  RefObjKey2 nVarChar(20) Referenced Object Subkey

# IRD1 - Report Definition - Rows
Module: Reports | 7 columns
Indexes (name: columns; first = primary key; U = unique) - WARNING: multi-column key order here is reversed vs SAP's 10.0 reference (read as a set; see references/dictionary/INDEX.md):
  PRIMARY U: Type, ReportId
Fields (name type(len) description [values] ->parent table):
  ReportId nVarChar(254) Report Id ->OIRD
  Type Int(11) Type default=1 [1=XLSX]
  Template Text(16) Template
  CreateBy nVarChar(25) Created By
  CreateDate Date(8) Creation Timestamp
  ModifyBy nVarChar(25) Modified By
  ModifyDate Date(8) Modification Timestamp

# LLR1 - Electronic Report Generation Result - Reports
Module: Reports | 4 columns
Indexes (name: columns; first = primary key; U = unique) - WARNING: multi-column key order here is reversed vs SAP's 10.0 reference (read as a set; see references/dictionary/INDEX.md):
  PRIMARY U: ReportNum, ResEntry
Fields (name type(len) description [values] ->parent table):
  ResEntry Int(11) Result Internal ID ->OLLR
  ReportNum Int(11) Report Number
  ReportCode nVarChar(8) Report Code ->RDOC
  Criteria Text(16) Selection Criteria

# OAMD - Amount Differences Report
Module: Reports | 9 columns
Indexes (name: columns; first = primary key; U = unique) - WARNING: multi-column key order here is reversed vs SAP's 10.0 reference (read as a set; see references/dictionary/INDEX.md):
  PRIMARY U: LineNum
Fields (name type(len) description [values] ->parent table):
  LineNum Int(11) Internal ID
  DateFrom Date(8) Date From
  DateTo Date(8) Date To
  CardCode nVarChar(15) BP Code ->OCRD
  Approved VarChar(1) Confirmed default=N [Y=Yes, N=No]
  AmountDiff Num(19,6) Amount Difference (LC)
  TaxAmtDiff Num(19,6) Tax Difference (LC)
  RpCurrency nVarChar(3) Currency Chosen for the Report ->OCRN
  VendOffAct nVarChar(15) Vendor Offset Account ->OACT

# OCRT - CRDB Tables Tree List
Module: Reports | 4 columns
Indexes (name: columns; first = primary key; U = unique) - WARNING: multi-column key order here is reversed vs SAP's 10.0 reference (read as a set; see references/dictionary/INDEX.md):
  PRIMARY U: ID
Fields (name type(len) description [values] ->parent table):
  ID Int(11) ID
  NodeStr nVarChar(20) Node String List
  FatherID Int(11) Parent ID
  TableName nVarChar(20) Table Name

# OEBL - E-Balance
Module: Reports | 5 columns
Indexes (name: columns; first = primary key; U = unique) - WARNING: multi-column key order here is reversed vs SAP's 10.0 reference (read as a set; see references/dictionary/INDEX.md):
  PRIMARY U: AbsEntry
Fields (name type(len) description [values] ->parent table):
  AbsEntry Int(11) Internal Key
  WizardName nVarChar(100) Wizard Name
  Status VarChar(1) Status [G=Generated, S=Saved]
  CreateDate Date(8) Create Date
  UserSign Int(6) User Signature ->OUSR

# OECDW - ECD Wizard
Module: Reports | 40 columns
Indexes (name: columns; first = primary key; U = unique) - WARNING: multi-column key order here is reversed vs SAP's 10.0 reference (read as a set; see references/dictionary/INDEX.md):
  PRIMARY U: AbsEntry
Fields (name type(len) description [values] ->parent table):
  AbsEntry Int(11) Internal Number
  RunName nVarChar(100) Wizard Run Name
  RunDate Date(8) Wizard Run Date
  RunTime Int(6) Wizard Run Time
  Status VarChar(1) Status [S=Saved, E=Executed]
  UserSign Int(11) User Signature ->OUSR
  DateFrom Date(8) Date From
  DateTo Date(8) Date To
  DecenInd VarChar(1) Decentralized Indicator [C=Relatório Consolidado, H=Matriz - Descentralizado, B=Filial - Descentralizado]
  Branch Int(11) Branch default=-2 ->OUBR
  InstCode nVarChar(2) Institution Code [00=Nenhuma inscrição em outras entidades, 01=Banco Central do Brasil, 02=Superintendência de Seguros Privados (Susep), 03=Comissão de Valores Mobiliários (CVM), 04=Agência Nacional de Transportes Terrestres (ANTT), AC=Secretaria da Fazenda do Estado do Acre, ou equivalente, AL=Secretaria da Fazenda de Alagoas, ou equivalente, AM=Secretaria da Fazenda de Amazonas, ou equivalente, AP=Secretaria da Fazenda do Amapá, ou equivalente, BA=Secretaria da Fazenda da Bahia, ou equivalente, DF=Secretaria da Fazenda do Distrito Federal, ou equivalente, CE=Secretaria da Fazenda do Ceará , ou equivalente, ES=Secretaria da Fazenda do Espírito Santo, ou equivalente, GO=Secretaria da Fazenda de Goiás, ou equivalente, MA=Secretaria da Fazenda do Maranhão, ou equivalente, MT=Secretaria da Fazenda do Mato Grosso, ou equivalente, MS=Secretaria da Fazenda do Mato Grosso do Sul, ou equivalente, MG=Secretaria da Fazenda de Minas Gerais, ou equivalente, PA=Secretaria da Fazenda do Pará, ou equivalente, PB=Secretaria da Fazenda da Paraíba, ou equivalente, PE=Secretaria da Fazenda de Pernambuco, ou equivalente, PR=Secretaria da Fazenda do Paraná, ou equivalente, PI=Secretaria da Fazenda do Piauí, ou equivalente, RJ=Secretaria da Fazenda do Rio de Janeiro, ou equivalente, RN=Secretaria da Fazenda do Rio Grande do Norte, ou equivalente, RS=Secretaria da Fazenda do Rio Grande do Sul, ou equivalente, RR=Secretaria da Fazenda de Roraima, ou equivalente, RO=Secretaria da Fazenda de Rondônia, ou equivalente, SC=Secretaria da Fazenda de Santa Catarina, ou equivalente, SP=Secretaria da Fazenda de São Paulo, ou equivalente, SE=Secretaria da Fazenda de Sergipe, ou equivalente, TO=Secretaria da Fazenda de Tocantins, ou equivalente]
  EntIdCode nVarChar(32) Entry Identification Code
  SituatInd VarChar(1) Situation Indicator [0=Opening (abertura), 1=Split-up/ Split-off (Cisão parcial/ cisão total), 2=Merger (Fusão), 3=Downstream merger/ Upstream merger (Incorporação), 4=Extinction (Extinção), 5=Transformation (Transformação)]
  ReportType VarChar(1) Report Type [G=Livro Diário, R=Livro Diário com Escrituração Resumida, A=Livro Diário Auxiliar ao Diário com Escrituração Resumida, B=Livro Balancetes Diários e Balanços (matriz)]
  CmpName nVarChar(100) Company Name
  CmpState nVarChar(2) Company State
  CmpCntCode nVarChar(10) Company County Code
  CmpCNPJ nVarChar(32) Company CNPJ
  CmpIE nVarChar(32) Company IE
  CmpCity nVarChar(32) Company City
  BrnState nVarChar(2) Branch State
  BrnCntCode nVarChar(10) Branch County Code
  BrnCNPJ nVarChar(32) Branch CNPJ
  BrnIE nVarChar(32) Branch IE
  BrnCity nVarChar(32) Branch City
  AccStIden VarChar(1) Account Statement Identification [1=Relatório apenas da empresa, 2=Relatório consolidado da matriz e filiais, afiliadas e empresas associadas]
  AccStRem Text(16) Account Statement Remark
  BookPurp nVarChar(80) Book Purpose
  JrnlNum Int(11) Journal Number
  PeriodSitu VarChar(1) Indicator of Initial Period Situation [0=Normal (Início no primeiro dia do ano), 1=Abertura, 2=Resultante de cisão/fusão ou remanescente de cisão, ou realizou incorporação, 3=Início de obrigatoriedade da entrega da ECD no curso do ano calendário]
  BkPrpsInd VarChar(1) Bookkeeping Purpose Indicator [0=Original, 1=Substituta com NIRE, 2=Substituta sem NIRE, 3=Substituta com troca de NIRE]
  NIREind VarChar(1) NIRE Indicator [0=Empresa não possui registro na Junta Comercial (não possui NIRE), 1=Empresa possui registro na Junta Comercial (possui NIRE)]
  SubBkNIRE nVarChar(11) Substitute Bookkeeping NIRE
  SubBkHash nVarChar(40) Substitute Bookkeeping Hash
  BalanTemp Int(11) Balance Sheet Template ->OFRT
  PrLosTemp Int(11) Profit and Loss Statement Template ->OFRT
  BalanRefF VarChar(1) Balance Sheet Reference Fields default=N [Y=Yes, N=No]
  BalanUdfF VarChar(1) Balance Sheet User-Defined Fields default=N [Y=Yes, N=No]
  PrLosRefF VarChar(1) Profit and Loss Statement Reference Fields default=N [Y=Yes, N=No]
  PrLosUdfF VarChar(1) Profit and Loss Statement User-Defined Fields default=N [Y=Yes, N=No]

# OECM - Electronic Communication Types or Protocols
Module: Reports | 6 columns
Indexes (name: columns; first = primary key; U = unique) - WARNING: multi-column key order here is reversed vs SAP's 10.0 reference (read as a set; see references/dictionary/INDEX.md):
  PRIMARY U: Code
Fields (name type(len) description [values] ->parent table):
  Code nVarChar(8) Communication Type or Protocol
  Descr nVarChar(200) Description
  LogInstanc Int(6) Log Instance
  UIOrder Int(6) UI Order
  StrIndex Int(6) String Index
  IsActive VarChar(1) Activation of Communication Type or Protocol default=N [Y=Yes, N=No]

# OEFDW - EFD Wizard
Module: Reports | 24 columns
Indexes (name: columns; first = primary key; U = unique) - WARNING: multi-column key order here is reversed vs SAP's 10.0 reference (read as a set; see references/dictionary/INDEX.md):
  PRIMARY U: AbsEntry
Fields (name type(len) description [values] ->parent table):
  AbsEntry Int(11) Internal Number
  RunName nVarChar(100) Wizard Run Name
  RunDate Date(8) Wizard Run Date
  RunTime Int(6) Wizard Run Time
  Status VarChar(1) Status [S=Saved, E=Executed]
  UserSign Int(11) User Signature ->OUSR
  DateFrom Date(8) Date From
  DateTo Date(8) Date To
  Branch Int(11) Branch default=-2 ->OUBR
  ProfType nVarChar(2) Profile Type
  BlockC VarChar(1) Block C default=Y [Y=Yes, N=No]
  BlockD VarChar(1) Block D default=Y [Y=Yes, N=No]
  BlockE VarChar(1) Block E default=Y [Y=Yes, N=No]
  BlockH VarChar(1) Block H default=Y [Y=Yes, N=No]
  BlockG VarChar(1) Block G default=Y [Y=Yes, N=No]
  BlockI VarChar(1) Block I default=Y [Y=Yes, N=No]
  FlPurCode VarChar(1) File Purpose Code [0=Remessa do arquivo original, 1=Remessa do arquivo substituto]
  AccEmploye Int(11) Accountant Employee ->OCRD
  AccExtern nVarChar(15) Accountant External ->OHEM
  ItmFrom nVarChar(50) From Item
  ItmTo nVarChar(50) To Item
  ItmGroup Int(6) Item Group
  ItQryGroup nVarChar(250) Item Properties
  RptReason nVarChar(2) Reporting Reason default=01 [01=No final no período, 02=Na mudança de forma de tributação da mercadoria (ICMS), 03=Na solicitação da baixa cadastral, paralisação temporária e outras situações, 04=Na alteração de regime de pagamento – condição do contribuinte, 05=Por determinação dos fiscos]

# OEJB - Wizard Run Details for ERV-JAb
Module: Reports | 24 columns
Indexes (name: columns; first = primary key; U = unique) - WARNING: multi-column key order here is reversed vs SAP's 10.0 reference (read as a set; see references/dictionary/INDEX.md):
  PRIMARY U: WizardId
Fields (name type(len) description [values] ->parent table):
  WizardId Int(11) Wizard ID
  WizardName nVarChar(100) Wizard Name
  FromDate Date(8) From Date
  ToDate Date(8) To Date
  PFromDate Date(8) Previous Year From Date
  PToDate Date(8) Previous Year To Date
  DateOfRun Date(8) Date of Run
  Status VarChar(1) Status default=O [O=Open, C=Closed]
  ActYearCl VarChar(1) Classifictn in Actual Yr [S=Small, M=Medium, L=Large]
  FormFinSt Int(11) Form of Financial Statement default=0 [0=, 1=Small GmbH (UGB Form 2,3), 2=Small GmbH with Balance Sheet, 3=Medium Large GmbH, 4=AG (Eng. PLC)]
  EBSTmpl Int(11) E-Balance Sheet Template ->OFRT
  EPaLTmpl Int(11) E-P&L Template ->OFRT
  OverwrFinS VarChar(1) Overwrite Financial Statement default=N [Y=Yes, N=No]
  Reference nVarChar(25) Reference
  HBCode Int(11) House Bank Code ->DSC1
  PayRef nVarChar(12) Payment Reference
  SndrRole Int(11) Sender Role default=0 [0=, 1=1 - Sole Company Representative and Signatory, 2=2 - Sole Authorized Company Representative, 3=3 - One of Authorized Company Representatives]
  CRegNumber nVarChar(7) Commercial Register Number
  LFBSheetD nVarChar(3) Legal Form on Actl Bal Sht Dte [AG=Public Limited Company (AG), SC=European Cooperative Society (SCE), SE=Company under European Law (SE, Societa Europaea), GEN=Industrial Cooperative Society, GES=Limited Liability Company (GmbH), KG=Limited Partnership, OG=Open Company]
  LFBSheetPr nVarChar(3) Lgl Form on Bal Sht Dte Prv Yr [AG=Public Limited Company (AG), SC=European Cooperative Society (SCE), SE=Company under European Law (SE, Societa Europaea), GEN=Industrial Cooperative Society, GES=Limited Liability Company (GmbH), KG=Limited Partnership, OG=Open Company]
  RegNum nVarChar(7) Reg. No. of Partner Company
  CmpanyName Text(16) Company Name
  XMLFile Text(16) XML File Storage
  TimeOfRun Int(6) Time of Run

# OEJD - Company Details for ERV-JAb
Module: Reports | 6 columns
Indexes (name: columns; first = primary key; U = unique) - WARNING: multi-column key order here is reversed vs SAP's 10.0 reference (read as a set; see references/dictionary/INDEX.md):
  PRIMARY U: AbsEntry
Fields (name type(len) description [values] ->parent table):
  AbsEntry Int(11) Internal Number
  CRegNum nVarChar(7) Commercial Register Number
  LFBSheet nVarChar(3) Legal Form on Actl Bal Sht Dte [AG=Public Limited Company (AG), SC=European Cooperative Society (SCE), SE=Company under European Law (SE, Societa Europaea), GEN=Industrial Cooperative Society, GES=Limited Liability Company (GmbH), KG=Limited Partnership, OG=Open Company]
  LFBSheetPr nVarChar(3) Lgl Form on Bal Sht Dte Prv Yr [AG=Public Limited Company (AG), SC=European Cooperative Society (SCE), SE=Company under European Law (SE, Societa Europaea), GEN=Industrial Cooperative Society, GES=Limited Liability Company (GmbH), KG=Limited Partnership, OG=Open Company, CNE=Company does not exist]
  RegNum nVarChar(7) Reg. No. of Partner Company
  CmpanyName Text(16) Company Name

# OEML - E-mail Log
Module: Reports | 14 columns
Indexes (name: columns; first = primary key; U = unique) - WARNING: multi-column key order here is reversed vs SAP's 10.0 reference (read as a set; see references/dictionary/INDEX.md):
  PRIMARY U: AbsEntry
Fields (name type(len) description [values] ->parent table):
  AbsEntry Int(11) Internal Number
  CardCode nVarChar(15) BP Code ->OCRD
  CardName nVarChar(100) BP Name
  DocEntry Int(11) Doc Internal Number
  ObjType nVarChar(20) Object Type
  DocNum Int(11) Document Number
  EMailAddr nVarChar(100) E-Mail Address
  SendDate Date(8) Send Date
  SendTime Int(6) Time Sent
  USERID Int(6) User Signature ->OUSR
  U_NAME nVarChar(155) User Name
  Subject nVarChar(254) Subject
  Body Text(16) Body
  AtcEntry Int(11) Attachment Entry ->OATC

# OFLT - Report - Selection Criteria
Module: Reports | 292 columns | ObjType: 54
Indexes (name: columns; first = primary key; U = unique) - WARNING: multi-column key order here is reversed vs SAP's 10.0 reference (read as a set; see references/dictionary/INDEX.md):
  PRIMARY U: FilterName, UserSign, FormNum
Fields (name type(len) description [values] ->parent table):
  FormNum nVarChar(20) Form Number
  QueryStr nVarChar(250) Query
  ItmOrCrd VarChar(1) Items or BP default=Y [Y=Yes, N=No]
  CardInclud VarChar(1) BP Area default=Y [Y=Yes, N=No]
  CardFrom1 nVarChar(15) From BP ->OCRD
  CardTo1 nVarChar(15) To BP ->OCRD
  CardExclud VarChar(1) Excluding BP default=N [Y=Yes, N=No]
  CardFrom2 nVarChar(15) BP Rejected
  CardTo2 nVarChar(15) BP Rejected
  ClienGroup Int(6) Customer Group
  VendGroup Int(6) Vendor Group
  ClntQryGrp nVarChar(250) Customer Properties
  VeQryGroup nVarChar(250) Vendor Properties
  ItmInclud VarChar(1) Item Range default=Y [Y=Yes, N=No]
  ItmFrom1 nVarChar(50) From Item ->OITM
  ItmTo1 nVarChar(50) To Item ->OITM
  ItmExclud VarChar(1) Excluding Materials default=N [Y=Yes, N=No]
  ItmFrom2 nVarChar(50) Item Rejected ->OITM
  ItmTo2 nVarChar(50) Item Rejected ->OITM
  ItmGroup Int(6) Item Group ->OITB
  ItQryGroup nVarChar(250) Item Properties
  WhsInclude VarChar(1) Warehouse Range default=Y [Y=Yes, N=No]
  WhsFrom1 nVarChar(8) From Warehouse ->OWHS
  WhsTo1 nVarChar(8) To Warehouse ->OWHS
  WhsExclude VarChar(1) Excluding Warehouses default=N [Y=Yes, N=No]
  WhsFrom2 nVarChar(8) Warehouse Rejected
  WhsTo2 nVarChar(8) Warehouse Rejected
  FromAcct nVarChar(15) From Account
  ToAcct nVarChar(15) To Account
  GroupMask nVarChar(12) Group Mask
  FromDate Date(8) From Posting Date
  ToDate Date(8) To Posting Date
  FrmDueDate Date(8) Due Date From
  ToDueDate Date(8) Due Date To
  FromDate3 Date(8) From Date 3
  ToDate3 Date(8) To Date 3
  FromDate4 Date(8) From Date 4
  ToDate4 Date(8) To Date 4
  SourceType Int(6) Original Journal default=-1 [15=Delivery, 16=Returns, 203=A/R Down Payment, 13=A/R Invoice, 14=A/R Credit Memo, 132=Correction Invoice, 20=Goods Receipt, 21=Goods Returns, 204=A/P Down Payment, 18=A/P Invoice, 19=A/P Credit Memo, 69=Landed Costs, 163=A/P Correction Invoice, 24=Incoming Payment, 25=Deposit, 46=Vendor Payment, 57=Checks for Payment, 76=Postdated Deposit, -2=Opening Balance, -3=Closing Balance, 30=Journal Entry, 58=Stock Update, 59=Goods Receipt, 60=Goods Issue, 67=Inventory Transfers, 68=Work Instructions, 162=Inventory Valuation, -1=All Transactions]
  FrmTrnsNum Int(11) From Transaction No.
  ToTrnsNum Int(11) To Transaction No.
  FromRef1 nVarChar(100) From Reference 1
  ToRef1 nVarChar(100) To Reference 1
  FromRef2 nVarChar(100) From Reference 2
  ToRef2 nVarChar(100) To Reference 2
  FrmTrnsCod nVarChar(4) From Transaction Code
  ToTrnsCod nVarChar(4) To Transaction Code
  FromSum Num(19,6) From Amount
  ToSum Num(19,6) To Amount
  FrmFRNAmnt Num(19,6) From FC Amount
  ToFRNAmnt Num(19,6) To FC Amount
  MemoIn nVarChar(50) Details Contained
  SortField1 Int(6) Sort Field 1 default=-1
  Break1 VarChar(1) Subtotal by Sort 1 default=N [Y=Yes, N=No]
  SortField2 Int(6) Sort Field 2 default=-1
  Break2 VarChar(1) Subtotal by Sort 2 default=N [Y=Yes, N=No]
  SortField3 Int(6) Sort Field 3 default=-1
  Break3 VarChar(1) Subtotal by Sort 3 default=N [Y=Yes, N=No]
  Display VarChar(1) Display default=L [L=Postings Only, T=Totals Only, B=Postings + Totals]
  PrntCutDat VarChar(1) Print Date Selection Criteria default=Y [Y=Yes, N=No]
  CheckBox0 VarChar(1) Check box 0 default=N [Y=Yes, N=No]
  CheckBox1 VarChar(1) Check box 1 default=N [Y=Yes, N=No]
  CheckBox2 VarChar(1) Check box 2 default=N [Y=Yes, N=No]
  CheckBox3 VarChar(1) Check box 3 default=N [Y=Yes, N=No]
  CheckBox4 VarChar(1) Check box 4 default=N [Y=Yes, N=No]
  CheckBox5 VarChar(1) Check box 5 default=N [Y=Yes, N=No]
  CheckBox6 VarChar(1) Check box 6 default=N [Y=Yes, N=No]
  CheckBox7 VarChar(1) Check box 7 default=N [Y=Yes, N=No]
  CheckBox8 VarChar(1) Check box 8 default=N [Y=Yes, N=No]
  CheckBox9 VarChar(1) Check box 9 default=N [Y=Yes, N=No]
  ShowZero VarChar(1) Display Zero Balances default=N [Y=Yes, N=No]
  DateCheck VarChar(1) Confirm Date Range default=N [Y=Yes, N=No]
  DueCheck VarChar(1) Confirm Due Date Range default=N [Y=Yes, N=No]
  CutCheck VarChar(1) Confirm Date Selectn Criteria default=N [Y=Yes, N=No]
  CutByObj VarChar(1) Selection Criteria by Object default=N [Y=Yes, N=No]
  ObjectC1 VarChar(1) C1 default=N [Y=Yes, N=No]
  ObjectC2 VarChar(1) C2 default=N [Y=Yes, N=No]
  ObjectC3 VarChar(1) C3 default=N [Y=Yes, N=No]
  ObjectC4 VarChar(1) C4 default=N [Y=Yes, N=No]
  ObjectC5 VarChar(1) C5 default=N [Y=Yes, N=No]
  ObjectC6 VarChar(1) C6 default=N [Y=Yes, N=No]
  ObjectC7 VarChar(1) C7 default=N [Y=Yes, N=No]
  ObjectC8 VarChar(1) C8 default=N [Y=Yes, N=No]
  ObjectC9 VarChar(1) C9 default=N [Y=Yes, N=No]
  ObjectC10 VarChar(1) C10 default=N [Y=Yes, N=No]
  ObjectC11 VarChar(1) C11 default=N [Y=Yes, N=No]
  ObjectC12 VarChar(1) C12 default=N [Y=Yes, N=No]
  ObjectC13 VarChar(1) C13 default=N [Y=Yes, N=No]
  ObjectC14 VarChar(1) C14 default=N [Y=Yes, N=No]
  ObjectC15 VarChar(1) C15 default=N [Y=Yes, N=No]
  ObjectC16 VarChar(1) C16 default=N [Y=Yes, N=No]
  FromAmount Num(19,6) From Amount
  ToAmount Num(19,6) To Amount
  FrmSalsMan Int(6) From Sales Employee
  ToSalsMan Int(6) To Sales Employee
  USER_CHK1 VarChar(1) User CheckBox 1 default=N [Y=Yes, N=No]
  USER_CHK2 VarChar(1) User CheckBox 2 default=N [Y=Yes, N=No]
  USER_CHK3 VarChar(1) User CheckBox 3 default=N [Y=Yes, N=No]
  USER_CHK4 VarChar(1) System Currrency default=N [Y=Yes, N=No]
  USER_CHK5 VarChar(1) System and Local Currency default=N [Y=Yes, N=No]
  UseSort VarChar(1) Sort default=N [Y=Yes, N=No]
  Sort1Up VarChar(1) Sort1 default=Y [Y=Ascending, N=Descending]
  Sort2Up VarChar(1) Sort2 default=Y [Y=Ascending, N=Descending]
  Sort3Up VarChar(1) Sort3 default=Y [Y=Ascending, N=Descending]
  FromAmnt2 Num(19,6) From Quantity Release
  ToAmount2 Num(19,6) For Quantity Release
  TaxDateFro Date(8) Lower Limit for Tax Data
  TaxDateTo Date(8) Top Limit for Document Dates
  FinancYear Date(8) Start of Fiscal Year
  BdgtScenar Int(11) Budget Scenario
  CompFolder nVarChar(100) Company Database
  CheckBox10 VarChar(1) Exapan Check Box 1 default=N [Y=Yes, N=No]
  FROM_FC Num(19,6) Foreign Currency from
  TO_FC Num(19,6) Foreign Currency to
  FCCurrency nVarChar(3) Foreign Currency
  TaxCheck VarChar(1) Confirm Document Date Range default=N [Y=Yes, N=No]
  DateType VarChar(1) Selection Criteria Type default=R [R=Posting Date, D=Due Date, T=Document Date]
  DateType2 VarChar(1) Selection Criteria Type default=R [R=Posting Date, D=Due Date, T=Document Date]
  FromPrject nVarChar(20) From Project ->OPRJ
  ToProject nVarChar(20) To Project ->OPRJ
  TemplateId Int(11) Template default=0
  ShowLeads VarChar(1) Display Leads default=N [Y=Yes, N=No]
  MthDate VarChar(1) Reconciliation Date default=N [Y=Yes, N=No]
  AccntntCod VarChar(1) External Code default=N [Y=Yes, N=No]
  UserSign Int(6) User Signature ->OUSR
  BlcNunFrom nVarChar(100) Block Number From
  BlcNunTo nVarChar(100) Block Number To
  ImpLogFrom nVarChar(20) Import Log From
  ImpLogTo nVarChar(20) Import Log To
  FolderNum VarChar(1) Folder Number default=1
  MainField Int(6) Main Field default=23
  TransMode VarChar(1) Transaction Mode default=Y [Y=Yes, N=No]
  MonthMode VarChar(1) Month Totals Mode default=N [Y=Yes, N=No]
  CheckBox11 VarChar(1) Expan Check Box 11 default=N [Y=Yes, N=No]
  FromIdc nVarChar(2) Indicator From
  ToIdc nVarChar(2) Indicator To
  IgnoreAdj VarChar(1) Ignore Adjustments default=N [Y=Yes, N=No]
  RefNumFrom nVarChar(254) From Reference No.
  RefNumTo nVarChar(254) To Reference No.
  PymNumfrom Int(11) Payment No. From
  PymNumTo Int(11) To Payment No.
  BankFrom nVarChar(30) From Bank Code
  BankTo nVarChar(30) To Bank Code
  DpstFrom Int(11) From Deposit Code
  DpstTo Int(11) To Deposit Code
  DpstType VarChar(1) Deposit Type
  ObjectC17 VarChar(1) Obj C17 default=N [Y=Yes, N=No]
  ObjectC18 VarChar(1) Obj C18 default=N [Y=Yes, N=No]
  ObjectC19 VarChar(1) Obj C19 default=N [Y=Yes, N=No]
  ObjAbs Int(11) Document Internal Number
  AddBTF VarChar(1) Add Journal Vouchers default=N [Y=Yes, N=No]
  FilePath Text(16) File Path
  DpsBnkActF nVarChar(50) From Deposit Bank Account
  DpsBnkActT nVarChar(50) To Deposit Bank Account
  FromKey Int(11) From Key
  ToKey Int(11) To Key
  ObjectC20 VarChar(1) Object C20 default=N [Y=Yes, N=No]
  ObjectC21 VarChar(1) Object C21 default=N [Y=Yes, N=No]
  ObjectC22 VarChar(1) Object C22 default=N [Y=Yes, N=No]
  ObjectC23 VarChar(1) Object C23 default=N [Y=Yes, N=No]
  ObjectC25 VarChar(1) Object C25 default=N [Y=Yes, N=No]
  USER_CHK6 VarChar(1) Include CB in P/L Accounts default=N [Y=Yes, N=No]
  OcrChkDim2 VarChar(1) Checkbox for Dimension 2 default=N [Y=Yes, N=No]
  OcrChkDim3 VarChar(1) Checkbox for Dimension 3 default=N [Y=Yes, N=No]
  OcrChkDim4 VarChar(1) Checkbox for Dimension 4 default=N [Y=Yes, N=No]
  OcrChkDim5 VarChar(1) Checkbox for Dimension 5 default=N [Y=Yes, N=No]
  OcrFrom2 nVarChar(8) From Costing Code 2 ->OOCR
  OcrFrom3 nVarChar(8) From Costing Code 3 ->OOCR
  OcrFrom4 nVarChar(8) From Costing Code 4 ->OOCR
  OcrFrom5 nVarChar(8) From Costing Code 5 ->OOCR
  OcrTo2 nVarChar(8) To Costing Code 2 ->OOCR
  OcrTo3 nVarChar(8) To Costing Code 3 ->OOCR
  OcrTo4 nVarChar(8) To Costing Code 4 ->OOCR
  OcrTo5 nVarChar(8) To Costing Code 5 ->OOCR
  TaxAdjRep Text(16) Object C24
  ObjectC26 VarChar(1) Object C26 default=N [Y=Yes, N=No]
  CBFilter VarChar(1) Closing Balances Filter default=2 [1=Closing Balance of Life-to-Date, 2=Closing Balance Before Selected Period Only]
  OBIncluded VarChar(1) Add Opening Balance for Period default=N [Y=Yes, N=No]
  OBFilter VarChar(1) Opening Balances Filter default=1 [1=Opening Balance from Start of Company Activity, 2=Opening Balance from Start of Fiscal Year]
  ExportCurr VarChar(1) Export Currency default=L [L=Local Currency, S=System Currency]
  CBIncluded VarChar(1) Add Closing Balances default=N [Y=Yes, N=No]
  SlpFrom nVarChar(155) Slp From
  SlpTo nVarChar(155) Slp To
  CBUDF VarChar(1) User-Defined Fields default=N [Y=Yes, N=No]
  CBREF VarChar(1) Reference Fields default=N [Y=Yes, N=No]
  CheckBoxB VarChar(1) Checkbox for Branch default=N [Y=Yes, N=No]
  FilterName nVarChar(30) Filter Name default=_
  JDTFixedF Int(6) JE Fixed Fields
  JDT1FixedF Int(6) JE Line Fixed Fields
  JDTUserF Int(6) JE User Fields
  JDT1UserF Int(6) JE Line User Fields
  BPFilter VarChar(1) BP Filter Enabled default=N [Y=Yes, N=No]
  AcctFltr VarChar(1) Account Filter Enabled default=N [Y=Yes, N=No]
  ZeroLCAmt VarChar(1) Show Zero LC Amount Lines default=N [Y=Yes, N=No]
  SplitByBin VarChar(1) Split By Bin Location default=N [Y=Yes, N=No]
  SplitBySnb VarChar(1) Split By Batch/Serial default=N [Y=Yes, N=No]
  CheckBox12 VarChar(1) Check Box 12 default=N [Y=Yes, N=No]
  CheckBox13 VarChar(1) Check Box 13 default=N [Y=Yes, N=No]
  CheckBox14 VarChar(1) Check Box 14 default=N [Y=Yes, N=No]
  CheckBox15 VarChar(1) Check Box 15 default=N [Y=Yes, N=No]
  CheckBox16 VarChar(1) Check Box 16 default=N [Y=Yes, N=No]
  CheckBox17 VarChar(1) Check Box 17 default=N [Y=Yes, N=No]
  CheckBox18 VarChar(1) Check Box 18 default=N [Y=Yes, N=No]
  CheckBox19 VarChar(1) Check Box 19 default=N [Y=Yes, N=No]
  CheckBox20 VarChar(1) Check Box 20 default=N [Y=Yes, N=No]
  CheckBox21 VarChar(1) Check Box 21 default=N [Y=Yes, N=No]
  CheckBox22 VarChar(1) Check Box 22 default=N [Y=Yes, N=No]
  CheckBox23 VarChar(1) Check Box 23 default=N [Y=Yes, N=No]
  CheckBox24 VarChar(1) Check Box 24 default=N [Y=Yes, N=No]
  CheckBox25 VarChar(1) Check Box 25 default=N [Y=Yes, N=No]
  CheckBox26 VarChar(1) Check Box 26 default=N [Y=Yes, N=No]
  CheckBox27 VarChar(1) Check Box 27 default=N [Y=Yes, N=No]
  CheckBox28 VarChar(1) Check Box 28 default=N [Y=Yes, N=No]
  CheckBox29 VarChar(1) Check Box 29 default=N [Y=Yes, N=No]
  CheckBox30 VarChar(1) Check Box 30 default=N [Y=Yes, N=No]
  CheckBox31 VarChar(1) Check Box 31 default=N [Y=Yes, N=No]
  CheckBox32 VarChar(1) Check Box 32 default=N [Y=Yes, N=No]
  CheckBox33 VarChar(1) Check Box 33 default=N [Y=Yes, N=No]
  BatchFrom nVarChar(36) Batch From
  BatchTo nVarChar(36) Batch To
  BatAttr1F nVarChar(36) Batch Attr. 1 From
  BatAttr1T nVarChar(36) Batch Attr. 1 To
  BatAttr2F nVarChar(36) Batch Attr. 2 From
  BatAttr2T nVarChar(36) Batch Attr. 2 To
  SerialNoF nVarChar(36) Serial Number From
  SerialNoT nVarChar(36) Serial Number To
  MfrSerailF nVarChar(36) Mfr Serial Number From
  MfrSerailT nVarChar(36) Mfr Serial Number To
  LotNumberF nVarChar(36) Lot Number From
  LotNumberT nVarChar(36) Lot Number To
  BinLocFrom nVarChar(228) Bin Location From
  BinLocTo nVarChar(228) Bin Location To
  AltSrtCodF nVarChar(50) Alternative Sort Code From
  AltSrtCodT nVarChar(50) Alternative Sort Code To
  BinSbl1F nVarChar(50) Bin Sublevel 1 From
  BinSbl1To nVarChar(50) Bin Sublevel 1 To
  BinSbl2F nVarChar(50) Bin Sublevel 2 From
  BinSbl2To nVarChar(50) Bin Sublevel 2 To
  BinSbl3F nVarChar(50) Bin Sublevel 3 From
  BinSbl3To nVarChar(50) Bin Sublevel 3 To
  BinSbl4F nVarChar(50) Bin Sublevel 4 From
  BinSbl4To nVarChar(50) Bin Sublevel 4 To
  BinAttr1F nVarChar(20) Bin Attribute 1 From
  BinAttr1To nVarChar(20) Bin Attribute 1 To
  BinAttr2F nVarChar(20) Bin Attribute 2 From
  BinAttr2To nVarChar(20) Bin Attribute 2 To
  BinAttr3F nVarChar(20) Bin Attribute 3 From
  BinAttr3To nVarChar(20) Bin Attribute 3 To
  BinAttr4F nVarChar(20) Bin Attribute 4 From
  BinAttr4To nVarChar(20) Bin Attribute 4 To
  BinAttr5F nVarChar(20) Bin Attribute 5 From
  BinAttr5To nVarChar(20) Bin Attribute 5 To
  BinAttr6F nVarChar(20) Bin Attribute 6 From
  BinAttr6To nVarChar(20) Bin Attribute 6 To
  BinAttr7F nVarChar(20) Bin Attribute 7 From
  BinAttr7To nVarChar(20) Bin Attribute 7 To
  BinAttr8F nVarChar(20) Bin Attribute 8 From
  BinAttr8To nVarChar(20) Bin Attribute 8 To
  BinAttr9F nVarChar(20) Bin Attribute 9 From
  BinAttr9To nVarChar(20) Bin Attribute 9 To
  BinAttr10F nVarChar(20) Bin Attribute 10 From
  BinAttr10T nVarChar(20) Bin Attribute 10 To
  EnfBinFltr VarChar(1) Enforced Bin Filter default=N [E=Enforced Bin Location, U=Unenforced Bin Location, B=Both, N=Bin not activated]
  ExItemFrom nVarChar(50) Expand from Item ->OITM
  ExItemTo nVarChar(50) Expand to Item ->OITM
  ExBPFrom nVarChar(15) Expand from BP ->OCRD
  ExBPTo nVarChar(15) Expand to BP ->OCRD
  CheckBox34 VarChar(1) Check Box 34 default=N [Y=Yes, N=No]
  CheckBox35 VarChar(1) Check Box 35 default=N [Y=Yes, N=No]
  BlAgreem VarChar(1) Checkbox for Blanket Agreement default=N
  BAFrom nVarChar(8) Blanket Agreement From
  BATo nVarChar(8) Blanket Agreement To
  AdjTrans VarChar(1) Adjustment Transactions default=N [Y=Yes, N=No]
  TitAcctLvl Int(11) Title Account Level default=2
  CCDFrom1 nVarChar(40) CCD Number from condition 1
  CCDTo1 nVarChar(40) CCD Number to Condition 1
  CCDFrom2 nVarChar(40) CCD Number from Condition 2
  CCDTo2 nVarChar(40) CCD Number to Condition 2
  ArchJrnal VarChar(1) Archiving Journal default=N [Y=Yes, N=No]
  CardFrom3 nVarChar(15) From BP
  CardTo3 nVarChar(15) To BP
  OBBranch VarChar(1) Divide Totals by Branch default=N [Y=Yes, N=No]
  AccumDbCr VarChar(1) Accumulated Debit/Credit default=N [Y=Yes, N=No]
  RscFrom1 nVarChar(50) From Resource ->ORSC
  RscTo1 nVarChar(50) To Resource ->ORSC
  RscGroup Int(6) Resource Group ->ORSB
  RouteStage VarChar(1) Use Route Stage default=N [Y=Yes, N=No]
  ExRSTFrom Int(11) From Route Stage ->ORST
  ExRSTTo Int(11) To Route Stage ->ORST
  StgSeqNum VarChar(1) Use Stage Sequence Number default=N [Y=Yes, N=No]
  ExSSNFrom Int(11) From Stage Sequence Number
  ExSSNTo Int(11) To Stage Sequence Number

# OGDP - General Data Protection Wizard
Module: Reports | 14 columns
Indexes (name: columns; first = primary key; U = unique) - WARNING: multi-column key order here is reversed vs SAP's 10.0 reference (read as a set; see references/dictionary/INDEX.md):
  PRIMARY U: AbsEntry
  SECONDARY U: RunName
Fields (name type(len) description [values] ->parent table):
  AbsEntry Int(11) Internal Number
  RunName nVarChar(100) Wizard Run Name
  RunDate Date(8) Wizard Run Date
  Status VarChar(1) Wizard Run Status default=S [S=Saved, E=Executed, P=Printed, V=Print Preview Generated]
  UserSign Int(6) User Signature
  UserSign2 Int(6) Updating User
  CreateDate Date(8) Creation Date
  CreateTS Int(11) Create Time - Incl. Secs
  UpdateDate Date(8) Date of Update
  UpdateTS Int(11) Update Full Time
  Action VarChar(1) Personal Data Management Wizard Action default=R [R=Personal Data Report, E=Personal Data Cleanup, B=Personal Data Blocking, U=Personal Data Unblocking, I=Determine Natural Persons, N=Reverse Natural Person Determination]
  BPType VarChar(1) Business Partner Type default=B [B=Business Partners, D=Default Customers]
  PostDateTo Date(8) Posting Date To
  EmpType VarChar(1) Employee Type default=E [E=Employees, S=Sales Employees/Buyers]

# OIRC - Interactive Report Category
Module: Reports | 10 columns
Indexes (name: columns; first = primary key; U = unique) - WARNING: multi-column key order here is reversed vs SAP's 10.0 reference (read as a set; see references/dictionary/INDEX.md):
  PRIMARY U: CategoryId
Fields (name type(len) description [values] ->parent table):
  CategoryId Int(11) Category Id
  ParentId Int(11) Parent Category Id default=-1
  Name nVarChar(254) Category Name
  ResKey nVarChar(128) Resource Key
  Comment nVarChar(254) Comment
  System VarChar(1) System default=N
  CreateBy nVarChar(25) Created By
  CreateDate Date(8) Creation Timestamp
  ModifyBy nVarChar(25) Modified By
  ModifyDate Date(8) Modification Timestamp

# OIRD - Report Definition
Module: Reports | 11 columns
Indexes (name: columns; first = primary key; U = unique) - WARNING: multi-column key order here is reversed vs SAP's 10.0 reference (read as a set; see references/dictionary/INDEX.md):
  PRIMARY U: ReportId
Fields (name type(len) description [values] ->parent table):
  ReportId nVarChar(254) Report Id
  Type Int(11) Type default=1
  CategoryId Int(11) Category Id
  Revision nVarChar(10) Revision
  Title nVarChar(254) Title
  Definition Text(16) Report Definition
  System VarChar(1) System
  CreateBy nVarChar(25) Created By
  CreateDate Date(8) Creation Timestamp
  ModifyBy nVarChar(25) Modified By
  ModifyDate Date(8) Modification Timestamp

# OLLR - Electronic Report Generation Result
Module: Reports | 9 columns
Indexes (name: columns; first = primary key; U = unique) - WARNING: multi-column key order here is reversed vs SAP's 10.0 reference (read as a set; see references/dictionary/INDEX.md):
  PRIMARY U: AbsEntry
  REPORT: EReportId
Fields (name type(len) description [values] ->parent table):
  AbsEntry Int(11) Internal Number
  UserSign Int(6) User Signature ->OUSR
  CreateDate Date(8) Creation Date
  CreateTime Int(6) Creation Time
  EReportId Int(11) Electronic Report ID ->OLLF
  Status VarChar(1) Status default=C [C=Canceled, E=Executed, F=Failed]
  Log Text(16) Run Log
  ReportInst Int(11) Electronic Report Instance
  VersionNum nVarChar(11) Version Number

# OQAG - Query Authorization Groups
Module: Reports | 10 columns
Indexes (name: columns; first = primary key; U = unique) - WARNING: multi-column key order here is reversed vs SAP's 10.0 reference (read as a set; see references/dictionary/INDEX.md):
  PRIMARY U: AUTHGRPID
  NAME_KEY U: AUTHGRPCD
  DES_KEY U: AUTHGRPN
Fields (name type(len) description [values] ->parent table):
  AUTHGRPID Int(11) Query Authorization Group ID
  AUTHGRPCD nVarChar(50) Group Code
  AUTHGRPN nVarChar(254) Group Description
  LogInstanc Int(11) Log Instance default=0
  UserSign Int(6) Item Created By ->OUSR
  UserSign2 Int(6) Item Updated By ->OUSR
  UpdateDate Date(8) Date of Update
  CreateDate Date(8) Date of Create
  Deleted VarChar(1) Deleted Field default=N
  SnapShotID Int(11) Snapshot ID default=0

# OQCN - Query Catagories
Module: Reports | 5 columns | ObjType: 134
Indexes (name: columns; first = primary key; U = unique) - WARNING: multi-column key order here is reversed vs SAP's 10.0 reference (read as a set; see references/dictionary/INDEX.md):
  PRIMARY U: CategoryId
  CAT_NAME_K: CatName
Fields (name type(len) description [values] ->parent table):
  CategoryId Int(11) Category ID
  CatName nVarChar(50) Category Name
  PermMask nVarChar(20) Permissions default=NNNNNNNNNNNNNNN
  DataSource VarChar(1) Data Source default=N [N=Unknown, I=Interface, U=Upgrade, M=Import, O=DI API, A=Doc. Generation Wizard, D=Restore Wizard, P=Partner Implementation, T=Year Transfer]
  UserSign Int(6) User Signature ->OUSR

# OQWZ - Query Wizard
Module: Reports | 3 columns | ObjType: 141
Indexes (name: columns; first = primary key; U = unique) - WARNING: multi-column key order here is reversed vs SAP's 10.0 reference (read as a set; see references/dictionary/INDEX.md):
  PRIMARY U: Code
  NAME U: Name
Fields (name type(len) description [values] ->parent table):
  Code nVarChar(8) Query Code
  Name nVarChar(50) Query Name
  UserSign Int(6) User Signature ->OUSR

# ORFL - Already Displayed 347, 349 and WTax Reports
Module: Reports | 6 columns | ObjType: 179
Indexes (name: columns; first = primary key; U = unique) - WARNING: multi-column key order here is reversed vs SAP's 10.0 reference (read as a set; see references/dictionary/INDEX.md):
  PRIMARY U: OrdinalNum, TaxCode, LineNum, DocType, ReportType, DocEntry
Fields (name type(len) description [values] ->parent table):
  ReportType Int(11) Report Type [1=347, 2=349, 3=WT, 4=O & P, 5=Annual List, 6=Tax Report]
  DocType nVarChar(20) Document Type [13=Invoice, 14=Revert Invoice, 18=Purchase, 19=Revert purchase, 203=A/R Down Payment, 204=A/P Down Payment]
  DocEntry Int(11) Document Internal ID
  LineNum Int(11) Row No.
  TaxCode nVarChar(8) Tax Code
  OrdinalNum Int(11) Ordinal Num (BTF & Cancelled) default=-1

# OSEL - Selection Lists
Module: Reports | 4 columns
Indexes (name: columns; first = primary key; U = unique) - WARNING: multi-column key order here is reversed vs SAP's 10.0 reference (read as a set; see references/dictionary/INDEX.md):
  PRIMARY U: AbsEntry
Fields (name type(len) description [values] ->parent table):
  UserID Int(6) User Signature ->OUSR
  FilterName nVarChar(30) Filter Name default=_
  FormNum nVarChar(20) Form Number
  AbsEntry Int(11) Internal ID

# OSOI - Statement of Import Wizard
Module: Reports | 12 columns
Indexes (name: columns; first = primary key; U = unique) - WARNING: multi-column key order here is reversed vs SAP's 10.0 reference (read as a set; see references/dictionary/INDEX.md):
  PRIMARY U: WizardId
Fields (name type(len) description [values] ->parent table):
  WizardId Int(11) Wizard ID
  Name nVarChar(100) Name
  Date Date(8) Run Date
  UserSign Int(6) User Signature
  AgrNoFrom Int(11) Agreement No. From
  AgrNoTo Int(11) Agreement No. To
  PDateFrm Date(8) Posting Date From
  PDateTo Date(8) Posting Date To
  OrigWizId Int(11) Original Wizard ID
  OrigSOINum Int(11) Original Statement No.
  Status VarChar(1) Status default=N [N=Created, C=Correction, U=Updated, D=Deleted]
  CorrType VarChar(1) Correction Type [R=Replacement, A=Adjustment]

# OSOIL - Statement of Import Wizard Run
Module: Reports | 4 columns
Indexes (name: columns; first = primary key; U = unique) - WARNING: multi-column key order here is reversed vs SAP's 10.0 reference (read as a set; see references/dictionary/INDEX.md):
  PRIMARY U: SOIWNum
  SECONDARY U: AbsEntry
Fields (name type(len) description [values] ->parent table):
  SOIWNum nVarChar(100) Statement No.
  WizardId Int(11) Wizard ID
  SOINum Int(11) SOI
  AbsEntry Int(11) Abs Entry

# OSQR - Standard Queries
Module: Reports | 7 columns
Indexes (name: columns; first = primary key; U = unique) - WARNING: multi-column key order here is reversed vs SAP's 10.0 reference (read as a set; see references/dictionary/INDEX.md):
  PRIMARY U: IntrnalKey
  QNAME_K U: QName
Fields (name type(len) description [values] ->parent table):
  IntrnalKey Int(11) Internal Key
  QCategory Int(11) Query Group
  QName nVarChar(100) Query Name
  QString Text(16) Query
  QType VarChar(1) Query Type default=R [R=Regular, W=Wizard, G=Report Generator]
  ColumnSize nVarChar(100) Column Size
  DBType Int(11) DB Type

# OSRA - Scheduled Report Actions
Module: Reports | 40 columns
Indexes (name: columns; first = primary key; U = unique) - WARNING: multi-column key order here is reversed vs SAP's 10.0 reference (read as a set; see references/dictionary/INDEX.md):
  PRIMARY U: ActionCode
Fields (name type(len) description [values] ->parent table):
  ActionCode Int(11) Action Code
  Title nVarChar(100) Title
  Notes Text(16) Remarks
  UserKey Int(11) User ->OUSR
  Password nVarChar(254) Password
  RunDate Date(8) Next Run Date
  RunTime Int(11) Next Run Time
  RunCounter Int(11) Next Run Counter default=0
  ReportType Int(11) Report Type default=0 [0=Invalid, 115=User Query, 857=Sales/Purchase Analysis, 6000=Inventory Valuation]
  Active VarChar(1) Schedule Active Status default=Y [N=No, Y=Yes]
  StartDate Date(8) Recurrence Start Date
  EndType VarChar(1) Recurrence End Type default=N [N=No End, C=By Counter, D=By Date]
  EndDate Date(8) Recurrence End Date
  EndCounter Int(11) Recurrence End Counter default=1
  MissBehav VarChar(1) Behavior of Missed Run default=S [S=Skip, R=Run as Soon as Possible]
  RcrType VarChar(1) Recurrence Type default=N [N=None, D=Daily, W=Weekly, M=Monthly, Y=Annually]
  RcrIntervl Int(11) Recurrence Interval default=1
  RcrSubType Int(11) Recurrence Subtype
  RcrData2 Int(11) Recurrence: Additional Data 2
  RcrData1 Int(11) Recurrence: Additional Data 1
  ErrAct VarChar(1) Action on Error default=1 [D=Deactivate Immediately, C=Continue, 1=Deactivate on Second Failure, 2=Deactivate on Third Failure, 3=Deactivate on Fourth Failure]
  TransfXslt Text(16) XSLT Transformation
  TimeOut Int(11) Rpt Creation Time-Out in Min. default=5
  MsgTitle nVarChar(254) Message Title
  MsgBody nVarChar(254) Message Body
  LicSrvr nVarChar(254) License Server
  Language Int(11) Language default=3
  LstRunStat VarChar(1) Last Run Status default=0 [0=Not yet executed, S=Success, T=SAP Business One client stopped due to time-out, U=The next run date was not updated, D=Unable to distribute result, X=Unspecified failure, F=Successfully finished]
  ErrorCount Int(11) Number of Failed Runs default=0
  PrntLayout nVarChar(20) Print Layout ->RDOC
  DistLstCod Int(11) Distribution List Code ->OMLS
  Finished VarChar(1) Schedule Finished Status default=N
  SLDAddr nVarChar(254) SLD Address
  ObjType nVarChar(20) Object Type
  ObjAbsEnt Int(11) Object Abs Entry
  OnceAt Int(11) Once At
  Every Int(11) Every
  StartAt Int(11) Starting At
  EndAt Int(11) Ending At
  DFType VarChar(1) Daily Frequency Type default=O [O=Once, E=Every, D=By Date]

# OSRT - Korean Summary Report
Module: Reports | 10 columns
Indexes (name: columns; first = primary key; U = unique) - WARNING: multi-column key order here is reversed vs SAP's 10.0 reference (read as a set; see references/dictionary/INDEX.md):
  PRIMARY U: AbsId
  SUM_RPT_ID U: SumRptId
Fields (name type(len) description [values] ->parent table):
  AbsId Int(11) Abstract ID
  SumRptId nVarChar(100) Summary Report ID
  SumRptDate Date(8) Summary Report Date
  BPLId Int(11) Business Place ID
  FromDate Date(8) From Date
  ToDate Date(8) To Date
  RptType VarChar(1) Report Type default=C [V=Vendor, C=Customer]
  version nVarChar(50) Report Generation Version
  SumSubId nVarChar(254) Summary Report Sub ID
  SumRptType nVarChar(254) Summary Report Type

# OTHL - Thresholds
Module: Reports | 12 columns
Indexes (name: columns; first = primary key; U = unique) - WARNING: multi-column key order here is reversed vs SAP's 10.0 reference (read as a set; see references/dictionary/INDEX.md):
  PRIMARY U: AbsEntry
Fields (name type(len) description [values] ->parent table):
  AbsEntry Int(11) Internal Number
  RecType VarChar(1) Report Type default=A [A=Annual Invoice Declaration, B=Blacklist Country]
  EffecFrom Date(8) Effective From
  Company nVarChar(20) Company
  PrivInv nVarChar(20) Private - Invoice
  PrivJE nVarChar(20) Private - Journal Entry
  LogInstanc Int(11) Log Instance
  UserSign Int(6) User Signature ->OUSR
  CreateDate Date(8) Creation Date
  UserSign2 Int(6) Updating User ->OUSR
  UpdateDate Date(8) Date of Update
  Tourism nVarChar(20) Tourism

# OTRB - Tax Report Wizard for Brazil
Module: Reports | 18 columns
Indexes (name: columns; first = primary key; U = unique) - WARNING: multi-column key order here is reversed vs SAP's 10.0 reference (read as a set; see references/dictionary/INDEX.md):
  PRIMARY U: AbsEntry
  SECONDARY U: RunName
Fields (name type(len) description [values] ->parent table):
  AbsEntry Int(11) Internal Number
  BPLId Int(11) Branch ID ->OBPL
  GPCId Int(11) Government Payment Code ->OGPC
  GPCCode nVarChar(6) Government Payment Code
  Year Int(6) Reporting Year
  PrdType VarChar(1) Period Type [Q=Quarter, M=Month, H=Half Month, T=Ten Days]
  PrdNum Int(11) Period Number
  PrdDate Date(8) Period Date To
  RunName nVarChar(100) Wizard Run Name
  RunDate Date(8) Wizard Run Date
  Status VarChar(1) Wizard Run Status [S=Saved, E=Executed, C=Canceled]
  StateTax VarChar(1) State Tax default=N [Y=Yes, N=No]
  DueDate Date(8) Due Date
  UserSign Int(6) User Signature
  UserSign2 Int(6) Updating User
  CreateDate Date(8) Creation Date
  CreateTime Int(6) Generation Time
  UpdateDate Date(8) Date of Update

# OTRS - Tax Report Saving Object
Module: Reports | 15 columns
Indexes (name: columns; first = primary key; U = unique) - WARNING: multi-column key order here is reversed vs SAP's 10.0 reference (read as a set; see references/dictionary/INDEX.md):
  PRIMARY U: AbsEntry
Fields (name type(len) description [values] ->parent table):
  AbsEntry Int(11) Internal Number
  ObjType nVarChar(20) Object Type
  ReportType Int(11) Report Type [1=VAT Report (UK)]
  PeriodType VarChar(1) Report Period Type [Y=Year, Q=Quarter, M=Month, P=Period]
  PeriodNum Int(11) Report Period Number
  Year Int(6) Report Year
  AdjustNum Int(6) Report Adjustment Number
  ApUserSign Int(6) Approved By (User Signature)
  ApDate Date(8) Approval Date
  ApTime Int(6) Approval Time
  DeclType VarChar(1) Declaration Type default=O [O=Original, S=Substitute, C=Complementary]
  SCDateFrom Date(8) Selection Criteria - Date From
  SCDateTo Date(8) Selection Criteria - Date To
  BosCode Int(11) Box Set Code ->OBOS
  BatchNum Int(11) Journal Voucher No. ->OBTD

# OTRX - Transformation Documents
Module: Reports | 5 columns
Indexes (name: columns; first = primary key; U = unique) - WARNING: multi-column key order here is reversed vs SAP's 10.0 reference (read as a set; see references/dictionary/INDEX.md):
  PRIMARY U: AbsEntry
  CODE U: Code
Fields (name type(len) description [values] ->parent table):
  AbsEntry Identity(11) Internal Number
  Code nVarChar(20) Code
  Descr nVarChar(250) Description
  Type nVarChar(8) Type default=XSLT [XSLT=XSLT Document]
  Data Text(16) Data

# OTSM - Tax Summary Report Method
Module: Reports | 2 columns
Indexes (name: columns; first = primary key; U = unique) - WARNING: multi-column key order here is reversed vs SAP's 10.0 reference (read as a set; see references/dictionary/INDEX.md):
  PRIMARY U: AbsEntry
Fields (name type(len) description [values] ->parent table):
  AbsEntry Int(11) Abs. Entry
  Descript nVarChar(20) Description

# OTWS - E-Tax Web Site
Module: Reports | 6 columns
Indexes (name: columns; first = primary key; U = unique) - WARNING: multi-column key order here is reversed vs SAP's 10.0 reference (read as a set; see references/dictionary/INDEX.md):
  PRIMARY U: AbsEntry
  TWSNAME: TwsName
Fields (name type(len) description [values] ->parent table):
  AbsEntry Int(6) E-Tax Internal ID
  TwsName nVarChar(64) E-Tax Web Site Name
  TwsURL Text(16) E-Tax Web Site URL
  TwsDescrip nVarChar(200) E-Tax Web Site Description
  UserSign Int(6) User Signature - Create ->OUSR
  UserSign2 Int(6) Updating User ->OUSR

# OUQR - Queries
Module: Reports | 10 columns | ObjType: 160
Indexes (name: columns; first = primary key; U = unique) - WARNING: multi-column key order here is reversed vs SAP's 10.0 reference (read as a set; see references/dictionary/INDEX.md):
  PRIMARY U: QCategory, IntrnalKey
  QNAME_K U: QCategory, QName
Fields (name type(len) description [values] ->parent table):
  IntrnalKey Int(11) Internal Key
  QCategory Int(11) Query Category ->OQCN
  QName nVarChar(100) Query Description
  QString Text(16) Query
  QType VarChar(1) Query Type default=W [R=Regular, W=Wizard, G=Report Generator, S=Stored Procedure]
  ColumnSize nVarChar(100) Column Size
  DBType Int(11) DB Type
  QLastDate Date(8) Last Upload Date
  QLastTime Int(6) Last Upload Time
  Xslt Text(16) XSLT Transformation

# PRS1 - Detail Lines of Print Sequence Definition
Module: Reports | 10 columns
Indexes (name: columns; first = primary key; U = unique) - WARNING: multi-column key order here is reversed vs SAP's 10.0 reference (read as a set; see references/dictionary/INDEX.md):
  PRIMARY U: LineNum, SeqID
Fields (name type(len) description [values] ->parent table):
  SeqID Int(11) Internal Number
  LineNum Int(6) Row Number
  ObjectID Int(11) Document Object ID
  LaytCode nVarChar(8) Report Code
  NumCopy Int(6) Number of Copies
  UsrQuery Int(11) User Query to Customize
  SubDocType Int(6) Document Subtype
  Printer nVarChar(100) Printer
  Prtr1st nVarChar(100) Printer for First Page
  Use1stPrtr VarChar(1) Use 1st Page Printer default=N [Y=Yes, N=No]

# QWZ1 - Query Tables
Module: Reports | 9 columns
Indexes (name: columns; first = primary key; U = unique) - WARNING: multi-column key order here is reversed vs SAP's 10.0 reference (read as a set; see references/dictionary/INDEX.md):
  PRIMARY U: Numerator, Code
Fields (name type(len) description [values] ->parent table):
  Code nVarChar(8) Query Code
  Numerator Int(11) Internal Number
  FileCode nVarChar(20) Table Name
  IsTemp VarChar(1) Is Temp default=N [Y=Yes, N=No]
  DoJoin VarChar(1) Do Join default=N [Y=Yes, N=No]
  JoinToTbl Int(11) Joined to Table
  NumOfConds Int(11) No. of Conds.
  OuterJoin VarChar(1) Outer Join default=N [Y=Yes, N=No]
  RightJoin VarChar(1) Right Join default=N [Y=Yes, N=No]

# QWZ2 - Query Result Fields
Module: Reports | 19 columns
Indexes (name: columns; first = primary key; U = unique) - WARNING: multi-column key order here is reversed vs SAP's 10.0 reference (read as a set; see references/dictionary/INDEX.md):
  PRIMARY U: Numerator, Code
Fields (name type(len) description [values] ->parent table):
  Code nVarChar(8) Query Code
  Numerator Int(11) Internal Number
  FileCode nVarChar(20) Table Name
  FieldAlias nVarChar(10) Field Alias
  Title nVarChar(30) Field Title
  SortOrder Int(11) Sort Order
  SortType VarChar(1) Sort Type default=N [Y=Yes, N=No]
  GroupBy VarChar(1) Group By default=N [Y=Yes, N=No]
  AgregType Int(11) Agreggate Function
  CalcField nVarChar(254) Calculation Field
  IsCalc VarChar(1) Is Calculation default=N [Y=Yes, N=No]
  TmpAlias nVarChar(11) New Alias in Res. Table
  TmpDescr nVarChar(30) New Description in Res. Table
  Fld2Alias nVarChar(10) Field 2 Number
  FileCode2 nVarChar(20) Field 2 Table Name
  Agreg2Type Int(11) Field 2 Aggregate Function
  FldOp Int(11) Formula Operation
  FldCnstVal nVarChar(254) Field Const. Val.
  Fld2CnsVal nVarChar(254) Field 2 Const. Val.

# QWZ3 - Query Condition Fields
Module: Reports | 15 columns
Indexes (name: columns; first = primary key; U = unique) - WARNING: multi-column key order here is reversed vs SAP's 10.0 reference (read as a set; see references/dictionary/INDEX.md):
  PRIMARY U: Numerator, Code
Fields (name type(len) description [values] ->parent table):
  Code nVarChar(8) Query Code
  Numerator Int(11) Internal Number
  OpenBrackt Int(11) Open Brackets Counter
  FileCode nVarChar(20) Table Name
  FieldAlias nVarChar(30) Field Alias
  Operation Int(11) Operation
  CondVal nVarChar(254) Cond. Val.
  CondEndVal nVarChar(254) Cond. and Val.
  CompareFld VarChar(1) Compare Fields default=N [Y=Yes, N=No]
  UseRes VarChar(1) Use Res. default=N [Y=Yes, N=No]
  CompTblIdx nVarChar(20) Compare Table Index
  CompFldNum nVarChar(254) Compare Field Number
  Relatship Int(11) Relationship
  ClosBrackt Int(11) Close Brackets Counter
  Free_Text Text(16) Free Text

# RDC1 - Multilingual Report
Module: Reports | 9 columns
Indexes (name: columns; first = primary key; U = unique) - WARNING: multi-column key order here is reversed vs SAP's 10.0 reference (read as a set; see references/dictionary/INDEX.md):
  PRIMARY U: LineNum, DocCode
  UniqueIdx U: LangCode, DocCode
Fields (name type(len) description [values] ->parent table):
  DocCode nVarChar(8) Doc. Code ->RDOC
  LineNum Int(11) Line Number
  DocName nVarChar(64) Doc. Name
  LangCode Int(11) Language Code
  Template Text(16) Report Template Data
  CreateDate Date(8) Create Date
  CreateTime Int(11) Create Time
  UpdateDate Date(8) Update Date
  UpdateTime Int(11) Update Time

# RDFL - Document Standards
Module: Reports | 6 columns
Indexes (name: columns; first = primary key; U = unique) - WARNING: multi-column key order here is reversed vs SAP's 10.0 reference (read as a set; see references/dictionary/INDEX.md):
  PRIMARY U: CardCode, UserId, DoumntDode
  CODE: DoumntDode
Fields (name type(len) description [values] ->parent table):
  DoumntDode nVarChar(4) Code
  UserId Int(11) User Signature
  DfltReport nVarChar(8) Standard Report
  CardCode nVarChar(15) BP Code default=-1 ->OCRD
  DfltSeq Int(11) Standard Sequence
  TYPE VarChar(1) Type default=L [L=Layout, P=Print Sequence]

# RDOC - Document
Module: Reports | 65 columns | ObjType: 232
Indexes (name: columns; first = primary key; U = unique) - WARNING: multi-column key order here is reversed vs SAP's 10.0 reference (read as a set; see references/dictionary/INDEX.md):
  PRIMARY U: DocCode
  TYPE: TypeCode
  TYPENAME: DocName, TypeCode
Fields (name type(len) description [values] ->parent table):
  DocCode nVarChar(8) Code
  DocName nVarChar(120) Name
  Author nVarChar(155) Author
  Notes nVarChar(254) Remarks
  Width Int(6) Width default=595
  Height Int(6) Height default=842
  LMargin Int(6) Left Margin default=10
  RMargin Int(6) Right Margin default=30
  TMargin Int(6) Top Margin default=10
  BMargin Int(6) Bottom Margin default=10
  CanChange VarChar(1) Changeable default=Y [Y=Yes, N=No]
  PaperSize nVarChar(100) Paper Size default=A4
  Oreint VarChar(1) Orientation default=P [P=Vertical, L=Horizontal]
  GridSize Int(6) Grid Size default=10
  GridType VarChar(1) Grid Type default=1 [1=Combination, 2=Continuous Line, 3=Broken Line, 4=Dots]
  ShowGrid VarChar(1) Display Grid default=Y [Y=Yes, N=No]
  SnapGrid VarChar(1) Next to Grid default=Y [Y=Yes, N=No]
  Picture Text(16) Picture
  TypeCode nVarChar(4) Type Code
  FrgnReport VarChar(1) Foreign Language Report default=N [Y=Yes, N=No]
  CanSort VarChar(1) Sortable default=Y [Y=Yes, N=No]
  LeaderCode nVarChar(8) Leader Report
  FollowCode nVarChar(8) Follow-Up Report
  SwapOnScrn VarChar(1) Convert Font in Print Preview default=N [Y=Yes, N=No]
  ScreenFont nVarChar(50) Preview Printing Font default=Arial
  ScrFOffset Int(6) Change Font Size in Print Preview default=-1
  SwpInEmail VarChar(1) Convert Font for E-Mail default=N [Y=Yes, N=No]
  EmailFont nVarChar(50) E-Mail Font default=Arial
  EmFOffset Int(6) Change Font Size for E-Mail default=-1
  QString Text(16) Query
  QType VarChar(1) Query Type default=R [R=Regular, W=Wizard]
  Language Int(11) Language ->OLNG
  RobjCode Int(11) Imp Exp Obj Code default=0
  ExtName Text(16) Extension Name
  ExtOnErr VarChar(1) Action for extension error default=S [S=Stop, I=Ignore, P=Prompt]
  NumRepArs Int(6) Number of Repetitive Areas default=1
  AlgnFooter VarChar(1) Allign Footer to Buttom default=N [Y=Yes, N=No]
  TimeFormat VarChar(1) Time Template default=0 [0=Default, 1=24H, 2=12H]
  DateFormat VarChar(1) Date Template default=0 [0=Default, 1=DD/MM/YY, 2=DD/MM/CCYY, 3=MM/DD/YY, 4=MM/DD/CCYY, 5=CCYY/MM/DD, 6=DD/Month/YYYY]
  DateSep VarChar(1) Date Separator
  DecSep VarChar(1) Decimal Separator
  ThousSep VarChar(1) Thousands Separator
  Printer nVarChar(100) Printer
  NumLayPage Int(11) Number of Layout Pages
  NumCopy Int(11) Number of Copies default=1
  GbiSupport VarChar(1) GBI Settings Supported default=N [Y=Yes, N=No]
  Use1stPrtr VarChar(1) Use 1st Page Printer default=N [Y=Yes, N=No]
  Prtr1st nVarChar(100) Printer for First Page
  Shading VarChar(1) Print Item Backgrounds default=Y [Y=Yes, N=No]
  Template Text(16) Report Binary Data
  Category VarChar(1) Category default=P [P=PLD, C=Crystal Reports, L=Legal List, A=Partner Type, E=Electronic Files]
  CreateDate Date(8) Creation Date
  UpdateDate Date(8) Date of Update
  UserSign Int(6) User Signature
  UserSign2 Int(6) Updating User
  Status VarChar(1) Status default=A [A=Active, I=Inactive]
  B1Version nVarChar(20) Required B1 Version
  CRVersion nVarChar(20) Required Crystal Version
  Local nVarChar(2) Localization
  UseSysPref VarChar(1) Use System Preference default=Y [Y=Yes, N=No]
  ForMobile VarChar(1) Visible For Mobile default=Y [Y=Yes, N=No]
  TypeDetail nVarChar(254) Type
  IsIMCE VarChar(1) Powered by SAP HANA default=N [Y=Yes, N=No]
  CsUrl nVarChar(254) URL in Crystal Server
  RptHash nVarChar(254) Hash for Report

# RITM - Reporting Element
Module: Reports | 88 columns
Indexes (name: columns; first = primary key; U = unique) - WARNING: multi-column key order here is reversed vs SAP's 10.0 reference (read as a set; see references/dictionary/INDEX.md):
  PRIMARY U: ItemId, DocCode
  CONTAINER: ItemGroup, ContIndex, Container, DocCode
  APPL_ID: ApplID, DocCode
  TYPE: ItemIndex, Type, DocCode
Fields (name type(len) description [values] ->parent table):
  DocCode nVarChar(8) Report ->RDOC
  ItemId Int(6) Item ID
  Container Int(6) Parent Type
  Type Int(6) Type [1=Page Header, 2=Start of Report, 3=Repetitive Area Header, 4=Repetitive Area, 5=Repetitive Area Footer, 6=End of Report, 7=Page Footer, 10=Text Field, 11=Picture Field, 12=User Field]
  VISIBLE VarChar(1) Visible default=Y [Y=Yes, N=No]
  SupZeros VarChar(1) Suppress Zeros default=N [Y=Yes, N=No]
  ItemLeft Int(6) Left Item
  ItemTop Int(6) Top
  Width Int(6) Width
  Height Int(6) Height
  LMargin Int(6) Left Margin default=0
  RMargin Int(6) Right Margin default=0
  TMargin Int(6) Top Margin default=0
  BMargin Int(6) Bottom Margin default=0
  LeftLine Int(6) Left Border Line Thickness default=0
  RightLine Int(6) Right Border Line Thickness default=0
  TopLine Int(6) Top Border Line Thickness default=0
  BottomLine Int(6) Bottom Border Line Thickness default=0
  Shadow Int(6) Shadow Thickness default=0
  BGRed Int(11) Background - Red default=255
  BGGreen Int(11) Background - Green default=255
  BGBlue Int(11) Background - Blue default=255
  FGRed Int(11) Text - Red default=0
  FGGreen Int(11) Text - Green default=0
  FGBlue Int(11) Text - Blue default=0
  MrkrRed Int(11) Bold - Red default=255
  MrkrGreen Int(11) Bold - Green default=255
  MrkrBlue Int(11) Bold - Blue default=255
  BrdrRed Int(11) Border - Red default=0
  BrdrGreen Int(11) Border - Green default=0
  BrdrBlue Int(11) Border - Blue default=0
  FromPane Int(6) From Area default=0
  ToPane Int(6) To Area default=0
  ItemGroup Int(6) Group No. default=0
  FontName nVarChar(50) Font Name default=Arial
  FontSize Int(6) Font Size default=12
  TextStyle Int(11) Text Style default=0
  Justific Int(6) Horizontal Justification default=2 [1=Right, 2=Left, 3=Centralized, 4=Language-Dependent]
  WRAP Int(6) Segment default=2 [0=Allow Overflow, 1=Adjust to Cell, 2=Divide into Rows]
  PictSize Int(6) Picture Size default=0 [0=Original Size, 1=Fit Field Size Non-Proportionally, 2=Fit Field Size Proportionally, 3=Fit Field Height, 4=Fit Fields Width]
  DataSource Int(6) Data Source default=1 [1=Static, 2=Variable, 3=Data, 4=Calculation]
  ItemStr Text(16) String
  VarNum Int(6) Variable No.
  FileName nVarChar(20) File Name
  FieldNum nVarChar(52) Field No.
  ShowDescr VarChar(1) Display Description default=Y [Y=Yes, N=No]
  CalcType nVarChar(2) Calculation Type default=1 [0=Formula, 1=Page Number, 17=Total Pages, 2=Date, 3=Time, 4=Column Total, 5=Column Average, 6=General Row No., 7=Group Row No., 8=Sort Field Name, 9=Sort Field Content, 10=Continue, 11=Continued on Next Page, 12=Generation Message, 13=Column Summary for Page, 14=Column Average for Page, 15=Column Summary for Report, 16=Column Average for Report]
  ChangFlags Int(11) Changeable
  ApplID Int(6) Item No.
  CalcCol Int(6) Calculation Column
  YJustific Int(6) Vertical Alignment default=3 [1=Top, 2=Bottom, 3=Centralized]
  SortLevel Int(6) Sort Level default=0
  RevOrder VarChar(1) Reverse Sort default=N [Y=Descending, N=Ascending]
  SortType Int(6) Sort Type default=0 [0=Alpha, 1=Numeric, 2=Currency, 3=Date]
  IsUnique VarChar(1) Unique default=N [Y=Yes, N=No]
  IsGroup VarChar(1) Set as Group default=N [Y=Yes, N=No]
  NewPage VarChar(1) New Page default=N [Y=Yes, N=No]
  BarCode VarChar(1) Print as Bar Code default=N [Y=Yes, N=No]
  Condition Text(16) Condition
  LinkTo nVarChar(20) Link to Field
  Operator1 Int(6) Operator 1
  Operator2 Int(6) Operator 2
  Operation Int(6) Operation default=0 [0=, 1=+, 2=-, 3=x, 4=/, 5=%, 17=Left Part (Characters), 18=Right Part (Mantissa), 19=Round, 6=$Concat, 7=$Right, 8=$Left, 9=$Sentence, 16=$Length, 20=$Currency, 21=$Number, 10=Less than, 11=Less or Equal, 12=Equal, 13=Not equal, 14=Greater or Equal, 15=Greater than]
  BCStandard Int(6) Bar Code Standard default=0 [0=EAN-13, 1=Code 39, 2=Code 128]
  SumInWords VarChar(1) Display Total as a Word default=N [Y=Yes, N=No]
  ExcFonting VarChar(1) Block Font Change default=N [Y=Yes, N=No]
  StrIndex Int(11) String Index default=0
  ContIndex Int(6) Container Index default=0
  ItemIndex Int(6) Item Index default=0
  StrLength Int(6) String Length
  StrFiller VarChar(1) String Filler
  RelatedTo nVarChar(20) Link to Field
  NextSeg nVarChar(20) Next Segment Item Number
  HightAdjst VarChar(1) Height Adjustments default=N [Y=Yes, N=No]
  DupRpttAre VarChar(1) Duplicate Repetitive Area default=N [Y=Yes, N=No]
  LnsRpttAre Int(11) No. of Rows in Repetitive Area default=0
  RptDupDist Int(11) Distance To Rptt Dup. (pixels) default=0
  FieldId nVarChar(20) Unique ID
  FGEnabled VarChar(1) Grid Enabled default=Y [Y=Yes, N=No]
  BGEnabled VarChar(1) Background Enabled default=Y [Y=Yes, N=No]
  MKEnabled VarChar(1) Highlight Enabled default=Y [Y=Yes, N=No]
  BDEnabled VarChar(1) Frame Enabled default=Y [Y=Yes, N=No]
  HidEmpRptt VarChar(1) Hide Empty Area default=N [Y=Yes, N=No]
  RpttFtrAll VarChar(1) Display Rep. Footer on All default=N [Y=Yes, N=No]
  GbiDataTyp Int(6) Data Type default=0 [0=, 1=C n, 2=C.. n, 3=I.. n, 4=D w.d]
  GbiDataLen nVarChar(6) Data Length
  PageBreak Int(6) Page Break default=0 [0=None, 1=Before Area, 2=After Area]
  IsLogo VarChar(1) Is Logo default=N [Y=Yes, N=No]

# RPRS - Print Sequence Definition
Module: Reports | 5 columns
Indexes (name: columns; first = primary key; U = unique) - WARNING: multi-column key order here is reversed vs SAP's 10.0 reference (read as a set; see references/dictionary/INDEX.md):
  PRIMARY U: SeqID
  OBJECT_ID: ObjectID
Fields (name type(len) description [values] ->parent table):
  SeqID Int(11) Sequence ID
  SeqName nVarChar(254) Sequence Name
  LineNum Int(6) Visual Order
  ObjectID Int(11) Document Object ID
  SubDocType Int(6) Document Subtype

# RTYP - Document Type List
Module: Reports | 9 columns | ObjType: 10000196
Indexes (name: columns; first = primary key; U = unique) - WARNING: multi-column key order here is reversed vs SAP's 10.0 reference (read as a set; see references/dictionary/INDEX.md):
  PRIMARY U: CODE
Fields (name type(len) description [values] ->parent table):
  CODE nVarChar(4) Report Type
  NAME nVarChar(250) Type Name
  DEFLT_REP nVarChar(8) Standard Report
  ADD_NAME nVarChar(250) Addon Name
  FRM_TYPE nVarChar(250) Add-On Form Type
  MNU_ID nVarChar(250) Menu Id
  IS_SYS VarChar(1) Is sytem type or not default=Y [Y=Yes, N=No]
  DEFLT_SEQ Int(11) Standard Sequence
  TYPE VarChar(1) Type default=L [L=Layout, P=Print Sequence]

# SCRT - SAP Crystal Reports Translations
Module: Reports | 4 columns
Indexes (name: columns; first = primary key; U = unique) - WARNING: multi-column key order here is reversed vs SAP's 10.0 reference (read as a set; see references/dictionary/INDEX.md):
  PRIMARY U: Language, ItemId, DocCode
Fields (name type(len) description [values] ->parent table):
  DocCode nVarChar(8) Doc. Code
  ItemId nVarChar(220) Item ID
  Language Int(11) Language ->OLNG
  String nVarChar(249) String

# SEL1 - Selection Lists - Lists
Module: Reports | 2 columns
Indexes (name: columns; first = primary key; U = unique) - WARNING: multi-column key order here is reversed vs SAP's 10.0 reference (read as a set; see references/dictionary/INDEX.md):
  PRIMARY U: ObjID, AbsEntry
Fields (name type(len) description [values] ->parent table):
  AbsEntry Int(11) Internal ID ->OSEL
  ObjID nVarChar(20) Object ID

# SOI1 - Statement of Import - Business Partners
Module: Reports | 2 columns
Indexes (name: columns; first = primary key; U = unique) - WARNING: multi-column key order here is reversed vs SAP's 10.0 reference (read as a set; see references/dictionary/INDEX.md):
  PRIMARY U: CardCode, WizardId
Fields (name type(len) description [values] ->parent table):
  WizardId Int(11) Wizard ID ->OSOI
  CardCode nVarChar(15) BP Card Code ->OCRD

# SOI2 - Statement of Import - Branches
Module: Reports | 2 columns
Indexes (name: columns; first = primary key; U = unique) - WARNING: multi-column key order here is reversed vs SAP's 10.0 reference (read as a set; see references/dictionary/INDEX.md):
  PRIMARY U: BPLId, WizardId
Fields (name type(len) description [values] ->parent table):
  WizardId Int(11) Wizard ID ->OSOI
  BPLId Int(11) Assigned Branch ->OBPL

# SOI3 - Statement of Import - Invoices
Module: Reports | 19 columns
Indexes (name: columns; first = primary key; U = unique) - WARNING: multi-column key order here is reversed vs SAP's 10.0 reference (read as a set; see references/dictionary/INDEX.md):
  PRIMARY U: SOINum, WizardId
Fields (name type(len) description [values] ->parent table):
  WizardId Int(11) Wizard ID
  SOINum Int(11) Statement No.
  AgrNum Int(11) Blanket Agreement No.
  AgrNo Int(11) Blanket Agreement Entry ->OOAT
  CardCode nVarChar(15) Customer/Vendor Code ->OCRD
  CardName nVarChar(100) Customer/Vendor Name
  PayToCtry nVarChar(3) BP Pay-to Country
  PmntNum Int(11) Payment No.
  PmntEntry Int(11) Payment Entry ->OVPM
  PmntType Int(11) Payment Type
  PmntDate Date(8) Payment Date
  ExcBasSum Num(19,6) Sum of Excise Base Amount
  ExciseSum Num(19,6) Sum of Excise Amount
  VatBaseSum Num(19,6) Sum of VAT Base Amount
  VatSum Num(19,6) Total of VAT
  RegNo nVarChar(18) Registration No.
  RegDate Date(8) Registration Date
  ExecStat VarChar(1) Execution Status default=S [S=Saved, E=Executed]
  BPLId Int(11) Branch ->OBPL

# SOI4 - Statement of Import - Invoices
Module: Reports | 9 columns
Indexes (name: columns; first = primary key; U = unique) - WARNING: multi-column key order here is reversed vs SAP's 10.0 reference (read as a set; see references/dictionary/INDEX.md):
  PRIMARY U: DocEntry, DocType, SOINum, WizardId
Fields (name type(len) description [values] ->parent table):
  WizardId Int(11) Wizard ID
  SOINum Int(11) Statement No.
  DocType Int(11) Document Type
  DocEntry Int(11) Document Abs Entry
  DocNum Int(11) Doc. No.
  DocDate Date(8) Posting Date
  TaxDate Date(8) Document Date
  NumAtCard nVarChar(100) BP Reference No.
  InvEntry Int(11) Invoice Abs Entry ->OINV

# SOI5 - Statement of Import - Lines
Module: Reports | 30 columns
Indexes (name: columns; first = primary key; U = unique) - WARNING: multi-column key order here is reversed vs SAP's 10.0 reference (read as a set; see references/dictionary/INDEX.md):
  PRIMARY U: DocLineNum, DocEntry, DocType, SOINum, WizardId
  SOILINENUM U: SOILineNum, SOINum, WizardId
Fields (name type(len) description [values] ->parent table):
  WizardId Int(11) Wizard ID
  SOINum Int(11) Statement No.
  DocType Int(11) Document Type
  DocEntry Int(11) Document Abs Entry
  SOILineNum Int(11) SOI Line No.
  DocLineNum Int(11) Line No.
  ItemCode nVarChar(50) Item No. ->OITM
  ItemName nVarChar(100) Item Description
  unitMsr nVarChar(100) UoM Name
  Quantity Num(19,6) Quantity
  TotalFrgn Num(19,6) Total (Doc.)
  LineTotal Num(19,6) Total (LC)
  Currency nVarChar(3) Currency ->OCRN
  Rate Num(19,6) Line Rate
  BaseRate Num(19,6) Base Currency Rate
  BasNumAtCr nVarChar(100) Base Ref. Vendor Ref. No.
  BaseDocNum Int(11) Base Ref. No.
  BaseEntry Int(11) Base Entry
  BasTaxDate Date(8) Base Ref. Document Date
  FExcBasSum Num(19,6) Fixed Excise Base Amount
  AExcBasSum Num(19,6) Ad Valorem Excise Base Amount
  ExciseUoM Int(11) Excise Units of Measure [112=Liters (m3), 168=Tons, metric tons (1000 kg), 251=Horsepower (1 hp = 0.75 kW), 831=Liters of anhydrous (pure) alcohol]
  ExcRateUoM Num(19,6) Excise Rate Units of Measure
  ExcRateAdV Num(19,6) Excise Rate Ad Valorem
  ExciseSum Num(19,6) Excise Amount
  VatBaseSum Num(19,6) VAT Base Amount
  VatPrcnt Num(19,6) VAT Rate per Row
  VatSum Num(19,6) VAT Amount
  TaxCtgr VarChar(1) Tax Type (Annual List)
  VatGroup nVarChar(8) VAT Code

# SQR1 - System Queries
Module: Reports | 2 columns
Indexes (name: columns; first = primary key; U = unique) - WARNING: multi-column key order here is reversed vs SAP's 10.0 reference (read as a set; see references/dictionary/INDEX.md):
  PRIMARY U: Module, InternlKey
Fields (name type(len) description [values] ->parent table):
  InternlKey Int(11) Internal ID
  Module Int(11) Module

# SRA1 - Scheduled Report Parameters
Module: Reports | 7 columns
Indexes (name: columns; first = primary key; U = unique) - WARNING: multi-column key order here is reversed vs SAP's 10.0 reference (read as a set; see references/dictionary/INDEX.md):
  PRIMARY U: ParamCode, ActionCode
  SECONDARY U: KeyNumber, KeyString, ActionCode
Fields (name type(len) description [values] ->parent table):
  ActionCode Int(11) Action Code
  ParamCode Int(11) Parameter Code
  KeyString nVarChar(32) Parameter Key String
  KeyNumber Int(11) Parameter Key Numerator
  ValString Text(16) Parameter Value String
  ValNumber Int(11) Parameter Value Number
  ValMoney Num(19,6) Parameter Value Money

# SRA2 - Scheduled Report Run Output
Module: Reports | 13 columns
Indexes (name: columns; first = primary key; U = unique) - WARNING: multi-column key order here is reversed vs SAP's 10.0 reference (read as a set; see references/dictionary/INDEX.md):
  PRIMARY U: Time, Date, ActionCode
  ACTIONCODE: ActionCode
Fields (name type(len) description [values] ->parent table):
  ActionCode Int(11) Action Code
  Date Date(8) Date of Run
  Time Int(11) Time of Run
  Status VarChar(1) Status default=0 [S=Successful, E=In progress, F=Failure, T=Results to Be Distributed, 0=Schedule Inactive, 1=Report Scheduled]
  ReturnCode Int(11) Return Code
  ReturnStr nVarChar(250) Return String
  ResDag Text(16) Result in DAG format
  ResPdf Text(16) Result in PDF format
  ResHtml Text(16) Result in HTML format
  ResXml Text(16) Result in XML format
  Results nVarChar(10) Result Availability default=NNNN
  ResLog Text(16) Report Creation Log
  ErrScreen Text(16) Error Screenshot

# SRA3 - Scheduled Report Recipients
Module: Reports | 15 columns
Indexes (name: columns; first = primary key; U = unique) - WARNING: multi-column key order here is reversed vs SAP's 10.0 reference (read as a set; see references/dictionary/INDEX.md):
  PRIMARY U: RecipCode, ActionCode
  USER: Name
Fields (name type(len) description [values] ->parent table):
  ActionCode Int(11) Action Code ->OSRA
  RecipCode Int(11) Recipient Code
  ObjType nVarChar(20) Object Type
  ObjCode nVarChar(50) Object Code
  Name nVarChar(155) Name
  SendInter VarChar(1) Send Internally default=N [Y=Yes, N=No]
  SendEmail VarChar(1) Send as E-Mail default=N [Y=Yes, N=No]
  SendSMS VarChar(1) Send as SMS default=N [Y=Yes, N=No]
  Email nVarChar(100) E-Mail Address
  Number nVarChar(100) Telephone Number
  AttachDAG VarChar(1) Attach DAG default=N [Y=Yes, N=No]
  AttachPDF VarChar(1) Attach PDF default=N [Y=Yes, N=No]
  AttachHTML VarChar(1) Attach HTML default=N
  AttachXML VarChar(1) Attach XML default=N [Y=Yes, N=No]
  ShowResult VarChar(1) Results Visible to User default=Y [Y=Yes, N=No]

# SRT1 - Korean Summary Report - Rows1
Module: Reports | 6 columns
Indexes (name: columns; first = primary key; U = unique) - WARNING: multi-column key order here is reversed vs SAP's 10.0 reference (read as a set; see references/dictionary/INDEX.md):
  PRIMARY U: SeqNo, SumRptId
Fields (name type(len) description [values] ->parent table):
  SumRptId nVarChar(100) Summary Rpt ID
  SeqNo Int(11) Sequence Number
  CardNum Int(11) Business Partner Total Numbers
  TransNum Int(11) Total Trans Number Under BP
  BaseAmt Num(19,6) Total Base Amount Under BPs
  TaxAmt Num(19,6) Total Tax Amount Under BPs

# SRT2 - Korean Summary Report - Rows2
Module: Reports | 9 columns
Indexes (name: columns; first = primary key; U = unique) - WARNING: multi-column key order here is reversed vs SAP's 10.0 reference (read as a set; see references/dictionary/INDEX.md):
  PRIMARY U: SeqNo, SumRptId
Fields (name type(len) description [values] ->parent table):
  SumRptId nVarChar(100) Summary Rpt ID
  SeqNo Int(11) Sequence Number
  VATRegNum nVarChar(12) VAT Reg. Number of BP
  CardCode nVarChar(15) BP Code on OCRD
  CardName nVarChar(100) BP Name
  TransNo Int(11) Total Trans Number under BP
  BaseAmt Num(19,6) Total Base Amount under BP
  TaxAmt Num(19,6) Total Tax Amount under BP
  Remark nVarChar(100) Line Item Remark, do not use

# TRB1 - Tax Report Wizard Selected States
Module: Reports | 2 columns
Indexes (name: columns; first = primary key; U = unique) - WARNING: multi-column key order here is reversed vs SAP's 10.0 reference (read as a set; see references/dictionary/INDEX.md):
  PRIMARY U: State, AbsEntry
Fields (name type(len) description [values] ->parent table):
  AbsEntry Int(11) Internal Number ->OTRB
  State nVarChar(3) State Code ->OCST

# TRB2 - Tax Report Wizard Selected Tax Types
Module: Reports | 2 columns
Indexes (name: columns; first = primary key; U = unique) - WARNING: multi-column key order here is reversed vs SAP's 10.0 reference (read as a set; see references/dictionary/INDEX.md):
  PRIMARY U: StaType, AbsEntry
Fields (name type(len) description [values] ->parent table):
  AbsEntry Int(11) Internal Number ->OTRB
  StaType Int(11) Tax Authority Type ->OSTT

# TRB3 - Tax Report Wizard - Selected Tax Categories
Module: Reports | 2 columns
Indexes (name: columns; first = primary key; U = unique) - WARNING: multi-column key order here is reversed vs SAP's 10.0 reference (read as a set; see references/dictionary/INDEX.md):
  PRIMARY U: NfTaxId, AbsEntry
Fields (name type(len) description [values] ->parent table):
  AbsEntry Int(11) Internal Number ->OTRB
  NfTaxId Int(11) ID of Nota Fiscal Tax Category ->ONFT

# TRB4 - Tax Report Wizard - Selected Tax Entries
Module: Reports | 4 columns
Indexes (name: columns; first = primary key; U = unique) - WARNING: multi-column key order here is reversed vs SAP's 10.0 reference (read as a set; see references/dictionary/INDEX.md):
  PRIMARY U: TaxLine, TaxEntry, TaxSrcType, AbsEntry
Fields (name type(len) description [values] ->parent table):
  AbsEntry Int(11) Internal Number ->OTRB
  TaxSrcType Int(11) Tax Source Object TYpe default=10000011 [10000011=VAT Transactions, 243000003=Brazil - Tax Adjustment]
  TaxEntry Int(11) Tax Entry
  TaxLine Int(11) Tax Line

# TRB5 - Tax Report Wizard Reported Tax Sums
Module: Reports | 12 columns
Indexes (name: columns; first = primary key; U = unique) - WARNING: multi-column key order here is reversed vs SAP's 10.0 reference (read as a set; see references/dictionary/INDEX.md):
  PRIMARY U: State, AbsEntry
Fields (name type(len) description [values] ->parent table):
  AbsEntry Int(11) Internal Number ->OTRB
  State nVarChar(3) State Code ->OCST
  CardCode nVarChar(15) Vendor Code ->OCRD
  TransCrdt Num(19,6) Transferred Credit
  TotalDbt Num(19,6) Total Reported Debit
  TtlDbtSc Num(19,6) Total Reported Debit SC
  TotalCrdt Num(19,6) Total Reported Credit
  TtlCrdtSc Num(19,6) Total Reported Credit SC
  TotalDed Num(19,6) Total Reported Tax Deductions
  TtlDedSc Num(19,6) Total Reported Tax Deductions SC
  BlncDue Num(19,6) Balance Due
  TransId Int(11) Transaction Number ->OJDT

# TRS1 - Tax Report Saving Object - Approved Documents
Module: Reports | 11 columns
Indexes (name: columns; first = primary key; U = unique) - WARNING: multi-column key order here is reversed vs SAP's 10.0 reference (read as a set; see references/dictionary/INDEX.md):
  PRIMARY U: LineID, AbsEntry
  SECONDARY U: PayDocEntr, PayDocType, PayLineID, MeansType, ApDocOrdNo, ApDocEntry, ApDocType, AbsEntry
Fields (name type(len) description [values] ->parent table):
  AbsEntry Int(11) Internal Number ->OTRS
  ObjType nVarChar(20) Object Type
  LineID Int(11) Internal Row Number
  ApDocType nVarChar(20) Approved Document Type
  ApDocEntry Int(11) Approved Document Key
  ApDocOrdNo Int(11) Appr. Doc. Ordinal Number default=-1
  ApDocAdRef Int(11) Appr. Doc. Additional Reference default=-1
  MeansType Int(11) Payment Means Type default=-1
  PayLineID Int(11) Payment Means Line ID default=-1
  PayDocType Int(11) Payment Document Type default=-1
  PayDocEntr Int(11) Payment Document Entry default=-1

# TRS2 - Tax Rpt Sav Obj Man Chgd Vals
Module: Reports | 8 columns
Indexes (name: columns; first = primary key; U = unique) - WARNING: multi-column key order here is reversed vs SAP's 10.0 reference (read as a set; see references/dictionary/INDEX.md):
  PRIMARY U: LineID, AbsEntry
  SECONDARY U: ParamCode, AbsEntry
Fields (name type(len) description [values] ->parent table):
  AbsEntry Int(11) Internal Number
  ObjType nVarChar(20) Object Type
  LineID Int(11) Internal Row Number
  ParamCode nVarChar(32) Parameter Code
  PrmValAmt Num(19,6) Parameter Value Amount
  PrmValNum Int(11) Parameter Value Number
  PrmValStr nVarChar(8) Parameter Value String
  PrmValTxt Text(16) Parameter Value Text

# UQR1 - Queries
Module: Reports | 2 columns
Indexes (name: columns; first = primary key; U = unique) - WARNING: multi-column key order here is reversed vs SAP's 10.0 reference (read as a set; see references/dictionary/INDEX.md):
  PRIMARY U: Module, InternlKey
Fields (name type(len) description [values] ->parent table):
  InternlKey Int(11) Internal ID
  Module Int(11) Module

# XRDBV - XLR company DB version
Module: Reports | 8 columns
Indexes (name: columns; first = primary key; U = unique) - WARNING: multi-column key order here is reversed vs SAP's 10.0 reference (read as a set; see references/dictionary/INDEX.md):
  PRIMARY U: DBObjVer
Fields (name type(len) description [values] ->parent table):
  DBObjVer nVarChar(20) IXDBObjectsVersion
  DBObjVerDe nVarChar(254) IXDBObjectsVersionDescr
  DBObjVerUp Date(8) IXDBObjectsVersionUpdated
  ParVer nVarChar(20) PartnerVersion
  ParVerDesc nVarChar(254) PartnerVersionDescr
  ParVerUpd Date(8) PartnerVersionUpdated
  Partner nVarChar(50) Partner
  PartnerDBV nVarChar(50) PartnerDBVersion

# XROBJ - XLR Company Report Objects
Module: Reports | 13 columns
Indexes (name: columns; first = primary key; U = unique) - WARNING: multi-column key order here is reversed vs SAP's 10.0 reference (read as a set; see references/dictionary/INDEX.md):
  PRIMARY U: Global, RepObjId
Fields (name type(len) description [values] ->parent table):
  RepObjId nVarChar(38) RepObjId
  Name nVarChar(50) Name
  Descriptio Text(16) Description
  Creator nVarChar(50) Creator
  CreateDate Date(8) Creation Date
  ModifyDate Date(8) ModifyDate
  ObjType Int(11) ObjType
  XmlId nVarChar(38) XmlId
  XlsId nVarChar(38) XlsID
  VariablesI nVarChar(38) VariablesID
  Reference Text(16) Reference
  RefType Int(11) RefType default=0
  Global Int(11) Global default=0

# XRREL - XLR Company Report Objects
Module: Reports | 5 columns
Indexes (name: columns; first = primary key; U = unique) - WARNING: multi-column key order here is reversed vs SAP's 10.0 reference (read as a set; see references/dictionary/INDEX.md):
  PRIMARY U: Global, ChildId, ParentId
Fields (name type(len) description [values] ->parent table):
  ParentId nVarChar(38) ParentId
  ChildId nVarChar(38) ChildId
  RelType Int(11) RelType default=1
  SeqNo Int(11) SeqNo default=0
  Global Int(11) Global default=0

# XRUDF - XLR company UDF
Module: Reports | 6 columns
Indexes (name: columns; first = primary key; U = unique) - WARNING: multi-column key order here is reversed vs SAP's 10.0 reference (read as a set; see references/dictionary/INDEX.md):
  PRIMARY U: UDFID
Fields (name type(len) description [values] ->parent table):
  UDFID Int(11) UDFID
  ColumnId nVarChar(254) ColumnId
  Module nVarChar(254) Module
  AttributeT Int(11) AttributeType
  Descriptio nVarChar(254) Description
  MetaName nVarChar(254) MetaName

# XRXLS - XLR company XLS
Module: Reports | 3 columns
Indexes (name: columns; first = primary key; U = unique) - WARNING: multi-column key order here is reversed vs SAP's 10.0 reference (read as a set; see references/dictionary/INDEX.md):
  PRIMARY U: Global, XlsId
Fields (name type(len) description [values] ->parent table):
  XlsId nVarChar(40) XlsID
  Xls Text(16) Xls
  Global Int(11) Global default=0

# XRXML - XLR company XML
Module: Reports | 3 columns
Indexes (name: columns; first = primary key; U = unique) - WARNING: multi-column key order here is reversed vs SAP's 10.0 reference (read as a set; see references/dictionary/INDEX.md):
  PRIMARY U: Global, XmlId
Fields (name type(len) description [values] ->parent table):
  XmlId nVarChar(40) XmlId
  Xml Text(16) Xml
  Global Int(11) Global default=0

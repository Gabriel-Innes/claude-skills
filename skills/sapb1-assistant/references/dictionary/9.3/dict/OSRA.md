<!-- source: erpref.com (schema IP: SAP) | version: SAP Business One 9.3 | verified: 2026-10-01 -->
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

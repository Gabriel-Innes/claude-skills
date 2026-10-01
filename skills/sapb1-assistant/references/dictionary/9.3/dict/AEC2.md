<!-- source: erpref.com (schema IP: SAP) | version: SAP Business One 9.3 | verified: 2026-10-01 -->
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

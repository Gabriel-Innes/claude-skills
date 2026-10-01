<!-- source: REFDB.chm (SAP Business One SDK 10.0 - Database Tables Reference) | version: SAP Business One 10.0 | verified: 2026-10-01 -->
# AEC2 - Electronic Transactions
Module: Reports | 40 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: AbsEntry, LogInstanc
Fields (name type(len) description [values] ->parent table):
  AbsEntry Int(11) Internal ID
  Code nVarChar(8) Code ->OECM
  ParentID Int(11) Parent ID ->ECM2
  ActType VarChar(1) Action Type [S=Setup, R=Report, D=A/R Document, P=A/P Document, F=A/R Draft Document, E=A/P Draft Document, O=Other, K=Skip, C=Contingency, B=BP Check, I=Incoming Payment, U=Outgoing Payment, A=Internal Reconciliation, T=Transportation Document, W=Inventory Transfer, V=VAT Obligations, N=VAT Declarations, L=VAT Liabilities, Y=VAT Payments, d=Delivery, r=Return, i=A/R Invoice, c=A/R Credit Memo, g=Goods Receipt PO, s=Goods Return, p=A/P Invoice, m=A/P Credit Memo, H=Draft Incoming Payment, J=Draft Outgoing Payment, Q=Journal Entry, X=E-Books Expense]
  ActDesc nVarChar(100) Action Description
  ActStatus VarChar(1) Action Status default=N [N=New, P=Pending, E=Error, T=Temporary Error, O=OK, S=Sent, R=Document Error, W=Waiting, A=Authorized, I=In Process, J=Rejected, D=Denied, C=Canceled, B=Aborted, Q=Queued, M=Imported, G=Warning, V=Approved, F=Approving, H=Rejecting, K=Generated, Y=Ready to Process, L=Determined]
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
  AssignedID nVarChar(100) Assigned ID
  DocBtch nVarChar(50) Document Batch
  DocBtchLn Int(6) Document Batch Line
  GenType VarChar(1) Generation Type default=N [N=Not Relevant, G=Generate, L=Generate - Later, S=Send, R=Send - Later]
  TestMode VarChar(1) Test Mode default=N [N=No, Y=Yes]
  PeriodType VarChar(1) Report Period Type [=Ignore, Y=Year, Q=Quarter, M=Month, P=Period]
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
  CancStatus VarChar(1) Cancelation Status default=T [T=, N=New Request, S=Request Sent, A=Approved, R=Rejected, E=Error, C=Canceled, I=In Process, U=Sent To Authorities]
  EDocType Int(11) E-Doc Type ->OUNCL
  EDocNum nVarChar(100) E-Doc Number
  ProcTarget nVarChar(40) Processing Target/Source

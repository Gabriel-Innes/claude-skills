<!-- source: REFDB.chm (SAP Business One SDK 10.0 - Database Tables Reference) | version: SAP Business One 10.0 | verified: 2026-10-01 -->
# ACLG - Activities - History
Module: Business Partners | 98 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: ClgCode, LogInstanc
  CRD_CODE: CardCode
  OPPORT: OprId, OprLine
Fields (name type(len) description [values] ->parent table):
  ClgCode Int(11) Activity Number
  CardCode nVarChar(15) BP Code ->OCRD
  Notes Text(16) Remarks
  CntctDate Date(8) System Date
  CntctTime Int(11) Time
  Recontact Date(8) Activity Date
  Closed VarChar(1) Closed Activity default=N [Y=Yes, N=No]
  CloseDate Date(8) Closing Date
  ContactPer nVarChar(90) Contact Person Name
  Tel nVarChar(50) Telephone
  Fax nVarChar(50) Fax
  CntctSbjct Int(6) Activity Subject default=-1 ->OCLS
  Transfered VarChar(1) Transferred to Next Year default=N [Y=Yes, N=No]
  DocType nVarChar(20) Linked Document default=-1 [13=A/R Invoice, 14=A/R Credit Memo, 15=Delivery, 16=Return, 17=Sales Order, 18=A/P Invoice, 19=A/P Credit Memo, 20=Goods Receipt PO, 21=Goods Return, 22=Purchase Order, 23=Sales Quotation, 24=Incoming Payment, 25=Deposit, 30=Journal Entry, 46=Outgoing Payment, 57=Checks for Payment, 59=Goods Receipt, 60=Goods Issue, 1250000001=Inventory Transfer Request, 67=Inventory Transfer, 68=Work Order, 69=Landed Costs, 132=Correction Invoice, 162=Material Revaluation, 202=Production Order, 203=A/R Down Payment, 204=A/P Down Payment, 140000009=Outgoing Excise Invoice, 140000010=Incoming Excise Invoice, -1=, 0=, 4=Items, 163=A/P Correction Invoice, 164=A/P Correction Invoice Reversal, 165=A/R Correction Invoice, 166=A/R Correction Invoice Reversal, 1320000012=Campaign, 540000006=Purchase Quotation, 1250000025=Blanket Agreements, 1470000113=Purchase Request, 112=Document Drafts, 140=Payment Drafts, 123=Checks for Payment Drafts]
  DocNum nVarChar(50) Linked Document Number
  DocEntry nVarChar(50) Linked Document Entry
  Attachment Text(16) Attachment
  DataSource VarChar(1) Data Source default=N [N=Unknown, I=Interface, U=Update, M=Import, O=DI API, S=Service Layer, W=Web Client, A=Doc. Generation Wizard, D=Restore Wizard, P=Partner Implementation, T=Year Transfer]
  AttendUser Int(6) Dealt by ->OUSR
  CntctCode Int(11) Contact Person ->OCPR
  UserSign Int(6) User Signature
  SlpCode Int(11) Sales Employee default=-1 ->OSLP
  Action VarChar(1) Activity default=C [C=Phone Call, M=Meeting, T=Task, E=Note, P=Campaign, N=Other]
  Details nVarChar(100) Details
  CntctType Int(6) Activity Type default=-1 ->OCLT
  Location Int(6) Location default=-1 ->OCLO
  BeginTime Int(11) Start Time
  Duration Num(19,6) Activity Duration
  DurType VarChar(1) Duration UoM default=M [S=Seconds, M=Minutes, H=Hours, D=Days]
  ENDTime Int(11) End Time
  Priority VarChar(1) Priority default=1 [0=Low, 1=Normal, 2=High]
  Reminder VarChar(1) Reminder default=N [Y=Yes, N=No]
  RemQty Num(19,6) Reminder Quantity
  RemType VarChar(1) Reminder Units default=M [S=Seconds, M=Minutes, H=Hours, D=Days]
  OprId Int(11) Opportunity - Key
  OprLine Int(6) Row No. - Opportunity
  RemDate Date(8) Reminder Date
  RemTime Int(6) Reminder Time
  RemSented VarChar(1) Reminder Was Sent default=N [Y=Yes, N=No]
  Instance Int(6) Instance default=0
  endDate Date(8) End/Due Date
  status Int(11) Status ->OCLA
  personal VarChar(1) Personal Flag default=N [Y=Yes, N=No]
  inactive VarChar(1) Inactive Flag default=N [Y=Yes, N=No]
  tentative VarChar(1) Tentative Flag default=N [Y=Yes, N=No]
  street nVarChar(100) Street
  city nVarChar(100) City
  country nVarChar(3) Country/Region ->OCRY
  state nVarChar(3) State ->OCST
  room nVarChar(50) Room
  parentType nVarChar(20) Parent Object Type [97=Opportunity, 191=Service Call]
  parentId Int(11) Parent Object ID
  prevActvty Int(11) Previous Activity
  AtcEntry Int(11) Attachment Entry
  RecurPat VarChar(1) Recurrence Pattern default=N [N=None, D=Daily, W=Weekly, M=Monthly, A=Annually]
  EndType VarChar(1) Recurrence End Type default=N [N=No End Date, C=By Counter, D=By Date]
  SeStartDat Date(8) Series Start Date
  SeEndDat Date(8) Series End Date
  MaxOccur Int(11) Max. Occurrences
  Interval Int(11) Interval default=1
  Sunday VarChar(1) Sunday default=N [N=No, Y=Yes]
  Monday VarChar(1) Monday default=N [N=No, Y=Yes]
  Tuesday VarChar(1) Tuesday default=N [N=No, Y=Yes]
  Wednesday VarChar(1) Wednesday default=N [N=No, Y=Yes]
  Thursday VarChar(1) Thursday default=N [N=No, Y=Yes]
  Friday VarChar(1) Friday default=N [N=No, Y=Yes]
  Saturday VarChar(1) Saturday default=N [N=No, Y=Yes]
  SubOption VarChar(1) Suboption default=1 [1=Option 1, 2=Option 2]
  DayInMonth Int(11) Repeat Day in Month
  Month Int(11) Repeat Month
  DayOfWeek Int(11) Repeat Day of Week
  Week Int(11) Repeat Week in Month [1=First, 2=Second, 3=Third, 4=Fourth, 5=Last]
  SeriesNum Int(11) Series Number
  OrigDate Date(8) Original Date
  IsRemoved VarChar(1) Removed Flag default=N [N=No, Y=Yes]
  LastRemind Date(8) Last Reminder Date
  AssignedBy Int(6) Assigned By ->OUSR
  AddrName nVarChar(50) Address Name
  AddrType VarChar(1) Address Type default=S [S=Ship To, B=Bill To]
  AttendEmpl Int(11) Dealt by Employee ->OHEM
  NextDate Date(8) Date of Next Occurrence
  NextTime Int(6) Time of Next Occurrence
  OwnerCode Int(11) Activities Owner ->OHEM
  AttendReci Int(11) Attend Recipient ->ORCI
  ActType Int(11) Activity Type ->PMC5
  LaborItem nVarChar(50) Labor Item No.
  ResCode nVarChar(50) Resource Code from ORSC ->ORSC
  FIPROJECT nVarChar(20) Financial Project ->OPRJ
  UpdateDate Date(8) Date of Update
  LogInstanc Int(11) Log Instance default=0
  UserSign2 Int(6) Updating User ->OUSR
  DPPStatus VarChar(1) Data Protection Status default=N [N=None, D=Erased]
  CreateDate Date(8) Creation Date
  EncryptIV nVarChar(100) Encrypt IV
  DataVers Int(11) Data Version default=1
  Of365EvtId nVarChar(200) Office 365 Event ID
  AssigneeTy Int(11) Assignee Type default=12 [12=User, 171=Employee, 234000033=Recipient List, -1=Multiple Recipients]
  VersionNum nVarChar(13) Version Number

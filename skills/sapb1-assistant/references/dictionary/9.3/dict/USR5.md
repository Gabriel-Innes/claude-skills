<!-- source: erpref.com (schema IP: SAP) | version: SAP Business One 9.3 | verified: 2026-10-01 -->
# USR5 - User Access Log
Module: Administration | 17 columns
Indexes (name: columns; first = primary key; U = unique) - WARNING: multi-column key order here is reversed vs SAP's 10.0 reference (read as a set; see references/dictionary/INDEX.md):
  PRIMARY U: SessionID, Time, Date, Action, UserCode
Fields (name type(len) description [values] ->parent table):
  UserCode nVarChar(25) User Code ->OUSR
  Action VarChar(1) Performed Action [I=Logon Succeeded, F=Logon Failed, O=Logoff, C=Created, S=Superuser Selected, D=Superuser Deselected, L=Locked, U=Unlocked, P=Password Changed, N=Screen Unlock Failed, T=Temporary User Change, R=Removed]
  ActionBy nVarChar(25) User Who Performed the Action
  ClientIP nVarChar(200) IP Address of Client Computer
  Date Date(8) Date
  Time Int(11) Time default=0
  ClientName nVarChar(32) Hostname of Client Computer
  ProcessID Int(11) Process ID of B1 Application default=-1
  SessionID Int(11) Connection Session ID default=-1
  ReasonID Int(11) Reason ID [1=Planned: Initial System Configuration, 2=Planned: System Configuration Change, 3=Planned: System Maintenance, 4=Planned: Knowledge Transfer to End-User, 11=Unplanned: Root Cause Analysis, 12=Unplanned: Knowledge Transfer to End-User, 13=Unplanned: System Maintenance, 14=Unplanned: System Configuration Change]
  ReasonDesc nVarChar(250) Reason Description
  WinSessnID Int(11) Client Windows Session ID default=-1
  WinUsrName nVarChar(100) User Name of Windows User
  ProcName nVarChar(80) Process Name of Logged-On App.
  AliveDurtn Int(11) Time Logged-On User Keep Alive default=0
  LogoutTime Int(11) User Logout Time
  Source nVarChar(100) Login Terminal

<!-- source: erpref.com (schema IP: SAP) | version: SAP Business One 9.3 | verified: 2026-10-01 -->
# OCPL - Quick Copy Log Manager
Module: Administration | 15 columns
Indexes (name: columns; first = primary key; U = unique) - WARNING: multi-column key order here is reversed vs SAP's 10.0 reference (read as a set; see references/dictionary/INDEX.md):
  PRIMARY U: AbsEntry
Fields (name type(len) description [values] ->parent table):
  AbsEntry Int(11) Internal Number
  StartDate Date(8) Start Date
  StartTime nVarChar(6) Start Time
  EndDate Date(8) End Date
  EndTime nVarChar(6) End Time
  CopySource nVarChar(254) Copy Source
  CopyTarget nVarChar(254) Copy Target
  UserName nVarChar(20) User Name
  CopyMethod Int(6) Copy Method [2=Delete All Records Then Add New Records, 4=Update Existing Records Without Adding New Records, 8=Add New Records Without Updating Existing Records, 16=Add New Records and Update Existing Records, 0=N/A]
  FailRpn Int(6) Copy failed [1=Ignore All Errors and Copy Valid Records, 2=Obtain User Confirmation, 3=Terminate Copy Process When One or More Errors Occur, 4=Terminate Copy Process When Number of Errors Exceeds]
  MissingUDF VarChar(1) UDF missing [2=N/A, 1=Copy Records and Ignore Missing UDFs, 0=Do Not Copy Records with Missing UDFs]
  CopyType Int(6) Copy Type
  ErrorNum nVarChar(11) Error Number
  NullifyAct Int(6) Nullify Account [2=N/A, 1=Use Default Accounts in Target, 0=Use Accounts in Source]
  CopyEmtVal Int(6) Copy Empty Value [2=N/A, 1=Do Not Overwrite Target Fields and Keep Original Values, 0=Overwrite Target Fields with Empty Values]

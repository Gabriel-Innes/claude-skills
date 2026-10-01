<!-- source: erpref.com (schema IP: SAP) | version: SAP Business One 9.3 | verified: 2026-10-01 -->
# OITR - Internal Reconciliation
Module: Banking | 30 columns | ObjType: 321
Indexes (name: columns; first = primary key; U = unique) - WARNING: multi-column key order here is reversed vs SAP's 10.0 reference (read as a set; see references/dictionary/INDEX.md):
  PRIMARY U: ReconNum
Fields (name type(len) description [values] ->parent table):
  ReconNum Int(11) Reconciliation Number
  IsCard VarChar(1) BP or Account [C=BP, A=G/L Account]
  ReconType nVarChar(2) Reconciliation Type [0=Manual, 1=Automatic, 2=Semi-Automatic, 3=Payment, 4=Credit Memo, 5=Reversal, 6=Zero Value, 7=Cancellation, 8=BoE, 9=Deposit, 10=Bank Statement Processing, 11=Period Closing, 12=Correction Invoice, 13=Inventory/Expense Allocation, 14=WIP, 15=Deferred Tax Interim Account, 16=Down Payment Allocation, 17=Auto. Conversion Difference, 18=Interim Document]
  ReconDate Date(8) Reconciliation Date
  Total Num(19,6) Total Reconciliation Amount
  ReconCurr nVarChar(3) Reconciliation Currency ->OCRN
  Canceled VarChar(1) Canceled default=N [Y=Yes, N=No]
  CancelAbs Int(11) Canceling/-ed Reconciliation default=0 ->OITR
  IsSystem VarChar(1) System or Manual [Y=Yes, N=No]
  InitObjTyp nVarChar(20) Reconc. Initiator Object Type
  InitObjAbs Int(11) Reconc. Initiator Internal ID
  CreateDate Date(8) Creation Date
  CreateTime Int(6) Creation Time
  DataSource VarChar(1) Data Source default=N [N=Unknown, I=Interface, U=Update, M=Import, O=OB Server, A=Auto Incr., D=Data Doc., P=Partner Implementation, T=Year Transfer]
  UserSign Int(6) User Signature ->OUSR
  ReconRule1 nVarChar(2) Reconciliation Rule 1 [0=Posting Date, 1=Due Date, 2=Document Date, 3=Ref. 1, 4=Ref. 2, 5=Ref. 3, 6=Project Code, 7=Control Account Code, 8=Posting Period]
  ReconRule2 nVarChar(2) Reconciliation Rule 2 [0=Posting Date, 1=Due Date, 2=Document Date, 3=Ref. 1, 4=Ref. 2, 5=Ref. 3, 6=Project Code, 7=Control Account Code, 8=Posting Period]
  ReconRule3 nVarChar(2) Reconciliation Rule 3 [0=Posting Date, 1=Due Date, 2=Document Date, 3=Ref. 1, 4=Ref. 2, 5=Ref. 3, 6=Project Code, 7=Control Account Code, 8=Posting Period]
  IsMultiBP VarChar(1) Multiple BP Reconciliation default=N [N=No, Y=Yes]
  VersionNum nVarChar(11) Version Number
  OldMatNum Int(11) Previous Reconciliation Number default=0
  ReconJEId Int(11) JE no. created by reconciliatn
  BuildDesc nVarChar(50) Build Descriptor
  BPLId Int(11) Branch ->OBPL
  BPLName nVarChar(100) Branch Name
  VATRegNum nVarChar(32) VAT Reg. Number
  IsElectr VarChar(1) Is Electronic default=N [N=No, Y=Yes]
  CreateTS Int(11) Creation Time - Incl. Sec.
  UpdateTS Int(11) Update Full Time
  ObjType nVarChar(20) Object Type default=321

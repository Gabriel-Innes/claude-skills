<!-- source: erpref.com (schema IP: SAP) | version: SAP Business One 9.3 | verified: 2026-10-01 -->
# OADP - Print Preferences
Module: Administration | 40 columns | ObjType: 32
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: PrintId
Fields (name type(len) description [values] ->parent table):
  PrintId nVarChar(4) Print Number
  ObjList Int(11) Object List default=13 [1470000049=Capitalization, 1470000071=Depreciation Run, 1470000090=Fixed Asset Transfer, 23=Sales Quotation, 17=Sales Order, 15=Delivery, 234000031=Return Request, 16=Returns, 203=A/R Down Payment, 13=A/R Invoice, 165=A/R Correction Invoice, 166=A/R Correction Invoice Reversal, 14=A/R Credit Memo, 1470000113=Purchase Request, 540000006=Purchase Quotation, 22=Purchase Order, 20=Goods Receipt PO, 234000032=Goods Return Request, 21=Goods Return, 204=A/P Down Payment, 18=A/P Invoice, 163=A/P Correction Invoice, 164=A/P Correction Invoice Reversal, 19=A/P Credit Memo, 69=Landed Costs, 24=Incoming Payment, 25=Deposit, 46=Outgoing Payment, 76=Postdated Deposit, 57=Check for Payment, 30=Journal Entry, 28=Journal Voucher, 140000010=Incoming Excise Invoice, 140000009=Outgoing Excise Invoice, 59=Goods Receipt, 60=Goods Issue, 1250000001=Inventory Transfer Request, 67=Inventory Transfer, 68=Work Instructions, 202=Production Order, 162=Inventory Revaluation, 156=Pick List, 1470000065=Inventory Counting, 10000071=Inventory Posting, 310000001=Inventory Opening Balances, 88=Entrada, 89=Salida, 90=Traspaso, 132=Correction Invoice, 234000021=Project Management Document]
  MaxLineNum Int(6) Max. Rows per Page default=99
  TopMrgn Int(6) Top Margin Width
  BtmMrgn Int(6) Bottom Margin Width
  LftMrgn Int(6) Left Margin Width
  RgtMrgn Int(6) Right Margin Width
  PrnCompany VarChar(1) Print on Company Paper default=N [Y=Yes, N=No]
  MnhlNote VarChar(1) Text Printed by PLD default=Y [Y=Yes, N=No]
  MaxWordLin Int(6) Max. Rows for Export default=10
  V_Compress Int(6) Compress Vertically default=100 [50=50, 60=60, 70=70, 80=80, 90=90, 100=100, 110=110, 120=120, 130=130, 140=140, 150=150]
  WordPath Text(16) WORD Template Path
  BitmapPath Text(16) Picture Path
  PrintMeta VarChar(1) Print as Picture default=N [Y=Yes, N=No]
  PrintRcpt VarChar(1) Print Receipt default=N [N=No, A=Only When Adding, Y=Always]
  ShortRcpt VarChar(1) Print Payment with Invoice default=N [Y=Yes, N=No]
  ExportCode VarChar(1) Export Material/Account Code default=N [Y=Yes, N=No]
  AttachPath Text(16) Attachments Path
  DraftNote VarChar(1) Print Draft Note default=Y [Y=Yes, N=No]
  ExtPath Text(16) Extensions Path
  DmePath Text(16) DME Files Store Path
  SNType Int(6) Serial Number Type default=2 [1=Mfr Serial No., 2=Serial No., 3=Lot Number]
  GBIPath Text(16) GB Data Interface Path
  LogoFile nVarChar(200) Logo File
  LogoImage Text(16) Logo Image
  B1Server Text(16) Business One Server Address
  IsTrustSrv VarChar(1) Always Trust This Server default=N [Y=Yes, N=No]
  LogInstanc Int(11) Log Instance default=0
  UpdateDate Date(8) Date of Update
  UserSign2 Int(6) Updating User ->OUSR
  SnapShotId Int(11) Snapshot ID default=0
  DefirExpP Text(16) Export Folder
  DefirDemop Text(16) DEFIR Database Path
  PrintPDF VarChar(1) Generate PDF When Printing default=N [Y=Yes, N=No]
  PrtCancel VarChar(1) Print Watermark on Cancl. Docs default=Y [Y=Yes, N=No]
  PrtUseSys VarChar(1) Use System Print Preferences default=N [Y=Yes, N=No]
  RptList nVarChar(20) Report List default=1 [1=Aging Report, 2=Dunning Wizard]
  PreAttach Text(16) Previous Attachment Path
  ExportPDF VarChar(1) Export PDF to Dflt Attachment default=N [Y=Yes, N=No]
  AttachPDF VarChar(1) Attach Exported PDF to Doc default=N [Y=Yes, N=No]

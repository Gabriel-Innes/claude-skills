<!-- source: erpref.com (schema IP: SAP) | version: SAP Business One 9.3 | verified: 2026-10-01 -->
# RIN9 - A/R Credit Memo - Drawn Dpm
Module: Marketing Documents | 27 columns
Indexes (name: columns; first = primary key; U = unique) - WARNING: multi-column key order here is reversed vs SAP's 10.0 reference (read as a set; see references/dictionary/INDEX.md):
  PRIMARY U: LineNum, DocEntry
Fields (name type(len) description [values] ->parent table):
  DocEntry Int(11) Document Internal ID ->ORIN
  LineNum Int(11) Row Number
  BaseAbs Int(11) Base Document Internal ID ->ODPI
  BaseLine Int(11) Base Document Row
  TargetBase VarChar(1) Target or Base Document default=B [B=Base, T=Target]
  ObjType nVarChar(20) Base Object Type
  DrawnSum Num(19,6) Net LC
  DrawnSumFc Num(19,6) Net FC
  DrawnSumSc Num(19,6) Net SC
  LogInstanc Int(11) Log Instance default=0
  ObjCode nVarChar(20) Object Type default=14 ->ADP1
  ApplDrawn Num(19,6) Applied Net LC
  ApplDrawnF Num(19,6) Applied Net FC
  ApplDrawnS Num(19,6) Applied Net SC
  BaseDocNum Int(11) Base Document Number
  BsDocDate Date(8) Base Posting Date
  BsDueDate Date(8) Base Due Date
  BsCardName nVarChar(100) Base BP Name
  BsComments nVarChar(254) Base Remarks
  Posted VarChar(1) Base Document Posted default=Y [Y=Yes, N=No]
  Vat Num(19,6) Tax LC
  VatFc Num(19,6) Tax FC
  VatSc Num(19,6) Tax SC
  Gross Num(19,6) Gross LC
  GrossFc Num(19,6) Gross FC
  GrossSc Num(19,6) Gross SC
  IsGross VarChar(1) Is Gross Line default=N [N=Net Line, Y=Gross Line]

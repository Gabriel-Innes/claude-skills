<!-- source: erpref.com (schema IP: SAP) | version: SAP Business One 9.3 | verified: 2026-10-01 -->
# OTPW - Tax Payment Wizard
Module: Banking | 17 columns
Indexes (name: columns; first = primary key; U = unique) - WARNING: multi-column key order here is reversed vs SAP's 10.0 reference (read as a set; see references/dictionary/INDEX.md):
  PRIMARY U: AbsEntry
  NAME U: WizName
Fields (name type(len) description [values] ->parent table):
  AbsEntry Int(11) Internal Key
  WizNumber Int(11) Wizard Number
  WizName nVarChar(50) Wizard Name
  WizStatus VarChar(1) Wizard Status default=S [S=Saved, E=Executed]
  CreateDate Date(8) Wizard Creation Date
  SaveDate Date(8) Wizard Save Date
  ExecDate Date(8) Wizard Execution Date
  UserSign Int(6) User Signature
  Series Int(11) Wizard Series
  JETransId Int(11) Journal Entry Number ->OJDT
  WizDate Date(8) Wizard Date
  RG23APart2 Int(11) RG23A Part 2
  RG23CPart2 Int(11) RG23C Part 2
  SeqCode Int(6) Sequence Code
  Serial Int(11) Serial Number
  SeriesStr nVarChar(3) Series String
  SubStr nVarChar(3) Subseries String

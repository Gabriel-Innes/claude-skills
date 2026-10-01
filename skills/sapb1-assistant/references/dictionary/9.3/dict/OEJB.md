<!-- source: erpref.com (schema IP: SAP) | version: SAP Business One 9.3 | verified: 2026-10-01 -->
# OEJB - Wizard Run Details for ERV-JAb
Module: Reports | 24 columns
Indexes (name: columns; first = primary key; U = unique) - WARNING: multi-column key order here is reversed vs SAP's 10.0 reference (read as a set; see references/dictionary/INDEX.md):
  PRIMARY U: WizardId
Fields (name type(len) description [values] ->parent table):
  WizardId Int(11) Wizard ID
  WizardName nVarChar(100) Wizard Name
  FromDate Date(8) From Date
  ToDate Date(8) To Date
  PFromDate Date(8) Previous Year From Date
  PToDate Date(8) Previous Year To Date
  DateOfRun Date(8) Date of Run
  Status VarChar(1) Status default=O [O=Open, C=Closed]
  ActYearCl VarChar(1) Classifictn in Actual Yr [S=Small, M=Medium, L=Large]
  FormFinSt Int(11) Form of Financial Statement default=0 [0=, 1=Small GmbH (UGB Form 2,3), 2=Small GmbH with Balance Sheet, 3=Medium Large GmbH, 4=AG (Eng. PLC)]
  EBSTmpl Int(11) E-Balance Sheet Template ->OFRT
  EPaLTmpl Int(11) E-P&L Template ->OFRT
  OverwrFinS VarChar(1) Overwrite Financial Statement default=N [Y=Yes, N=No]
  Reference nVarChar(25) Reference
  HBCode Int(11) House Bank Code ->DSC1
  PayRef nVarChar(12) Payment Reference
  SndrRole Int(11) Sender Role default=0 [0=, 1=1 - Sole Company Representative and Signatory, 2=2 - Sole Authorized Company Representative, 3=3 - One of Authorized Company Representatives]
  CRegNumber nVarChar(7) Commercial Register Number
  LFBSheetD nVarChar(3) Legal Form on Actl Bal Sht Dte [AG=Public Limited Company (AG), SC=European Cooperative Society (SCE), SE=Company under European Law (SE, Societa Europaea), GEN=Industrial Cooperative Society, GES=Limited Liability Company (GmbH), KG=Limited Partnership, OG=Open Company]
  LFBSheetPr nVarChar(3) Lgl Form on Bal Sht Dte Prv Yr [AG=Public Limited Company (AG), SC=European Cooperative Society (SCE), SE=Company under European Law (SE, Societa Europaea), GEN=Industrial Cooperative Society, GES=Limited Liability Company (GmbH), KG=Limited Partnership, OG=Open Company]
  RegNum nVarChar(7) Reg. No. of Partner Company
  CmpanyName Text(16) Company Name
  XMLFile Text(16) XML File Storage
  TimeOfRun Int(6) Time of Run

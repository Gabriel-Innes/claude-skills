<!-- source: REFDB.chm (SAP Business One SDK 10.0 - Database Tables Reference) | version: SAP Business One 10.0 | verified: 2026-10-01 -->
# EJB2 - Docs List for ERV-JAb Wizard
Module: Reports | 9 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: WizardID, DocID
Fields (name type(len) description [values] ->parent table):
  WizardID Int(11) Wizard ID ->OEJB
  DocID Int(11) Document ID
  Selected VarChar(1) Selected default=Y [Y=Yes, N=No]
  Mandatory VarChar(1) Mandatory default=N [Y=Yes, N=No]
  Type nVarChar(3) Type [XML=XML, PDF=PDF]
  RptSec Int(11) Report Section default=0 [0=, 1=General Information for ERV-JAb, 2=Names of Signatories:, 3=Legal Size Classification, 4=Extract from Balance Sheet (UGB Form 2), 5=Balance Sheet, 6=P&L Statement, 7=Annex To Be Published (UGB Form 3), 8=General and Other Explanations, 9=Annex to Balance Sheet Entry, 10=Annex to P&L Statement, 11=Annual Report, 12=Suggestion for Financial Statement Usage, 13=Decision About Financial Statement Usage, 14=Note of Confirmation, 15=Supervisory Board Report, 16=External Auditor Report Acc. to Art. 44 Para. 3 EStG (Income Tax Act), 17=Finance-Specific Annex, 18=Assets History Sheet, 19=Liabilities History Sheet]
  FilePath nVarChar(254) File Path
  FileStorag Text(16) File Storage
  VisOrder Int(11) Visual Order

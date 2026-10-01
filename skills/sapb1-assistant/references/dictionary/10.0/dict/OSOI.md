<!-- source: REFDB.chm (SAP Business One SDK 10.0 - Database Tables Reference) | version: SAP Business One 10.0 | verified: 2026-10-01 -->
# OSOI - Statement of Import Wizard
Module: Reports | 12 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: WizardId
Fields (name type(len) description [values] ->parent table):
  WizardId Int(11) Wizard ID
  Name nVarChar(100) Name
  Date Date(8) Run Date
  UserSign Int(6) User Signature
  AgrNoFrom Int(11) Agreement No. From
  AgrNoTo Int(11) Agreement No. To
  PDateFrm Date(8) Posting Date From
  PDateTo Date(8) Posting Date To
  OrigWizId Int(11) Original Wizard ID
  OrigSOINum Int(11) Original Statement No.
  Status VarChar(1) Status default=N [N=Created, C=Correction, U=Updated, D=Deleted]
  CorrType VarChar(1) Correction Type [R=Replacement, A=Adjustment]

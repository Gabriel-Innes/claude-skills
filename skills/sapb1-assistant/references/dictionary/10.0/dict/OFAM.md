<!-- source: REFDB.chm (SAP Business One SDK 10.0 - Database Tables Reference) | version: SAP Business One 10.0 | verified: 2026-10-01 -->
# OFAM - Fixed Asset Data Migration
Module: Finance | 13 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: WizardId
Fields (name type(len) description [values] ->parent table):
  WizardId Int(11) Wizard ID
  WizardName nVarChar(100) Migration Run Name
  CreateDate Date(8) Migration Run Date
  AcctDtn VarChar(1) Migrate Account Determination default=Y [Y=Yes, N=No]
  DprArea VarChar(1) Migrate Depreciation Areas default=Y [Y=Yes, N=No]
  DprType VarChar(1) Migrate Depreciation Types default=Y [Y=Yes, N=No]
  AssetClass VarChar(1) Migrate Asset Classes default=Y [Y=Yes, N=No]
  AssetNum VarChar(1) Migrate Asset Numbering default=Y [Y=Yes, N=No]
  AssetItem VarChar(1) Migrate Asset Items default=Y [Y=Yes, N=No]
  UpdExstItm VarChar(1) Overwrite Existing Data default=N [Y=Overwrite Existing Data, N=Skip if Data Already Exists]
  Status VarChar(1) Status of Migration Run default=S [S=Successful, P=Partially Successful, F=Failed]
  Remarks nVarChar(254) Remarks
  FiscalYear nVarChar(10) Migration Data to Fiscal Year

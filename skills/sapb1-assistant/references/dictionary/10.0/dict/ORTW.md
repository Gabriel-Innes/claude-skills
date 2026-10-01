<!-- source: REFDB.chm (SAP Business One SDK 10.0 - Database Tables Reference) | version: SAP Business One 10.0 | verified: 2026-10-01 -->
# ORTW - Boleto Retorno Wizard: Parameter Sets
Module: Banking | 13 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: AbsEntry
Fields (name type(len) description [values] ->parent table):
  AbsEntry Int(11) Internal Number
  WDueDtFrom Date(8) Due Date From
  WDueDtTo Date(8) Due Date To
  WImpFile Text(16) Import File
  WMatching Int(11) Boleto Matching
  WBoletosAu Int(11) Boletos Automatic Count
  WBoletosMn Int(11) Boletos Manual Count
  WBoletosNI Int(11) Boletos Not Identified Count
  WRelDate Date(8) Release Date
  WCollDisc Int(11) Collection or Discounted
  WBankAcc1 nVarChar(50) Bank Acct No. 1
  WBankAcc2 nVarChar(50) Bank Acct No. 2
  WFileForm2 nVarChar(50) File Format 2

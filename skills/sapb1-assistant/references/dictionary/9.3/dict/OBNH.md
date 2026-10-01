<!-- source: erpref.com (schema IP: SAP) | version: SAP Business One 9.3 | verified: 2026-10-01 -->
# OBNH - Bank Statement Header
Module: Banking | 16 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: IdNumber
  ACT_NUM_DT U: BSDate, BSNum, ActKey
Fields (name type(len) description [values] ->parent table):
  IdNumber Int(11) Internal Number
  ActKey Int(11) Bank Account Internal Number ->DSC1
  BSNum Int(11) Statement Internal Number
  BSDate Date(8) Statement Date
  Status VarChar(1) Status default=D [E=Finalized, D=Draft, O=Old]
  Imported VarChar(1) Imported From File default=Y [Y=Yes, N=No]
  StrtBlncF Num(19,6) Starting Balance (FC)
  EndBlncF Num(19,6) Ending Balance (FC)
  Currency nVarChar(3) Currency ->OCRN
  StrtBlncL Num(19,6) Starting Balance (LC)
  EndBlncL Num(19,6) Ending Balance (LC)
  FileCRC nVarChar(32) Bank Statement File Hash
  StmtGuid nVarChar(32) Bank Statement GUID
  BSFileNum nVarChar(50) Bank Statement Number
  PeriodAbs Int(11) Period Abs Entry
  DfltBPL Int(11) Default Branch

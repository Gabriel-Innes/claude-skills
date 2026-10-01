<!-- source: REFDB.chm (SAP Business One SDK 10.0 - Database Tables Reference) | version: SAP Business One 10.0 | verified: 2026-10-01 -->
# ISW2 - Intrastat Reported Items
Module: Finance | 19 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: WizAbsEnt, ItemCode
Fields (name type(len) description [values] ->parent table):
  WizAbsEnt Int(11) Wizard Run Key ->OISW
  ItemCode nVarChar(50) Item Code ->OITM
  CommCode nVarChar(12) Commodity Code
  SerCode nVarChar(12) Service Code
  AddMUnit nVarChar(50) Additional Measure Unit
  FactorAM Num(19,6) Factor Additional Measure
  OriRegSta nVarChar(12) Region of Origin (for Export)
  DstRegSta nVarChar(12) Destination Region (Import)
  CtryOrig nVarChar(3) Country/Region of Origin
  SerSupplM nVarChar(12) Service Supply Method default=I [I=Immediate, R=To More Resumptions]
  SerPymMeth nVarChar(12) Service Payment Method default=X [A=Accredited to Bank Account, B=Bank Transfer, X=Other]
  ItemType VarChar(1) Item Type default=I [I=Item, S=Service, N=Item not relevant to Intrastat]
  ItemName nVarChar(200) Item Name
  DestRegCry nVarChar(3) Destination Country - Region
  OrigRegCry nVarChar(3) Origin Region Country
  UseWeight VarChar(1) Use Wt in Add. Measure Calc. default=Y [Y=Yes, N=No]
  StatCode nVarChar(2) Statistical Code
  NatOfTrans nVarChar(50) Nature of Transaction
  StatProc nVarChar(50) Statistical Procedure

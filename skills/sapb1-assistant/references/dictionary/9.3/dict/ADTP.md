<!-- source: erpref.com (schema IP: SAP) | version: SAP Business One 9.3 | verified: 2026-10-01 -->
# ADTP - Fixed Assets Depreciation Types - History
Module: Finance | 50 columns
Indexes (name: columns; first = primary key; U = unique) - WARNING: multi-column key order here is reversed vs SAP's 10.0 reference (read as a set; see references/dictionary/INDEX.md):
  PRIMARY U: LogInstanc, Code
Fields (name type(len) description [values] ->parent table):
  Code nVarChar(15) Code
  Descr nVarChar(100) Description
  DprMeth nVarChar(2) Depreciation Method default=NO [NO=No Depreciation, SL=Straight Line, SP=Straight Line Period Control, DB=Declining Balance, ML=Multilevel, WO=Immediate Write-Off, SD=Special Depreciation, MD=Manual Depreciation, CF=Accelerated]
  DprTo Num(19,6) Minimum Depreciated Value
  Rounding VarChar(1) Round Year End Book Value default=Y [Y=Yes, N=No]
  InclSalv VarChar(1) Include Salvage Value in Depr. default=N [Y=Yes, N=No]
  SalvPerc Num(19,6) Percentage for Salvage Value
  PerAcq nVarChar(2) Period Control for Acquisition default=PR [PR=Pro Rata Temporis, HY=First Year Convention, 6M=Half Year, FY=Full Year]
  PerSubAcq nVarChar(2) Period Control Subacquisition default=PR [PR=Pro Rata Temporis, YR=Half Year Convention, FY=Full Year]
  PerRet nVarChar(2) Period Control for Retirement default=PR [PR=Pro Rata Temporis, YR=Half Year Convention, EL=After End of Useful Life]
  AcqPRTyp nVarChar(3) Type of PRT for Acquisition default=EDB [EDB=Exact Daily Base, FCP=First Day of Current Period, FNP=First Day of Next Period]
  SubPRTyp nVarChar(3) Type of PR for Subacquisition default=EDB [EDB=Exact Daily Base, FCP=First Day of Current Period, FNP=First Day of Next Period]
  RetPRTyp nVarChar(3) Type of PR for Retirement default=EDB [EDB=Exact Daily Base, LPP=Last Day of Prior Period, LCP=Last Day of Current Period]
  PerDpRev Num(19,6) Depreciation to Be Reversed %
  ValidFrom Date(8) Valid From default=19000101
  ValidTo Date(8) Valid To default=20991231
  sCalcMeth nVarChar(3) Calc. Method for Straight Line default=APC [APC=Acquisition Value/Total Useful Life, PRC=Percentage of Acquisition Value, NBV=Net Book Value/Remaining Life]
  sPercent Num(19,6) Percentage for Straight Line
  dBase nVarChar(3) Base for Declining Balance default=NBV [NBV=Net Book Value]
  dPercent Num(19,6) Percentage for Decl. Balance
  dFactor Num(19,6) Factor for Declining Balance default=1
  dAltDprTyp nVarChar(15) Auto. Change Depreciation Type ->ODTP
  maDecBase VarChar(1) Reduce Depreciation Base default=Y [Y=Yes, N=No]
  spMeth VarChar(1) Calc. Method for Special Depr. default=D [D=Additional, A=Alternative]
  spConcPer Int(11) Concession Period in Years
  spMaxPerc Num(19,6) Maximum Percentage
  spAdDpr nVarChar(15) Normal Depreciation ->ODTP
  spAlDpr nVarChar(15) Alternative Depreciation ->ODTP
  PoolID nVarChar(2) Depreciation Type Pool ID ->ODPP
  DataSource VarChar(1) Data Source default=N [N=Unknown, I=Interface, U=Update, M=Import, O=DI API, A=Doc. Generation Wizard, D=Restore Wizard, P=Partner Implementation, T=Year Transfer]
  UserSign Int(6) User Signature ->OUSR
  LogInstanc Int(11) Log Instance default=0
  CreateDate Date(8) Create Date
  UserSign2 Int(6) Updating User ->OUSR
  UpdateDate Date(8) Date of Update
  DprPer VarChar(1) Depreciation Periods default=S [S=Standard, I=Individual, U=Individual Usage]
  PerFactor Num(19,6) Period Factor default=1
  spMaxAmnt Num(19,6) Maximum Amount
  spMaxFlag VarChar(1) Max. [PercentageAmount] default=P [P=Percentage, A=Amount]
  CalcBase VarChar(1) Calculation Base default=Y [Y=Yearly, M=Monthly]
  DeprEndLFY VarChar(1) Depr. End at Last Full Year default=N [Y=Yes, N=No]
  AccuPriorP VarChar(1) Accu. Depr. of Prior Periods default=N [Y=Yes, N=No]
  DeltaCoeff Int(11) Delta Coefficient default=0
  MaxDepr Num(19,6) Maximum Depreciable Value
  FactorFFY VarChar(1) Factor Only Relevant to FFY default=N [Y=Yes, N=No]
  SnapshotId Int(11) Snapshot ID default=0
  PerTranSou nVarChar(2) Period Control Transfer Source default=PR [PR=Pro Rata Temporis, YR=Half Year Convention, FY=Full Year]
  PerTranTar nVarChar(2) Period Control Transfer Target default=PR [PR=Pro Rata Temporis, YR=Half Year Convention, EL=After End of Useful Life]
  TranSPRTyp nVarChar(3) Type of PR for Transfer Source default=EDB [EDB=Exact Daily Base, LPP=Last Day of Prior Period, LCP=Last Day of Current Period]
  TranTPRTyp nVarChar(3) Type of PR for Transfer Target default=EDB [EDB=Exact Daily Base, FCP=First Day of Current Period, FNP=First Day of Next Period]

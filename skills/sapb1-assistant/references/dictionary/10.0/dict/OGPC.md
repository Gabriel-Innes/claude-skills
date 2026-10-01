<!-- source: REFDB.chm (SAP Business One SDK 10.0 - Database Tables Reference) | version: SAP Business One 10.0 | verified: 2026-10-01 -->
# OGPC - Government Payment Code
Module: Administration | 6 columns | ObjType: 243000001
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: AbsId
  CODE U: Code
Fields (name type(len) description [values] ->parent table):
  AbsId Int(11) Internal Number
  Code nVarChar(6) Code
  Descr nVarChar(100) Description
  StateTax VarChar(1) Reporting by State default=N [Y=Yes, N=No]
  Prdcity VarChar(1) Periodicity default=M [M=Monthly, Q=Quarterly, H=Semimonthly, T=Every 10 Days]
  SPEDCtgory Int(11) SPED Category [1=ICMS, 2=ICMS-ST, 3=IPI, 4=ISS, 5=PIS, 6=COFINS, 7=PIS-ST, 8=COFINS-ST]

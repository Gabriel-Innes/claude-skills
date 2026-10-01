<!-- source: erpref.com (schema IP: SAP) | version: SAP Business One 9.3 | verified: 2026-10-01 -->
# OGPC - Government Payment Code
Module: Administration | 6 columns | ObjType: 243000001
Indexes (name: columns; first = primary key; U = unique) - WARNING: multi-column key order here is reversed vs SAP's 10.0 reference (read as a set; see references/dictionary/INDEX.md):
  PRIMARY U: AbsId
  CODE U: Code
Fields (name type(len) description [values] ->parent table):
  AbsId Int(11) Internal Number
  Code nVarChar(6) Code
  Descr nVarChar(100) Description
  StateTax VarChar(1) Reporting by State default=N [Y=Yes, N=No]
  Prdcity VarChar(1) Periodicity default=M [M=Monthly, Q=Quarterly, H=Semimonthly, T=Every 10 Days]
  SPEDCtgory Int(11) SPED Category [1=ICMS, 2=ICMS-ST, 3=IPI, 4=ISS, 5=PIS, 6=COFINS, 7=PIS-ST, 8=COFINS-ST]

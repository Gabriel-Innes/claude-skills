<!-- source: erpref.com (schema IP: SAP) | version: SAP Business One 9.3 | verified: 2026-10-01 -->
# OCDT - Credit Card Payment
Module: Administration | 23 columns | ObjType: 71
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: Code
Fields (name type(len) description [values] ->parent table):
  Code nVarChar(8) Credit Card Payment Code
  Name nVarChar(30) Credit Card Payment Name
  TERM_TYPE VarChar(1) Credit Card Payment Types default=F [D=By Dates, F=After Time Period]
  After_Days Int(6) Payment After Days
  After_Mnth Int(6) Payment After Months
  Day_From1 Int(6) From Day 1
  Day_To1 Int(6) To Day 1
  Pay_Day1 Int(6) Payment Date 1
  Pay_Month1 Int(6) No. of Months 1
  Day_From2 Int(6) From Day 2
  Day_To2 Int(6) To Day 2
  Pay_Day2 Int(6) Payment Date 2
  Pay_Month2 Int(6) No. of Months 2
  Day_From3 Int(6) From Day 3
  Day_To3 Int(6) To Day 3
  Pay_Day3 Int(6) Payment Date 3
  Pay_Month3 Int(6) No. of Months 3
  Day_From4 Int(6) From Day 4
  Day_To4 Int(6) To Day 4
  Pay_Day4 Int(6) Payment Date 4
  Pay_Month4 Int(6) No. of Months 4
  DataSource VarChar(1) Data Source default=N [N=Unknown, I=Interface, U=Update, M=Import, O=DI API, A=Doc. Generation Wizard, D=Restore Wizard, P=Partner Implementation, T=Year Transfer]
  UserSign Int(6) User Signature ->OUSR

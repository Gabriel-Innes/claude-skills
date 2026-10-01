<!-- source: erpref.com (schema IP: SAP) | version: SAP Business One 9.3 | verified: 2026-10-01 -->
# AIT13 - Asset Attributes
Module: Inventory and Production | 67 columns
Indexes (name: columns; first = primary key; U = unique) - WARNING: multi-column key order here is reversed vs SAP's 10.0 reference (read as a set; see references/dictionary/INDEX.md):
  PRIMARY U: LogInstanc, ItemCode
Fields (name type(len) description [values] ->parent table):
  ItemCode nVarChar(50) Item No. ->OITM
  AttriTxt1 nVarChar(100) Attribute 1
  AttriTxt2 nVarChar(100) Attribute 2
  AttriTxt3 nVarChar(100) Attribute 3
  AttriTxt4 nVarChar(100) Attribute 4
  AttriTxt5 nVarChar(100) Attribute 5
  AttriTxt6 nVarChar(100) Attribute 6
  AttriTxt7 nVarChar(100) Attribute 7
  AttriTxt8 nVarChar(100) Attribute 8
  AttriTxt9 nVarChar(100) Attribute 9
  AttriTxt10 nVarChar(100) Attribute 10
  AttriTxt11 nVarChar(100) Attribute 11
  AttriTxt12 nVarChar(100) Attribute 12
  AttriTxt13 nVarChar(100) Attribute 13
  AttriTxt14 nVarChar(100) Attribute 14
  AttriTxt15 nVarChar(100) Attribute 15
  AttriTxt16 nVarChar(100) Attribute 16
  AttriTxt17 nVarChar(100) Attribute 17
  AttriTxt18 nVarChar(100) Attribute 18
  AttriTxt19 nVarChar(100) Attribute 19
  AttriTxt20 nVarChar(100) Attribute 20
  AttriTxt21 nVarChar(100) Attribute 21
  AttriTxt22 nVarChar(100) Attribute 22
  AttriTxt23 nVarChar(100) Attribute 23
  AttriTxt24 nVarChar(100) Attribute 24
  AttriTxt25 nVarChar(100) Attribute 25
  AttriTxt26 nVarChar(100) Attribute 26
  AttriTxt27 nVarChar(100) Attribute 27
  AttriTxt28 nVarChar(100) Attribute 28
  AttriTxt29 nVarChar(100) Attribute 29
  AttriTxt30 nVarChar(100) Attribute 30
  AttriTxt31 nVarChar(100) Attribute 31
  AttriTxt32 nVarChar(100) Attribute 32
  AttriInt33 Int(11) Attribute 33
  AttriInt34 Int(11) Attribute 34
  AttriInt35 Int(11) Attribute 35
  AttriInt36 Int(11) Attribute 36
  AttriInt37 Int(11) Attribute 37
  AttriInt38 Int(11) Attribute 38
  AttriInt39 Int(11) Attribute 39
  AttriInt40 Int(11) Attribute 40
  AttriInt41 Int(11) Attribute 41
  AttriInt42 Int(11) Attribute 42
  AttriDt43 Date(8) Attribute 43
  AttriDt44 Date(8) Attribute 44
  AttriDt45 Date(8) Attribute 45
  AttriDt46 Date(8) Attribute 46
  AttriDt47 Date(8) Attribute 47
  AttriAm48 Num(19,6) Attribute 48
  AttriAm49 Num(19,6) Attribute 49
  AttriAm50 Num(19,6) Attribute 50
  AttriAm51 Num(19,6) Attribute 51
  AttriAm52 Num(19,6) Attribute 52
  AttriAm53 Num(19,6) Attribute 53
  AttriAm54 Num(19,6) Attribute 54
  AttriPr55 Num(19,6) Attribute 55
  AttriPr56 Num(19,6) Attribute 56
  AttriPr57 Num(19,6) Attribute 57
  AttriPr58 Num(19,6) Attribute 58
  AttriPr59 Num(19,6) Attribute 59
  AttriQTY60 Num(19,6) Attribute 60
  AttriQTY61 Num(19,6) Attribute 61
  AttriQTY62 Num(19,6) Attribute 62
  AttriQTY63 Num(19,6) Attribute 63
  AttriQTY64 Num(19,6) Attribute 64
  LogInstanc Int(11) Log Instance default=0
  ObjType nVarChar(20) Object default=4 ->ADP1

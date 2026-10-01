<!-- source: erpref.com (schema IP: SAP) | version: SAP Business One 9.3 | verified: 2026-10-01 -->
# MAP1 - Input and Output of Mapping
Module: Administration | 8 columns
Indexes (name: columns; first = primary key; U = unique) - WARNING: multi-column key order here is reversed vs SAP's 10.0 reference (read as a set; see references/dictionary/INDEX.md):
  PRIMARY U: Code, MapID
Fields (name type(len) description [values] ->parent table):
  MapID Int(11) Mapping ID ->OMAP
  Code Int(11) Code
  Type nVarChar(10) Type default=NA [CRYSTAL=Crystal Report, XML=XML File, NA=Not Avalible, TXT=Text File, CSV=CSV File]
  RuleType nVarChar(10) Rule Type default=NA [XSLT=XSLT Rule, NA=Not Avalible, REGEX=Reguler expression]
  RuleRef nVarChar(50) Rule Reference ID
  RefID nVarChar(50) Reference ID
  RuleVer nVarChar(5) Rule Version
  IsFinal VarChar(1) Is Final Result default=N [Y=Yes, N=No]

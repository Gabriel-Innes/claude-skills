<!-- source: erpref.com (schema IP: SAP) | version: SAP Business One 9.3 | verified: 2026-10-01 -->
# OPTI - Point of Issue
Module: General | 9 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: Code
Fields (name type(len) description [values] ->parent table):
  Code nVarChar(5) Code
  Desc nVarChar(100) Description
  Type VarChar(1) Type default=P [P=Domestic Printing, E=Domestic Electronic, F=Fiscal, X=Export Printing, T=Export Electronic]
  SOpDate Date(8) Start Operating Date
  EndOpDate Date(8) End Operating Date
  Remarks nVarChar(100) Remarks
  EDocExpFrm Int(11) Electronic Doc. Export Format
  BPLId Int(11) Branch ->OBPL
  EDocGenTyp VarChar(1) Electronic Doc. Generation Type [N=Not Relevant, G=Generate]

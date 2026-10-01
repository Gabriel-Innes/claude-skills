<!-- source: erpref.com (schema IP: SAP) | version: SAP Business One 9.3 | verified: 2026-10-01 -->
# OCSQ - Column Sequences
Module: Administration | 6 columns
Indexes (name: columns; first = primary key; U = unique) - WARNING: multi-column key order here is reversed vs SAP's 10.0 reference (read as a set; see references/dictionary/INDEX.md):
  PRIMARY U: AbsId
Fields (name type(len) description [values] ->parent table):
  AbsId Int(11) Numerator
  SeqType nVarChar(8) Sequence Type
  FormID nVarChar(20) Form ID
  ColToken nVarChar(20) Column Token
  VisualIndx Int(11) Tabs Layout
  VisInForm VarChar(1) Visible in Form default=N [Y=, N=]

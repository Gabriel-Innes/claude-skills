<!-- source: erpref.com (schema IP: SAP) | version: SAP Business One 9.3 | verified: 2026-10-01 -->
# SRA2 - Scheduled Report Run Output
Module: Reports | 13 columns
Indexes (name: columns; first = primary key; U = unique) - WARNING: multi-column key order here is reversed vs SAP's 10.0 reference (read as a set; see references/dictionary/INDEX.md):
  PRIMARY U: Time, Date, ActionCode
  ACTIONCODE: ActionCode
Fields (name type(len) description [values] ->parent table):
  ActionCode Int(11) Action Code
  Date Date(8) Date of Run
  Time Int(11) Time of Run
  Status VarChar(1) Status default=0 [S=Successful, E=In progress, F=Failure, T=Results to Be Distributed, 0=Schedule Inactive, 1=Report Scheduled]
  ReturnCode Int(11) Return Code
  ReturnStr nVarChar(250) Return String
  ResDag Text(16) Result in DAG format
  ResPdf Text(16) Result in PDF format
  ResHtml Text(16) Result in HTML format
  ResXml Text(16) Result in XML format
  Results nVarChar(10) Result Availability default=NNNN
  ResLog Text(16) Report Creation Log
  ErrScreen Text(16) Error Screenshot

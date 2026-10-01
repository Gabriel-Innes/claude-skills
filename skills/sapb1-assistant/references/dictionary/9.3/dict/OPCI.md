<!-- source: erpref.com (schema IP: SAP) | version: SAP Business One 9.3 | verified: 2026-10-01 -->
# OPCI - Process Checklist Instance
Module: Administration | 12 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: InstancePk
Fields (name type(len) description [values] ->parent table):
  InstancePk Int(11) Instance Primary Key
  TemplateFk Int(11) Template Foreign Key ->OPCT
  InstName nVarChar(100) Instance Name
  InstDesc nVarChar(100) Instance Description
  Creator nVarChar(100) Instance Creator
  Status VarChar(1) Instance Status default=N [N=New, P=In Process, F=Finished]
  StartDate Date(8) Start Date
  CloseDate Date(8) Close Date
  CloPrcnt Num(19,6) Closing Percentage
  Memo Text(16) Remarks
  Attachment Text(16) Attachment
  AtcEntry Int(11) Attachment Entry

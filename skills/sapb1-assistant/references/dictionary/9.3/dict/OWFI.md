<!-- source: erpref.com (schema IP: SAP) | version: SAP Business One 9.3 | verified: 2026-10-01 -->
# OWFI - Workflow - Instances
Module: Administration | 10 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: WFInstID
Fields (name type(len) description [values] ->parent table):
  WFInstID Identity(11) WF Instance ID
  ExecID Int(11) WF Instance on Engine
  TemplateID Int(11) WF Template ID
  Creator nVarChar(25) Creator
  Status nVarChar(8) Status [S=Setup, F=Completed, G=In Progress, C=Cancelling, Q=Canceled, E=Error]
  StartDate Date(8) Start Date
  StartTime Int(6) Start Time
  EndTime Int(6) End Time
  EndDate Date(8) End Date
  IsAutoStar Int(6) Is auto start instance

<!-- source: erpref.com (schema IP: SAP) | version: SAP Business One 9.3 | verified: 2026-10-01 -->
# OSHR - Shareholder's Rights and Interests Report History
Module: Finance | 8 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: Id
Fields (name type(len) description [values] ->parent table):
  Id Int(11) Identity
  Name nVarChar(40) Report Name
  UserSign Int(6) Creater's code
  UserName nVarChar(20) Name of Creator
  CreateDate Date(8) Report Created on
  StartDate Date(8) Date Range Start
  EndDate Date(8) Date Range End
  TemplateId Int(11) Template ID

<!-- source: erpref.com (schema IP: SAP) | version: SAP Business One 9.3 | verified: 2026-10-01 -->
# OISR - Service Calls
Module: Service | 10 columns | ObjType: 105
Indexes (name: columns; first = primary key; U = unique) - WARNING: multi-column key order here is reversed vs SAP's 10.0 reference (read as a set; see references/dictionary/INDEX.md):
  PRIMARY U: RequestNum
Fields (name type(len) description [values] ->parent table):
  RequestNum Int(11) Request No.
  Open_Date Date(8) Start Date
  Open_Time Int(11) Start Time
  Task_Id Int(11) Request No. in SAP Business One
  Contact nVarChar(30) Contact Person
  Phone nVarChar(20) Telephone
  TaskType Int(6) Request Type default=0 [0=Explanation, 1=Error, 2=Complaints]
  Dscription nVarChar(254) Call Description
  Answer Text(16) Troubleshooting
  Status VarChar(1) Call Status default=O [O=Open, C=Closed]

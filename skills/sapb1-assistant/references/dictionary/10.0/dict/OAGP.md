<!-- source: REFDB.chm (SAP Business One SDK 10.0 - Database Tables Reference) | version: SAP Business One 10.0 | verified: 2026-10-01 -->
# OAGP - Agent Name
Module: Service | 6 columns | ObjType: 177
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: AgentCode
  AGENT_NAME U: AgentName
Fields (name type(len) description [values] ->parent table):
  AgentCode nVarChar(32) Agents
  AgentName nVarChar(50) Agent Name
  Memo nVarChar(50) Description
  Locked VarChar(1) Locked
  DataSource VarChar(1) Data Source default=N [N=Unknown, I=Interface, U=Update, M=Import, O=DI API, S=Service Layer, W=Web Client, A=Doc. Generation Wizard, D=Restore Wizard, P=Partner Implementation, T=Year Transfer]
  UserSign Int(6) User Signature ->OUSR

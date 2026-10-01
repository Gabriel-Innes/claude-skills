<!-- source: erpref.com (schema IP: SAP) | version: SAP Business One 9.3 | verified: 2026-10-01 -->
# OAGP - Agent Name
Module: Service | 6 columns | ObjType: 177
Indexes (name: columns; first = primary key; U = unique) - WARNING: multi-column key order here is reversed vs SAP's 10.0 reference (read as a set; see references/dictionary/INDEX.md):
  PRIMARY U: AgentCode
  AGENT_NAME U: AgentName
Fields (name type(len) description [values] ->parent table):
  AgentCode nVarChar(32) Agents
  AgentName nVarChar(50) Agent Name
  Memo nVarChar(50) Description
  Locked VarChar(1) Locked
  DataSource VarChar(1) Data Source default=N [N=Unknown, I=Interface, U=Update, M=Import, O=DI API, A=Doc. Generation Wizard, D=Restore Wizard, P=Partner Implementation, T=Year Transfer]
  UserSign Int(6) User Signature ->OUSR

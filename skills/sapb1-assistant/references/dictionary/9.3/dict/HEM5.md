<!-- source: erpref.com (schema IP: SAP) | version: SAP Business One 9.3 | verified: 2026-10-01 -->
# HEM5 - Employee Data Ownership Authorization
Module: Human Resources | 10 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: Object, empID
Fields (name type(len) description [values] ->parent table):
  empID Int(11) Employee No. ->OHEM
  Object nVarChar(20) The Object Number
  Peer VarChar(1) Peer Authorization default=N [F=Full, R=Read Only, N=None, U=Undefined Type]
  Manager VarChar(1) Manager Authorization default=N [F=Full, R=Read Only, N=None, U=Undefined Type, =]
  Subord VarChar(1) Subordinate Authorization default=N [F=Full, R=Read Only, N=None, U=Undefined Type, =]
  Dept VarChar(1) Department Authorization default=N [F=Full, R=Read Only, N=None, U=Undefined Type, =]
  Branch VarChar(1) Branch Authorization default=N [F=Full, R=Read Only, N=None, U=Undefined Type, =]
  Team VarChar(1) Team Authorization default=N [F=Full, R=Read Only, N=None, U=Undefined Type, =]
  AC Int(11) Cache Access Counter default=0
  Cmpny VarChar(1) Company Authorization default=N [F=Full, R=Read Only, N=None, U=Undefined Type]

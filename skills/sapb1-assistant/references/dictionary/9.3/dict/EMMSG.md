<!-- source: erpref.com (schema IP: SAP) | version: SAP Business One 9.3 | verified: 2026-10-01 -->
# EMMSG - EMMSG
Module: General | 10 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: ID
Fields (name type(len) description [values] ->parent table):
  ID nVarChar(60) Message ID
  Service nVarChar(160) Service
  Operation nVarChar(60) Operation
  Sender nVarChar(50) Sender ID
  Receiver nVarChar(50) Receiver ID
  InOut nVarChar(10) Incoming outgoing indicator
  BOType nVarChar(100) Business object type
  BOID nVarChar(30) Business object ID
  SboBoType nVarChar(100) Business one object type
  SboBoID nVarChar(30) Business one object ID

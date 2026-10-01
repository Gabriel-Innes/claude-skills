<!-- source: erpref.com (schema IP: SAP) | version: SAP Business One 9.3 | verified: 2026-10-01 -->
# PCI1 - Process Checklist Element Extended Data
Module: Administration | 7 columns
Indexes (name: columns; first = primary key; U = unique) - WARNING: multi-column key order here is reversed vs SAP's 10.0 reference (read as a set; see references/dictionary/INDEX.md):
  PRIMARY U: LineNum, InstancePk
Fields (name type(len) description [values] ->parent table):
  InstancePk Int(11) Instance Primary Key ->OPCI
  LineNum Int(11) Line Number
  BPMNElId nVarChar(254) BPMN Model Element ID
  BPMNElDes nVarChar(254) BPMN Model Element Description
  ParamType nVarChar(254) Parameter Type
  ParamKey nVarChar(254) Parameter Key
  ParamVal nVarChar(254) Parameter Value

<!-- source: erpref.com (schema IP: SAP) | version: SAP Business One 9.3 | verified: 2026-10-01 -->
# WMNU - WMNU
Module: General | 19 columns
Indexes (name: columns; first = primary key; U = unique) - WARNING: multi-column key order here is reversed vs SAP's 10.0 reference (read as a set; see references/dictionary/INDEX.md):
  PRIMARY U: ObjCode
Fields (name type(len) description [values] ->parent table):
  ObjCode Int(11) Object Code
  ObjName nVarChar(20) Object Name
  FatherID Int(11) Father Menu ID
  BrothetID Int(11) Older Brother Menu ID
  KeyNum nVarChar(100) m_KeyNum
  ExCommand nVarChar(100) m_exCommand
  Params nVarChar(100) m_params
  ParamsEx nVarChar(100) m_paramsEx
  MatchFlag nVarChar(100) m_matchFlag
  Dag nVarChar(100) m_dag
  Form nVarChar(100) m_form
  RetProc nVarChar(100) m_paRetProc
  InitMode nVarChar(100) m_initialMode
  Message nVarChar(100) m_message
  KeyStr nVarChar(100) m_keyStr
  SubType nVarChar(100) m_subType
  Condition nVarChar(254) local setting condition
  FormProc nVarChar(100) Draw Form Proc
  StrList Int(11) StrList Num

<!-- source: erpref.com (schema IP: SAP) | version: SAP Business One 9.3 | verified: 2026-10-01 -->
# RHKY - Hotkeys
Module: General | 5 columns
Indexes (name: columns; first = primary key; U = unique) - WARNING: multi-column key order here is reversed vs SAP's 10.0 reference (read as a set; see references/dictionary/INDEX.md):
  PRIMARY U: Num, Language
  ITEM U: ItemNum, FormName, Language
Fields (name type(len) description [values] ->parent table):
  Language Int(11) Language code
  Num Int(11) Hotkey Number
  FormName nVarChar(64) Form name
  ItemNum Int(11) Item number
  HkeyIndex Int(11) Hotkey Index in String

<!-- source: erpref.com (schema IP: SAP) | version: SAP Business One 9.3 | verified: 2026-10-01 -->
# RLNG - ????
Module: General | 14 columns
Indexes (name: columns; first = primary key; U = unique) - WARNING: multi-column key order here is reversed vs SAP's 10.0 reference (read as a set; see references/dictionary/INDEX.md):
  PRIMARY U: Code
  BASE: IsBase
  SHORT_NAME U: ShortName
Fields (name type(len) description [values] ->parent table):
  Created Date(8) Creation date
  Updated Date(8) Update date
  Code Int(11) Language code
  Name nVarChar(50) Language name
  ShortName nVarChar(4) Short name
  Direction VarChar(1) Direction default=1 [0=Right to left, 1=Left to right]
  IsBase VarChar(1) Is base default=0 [0=No, 1=Yes]
  Charset Int(11) Charset
  CodePage Int(11) Codepage
  KBLayout Int(11) Keyboard layout
  LangStr nVarChar(50) Language String
  TransInB5I VarChar(1) Translated In B5I System default=0
  HelpLang nVarChar(4) Online Help Language Code
  hasHotKey VarChar(1) The language has hot key default=Y [Y=Has HotKey, N=Does not have HotKey]

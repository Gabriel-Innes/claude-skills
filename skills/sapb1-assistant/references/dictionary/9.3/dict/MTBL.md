<!-- source: erpref.com (schema IP: SAP) | version: SAP Business One 9.3 | verified: 2026-10-01 -->
# MTBL - MetaData Tables
Module: General | 12 columns
Indexes (name: columns; first = primary key; U = unique) - WARNING: multi-column key order here is reversed vs SAP's 10.0 reference (read as a set; see references/dictionary/INDEX.md):
  PRIMARY U: RevCode, ResCode, Name
Fields (name type(len) description [values] ->parent table):
  Name nVarChar(5) Table Name
  ViewOrder Int(6) View Order default=30 [-1=Invisible, 10=Administration, 20=Administration Plus, 30=Master Data, 40=Document Line, 50=Document, 60=Log File, 70=Payment Line, 80=Payments]
  Type Int(6) Table Type default=1 [1=User OM, 2=User, 3=System OM, 4=System]
  Descr nVarChar(254) Description
  Category Int(6) Category default=0
  SubCateg Int(6) Sub Category default=0
  Dirty VarChar(1) Dirty default=Y [Y=Yes, N=No]
  Created Date(8) Creation Date
  Updated Date(8) Update Date
  InfoCtgory Int(6) Information Category default=0
  ResCode Int(11) Resource Code from RSBD default=-1
  RevCode Int(11) Revision Code default=-1

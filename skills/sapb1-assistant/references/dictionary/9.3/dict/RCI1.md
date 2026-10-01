<!-- source: erpref.com (schema IP: SAP) | version: SAP Business One 9.3 | verified: 2026-10-01 -->
# RCI1 - Recipient List - Rows
Module: Finance | 4 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: LineNum, Code
Fields (name type(len) description [values] ->parent table):
  Code Int(11) Code ->ORCI
  LineNum Int(11) Addressee Number
  ObjType nVarChar(20) Object [12=User, 171=Employee]
  ObjCode nVarChar(50) Object Code

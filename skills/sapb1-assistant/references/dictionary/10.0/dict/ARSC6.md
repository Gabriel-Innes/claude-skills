<!-- source: REFDB.chm (SAP Business One SDK 10.0 - Database Tables Reference) | version: SAP Business One 10.0 | verified: 2026-10-01 -->
# ARSC6 - Resources - Daily Capacities - Log
Module: General | 10 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: ResCode, WeekDay, LogInstanc
Fields (name type(len) description [values] ->parent table):
  ResCode nVarChar(50) Internal Resource ID ->ORSC
  WeekDay Int(11) Weekday No. [1=First Day of Week, 2=Second Day of Week, 3=Third Day of Week, 4=Fourth Day of Week, 5=Fifth Day of Week, 6=Sixth Day of Week, 7=Seventh Day of Week]
  CapFactor1 Num(19,6) Day 1 Capacity Factor 1
  CapFactor2 Num(19,6) Day 1 Capacity Factor 2
  CapFactor3 Num(19,6) Day 1 Capacity Factor 3
  CapFactor4 Num(19,6) Day 1 Capacity Factor 4
  CapTotal Num(19,6) Total Daily Capacity
  Remarks nVarChar(100) Remarks
  LogInstanc Int(11) Log Instance default=0
  SngRunCap Num(19,6) Single Run Capacity

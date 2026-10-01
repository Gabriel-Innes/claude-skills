<!-- source: REFDB.chm (SAP Business One SDK 10.0 - Database Tables Reference) | version: SAP Business One 10.0 | verified: 2026-10-01 -->
# WVT8 - Variant -- Mchart
Module: General | 10 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: ParentId, Guid
Fields (name type(len) description [values] ->parent table):
  ParentId nVarChar(40) Parent Id
  Guid nVarChar(40) Guid
  ChartType nVarChar(50) Chart Type
  ShowLegend VarChar(1) Show Legend default=N [Y=Yes, N=No]
  CtgrAxis1 nVarChar(254) Category axis 1
  CtgrAxis2 nVarChar(254) Category axis 2
  TimeAxis nVarChar(254) Time Axis
  Color nVarChar(254) Color
  Shape nVarChar(254) Shape
  BblWidth nVarChar(254) Bubble Width

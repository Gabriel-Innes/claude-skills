<!-- source: erpref.com (schema IP: SAP) | version: SAP Business One 9.3 | verified: 2026-10-01 -->
# OMSN - MRP Scenarios
Module: MRP | 57 columns | ObjType: 199
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: AbsEntry
  MSN_CODE U: MsnCode
Fields (name type(len) description [values] ->parent table):
  AbsEntry Int(11) Internal Number
  MsnCode nVarChar(30) MRP Scenario Code
  Descr nVarChar(100) Description
  GrpPeriods VarChar(1) Group Data into Periods of default=D [D=Days, W=Weeks, M=Months]
  PeriodsLen Int(11) Group Data into Periods of default=1
  StartDate Date(8) Report Start Date
  EndDate Date(8) Report End Date
  MaxLdTime Int(11) Maximum Cumulative Lead Time
  HldaysProd VarChar(1) Holidays for Production default=Y [Y=Yes, N=No]
  HldaysPurc VarChar(1) Holidays for Purchase default=Y [Y=Yes, N=No]
  ItmFrom nVarChar(50) Items Codes From ->OITM
  ItmTo nVarChar(50) Items Codes To ->OITM
  ItmGrp Int(11) Items Groups ->OITB
  ItmQryGrp nVarChar(250) Item Summary Report Group
  ExistStock VarChar(1) Consider Existing Inventory default=Y [Y=Yes, N=No]
  PurchOrder VarChar(1) Consider Purchase Orders default=Y [Y=Yes, N=No]
  SalesOrder VarChar(1) Consider Sales Orders default=Y [Y=Yes, N=No]
  WorkOrder VarChar(1) Consider Work Orders default=Y [Y=Yes, N=No]
  MinStckLvl VarChar(1) Minimum Inventory Level default=N [Y=Yes, N=No]
  FCTAbs Int(11) Forecast Absolute Entry ->OFCT
  SortBy VarChar(1) Sort By default=L [L=Assembly Sequence, C=Item Number, N=Item Description, G=Item Group]
  ItmReq VarChar(1) Items Without Requirement default=N [Y=Yes, N=No]
  Simulation VarChar(1) Is Scenario a Simulation default=N [Y=Yes, N=No]
  UpdateDate Date(8) Update Date
  UpdateBy nVarChar(20) Update By
  LastExecDa Date(8) Last Execute Date
  AllItems VarChar(1) All Items default=Y
  ByCompany VarChar(1) By Company default=Y
  IncHisData VarChar(1) Include Historical Data default=N [Y=Yes, N=No]
  ResInv VarChar(1) Reserve Invoice default=N [Y=Yes, N=No]
  Wtrq VarChar(1) Inventory Transfer Request default=N [Y=Yes, N=No]
  InvtLevel VarChar(1) Inventory Level default=D [D=, R=Required, I=Minimum, A=Maximum, M=Minimum - Maximum]
  RcmPO VarChar(1) Recommend Purchase Order default=N [Y=Yes, N=No]
  RcmWO VarChar(1) Recommend Production Order default=Y [Y=Yes, N=No]
  RcmWTRQ VarChar(1) Recommend ITRQ default=N [Y=Yes, N=No]
  RCMDefWhs VarChar(1) Recommend to Default Warehouse default=Y [Y=Yes, N=No]
  OnlyNettbl VarChar(1) Only Nettable default=Y [Y=Yes, N=No]
  ExpandedPO VarChar(1) Expanded Purchase Order default=N
  ExpandedSO VarChar(1) Expanded Sales Order default=N [Y=Yes, N=No]
  RcmCalDate Date(8) Recommendation Calculated Date
  RcmCalTime Int(11) Recommendation Calculated Time
  PurchOAT VarChar(1) Blanket Purchase Agreement default=Y [Y=Yes, N=No]
  SalesOAT VarChar(1) Blanket Sales Agreement default=Y
  Rots VarChar(1) Recurring Order Transactions default=N [Y=Yes, N=No]
  ExpdResINV VarChar(1) Expanded Reserve Invoice default=N
  ExpdWOR VarChar(1) Expanded Production Order default=N [Y=Yes, N=No]
  IgnoreCLT VarChar(1) Ignore Cumulative Lead Time default=N [Y=Yes, N=No]
  PurchReq VarChar(1) Consider Purchase Request default=N [Y=Yes, N=No]
  PurchQuota VarChar(1) Consider Purchase Quotations default=N [Y=Yes, N=No]
  SalesQuota VarChar(1) Consider Sales Quotations default=N [Y=Yes, N=No]
  ExpdPurReq VarChar(1) Expanded Purchase Request default=N [Y=Yes, N=No]
  ExpdPQuota VarChar(1) Expanded Purchase Quotations default=N [Y=Yes, N=No]
  ExpdSQuota VarChar(1) Expanded Sales Quotations default=N [Y=Yes, N=No]
  ExpdPAgree VarChar(1) Expanded Purchase Agreements default=N [Y=Yes, N=No]
  ExpdSAgree VarChar(1) Expanded Sales Agreements default=N [Y=Yes, N=No]
  ExpdTraReq VarChar(1) Expanded Transfer Request default=N [Y=Yes, N=No]
  DisSelItem VarChar(1) Display Selected Item Only default=N [Y=Yes, N=No]

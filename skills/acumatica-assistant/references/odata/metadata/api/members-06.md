<!-- source: DAC-based OData $metadata of a clean Acumatica ERP instance (GET <instance URL>/t/<TenantName>/api/odata/dac/$metadata) | version: Acumatica ERP 2026 R2 | verified: 2026-10-06 -->

# PX.Objects.SO.SOLine2 (EntityType)

Key: LineNbr, OrderNbr, OrderType
Entity sets: PX_Objects_SO_SOLine2
Non-filterable, non-selectable: CuryID, CuryRate, CuryViewState

PX.Objects.SO.SOLine2.OrderType : Edm.String [key]
PX.Objects.SO.SOLine2.Behavior : Edm.String
PX.Objects.SO.SOLine2.OrderNbr : Edm.String [key]
PX.Objects.SO.SOLine2.LineNbr : Edm.Int32 [key]
PX.Objects.SO.SOLine2.SortOrder : Edm.Int32
PX.Objects.SO.SOLine2.LineType : Edm.String
PX.Objects.SO.SOLine2.Operation : Edm.String "Operation"
PX.Objects.SO.SOLine2.LineSign : Edm.Int16
PX.Objects.SO.SOLine2.ShipComplete : Edm.String
PX.Objects.SO.SOLine2.Completed : Edm.Boolean
PX.Objects.SO.SOLine2.InventoryID : Edm.Int32
PX.Objects.SO.SOLine2.SubItemID : Edm.Int32
PX.Objects.SO.SOLine2.SiteID : Edm.Int32
PX.Objects.SO.SOLine2.SalesAcctID : Edm.Int32
PX.Objects.SO.SOLine2.SalesSubID : Edm.Int32
PX.Objects.SO.SOLine2.TranDesc : Edm.String
PX.Objects.SO.SOLine2.UOM : Edm.String "UOM"
PX.Objects.SO.SOLine2.OrderQty : Edm.Decimal
PX.Objects.SO.SOLine2.BaseOrderQty : Edm.Decimal
PX.Objects.SO.SOLine2.BaseShippedQty : Edm.Decimal
PX.Objects.SO.SOLine2.OriginalBaseShippedQty : Edm.Decimal
PX.Objects.SO.SOLine2.ShippedQty : Edm.Decimal
PX.Objects.SO.SOLine2.BilledQty : Edm.Decimal
PX.Objects.SO.SOLine2.BaseBilledQty : Edm.Decimal
PX.Objects.SO.SOLine2.UnbilledQty : Edm.Decimal
PX.Objects.SO.SOLine2.BaseUnbilledQty : Edm.Decimal
PX.Objects.SO.SOLine2.OpenQty : Edm.Decimal
PX.Objects.SO.SOLine2.BaseOpenQty : Edm.Decimal "Base Open Qty."
PX.Objects.SO.SOLine2.CompleteQtyMin : Edm.Decimal
PX.Objects.SO.SOLine2.CompleteQtyMax : Edm.Decimal
PX.Objects.SO.SOLine2.ShipDate : Edm.DateTimeOffset
PX.Objects.SO.SOLine2.CuryInfoID : Edm.Int64
PX.Objects.SO.SOLine2.CuryUnitPrice : Edm.Decimal
PX.Objects.SO.SOLine2.ActualUnitPrice : Edm.Decimal
PX.Objects.SO.SOLine2.UnitCost : Edm.Decimal
PX.Objects.SO.SOLine2.DiscPct : Edm.Decimal
PX.Objects.SO.SOLine2.CuryBilledAmt : Edm.Decimal
PX.Objects.SO.SOLine2.BilledAmt : Edm.Decimal
PX.Objects.SO.SOLine2.CuryOpenAmt : Edm.Decimal "Open Amount"
PX.Objects.SO.SOLine2.OpenAmt : Edm.Decimal
PX.Objects.SO.SOLine2.CuryUnbilledAmt : Edm.Decimal
PX.Objects.SO.SOLine2.CuryLineAmt : Edm.Decimal
PX.Objects.SO.SOLine2.LineAmt : Edm.Decimal
PX.Objects.SO.SOLine2.UnbilledAmt : Edm.Decimal
PX.Objects.SO.SOLine2.GroupDiscountRate : Edm.Decimal
PX.Objects.SO.SOLine2.DocumentDiscountRate : Edm.Decimal
PX.Objects.SO.SOLine2.DisableAutomaticTaxCalculation : Edm.Boolean
PX.Objects.SO.SOLine2.TaxZoneID : Edm.String
PX.Objects.SO.SOLine2.TaxCategoryID : Edm.String
PX.Objects.SO.SOLine2.PlanType : Edm.String
PX.Objects.SO.SOLine2.POSource : Edm.String
PX.Objects.SO.SOLine2.CuryDiscAmt : Edm.Decimal "Discount Amount"
PX.Objects.SO.SOLine2.DiscAmt : Edm.Decimal
PX.Objects.SO.SOLine2.CuryExtPrice : Edm.Decimal "Ext. Price"
PX.Objects.SO.SOLine2.ExtPrice : Edm.Decimal
PX.Objects.SO.SOLine2.LastModifiedByID : Edm.Guid "Last Modified By"
PX.Objects.SO.SOLine2.LastModifiedByScreenID : Edm.String
PX.Objects.SO.SOLine2.LastModifiedDateTime : Edm.DateTimeOffset
PX.Objects.SO.SOLine2.tstamp : Edm.Binary
PX.Objects.SO.SOLine2.CuryID : Edm.String "Currency"
PX.Objects.SO.SOLine2.CuryRate : Edm.Decimal
PX.Objects.SO.SOLine2.CuryViewState : Edm.Boolean
PX.Objects.SO.SOLine2.SOOrderByOrderNbr -> PX.Objects.SO.SOOrder (OrderType=OrderType, OrderNbr=OrderNbr)
PX.Objects.SO.SOLine2.InventoryItemByInventoryID -> PX.Objects.IN.InventoryItem (InventoryID=InventoryID)
PX.Objects.SO.SOLine2.CurrencyInfoByCuryInfoID -> PX.Objects.CM.CurrencyInfo (CuryInfoID=CuryInfoID)
PX.Objects.SO.SOLine2.TaxCategoryByTaxCategoryID -> PX.Objects.TX.TaxCategory (TaxCategoryID=TaxCategoryID)
PX.Objects.SO.SOLine2.TaxZoneByTaxZoneID -> PX.Objects.TX.TaxZone (TaxZoneID=TaxZoneID)
PX.Objects.SO.SOLine2.SOOrderSiteBySiteID -> PX.Objects.SO.SOOrderSite (OrderType=OrderType, OrderNbr=OrderNbr, SiteID=SiteID)
PX.Objects.SO.SOLine2.SOOrderTypeByOrderType -> PX.Objects.SO.SOOrderType (OrderType=OrderType)
PX.Objects.SO.SOLine2.SOOrderTypeOperationByOperation -> PX.Objects.SO.SOOrderTypeOperation (OrderType=OrderType, Operation=Operation)
PX.Objects.SO.SOLine2.SOOrderTypeOperationByOrderType -> PX.Objects.SO.SOOrderTypeOperation (Operation=Operation, OrderType=OrderType)
PX.Objects.SO.SOLine2.INSiteByPOSiteID -> PX.Objects.IN.INSite
PX.Objects.SO.SOLine2.INSiteBySiteID -> PX.Objects.IN.INSite (SiteID=SiteID)
PX.Objects.SO.SOLine2.INSubItemBySubItemID -> PX.Objects.IN.INSubItem (SubItemID=SubItemID)
PX.Objects.SO.SOLine2.AccountBySalesAcctID -> PX.Objects.GL.Account (SalesAcctID=AccountID)
PX.Objects.SO.SOLine2.SubBySalesSubID -> PX.Objects.GL.Sub (SalesSubID=SubID)
PX.Objects.SO.SOLine2.INSiteStatusBySiteID -> PX.Objects.IN.INSiteStatus (InventoryID=InventoryID, SubItemID=SubItemID, SiteID=SiteID)
PX.Objects.SO.SOLine2.SOTaxCollection -> Collection(PX.Objects.SO.SOTax)
PX.Objects.SO.SOLine2.SOTaxTranCollection -> Collection(PX.Objects.SO.SOTaxTran)
PX.Objects.SO.SOLine2.INTranCollection -> Collection(PX.Objects.IN.INTran)
PX.Objects.SO.SOLine2.POReceiptLineCollection -> Collection(PX.Objects.PO.POReceiptLine)
PX.Objects.SO.SOLine2.ARTranCollection -> Collection(PX.Objects.AR.ARTran)
PX.Objects.SO.SOLine2.SOLineSplitCollection -> Collection(PX.Objects.SO.SOLineSplit)
PX.Objects.SO.SOLine2.SOShipLineCollection -> Collection(PX.Objects.SO.SOShipLine)
PX.Objects.SO.SOLine2.SOShipLineSplitCollection -> Collection(PX.Objects.SO.SOShipLineSplit)
PX.Objects.SO.SOLine2.INCostCenterCollection -> Collection(PX.Objects.IN.INCostCenter)
PX.Objects.SO.SOLine2.INReplenishmentLineCollection -> Collection(PX.Objects.IN.INReplenishmentLine)
PX.Objects.SO.SOLine2.INTransitLineCollection -> Collection(PX.Objects.IN.INTransitLine)
PX.Objects.SO.SOLine2.RelatedItemHistoryCollection -> Collection(PX.Objects.IN.RelatedItems.RelatedItemHistory)
PX.Objects.SO.SOLine2.DropShipLinkCollection -> Collection(PX.Objects.Common.DAC.DropShipLink)
PX.Objects.SO.SOLine2.AMConfigurationResultsCollection -> Collection(PX.Objects.AM.AMConfigurationResults)
PX.Objects.SO.SOLine2.FSPostDetCollection -> Collection(PX.Objects.FS.FSPostDet)
PX.Objects.SO.SOLine2.FSPostInfoCollection -> Collection(PX.Objects.FS.FSPostInfo)

# PX.Objects.SO.SOLine4 (EntityType)

Key: LineNbr, OrderNbr, OrderType
Entity sets: PX_Objects_SO_SOLine4
Non-filterable, non-selectable: CuryID, CuryRate, CuryViewState

PX.Objects.SO.SOLine4.BranchID : Edm.Int32
PX.Objects.SO.SOLine4.OrderType : Edm.String [key]
PX.Objects.SO.SOLine4.OrderNbr : Edm.String [key]
PX.Objects.SO.SOLine4.LineNbr : Edm.Int32 [key]
PX.Objects.SO.SOLine4.SortOrder : Edm.Int32
PX.Objects.SO.SOLine4.Operation : Edm.String "Operation"
PX.Objects.SO.SOLine4.LineSign : Edm.Int16
PX.Objects.SO.SOLine4.ShipComplete : Edm.String
PX.Objects.SO.SOLine4.InventoryID : Edm.Int32
PX.Objects.SO.SOLine4.SiteID : Edm.Int32
PX.Objects.SO.SOLine4.UOM : Edm.String "UOM"
PX.Objects.SO.SOLine4.BaseOrderQty : Edm.Decimal
PX.Objects.SO.SOLine4.OrderQty : Edm.Decimal
PX.Objects.SO.SOLine4.BaseShippedQty : Edm.Decimal
PX.Objects.SO.SOLine4.ShippedQty : Edm.Decimal
PX.Objects.SO.SOLine4.UnbilledQty : Edm.Decimal
PX.Objects.SO.SOLine4.BaseUnbilledQty : Edm.Decimal
PX.Objects.SO.SOLine4.OpenQty : Edm.Decimal
PX.Objects.SO.SOLine4.BaseOpenQty : Edm.Decimal "Base Open Qty."
PX.Objects.SO.SOLine4.CompleteQtyMin : Edm.Decimal
PX.Objects.SO.SOLine4.CompleteQtyMax : Edm.Decimal
PX.Objects.SO.SOLine4.Completed : Edm.Boolean
PX.Objects.SO.SOLine4.CuryInfoID : Edm.Int64
PX.Objects.SO.SOLine4.CuryUnitPrice : Edm.Decimal
PX.Objects.SO.SOLine4.UnitPrice : Edm.Decimal
PX.Objects.SO.SOLine4.DiscPct : Edm.Decimal
PX.Objects.SO.SOLine4.CuryOpenAmt : Edm.Decimal "Open Amount"
PX.Objects.SO.SOLine4.OpenAmt : Edm.Decimal
PX.Objects.SO.SOLine4.CuryUnbilledAmt : Edm.Decimal
PX.Objects.SO.SOLine4.UnbilledAmt : Edm.Decimal
PX.Objects.SO.SOLine4.GroupDiscountRate : Edm.Decimal
PX.Objects.SO.SOLine4.DocumentDiscountRate : Edm.Decimal
PX.Objects.SO.SOLine4.TaxCategoryID : Edm.String
PX.Objects.SO.SOLine4.ShipDate : Edm.DateTimeOffset
PX.Objects.SO.SOLine4.CuryLineAmt : Edm.Decimal
PX.Objects.SO.SOLine4.LineAmt : Edm.Decimal
PX.Objects.SO.SOLine4.SalesAcctID : Edm.Int32
PX.Objects.SO.SOLine4.ProjectID : Edm.Int32
PX.Objects.SO.SOLine4.TaskID : Edm.Int32
PX.Objects.SO.SOLine4.OpenLine : Edm.Boolean
PX.Objects.SO.SOLine4.POCreate : Edm.Boolean
PX.Objects.SO.SOLine4.POSource : Edm.String
PX.Objects.SO.SOLine4.tstamp : Edm.Binary
PX.Objects.SO.SOLine4.BlanketType : Edm.String
PX.Objects.SO.SOLine4.BlanketNbr : Edm.String
PX.Objects.SO.SOLine4.BlanketLineNbr : Edm.Int32
PX.Objects.SO.SOLine4.BlanketSplitLineNbr : Edm.Int32
PX.Objects.SO.SOLine4.CuryID : Edm.String "Currency"
PX.Objects.SO.SOLine4.CuryRate : Edm.Decimal
PX.Objects.SO.SOLine4.CuryViewState : Edm.Boolean
PX.Objects.SO.SOLine4.SOOrderByOrderNbr -> PX.Objects.SO.SOOrder (OrderType=OrderType, OrderNbr=OrderNbr)
PX.Objects.SO.SOLine4.SOOrderSiteBySiteID -> PX.Objects.SO.SOOrderSite (OrderType=OrderType, OrderNbr=OrderNbr, SiteID=SiteID)
PX.Objects.SO.SOLine4.PMProjectByProjectID -> PX.Objects.PM.PMProject (ProjectID=ContractID)
PX.Objects.SO.SOLine4.PMTaskByTaskID -> PX.Objects.PM.PMTask (ProjectID=ProjectID, TaskID=TaskID)
PX.Objects.SO.SOLine4.PMTaskByProjectID -> PX.Objects.PM.PMTask (TaskID=TaskID, ProjectID=ProjectID)
PX.Objects.SO.SOLine4.InventoryItemByInventoryID -> PX.Objects.IN.InventoryItem (InventoryID=InventoryID)
PX.Objects.SO.SOLine4.BranchByBranchID -> PX.Objects.GL.Branch (BranchID=BranchID)
PX.Objects.SO.SOLine4.CurrencyInfoByCuryInfoID -> PX.Objects.CM.CurrencyInfo (CuryInfoID=CuryInfoID)
PX.Objects.SO.SOLine4.TaxCategoryByTaxCategoryID -> PX.Objects.TX.TaxCategory (TaxCategoryID=TaxCategoryID)
PX.Objects.SO.SOLine4.SOOrderTypeByOrderType -> PX.Objects.SO.SOOrderType (OrderType=OrderType)
PX.Objects.SO.SOLine4.SOOrderTypeOperationByOperation -> PX.Objects.SO.SOOrderTypeOperation (OrderType=OrderType, Operation=Operation)
PX.Objects.SO.SOLine4.SOOrderTypeOperationByOrderType -> PX.Objects.SO.SOOrderTypeOperation (Operation=Operation, OrderType=OrderType)
PX.Objects.SO.SOLine4.INSiteByPOSiteID -> PX.Objects.IN.INSite
PX.Objects.SO.SOLine4.INSiteBySiteID -> PX.Objects.IN.INSite (SiteID=SiteID)
PX.Objects.SO.SOLine4.AccountBySalesAcctID -> PX.Objects.GL.Account (SalesAcctID=AccountID)
PX.Objects.SO.SOLine4.SOTaxCollection -> Collection(PX.Objects.SO.SOTax)
PX.Objects.SO.SOLine4.SOTaxTranCollection -> Collection(PX.Objects.SO.SOTaxTran)
PX.Objects.SO.SOLine4.INTranCollection -> Collection(PX.Objects.IN.INTran)
PX.Objects.SO.SOLine4.POReceiptLineCollection -> Collection(PX.Objects.PO.POReceiptLine)
PX.Objects.SO.SOLine4.ARTranCollection -> Collection(PX.Objects.AR.ARTran)
PX.Objects.SO.SOLine4.SOLineSplitCollection -> Collection(PX.Objects.SO.SOLineSplit)
PX.Objects.SO.SOLine4.SOShipLineCollection -> Collection(PX.Objects.SO.SOShipLine)
PX.Objects.SO.SOLine4.SOShipLineSplitCollection -> Collection(PX.Objects.SO.SOShipLineSplit)
PX.Objects.SO.SOLine4.INCostCenterCollection -> Collection(PX.Objects.IN.INCostCenter)
PX.Objects.SO.SOLine4.INReplenishmentLineCollection -> Collection(PX.Objects.IN.INReplenishmentLine)
PX.Objects.SO.SOLine4.INTransitLineCollection -> Collection(PX.Objects.IN.INTransitLine)
PX.Objects.SO.SOLine4.RelatedItemHistoryCollection -> Collection(PX.Objects.IN.RelatedItems.RelatedItemHistory)
PX.Objects.SO.SOLine4.DropShipLinkCollection -> Collection(PX.Objects.Common.DAC.DropShipLink)
PX.Objects.SO.SOLine4.AMConfigurationResultsCollection -> Collection(PX.Objects.AM.AMConfigurationResults)
PX.Objects.SO.SOLine4.FSPostDetCollection -> Collection(PX.Objects.FS.FSPostDet)
PX.Objects.SO.SOLine4.FSPostInfoCollection -> Collection(PX.Objects.FS.FSPostInfo)

# PX.Objects.SO.SOLineSplit (EntityType)

Label: "Sales Order Line Split"
Key: LineNbr, OrderNbr, OrderType, SplitLineNbr
Entity sets: PX_Objects_SO_SOLineSplit, SalesOrderLineSplit, SOLineSplit
Non-filterable, non-selectable: RequireShipping, RequireAllocation, RequireLocation, IsMergeable, LotSerClassID, AssignedNbr, UnreceivedQty, BaseUnreceivedQty, OpenQty, BaseOpenQty, TranType, PlanType, ProjectID, TaskID

PX.Objects.SO.SOLineSplit.OrderType : Edm.String [key]
PX.Objects.SO.SOLineSplit.OrderNbr : Edm.String [key]
PX.Objects.SO.SOLineSplit.LineNbr : Edm.Int32 [key]
PX.Objects.SO.SOLineSplit.SplitLineNbr : Edm.Int32 [key] "Allocation ID"
PX.Objects.SO.SOLineSplit.ParentSplitLineNbr : Edm.Int32 "Parent Allocation ID"
PX.Objects.SO.SOLineSplit.RootSplitLineNbr : Edm.Int32 "Root Allocation ID"
PX.Objects.SO.SOLineSplit.Behavior : Edm.String
PX.Objects.SO.SOLineSplit.DefaultOperation : Edm.String
PX.Objects.SO.SOLineSplit.Operation : Edm.String
PX.Objects.SO.SOLineSplit.InvtMult : Edm.Int16
PX.Objects.SO.SOLineSplit.RequireShipping : Edm.Boolean
PX.Objects.SO.SOLineSplit.RequireAllocation : Edm.Boolean
PX.Objects.SO.SOLineSplit.RequireLocation : Edm.Boolean
PX.Objects.SO.SOLineSplit.InventoryID : Edm.Int32 "Inventory ID"
PX.Objects.SO.SOLineSplit.LineType : Edm.String
PX.Objects.SO.SOLineSplit.IsStockItem : Edm.Boolean
PX.Objects.SO.SOLineSplit.IsAllocated : Edm.Boolean [required] "Allocated"
PX.Objects.SO.SOLineSplit.IsMergeable : Edm.Boolean
PX.Objects.SO.SOLineSplit.ShipDate : Edm.DateTimeOffset "Ship On"
PX.Objects.SO.SOLineSplit.ShipComplete : Edm.String
PX.Objects.SO.SOLineSplit.Completed : Edm.Boolean "Completed"
PX.Objects.SO.SOLineSplit.ShipmentNbr : Edm.String "Shipment Nbr."
PX.Objects.SO.SOLineSplit.CostCenterID : Edm.Int32 [required]
PX.Objects.SO.SOLineSplit.LotSerClassID : Edm.String
PX.Objects.SO.SOLineSplit.AssignedNbr : Edm.String
PX.Objects.SO.SOLineSplit.UOM : Edm.String "UOM"
PX.Objects.SO.SOLineSplit.Qty : Edm.Decimal [required] "Quantity"
PX.Objects.SO.SOLineSplit.BaseQty : Edm.Decimal
PX.Objects.SO.SOLineSplit.ShippedQty : Edm.Decimal [required] "Qty. On Shipments"
PX.Objects.SO.SOLineSplit.BaseShippedQty : Edm.Decimal [required]
PX.Objects.SO.SOLineSplit.ClosedQty : Edm.Decimal [required]
PX.Objects.SO.SOLineSplit.BaseClosedQty : Edm.Decimal [required]
PX.Objects.SO.SOLineSplit.ReceivedQty : Edm.Decimal [required] "Qty. Received"
PX.Objects.SO.SOLineSplit.BaseReceivedQty : Edm.Decimal [required]
PX.Objects.SO.SOLineSplit.UnreceivedQty : Edm.Decimal
PX.Objects.SO.SOLineSplit.BaseUnreceivedQty : Edm.Decimal
PX.Objects.SO.SOLineSplit.OpenQty : Edm.Decimal
PX.Objects.SO.SOLineSplit.BaseOpenQty : Edm.Decimal
PX.Objects.SO.SOLineSplit.OrderDate : Edm.DateTimeOffset
PX.Objects.SO.SOLineSplit.TranType : Edm.String
PX.Objects.SO.SOLineSplit.PlanType : Edm.String
PX.Objects.SO.SOLineSplit.OrigPlanType : Edm.String
PX.Objects.SO.SOLineSplit.POCreate : Edm.Boolean "Mark for PO"
PX.Objects.SO.SOLineSplit.POCompleted : Edm.Boolean
PX.Objects.SO.SOLineSplit.POCancelled : Edm.Boolean
PX.Objects.SO.SOLineSplit.POSource : Edm.String
PX.Objects.SO.SOLineSplit.FixedSource : Edm.String
PX.Objects.SO.SOLineSplit.VendorID : Edm.Int32
PX.Objects.SO.SOLineSplit.POSiteID : Edm.Int32
PX.Objects.SO.SOLineSplit.POType : Edm.String "PO Type"
PX.Objects.SO.SOLineSplit.PONbr : Edm.String "PO Nbr."
PX.Objects.SO.SOLineSplit.POLineNbr : Edm.Int32 "PO Line Nbr."
PX.Objects.SO.SOLineSplit.POReceiptType : Edm.String "PO Receipt Type"
PX.Objects.SO.SOLineSplit.POReceiptNbr : Edm.String "PO Receipt Nbr."
PX.Objects.SO.SOLineSplit.POPromisedDate : Edm.DateTimeOffset "PO Promised On"
PX.Objects.SO.SOLineSplit.SOOrderType : Edm.String
PX.Objects.SO.SOLineSplit.SOOrderNbr : Edm.String
PX.Objects.SO.SOLineSplit.SOLineNbr : Edm.Int32
PX.Objects.SO.SOLineSplit.SOSplitLineNbr : Edm.Int32
PX.Objects.SO.SOLineSplit.RefNoteID : Edm.Guid "Related Document"
PX.Objects.SO.SOLineSplit.SOTransferRequestedOn : Edm.DateTimeOffset "Transfer Requested On"
PX.Objects.SO.SOLineSplit.PlanID : Edm.Int64
PX.Objects.SO.SOLineSplit.ProjectID : Edm.Int32
PX.Objects.SO.SOLineSplit.TaskID : Edm.Int32
PX.Objects.SO.SOLineSplit.AMProdCreate : Edm.Boolean "Mark for Production"
PX.Objects.SO.SOLineSplit.CustomerOrderNbr : Edm.String "Customer Order Nbr."
PX.Objects.SO.SOLineSplit.SchedOrderDate : Edm.DateTimeOffset "Sched. Order Date"
PX.Objects.SO.SOLineSplit.SchedShipDate : Edm.DateTimeOffset "Sched. Shipment Date"
PX.Objects.SO.SOLineSplit.POCreateDate : Edm.DateTimeOffset "PO Creation Date"
PX.Objects.SO.SOLineSplit.QtyOnOrders : Edm.Decimal [required] "Qty. On Orders"
PX.Objects.SO.SOLineSplit.BaseQtyOnOrders : Edm.Decimal [required]
PX.Objects.SO.SOLineSplit.BlanketOpenQty : Edm.Decimal "Blanket Open Qty."
PX.Objects.SO.SOLineSplit.ChildLineCntr : Edm.Int32 [required]
PX.Objects.SO.SOLineSplit.EffectiveChildLineCntr : Edm.Int32 [required]
PX.Objects.SO.SOLineSplit.OpenChildLineCntr : Edm.Int32 [required]
PX.Objects.SO.SOLineSplit.CreatedByID : Edm.Guid "Created By"
PX.Objects.SO.SOLineSplit.CreatedByScreenID : Edm.String
PX.Objects.SO.SOLineSplit.CreatedDateTime : Edm.DateTimeOffset
PX.Objects.SO.SOLineSplit.LastModifiedByID : Edm.Guid "Last Modified By"
PX.Objects.SO.SOLineSplit.LastModifiedByScreenID : Edm.String
PX.Objects.SO.SOLineSplit.LastModifiedDateTime : Edm.DateTimeOffset
PX.Objects.SO.SOLineSplit.tstamp : Edm.Binary
PX.Objects.SO.SOLineSplit.VendorByVendorID -> PX.Objects.AP.Vendor (VendorID=BAccountID)
PX.Objects.SO.SOLineSplit.POLineByPOLineNbr -> PX.Objects.PO.POLine (POType=OrderType, PONbr=OrderNbr, POLineNbr=LineNbr)
PX.Objects.SO.SOLineSplit.POOrderByPONbr -> PX.Objects.PO.POOrder (POType=OrderType, PONbr=OrderNbr)
PX.Objects.SO.SOLineSplit.POOrderByPOType -> PX.Objects.PO.POOrder (PONbr=OrderNbr, POType=OrderType)
PX.Objects.SO.SOLineSplit.InventoryItemByInventoryID -> PX.Objects.IN.InventoryItem (InventoryID=InventoryID)
PX.Objects.SO.SOLineSplit.SOOrderByOrderNbr -> PX.Objects.SO.SOOrder (OrderType=OrderType, OrderNbr=OrderNbr)
PX.Objects.SO.SOLineSplit.INItemPlanByPlanID -> PX.Objects.IN.INItemPlan (PlanID=PlanID)
PX.Objects.SO.SOLineSplit.UsersByCreatedByID -> PX.SM.Users (CreatedByID=PKID)
PX.Objects.SO.SOLineSplit.UsersByLastModifiedByID -> PX.SM.Users (LastModifiedByID=PKID)
PX.Objects.SO.SOLineSplit.SOLineByLineNbr -> PX.Objects.SO.SOLine (OrderType=OrderType, OrderNbr=OrderNbr, LineNbr=LineNbr)
PX.Objects.SO.SOLineSplit.SOLineSplitBySplitLineNbr -> PX.Objects.SO.SOLineSplit (SplitLineNbr=ParentSplitLineNbr)
PX.Objects.SO.SOLineSplit.SOOrderTypeByOrderType -> PX.Objects.SO.SOOrderType (OrderType=OrderType)
PX.Objects.SO.SOLineSplit.SOOrderTypeOperationByOperation -> PX.Objects.SO.SOOrderTypeOperation (OrderType=OrderType, Operation=Operation)
PX.Objects.SO.SOLineSplit.SOOrderTypeOperationByOrderType -> PX.Objects.SO.SOOrderTypeOperation (Operation=Operation, OrderType=OrderType)
PX.Objects.SO.SOLineSplit.SOShipmentByShipmentNbr -> PX.Objects.SO.SOShipment (ShipmentNbr=ShipmentNbr)
PX.Objects.SO.SOLineSplit.POReceiptByPOReceiptNbr -> PX.Objects.PO.POReceipt (POReceiptType=ReceiptType, POReceiptNbr=ReceiptNbr)
PX.Objects.SO.SOLineSplit.POReceiptByPOReceiptType -> PX.Objects.PO.POReceipt (POReceiptNbr=ReceiptNbr, POReceiptType=ReceiptType)
PX.Objects.SO.SOLineSplit.INLocationByLocationID -> PX.Objects.IN.INLocation
PX.Objects.SO.SOLineSplit.INLocationBySiteID -> PX.Objects.IN.INLocation
PX.Objects.SO.SOLineSplit.INSiteBySiteID -> PX.Objects.IN.INSite
PX.Objects.SO.SOLineSplit.INSiteByToSiteID -> PX.Objects.IN.INSite
PX.Objects.SO.SOLineSplit.INSubItemBySubItemID -> PX.Objects.IN.INSubItem
PX.Objects.SO.SOLineSplit.INUnitByInventoryID -> PX.Objects.IN.INUnit (UOM=FromUnit, InventoryID=InventoryID)
PX.Objects.SO.SOLineSplit.SupplyPOLineByPOLineNbr -> PX.Objects.SO.SupplyPOLine (POType=OrderType, PONbr=OrderNbr, POLineNbr=LineNbr)
PX.Objects.SO.SOLineSplit.INLotSerialStatusByCostCenterBySiteID -> PX.Objects.IN.INLotSerialStatusByCostCenter (InventoryID=InventoryID, CostCenterID=CostCenterID)
PX.Objects.SO.SOLineSplit.INLocationStatusByLocationID -> PX.Objects.IN.INLocationStatus (InventoryID=InventoryID)
PX.Objects.SO.SOLineSplit.INLotSerialStatusByLotSerialNbr -> PX.Objects.IN.INLotSerialStatus (InventoryID=InventoryID)
PX.Objects.SO.SOLineSplit.INSiteStatusBySiteID -> PX.Objects.IN.INSiteStatus (InventoryID=InventoryID)
PX.Objects.SO.SOLineSplit.INSiteStatusByToSiteID -> PX.Objects.IN.INSiteStatus (InventoryID=InventoryID)
PX.Objects.SO.SOLineSplit.INPlanTypeByOrigPlanType -> PX.Objects.IN.INPlanType (OrigPlanType=PlanType)
PX.Objects.SO.SOLineSplit.SOLineSplitCollection -> Collection(PX.Objects.SO.SOLineSplit)
PX.Objects.SO.SOLineSplit.SOShipLineCollection -> Collection(PX.Objects.SO.SOShipLine)
PX.Objects.SO.SOLineSplit.SOShipLineSplitCollection -> Collection(PX.Objects.SO.SOShipLineSplit)
PX.Objects.SO.SOLineSplit.INReplenishmentLineCollection -> Collection(PX.Objects.IN.INReplenishmentLine)

# PX.Objects.SO.SOLineSplit2 (EntityType)

Key: LineNbr, OrderNbr, OrderType, SplitLineNbr
Entity sets: PX_Objects_SO_SOLineSplit2

PX.Objects.SO.SOLineSplit2.OrderType : Edm.String [key]
PX.Objects.SO.SOLineSplit2.OrderNbr : Edm.String [key]
PX.Objects.SO.SOLineSplit2.LineNbr : Edm.Int32 [key]
PX.Objects.SO.SOLineSplit2.SplitLineNbr : Edm.Int32 [key]
PX.Objects.SO.SOLineSplit2.Operation : Edm.String "Operation"
PX.Objects.SO.SOLineSplit2.Completed : Edm.Boolean
PX.Objects.SO.SOLineSplit2.InventoryID : Edm.Int32
PX.Objects.SO.SOLineSplit2.SiteID : Edm.Int32
PX.Objects.SO.SOLineSplit2.ToSiteID : Edm.Int32
PX.Objects.SO.SOLineSplit2.CostCenterID : Edm.Int32
PX.Objects.SO.SOLineSplit2.LotSerialNbr : Edm.String
PX.Objects.SO.SOLineSplit2.UOM : Edm.String "UOM"
PX.Objects.SO.SOLineSplit2.Qty : Edm.Decimal
PX.Objects.SO.SOLineSplit2.BaseQty : Edm.Decimal
PX.Objects.SO.SOLineSplit2.ShippedQty : Edm.Decimal
PX.Objects.SO.SOLineSplit2.BaseShippedQty : Edm.Decimal
PX.Objects.SO.SOLineSplit2.ShipDate : Edm.DateTimeOffset
PX.Objects.SO.SOLineSplit2.PlanType : Edm.String
PX.Objects.SO.SOLineSplit2.POCreate : Edm.Boolean
PX.Objects.SO.SOLineSplit2.IsAllocated : Edm.Boolean
PX.Objects.SO.SOLineSplit2.RefNoteID : Edm.Guid
PX.Objects.SO.SOLineSplit2.SOTransferRequestedOn : Edm.DateTimeOffset
PX.Objects.SO.SOLineSplit2.PlanID : Edm.Int64
PX.Objects.SO.SOLineSplit2.SOOrderType : Edm.String
PX.Objects.SO.SOLineSplit2.SOOrderNbr : Edm.String
PX.Objects.SO.SOLineSplit2.SOLineNbr : Edm.Int32
PX.Objects.SO.SOLineSplit2.SOSplitLineNbr : Edm.Int32
PX.Objects.SO.SOLineSplit2.LastModifiedByID : Edm.Guid "Last Modified By"
PX.Objects.SO.SOLineSplit2.LastModifiedByScreenID : Edm.String
PX.Objects.SO.SOLineSplit2.LastModifiedDateTime : Edm.DateTimeOffset
PX.Objects.SO.SOLineSplit2.tstamp : Edm.Binary
PX.Objects.SO.SOLineSplit2.InventoryItemByInventoryID -> PX.Objects.IN.InventoryItem (InventoryID=InventoryID)
PX.Objects.SO.SOLineSplit2.SOOrderByOrderNbr -> PX.Objects.SO.SOOrder (OrderType=OrderType, OrderNbr=OrderNbr)
PX.Objects.SO.SOLineSplit2.INItemPlanByPlanID -> PX.Objects.IN.INItemPlan (PlanID=PlanID)
PX.Objects.SO.SOLineSplit2.SOLineByLineNbr -> PX.Objects.SO.SOLine (OrderType=OrderType, OrderNbr=OrderNbr, LineNbr=LineNbr)
PX.Objects.SO.SOLineSplit2.SOLineSplitBySplitLineNbr -> PX.Objects.SO.SOLineSplit (SplitLineNbr=ParentSplitLineNbr)
PX.Objects.SO.SOLineSplit2.SOOrderTypeByOrderType -> PX.Objects.SO.SOOrderType (OrderType=OrderType)
PX.Objects.SO.SOLineSplit2.SOOrderTypeOperationByOperation -> PX.Objects.SO.SOOrderTypeOperation (OrderType=OrderType, Operation=Operation)
PX.Objects.SO.SOLineSplit2.SOOrderTypeOperationByOrderType -> PX.Objects.SO.SOOrderTypeOperation (Operation=Operation, OrderType=OrderType)
PX.Objects.SO.SOLineSplit2.INSiteBySiteID -> PX.Objects.IN.INSite (SiteID=SiteID)
PX.Objects.SO.SOLineSplit2.INSiteByToSiteID -> PX.Objects.IN.INSite (ToSiteID=SiteID)
PX.Objects.SO.SOLineSplit2.SOLineSplitCollection -> Collection(PX.Objects.SO.SOLineSplit)
PX.Objects.SO.SOLineSplit2.SOShipLineCollection -> Collection(PX.Objects.SO.SOShipLine)
PX.Objects.SO.SOLineSplit2.SOShipLineSplitCollection -> Collection(PX.Objects.SO.SOShipLineSplit)
PX.Objects.SO.SOLineSplit2.INReplenishmentLineCollection -> Collection(PX.Objects.IN.INReplenishmentLine)

# PX.Objects.SO.SOMiscLine2 (EntityType)

Key: LineNbr, OrderNbr, OrderType
Entity sets: PX_Objects_SO_SOMiscLine2
Non-filterable, non-selectable: CuryID, CuryRate, CuryViewState

PX.Objects.SO.SOMiscLine2.BranchID : Edm.Int32
PX.Objects.SO.SOMiscLine2.OrderType : Edm.String [key]
PX.Objects.SO.SOMiscLine2.OrderNbr : Edm.String [key]
PX.Objects.SO.SOMiscLine2.LineNbr : Edm.Int32 [key]
PX.Objects.SO.SOMiscLine2.SortOrder : Edm.Int32
PX.Objects.SO.SOMiscLine2.DefaultOperation : Edm.String
PX.Objects.SO.SOMiscLine2.Operation : Edm.String "Operation"
PX.Objects.SO.SOMiscLine2.LineSign : Edm.Int16
PX.Objects.SO.SOMiscLine2.Completed : Edm.Boolean "Completed"
PX.Objects.SO.SOMiscLine2.InventoryID : Edm.Int32 "Inventory ID"
PX.Objects.SO.SOMiscLine2.SiteID : Edm.Int32
PX.Objects.SO.SOMiscLine2.ProjectID : Edm.Int32
PX.Objects.SO.SOMiscLine2.ShipDate : Edm.DateTimeOffset
PX.Objects.SO.SOMiscLine2.InvoiceType : Edm.String
PX.Objects.SO.SOMiscLine2.InvoiceNbr : Edm.String
PX.Objects.SO.SOMiscLine2.InvoiceLineNbr : Edm.Int32
PX.Objects.SO.SOMiscLine2.InvoiceDate : Edm.DateTimeOffset
PX.Objects.SO.SOMiscLine2.CuryInfoID : Edm.Int64
PX.Objects.SO.SOMiscLine2.UOM : Edm.String "UOM"
PX.Objects.SO.SOMiscLine2.OrderQty : Edm.Decimal
PX.Objects.SO.SOMiscLine2.BilledQty : Edm.Decimal
PX.Objects.SO.SOMiscLine2.BaseBilledQty : Edm.Decimal
PX.Objects.SO.SOMiscLine2.UnbilledQty : Edm.Decimal
PX.Objects.SO.SOMiscLine2.BaseUnbilledQty : Edm.Decimal
PX.Objects.SO.SOMiscLine2.CuryUnitPrice : Edm.Decimal
PX.Objects.SO.SOMiscLine2.CuryExtPrice : Edm.Decimal
PX.Objects.SO.SOMiscLine2.CuryLineAmt : Edm.Decimal "Ext. Amount"
PX.Objects.SO.SOMiscLine2.LineAmt : Edm.Decimal
PX.Objects.SO.SOMiscLine2.CuryBilledAmt : Edm.Decimal
PX.Objects.SO.SOMiscLine2.BilledAmt : Edm.Decimal
PX.Objects.SO.SOMiscLine2.CuryUnbilledAmt : Edm.Decimal
PX.Objects.SO.SOMiscLine2.UnbilledAmt : Edm.Decimal
PX.Objects.SO.SOMiscLine2.CuryDiscAmt : Edm.Decimal "Ext. Amount"
PX.Objects.SO.SOMiscLine2.DiscAmt : Edm.Decimal
PX.Objects.SO.SOMiscLine2.DiscPct : Edm.Decimal
PX.Objects.SO.SOMiscLine2.GroupDiscountRate : Edm.Decimal
PX.Objects.SO.SOMiscLine2.DocumentDiscountRate : Edm.Decimal
PX.Objects.SO.SOMiscLine2.TaxZoneID : Edm.String
PX.Objects.SO.SOMiscLine2.TaxCategoryID : Edm.String
PX.Objects.SO.SOMiscLine2.SalesPersonID : Edm.Int32 "Salesperson ID"
PX.Objects.SO.SOMiscLine2.CostCodeID : Edm.Int32
PX.Objects.SO.SOMiscLine2.TranDesc : Edm.String "Line Description"
PX.Objects.SO.SOMiscLine2.NoteID : Edm.Guid
PX.Objects.SO.SOMiscLine2.Commissionable : Edm.Boolean
PX.Objects.SO.SOMiscLine2.IsFree : Edm.Boolean "Free Item"
PX.Objects.SO.SOMiscLine2.ManualPrice : Edm.Boolean
PX.Objects.SO.SOMiscLine2.ManualDisc : Edm.Boolean "Manual Discount"
PX.Objects.SO.SOMiscLine2.DiscountID : Edm.String "Discount Code"
PX.Objects.SO.SOMiscLine2.DiscountSequenceID : Edm.String "Discount Sequence"
PX.Objects.SO.SOMiscLine2.DRTermStartDate : Edm.DateTimeOffset "Term Start Date"
PX.Objects.SO.SOMiscLine2.DRTermEndDate : Edm.DateTimeOffset "Term End Date"
PX.Objects.SO.SOMiscLine2.CuryUnitPriceDR : Edm.Decimal "Unit Price for DR"
PX.Objects.SO.SOMiscLine2.DiscPctDR : Edm.Decimal "Discount Percent for DR"
PX.Objects.SO.SOMiscLine2.DefScheduleID : Edm.Int32
PX.Objects.SO.SOMiscLine2.BlanketType : Edm.String
PX.Objects.SO.SOMiscLine2.BlanketNbr : Edm.String
PX.Objects.SO.SOMiscLine2.BlanketLineNbr : Edm.Int32
PX.Objects.SO.SOMiscLine2.BlanketSplitLineNbr : Edm.Int32
PX.Objects.SO.SOMiscLine2.tstamp : Edm.Binary
PX.Objects.SO.SOMiscLine2.CuryID : Edm.String "Currency"
PX.Objects.SO.SOMiscLine2.CuryRate : Edm.Decimal
PX.Objects.SO.SOMiscLine2.CuryViewState : Edm.Boolean
PX.Objects.SO.SOMiscLine2.SOOrderByOrderNbr -> PX.Objects.SO.SOOrder (OrderType=OrderType, OrderNbr=OrderNbr)
PX.Objects.SO.SOMiscLine2.ARDiscountByDiscountID -> PX.Objects.AR.ARDiscount (DiscountID=DiscountID)
PX.Objects.SO.SOMiscLine2.PMProjectByProjectID -> PX.Objects.PM.PMProject (ProjectID=ContractID)
PX.Objects.SO.SOMiscLine2.BranchByBranchID -> PX.Objects.GL.Branch (BranchID=BranchID)
PX.Objects.SO.SOMiscLine2.CurrencyInfoByCuryInfoID -> PX.Objects.CM.CurrencyInfo (CuryInfoID=CuryInfoID)
PX.Objects.SO.SOMiscLine2.TaxCategoryByTaxCategoryID -> PX.Objects.TX.TaxCategory (TaxCategoryID=TaxCategoryID)
PX.Objects.SO.SOMiscLine2.TaxZoneByTaxZoneID -> PX.Objects.TX.TaxZone (TaxZoneID=TaxZoneID)
PX.Objects.SO.SOMiscLine2.SOOrderSiteBySiteID -> PX.Objects.SO.SOOrderSite (OrderType=OrderType, OrderNbr=OrderNbr, SiteID=SiteID)
PX.Objects.SO.SOMiscLine2.SOOrderTypeByOrderType -> PX.Objects.SO.SOOrderType (OrderType=OrderType)
PX.Objects.SO.SOMiscLine2.SOOrderTypeOperationByOperation -> PX.Objects.SO.SOOrderTypeOperation (OrderType=OrderType, Operation=Operation)
PX.Objects.SO.SOMiscLine2.SOOrderTypeOperationByOrderType -> PX.Objects.SO.SOOrderTypeOperation (Operation=Operation, OrderType=OrderType)
PX.Objects.SO.SOMiscLine2.PMCostCodeByCostCodeID -> PX.Objects.PM.PMCostCode (CostCodeID=CostCodeID)
PX.Objects.SO.SOMiscLine2.DRScheduleByDefScheduleID -> PX.Objects.DR.DRSchedule (DefScheduleID=ScheduleID)
PX.Objects.SO.SOMiscLine2.INSiteByPOSiteID -> PX.Objects.IN.INSite
PX.Objects.SO.SOMiscLine2.INSiteBySiteID -> PX.Objects.IN.INSite (SiteID=SiteID)
PX.Objects.SO.SOMiscLine2.ARTranByInvoiceLineNbr -> PX.Objects.AR.ARTran (InvoiceType=TranType, InvoiceNbr=RefNbr, InvoiceLineNbr=LineNbr)
PX.Objects.SO.SOMiscLine2.DiscountSequenceByDiscountSequenceID -> PX.Objects.AR.DiscountSequence (DiscountID=DiscountID, DiscountSequenceID=DiscountSequenceID)
PX.Objects.SO.SOMiscLine2.SOInvoiceByInvoiceNbr -> PX.Objects.SO.SOInvoice (InvoiceType=DocType, InvoiceNbr=RefNbr)
PX.Objects.SO.SOMiscLine2.SOTaxCollection -> Collection(PX.Objects.SO.SOTax)
PX.Objects.SO.SOMiscLine2.SOTaxTranCollection -> Collection(PX.Objects.SO.SOTaxTran)
PX.Objects.SO.SOMiscLine2.INTranCollection -> Collection(PX.Objects.IN.INTran)
PX.Objects.SO.SOMiscLine2.POReceiptLineCollection -> Collection(PX.Objects.PO.POReceiptLine)
PX.Objects.SO.SOMiscLine2.ARTranCollection -> Collection(PX.Objects.AR.ARTran)
PX.Objects.SO.SOMiscLine2.SOLineSplitCollection -> Collection(PX.Objects.SO.SOLineSplit)
PX.Objects.SO.SOMiscLine2.SOShipLineCollection -> Collection(PX.Objects.SO.SOShipLine)
PX.Objects.SO.SOMiscLine2.SOShipLineSplitCollection -> Collection(PX.Objects.SO.SOShipLineSplit)
PX.Objects.SO.SOMiscLine2.INCostCenterCollection -> Collection(PX.Objects.IN.INCostCenter)
PX.Objects.SO.SOMiscLine2.INReplenishmentLineCollection -> Collection(PX.Objects.IN.INReplenishmentLine)
PX.Objects.SO.SOMiscLine2.INTransitLineCollection -> Collection(PX.Objects.IN.INTransitLine)
PX.Objects.SO.SOMiscLine2.RelatedItemHistoryCollection -> Collection(PX.Objects.IN.RelatedItems.RelatedItemHistory)
PX.Objects.SO.SOMiscLine2.DropShipLinkCollection -> Collection(PX.Objects.Common.DAC.DropShipLink)
PX.Objects.SO.SOMiscLine2.AMConfigurationResultsCollection -> Collection(PX.Objects.AM.AMConfigurationResults)
PX.Objects.SO.SOMiscLine2.FSPostDetCollection -> Collection(PX.Objects.FS.FSPostDet)
PX.Objects.SO.SOMiscLine2.FSPostInfoCollection -> Collection(PX.Objects.FS.FSPostInfo)

# PX.Objects.SO.SONotification (EntityType)

Label: "Default Notification setup"
BaseType: PX.Objects.CS.NotificationSetup
Key: SetupID (inherited from PX.Objects.CS.NotificationSetup)
Entity sets: PX_Objects_SO_SONotification

# PX.Objects.SO.SOOrchestrationPlan (EntityType)

Label: "Orchestration Plan"
Key: PlanID
Entity sets: PX_Objects_SO_SOOrchestrationPlan, OrchestrationPlan, SOOrchestrationPlan

PX.Objects.SO.SOOrchestrationPlan.PlanID : Edm.String [key] "Plan ID"
PX.Objects.SO.SOOrchestrationPlan.PlanDescription : Edm.String "Description"
PX.Objects.SO.SOOrchestrationPlan.Strategy : Edm.String "Fulfillment Strategy"
PX.Objects.SO.SOOrchestrationPlan.ShippingZoneID : Edm.String "Shipping Zone"
PX.Objects.SO.SOOrchestrationPlan.IncludeSourceWarehouse : Edm.Boolean [required] "Include Source Warehouse"
PX.Objects.SO.SOOrchestrationPlan.IsActive : Edm.Boolean [required] "Active"
PX.Objects.SO.SOOrchestrationPlan.LineCntr : Edm.Int32 [required]
PX.Objects.SO.SOOrchestrationPlan.CreatedByID : Edm.Guid "Created By"
PX.Objects.SO.SOOrchestrationPlan.CreatedByScreenID : Edm.String
PX.Objects.SO.SOOrchestrationPlan.CreatedDateTime : Edm.DateTimeOffset
PX.Objects.SO.SOOrchestrationPlan.LastModifiedByID : Edm.Guid "Last Modified By"
PX.Objects.SO.SOOrchestrationPlan.LastModifiedByScreenID : Edm.String
PX.Objects.SO.SOOrchestrationPlan.LastModifiedDateTime : Edm.DateTimeOffset
PX.Objects.SO.SOOrchestrationPlan.tstamp : Edm.Binary
PX.Objects.SO.SOOrchestrationPlan.UsersByCreatedByID -> PX.SM.Users (CreatedByID=PKID)
PX.Objects.SO.SOOrchestrationPlan.UsersByLastModifiedByID -> PX.SM.Users (LastModifiedByID=PKID)
PX.Objects.SO.SOOrchestrationPlan.ShippingZoneByShippingZoneID -> PX.Objects.CS.ShippingZone (ShippingZoneID=ZoneID)
PX.Objects.SO.SOOrchestrationPlan.INSiteBySourceSiteID -> PX.Objects.IN.INSite
PX.Objects.SO.SOOrchestrationPlan.SOLineCollection -> Collection(PX.Objects.SO.SOLine)
PX.Objects.SO.SOOrchestrationPlan.SOOrchestrationPlanLineCollection -> Collection(PX.Objects.SO.SOOrchestrationPlanLine)

# PX.Objects.SO.SOOrchestrationPlanLine (EntityType)

Label: "Orchestration Plan Line"
Key: LineNbr, PlanID
Entity sets: PX_Objects_SO_SOOrchestrationPlanLine, OrchestrationPlanLine, SOOrchestrationPlanLine

PX.Objects.SO.SOOrchestrationPlanLine.PlanID : Edm.String [key] "Plan ID"
PX.Objects.SO.SOOrchestrationPlanLine.LineNbr : Edm.Int32 [key] "Line Nbr."
PX.Objects.SO.SOOrchestrationPlanLine.Priority : Edm.Int32 "Priority"
PX.Objects.SO.SOOrchestrationPlanLine.MaintainSaftyStock : Edm.Boolean [required] "Maintain Safety Stock"
PX.Objects.SO.SOOrchestrationPlanLine.CreatedByID : Edm.Guid "Created By"
PX.Objects.SO.SOOrchestrationPlanLine.CreatedByScreenID : Edm.String
PX.Objects.SO.SOOrchestrationPlanLine.CreatedDateTime : Edm.DateTimeOffset
PX.Objects.SO.SOOrchestrationPlanLine.LastModifiedByID : Edm.Guid "Last Modified By"
PX.Objects.SO.SOOrchestrationPlanLine.LastModifiedByScreenID : Edm.String
PX.Objects.SO.SOOrchestrationPlanLine.LastModifiedDateTime : Edm.DateTimeOffset
PX.Objects.SO.SOOrchestrationPlanLine.tstamp : Edm.Binary
PX.Objects.SO.SOOrchestrationPlanLine.UsersByCreatedByID -> PX.SM.Users (CreatedByID=PKID)
PX.Objects.SO.SOOrchestrationPlanLine.UsersByLastModifiedByID -> PX.SM.Users (LastModifiedByID=PKID)
PX.Objects.SO.SOOrchestrationPlanLine.SOOrchestrationPlanByPlanID -> PX.Objects.SO.SOOrchestrationPlan (PlanID=PlanID)
PX.Objects.SO.SOOrchestrationPlanLine.INSiteByTargetSiteID -> PX.Objects.IN.INSite

# PX.Objects.SO.SOOrder (EntityType)

Label: "Sales Order"
Key: OrderNbr, OrderType
Entity sets: PX_Objects_SO_SOOrder, SalesOrder, SOOrder
Non-filterable, non-selectable: IsInvoiceOrder, DontApprove, Rejected, ShipmentDeleted, BackOrdered, NoteText, WillCall, EmployeeID, CuryTermsDiscAmt, TermsDiscAmt, DestinationSiteIdErrorMessage, ActiveOperationsCntr, DefaultTranType, UpdateNextNumber, ExternalTaxesImportInProgress, CuryDocBal, DocBal, DeferPriceDiscountRecalculation, IsPriceAndDiscountsValid, ForceCompleteOrder, ArePaymentsApplicable, IsFullyPaid, AllowsRequiredPrepayment, IsIntercompany, SuggestRelatedItems, IsCreditMemoOrder, IsRMAOrder, IsMixedOrder, IsTransferOrder, IsDebitMemoOrder, IsNoAROrder, IsCashSaleOrder, IsPaymentInfoEnabled, IsUserInvoiceNumbering, IsFreightAvailable, ShowDiscountsTab, ShowShipmentsTab, ShowOrdersTab, IsOrchestrationAllowed, KeepOrchestrationStatus, IsBeingCopied, ExtCarrierPlugIn, ExtCarrierServiceMethod, CuryRate, CuryViewState

PX.Objects.SO.SOOrder.RiskLineCntr : Edm.Int32 [required]
PX.Objects.SO.SOOrder.OrderType : Edm.String [key required] "Order Type"
PX.Objects.SO.SOOrder.Behavior : Edm.String "Behavior"
PX.Objects.SO.SOOrder.ARDocType : Edm.String "AR Document Type"
PX.Objects.SO.SOOrder.IsInvoiceOrder : Edm.Boolean
PX.Objects.SO.SOOrder.OrderNbr : Edm.String [key] "Order Nbr."
PX.Objects.SO.SOOrder.CustomerID : Edm.Int32 "Customer"
PX.Objects.SO.SOOrder.ContactID : Edm.Int32 "Contact"
PX.Objects.SO.SOOrder.OrderDate : Edm.DateTimeOffset "Date"
PX.Objects.SO.SOOrder.CustomerOrderNbr : Edm.String "Customer Order Nbr."
PX.Objects.SO.SOOrder.CustomerRefNbr : Edm.String "External Reference"
PX.Objects.SO.SOOrder.CancelDate : Edm.DateTimeOffset "Cancel By"
PX.Objects.SO.SOOrder.RequestDate : Edm.DateTimeOffset "Requested On"
PX.Objects.SO.SOOrder.ShipDate : Edm.DateTimeOffset "Sched. Shipment"
PX.Objects.SO.SOOrder.DontApprove : Edm.Boolean "Don't Approve"
PX.Objects.SO.SOOrder.Hold : Edm.Boolean [required] "Hold"
PX.Objects.SO.SOOrder.Approved : Edm.Boolean [required]
PX.Objects.SO.SOOrder.Rejected : Edm.Boolean
PX.Objects.SO.SOOrder.Emailed : Edm.Boolean [required] "Emailed"
PX.Objects.SO.SOOrder.Printed : Edm.Boolean [required] "Printed"
PX.Objects.SO.SOOrder.CreditHold : Edm.Boolean [required] "Credit Hold"
PX.Objects.SO.SOOrder.Completed : Edm.Boolean [required] "Completed"
PX.Objects.SO.SOOrder.Cancelled : Edm.Boolean "Canceled"
PX.Objects.SO.SOOrder.OpenDoc : Edm.Boolean [required]
PX.Objects.SO.SOOrder.ShipmentDeleted : Edm.Boolean
PX.Objects.SO.SOOrder.BackOrdered : Edm.Boolean "BackOrdered"
PX.Objects.SO.SOOrder.LastSiteID : Edm.Int32 "Last Shipment Site"
PX.Objects.SO.SOOrder.LastShipDate : Edm.DateTimeOffset "Last Shipment Date"
PX.Objects.SO.SOOrder.BillSeparately : Edm.Boolean "Bill Separately"
PX.Objects.SO.SOOrder.ShipSeparately : Edm.Boolean "Ship Separately"
PX.Objects.SO.SOOrder.Status : Edm.String "Status"
PX.Objects.SO.SOOrder.NoteID : Edm.Guid
PX.Objects.SO.SOOrder.NoteText : Edm.String "Note Text"
PX.Objects.SO.SOOrder.LineCntr : Edm.Int32 [required]
PX.Objects.SO.SOOrder.BilledCntr : Edm.Int32
PX.Objects.SO.SOOrder.ReleasedCntr : Edm.Int32
PX.Objects.SO.SOOrder.PaymentCntr : Edm.Int32 [required]
PX.Objects.SO.SOOrder.AuthorizedPaymentCntr : Edm.Int32 [required]
PX.Objects.SO.SOOrder.OrderDesc : Edm.String "Description"
PX.Objects.SO.SOOrder.BillAddressID : Edm.Int32
PX.Objects.SO.SOOrder.ShipAddressID : Edm.Int32
PX.Objects.SO.SOOrder.BillContactID : Edm.Int32
PX.Objects.SO.SOOrder.ShipContactID : Edm.Int32
PX.Objects.SO.SOOrder.CuryID : Edm.String "Currency"
PX.Objects.SO.SOOrder.CuryInfoID : Edm.Int64
PX.Objects.SO.SOOrder.CuryLineDiscTotal : Edm.Decimal [required] "Line Discounts"
PX.Objects.SO.SOOrder.LineDiscTotal : Edm.Decimal [required] "Line Discounts"
PX.Objects.SO.SOOrder.CuryGroupDiscTotal : Edm.Decimal [required] "Group Discounts"
PX.Objects.SO.SOOrder.GroupDiscTotal : Edm.Decimal [required] "Group Discounts"
PX.Objects.SO.SOOrder.CuryDocumentDiscTotal : Edm.Decimal [required] "Document Discount"
PX.Objects.SO.SOOrder.DocumentDiscTotal : Edm.Decimal [required] "Document Discount"
PX.Objects.SO.SOOrder.DiscTot : Edm.Decimal [required] "Group and Document Discount Total"
PX.Objects.SO.SOOrder.CuryDiscTot : Edm.Decimal [required] "Document Discounts"
PX.Objects.SO.SOOrder.CuryOrderDiscTotal : Edm.Decimal "Discount Total"
PX.Objects.SO.SOOrder.OrderDiscTotal : Edm.Decimal "Discount Total"
PX.Objects.SO.SOOrder.CuryOrderTotal : Edm.Decimal [required] "Order Total"
PX.Objects.SO.SOOrder.OrderTotal : Edm.Decimal [required]
PX.Objects.SO.SOOrder.CuryLineTotal : Edm.Decimal [required] "Line Total"
PX.Objects.SO.SOOrder.LineTotal : Edm.Decimal [required]
PX.Objects.SO.SOOrder.CuryVatExemptTotal : Edm.Decimal [required] "Tax Exempt Total"
PX.Objects.SO.SOOrder.VatExemptTotal : Edm.Decimal [required]
PX.Objects.SO.SOOrder.CuryVatTaxableTotal : Edm.Decimal [required] "Taxable Total"
PX.Objects.SO.SOOrder.VatTaxableTotal : Edm.Decimal [required]
PX.Objects.SO.SOOrder.CuryTaxTotal : Edm.Decimal [required] "Tax Total"
PX.Objects.SO.SOOrder.TaxTotal : Edm.Decimal [required]
PX.Objects.SO.SOOrder.CuryInclTaxTotal : Edm.Decimal [required]
PX.Objects.SO.SOOrder.InclTaxTotal : Edm.Decimal [required]
PX.Objects.SO.SOOrder.CuryPremiumFreightAmt : Edm.Decimal [required] "Premium Freight Price"
PX.Objects.SO.SOOrder.PremiumFreightAmt : Edm.Decimal
PX.Objects.SO.SOOrder.CuryFreightCost : Edm.Decimal [required] "Freight Cost"
PX.Objects.SO.SOOrder.FreightCost : Edm.Decimal
PX.Objects.SO.SOOrder.FreightCostIsValid : Edm.Boolean [required] "Freight Cost Is up-to-date"
PX.Objects.SO.SOOrder.IsPackageValid : Edm.Boolean [required]
PX.Objects.SO.SOOrder.OverrideFreightAmount : Edm.Boolean [required] "Override Freight Price"
PX.Objects.SO.SOOrder.FreightAmountSource : Edm.String "Invoice Freight Price Based On"
PX.Objects.SO.SOOrder.CuryFreightAmt : Edm.Decimal [required] "Freight Price"
PX.Objects.SO.SOOrder.FreightAmt : Edm.Decimal
PX.Objects.SO.SOOrder.CuryFreightTot : Edm.Decimal [required] "Freight Total"
PX.Objects.SO.SOOrder.FreightTot : Edm.Decimal
PX.Objects.SO.SOOrder.FreightTaxCategoryID : Edm.String "Freight Tax Category"
PX.Objects.SO.SOOrder.CuryMiscTot : Edm.Decimal [required] "Misc. Charges"
PX.Objects.SO.SOOrder.MiscTot : Edm.Decimal
PX.Objects.SO.SOOrder.CuryGoodsExtPriceTotal : Edm.Decimal [required] "Goods"
PX.Objects.SO.SOOrder.GoodsExtPriceTotal : Edm.Decimal [required]
PX.Objects.SO.SOOrder.CuryMiscExtPriceTotal : Edm.Decimal [required] "Misc. Charges"
PX.Objects.SO.SOOrder.MiscExtPriceTotal : Edm.Decimal
PX.Objects.SO.SOOrder.CuryDetailExtPriceTotal : Edm.Decimal "Detail Total"
PX.Objects.SO.SOOrder.DetailExtPriceTotal : Edm.Decimal
PX.Objects.SO.SOOrder.OrderQty : Edm.Decimal [required] "Ordered Qty."
PX.Objects.SO.SOOrder.OrderWeight : Edm.Decimal [required] "Order Weight"
PX.Objects.SO.SOOrder.OrderVolume : Edm.Decimal [required] "Order Volume"
PX.Objects.SO.SOOrder.CuryOpenOrderTotal : Edm.Decimal [required] "Unshipped Amount"
PX.Objects.SO.SOOrder.OpenOrderTotal : Edm.Decimal [required]
PX.Objects.SO.SOOrder.CuryOpenLineTotal : Edm.Decimal [required] "Unshipped Line Total"
PX.Objects.SO.SOOrder.OpenLineTotal : Edm.Decimal [required]
PX.Objects.SO.SOOrder.CuryOpenDiscTotal : Edm.Decimal [required]
PX.Objects.SO.SOOrder.OpenDiscTotal : Edm.Decimal [required]
PX.Objects.SO.SOOrder.CuryOpenTaxTotal : Edm.Decimal [required] "Unshipped Tax Total"
PX.Objects.SO.SOOrder.OpenTaxTotal : Edm.Decimal [required]
PX.Objects.SO.SOOrder.CuryOpenInclTaxTotal : Edm.Decimal [required]
PX.Objects.SO.SOOrder.OpenInclTaxTotal : Edm.Decimal [required]
PX.Objects.SO.SOOrder.OpenOrderQty : Edm.Decimal [required] "Unshipped Quantity"
PX.Objects.SO.SOOrder.CuryUnbilledOrderTotal : Edm.Decimal [required] "Unbilled Balance"
PX.Objects.SO.SOOrder.UnbilledOrderTotal : Edm.Decimal [required]
PX.Objects.SO.SOOrder.CuryUnbilledLineTotal : Edm.Decimal [required] "Unbilled Line Total"
PX.Objects.SO.SOOrder.UnbilledLineTotal : Edm.Decimal [required]
PX.Objects.SO.SOOrder.CuryUnbilledMiscTot : Edm.Decimal [required] "Unbilled Misc. Total"
PX.Objects.SO.SOOrder.UnbilledMiscTot : Edm.Decimal [required]
PX.Objects.SO.SOOrder.CuryUnbilledTaxTotal : Edm.Decimal [required] "Unbilled Tax Total"
PX.Objects.SO.SOOrder.UnbilledTaxTotal : Edm.Decimal [required]
PX.Objects.SO.SOOrder.CuryUnbilledInclTaxTotal : Edm.Decimal [required]
PX.Objects.SO.SOOrder.UnbilledInclTaxTotal : Edm.Decimal [required]
PX.Objects.SO.SOOrder.CuryUnbilledDiscTotal : Edm.Decimal [required]
PX.Objects.SO.SOOrder.UnbilledDiscTotal : Edm.Decimal [required]
PX.Objects.SO.SOOrder.CuryBilledFreightTot : Edm.Decimal [required]
PX.Objects.SO.SOOrder.BilledFreightTot : Edm.Decimal [required]
PX.Objects.SO.SOOrder.CuryUnbilledFreightTot : Edm.Decimal [required]
PX.Objects.SO.SOOrder.UnbilledFreightTot : Edm.Decimal [required]
PX.Objects.SO.SOOrder.UnbilledOrderQty : Edm.Decimal [required] "Unbilled Quantity"
PX.Objects.SO.SOOrder.CuryControlTotal : Edm.Decimal [required] "Control Total"
PX.Objects.SO.SOOrder.ControlTotal : Edm.Decimal [required]
PX.Objects.SO.SOOrder.CuryPaymentTotal : Edm.Decimal [required] "Total Paid"
PX.Objects.SO.SOOrder.PaymentTotal : Edm.Decimal [required]
PX.Objects.SO.SOOrder.OverrideTaxZone : Edm.Boolean [required] "Override Tax Zone"
PX.Objects.SO.SOOrder.TaxZoneID : Edm.String "Customer Tax Zone"
PX.Objects.SO.SOOrder.TaxCalcMode : Edm.String "Tax Calculation Mode"
PX.Objects.SO.SOOrder.ExternalTaxExemptionNumber : Edm.String "Tax Exemption Number"
PX.Objects.SO.SOOrder.AvalaraCustomerUsageType : Edm.String "Tax Exemption Type"
PX.Objects.SO.SOOrder.ShipComplete : Edm.String "Shipping Rule"
PX.Objects.SO.SOOrder.FOBPoint : Edm.String "FOB Point"
PX.Objects.SO.SOOrder.ShipVia : Edm.String "Ship Via"
PX.Objects.SO.SOOrder.WillCall : Edm.Boolean "Will Call"
PX.Objects.SO.SOOrder.PackageLineCntr : Edm.Int32 [required]
PX.Objects.SO.SOOrder.PackageWeight : Edm.Decimal [required] "Package Weight"
PX.Objects.SO.SOOrder.UseCustomerAccount : Edm.Boolean [required] "Use Customer's Account"
PX.Objects.SO.SOOrder.Resedential : Edm.Boolean "Residential Delivery"
PX.Objects.SO.SOOrder.SaturdayDelivery : Edm.Boolean "Saturday Delivery"
PX.Objects.SO.SOOrder.GroundCollect : Edm.Boolean "Ground Collect"
PX.Objects.SO.SOOrder.Insurance : Edm.Boolean "Insurance"
PX.Objects.SO.SOOrder.Priority : Edm.Int16 [required] "Priority"
PX.Objects.SO.SOOrder.SalesPersonID : Edm.Int32 "Default Salesperson"
PX.Objects.SO.SOOrder.CommnPct : Edm.Decimal [required]
PX.Objects.SO.SOOrder.TermsID : Edm.String "Terms"
PX.Objects.SO.SOOrder.DueDate : Edm.DateTimeOffset "Due Date"
PX.Objects.SO.SOOrder.DiscDate : Edm.DateTimeOffset "Cash Discount Date"
PX.Objects.SO.SOOrder.InvoiceNbr : Edm.String "Invoice Nbr."
PX.Objects.SO.SOOrder.InvoiceDate : Edm.DateTimeOffset "Invoice Date"
PX.Objects.SO.SOOrder.FinPeriodID : Edm.String "Post Period"
PX.Objects.SO.SOOrder.WorkgroupID : Edm.Int32 "Workgroup"
PX.Objects.SO.SOOrder.OwnerID : Edm.Int32 "Owner"
PX.Objects.SO.SOOrder.EmployeeID : Edm.Int32
PX.Objects.SO.SOOrder.CreatedByID : Edm.Guid "Created By"
PX.Objects.SO.SOOrder.CreatedByScreenID : Edm.String
PX.Objects.SO.SOOrder.CreatedDateTime : Edm.DateTimeOffset "Created On"
PX.Objects.SO.SOOrder.LastModifiedByID : Edm.Guid "Last Modified By"
PX.Objects.SO.SOOrder.LastModifiedByScreenID : Edm.String
PX.Objects.SO.SOOrder.LastModifiedDateTime : Edm.DateTimeOffset "Last Modified On"
PX.Objects.SO.SOOrder.GotReadyForArchiveAt : Edm.DateTimeOffset
PX.Objects.SO.SOOrder.tstamp : Edm.Binary
PX.Objects.SO.SOOrder.CuryTermsDiscAmt : Edm.Decimal
PX.Objects.SO.SOOrder.TermsDiscAmt : Edm.Decimal
PX.Objects.SO.SOOrder.ShipTermsID : Edm.String "Shipping Terms"
PX.Objects.SO.SOOrder.ShipZoneID : Edm.String "Shipping Zone"
PX.Objects.SO.SOOrder.InclCustOpenOrders : Edm.Boolean [required]
PX.Objects.SO.SOOrder.ShipmentCntr : Edm.Int32 [required]
PX.Objects.SO.SOOrder.OpenShipmentCntr : Edm.Int32 [required]
PX.Objects.SO.SOOrder.OpenSiteCntr : Edm.Int32 [required]
PX.Objects.SO.SOOrder.SiteCntr : Edm.Int32 [required]
PX.Objects.SO.SOOrder.OpenLineCntr : Edm.Int32 [required]
PX.Objects.SO.SOOrder.DestinationSiteID : Edm.Int32 "Destination Warehouse"
PX.Objects.SO.SOOrder.DestinationSiteIdErrorMessage : Edm.String
PX.Objects.SO.SOOrder.DefaultOperation : Edm.String
PX.Objects.SO.SOOrder.ActiveOperationsCntr : Edm.Int32
PX.Objects.SO.SOOrder.DefaultTranType : Edm.String
PX.Objects.SO.SOOrder.OrigOrderType : Edm.String "Orig. Order Type"
PX.Objects.SO.SOOrder.OrigOrderNbr : Edm.String "Orig. Order Nbr."
PX.Objects.SO.SOOrder.ManDisc : Edm.Decimal [required]
PX.Objects.SO.SOOrder.CuryManDisc : Edm.Decimal [required] "Manual Total"
PX.Objects.SO.SOOrder.ApprovedCredit : Edm.Boolean [required]
PX.Objects.SO.SOOrder.ApprovedCreditByPayment : Edm.Boolean [required]
PX.Objects.SO.SOOrder.ApprovedCreditAmt : Edm.Decimal [required]
PX.Objects.SO.SOOrder.PaymentMethodID : Edm.String "Payment Method"
PX.Objects.SO.SOOrder.PMInstanceID : Edm.Int32 "Card/Account Nbr."
PX.Objects.SO.SOOrder.ExtRefNbr : Edm.String "Payment Ref."
PX.Objects.SO.SOOrder.UpdateNextNumber : Edm.Boolean "Update Next Number"
PX.Objects.SO.SOOrder.CuryUnreleasedPaymentAmt : Edm.Decimal [required] "Not Released"
PX.Objects.SO.SOOrder.UnreleasedPaymentAmt : Edm.Decimal [required]
PX.Objects.SO.SOOrder.CuryCCAuthorizedAmt : Edm.Decimal [required] "Authorized"
PX.Objects.SO.SOOrder.CCAuthorizedAmt : Edm.Decimal [required]
PX.Objects.SO.SOOrder.CuryPaidAmt : Edm.Decimal [required] "Released"
PX.Objects.SO.SOOrder.PaidAmt : Edm.Decimal [required]
PX.Objects.SO.SOOrder.CuryBilledPaymentTotal : Edm.Decimal [required] "Total Transferred to Invoices"
PX.Objects.SO.SOOrder.BilledPaymentTotal : Edm.Decimal [required]
PX.Objects.SO.SOOrder.CuryTransferredToChildrenPaymentTotal : Edm.Decimal [required] "Total Transferred to Child Orders"
PX.Objects.SO.SOOrder.TransferredToChildrenPaymentTotal : Edm.Decimal [required]
PX.Objects.SO.SOOrder.CuryUnpaidBalance : Edm.Decimal [required] "Unpaid Balance"
PX.Objects.SO.SOOrder.UnpaidBalance : Edm.Decimal [required]
PX.Objects.SO.SOOrder.CuryUnrefundedBalance : Edm.Decimal [required] "Unrefunded Balance"
PX.Objects.SO.SOOrder.UnrefundedBalance : Edm.Decimal [required]
PX.Objects.SO.SOOrder.IsManualPackage : Edm.Boolean "Manual Packaging"
PX.Objects.SO.SOOrder.IsTaxValid : Edm.Boolean [required] "Tax Is Up to Date"
PX.Objects.SO.SOOrder.IsOpenTaxValid : Edm.Boolean [required]
PX.Objects.SO.SOOrder.IsUnbilledTaxValid : Edm.Boolean [required]
PX.Objects.SO.SOOrder.ExternalTaxesImportInProgress : Edm.Boolean
PX.Objects.SO.SOOrder.IsManualTaxesValid : Edm.Boolean "Tax Is Up to Date"
PX.Objects.SO.SOOrder.OrderTaxAllocated : Edm.Boolean [required]
PX.Objects.SO.SOOrder.CuryDocBal : Edm.Decimal
PX.Objects.SO.SOOrder.DocBal : Edm.Decimal
PX.Objects.SO.SOOrder.DisableAutomaticDiscountCalculation : Edm.Boolean [required] "Disable Automatic Discount Update"
PX.Objects.SO.SOOrder.DeferPriceDiscountRecalculation : Edm.Boolean "Defer Price/Discount Recalculation"
PX.Objects.SO.SOOrder.IsPriceAndDiscountsValid : Edm.Boolean "Prices and discounts are up to date."
PX.Objects.SO.SOOrder.DisableAutomaticTaxCalculation : Edm.Boolean [required] "Disable Automatic Tax Calculation"
PX.Objects.SO.SOOrder.OverridePrepayment : Edm.Boolean [required] "Override Prepayment"
PX.Objects.SO.SOOrder.PrepaymentReqPct : Edm.Decimal "Prepayment Percent"
PX.Objects.SO.SOOrder.PrepaymentReqPctToRestore : Edm.Decimal
PX.Objects.SO.SOOrder.CuryPrepaymentReqAmt : Edm.Decimal "Prepayment Amount"
PX.Objects.SO.SOOrder.PrepaymentReqAmt : Edm.Decimal
PX.Objects.SO.SOOrder.CuryPaymentOverall : Edm.Decimal [required]
PX.Objects.SO.SOOrder.PaymentOverall : Edm.Decimal
PX.Objects.SO.SOOrder.CuryUnaccountedPrepaymentAmt : Edm.Decimal [required]
PX.Objects.SO.SOOrder.UnaccountedPrepaymentAmt : Edm.Decimal
PX.Objects.SO.SOOrder.PrepaymentReqSatisfied : Edm.Boolean "Prepayment Requirements Satisfied"
PX.Objects.SO.SOOrder.ForceCompleteOrder : Edm.Boolean
PX.Objects.SO.SOOrder.PaymentsNeedValidationCntr : Edm.Int32 [required]
PX.Objects.SO.SOOrder.ArePaymentsApplicable : Edm.Boolean "ArePaymentsApplicable"
PX.Objects.SO.SOOrder.IsFullyPaid : Edm.Boolean
PX.Objects.SO.SOOrder.AllowsRequiredPrepayment : Edm.Boolean
PX.Objects.SO.SOOrder.IsIntercompany : Edm.Boolean
PX.Objects.SO.SOOrder.IntercompanyPOWithEmptyInventory : Edm.Boolean [required]
PX.Objects.SO.SOOrder.SuggestRelatedItems : Edm.Boolean
PX.Objects.SO.SOOrder.IsCreditMemoOrder : Edm.Boolean
PX.Objects.SO.SOOrder.IsRMAOrder : Edm.Boolean
PX.Objects.SO.SOOrder.IsMixedOrder : Edm.Boolean
PX.Objects.SO.SOOrder.IsTransferOrder : Edm.Boolean
PX.Objects.SO.SOOrder.IsDebitMemoOrder : Edm.Boolean
PX.Objects.SO.SOOrder.IsNoAROrder : Edm.Boolean
PX.Objects.SO.SOOrder.IsCashSaleOrder : Edm.Boolean
PX.Objects.SO.SOOrder.IsPaymentInfoEnabled : Edm.Boolean
PX.Objects.SO.SOOrder.IsUserInvoiceNumbering : Edm.Boolean
PX.Objects.SO.SOOrder.IsFreightAvailable : Edm.Boolean
PX.Objects.SO.SOOrder.IsLegacyMiscBilling : Edm.Boolean [required]
PX.Objects.SO.SOOrder.ExpireDate : Edm.DateTimeOffset "Expires On"
PX.Objects.SO.SOOrder.IsExpired : Edm.Boolean [required]
PX.Objects.SO.SOOrder.MinSchedOrderDate : Edm.DateTimeOffset "Sched. Order Date"
PX.Objects.SO.SOOrder.QtyOnOrders : Edm.Decimal [required] "Qty. on Child Orders"
PX.Objects.SO.SOOrder.BlanketOpenQty : Edm.Decimal [required] "Open Quantity"
PX.Objects.SO.SOOrder.BlanketLineCntr : Edm.Int32 [required]
PX.Objects.SO.SOOrder.BlanketSOAdjustCntr : Edm.Int32 [required]
PX.Objects.SO.SOOrder.SpecialLineCntr : Edm.Int32 [required]
PX.Objects.SO.SOOrder.NoMarginLineCntr : Edm.Int32 [required]
PX.Objects.SO.SOOrder.CuryTaxableFreightAmt : Edm.Decimal [required]
PX.Objects.SO.SOOrder.TaxableFreightAmt : Edm.Decimal [required]
PX.Objects.SO.SOOrder.CurySalesCostTotal : Edm.Decimal [required]
PX.Objects.SO.SOOrder.SalesCostTotal : Edm.Decimal [required]
PX.Objects.SO.SOOrder.CuryNetSalesTotal : Edm.Decimal [required]
PX.Objects.SO.SOOrder.NetSalesTotal : Edm.Decimal [required]
PX.Objects.SO.SOOrder.CuryMarginNetSalesTotal : Edm.Decimal [required]
PX.Objects.SO.SOOrder.MarginNetSalesTotal : Edm.Decimal [required]
PX.Objects.SO.SOOrder.CuryOrderNetSales : Edm.Decimal [required]
PX.Objects.SO.SOOrder.OrderNetSales : Edm.Decimal [required]
PX.Objects.SO.SOOrder.CuryOrderMarginNetSales : Edm.Decimal [required]
PX.Objects.SO.SOOrder.OrderMarginNetSales : Edm.Decimal [required]
PX.Objects.SO.SOOrder.CuryOrderCosts : Edm.Decimal [required]
PX.Objects.SO.SOOrder.OrderCosts : Edm.Decimal [required]
PX.Objects.SO.SOOrder.CuryMarginAmt : Edm.Decimal [required] "Est. Margin Amount"
PX.Objects.SO.SOOrder.MarginAmt : Edm.Decimal [required]
PX.Objects.SO.SOOrder.MarginPct : Edm.Decimal [required] "Est. Margin (%)"
PX.Objects.SO.SOOrder.ShowDiscountsTab : Edm.Boolean "ShowDiscountsTab"
PX.Objects.SO.SOOrder.ShowShipmentsTab : Edm.Boolean "ShowShipmentsTab"
PX.Objects.SO.SOOrder.ShowOrdersTab : Edm.Boolean "ShowOrdersTab"
PX.Objects.SO.SOOrder.ChildLineCntr : Edm.Int32 [required]
PX.Objects.SO.SOOrder.IsOrchestrationAllowed : Edm.Boolean
PX.Objects.SO.SOOrder.KeepOrchestrationStatus : Edm.Boolean
PX.Objects.SO.SOOrder.UnbilledMiscQty : Edm.Decimal [required]
PX.Objects.SO.SOOrder.IsBeingCopied : Edm.Boolean
PX.Objects.SO.SOOrder.PayLinkID : Edm.Int32
PX.Objects.SO.SOOrder.ProcessingCenterID : Edm.String "Processing Center"
PX.Objects.SO.SOOrder.DeliveryMethod : Edm.String "Link Delivery Method"
PX.Objects.SO.SOOrder.ExtCarrierPlugIn : Edm.String
PX.Objects.SO.SOOrder.ExtCarrierServiceMethod : Edm.String
PX.Objects.SO.SOOrder.FreightClass : Edm.String "Freight Class"
PX.Objects.SO.SOOrder.EndorsementService : Edm.String "Endorsement"
PX.Objects.SO.SOOrder.DeliveryConfirmation : Edm.String "Delivery Confirmation"
PX.Objects.SO.SOOrder.CuryRate : Edm.Decimal
PX.Objects.SO.SOOrder.CuryViewState : Edm.Boolean
PX.Objects.SO.SOOrder.PMProjectByProjectID -> PX.Objects.PM.PMProject
PX.Objects.SO.SOOrder.SOAddressByBillAddressID -> PX.Objects.SO.SOAddress (BillAddressID=AddressID)
PX.Objects.SO.SOOrder.SOAddressByShipAddressID -> PX.Objects.SO.SOAddress (ShipAddressID=AddressID)
PX.Objects.SO.SOOrder.SOContactByBillContactID -> PX.Objects.SO.SOContact (BillContactID=ContactID)
PX.Objects.SO.SOOrder.SOContactByShipContactID -> PX.Objects.SO.SOContact (ShipContactID=ContactID)
PX.Objects.SO.SOOrder.POOrderByIntercompanyPONbr -> PX.Objects.PO.POOrder
PX.Objects.SO.SOOrder.POOrderByIntercompanyPOType -> PX.Objects.PO.POOrder
PX.Objects.SO.SOOrder.BAccountByCustomerID -> PX.Objects.CR.BAccount (CustomerID=BAccountID)
PX.Objects.SO.SOOrder.CustomerByCustomerID -> PX.Objects.AR.Customer (CustomerID=BAccountID)
PX.Objects.SO.SOOrder.ContactByContactID -> PX.Objects.CR.Contact (ContactID=ContactID)
PX.Objects.SO.SOOrder.ContactByOwnerID -> PX.Objects.CR.Contact (OwnerID=ContactID)
PX.Objects.SO.SOOrder.SOOrderByOrigOrderNbr -> PX.Objects.SO.SOOrder (OrigOrderType=OrderType, OrigOrderNbr=OrderNbr)
PX.Objects.SO.SOOrder.SOOrderByOrigOrderType -> PX.Objects.SO.SOOrder (OrigOrderNbr=OrderNbr, OrigOrderType=OrderType)
PX.Objects.SO.SOOrder.BranchByBranchID -> PX.Objects.GL.Branch
PX.Objects.SO.SOOrder.CurrencyInfoByCuryInfoID -> PX.Objects.CM.CurrencyInfo (CuryInfoID=CuryInfoID)
PX.Objects.SO.SOOrder.UsersByCreatedByID -> PX.SM.Users (CreatedByID=PKID)
PX.Objects.SO.SOOrder.UsersByLastModifiedByID -> PX.SM.Users (LastModifiedByID=PKID)
PX.Objects.SO.SOOrder.EPCompanyTreeByWorkgroupID -> PX.TM.EPCompanyTree (WorkgroupID=WorkGroupID)
PX.Objects.SO.SOOrder.TaxCategoryByFreightTaxCategoryID -> PX.Objects.TX.TaxCategory (FreightTaxCategoryID=TaxCategoryID)
PX.Objects.SO.SOOrder.TaxZoneByTaxZoneID -> PX.Objects.TX.TaxZone (TaxZoneID=TaxZoneID)
PX.Objects.SO.SOOrder.SOOrderTypeByOrderType -> PX.Objects.SO.SOOrderType (OrderType=OrderType)
PX.Objects.SO.SOOrder.SOOrderTypeByOrigOrderType -> PX.Objects.SO.SOOrderType (OrigOrderType=OrderType)
PX.Objects.SO.SOOrder.SOOrderTypeOperationByOrderType -> PX.Objects.SO.SOOrderTypeOperation (DefaultOperation=Operation, OrderType=OrderType)
PX.Objects.SO.SOOrder.POReceiptByIntercompanyPOReturnNbr -> PX.Objects.PO.POReceipt
PX.Objects.SO.SOOrder.CarrierByShipVia -> PX.Objects.CS.Carrier (ShipVia=CarrierID)
PX.Objects.SO.SOOrder.FOBPointByFOBPoint -> PX.Objects.CS.FOBPoint (FOBPoint=FOBPointID)
PX.Objects.SO.SOOrder.ShippingZoneByShipZoneID -> PX.Objects.CS.ShippingZone (ShipZoneID=ZoneID)
PX.Objects.SO.SOOrder.ShipTermsByShipTermsID -> PX.Objects.CS.ShipTerms (ShipTermsID=ShipTermsID)
PX.Objects.SO.SOOrder.TermsByTermsID -> PX.Objects.CS.Terms (TermsID=TermsID)
PX.Objects.SO.SOOrder.INSiteByDefaultSiteID -> PX.Objects.IN.INSite
PX.Objects.SO.SOOrder.INSiteByDestinationSiteID -> PX.Objects.IN.INSite (DestinationSiteID=SiteID)
PX.Objects.SO.SOOrder.INSiteByLastSiteID -> PX.Objects.IN.INSite (LastSiteID=SiteID)
PX.Objects.SO.SOOrder.CurrencyByCuryID -> PX.Objects.CM.Currency (CuryID=CuryID)
PX.Objects.SO.SOOrder.AccountByCashAccountID -> PX.Objects.GL.Account
PX.Objects.SO.SOOrder.CashAccountByBranchID -> PX.Objects.CA.CashAccount
PX.Objects.SO.SOOrder.PaymentMethodByPaymentMethodID -> PX.Objects.CA.PaymentMethod (PaymentMethodID=PaymentMethodID)
PX.Objects.SO.SOOrder.LocationByCustomerLocationID -> PX.Objects.CR.Location (CustomerID=BAccountID)
PX.Objects.SO.SOOrder.LocationByCustomerID -> PX.Objects.CR.Location (CustomerID=BAccountID)
PX.Objects.SO.SOOrder.CustomerPaymentMethodByPMInstanceID -> PX.Objects.AR.CustomerPaymentMethod (PMInstanceID=PMInstanceID)
PX.Objects.SO.SOOrder.CustomerPaymentMethodByPaymentMethodID -> PX.Objects.AR.CustomerPaymentMethod (PMInstanceID=PMInstanceID, CustomerID=BAccountID, PaymentMethodID=PaymentMethodID)
PX.Objects.SO.SOOrder.SalesPersonBySalesPersonID -> PX.Objects.AR.SalesPerson (SalesPersonID=SalesPersonID)
PX.Objects.SO.SOOrder.SOInvoiceByInvoiceNbr -> PX.Objects.SO.SOInvoice (ARDocType=DocType, InvoiceNbr=RefNbr)
PX.Objects.SO.SOOrder.SOTaxTranCollection -> Collection(PX.Objects.SO.SOTaxTran)
PX.Objects.SO.SOOrder.SOBlanketOrderLinkCollection -> Collection(PX.Objects.SO.SOBlanketOrderLink)
PX.Objects.SO.SOOrder.SOPackageInfoCollection -> Collection(PX.Objects.SO.SOPackageInfo)
PX.Objects.SO.SOOrder.SOTaxCollection -> Collection(PX.Objects.SO.SOTax)
PX.Objects.SO.SOOrder.SOOrderCollection -> Collection(PX.Objects.SO.SOOrder)
PX.Objects.SO.SOOrder.POOrderCollection -> Collection(PX.Objects.PO.POOrder)
PX.Objects.SO.SOOrder.INTranCollection -> Collection(PX.Objects.IN.INTran)
PX.Objects.SO.SOOrder.INRegisterCollection -> Collection(PX.Objects.IN.INRegister)
PX.Objects.SO.SOOrder.ARAdjustCollection -> Collection(PX.Objects.AR.ARAdjust)
PX.Objects.SO.SOOrder.AMProdItemCollection -> Collection(PX.Objects.AM.AMProdItem)
PX.Objects.SO.SOOrder.AMFixedDemandCollection -> Collection(PX.Objects.AM.AMFixedDemand)
PX.Objects.SO.SOOrder.SOLineCollection -> Collection(PX.Objects.SO.SOLine)
PX.Objects.SO.SOOrder.FSEquipmentCollection -> Collection(PX.Objects.FS.FSEquipment)
PX.Objects.SO.SOOrder.POReceiptLineCollection -> Collection(PX.Objects.PO.POReceiptLine)
PX.Objects.SO.SOOrder.ARTranCollection -> Collection(PX.Objects.AR.ARTran)
PX.Objects.SO.SOOrder.SOAdjustCollection -> Collection(PX.Objects.SO.SOAdjust)
PX.Objects.SO.SOOrder.InvoiceSplitCollection -> Collection(PX.Objects.SO.DAC.Projections.InvoiceSplit)
PX.Objects.SO.SOOrder.CCPayLinkCollection -> Collection(PX.Objects.CC.CCPayLink)
PX.Objects.SO.SOOrder.SOFreightDetailCollection -> Collection(PX.Objects.SO.SOFreightDetail)
PX.Objects.SO.SOOrder.SOLineSplitCollection -> Collection(PX.Objects.SO.SOLineSplit)
PX.Objects.SO.SOOrder.SOOrderDiscountDetailCollection -> Collection(PX.Objects.SO.SOOrderDiscountDetail)
PX.Objects.SO.SOOrder.SOOrderShipmentCollection -> Collection(PX.Objects.SO.SOOrderShipment)
PX.Objects.SO.SOOrder.SOOrderSiteCollection -> Collection(PX.Objects.SO.SOOrderSite)
PX.Objects.SO.SOOrder.SOSalesPerTranCollection -> Collection(PX.Objects.SO.SOSalesPerTran)
PX.Objects.SO.SOOrder.SOShipLineCollection -> Collection(PX.Objects.SO.SOShipLine)
PX.Objects.SO.SOOrder.SOShipLineSplitCollection -> Collection(PX.Objects.SO.SOShipLineSplit)
PX.Objects.SO.SOOrder.SOShipmentDiscountDetailCollection -> Collection(PX.Objects.SO.SOShipmentDiscountDetail)
PX.Objects.SO.SOOrder.POReceiptCollection -> Collection(PX.Objects.PO.POReceipt)
PX.Objects.SO.SOOrder.POReceiptToShipmentLinkCollection -> Collection(PX.Objects.PO.POReceiptToShipmentLink)
PX.Objects.SO.SOOrder.INReplenishmentLineCollection -> Collection(PX.Objects.IN.INReplenishmentLine)
PX.Objects.SO.SOOrder.INTransitLineCollection -> Collection(PX.Objects.IN.INTransitLine)
PX.Objects.SO.SOOrder.RelatedItemHistoryCollection -> Collection(PX.Objects.IN.RelatedItems.RelatedItemHistory)
PX.Objects.SO.SOOrder.ARInvoiceDiscountDetailCollection -> Collection(PX.Objects.AR.ARInvoiceDiscountDetail)
PX.Objects.SO.SOOrder.ARPaymentTotalsCollection -> Collection(PX.Objects.AR.ARPaymentTotals)
PX.Objects.SO.SOOrder.SOOrderCarrierDataCollection -> Collection(PX.ExternalCarriersHelper.SOOrderCarrierData)
PX.Objects.SO.SOOrder.AMConfigurationResultsCollection -> Collection(PX.Objects.AM.AMConfigurationResults)
PX.Objects.SO.SOOrder.AMEstimateReferenceCollection -> Collection(PX.Objects.AM.AMEstimateReference)
PX.Objects.SO.SOOrder.FSEquipmentComponentCollection -> Collection(PX.Objects.FS.FSEquipmentComponent)
PX.Objects.SO.SOOrder.FSPostDetCollection -> Collection(PX.Objects.FS.FSPostDet)
PX.Objects.SO.SOOrder.FSPostInfoCollection -> Collection(PX.Objects.FS.FSPostInfo)
PX.Objects.SO.SOOrder.SchedulerWCOperationCollection -> Collection(PX.Objects.AM.SchedulerWCOperation)
PX.Objects.SO.SOOrder.SchedulerProductionOrderCollection -> Collection(PX.Objects.AM.SchedulerProductionOrder)
PX.Objects.SO.SOOrder.DropShipSOLineCollection -> Collection(PX.Objects.SO.DropShipSOLine)
PX.Objects.SO.SOOrder.RQRequisitionOrderCollection -> Collection(PX.Objects.RQ.RQRequisitionOrder)
PX.Objects.SO.SOOrder.DropShipPOLineCollection -> Collection(PX.Objects.PO.DropShipPOLine)
PX.Objects.SO.SOOrder.SOInvoiceCollection -> Collection(PX.Objects.SO.SOInvoice)
PX.Objects.SO.SOOrder.SalesAllocationCollection -> Collection(PX.Objects.SO.SalesAllocation)
PX.Objects.SO.SOOrder.SOLine2Collection -> Collection(PX.Objects.SO.SOLine2)
PX.Objects.SO.SOOrder.SOLine4Collection -> Collection(PX.Objects.SO.SOLine4)
PX.Objects.SO.SOOrder.SOMiscLine2Collection -> Collection(PX.Objects.SO.SOMiscLine2)
PX.Objects.SO.SOOrder.BlanketSOLineSplitCollection -> Collection(PX.Objects.SO.DAC.Projections.BlanketSOLineSplit)
PX.Objects.SO.SOOrder.IntercompanyReturnedGoodsInTransitResultCollection -> Collection(PX.Objects.IN.IntercompanyReturnedGoodsInTransitResult)
PX.Objects.SO.SOOrder.ExternalTransactionCollection -> Collection(PX.Objects.AR.ExternalTransaction)
PX.Objects.SO.SOOrder.SOOrderRisksCollection -> Collection(PX.Commerce.Objects.SOOrderRisks)
PX.Objects.SO.SOOrder.AMConfigurationKeysCollection -> Collection(PX.Objects.AM.AMConfigurationKeys)
PX.Objects.SO.SOOrder.SchedulerMachineOperationCollection -> Collection(PX.Objects.AM.SchedulerMachineOperation)

# PX.Objects.SO.SOOrderDiscountDetail (EntityType)

Label: "Sales Order Discount Detail"
Key: OrderNbr, OrderType, RecordID
Entity sets: PX_Objects_SO_SOOrderDiscountDetail, SalesOrderDiscountDetail, SOOrderDiscountDetail
Non-filterable, non-selectable: IsOrigDocDiscount, CuryID, CuryRate, CuryViewState

PX.Objects.SO.SOOrderDiscountDetail.RecordID : Edm.Int32 [key]
PX.Objects.SO.SOOrderDiscountDetail.LineNbr : Edm.Int32 "Line Nbr."
PX.Objects.SO.SOOrderDiscountDetail.SkipDiscount : Edm.Boolean [required] "Skip Discount"
PX.Objects.SO.SOOrderDiscountDetail.OrderType : Edm.String [key] "Order Type"
PX.Objects.SO.SOOrderDiscountDetail.OrderNbr : Edm.String [key] "Order Nbr."
PX.Objects.SO.SOOrderDiscountDetail.DiscountID : Edm.String "Discount Code"
PX.Objects.SO.SOOrderDiscountDetail.DiscountSequenceID : Edm.String "Sequence ID"
PX.Objects.SO.SOOrderDiscountDetail.Type : Edm.String "Type"
PX.Objects.SO.SOOrderDiscountDetail.ManualOrder : Edm.Int16 "Line Nbr."
PX.Objects.SO.SOOrderDiscountDetail.CuryInfoID : Edm.Int64
PX.Objects.SO.SOOrderDiscountDetail.DiscountableAmt : Edm.Decimal
PX.Objects.SO.SOOrderDiscountDetail.CuryDiscountableAmt : Edm.Decimal "Discountable Amt."
PX.Objects.SO.SOOrderDiscountDetail.DiscountableQty : Edm.Decimal "Discountable Qty."
PX.Objects.SO.SOOrderDiscountDetail.DiscountAmt : Edm.Decimal [required]
PX.Objects.SO.SOOrderDiscountDetail.CuryDiscountAmt : Edm.Decimal [required] "Discount Amt."
PX.Objects.SO.SOOrderDiscountDetail.DiscountPct : Edm.Decimal "Discount Percent"
PX.Objects.SO.SOOrderDiscountDetail.FreeItemID : Edm.Int32 "Free Item"
PX.Objects.SO.SOOrderDiscountDetail.FreeItemQty : Edm.Decimal "Free Item Qty."
PX.Objects.SO.SOOrderDiscountDetail.IsManual : Edm.Boolean [required] "Manual Discount"
PX.Objects.SO.SOOrderDiscountDetail.IsOrigDocDiscount : Edm.Boolean
PX.Objects.SO.SOOrderDiscountDetail.ExtDiscCode : Edm.String "External Discount Code"
PX.Objects.SO.SOOrderDiscountDetail.Description : Edm.String "Description"
PX.Objects.SO.SOOrderDiscountDetail.tstamp : Edm.Binary
PX.Objects.SO.SOOrderDiscountDetail.CreatedByID : Edm.Guid "Created By"
PX.Objects.SO.SOOrderDiscountDetail.CreatedByScreenID : Edm.String
PX.Objects.SO.SOOrderDiscountDetail.CreatedDateTime : Edm.DateTimeOffset
PX.Objects.SO.SOOrderDiscountDetail.LastModifiedByID : Edm.Guid "Last Modified By"
PX.Objects.SO.SOOrderDiscountDetail.LastModifiedByScreenID : Edm.String
PX.Objects.SO.SOOrderDiscountDetail.LastModifiedDateTime : Edm.DateTimeOffset
PX.Objects.SO.SOOrderDiscountDetail.CuryID : Edm.String "Currency"
PX.Objects.SO.SOOrderDiscountDetail.CuryRate : Edm.Decimal
PX.Objects.SO.SOOrderDiscountDetail.CuryViewState : Edm.Boolean
PX.Objects.SO.SOOrderDiscountDetail.InventoryItemByFreeItemID -> PX.Objects.IN.InventoryItem (FreeItemID=InventoryID)
PX.Objects.SO.SOOrderDiscountDetail.SOOrderByOrderNbr -> PX.Objects.SO.SOOrder (OrderType=OrderType, OrderNbr=OrderNbr)
PX.Objects.SO.SOOrderDiscountDetail.CurrencyInfoByCuryInfoID -> PX.Objects.CM.CurrencyInfo (CuryInfoID=CuryInfoID)
PX.Objects.SO.SOOrderDiscountDetail.UsersByCreatedByID -> PX.SM.Users (CreatedByID=PKID)
PX.Objects.SO.SOOrderDiscountDetail.UsersByLastModifiedByID -> PX.SM.Users (LastModifiedByID=PKID)
PX.Objects.SO.SOOrderDiscountDetail.SOOrderTypeByOrderType -> PX.Objects.SO.SOOrderType (OrderType=OrderType)
PX.Objects.SO.SOOrderDiscountDetail.ARDiscountByDiscountID -> PX.Objects.AR.ARDiscount (DiscountID=DiscountID)
PX.Objects.SO.SOOrderDiscountDetail.DiscountSequenceByDiscountSequenceID -> PX.Objects.AR.DiscountSequence (DiscountID=DiscountID, DiscountSequenceID=DiscountSequenceID)
PX.Objects.SO.SOOrderDiscountDetail.DiscountSequenceByDiscountID -> PX.Objects.AR.DiscountSequence (DiscountSequenceID=DiscountSequenceID, DiscountID=DiscountID)

# PX.Objects.SO.SOOrderProcessSelected (EntityType)

Label: "Sales Order"
BaseType: PX.Objects.SO.SOOrder
Key: OrderNbr, OrderType (inherited from PX.Objects.SO.SOOrder)
Entity sets: PX_Objects_SO_SOOrderProcessSelected

# PX.Objects.SO.SOOrderShipment (EntityType)

Label: "Sales Order Shipment"
Key: OrderNbr, OrderType, ShippingRefNoteID
Entity sets: PX_Objects_SO_SOOrderShipment, SalesOrderShipment, SOOrderShipment
Non-filterable, non-selectable: DisplayShippingRefNoteID, HasDetailDeleted, IsPartialInvoiceConstraintViolated, HasUnhandledErrors, NoteText, BillShipmentSeparately

PX.Objects.SO.SOOrderShipment.OrderType : Edm.String [key] "Order Type"
PX.Objects.SO.SOOrderShipment.OrderNbr : Edm.String [key] "Order Nbr."
PX.Objects.SO.SOOrderShipment.Operation : Edm.String "Operation"
PX.Objects.SO.SOOrderShipment.ShippingRefNoteID : Edm.Guid [key]
PX.Objects.SO.SOOrderShipment.DisplayShippingRefNoteID : Edm.Guid "Document Nbr."
PX.Objects.SO.SOOrderShipment.ShipmentType : Edm.String "Shipment Type"
PX.Objects.SO.SOOrderShipment.ShipmentNbr : Edm.String "Shipment Nbr."
PX.Objects.SO.SOOrderShipment.CustomerID : Edm.Int32 "Customer"
PX.Objects.SO.SOOrderShipment.ShipAddressID : Edm.Int32
PX.Objects.SO.SOOrderShipment.ShipContactID : Edm.Int32
PX.Objects.SO.SOOrderShipment.LineCntr : Edm.Int32 [required]
PX.Objects.SO.SOOrderShipment.ShipDate : Edm.DateTimeOffset "Shipment Date"
PX.Objects.SO.SOOrderShipment.ProjectID : Edm.Int32
PX.Objects.SO.SOOrderShipment.Hold : Edm.Boolean [required]
PX.Objects.SO.SOOrderShipment.Confirmed : Edm.Boolean
PX.Objects.SO.SOOrderShipment.ShipComplete : Edm.String
PX.Objects.SO.SOOrderShipment.ShipmentQty : Edm.Decimal [required] "Shipped Qty."
PX.Objects.SO.SOOrderShipment.ShipmentWeight : Edm.Decimal [required] "Shipped Weight"
PX.Objects.SO.SOOrderShipment.ShipmentVolume : Edm.Decimal [required] "Shipped Volume"
PX.Objects.SO.SOOrderShipment.LineTotal : Edm.Decimal [required] "Line Total"
PX.Objects.SO.SOOrderShipment.InvoiceType : Edm.String "Invoice Type"
PX.Objects.SO.SOOrderShipment.InvoiceNbr : Edm.String "Invoice Nbr."
PX.Objects.SO.SOOrderShipment.InvoiceReleased : Edm.Boolean [required]
PX.Objects.SO.SOOrderShipment.CreateINDoc : Edm.Boolean [required]
PX.Objects.SO.SOOrderShipment.CreateARDoc : Edm.Boolean
PX.Objects.SO.SOOrderShipment.InvtDocType : Edm.String "Inventory Doc. Type"
PX.Objects.SO.SOOrderShipment.InvtRefNbr : Edm.String "Inventory Ref. Nbr."
PX.Objects.SO.SOOrderShipment.OrderFreightAllocated : Edm.Boolean [required]
PX.Objects.SO.SOOrderShipment.OrderTaxAllocated : Edm.Boolean [required]
PX.Objects.SO.SOOrderShipment.HasDetailDeleted : Edm.Boolean
PX.Objects.SO.SOOrderShipment.IsPartialInvoiceConstraintViolated : Edm.Boolean
PX.Objects.SO.SOOrderShipment.HasUnhandledErrors : Edm.Boolean
PX.Objects.SO.SOOrderShipment.ShipmentNoteID : Edm.Guid
PX.Objects.SO.SOOrderShipment.InvtNoteID : Edm.Guid
PX.Objects.SO.SOOrderShipment.OrderNoteID : Edm.Guid
PX.Objects.SO.SOOrderShipment.NoteText : Edm.String "Note Text"
PX.Objects.SO.SOOrderShipment.Canceled : Edm.Boolean [required]
PX.Objects.SO.SOOrderShipment.CreatedByID : Edm.Guid "Created By"
PX.Objects.SO.SOOrderShipment.CreatedByScreenID : Edm.String
PX.Objects.SO.SOOrderShipment.CreatedDateTime : Edm.DateTimeOffset
PX.Objects.SO.SOOrderShipment.LastModifiedByID : Edm.Guid "Last Modified By"
PX.Objects.SO.SOOrderShipment.LastModifiedByScreenID : Edm.String
PX.Objects.SO.SOOrderShipment.LastModifiedDateTime : Edm.DateTimeOffset
PX.Objects.SO.SOOrderShipment.tstamp : Edm.Binary
PX.Objects.SO.SOOrderShipment.BillShipmentSeparately : Edm.Boolean
PX.Objects.SO.SOOrderShipment.PMProjectByProjectID -> PX.Objects.PM.PMProject (ProjectID=ContractID)
PX.Objects.SO.SOOrderShipment.ARInvoiceByInvoiceNbr -> PX.Objects.AR.ARInvoice (InvoiceType=DocType, InvoiceNbr=RefNbr)
PX.Objects.SO.SOOrderShipment.SOAddressByShipAddressID -> PX.Objects.SO.SOAddress (ShipAddressID=AddressID)
PX.Objects.SO.SOOrderShipment.SOContactByShipContactID -> PX.Objects.SO.SOContact (ShipContactID=ContactID)
PX.Objects.SO.SOOrderShipment.BAccountByCustomerID -> PX.Objects.CR.BAccount (CustomerID=BAccountID)
PX.Objects.SO.SOOrderShipment.CustomerByCustomerID -> PX.Objects.AR.Customer (CustomerID=BAccountID)
PX.Objects.SO.SOOrderShipment.SOOrderByOrderNbr -> PX.Objects.SO.SOOrder (OrderType=OrderType, OrderNbr=OrderNbr)
PX.Objects.SO.SOOrderShipment.SOOrderByOrderType -> PX.Objects.SO.SOOrder (OrderNbr=OrderNbr, OrderType=OrderType)
PX.Objects.SO.SOOrderShipment.ARRegisterByInvoiceNbr -> PX.Objects.AR.ARRegister (InvoiceType=DocType, InvoiceNbr=RefNbr)
PX.Objects.SO.SOOrderShipment.UsersByCreatedByID -> PX.SM.Users (CreatedByID=PKID)
PX.Objects.SO.SOOrderShipment.UsersByLastModifiedByID -> PX.SM.Users (LastModifiedByID=PKID)
PX.Objects.SO.SOOrderShipment.SOOrderSiteBySiteID -> PX.Objects.SO.SOOrderSite (OrderType=OrderType, OrderNbr=OrderNbr)
PX.Objects.SO.SOOrderShipment.SOOrderTypeByOrderType -> PX.Objects.SO.SOOrderType (OrderType=OrderType)
PX.Objects.SO.SOOrderShipment.SOOrderTypeOperationByOperation -> PX.Objects.SO.SOOrderTypeOperation (OrderType=OrderType, Operation=Operation)
PX.Objects.SO.SOOrderShipment.SOShipmentByShipmentNbr -> PX.Objects.SO.SOShipment (ShipmentType=ShipmentType, ShipmentNbr=ShipmentNbr)
PX.Objects.SO.SOOrderShipment.SOShipmentByShipmentType -> PX.Objects.SO.SOShipment (ShipmentNbr=ShipmentNbr, ShipmentType=ShipmentType)
PX.Objects.SO.SOOrderShipment.INRegisterByInvtRefNbr -> PX.Objects.IN.INRegister (InvtDocType=DocType, InvtRefNbr=RefNbr)
PX.Objects.SO.SOOrderShipment.INRegisterByInvtDocType -> PX.Objects.IN.INRegister (InvtRefNbr=RefNbr, InvtDocType=DocType)
PX.Objects.SO.SOOrderShipment.INSiteBySiteID -> PX.Objects.IN.INSite
PX.Objects.SO.SOOrderShipment.LocationByCustomerLocationID -> PX.Objects.CR.Location (CustomerID=BAccountID)
PX.Objects.SO.SOOrderShipment.LocationByCustomerID -> PX.Objects.CR.Location (CustomerID=BAccountID)
PX.Objects.SO.SOOrderShipment.SOInvoiceByInvoiceNbr -> PX.Objects.SO.SOInvoice (InvoiceType=DocType, InvoiceNbr=RefNbr)
PX.Objects.SO.SOOrderShipment.SOInvoiceByInvoiceType -> PX.Objects.SO.SOInvoice (InvoiceNbr=RefNbr, InvoiceType=DocType)
PX.Objects.SO.SOOrderShipment.ARTranCollection -> Collection(PX.Objects.AR.ARTran)
PX.Objects.SO.SOOrderShipment.SOFreightDetailCollection -> Collection(PX.Objects.SO.SOFreightDetail)
PX.Objects.SO.SOOrderShipment.SOShipLineCollection -> Collection(PX.Objects.SO.SOShipLine)
PX.Objects.SO.SOOrderShipment.POReceiptToShipmentLinkCollection -> Collection(PX.Objects.PO.POReceiptToShipmentLink)
PX.Objects.SO.SOOrderShipment.INTranCollection -> Collection(PX.Objects.IN.INTran)

# PX.Objects.SO.SOOrderSite (EntityType)

Label: "SO Order Warehouse"
Key: OrderNbr, OrderType, SiteID
Entity sets: PX_Objects_SO_SOOrderSite, SOOrderWarehouse, SOOrderSite

PX.Objects.SO.SOOrderSite.OrderType : Edm.String [key]
PX.Objects.SO.SOOrderSite.OrderNbr : Edm.String [key]
PX.Objects.SO.SOOrderSite.SiteID : Edm.Int32 [key] "Warehouse ID"
PX.Objects.SO.SOOrderSite.LineCntr : Edm.Int32 [required]
PX.Objects.SO.SOOrderSite.OpenLineCntr : Edm.Int32 [required]
PX.Objects.SO.SOOrderSite.ShipmentCntr : Edm.Int32 [required]
PX.Objects.SO.SOOrderSite.OpenShipmentCntr : Edm.Int32 [required]
PX.Objects.SO.SOOrderSite.CreatedByID : Edm.Guid "Created By"
PX.Objects.SO.SOOrderSite.CreatedByScreenID : Edm.String
PX.Objects.SO.SOOrderSite.CreatedDateTime : Edm.DateTimeOffset
PX.Objects.SO.SOOrderSite.LastModifiedByID : Edm.Guid "Last Modified By"
PX.Objects.SO.SOOrderSite.LastModifiedByScreenID : Edm.String
PX.Objects.SO.SOOrderSite.LastModifiedDateTime : Edm.DateTimeOffset
PX.Objects.SO.SOOrderSite.tstamp : Edm.Binary
PX.Objects.SO.SOOrderSite.SOOrderByOrderNbr -> PX.Objects.SO.SOOrder (OrderType=OrderType, OrderNbr=OrderNbr)
PX.Objects.SO.SOOrderSite.UsersByCreatedByID -> PX.SM.Users (CreatedByID=PKID)
PX.Objects.SO.SOOrderSite.UsersByLastModifiedByID -> PX.SM.Users (LastModifiedByID=PKID)
PX.Objects.SO.SOOrderSite.SOOrderTypeByOrderType -> PX.Objects.SO.SOOrderType (OrderType=OrderType)
PX.Objects.SO.SOOrderSite.INSiteBySiteID -> PX.Objects.IN.INSite (SiteID=SiteID)
PX.Objects.SO.SOOrderSite.SOLineCollection -> Collection(PX.Objects.SO.SOLine)
PX.Objects.SO.SOOrderSite.SOOrderShipmentCollection -> Collection(PX.Objects.SO.SOOrderShipment)
PX.Objects.SO.SOOrderSite.SOLine4Collection -> Collection(PX.Objects.SO.SOLine4)

# PX.Objects.SO.SOOrderSiteStatusSelected (EntityType)

Label: "Sales Order Inventory Lookup Row"
Key: InventoryID
Entity sets: PX_Objects_SO_SOOrderSiteStatusSelected, SalesOrderInventoryLookupRow, SOOrderSiteStatusSelected
Non-filterable, non-selectable: CuryID, CuryInfoID, QtySelected, CuryUnitPrice, DropShipCuryUnitPrice, Rank, CuryRate, CuryViewState

PX.Objects.SO.SOOrderSiteStatusSelected.InventoryID : Edm.Int32 [key] "Inventory ID"
PX.Objects.SO.SOOrderSiteStatusSelected.InventoryCD : Edm.String "Inventory ID"
PX.Objects.SO.SOOrderSiteStatusSelected.Descr : Edm.String "Description"
PX.Objects.SO.SOOrderSiteStatusSelected.ItemClassID : Edm.Int32 "Item Class ID"
PX.Objects.SO.SOOrderSiteStatusSelected.ItemClassCD : Edm.String
PX.Objects.SO.SOOrderSiteStatusSelected.ItemClassDescription : Edm.String "Item Class Description"
PX.Objects.SO.SOOrderSiteStatusSelected.PriceClassID : Edm.String "Price Class ID"
PX.Objects.SO.SOOrderSiteStatusSelected.PriceClassDescription : Edm.String "Price Class Description"
PX.Objects.SO.SOOrderSiteStatusSelected.PreferredVendorID : Edm.Int32 "Preferred Vendor ID"
PX.Objects.SO.SOOrderSiteStatusSelected.PreferredVendorDescription : Edm.String "Preferred Vendor Name"
PX.Objects.SO.SOOrderSiteStatusSelected.BarCode : Edm.String "Barcode"
PX.Objects.SO.SOOrderSiteStatusSelected.BarCodeType : Edm.String
PX.Objects.SO.SOOrderSiteStatusSelected.BarCodeDescr : Edm.String
PX.Objects.SO.SOOrderSiteStatusSelected.AlternateID : Edm.String "Alternate ID"
PX.Objects.SO.SOOrderSiteStatusSelected.AlternateType : Edm.String "Alternate Type"
PX.Objects.SO.SOOrderSiteStatusSelected.AlternateDescr : Edm.String "Alternate Description"
PX.Objects.SO.SOOrderSiteStatusSelected.InventoryAlternateID : Edm.String
PX.Objects.SO.SOOrderSiteStatusSelected.InventoryAlternateType : Edm.String
PX.Objects.SO.SOOrderSiteStatusSelected.InventoryAlternateDescr : Edm.String
PX.Objects.SO.SOOrderSiteStatusSelected.SiteCD : Edm.String
PX.Objects.SO.SOOrderSiteStatusSelected.SubItemCD : Edm.String
PX.Objects.SO.SOOrderSiteStatusSelected.BaseUnit : Edm.String "Base Unit"
PX.Objects.SO.SOOrderSiteStatusSelected.CuryID : Edm.String "Currency"
PX.Objects.SO.SOOrderSiteStatusSelected.CuryInfoID : Edm.Int64
PX.Objects.SO.SOOrderSiteStatusSelected.SalesUnit : Edm.String "Sales Unit"
PX.Objects.SO.SOOrderSiteStatusSelected.QtySelected : Edm.Decimal "Qty. Selected"
PX.Objects.SO.SOOrderSiteStatusSelected.QtyOnHand : Edm.Decimal "Qty. On Hand"
PX.Objects.SO.SOOrderSiteStatusSelected.QtyAvail : Edm.Decimal "Qty. Available"
PX.Objects.SO.SOOrderSiteStatusSelected.QtyLast : Edm.Decimal
PX.Objects.SO.SOOrderSiteStatusSelected.BaseUnitPrice : Edm.Decimal
PX.Objects.SO.SOOrderSiteStatusSelected.CuryUnitPrice : Edm.Decimal "Last Unit Price"
PX.Objects.SO.SOOrderSiteStatusSelected.QtyAvailSale : Edm.Decimal "Qty. Available"
PX.Objects.SO.SOOrderSiteStatusSelected.QtyOnHandSale : Edm.Decimal "Qty. On Hand"
PX.Objects.SO.SOOrderSiteStatusSelected.QtyLastSale : Edm.Decimal "Qty. Last Sales"
PX.Objects.SO.SOOrderSiteStatusSelected.LastSalesDate : Edm.DateTimeOffset "Last Sales Date"
PX.Objects.SO.SOOrderSiteStatusSelected.DropShipLastBaseQty : Edm.Decimal
PX.Objects.SO.SOOrderSiteStatusSelected.DropShipLastQty : Edm.Decimal "Qty. of Last Drop Ship"
PX.Objects.SO.SOOrderSiteStatusSelected.DropShipLastUnitPrice : Edm.Decimal
PX.Objects.SO.SOOrderSiteStatusSelected.DropShipCuryUnitPrice : Edm.Decimal "Unit Price of Last Drop Ship"
PX.Objects.SO.SOOrderSiteStatusSelected.DropShipLastDate : Edm.DateTimeOffset "Date of Last Drop Ship"
PX.Objects.SO.SOOrderSiteStatusSelected.NoteID : Edm.Guid
PX.Objects.SO.SOOrderSiteStatusSelected.ItemStatus : Edm.String
PX.Objects.SO.SOOrderSiteStatusSelected.Rank : Edm.Int32
PX.Objects.SO.SOOrderSiteStatusSelected.CombinedSearchString : Edm.String
PX.Objects.SO.SOOrderSiteStatusSelected.CuryRate : Edm.Decimal
PX.Objects.SO.SOOrderSiteStatusSelected.CuryViewState : Edm.Boolean
PX.Objects.SO.SOOrderSiteStatusSelected.INItemClassByItemClassID -> PX.Objects.IN.INItemClass (ItemClassID=ItemClassID)
PX.Objects.SO.SOOrderSiteStatusSelected.INPriceClassByPriceClassID -> PX.Objects.IN.INPriceClass (PriceClassID=PriceClassID)
PX.Objects.SO.SOOrderSiteStatusSelected.CSAnswersByNoteID -> PX.Objects.CS.CSAnswers (NoteID=RefNoteID)
PX.Objects.SO.SOOrderSiteStatusSelected.POFixedDemandCollection -> Collection(PX.Objects.PO.POFixedDemand)

# PX.Objects.SO.SOOrderType (EntityType)

Label: "Order Type"
Key: OrderType
Entity sets: PX_Objects_SO_SOOrderType, OrderType1, SOOrderType
Non-filterable, non-selectable: UserInvoiceNumbering, NoteText

PX.Objects.SO.SOOrderType.OrderType : Edm.String [key] "Order Type"
PX.Objects.SO.SOOrderType.Active : Edm.Boolean [required] "Active"
PX.Objects.SO.SOOrderType.DaysToKeep : Edm.Int16 [required] "Days To Keep"
PX.Objects.SO.SOOrderType.Descr : Edm.String "Description"
PX.Objects.SO.SOOrderType.Template : Edm.String "Order Template"
PX.Objects.SO.SOOrderType.IsSystem : Edm.Boolean [required] "Is System Template"
PX.Objects.SO.SOOrderType.Behavior : Edm.String "Automation Behavior"
PX.Objects.SO.SOOrderType.DefaultOperation : Edm.String "Default Operation"
PX.Objects.SO.SOOrderType.INDocType : Edm.String "Inventory Transaction Type"
PX.Objects.SO.SOOrderType.ARDocType : Edm.String "AR Document Type"
PX.Objects.SO.SOOrderType.OrderPlanType : Edm.String "Order Plan Type"
PX.Objects.SO.SOOrderType.ShipmentPlanType : Edm.String "Shipment Plan Type"
PX.Objects.SO.SOOrderType.OrderNumberingID : Edm.String "Order Numbering Sequence"
PX.Objects.SO.SOOrderType.InvoiceNumberingID : Edm.String "Invoice Numbering Sequence"
PX.Objects.SO.SOOrderType.UserInvoiceNumbering : Edm.Boolean "Manual Invoice Numbering"
PX.Objects.SO.SOOrderType.MarkInvoicePrinted : Edm.Boolean [required] "Mark as Printed"
PX.Objects.SO.SOOrderType.MarkInvoiceEmailed : Edm.Boolean [required] "Mark as Emailed"
PX.Objects.SO.SOOrderType.HoldEntry : Edm.Boolean [required] "Hold Orders on Entry"
PX.Objects.SO.SOOrderType.InvoiceHoldEntry : Edm.Boolean [required] "Hold Invoices on Entry"
PX.Objects.SO.SOOrderType.CreditHoldEntry : Edm.Boolean [required] "Hold Document on Failed Credit Check"
PX.Objects.SO.SOOrderType.RemoveCreditHoldByPayment : Edm.Boolean [required] "Remove Credit Hold on Payment Application"
PX.Objects.SO.SOOrderType.ValidateInvoicesFullPrepayment : Edm.Boolean [required] "Validate Invoices from Orders with 100% Prepayment Required"
PX.Objects.SO.SOOrderType.RequireAllocation : Edm.Boolean [required] "Require Stock Allocation"
PX.Objects.SO.SOOrderType.RequireLocation : Edm.Boolean "Require Location"
PX.Objects.SO.SOOrderType.RequireLotSerial : Edm.Boolean [required] "Require Lot/Serial Entry"
PX.Objects.SO.SOOrderType.AllowQuickProcess : Edm.Boolean [required] "Allow Quick Process"
PX.Objects.SO.SOOrderType.RequireControlTotal : Edm.Boolean [required] "Require Control Total"
PX.Objects.SO.SOOrderType.RequireShipping : Edm.Boolean [required] "Process Shipments"
PX.Objects.SO.SOOrderType.CopyLotSerialFromShipment : Edm.Boolean [required] "Copy Lot/Serial numbers from Shipment back to Sales Order"
PX.Objects.SO.SOOrderType.BillSeparately : Edm.Boolean [required] "Bill Separately"
PX.Objects.SO.SOOrderType.ShipSeparately : Edm.Boolean [required] "Ship Separately"
PX.Objects.SO.SOOrderType.SalesAcctDefault : Edm.String "Use Sales Account from"
PX.Objects.SO.SOOrderType.MiscAcctDefault : Edm.String "Use Misc. Account from"
PX.Objects.SO.SOOrderType.FreightAcctDefault : Edm.String "Use Freight Account from"
PX.Objects.SO.SOOrderType.DiscAcctDefault : Edm.String "Use Discount Account from"
PX.Objects.SO.SOOrderType.COGSAcctDefault : Edm.String "Use COGS Account from"
PX.Objects.SO.SOOrderType.UseShippedNotInvoiced : Edm.Boolean [required] "Use Shipped-Not-Invoiced Account"
PX.Objects.SO.SOOrderType.DisableAutomaticDiscountCalculation : Edm.Boolean [required] "Disable Automatic Discount Update"
PX.Objects.SO.SOOrderType.DeferPriceDiscountRecalculation : Edm.Boolean [required] "Defer Discount Recalculation"
PX.Objects.SO.SOOrderType.RecalculateDiscOnPartialShipment : Edm.Boolean [required] "Recalculate Discount On Partial Shipment"
PX.Objects.SO.SOOrderType.DisableAutomaticTaxCalculation : Edm.Boolean [required] "Disable Automatic Tax Calculation"
PX.Objects.SO.SOOrderType.ShipFullIfNegQtyAllowed : Edm.Boolean [required] "Ship in Full if Negative Quantity Is Allowed"
PX.Objects.SO.SOOrderType.CalculateFreight : Edm.Boolean [required] "Calculate Freight"
PX.Objects.SO.SOOrderType.OrderPriority : Edm.Int16
PX.Objects.SO.SOOrderType.CopyNotes : Edm.Boolean [required] "Copy Notes"
PX.Objects.SO.SOOrderType.CopyFiles : Edm.Boolean [required] "Copy Attachments"
PX.Objects.SO.SOOrderType.CopyHeaderNotesToShipment : Edm.Boolean [required] "Copy Header Notes to Shipment"
PX.Objects.SO.SOOrderType.CopyHeaderFilesToShipment : Edm.Boolean [required] "Copy Header Attachments to Shipment"
PX.Objects.SO.SOOrderType.CopyHeaderNotesToInvoice : Edm.Boolean [required] "Copy Header Notes to Invoice"
PX.Objects.SO.SOOrderType.CopyHeaderFilesToInvoice : Edm.Boolean [required] "Copy Header Attachments to Invoice"
PX.Objects.SO.SOOrderType.CopyLineNotesToShipment : Edm.Boolean [required] "Copy Line Notes To Shipment"
PX.Objects.SO.SOOrderType.CopyLineFilesToShipment : Edm.Boolean [required] "Copy Line Attachments To Shipment"
PX.Objects.SO.SOOrderType.CopyLineNotesToInvoice : Edm.Boolean [required] "Copy Line Notes To Invoice"
PX.Objects.SO.SOOrderType.CopyLineNotesToInvoiceOnlyNS : Edm.Boolean [required] "Only Non-Stock"
PX.Objects.SO.SOOrderType.CopyLineFilesToInvoice : Edm.Boolean [required] "Copy Line Attachments To Invoice"
PX.Objects.SO.SOOrderType.CopyLineFilesToInvoiceOnlyNS : Edm.Boolean [required] "Only Non-Stock"
PX.Objects.SO.SOOrderType.CopyLineNotesToChildOrder : Edm.Boolean [required] "Copy Line Notes To Child Order"
PX.Objects.SO.SOOrderType.CopyLineFilesToChildOrder : Edm.Boolean [required] "Copy Line Attachments To Child Order"
PX.Objects.SO.SOOrderType.CustomerOrderIsRequired : Edm.Boolean [required] "Require Customer Order Nbr."
PX.Objects.SO.SOOrderType.CustomerOrderValidation : Edm.String "Customer Order Nbr. Validation"
PX.Objects.SO.SOOrderType.PostLineDiscSeparately : Edm.Boolean [required] "Post Line Discounts Separately"
PX.Objects.SO.SOOrderType.AutoWriteOff : Edm.Boolean [required] "Auto Write-Off"
PX.Objects.SO.SOOrderType.NoteID : Edm.Guid
PX.Objects.SO.SOOrderType.NoteText : Edm.String "Note Text"
PX.Objects.SO.SOOrderType.CreatedByID : Edm.Guid "Created By"
PX.Objects.SO.SOOrderType.CreatedByScreenID : Edm.String
PX.Objects.SO.SOOrderType.CreatedDateTime : Edm.DateTimeOffset "Created On"
PX.Objects.SO.SOOrderType.LastModifiedByID : Edm.Guid "Last Modified By"
PX.Objects.SO.SOOrderType.LastModifiedByScreenID : Edm.String
PX.Objects.SO.SOOrderType.LastModifiedDateTime : Edm.DateTimeOffset "Last Modified On"
PX.Objects.SO.SOOrderType.tstamp : Edm.Binary
PX.Objects.SO.SOOrderType.ActiveOperationsCntr : Edm.Int32 [required]
PX.Objects.SO.SOOrderType.AllowRefundBeforeReturn : Edm.Boolean "Allow Refund Before Return"
PX.Objects.SO.SOOrderType.CanHavePayments : Edm.Boolean
PX.Objects.SO.SOOrderType.CanHaveRefunds : Edm.Boolean
PX.Objects.SO.SOOrderType.ValidateCCRefundsOrigTransactions : Edm.Boolean [required] "Validate Card Refunds Against Original Transactions"
PX.Objects.SO.SOOrderType.DfltChildOrderType : Edm.String "Default Child Order Type"
PX.Objects.SO.SOOrderType.AuthorizeRemainderAfterPartialCapture : Edm.Boolean [required] "Authorize Remainder After Partial Capture"
PX.Objects.SO.SOOrderType.UsersByCreatedByID -> PX.SM.Users (CreatedByID=PKID)
PX.Objects.SO.SOOrderType.UsersByLastModifiedByID -> PX.SM.Users (LastModifiedByID=PKID)
PX.Objects.SO.SOOrderType.SOOrderTypeByTemplate -> PX.Objects.SO.SOOrderType (Template=OrderType)
PX.Objects.SO.SOOrderType.SOOrderTypeByOrderType -> PX.Objects.SO.SOOrderType (OrderType=DfltChildOrderType)
PX.Objects.SO.SOOrderType.NumberingByOrderNumberingID -> PX.Objects.CS.Numbering (OrderNumberingID=NumberingID)
PX.Objects.SO.SOOrderType.NumberingByInvoiceNumberingID -> PX.Objects.CS.Numbering (InvoiceNumberingID=NumberingID)
PX.Objects.SO.SOOrderType.AccountByFreightAcctID -> PX.Objects.GL.Account
PX.Objects.SO.SOOrderType.AccountByDiscountAcctID -> PX.Objects.GL.Account
PX.Objects.SO.SOOrderType.AccountByShippedNotInvoicedAcctID -> PX.Objects.GL.Account
PX.Objects.SO.SOOrderType.SubByFreightSubID -> PX.Objects.GL.Sub
PX.Objects.SO.SOOrderType.SubByDiscountSubID -> PX.Objects.GL.Sub
PX.Objects.SO.SOOrderType.SubByShippedNotInvoicedSubID -> PX.Objects.GL.Sub
PX.Objects.SO.SOOrderType.INPlanTypeByOrderPlanType -> PX.Objects.IN.INPlanType (OrderPlanType=PlanType)
PX.Objects.SO.SOOrderType.INPlanTypeByShipmentPlanType -> PX.Objects.IN.INPlanType (ShipmentPlanType=PlanType)
PX.Objects.SO.SOOrderType.SOBlanketOrderLinkCollection -> Collection(PX.Objects.SO.SOBlanketOrderLink)
PX.Objects.SO.SOOrderType.SOPackageInfoCollection -> Collection(PX.Objects.SO.SOPackageInfo)
PX.Objects.SO.SOOrderType.SOTaxCollection -> Collection(PX.Objects.SO.SOTax)
PX.Objects.SO.SOOrderType.SOOrderCollection -> Collection(PX.Objects.SO.SOOrder)
PX.Objects.SO.SOOrderType.POOrderCollection -> Collection(PX.Objects.PO.POOrder)
PX.Objects.SO.SOOrderType.INTranCollection -> Collection(PX.Objects.IN.INTran)
PX.Objects.SO.SOOrderType.INRegisterCollection -> Collection(PX.Objects.IN.INRegister)
PX.Objects.SO.SOOrderType.ARAdjustCollection -> Collection(PX.Objects.AR.ARAdjust)
PX.Objects.SO.SOOrderType.AMFixedDemandCollection -> Collection(PX.Objects.AM.AMFixedDemand)
PX.Objects.SO.SOOrderType.SOLineCollection -> Collection(PX.Objects.SO.SOLine)
PX.Objects.SO.SOOrderType.FSAppointmentDetCollection -> Collection(PX.Objects.FS.FSAppointmentDet)
PX.Objects.SO.SOOrderType.FSSetupCollection -> Collection(PX.Objects.FS.FSSetup)
PX.Objects.SO.SOOrderType.AppointmentToPostCollection -> Collection(PX.Objects.FS.AppointmentToPost)
PX.Objects.SO.SOOrderType.FSSODetCollection -> Collection(PX.Objects.FS.FSSODet)
PX.Objects.SO.SOOrderType.ServiceOrderToPostCollection -> Collection(PX.Objects.FS.ServiceOrderToPost)
PX.Objects.SO.SOOrderType.SOOrderTypeCollection -> Collection(PX.Objects.SO.SOOrderType)
PX.Objects.SO.SOOrderType.ARTranCollection -> Collection(PX.Objects.AR.ARTran)
PX.Objects.SO.SOOrderType.SOAdjustCollection -> Collection(PX.Objects.SO.SOAdjust)
PX.Objects.SO.SOOrderType.SPPortalCollection -> Collection(PX.Objects.Portals.SPPortal)
PX.Objects.SO.SOOrderType.InvoiceSplitCollection -> Collection(PX.Objects.SO.DAC.Projections.InvoiceSplit)
PX.Objects.SO.SOOrderType.SOQuickProcessParametersCollection -> Collection(PX.Objects.SO.SOQuickProcessParameters)
PX.Objects.SO.SOOrderType.SOFreightDetailCollection -> Collection(PX.Objects.SO.SOFreightDetail)
PX.Objects.SO.SOOrderType.SOLineSplitCollection -> Collection(PX.Objects.SO.SOLineSplit)
PX.Objects.SO.SOOrderType.SOOrderDiscountDetailCollection -> Collection(PX.Objects.SO.SOOrderDiscountDetail)
PX.Objects.SO.SOOrderType.SOOrderShipmentCollection -> Collection(PX.Objects.SO.SOOrderShipment)
PX.Objects.SO.SOOrderType.SOOrderSiteCollection -> Collection(PX.Objects.SO.SOOrderSite)
PX.Objects.SO.SOOrderType.SOOrderTypeOperationCollection -> Collection(PX.Objects.SO.SOOrderTypeOperation)
PX.Objects.SO.SOOrderType.SOSalesPerTranCollection -> Collection(PX.Objects.SO.SOSalesPerTran)
PX.Objects.SO.SOOrderType.SOSetupCollection -> Collection(PX.Objects.SO.SOSetup)
PX.Objects.SO.SOOrderType.SOSetupApprovalCollection -> Collection(PX.Objects.SO.SOSetupApproval)
PX.Objects.SO.SOOrderType.SOSetupCrossSellExcludedOrderTypeCollection -> Collection(PX.Objects.SO.SOSetupCrossSellExcludedOrderType)
PX.Objects.SO.SOOrderType.SOShipLineCollection -> Collection(PX.Objects.SO.SOShipLine)
PX.Objects.SO.SOOrderType.SOShipLineSplitCollection -> Collection(PX.Objects.SO.SOShipLineSplit)
PX.Objects.SO.SOOrderType.SOShipmentDiscountDetailCollection -> Collection(PX.Objects.SO.SOShipmentDiscountDetail)
PX.Objects.SO.SOOrderType.RQSetupCollection -> Collection(PX.Objects.RQ.RQSetup)
PX.Objects.SO.SOOrderType.POReceiptCollection -> Collection(PX.Objects.PO.POReceipt)
PX.Objects.SO.SOOrderType.INReplenishmentLineCollection -> Collection(PX.Objects.IN.INReplenishmentLine)
PX.Objects.SO.SOOrderType.INTransitLineCollection -> Collection(PX.Objects.IN.INTransitLine)
PX.Objects.SO.SOOrderType.ARPaymentTotalsCollection -> Collection(PX.Objects.AR.ARPaymentTotals)
PX.Objects.SO.SOOrderType.BCBindingAmazonCollection -> Collection(PX.Commerce.Amazon.BCBindingAmazon)
PX.Objects.SO.SOOrderType.BCBindingExtCollection -> Collection(PX.Commerce.Objects.BCBindingExt)
PX.Objects.SO.SOOrderType.BCBindingShopifyCollection -> Collection(PX.Commerce.Shopify.BCBindingShopify)
PX.Objects.SO.SOOrderType.AMEstimateReferenceCollection -> Collection(PX.Objects.AM.AMEstimateReference)
PX.Objects.SO.SOOrderType.FSPostDetCollection -> Collection(PX.Objects.FS.FSPostDet)
PX.Objects.SO.SOOrderType.FSPostInfoCollection -> Collection(PX.Objects.FS.FSPostInfo)
PX.Objects.SO.SOOrderType.FSSrvOrdTypeCollection -> Collection(PX.Objects.FS.FSSrvOrdType)
PX.Objects.SO.SOOrderType.BlanketSOOrderSiteCollection -> Collection(PX.Objects.SO.DAC.Projections.BlanketSOOrderSite)
PX.Objects.SO.SOOrderType.SOInvoiceCollection -> Collection(PX.Objects.SO.SOInvoice)
PX.Objects.SO.SOOrderType.SOLineForDirectInvoiceCollection -> Collection(PX.Objects.SO.DAC.Projections.SOLineForDirectInvoice)
PX.Objects.SO.SOOrderType.SalesAllocationCollection -> Collection(PX.Objects.SO.SalesAllocation)
PX.Objects.SO.SOOrderType.ExternalTransactionCollection -> Collection(PX.Objects.AR.ExternalTransaction)

# PX.Objects.SO.SOOrderTypeOperation (EntityType)

Label: "SO Order Type Operation"
Key: Operation, OrderType
Entity sets: PX_Objects_SO_SOOrderTypeOperation, SOOrderTypeOperation

PX.Objects.SO.SOOrderTypeOperation.OrderType : Edm.String [key] "Order Type"
PX.Objects.SO.SOOrderTypeOperation.Operation : Edm.String [key] "Operation"
PX.Objects.SO.SOOrderTypeOperation.INDocType : Edm.String "Inventory Transaction Type"
PX.Objects.SO.SOOrderTypeOperation.OrderPlanType : Edm.String "Order Plan Type"
PX.Objects.SO.SOOrderTypeOperation.ShipmentPlanType : Edm.String "Shipment Plan Type"
PX.Objects.SO.SOOrderTypeOperation.AutoCreateIssueLine : Edm.Boolean [required] "Auto Create Issue Line"
PX.Objects.SO.SOOrderTypeOperation.Active : Edm.Boolean [required] "Active"
PX.Objects.SO.SOOrderTypeOperation.RequireReasonCode : Edm.Boolean "Require Reason Code"
PX.Objects.SO.SOOrderTypeOperation.InvtMult : Edm.Int16
PX.Objects.SO.SOOrderTypeOperation.CreatedByID : Edm.Guid "Created By"
PX.Objects.SO.SOOrderTypeOperation.CreatedByScreenID : Edm.String
PX.Objects.SO.SOOrderTypeOperation.CreatedDateTime : Edm.DateTimeOffset
PX.Objects.SO.SOOrderTypeOperation.LastModifiedByID : Edm.Guid "Last Modified By"
PX.Objects.SO.SOOrderTypeOperation.LastModifiedByScreenID : Edm.String
PX.Objects.SO.SOOrderTypeOperation.LastModifiedDateTime : Edm.DateTimeOffset
PX.Objects.SO.SOOrderTypeOperation.tstamp : Edm.Binary
PX.Objects.SO.SOOrderTypeOperation.UsersByCreatedByID -> PX.SM.Users (CreatedByID=PKID)
PX.Objects.SO.SOOrderTypeOperation.UsersByLastModifiedByID -> PX.SM.Users (LastModifiedByID=PKID)
PX.Objects.SO.SOOrderTypeOperation.SOOrderTypeByOrderType -> PX.Objects.SO.SOOrderType (OrderType=OrderType)
PX.Objects.SO.SOOrderTypeOperation.INPlanTypeByOrderPlanType -> PX.Objects.IN.INPlanType (OrderPlanType=PlanType)
PX.Objects.SO.SOOrderTypeOperation.INPlanTypeByShipmentPlanType -> PX.Objects.IN.INPlanType (ShipmentPlanType=PlanType)
PX.Objects.SO.SOOrderTypeOperation.SOOrderCollection -> Collection(PX.Objects.SO.SOOrder)
PX.Objects.SO.SOOrderTypeOperation.SOLineCollection -> Collection(PX.Objects.SO.SOLine)
PX.Objects.SO.SOOrderTypeOperation.FSSODetCollection -> Collection(PX.Objects.FS.FSSODet)
PX.Objects.SO.SOOrderTypeOperation.SOLineSplitCollection -> Collection(PX.Objects.SO.SOLineSplit)
PX.Objects.SO.SOOrderTypeOperation.SOOrderShipmentCollection -> Collection(PX.Objects.SO.SOOrderShipment)
PX.Objects.SO.SOOrderTypeOperation.SOShipLineCollection -> Collection(PX.Objects.SO.SOShipLine)
PX.Objects.SO.SOOrderTypeOperation.SOShipLineSplitCollection -> Collection(PX.Objects.SO.SOShipLineSplit)
PX.Objects.SO.SOOrderTypeOperation.FSSODetSplitCollection -> Collection(PX.Objects.FS.FSSODetSplit)
PX.Objects.SO.SOOrderTypeOperation.SOShipLineSplitForPackingCollection -> Collection(PX.Objects.SO.Report.SOShipLineSplitForPacking)

# PX.Objects.SO.SOPackageDetail (EntityType)

Label: "SO Package Detail"
Key: LineNbr, ShipmentNbr
Entity sets: PX_Objects_SO_SOPackageDetail, SOPackageDetail
Non-filterable, non-selectable: WeightUOM, NoteText, AllowOverrideDimension

PX.Objects.SO.SOPackageDetail.ShipmentNbr : Edm.String [key] "Shipment Nbr."
PX.Objects.SO.SOPackageDetail.LineNbr : Edm.Int32 [key] "Line Nbr."
PX.Objects.SO.SOPackageDetail.BoxID : Edm.String "Box ID"
PX.Objects.SO.SOPackageDetail.Weight : Edm.Decimal [required] "Weight"
PX.Objects.SO.SOPackageDetail.WeightUOM : Edm.String "UOM"
PX.Objects.SO.SOPackageDetail.InventoryID : Edm.Int32 "Inventory ID"
PX.Objects.SO.SOPackageDetail.Description : Edm.String "Description"
PX.Objects.SO.SOPackageDetail.Qty : Edm.Decimal "Qty"
PX.Objects.SO.SOPackageDetail.QtyUOM : Edm.String "Qty. UOM"
PX.Objects.SO.SOPackageDetail.TrackNumber : Edm.String "Tracking Number"
PX.Objects.SO.SOPackageDetail.TrackUrl : Edm.String "Tracking URL"
PX.Objects.SO.SOPackageDetail.TrackData : Edm.String
PX.Objects.SO.SOPackageDetail.DeclaredValue : Edm.Decimal [required] "Declared Value"
PX.Objects.SO.SOPackageDetail.COD : Edm.Decimal [required] "C.O.D. Amount"
PX.Objects.SO.SOPackageDetail.Confirmed : Edm.Boolean [required] "Confirmed"
PX.Objects.SO.SOPackageDetail.CustomRefNbr1 : Edm.String "Custom Ref. Nbr. 1"
PX.Objects.SO.SOPackageDetail.CustomRefNbr2 : Edm.String "Custom Ref. Nbr. 2"
PX.Objects.SO.SOPackageDetail.PackageType : Edm.String "Type"
PX.Objects.SO.SOPackageDetail.ReturnTrackNumber : Edm.String "Return Tracking Number"
PX.Objects.SO.SOPackageDetail.NoteID : Edm.Guid
PX.Objects.SO.SOPackageDetail.NoteText : Edm.String "Note Text"
PX.Objects.SO.SOPackageDetail.tstamp : Edm.Binary
PX.Objects.SO.SOPackageDetail.CreatedByID : Edm.Guid "Created By"
PX.Objects.SO.SOPackageDetail.CreatedByScreenID : Edm.String
PX.Objects.SO.SOPackageDetail.CreatedDateTime : Edm.DateTimeOffset
PX.Objects.SO.SOPackageDetail.LastModifiedByID : Edm.Guid "Last Modified By"
PX.Objects.SO.SOPackageDetail.LastModifiedByScreenID : Edm.String
PX.Objects.SO.SOPackageDetail.LastModifiedDateTime : Edm.DateTimeOffset
PX.Objects.SO.SOPackageDetail.AllowOverrideDimension : Edm.Boolean "Editable Dimensions"
PX.Objects.SO.SOPackageDetail.Length : Edm.Decimal "Length"
PX.Objects.SO.SOPackageDetail.Width : Edm.Decimal "Width"
PX.Objects.SO.SOPackageDetail.Height : Edm.Decimal "Height"
PX.Objects.SO.SOPackageDetail.InventoryItemByInventoryID -> PX.Objects.IN.InventoryItem (InventoryID=InventoryID)
PX.Objects.SO.SOPackageDetail.UsersByCreatedByID -> PX.SM.Users (CreatedByID=PKID)
PX.Objects.SO.SOPackageDetail.UsersByLastModifiedByID -> PX.SM.Users (LastModifiedByID=PKID)
PX.Objects.SO.SOPackageDetail.SOShipmentByShipmentNbr -> PX.Objects.SO.SOShipment (ShipmentNbr=ShipmentNbr)
PX.Objects.SO.SOPackageDetail.CSBoxByBoxID -> PX.Objects.CS.CSBox (BoxID=BoxID)
PX.Objects.SO.SOPackageDetail.SOShipLineSplitPackageCollection -> Collection(PX.Objects.SO.SOShipLineSplitPackage)

# PX.Objects.SO.SOPackageDetailEx (EntityType)

Label: "SO Package Detail"
BaseType: PX.Objects.SO.SOPackageDetail
Key: LineNbr, ShipmentNbr (inherited from PX.Objects.SO.SOPackageDetail)
Entity sets: PX_Objects_SO_SOPackageDetailEx
Non-filterable, non-selectable: NetWeight

PX.Objects.SO.SOPackageDetailEx.BoxDescription : Edm.String "Box Description"
PX.Objects.SO.SOPackageDetailEx.BoxWeight : Edm.Decimal "Box Weight"
PX.Objects.SO.SOPackageDetailEx.MaxWeight : Edm.Decimal "Max Weight"
PX.Objects.SO.SOPackageDetailEx.NetWeight : Edm.Decimal "Net Weight"
PX.Objects.SO.SOPackageDetailEx.LinearUOM : Edm.String "Linear UOM"
PX.Objects.SO.SOPackageDetailEx.StampsAddOns : Edm.String "Stamps Surcharges"
PX.Objects.SO.SOPackageDetailEx.ContentType : Edm.String "Content Type"
PX.Objects.SO.SOPackageDetailEx.ContentTypeDesc : Edm.String "Other Content Type Desc."
PX.Objects.SO.SOPackageDetailEx.LicenseNumber : Edm.String "License Number"
PX.Objects.SO.SOPackageDetailEx.CertificateNumber : Edm.String "Certificate Number"
PX.Objects.SO.SOPackageDetailEx.InvoiceNumber : Edm.String "Invoice Number"
PX.Objects.SO.SOPackageDetailEx.EELPFC : Edm.String "EEL/PFC (EasyPost)"
PX.Objects.SO.SOPackageDetailEx.NonStandardContainer : Edm.Boolean "Non-Standard Container"
PX.Objects.SO.SOPackageDetailEx.AdditionalHandling : Edm.Boolean "Additional Handling"
PX.Objects.SO.SOPackageDetailEx.SSCC : Edm.String "SSCC"

# PX.Objects.SO.SOPackageInfo (EntityType)

Label: "SO Package Info"
Key: LineNbr, OrderNbr, OrderType
Entity sets: PX_Objects_SO_SOPackageInfo, SOPackageInfo
Non-filterable, non-selectable: WeightUOM, AllowOverrideDimension

PX.Objects.SO.SOPackageInfo.OrderType : Edm.String [key]
PX.Objects.SO.SOPackageInfo.OrderNbr : Edm.String [key]
PX.Objects.SO.SOPackageInfo.LineNbr : Edm.Int32 [key] "Line Nbr."
PX.Objects.SO.SOPackageInfo.Operation : Edm.String "Operation"
PX.Objects.SO.SOPackageInfo.InventoryID : Edm.Int32 "Inventory ID"
PX.Objects.SO.SOPackageInfo.BoxID : Edm.String "Box ID"
PX.Objects.SO.SOPackageInfo.Weight : Edm.Decimal [required] "Net Weight"
PX.Objects.SO.SOPackageInfo.GrossWeight : Edm.Decimal [required] "Gross Weight"
PX.Objects.SO.SOPackageInfo.WeightUOM : Edm.String "Weight UOM"
PX.Objects.SO.SOPackageInfo.Qty : Edm.Decimal [required] "Qty"
PX.Objects.SO.SOPackageInfo.QtyUOM : Edm.String "Qty. UOM"
PX.Objects.SO.SOPackageInfo.DeclaredValue : Edm.Decimal [required] "Declared Value"
PX.Objects.SO.SOPackageInfo.COD : Edm.Boolean [required] "C.O.D."
PX.Objects.SO.SOPackageInfo.tstamp : Edm.Binary
PX.Objects.SO.SOPackageInfo.CreatedByID : Edm.Guid "Created By"
PX.Objects.SO.SOPackageInfo.CreatedByScreenID : Edm.String
PX.Objects.SO.SOPackageInfo.CreatedDateTime : Edm.DateTimeOffset
PX.Objects.SO.SOPackageInfo.LastModifiedByID : Edm.Guid "Last Modified By"
PX.Objects.SO.SOPackageInfo.LastModifiedByScreenID : Edm.String
PX.Objects.SO.SOPackageInfo.LastModifiedDateTime : Edm.DateTimeOffset
PX.Objects.SO.SOPackageInfo.AllowOverrideDimension : Edm.Boolean "Editable Dimensions"
PX.Objects.SO.SOPackageInfo.Length : Edm.Decimal "Length"
PX.Objects.SO.SOPackageInfo.Width : Edm.Decimal "Width"
PX.Objects.SO.SOPackageInfo.Height : Edm.Decimal "Height"
PX.Objects.SO.SOPackageInfo.StampsAddOns : Edm.String "Stamps Surcharges"
PX.Objects.SO.SOPackageInfo.InventoryItemByInventoryID -> PX.Objects.IN.InventoryItem (InventoryID=InventoryID)
PX.Objects.SO.SOPackageInfo.SOOrderByOrderNbr -> PX.Objects.SO.SOOrder (OrderType=OrderType, OrderNbr=OrderNbr)
PX.Objects.SO.SOPackageInfo.UsersByCreatedByID -> PX.SM.Users (CreatedByID=PKID)
PX.Objects.SO.SOPackageInfo.UsersByLastModifiedByID -> PX.SM.Users (LastModifiedByID=PKID)
PX.Objects.SO.SOPackageInfo.SOOrderTypeByOrderType -> PX.Objects.SO.SOOrderType (OrderType=OrderType)
PX.Objects.SO.SOPackageInfo.CSBoxByBoxID -> PX.Objects.CS.CSBox (BoxID=BoxID)
PX.Objects.SO.SOPackageInfo.INSiteBySiteID -> PX.Objects.IN.INSite

# PX.Objects.SO.SOPackageInfoEx (EntityType)

Label: "SO Package Info"
BaseType: PX.Objects.SO.SOPackageInfo
Key: LineNbr, OrderNbr, OrderType (inherited from PX.Objects.SO.SOPackageInfo)
Entity sets: PX_Objects_SO_SOPackageInfoEx

PX.Objects.SO.SOPackageInfoEx.Description : Edm.String "Description"
PX.Objects.SO.SOPackageInfoEx.BoxWeight : Edm.Decimal "Box Weight"
PX.Objects.SO.SOPackageInfoEx.MaxWeight : Edm.Decimal "Max Weight"
PX.Objects.SO.SOPackageInfoEx.LinearUOM : Edm.String "Linear UOM"

# PX.Objects.SO.SOPicker (EntityType)

Label: "SO Picker"
Key: PickerNbr, WorksheetNbr
Entity sets: PX_Objects_SO_SOPicker, SOPicker
Non-filterable, non-selectable: PickListNbr

PX.Objects.SO.SOPicker.WorksheetNbr : Edm.String [key] "Worksheet Nbr."
PX.Objects.SO.SOPicker.PickerNbr : Edm.Int32 [key] "Picker Nbr."
PX.Objects.SO.SOPicker.UserID : Edm.Guid "User"
PX.Objects.SO.SOPicker.CartID : Edm.Int32 "Cart ID"
PX.Objects.SO.SOPicker.NumberOfTotes : Edm.Int32 "Nbr. of Totes"
PX.Objects.SO.SOPicker.PathLength : Edm.Int32 "Path Length"
PX.Objects.SO.SOPicker.Confirmed : Edm.Boolean [required] "Confirmed"
PX.Objects.SO.SOPicker.LinesCount : Edm.Int32 [required]
PX.Objects.SO.SOPicker.RequireApprovingTotes : Edm.Boolean [required]
PX.Objects.SO.SOPicker.PickListNbr : Edm.String
PX.Objects.SO.SOPicker.tstamp : Edm.Binary
PX.Objects.SO.SOPicker.CreatedByID : Edm.Guid "Created By"
PX.Objects.SO.SOPicker.CreatedByScreenID : Edm.String "Created At"
PX.Objects.SO.SOPicker.CreatedDateTime : Edm.DateTimeOffset "Created On"
PX.Objects.SO.SOPicker.LastModifiedByID : Edm.Guid "Last Modified By"
PX.Objects.SO.SOPicker.LastModifiedByScreenID : Edm.String "Last Modified At"
PX.Objects.SO.SOPicker.LastModifiedDateTime : Edm.DateTimeOffset "Last Modified On"
PX.Objects.SO.SOPicker.UsersByUserID -> PX.SM.Users (UserID=PKID)
PX.Objects.SO.SOPicker.UsersByCreatedByID -> PX.SM.Users (CreatedByID=PKID)
PX.Objects.SO.SOPicker.UsersByLastModifiedByID -> PX.SM.Users (LastModifiedByID=PKID)
PX.Objects.SO.SOPicker.SOPickingWorksheetByWorksheetNbr -> PX.Objects.SO.SOPickingWorksheet (WorksheetNbr=WorksheetNbr)
PX.Objects.SO.SOPicker.INCartByCartID -> PX.Objects.IN.INCart (CartID=CartID)
PX.Objects.SO.SOPicker.INLocationByFirstLocationID -> PX.Objects.IN.INLocation
PX.Objects.SO.SOPicker.INLocationByLastLocationID -> PX.Objects.IN.INLocation
PX.Objects.SO.SOPicker.INLocationBySortingLocationID -> PX.Objects.IN.INLocation
PX.Objects.SO.SOPicker.INLocationBySiteID -> PX.Objects.IN.INLocation
PX.Objects.SO.SOPicker.INSiteBySiteID -> PX.Objects.IN.INSite
PX.Objects.SO.SOPicker.SOPickingJobCollection -> Collection(PX.Objects.SO.SOPickingJob)
PX.Objects.SO.SOPicker.SOPickerListEntryCollection -> Collection(PX.Objects.SO.SOPickerListEntry)
PX.Objects.SO.SOPicker.SOPickerToShipmentLinkCollection -> Collection(PX.Objects.SO.SOPickerToShipmentLink)
PX.Objects.SO.SOPicker.SOPickListEntryToCartSplitLinkCollection -> Collection(PX.Objects.SO.SOPickListEntryToCartSplitLink)
PX.Objects.SO.SOPicker.SOShipmentProcessedByUserCollection -> Collection(PX.Objects.SO.SOShipmentProcessedByUser)

# PX.Objects.SO.SOPickerListEntry (EntityType)

Label: "SO Picker List Entry"
Key: EntryNbr, PickerNbr, WorksheetNbr
Entity sets: PX_Objects_SO_SOPickerListEntry, SOPickerListEntry
Non-filterable, non-selectable: MatchingLocationID, MatchingLotSerialNbr

PX.Objects.SO.SOPickerListEntry.WorksheetNbr : Edm.String [key] "Worksheet Nbr."
PX.Objects.SO.SOPickerListEntry.PickerNbr : Edm.Int32 [key] "Picker Nbr."
PX.Objects.SO.SOPickerListEntry.EntryNbr : Edm.Int32 [key] "Entry Nbr."
PX.Objects.SO.SOPickerListEntry.ShipmentNbr : Edm.String "Shipment Nbr."
PX.Objects.SO.SOPickerListEntry.ToteID : Edm.Int32 "Tote ID"
PX.Objects.SO.SOPickerListEntry.InventoryID : Edm.Int32 "Inventory ID"
PX.Objects.SO.SOPickerListEntry.OrderLineUOM : Edm.String "UOM"
PX.Objects.SO.SOPickerListEntry.UOM : Edm.String "UOM"
PX.Objects.SO.SOPickerListEntry.Qty : Edm.Decimal [required] "Quantity"
PX.Objects.SO.SOPickerListEntry.BaseQty : Edm.Decimal
PX.Objects.SO.SOPickerListEntry.PickedQty : Edm.Decimal [required] "Picked Quantity"
PX.Objects.SO.SOPickerListEntry.BasePickedQty : Edm.Decimal
PX.Objects.SO.SOPickerListEntry.FulfilledQty : Edm.Decimal [required]
PX.Objects.SO.SOPickerListEntry.BaseFulfilledQty : Edm.Decimal
PX.Objects.SO.SOPickerListEntry.IsUnassigned : Edm.Boolean [required]
PX.Objects.SO.SOPickerListEntry.HasGeneratedLotSerialNbr : Edm.Boolean [required]
PX.Objects.SO.SOPickerListEntry.PlanID : Edm.Int64
PX.Objects.SO.SOPickerListEntry.IsAllocating : Edm.Boolean [required]
PX.Objects.SO.SOPickerListEntry.IsPreAllocated : Edm.Boolean [required]
PX.Objects.SO.SOPickerListEntry.InitialLotSerialNbr : Edm.String
PX.Objects.SO.SOPickerListEntry.AllocationChangedDateTime : Edm.DateTimeOffset
PX.Objects.SO.SOPickerListEntry.AllocationChangedUserID : Edm.Guid
PX.Objects.SO.SOPickerListEntry.MatchingLocationID : Edm.Int32
PX.Objects.SO.SOPickerListEntry.MatchingLotSerialNbr : Edm.String
PX.Objects.SO.SOPickerListEntry.UserID : Edm.Guid
PX.Objects.SO.SOPickerListEntry.tstamp : Edm.Binary
PX.Objects.SO.SOPickerListEntry.CreatedByID : Edm.Guid "Created By"
PX.Objects.SO.SOPickerListEntry.CreatedByScreenID : Edm.String "Created At"
PX.Objects.SO.SOPickerListEntry.CreatedDateTime : Edm.DateTimeOffset "Created On"
PX.Objects.SO.SOPickerListEntry.LastModifiedByID : Edm.Guid "Last Modified By"
PX.Objects.SO.SOPickerListEntry.LastModifiedByScreenID : Edm.String "Last Modified At"
PX.Objects.SO.SOPickerListEntry.LastModifiedDateTime : Edm.DateTimeOffset "Last Modified On"
PX.Objects.SO.SOPickerListEntry.InventoryItemByInventoryID -> PX.Objects.IN.InventoryItem (InventoryID=InventoryID)
PX.Objects.SO.SOPickerListEntry.UsersByUserID -> PX.SM.Users (UserID=PKID)
PX.Objects.SO.SOPickerListEntry.UsersByCreatedByID -> PX.SM.Users (CreatedByID=PKID)
PX.Objects.SO.SOPickerListEntry.UsersByLastModifiedByID -> PX.SM.Users (LastModifiedByID=PKID)
PX.Objects.SO.SOPickerListEntry.SOPickerByPickerNbr -> PX.Objects.SO.SOPicker (WorksheetNbr=WorksheetNbr, PickerNbr=PickerNbr)
PX.Objects.SO.SOPickerListEntry.SOPickingWorksheetByWorksheetNbr -> PX.Objects.SO.SOPickingWorksheet (WorksheetNbr=WorksheetNbr)
PX.Objects.SO.SOPickerListEntry.SOShipmentByShipmentNbr -> PX.Objects.SO.SOShipment (ShipmentNbr=ShipmentNbr)
PX.Objects.SO.SOPickerListEntry.INToteByToteID -> PX.Objects.IN.INTote (ToteID=ToteID)
PX.Objects.SO.SOPickerListEntry.INLocationByLocationID -> PX.Objects.IN.INLocation
PX.Objects.SO.SOPickerListEntry.INLocationByInitialLocationID -> PX.Objects.IN.INLocation
PX.Objects.SO.SOPickerListEntry.INLocationBySiteID -> PX.Objects.IN.INLocation
PX.Objects.SO.SOPickerListEntry.INSiteBySiteID -> PX.Objects.IN.INSite
PX.Objects.SO.SOPickerListEntry.INSubItemBySubItemID -> PX.Objects.IN.INSubItem
PX.Objects.SO.SOPickerListEntry.INUnitByInventoryID -> PX.Objects.IN.INUnit (OrderLineUOM=FromUnit, InventoryID=InventoryID)
PX.Objects.SO.SOPickerListEntry.INLocationStatusByLocationID -> PX.Objects.IN.INLocationStatus (InventoryID=InventoryID)
PX.Objects.SO.SOPickerListEntry.INSiteStatusBySiteID -> PX.Objects.IN.INSiteStatus (InventoryID=InventoryID)
PX.Objects.SO.SOPickerListEntry.SOPickListEntryToCartSplitLinkCollection -> Collection(PX.Objects.SO.SOPickListEntryToCartSplitLink)

# PX.Objects.SO.SOPickerToShipmentLink (EntityType)

Label: "SO Picker to Shipment Link"
Key: PickerNbr, ShipmentNbr, SiteID, ToteID, WorksheetNbr
Entity sets: PX_Objects_SO_SOPickerToShipmentLink, SOPickertoShipmentLink

PX.Objects.SO.SOPickerToShipmentLink.WorksheetNbr : Edm.String [key] "Worksheet Nbr."
PX.Objects.SO.SOPickerToShipmentLink.PickerNbr : Edm.Int32 [key] "Picker Nbr."
PX.Objects.SO.SOPickerToShipmentLink.ShipmentNbr : Edm.String [key] "Shipment Nbr."
PX.Objects.SO.SOPickerToShipmentLink.SiteID : Edm.Int32 [key] "Warehouse ID"
PX.Objects.SO.SOPickerToShipmentLink.ToteID : Edm.Int32 [key required] "Tote ID"
PX.Objects.SO.SOPickerToShipmentLink.tstamp : Edm.Binary
PX.Objects.SO.SOPickerToShipmentLink.CreatedByID : Edm.Guid "Created By"
PX.Objects.SO.SOPickerToShipmentLink.CreatedByScreenID : Edm.String "Created At"
PX.Objects.SO.SOPickerToShipmentLink.CreatedDateTime : Edm.DateTimeOffset "Created On"
PX.Objects.SO.SOPickerToShipmentLink.LastModifiedByID : Edm.Guid "Last Modified By"
PX.Objects.SO.SOPickerToShipmentLink.LastModifiedByScreenID : Edm.String "Last Modified At"
PX.Objects.SO.SOPickerToShipmentLink.LastModifiedDateTime : Edm.DateTimeOffset "Last Modified On"
PX.Objects.SO.SOPickerToShipmentLink.UsersByCreatedByID -> PX.SM.Users (CreatedByID=PKID)
PX.Objects.SO.SOPickerToShipmentLink.UsersByLastModifiedByID -> PX.SM.Users (LastModifiedByID=PKID)
PX.Objects.SO.SOPickerToShipmentLink.SOPickerByPickerNbr -> PX.Objects.SO.SOPicker (WorksheetNbr=WorksheetNbr, PickerNbr=PickerNbr)
PX.Objects.SO.SOPickerToShipmentLink.SOPickingWorksheetByWorksheetNbr -> PX.Objects.SO.SOPickingWorksheet (WorksheetNbr=WorksheetNbr)
PX.Objects.SO.SOPickerToShipmentLink.SOShipmentByShipmentNbr -> PX.Objects.SO.SOShipment (ShipmentNbr=ShipmentNbr)
PX.Objects.SO.SOPickerToShipmentLink.INToteByToteID -> PX.Objects.IN.INTote (SiteID=SiteID, ToteID=ToteID)
PX.Objects.SO.SOPickerToShipmentLink.INSiteBySiteID -> PX.Objects.IN.INSite (SiteID=SiteID)

# PX.Objects.SO.SOPickingJob (EntityType)

Label: "SO Picking Job"
BaseType: PX.Objects.IN.WMSJob
Key: JobID (inherited from PX.Objects.IN.WMSJob)
Entity sets: PX_Objects_SO_SOPickingJob, SOPickingJob
Non-filterable, non-selectable: PickListNbr

PX.Objects.SO.SOPickingJob.WorksheetNbr : Edm.String "Worksheet Nbr."
PX.Objects.SO.SOPickingJob.PickerNbr : Edm.Int32 "Picker Nbr."
PX.Objects.SO.SOPickingJob.PickingStartedAt : Edm.DateTimeOffset "Picking Started"
PX.Objects.SO.SOPickingJob.PickedAt : Edm.DateTimeOffset "Picking Finished"
PX.Objects.SO.SOPickingJob.PickListNbr : Edm.String "Pick List Nbr."
PX.Objects.SO.SOPickingJob.AutomaticShipmentConfirmation : Edm.Boolean [required] "Automatic Shipment Confirmation"
PX.Objects.SO.SOPickingJob.SOPickerByPickerNbr -> PX.Objects.SO.SOPicker (WorksheetNbr=WorksheetNbr, PickerNbr=PickerNbr)
PX.Objects.SO.SOPickingJob.SOPickingWorksheetByWorksheetNbr -> PX.Objects.SO.SOPickingWorksheet (WorksheetNbr=WorksheetNbr)
PX.Objects.SO.SOPickingJob.WMSJobByJobID -> PX.Objects.IN.WMSJob (JobID=JobID)

# PX.Objects.SO.SOPickingWorksheet (EntityType)

Label: "SO Shipment Picking Worksheet"
Key: WorksheetNbr
Entity sets: PX_Objects_SO_SOPickingWorksheet, SOShipmentPickingWorksheet, SOPickingWorksheet
Non-filterable, non-selectable: NoteText

PX.Objects.SO.SOPickingWorksheet.WorksheetNbr : Edm.String [key] "Worksheet Nbr."
PX.Objects.SO.SOPickingWorksheet.WorksheetType : Edm.String "Type"
PX.Objects.SO.SOPickingWorksheet.PickDate : Edm.DateTimeOffset "Date"
PX.Objects.SO.SOPickingWorksheet.PickStartDate : Edm.DateTimeOffset "Picking Started On"
PX.Objects.SO.SOPickingWorksheet.PickCompleteDate : Edm.DateTimeOffset "Picking Finished On"
PX.Objects.SO.SOPickingWorksheet.Status : Edm.String "Status"
PX.Objects.SO.SOPickingWorksheet.Hold : Edm.Boolean "Hold"
PX.Objects.SO.SOPickingWorksheet.Qty : Edm.Decimal [required] "Shipped Quantity"
PX.Objects.SO.SOPickingWorksheet.ShipmentWeight : Edm.Decimal [required] "Shipped Weight"
PX.Objects.SO.SOPickingWorksheet.ShipmentVolume : Edm.Decimal [required] "Shipped Volume"
PX.Objects.SO.SOPickingWorksheet.SingleShipmentNbr : Edm.String "Shipment Nbr."
PX.Objects.SO.SOPickingWorksheet.HasNonShippable : Edm.Boolean [required] "Includes Non-Shippable Documents"
PX.Objects.SO.SOPickingWorksheet.NoteID : Edm.Guid
PX.Objects.SO.SOPickingWorksheet.NoteText : Edm.String "Note Text"
PX.Objects.SO.SOPickingWorksheet.tstamp : Edm.Binary
PX.Objects.SO.SOPickingWorksheet.CreatedByID : Edm.Guid "Created By"
PX.Objects.SO.SOPickingWorksheet.CreatedByScreenID : Edm.String "Created At"
PX.Objects.SO.SOPickingWorksheet.CreatedDateTime : Edm.DateTimeOffset "Created On"
PX.Objects.SO.SOPickingWorksheet.LastModifiedByID : Edm.Guid "Last Modified By"
PX.Objects.SO.SOPickingWorksheet.LastModifiedByScreenID : Edm.String "Last Modified At"
PX.Objects.SO.SOPickingWorksheet.LastModifiedDateTime : Edm.DateTimeOffset "Last Modified On"
PX.Objects.SO.SOPickingWorksheet.UsersByCreatedByID -> PX.SM.Users (CreatedByID=PKID)
PX.Objects.SO.SOPickingWorksheet.UsersByLastModifiedByID -> PX.SM.Users (LastModifiedByID=PKID)
PX.Objects.SO.SOPickingWorksheet.SOShipmentBySingleShipmentNbr -> PX.Objects.SO.SOShipment (SingleShipmentNbr=ShipmentNbr)
PX.Objects.SO.SOPickingWorksheet.INSiteBySiteID -> PX.Objects.IN.INSite
PX.Objects.SO.SOPickingWorksheet.SOPickingJobCollection -> Collection(PX.Objects.SO.SOPickingJob)
PX.Objects.SO.SOPickingWorksheet.SOPickerCollection -> Collection(PX.Objects.SO.SOPicker)
PX.Objects.SO.SOPickingWorksheet.SOPickerListEntryCollection -> Collection(PX.Objects.SO.SOPickerListEntry)
PX.Objects.SO.SOPickingWorksheet.SOPickerToShipmentLinkCollection -> Collection(PX.Objects.SO.SOPickerToShipmentLink)
PX.Objects.SO.SOPickingWorksheet.SOPickingWorksheetLineCollection -> Collection(PX.Objects.SO.SOPickingWorksheetLine)
PX.Objects.SO.SOPickingWorksheet.SOPickingWorksheetLineSplitCollection -> Collection(PX.Objects.SO.SOPickingWorksheetLineSplit)
PX.Objects.SO.SOPickingWorksheet.SOPickingWorksheetShipmentCollection -> Collection(PX.Objects.SO.SOPickingWorksheetShipment)
PX.Objects.SO.SOPickingWorksheet.SOPickListEntryToCartSplitLinkCollection -> Collection(PX.Objects.SO.SOPickListEntryToCartSplitLink)
PX.Objects.SO.SOPickingWorksheet.SOShipmentCollection -> Collection(PX.Objects.SO.SOShipment)
PX.Objects.SO.SOPickingWorksheet.SOShipmentProcessedByUserCollection -> Collection(PX.Objects.SO.SOShipmentProcessedByUser)

# PX.Objects.SO.SOPickingWorksheetLine (EntityType)

Label: "SO Shipment Picking Worksheet Line"
Key: LineNbr, WorksheetNbr
Entity sets: PX_Objects_SO_SOPickingWorksheetLine, SOShipmentPickingWorksheetLine, SOPickingWorksheetLine

PX.Objects.SO.SOPickingWorksheetLine.WorksheetNbr : Edm.String [key] "Worksheet Nbr."
PX.Objects.SO.SOPickingWorksheetLine.LineNbr : Edm.Int32 [key] "Line Nbr."
PX.Objects.SO.SOPickingWorksheetLine.InventoryID : Edm.Int32 "Inventory ID"
PX.Objects.SO.SOPickingWorksheetLine.UOM : Edm.String "UOM"
PX.Objects.SO.SOPickingWorksheetLine.Qty : Edm.Decimal [required] "Shipped Qty."
PX.Objects.SO.SOPickingWorksheetLine.BaseQty : Edm.Decimal [required] "Base Shipped Qty."
PX.Objects.SO.SOPickingWorksheetLine.OrigOrderQty : Edm.Decimal [required] "Ordered Qty."
PX.Objects.SO.SOPickingWorksheetLine.BaseOrigOrderQty : Edm.Decimal [required]
PX.Objects.SO.SOPickingWorksheetLine.OpenOrderQty : Edm.Decimal [required] "Open Qty."
PX.Objects.SO.SOPickingWorksheetLine.UnassignedQty : Edm.Decimal [required] "Unassigned Qty."
PX.Objects.SO.SOPickingWorksheetLine.PickedQty : Edm.Decimal [required] "Picked Qty."
PX.Objects.SO.SOPickingWorksheetLine.BasePickedQty : Edm.Decimal [required]
PX.Objects.SO.SOPickingWorksheetLine.TranDesc : Edm.String "Description"
PX.Objects.SO.SOPickingWorksheetLine.tstamp : Edm.Binary
PX.Objects.SO.SOPickingWorksheetLine.CreatedByID : Edm.Guid "Created By"
PX.Objects.SO.SOPickingWorksheetLine.CreatedByScreenID : Edm.String "Created At"
PX.Objects.SO.SOPickingWorksheetLine.CreatedDateTime : Edm.DateTimeOffset "Created On"
PX.Objects.SO.SOPickingWorksheetLine.LastModifiedByID : Edm.Guid "Last Modified By"
PX.Objects.SO.SOPickingWorksheetLine.LastModifiedByScreenID : Edm.String "Last Modified At"
PX.Objects.SO.SOPickingWorksheetLine.LastModifiedDateTime : Edm.DateTimeOffset "Last Modified On"
PX.Objects.SO.SOPickingWorksheetLine.InventoryItemByInventoryID -> PX.Objects.IN.InventoryItem (InventoryID=InventoryID)
PX.Objects.SO.SOPickingWorksheetLine.UsersByCreatedByID -> PX.SM.Users (CreatedByID=PKID)
PX.Objects.SO.SOPickingWorksheetLine.UsersByLastModifiedByID -> PX.SM.Users (LastModifiedByID=PKID)
PX.Objects.SO.SOPickingWorksheetLine.SOPickingWorksheetByWorksheetNbr -> PX.Objects.SO.SOPickingWorksheet (WorksheetNbr=WorksheetNbr)
PX.Objects.SO.SOPickingWorksheetLine.INLocationByLocationID -> PX.Objects.IN.INLocation
PX.Objects.SO.SOPickingWorksheetLine.INLocationBySiteID -> PX.Objects.IN.INLocation
PX.Objects.SO.SOPickingWorksheetLine.INSiteBySiteID -> PX.Objects.IN.INSite
PX.Objects.SO.SOPickingWorksheetLine.INSubItemBySubItemID -> PX.Objects.IN.INSubItem
PX.Objects.SO.SOPickingWorksheetLine.INUnitByInventoryID -> PX.Objects.IN.INUnit (UOM=FromUnit, InventoryID=InventoryID)
PX.Objects.SO.SOPickingWorksheetLine.INLocationStatusByLocationID -> PX.Objects.IN.INLocationStatus (InventoryID=InventoryID)
PX.Objects.SO.SOPickingWorksheetLine.INSiteStatusBySiteID -> PX.Objects.IN.INSiteStatus (InventoryID=InventoryID)
PX.Objects.SO.SOPickingWorksheetLine.SOPickingWorksheetLineSplitCollection -> Collection(PX.Objects.SO.SOPickingWorksheetLineSplit)

# PX.Objects.SO.SOPickingWorksheetLineSplit (EntityType)

Label: "SO Shipment Picking Worksheet Line Split"
Key: LineNbr, SplitNbr, WorksheetNbr
Entity sets: PX_Objects_SO_SOPickingWorksheetLineSplit, SOShipmentPickingWorksheetLineSplit, SOPickingWorksheetLineSplit

PX.Objects.SO.SOPickingWorksheetLineSplit.WorksheetNbr : Edm.String [key] "Worksheet Nbr."
PX.Objects.SO.SOPickingWorksheetLineSplit.LineNbr : Edm.Int32 [key] "Line Nbr."
PX.Objects.SO.SOPickingWorksheetLineSplit.SplitNbr : Edm.Int32 [key] "Split Nbr."
PX.Objects.SO.SOPickingWorksheetLineSplit.InventoryID : Edm.Int32 "Inventory ID"
PX.Objects.SO.SOPickingWorksheetLineSplit.UOM : Edm.String "UOM"
PX.Objects.SO.SOPickingWorksheetLineSplit.Qty : Edm.Decimal [required] "Quantity"
PX.Objects.SO.SOPickingWorksheetLineSplit.BaseQty : Edm.Decimal
PX.Objects.SO.SOPickingWorksheetLineSplit.PickedQty : Edm.Decimal [required] "Picked Quantity"
PX.Objects.SO.SOPickingWorksheetLineSplit.BasePickedQty : Edm.Decimal
PX.Objects.SO.SOPickingWorksheetLineSplit.IsUnassigned : Edm.Boolean [required]
PX.Objects.SO.SOPickingWorksheetLineSplit.IsPreAllocated : Edm.Boolean [required]
PX.Objects.SO.SOPickingWorksheetLineSplit.HasGeneratedLotSerialNbr : Edm.Boolean [required]
PX.Objects.SO.SOPickingWorksheetLineSplit.tstamp : Edm.Binary
PX.Objects.SO.SOPickingWorksheetLineSplit.CreatedByID : Edm.Guid "Created By"
PX.Objects.SO.SOPickingWorksheetLineSplit.CreatedByScreenID : Edm.String "Created At"
PX.Objects.SO.SOPickingWorksheetLineSplit.CreatedDateTime : Edm.DateTimeOffset "Created On"
PX.Objects.SO.SOPickingWorksheetLineSplit.LastModifiedByID : Edm.Guid "Last Modified By"
PX.Objects.SO.SOPickingWorksheetLineSplit.LastModifiedByScreenID : Edm.String "Last Modified At"
PX.Objects.SO.SOPickingWorksheetLineSplit.LastModifiedDateTime : Edm.DateTimeOffset "Last Modified On"
PX.Objects.SO.SOPickingWorksheetLineSplit.InventoryItemByInventoryID -> PX.Objects.IN.InventoryItem (InventoryID=InventoryID)
PX.Objects.SO.SOPickingWorksheetLineSplit.UsersByCreatedByID -> PX.SM.Users (CreatedByID=PKID)
PX.Objects.SO.SOPickingWorksheetLineSplit.UsersByLastModifiedByID -> PX.SM.Users (LastModifiedByID=PKID)
PX.Objects.SO.SOPickingWorksheetLineSplit.SOPickingWorksheetByWorksheetNbr -> PX.Objects.SO.SOPickingWorksheet (WorksheetNbr=WorksheetNbr)
PX.Objects.SO.SOPickingWorksheetLineSplit.SOPickingWorksheetLineByLineNbr -> PX.Objects.SO.SOPickingWorksheetLine (WorksheetNbr=WorksheetNbr, LineNbr=LineNbr)
PX.Objects.SO.SOPickingWorksheetLineSplit.INLocationByLocationID -> PX.Objects.IN.INLocation
PX.Objects.SO.SOPickingWorksheetLineSplit.INLocationBySortingLocationID -> PX.Objects.IN.INLocation
PX.Objects.SO.SOPickingWorksheetLineSplit.INLocationBySiteID -> PX.Objects.IN.INLocation
PX.Objects.SO.SOPickingWorksheetLineSplit.INSiteBySiteID -> PX.Objects.IN.INSite
PX.Objects.SO.SOPickingWorksheetLineSplit.INSubItemBySubItemID -> PX.Objects.IN.INSubItem
PX.Objects.SO.SOPickingWorksheetLineSplit.INUnitByInventoryID -> PX.Objects.IN.INUnit (UOM=FromUnit, InventoryID=InventoryID)
PX.Objects.SO.SOPickingWorksheetLineSplit.INLocationStatusByLocationID -> PX.Objects.IN.INLocationStatus (InventoryID=InventoryID)
PX.Objects.SO.SOPickingWorksheetLineSplit.INSiteStatusBySiteID -> PX.Objects.IN.INSiteStatus (InventoryID=InventoryID)

# PX.Objects.SO.SOPickingWorksheetShipment (EntityType)

Label: "SO Shipment Picking Worksheet Link"
Key: ShipmentNbr, WorksheetNbr
Entity sets: PX_Objects_SO_SOPickingWorksheetShipment, SOShipmentPickingWorksheetLink, SOPickingWorksheetShipment

PX.Objects.SO.SOPickingWorksheetShipment.WorksheetNbr : Edm.String [key] "Worksheet Nbr."
PX.Objects.SO.SOPickingWorksheetShipment.ShipmentNbr : Edm.String [key] "Shipment Nbr."
PX.Objects.SO.SOPickingWorksheetShipment.Unlinked : Edm.Boolean "Unlinked"
PX.Objects.SO.SOPickingWorksheetShipment.Status : Edm.String "Status"
PX.Objects.SO.SOPickingWorksheetShipment.ShipmentType : Edm.String "Type"
PX.Objects.SO.SOPickingWorksheetShipment.Picked : Edm.Boolean "Picked"
PX.Objects.SO.SOPickingWorksheetShipment.IsNonShippable : Edm.Boolean "Non-Shippable"
PX.Objects.SO.SOPickingWorksheetShipment.PickedViaWorksheet : Edm.Boolean "Picked via Worksheet"
PX.Objects.SO.SOPickingWorksheetShipment.PickedQty : Edm.Decimal "Picked Qty."
PX.Objects.SO.SOPickingWorksheetShipment.ShipmentQty : Edm.Decimal "Shipped Quantity"
PX.Objects.SO.SOPickingWorksheetShipment.ShipmentWeight : Edm.Decimal "Shipped Weight"
PX.Objects.SO.SOPickingWorksheetShipment.ShipmentVolume : Edm.Decimal "Shipped Volume"
PX.Objects.SO.SOPickingWorksheetShipment.tstamp : Edm.Binary
PX.Objects.SO.SOPickingWorksheetShipment.CreatedByID : Edm.Guid "Created By"
PX.Objects.SO.SOPickingWorksheetShipment.CreatedByScreenID : Edm.String "Created At"
PX.Objects.SO.SOPickingWorksheetShipment.CreatedDateTime : Edm.DateTimeOffset "Created On"
PX.Objects.SO.SOPickingWorksheetShipment.LastModifiedByID : Edm.Guid "Last Modified By"
PX.Objects.SO.SOPickingWorksheetShipment.LastModifiedByScreenID : Edm.String "Last Modified At"
PX.Objects.SO.SOPickingWorksheetShipment.LastModifiedDateTime : Edm.DateTimeOffset "Last Modified On"
PX.Objects.SO.SOPickingWorksheetShipment.UsersByCreatedByID -> PX.SM.Users (CreatedByID=PKID)
PX.Objects.SO.SOPickingWorksheetShipment.UsersByLastModifiedByID -> PX.SM.Users (LastModifiedByID=PKID)
PX.Objects.SO.SOPickingWorksheetShipment.SOPickingWorksheetByWorksheetNbr -> PX.Objects.SO.SOPickingWorksheet (WorksheetNbr=WorksheetNbr)
PX.Objects.SO.SOPickingWorksheetShipment.SOShipmentByShipmentNbr -> PX.Objects.SO.SOShipment (ShipmentNbr=ShipmentNbr)

# PX.Objects.SO.SOPickListEntryToCartSplitLink (EntityType)

Label: "Pick List Entry To Cart Split Link"
Key: CartID, CartSplitLineNbr, EntryNbr, PickerNbr, SiteID, WorksheetNbr
Entity sets: PX_Objects_SO_SOPickListEntryToCartSplitLink, PickListEntryToCartSplitLink, SOPickListEntryToCartSplitLink

PX.Objects.SO.SOPickListEntryToCartSplitLink.WorksheetNbr : Edm.String [key]
PX.Objects.SO.SOPickListEntryToCartSplitLink.PickerNbr : Edm.Int32 [key]
PX.Objects.SO.SOPickListEntryToCartSplitLink.EntryNbr : Edm.Int32 [key]
PX.Objects.SO.SOPickListEntryToCartSplitLink.SiteID : Edm.Int32 [key] "Warehouse"
PX.Objects.SO.SOPickListEntryToCartSplitLink.CartID : Edm.Int32 [key]
PX.Objects.SO.SOPickListEntryToCartSplitLink.CartSplitLineNbr : Edm.Int32 [key]
PX.Objects.SO.SOPickListEntryToCartSplitLink.Qty : Edm.Decimal [required] "Quantity"
PX.Objects.SO.SOPickListEntryToCartSplitLink.CreatedByID : Edm.Guid "Created By"
PX.Objects.SO.SOPickListEntryToCartSplitLink.CreatedByScreenID : Edm.String
PX.Objects.SO.SOPickListEntryToCartSplitLink.CreatedDateTime : Edm.DateTimeOffset
PX.Objects.SO.SOPickListEntryToCartSplitLink.LastModifiedByID : Edm.Guid "Last Modified By"
PX.Objects.SO.SOPickListEntryToCartSplitLink.LastModifiedByScreenID : Edm.String
PX.Objects.SO.SOPickListEntryToCartSplitLink.LastModifiedDateTime : Edm.DateTimeOffset
PX.Objects.SO.SOPickListEntryToCartSplitLink.tstamp : Edm.Binary
PX.Objects.SO.SOPickListEntryToCartSplitLink.UsersByCreatedByID -> PX.SM.Users (CreatedByID=PKID)
PX.Objects.SO.SOPickListEntryToCartSplitLink.UsersByLastModifiedByID -> PX.SM.Users (LastModifiedByID=PKID)
PX.Objects.SO.SOPickListEntryToCartSplitLink.SOPickerByPickerNbr -> PX.Objects.SO.SOPicker (WorksheetNbr=WorksheetNbr, PickerNbr=PickerNbr)
PX.Objects.SO.SOPickListEntryToCartSplitLink.SOPickerListEntryByEntryNbr -> PX.Objects.SO.SOPickerListEntry (WorksheetNbr=WorksheetNbr, PickerNbr=PickerNbr, EntryNbr=EntryNbr)
PX.Objects.SO.SOPickListEntryToCartSplitLink.SOPickingWorksheetByWorksheetNbr -> PX.Objects.SO.SOPickingWorksheet (WorksheetNbr=WorksheetNbr)
PX.Objects.SO.SOPickListEntryToCartSplitLink.INCartByCartID -> PX.Objects.IN.INCart (SiteID=SiteID, CartID=CartID)
PX.Objects.SO.SOPickListEntryToCartSplitLink.INCartSplitByCartSplitLineNbr -> PX.Objects.IN.INCartSplit (SiteID=SiteID, CartID=CartID, CartSplitLineNbr=SplitLineNbr)
PX.Objects.SO.SOPickListEntryToCartSplitLink.INSiteBySiteID -> PX.Objects.IN.INSite (SiteID=SiteID)

# PX.Objects.SO.SOPickPackShipSetup (EntityType)

Label: "Pick Pack Ship Setup"
Key: BranchID
Entity sets: PX_Objects_SO_SOPickPackShipSetup, PickPackShipSetup, SOPickPackShipSetup

PX.Objects.SO.SOPickPackShipSetup.BranchID : Edm.Int32 [key] "Branch"
PX.Objects.SO.SOPickPackShipSetup.ShowPickTab : Edm.Boolean "Display the Pick Tab"
PX.Objects.SO.SOPickPackShipSetup.ShowPackTab : Edm.Boolean "Display the Pack Tab"
PX.Objects.SO.SOPickPackShipSetup.ShowShipTab : Edm.Boolean "Display the Ship Tab"
PX.Objects.SO.SOPickPackShipSetup.ShowReturningTab : Edm.Boolean "Display the Return Tab"
PX.Objects.SO.SOPickPackShipSetup.ShowScanLogTab : Edm.Boolean "Display the Scan Log Tab"
PX.Objects.SO.SOPickPackShipSetup.ExplicitLineConfirmation : Edm.Boolean "Use Explicit Line Confirmation"
PX.Objects.SO.SOPickPackShipSetup.QtyEnterMode : Edm.String "Quantity Input Mode"
PX.Objects.SO.SOPickPackShipSetup.UsePackedQtyAsShippedQty : Edm.Boolean [required] "Use Packed Quantity as Shipped Quantity"
PX.Objects.SO.SOPickPackShipSetup.ShortShipmentConfirmation : Edm.String "Short Shipment Confirmation"
PX.Objects.SO.SOPickPackShipSetup.ShipmentLocationOrdering : Edm.String "Order Shipment Lines by Location's"
PX.Objects.SO.SOPickPackShipSetup.ConfirmEachPackageWeight : Edm.Boolean [required] "Confirm Weight for Each Package"
PX.Objects.SO.SOPickPackShipSetup.ConfirmEachPackageDimensions : Edm.Boolean [required] "Confirm Dimensions for Packages with Editable Dimensions"
PX.Objects.SO.SOPickPackShipSetup.RequestLocationForEachItem : Edm.Boolean [required] "Request Location for Each Item"
PX.Objects.SO.SOPickPackShipSetup.ConfirmToteForEachItem : Edm.Boolean [required] "Confirm Tote Selection on Wave Picking"
PX.Objects.SO.SOPickPackShipSetup.AllowMultipleTotesPerShipment : Edm.Boolean [required] "Add Totes to Shipments on the Fly"
PX.Objects.SO.SOPickPackShipSetup.AllowBidirectionalPickLists : Edm.Boolean "Allow Bidirectional Pick Lists"
PX.Objects.SO.SOPickPackShipSetup.AllowPickingLocationOverride : Edm.Boolean [required] "Allow Picking Location Changes"
PX.Objects.SO.SOPickPackShipSetup.UseGuidanceInPaperlessPicking : Edm.Boolean [required] "Use Guidance in Paperless Picking"
PX.Objects.SO.SOPickPackShipSetup.PrintPickListsAndPackSlipsTogether : Edm.Boolean [required] "Print Packing Slips with Pick Lists"
PX.Objects.SO.SOPickPackShipSetup.DefaultLocationFromShipment : Edm.Boolean [required] "Use Default Location"
PX.Objects.SO.SOPickPackShipSetup.DefaultLotSerialFromShipment : Edm.Boolean [required] "Use Default Lot/Serial Nbr."
PX.Objects.SO.SOPickPackShipSetup.EnterSizeForPackages : Edm.Boolean [required] "Enter Length/Width/Height for Packages"
PX.Objects.SO.SOPickPackShipSetup.tstamp : Edm.Binary
PX.Objects.SO.SOPickPackShipSetup.CreatedByID : Edm.Guid "Created By"
PX.Objects.SO.SOPickPackShipSetup.CreatedByScreenID : Edm.String
PX.Objects.SO.SOPickPackShipSetup.CreatedDateTime : Edm.DateTimeOffset
PX.Objects.SO.SOPickPackShipSetup.LastModifiedByID : Edm.Guid "Last Modified By"
PX.Objects.SO.SOPickPackShipSetup.LastModifiedByScreenID : Edm.String
PX.Objects.SO.SOPickPackShipSetup.LastModifiedDateTime : Edm.DateTimeOffset
PX.Objects.SO.SOPickPackShipSetup.BranchByBranchID -> PX.Objects.GL.Branch (BranchID=BranchID)
PX.Objects.SO.SOPickPackShipSetup.UsersByCreatedByID -> PX.SM.Users (CreatedByID=PKID)
PX.Objects.SO.SOPickPackShipSetup.UsersByLastModifiedByID -> PX.SM.Users (LastModifiedByID=PKID)

# PX.Objects.SO.SOPickPackShipUserSetup (EntityType)

Label: "Pick Pack Ship User Setup"
Key: UserID
Entity sets: PX_Objects_SO_SOPickPackShipUserSetup, PickPackShipUserSetup, SOPickPackShipUserSetup

PX.Objects.SO.SOPickPackShipUserSetup.UserID : Edm.Guid [key] "User"
PX.Objects.SO.SOPickPackShipUserSetup.IsOverridden : Edm.Boolean [required] "Is Overridden"
PX.Objects.SO.SOPickPackShipUserSetup.DefaultLocationFromShipment : Edm.Boolean [required] "Use Default Location"
PX.Objects.SO.SOPickPackShipUserSetup.DefaultLotSerialFromShipment : Edm.Boolean [required] "Use Default Lot/Serial Nbr."
PX.Objects.SO.SOPickPackShipUserSetup.UseGuidanceInPaperlessPicking : Edm.Boolean [required] "Use Guidance in Paperless Picking"
PX.Objects.SO.SOPickPackShipUserSetup.EnterSizeForPackages : Edm.Boolean [required] "Enter Length/Width/Height for Packages"
PX.Objects.SO.SOPickPackShipUserSetup.UsersByUserID -> PX.SM.Users (UserID=PKID)
PX.Objects.SO.SOPickPackShipUserSetup.SMScaleByScaleDeviceID -> PX.SM.SMScale

# PX.Objects.SO.SOQuickProcessParameters (EntityType)

Key: OrderType
Entity sets: PX_Objects_SO_SOQuickProcessParameters
Non-filterable, non-selectable: AvailabilityStatus, GreenStatus, YellowStatus, RedStatus, AvailabilityMessage, AvailabilityStatusMessage, SkipByDateMsg, HideWhenNothingToPrint, ShipDateMode, ShipDate, Today, Tomorrow

PX.Objects.SO.SOQuickProcessParameters.OrderType : Edm.String [key]
PX.Objects.SO.SOQuickProcessParameters.CreateShipment : Edm.Boolean [required] "Create Shipment"
PX.Objects.SO.SOQuickProcessParameters.ConfirmShipment : Edm.Boolean [required] "Confirm Shipment"
PX.Objects.SO.SOQuickProcessParameters.UpdateIN : Edm.Boolean [required] "Update IN"
PX.Objects.SO.SOQuickProcessParameters.PrepareInvoiceFromShipment : Edm.Boolean [required] "Prepare Invoice"
PX.Objects.SO.SOQuickProcessParameters.PrepareInvoice : Edm.Boolean [required] "Prepare Invoice"
PX.Objects.SO.SOQuickProcessParameters.EmailInvoice : Edm.Boolean [required] "Email Invoice"
PX.Objects.SO.SOQuickProcessParameters.ReleaseInvoice : Edm.Boolean [required] "Release Invoice"
PX.Objects.SO.SOQuickProcessParameters.AutoRedirect : Edm.Boolean [required] "Open All Created Documents in New Tabs"
PX.Objects.SO.SOQuickProcessParameters.AutoDownloadReports : Edm.Boolean [required] "Download Created Printable Documents"
PX.Objects.SO.SOQuickProcessParameters.AvailabilityStatus : Edm.String
PX.Objects.SO.SOQuickProcessParameters.GreenStatus : Edm.Boolean "GreenStatus"
PX.Objects.SO.SOQuickProcessParameters.YellowStatus : Edm.Boolean "YellowStatus"
PX.Objects.SO.SOQuickProcessParameters.RedStatus : Edm.Boolean "RedStatus"
PX.Objects.SO.SOQuickProcessParameters.AvailabilityMessage : Edm.String "AvailabilityMessage"
PX.Objects.SO.SOQuickProcessParameters.AvailabilityStatusMessage : Edm.String "AvailabilityStatusMessage"
PX.Objects.SO.SOQuickProcessParameters.SkipByDateMsg : Edm.String
PX.Objects.SO.SOQuickProcessParameters.HideWhenNothingToPrint : Edm.Boolean
PX.Objects.SO.SOQuickProcessParameters.NumberOfCopies : Edm.Int32 [required] "Number of Copies"
PX.Objects.SO.SOQuickProcessParameters.PrintPickList : Edm.Boolean [required] "Print Pick List"
PX.Objects.SO.SOQuickProcessParameters.PrintLabels : Edm.Boolean [required] "Print Labels"
PX.Objects.SO.SOQuickProcessParameters.PrintConfirmation : Edm.Boolean [required] "Print Shipment Confirmation"
PX.Objects.SO.SOQuickProcessParameters.PrintInvoice : Edm.Boolean [required] "Print Invoice"
PX.Objects.SO.SOQuickProcessParameters.ShipDateMode : Edm.Int16 "Shipment Date"
PX.Objects.SO.SOQuickProcessParameters.ShipDate : Edm.DateTimeOffset "Custom Date"
PX.Objects.SO.SOQuickProcessParameters.Today : Edm.DateTimeOffset
PX.Objects.SO.SOQuickProcessParameters.Tomorrow : Edm.DateTimeOffset
PX.Objects.SO.SOQuickProcessParameters.SMPrinterByPrinterID -> PX.SM.SMPrinter
PX.Objects.SO.SOQuickProcessParameters.SOOrderTypeByOrderType -> PX.Objects.SO.SOOrderType (OrderType=OrderType)

# PX.Objects.SO.SOSalesPerTran (EntityType)

Label: "SO Salesperson Commission"
Key: OrderNbr, OrderType, SalespersonID
Entity sets: PX_Objects_SO_SOSalesPerTran, SOSalespersonCommission, SOSalesPerTran
Non-filterable, non-selectable: CuryID, CuryRate, CuryViewState

PX.Objects.SO.SOSalesPerTran.OrderType : Edm.String [key]
PX.Objects.SO.SOSalesPerTran.OrderNbr : Edm.String [key]
PX.Objects.SO.SOSalesPerTran.SalespersonID : Edm.Int32 [key] "Salesperson ID"
PX.Objects.SO.SOSalesPerTran.RefCntr : Edm.Int32 [required]
PX.Objects.SO.SOSalesPerTran.CuryInfoID : Edm.Int64
PX.Objects.SO.SOSalesPerTran.CommnPct : Edm.Decimal [required] "Commission %"
PX.Objects.SO.SOSalesPerTran.CuryCommnblAmt : Edm.Decimal [required] "Commissionable Amount"
PX.Objects.SO.SOSalesPerTran.CommnblAmt : Edm.Decimal
PX.Objects.SO.SOSalesPerTran.CuryCommnAmt : Edm.Decimal [required] "Commission Amt."
PX.Objects.SO.SOSalesPerTran.CommnAmt : Edm.Decimal
PX.Objects.SO.SOSalesPerTran.tstamp : Edm.Binary
PX.Objects.SO.SOSalesPerTran.CreatedByID : Edm.Guid "Created By"
PX.Objects.SO.SOSalesPerTran.CreatedByScreenID : Edm.String
PX.Objects.SO.SOSalesPerTran.CreatedDateTime : Edm.DateTimeOffset
PX.Objects.SO.SOSalesPerTran.LastModifiedByID : Edm.Guid "Last Modified By"
PX.Objects.SO.SOSalesPerTran.LastModifiedByScreenID : Edm.String
PX.Objects.SO.SOSalesPerTran.LastModifiedDateTime : Edm.DateTimeOffset
PX.Objects.SO.SOSalesPerTran.CuryID : Edm.String "Currency"
PX.Objects.SO.SOSalesPerTran.CuryRate : Edm.Decimal
PX.Objects.SO.SOSalesPerTran.CuryViewState : Edm.Boolean
PX.Objects.SO.SOSalesPerTran.SOOrderByOrderNbr -> PX.Objects.SO.SOOrder (OrderType=OrderType, OrderNbr=OrderNbr)
PX.Objects.SO.SOSalesPerTran.CurrencyInfoByCuryInfoID -> PX.Objects.CM.CurrencyInfo (CuryInfoID=CuryInfoID)
PX.Objects.SO.SOSalesPerTran.UsersByCreatedByID -> PX.SM.Users (CreatedByID=PKID)
PX.Objects.SO.SOSalesPerTran.UsersByLastModifiedByID -> PX.SM.Users (LastModifiedByID=PKID)
PX.Objects.SO.SOSalesPerTran.SOOrderTypeByOrderType -> PX.Objects.SO.SOOrderType (OrderType=OrderType)
PX.Objects.SO.SOSalesPerTran.SalesPersonBySalespersonID -> PX.Objects.AR.SalesPerson (SalespersonID=SalesPersonID)
PX.Objects.SO.SOSalesPerTran.SOLineCollection -> Collection(PX.Objects.SO.SOLine)

# PX.Objects.SO.SOSetup (EntityType)

Label: "Sales Orders Preferences"
Singletons: PX_Objects_SO_SOSetup, SalesOrdersPreferences, SOSetup

PX.Objects.SO.SOSetup.ShipmentNumberingID : Edm.String "Shipment Numbering Sequence"
PX.Objects.SO.SOSetup.PickingWorksheetNumberingID : Edm.String "Picking Worksheet Numbering Sequence"
PX.Objects.SO.SOSetup.HoldShipments : Edm.Boolean "Hold Shipments on Entry"
PX.Objects.SO.SOSetup.RequireShipmentTotal : Edm.Boolean "Validate Shipment Total on Confirmation"
PX.Objects.SO.SOSetup.AddAllToShipment : Edm.Boolean [required] "Add Zero Lines for Items Not in Stock"
PX.Objects.SO.SOSetup.CreateZeroShipments : Edm.Boolean [required] "Create Zero Shipments"
PX.Objects.SO.SOSetup.AutoReleaseIN : Edm.Boolean [required] "Automatically Release IN Documents"
PX.Objects.SO.SOSetup.DefaultOrderAssignmentMapID : Edm.Int32 "Default Sales Order Assignment Map"
PX.Objects.SO.SOSetup.DefaultShipmentAssignmentMapID : Edm.Int32 "Default Sales Order Shipment Assignment Map"
PX.Objects.SO.SOSetup.ProrateDiscounts : Edm.Boolean [required] "Prorate Discounts"
PX.Objects.SO.SOSetup.FreeItemShipping : Edm.String "Free Item Shipping"
PX.Objects.SO.SOSetup.FreightAllocation : Edm.String "Freight Allocation on Partial Shipping"
PX.Objects.SO.SOSetup.MinGrossProfitValidation : Edm.String "Validate Min. Markup"
PX.Objects.SO.SOSetup.UsePriceAdjustmentMultiplier : Edm.Boolean [required] "Use a Price Adjustment Multiplier"
PX.Objects.SO.SOSetup.IgnoreMinGrossProfitCustomerPrice : Edm.Boolean [required] "Specific to Customers"
PX.Objects.SO.SOSetup.IgnoreMinGrossProfitCustomerPriceClass : Edm.Boolean [required] "Specific to Customer Price Classes"
PX.Objects.SO.SOSetup.IgnoreMinGrossProfitPromotionalPrice : Edm.Boolean [required] "Specific to Promotions"
PX.Objects.SO.SOSetup.DefaultOrderType : Edm.String "Default Sales Order Type"
PX.Objects.SO.SOSetup.TransferOrderType : Edm.String "Default Transfer Order Type"
PX.Objects.SO.SOSetup.CreditCheckError : Edm.Boolean [required] "Hold Invoices on Failed Credit Check"
PX.Objects.SO.SOSetup.UseShipDateForInvoiceDate : Edm.Boolean [required] "Use Shipment Date for Invoice Date"
PX.Objects.SO.SOSetup.SalesProfitabilityForNSKits : Edm.String "Cost Calculation Basis for Non-Stock Kits"
PX.Objects.SO.SOSetup.DeferPriceDiscountRecalculation : Edm.Boolean [required] "Defer Discount Recalculation"
PX.Objects.SO.SOSetup.ShowOnlyAvailableRelatedItems : Edm.Boolean [required] "Show Only Available Items"
PX.Objects.SO.SOSetup.UseBaseUomTransferringAllocations : Edm.Boolean [required]
PX.Objects.SO.SOSetup.tstamp : Edm.Binary
PX.Objects.SO.SOSetup.CreatedByID : Edm.Guid "Created By"
PX.Objects.SO.SOSetup.CreatedByScreenID : Edm.String
PX.Objects.SO.SOSetup.CreatedDateTime : Edm.DateTimeOffset
PX.Objects.SO.SOSetup.LastModifiedByID : Edm.Guid "Last Modified By"
PX.Objects.SO.SOSetup.LastModifiedByScreenID : Edm.String
PX.Objects.SO.SOSetup.LastModifiedDateTime : Edm.DateTimeOffset
PX.Objects.SO.SOSetup.UsersByCreatedByID -> PX.SM.Users (CreatedByID=PKID)
PX.Objects.SO.SOSetup.UsersByLastModifiedByID -> PX.SM.Users (LastModifiedByID=PKID)
PX.Objects.SO.SOSetup.SOOrderTypeByDefaultOrderType -> PX.Objects.SO.SOOrderType (DefaultOrderType=OrderType)
PX.Objects.SO.SOSetup.SOOrderTypeByTransferOrderType -> PX.Objects.SO.SOOrderType (TransferOrderType=OrderType)
PX.Objects.SO.SOSetup.SOOrderTypeByDefaultReturnOrderType -> PX.Objects.SO.SOOrderType
PX.Objects.SO.SOSetup.SOOrderTypeByDfltIntercompanyOrderType -> PX.Objects.SO.SOOrderType
PX.Objects.SO.SOSetup.SOOrderTypeByDfltIntercompanyRMAType -> PX.Objects.SO.SOOrderType
PX.Objects.SO.SOSetup.NumberingByShipmentNumberingID -> PX.Objects.CS.Numbering (ShipmentNumberingID=NumberingID)
PX.Objects.SO.SOSetup.NumberingByPickingWorksheetNumberingID -> PX.Objects.CS.Numbering (PickingWorksheetNumberingID=NumberingID)
PX.Objects.SO.SOSetup.EPAssignmentMapByDefaultOrderAssignmentMapID -> PX.Objects.EP.EPAssignmentMap (DefaultOrderAssignmentMapID=AssignmentMapID)
PX.Objects.SO.SOSetup.EPAssignmentMapByDefaultShipmentAssignmentMapID -> PX.Objects.EP.EPAssignmentMap (DefaultShipmentAssignmentMapID=AssignmentMapID)

# PX.Objects.SO.SOSetupApproval (EntityType)

Label: "SO Approval"
Key: ApprovalID
Entity sets: PX_Objects_SO_SOSetupApproval, SOApproval, SOSetupApproval

PX.Objects.SO.SOSetupApproval.IsActive : Edm.Boolean [required] "Active"
PX.Objects.SO.SOSetupApproval.OrderType : Edm.String "SO Type"
PX.Objects.SO.SOSetupApproval.ApprovalID : Edm.Int32 [key]
PX.Objects.SO.SOSetupApproval.AssignmentMapID : Edm.Int32 "Approval Map"
PX.Objects.SO.SOSetupApproval.AssignmentNotificationID : Edm.Int32 "Pending Approval Notification"
PX.Objects.SO.SOSetupApproval.tstamp : Edm.Binary
PX.Objects.SO.SOSetupApproval.CreatedByID : Edm.Guid "Created By"
PX.Objects.SO.SOSetupApproval.CreatedByScreenID : Edm.String
PX.Objects.SO.SOSetupApproval.CreatedDateTime : Edm.DateTimeOffset
PX.Objects.SO.SOSetupApproval.LastModifiedByID : Edm.Guid "Last Modified By"
PX.Objects.SO.SOSetupApproval.LastModifiedByScreenID : Edm.String
PX.Objects.SO.SOSetupApproval.LastModifiedDateTime : Edm.DateTimeOffset
PX.Objects.SO.SOSetupApproval.UsersByCreatedByID -> PX.SM.Users (CreatedByID=PKID)
PX.Objects.SO.SOSetupApproval.UsersByLastModifiedByID -> PX.SM.Users (LastModifiedByID=PKID)
PX.Objects.SO.SOSetupApproval.NotificationByAssignmentNotificationID -> PX.SM.Notification (AssignmentNotificationID=NotificationID)
PX.Objects.SO.SOSetupApproval.SOOrderTypeByOrderType -> PX.Objects.SO.SOOrderType (OrderType=OrderType)
PX.Objects.SO.SOSetupApproval.EPAssignmentMapByAssignmentMapID -> PX.Objects.EP.EPAssignmentMap (AssignmentMapID=AssignmentMapID)

# PX.Objects.SO.SOSetupCrossSellExcludedItemClasses (EntityType)

Label: "SO Setup Cross Sell Excluded Item Classes"
Key: ItemClassID
Entity sets: PX_Objects_SO_SOSetupCrossSellExcludedItemClasses, SOSetupCrossSellExcludedItemClasses

PX.Objects.SO.SOSetupCrossSellExcludedItemClasses.ItemClassID : Edm.Int32 [key] "Class ID"
PX.Objects.SO.SOSetupCrossSellExcludedItemClasses.tstamp : Edm.Binary
PX.Objects.SO.SOSetupCrossSellExcludedItemClasses.CreatedByID : Edm.Guid "Created By"
PX.Objects.SO.SOSetupCrossSellExcludedItemClasses.CreatedByScreenID : Edm.String
PX.Objects.SO.SOSetupCrossSellExcludedItemClasses.CreatedDateTime : Edm.DateTimeOffset
PX.Objects.SO.SOSetupCrossSellExcludedItemClasses.UsersByCreatedByID -> PX.SM.Users (CreatedByID=PKID)
PX.Objects.SO.SOSetupCrossSellExcludedItemClasses.INItemClassByItemClassID -> PX.Objects.IN.INItemClass (ItemClassID=ItemClassID)

# PX.Objects.SO.SOSetupCrossSellExcludedOrderType (EntityType)

Label: "SO Setup Cross Sell Excluded Order Types"
Key: OrderType
Entity sets: PX_Objects_SO_SOSetupCrossSellExcludedOrderType, SOSetupCrossSellExcludedOrderTypes, SOSetupCrossSellExcludedOrderType

PX.Objects.SO.SOSetupCrossSellExcludedOrderType.OrderType : Edm.String [key] "Order Type"
PX.Objects.SO.SOSetupCrossSellExcludedOrderType.tstamp : Edm.Binary
PX.Objects.SO.SOSetupCrossSellExcludedOrderType.CreatedByID : Edm.Guid "Created By"
PX.Objects.SO.SOSetupCrossSellExcludedOrderType.CreatedByScreenID : Edm.String
PX.Objects.SO.SOSetupCrossSellExcludedOrderType.CreatedDateTime : Edm.DateTimeOffset
PX.Objects.SO.SOSetupCrossSellExcludedOrderType.UsersByCreatedByID -> PX.SM.Users (CreatedByID=PKID)
PX.Objects.SO.SOSetupCrossSellExcludedOrderType.SOOrderTypeByOrderType -> PX.Objects.SO.SOOrderType (OrderType=OrderType)

# PX.Objects.SO.SOSetupInvoiceApproval (EntityType)

Label: "SO Invoice Approval"
Key: ApprovalID
Entity sets: PX_Objects_SO_SOSetupInvoiceApproval, SOInvoiceApproval, SOSetupInvoiceApproval

PX.Objects.SO.SOSetupInvoiceApproval.DocType : Edm.String "Type"
PX.Objects.SO.SOSetupInvoiceApproval.IsActive : Edm.Boolean [required] "Active"
PX.Objects.SO.SOSetupInvoiceApproval.ApprovalID : Edm.Int32 [key]
PX.Objects.SO.SOSetupInvoiceApproval.AssignmentMapID : Edm.Int32 "Approval Map"
PX.Objects.SO.SOSetupInvoiceApproval.AssignmentNotificationID : Edm.Int32 "Pending Approval Notification"
PX.Objects.SO.SOSetupInvoiceApproval.tstamp : Edm.Binary
PX.Objects.SO.SOSetupInvoiceApproval.CreatedByID : Edm.Guid "Created By"
PX.Objects.SO.SOSetupInvoiceApproval.CreatedByScreenID : Edm.String
PX.Objects.SO.SOSetupInvoiceApproval.CreatedDateTime : Edm.DateTimeOffset
PX.Objects.SO.SOSetupInvoiceApproval.LastModifiedByID : Edm.Guid "Last Modified By"
PX.Objects.SO.SOSetupInvoiceApproval.LastModifiedByScreenID : Edm.String
PX.Objects.SO.SOSetupInvoiceApproval.LastModifiedDateTime : Edm.DateTimeOffset
PX.Objects.SO.SOSetupInvoiceApproval.UsersByCreatedByID -> PX.SM.Users (CreatedByID=PKID)
PX.Objects.SO.SOSetupInvoiceApproval.UsersByLastModifiedByID -> PX.SM.Users (LastModifiedByID=PKID)
PX.Objects.SO.SOSetupInvoiceApproval.NotificationByAssignmentNotificationID -> PX.SM.Notification (AssignmentNotificationID=NotificationID)
PX.Objects.SO.SOSetupInvoiceApproval.EPAssignmentMapByAssignmentMapID -> PX.Objects.EP.EPAssignmentMap (AssignmentMapID=AssignmentMapID)

# PX.Objects.SO.SOShipLine (EntityType)

Label: "Shipment Line"
Key: LineNbr, ShipmentNbr
Entity sets: PX_Objects_SO_SOShipLine, ShipmentLine, SOShipLine
Non-filterable, non-selectable: TranType, OriginalShippedQty, OpenOrderQty, LineAmt, KeepManualFreight, NoteText

PX.Objects.SO.SOShipLine.ShipmentNbr : Edm.String [key] "Shipment Nbr."
PX.Objects.SO.SOShipLine.ShipmentType : Edm.String
PX.Objects.SO.SOShipLine.LineNbr : Edm.Int32 [key] "Line Nbr."
PX.Objects.SO.SOShipLine.SortOrder : Edm.Int32
PX.Objects.SO.SOShipLine.OrigDocumentType : Edm.String "Document Type"
PX.Objects.SO.SOShipLine.CustomerID : Edm.Int32
PX.Objects.SO.SOShipLine.ShipDate : Edm.DateTimeOffset
PX.Objects.SO.SOShipLine.Confirmed : Edm.Boolean
PX.Objects.SO.SOShipLine.Released : Edm.Boolean [required]
PX.Objects.SO.SOShipLine.LineType : Edm.String
PX.Objects.SO.SOShipLine.OrigOrderType : Edm.String "Order Type"
PX.Objects.SO.SOShipLine.OrigOrderNbr : Edm.String "Order Nbr."
PX.Objects.SO.SOShipLine.OrigLineNbr : Edm.Int32 "Order Line Nbr."
PX.Objects.SO.SOShipLine.OrigSplitLineNbr : Edm.Int32 "Split Line Nbr."
PX.Objects.SO.SOShipLine.Operation : Edm.String
PX.Objects.SO.SOShipLine.SOLineSign : Edm.Int16
PX.Objects.SO.SOShipLine.OrigPlanType : Edm.String
PX.Objects.SO.SOShipLine.InvtMult : Edm.Int16 [required] "Inventory Multiplier"
PX.Objects.SO.SOShipLine.IsStockItem : Edm.Boolean "Is stock"
PX.Objects.SO.SOShipLine.InventoryID : Edm.Int32 "Inventory ID"
PX.Objects.SO.SOShipLine.IsIntercompany : Edm.Boolean
PX.Objects.SO.SOShipLine.TranType : Edm.String
PX.Objects.SO.SOShipLine.PlanType : Edm.String
PX.Objects.SO.SOShipLine.OrderUOM : Edm.String
PX.Objects.SO.SOShipLine.UOM : Edm.String "UOM"
PX.Objects.SO.SOShipLine.ShippedQty : Edm.Decimal [required] "Shipped Qty."
PX.Objects.SO.SOShipLine.BaseShippedQty : Edm.Decimal [required] "Base Shipped Qty."
PX.Objects.SO.SOShipLine.BaseOriginalShippedQty : Edm.Decimal [required]
PX.Objects.SO.SOShipLine.OriginalShippedQty : Edm.Decimal "Original Qty."
PX.Objects.SO.SOShipLine.UnassignedQty : Edm.Decimal [required] "Unassigned Qty."
PX.Objects.SO.SOShipLine.CompleteQtyMin : Edm.Decimal "Undership Threshold (%)"
PX.Objects.SO.SOShipLine.BaseOrigOrderQty : Edm.Decimal [required]
PX.Objects.SO.SOShipLine.OrigOrderQty : Edm.Decimal [required]
PX.Objects.SO.SOShipLine.OpenOrderQty : Edm.Decimal "Open Qty."
PX.Objects.SO.SOShipLine.FullOrderQty : Edm.Decimal [required] "Ordered Qty."
PX.Objects.SO.SOShipLine.BaseFullOrderQty : Edm.Decimal [required]
PX.Objects.SO.SOShipLine.FullOpenQty : Edm.Decimal [required] "Open Order Qty."
PX.Objects.SO.SOShipLine.BaseFullOpenQty : Edm.Decimal [required]
PX.Objects.SO.SOShipLine.FullShippedQty : Edm.Decimal [required]
PX.Objects.SO.SOShipLine.BaseFullShippedQty : Edm.Decimal [required]
PX.Objects.SO.SOShipLine.UnitCost : Edm.Decimal
PX.Objects.SO.SOShipLine.ExtCost : Edm.Decimal [required]
PX.Objects.SO.SOShipLine.UnitPrice : Edm.Decimal
PX.Objects.SO.SOShipLine.DiscPct : Edm.Decimal
PX.Objects.SO.SOShipLine.LineAmt : Edm.Decimal
PX.Objects.SO.SOShipLine.AlternateID : Edm.String
PX.Objects.SO.SOShipLine.TranDesc : Edm.String "Description"
PX.Objects.SO.SOShipLine.UnitWeigth : Edm.Decimal [required] "Unit Weight"
PX.Objects.SO.SOShipLine.UnitVolume : Edm.Decimal [required]
PX.Objects.SO.SOShipLine.ExtWeight : Edm.Decimal [required]
PX.Objects.SO.SOShipLine.ExtVolume : Edm.Decimal [required]
PX.Objects.SO.SOShipLine.ProjectID : Edm.Int32 "Project"
PX.Objects.SO.SOShipLine.TaskID : Edm.Int32 "Project Task"
PX.Objects.SO.SOShipLine.ReasonCode : Edm.String "Reason Code"
PX.Objects.SO.SOShipLine.IsFree : Edm.Boolean "Free Item"
PX.Objects.SO.SOShipLine.ManualPrice : Edm.Boolean
PX.Objects.SO.SOShipLine.ManualDisc : Edm.Boolean "Manual Cash Discount"
PX.Objects.SO.SOShipLine.IsUnassigned : Edm.Boolean [required]
PX.Objects.SO.SOShipLine.DiscountID : Edm.String "Discount Code"
PX.Objects.SO.SOShipLine.DiscountSequenceID : Edm.String "Discount Sequence"
PX.Objects.SO.SOShipLine.KeepManualFreight : Edm.Boolean
PX.Objects.SO.SOShipLine.ShipComplete : Edm.String "Shipping Rule"
PX.Objects.SO.SOShipLine.RequireINUpdate : Edm.Boolean
PX.Objects.SO.SOShipLine.PickedQty : Edm.Decimal [required] "Picked Qty."
PX.Objects.SO.SOShipLine.BasePickedQty : Edm.Decimal [required]
PX.Objects.SO.SOShipLine.PackedQty : Edm.Decimal [required] "Packed Qty."
PX.Objects.SO.SOShipLine.BasePackedQty : Edm.Decimal [required]
PX.Objects.SO.SOShipLine.NoteID : Edm.Guid
PX.Objects.SO.SOShipLine.NoteText : Edm.String "Note Text"
PX.Objects.SO.SOShipLine.CreatedByID : Edm.Guid "Created By"
PX.Objects.SO.SOShipLine.CreatedByScreenID : Edm.String
PX.Objects.SO.SOShipLine.CreatedDateTime : Edm.DateTimeOffset
PX.Objects.SO.SOShipLine.LastModifiedByID : Edm.Guid "Last Modified By"
PX.Objects.SO.SOShipLine.LastModifiedByScreenID : Edm.String
PX.Objects.SO.SOShipLine.LastModifiedDateTime : Edm.DateTimeOffset
PX.Objects.SO.SOShipLine.tstamp : Edm.Binary
PX.Objects.SO.SOShipLine.BlanketType : Edm.String
PX.Objects.SO.SOShipLine.BlanketNbr : Edm.String "Blanket SO Ref. Nbr."
PX.Objects.SO.SOShipLine.BlanketLineNbr : Edm.Int32
PX.Objects.SO.SOShipLine.BlanketSplitLineNbr : Edm.Int32
PX.Objects.SO.SOShipLine.IsSpecialOrder : Edm.Boolean [required]
PX.Objects.SO.SOShipLine.CostCenterID : Edm.Int32 [required]
PX.Objects.SO.SOShipLine.InventorySource : Edm.String "Inventory Source"
PX.Objects.SO.SOShipLine.InvoiceGroupNbr : Edm.Int32
PX.Objects.SO.SOShipLine.PMProjectByProjectID -> PX.Objects.PM.PMProject (ProjectID=ContractID)
PX.Objects.SO.SOShipLine.PMTaskByTaskID -> PX.Objects.PM.PMTask (ProjectID=ProjectID, TaskID=TaskID)
PX.Objects.SO.SOShipLine.CustomerByCustomerID -> PX.Objects.AR.Customer (CustomerID=BAccountID)
PX.Objects.SO.SOShipLine.InventoryItemByInventoryID -> PX.Objects.IN.InventoryItem (InventoryID=InventoryID)
PX.Objects.SO.SOShipLine.SOOrderByOrigOrderNbr -> PX.Objects.SO.SOOrder (OrigOrderType=OrderType, OrigOrderNbr=OrderNbr)
PX.Objects.SO.SOShipLine.SOOrderByOrigOrderType -> PX.Objects.SO.SOOrder (OrigOrderNbr=OrderNbr, OrigOrderType=OrderType)
PX.Objects.SO.SOShipLine.SOOrderByBlanketType -> PX.Objects.SO.SOOrder (BlanketNbr=OrderNbr, BlanketType=OrderType)
PX.Objects.SO.SOShipLine.UsersByCreatedByID -> PX.SM.Users (CreatedByID=PKID)
PX.Objects.SO.SOShipLine.UsersByLastModifiedByID -> PX.SM.Users (LastModifiedByID=PKID)
PX.Objects.SO.SOShipLine.SOBlanketOrderLinkByOrigOrderNbr -> PX.Objects.SO.SOBlanketOrderLink (BlanketType=BlanketType, BlanketNbr=BlanketNbr, OrigOrderType=OrderType, OrigOrderNbr=OrderNbr)
PX.Objects.SO.SOShipLine.SOLineByOrigLineNbr -> PX.Objects.SO.SOLine (OrigOrderType=OrderType, OrigOrderNbr=OrderNbr, OrigLineNbr=LineNbr)
PX.Objects.SO.SOShipLine.SOLineSplitByOrigSplitLineNbr -> PX.Objects.SO.SOLineSplit (OrigOrderType=OrderType, OrigOrderNbr=OrderNbr, OrigLineNbr=LineNbr, OrigSplitLineNbr=SplitLineNbr)
PX.Objects.SO.SOShipLine.SOOrderShipmentByOrigOrderNbr -> PX.Objects.SO.SOOrderShipment (ShipmentType=ShipmentType, ShipmentNbr=ShipmentNbr, OrigOrderType=OrderType, OrigOrderNbr=OrderNbr)
PX.Objects.SO.SOShipLine.SOOrderTypeByOrigOrderType -> PX.Objects.SO.SOOrderType (OrigOrderType=OrderType)
PX.Objects.SO.SOShipLine.SOOrderTypeOperationByOperation -> PX.Objects.SO.SOOrderTypeOperation (OrigOrderType=OrderType, Operation=Operation)
PX.Objects.SO.SOShipLine.SOOrderTypeOperationByOrigOrderType -> PX.Objects.SO.SOOrderTypeOperation (Operation=Operation, OrigOrderType=OrderType)
PX.Objects.SO.SOShipLine.SOShipmentByShipmentNbr -> PX.Objects.SO.SOShipment (ShipmentType=ShipmentType, ShipmentNbr=ShipmentNbr)
PX.Objects.SO.SOShipLine.SOShipmentByShipmentType -> PX.Objects.SO.SOShipment (ShipmentNbr=ShipmentNbr, ShipmentType=ShipmentType)
PX.Objects.SO.SOShipLine.PMCostCodeByCostCodeID -> PX.Objects.PM.PMCostCode
PX.Objects.SO.SOShipLine.ReasonCodeByReasonCode -> PX.Objects.CS.ReasonCode (ReasonCode=ReasonCodeID)
PX.Objects.SO.SOShipLine.INLocationByLocationID -> PX.Objects.IN.INLocation
PX.Objects.SO.SOShipLine.INLocationBySiteID -> PX.Objects.IN.INLocation
PX.Objects.SO.SOShipLine.INLocationByToLocationID -> PX.Objects.IN.INLocation
PX.Objects.SO.SOShipLine.INSiteBySiteID -> PX.Objects.IN.INSite
PX.Objects.SO.SOShipLine.INSubItemBySubItemID -> PX.Objects.IN.INSubItem
PX.Objects.SO.SOShipLine.INUnitByInventoryID -> PX.Objects.IN.INUnit (UOM=FromUnit, InventoryID=InventoryID)
PX.Objects.SO.SOShipLine.INSiteZoneBySiteID -> PX.Objects.IN.DAC.INSiteZone
PX.Objects.SO.SOShipLine.ARDiscountByDiscountID -> PX.Objects.AR.ARDiscount (DiscountID=DiscountID)
PX.Objects.SO.SOShipLine.DiscountSequenceByDiscountSequenceID -> PX.Objects.AR.DiscountSequence (DiscountID=DiscountID, DiscountSequenceID=DiscountSequenceID)
PX.Objects.SO.SOShipLine.INLocationStatusByCostCenterByCostCenterID -> PX.Objects.IN.INLocationStatusByCostCenter (InventoryID=InventoryID, CostCenterID=CostCenterID)
PX.Objects.SO.SOShipLine.INLotSerialStatusByCostCenterByCostCenterID -> PX.Objects.IN.INLotSerialStatusByCostCenter (InventoryID=InventoryID, CostCenterID=CostCenterID)
PX.Objects.SO.SOShipLine.INSiteStatusByCostCenterByCostCenterID -> PX.Objects.IN.INSiteStatusByCostCenter (InventoryID=InventoryID, CostCenterID=CostCenterID)
PX.Objects.SO.SOShipLine.INLocationStatusByLocationID -> PX.Objects.IN.INLocationStatus (InventoryID=InventoryID)
PX.Objects.SO.SOShipLine.INLotSerialStatusByLotSerialNbr -> PX.Objects.IN.INLotSerialStatus (InventoryID=InventoryID)
PX.Objects.SO.SOShipLine.INSiteStatusBySiteID -> PX.Objects.IN.INSiteStatus (InventoryID=InventoryID)
PX.Objects.SO.SOShipLine.INPlanTypeByPlanType -> PX.Objects.IN.INPlanType (PlanType=PlanType)
PX.Objects.SO.SOShipLine.INPlanTypeByOrigPlanType -> PX.Objects.IN.INPlanType (OrigPlanType=PlanType)
PX.Objects.SO.SOShipLine.INTranCollection -> Collection(PX.Objects.IN.INTran)
PX.Objects.SO.SOShipLine.SOShipLineSplitCollection -> Collection(PX.Objects.SO.SOShipLineSplit)
PX.Objects.SO.SOShipLine.SOShipLineSplitPackageCollection -> Collection(PX.Objects.SO.SOShipLineSplitPackage)
PX.Objects.SO.SOShipLine.SOShipmentSplitToCartSplitLinkCollection -> Collection(PX.Objects.SO.SOShipmentSplitToCartSplitLink)
PX.Objects.SO.SOShipLine.INTransitLineCollection -> Collection(PX.Objects.IN.INTransitLine)

# PX.Objects.SO.SOShipLineSplit (EntityType)

Label: "Shipment Line Split"
Key: LineNbr, ShipmentNbr, SplitLineNbr
Entity sets: PX_Objects_SO_SOShipLineSplit, ShipmentLineSplit, SOShipLineSplit
Non-filterable, non-selectable: TranType, LastLotSerialNbr, LotSerClassID, AssignedNbr, ProjectID, TaskID

PX.Objects.SO.SOShipLineSplit.ShipmentNbr : Edm.String [key]
PX.Objects.SO.SOShipLineSplit.LineNbr : Edm.Int32 [key] "Line Nbr."
PX.Objects.SO.SOShipLineSplit.OrigOrderType : Edm.String
PX.Objects.SO.SOShipLineSplit.OrigOrderNbr : Edm.String
PX.Objects.SO.SOShipLineSplit.OrigLineNbr : Edm.Int32
PX.Objects.SO.SOShipLineSplit.OrigSplitLineNbr : Edm.Int32
PX.Objects.SO.SOShipLineSplit.OrigPlanType : Edm.String
PX.Objects.SO.SOShipLineSplit.Operation : Edm.String
PX.Objects.SO.SOShipLineSplit.SplitLineNbr : Edm.Int32 [key] "Split Line Nbr."
PX.Objects.SO.SOShipLineSplit.InvtMult : Edm.Int16
PX.Objects.SO.SOShipLineSplit.InventoryID : Edm.Int32 "Inventory ID"
PX.Objects.SO.SOShipLineSplit.LineType : Edm.String
PX.Objects.SO.SOShipLineSplit.IsStockItem : Edm.Boolean
PX.Objects.SO.SOShipLineSplit.IsComponentItem : Edm.Boolean
PX.Objects.SO.SOShipLineSplit.IsIntercompany : Edm.Boolean
PX.Objects.SO.SOShipLineSplit.TranType : Edm.String
PX.Objects.SO.SOShipLineSplit.PlanType : Edm.String
PX.Objects.SO.SOShipLineSplit.PlanID : Edm.Int64
PX.Objects.SO.SOShipLineSplit.LastLotSerialNbr : Edm.String
PX.Objects.SO.SOShipLineSplit.LotSerClassID : Edm.String
PX.Objects.SO.SOShipLineSplit.AssignedNbr : Edm.String
PX.Objects.SO.SOShipLineSplit.HasGeneratedLotSerialNbr : Edm.Boolean [required]
PX.Objects.SO.SOShipLineSplit.UOM : Edm.String "UOM"
PX.Objects.SO.SOShipLineSplit.Qty : Edm.Decimal [required] "Quantity"
PX.Objects.SO.SOShipLineSplit.BaseQty : Edm.Decimal
PX.Objects.SO.SOShipLineSplit.PickedQty : Edm.Decimal [required] "Picked Quantity"
PX.Objects.SO.SOShipLineSplit.BasePickedQty : Edm.Decimal
PX.Objects.SO.SOShipLineSplit.PackedQty : Edm.Decimal [required] "Packed Quantity"
PX.Objects.SO.SOShipLineSplit.BasePackedQty : Edm.Decimal
PX.Objects.SO.SOShipLineSplit.ShipDate : Edm.DateTimeOffset
PX.Objects.SO.SOShipLineSplit.Confirmed : Edm.Boolean "Confirmed"
PX.Objects.SO.SOShipLineSplit.Released : Edm.Boolean "Released"
PX.Objects.SO.SOShipLineSplit.IsUnassigned : Edm.Boolean [required]
PX.Objects.SO.SOShipLineSplit.ProjectID : Edm.Int32
PX.Objects.SO.SOShipLineSplit.TaskID : Edm.Int32
PX.Objects.SO.SOShipLineSplit.CreatedByID : Edm.Guid "Created By"
PX.Objects.SO.SOShipLineSplit.CreatedByScreenID : Edm.String
PX.Objects.SO.SOShipLineSplit.CreatedDateTime : Edm.DateTimeOffset
PX.Objects.SO.SOShipLineSplit.LastModifiedByID : Edm.Guid "Last Modified By"
PX.Objects.SO.SOShipLineSplit.LastModifiedByScreenID : Edm.String
PX.Objects.SO.SOShipLineSplit.LastModifiedDateTime : Edm.DateTimeOffset
PX.Objects.SO.SOShipLineSplit.tstamp : Edm.Binary
PX.Objects.SO.SOShipLineSplit.BeforeChangeLotSerialNbr : Edm.String
PX.Objects.SO.SOShipLineSplit.AllocationChangedDateTime : Edm.DateTimeOffset
PX.Objects.SO.SOShipLineSplit.AllocationChangedUserID : Edm.Guid
PX.Objects.SO.SOShipLineSplit.OriginalLotSerialNbr : Edm.String
PX.Objects.SO.SOShipLineSplit.InventoryItemByInventoryID -> PX.Objects.IN.InventoryItem (InventoryID=InventoryID)
PX.Objects.SO.SOShipLineSplit.SOOrderByOrigOrderNbr -> PX.Objects.SO.SOOrder (OrigOrderType=OrderType, OrigOrderNbr=OrderNbr)
PX.Objects.SO.SOShipLineSplit.INItemPlanByPlanID -> PX.Objects.IN.INItemPlan (PlanID=PlanID)
PX.Objects.SO.SOShipLineSplit.UsersByCreatedByID -> PX.SM.Users (CreatedByID=PKID)
PX.Objects.SO.SOShipLineSplit.UsersByLastModifiedByID -> PX.SM.Users (LastModifiedByID=PKID)
PX.Objects.SO.SOShipLineSplit.SOLineByOrigLineNbr -> PX.Objects.SO.SOLine (OrigOrderType=OrderType, OrigOrderNbr=OrderNbr, OrigLineNbr=LineNbr)
PX.Objects.SO.SOShipLineSplit.SOLineSplitByOrigSplitLineNbr -> PX.Objects.SO.SOLineSplit (OrigOrderType=OrderType, OrigOrderNbr=OrderNbr, OrigLineNbr=LineNbr, OrigSplitLineNbr=SplitLineNbr)
PX.Objects.SO.SOShipLineSplit.SOOrderTypeByOrigOrderType -> PX.Objects.SO.SOOrderType (OrigOrderType=OrderType)
PX.Objects.SO.SOShipLineSplit.SOOrderTypeOperationByOperation -> PX.Objects.SO.SOOrderTypeOperation (OrigOrderType=OrderType, Operation=Operation)
PX.Objects.SO.SOShipLineSplit.SOOrderTypeOperationByOrigOrderType -> PX.Objects.SO.SOOrderTypeOperation (Operation=Operation, OrigOrderType=OrderType)
PX.Objects.SO.SOShipLineSplit.SOShipLineByLineNbr -> PX.Objects.SO.SOShipLine (ShipmentNbr=ShipmentNbr, LineNbr=LineNbr)
PX.Objects.SO.SOShipLineSplit.SOShipmentByShipmentNbr -> PX.Objects.SO.SOShipment (ShipmentNbr=ShipmentNbr)
PX.Objects.SO.SOShipLineSplit.INLocationByLocationID -> PX.Objects.IN.INLocation
PX.Objects.SO.SOShipLineSplit.INLocationBySiteID -> PX.Objects.IN.INLocation
PX.Objects.SO.SOShipLineSplit.INSiteBySiteID -> PX.Objects.IN.INSite
PX.Objects.SO.SOShipLineSplit.INSubItemBySubItemID -> PX.Objects.IN.INSubItem
PX.Objects.SO.SOShipLineSplit.INUnitByInventoryID -> PX.Objects.IN.INUnit (UOM=FromUnit, InventoryID=InventoryID)
PX.Objects.SO.SOShipLineSplit.INSiteZoneByWarehouseZoneID -> PX.Objects.IN.DAC.INSiteZone
PX.Objects.SO.SOShipLineSplit.INSiteZoneBySiteID -> PX.Objects.IN.DAC.INSiteZone
PX.Objects.SO.SOShipLineSplit.INLotSerialStatusByCostCenterByLocationID -> PX.Objects.IN.INLotSerialStatusByCostCenter (InventoryID=InventoryID)
PX.Objects.SO.SOShipLineSplit.INLocationStatusByLocationID -> PX.Objects.IN.INLocationStatus (InventoryID=InventoryID)
PX.Objects.SO.SOShipLineSplit.INLotSerialStatusByLotSerialNbr -> PX.Objects.IN.INLotSerialStatus (InventoryID=InventoryID)
PX.Objects.SO.SOShipLineSplit.INSiteStatusBySiteID -> PX.Objects.IN.INSiteStatus (InventoryID=InventoryID)
PX.Objects.SO.SOShipLineSplit.INPlanTypeByPlanType -> PX.Objects.IN.INPlanType (PlanType=PlanType)
PX.Objects.SO.SOShipLineSplit.INPlanTypeByOrigPlanType -> PX.Objects.IN.INPlanType (OrigPlanType=PlanType)
PX.Objects.SO.SOShipLineSplit.SOShipLineSplitPackageCollection -> Collection(PX.Objects.SO.SOShipLineSplitPackage)
PX.Objects.SO.SOShipLineSplit.SOShipmentSplitToCartSplitLinkCollection -> Collection(PX.Objects.SO.SOShipmentSplitToCartSplitLink)

# PX.Objects.SO.SOShipLineSplitPackage (EntityType)

Label: "Shipment Package Detail"
Key: RecordID
Entity sets: PX_Objects_SO_SOShipLineSplitPackage, ShipmentPackageDetail, SOShipLineSplitPackage

PX.Objects.SO.SOShipLineSplitPackage.RecordID : Edm.Int32 [key]
PX.Objects.SO.SOShipLineSplitPackage.ShipmentNbr : Edm.String
PX.Objects.SO.SOShipLineSplitPackage.ShipmentLineNbr : Edm.Int32
PX.Objects.SO.SOShipLineSplitPackage.ShipmentSplitLineNbr : Edm.Int32 "Shipment Split Line Nbr."
PX.Objects.SO.SOShipLineSplitPackage.PackageLineNbr : Edm.Int32
PX.Objects.SO.SOShipLineSplitPackage.InventoryID : Edm.Int32 "Inventory ID"
PX.Objects.SO.SOShipLineSplitPackage.UOM : Edm.String "UOM"
PX.Objects.SO.SOShipLineSplitPackage.PackedQty : Edm.Decimal [required] "Quantity"
PX.Objects.SO.SOShipLineSplitPackage.BasePackedQty : Edm.Decimal
PX.Objects.SO.SOShipLineSplitPackage.UnitPriceFactor : Edm.Decimal [required]
PX.Objects.SO.SOShipLineSplitPackage.WeightFactor : Edm.Decimal [required]
PX.Objects.SO.SOShipLineSplitPackage.CreatedByID : Edm.Guid "Created By"
PX.Objects.SO.SOShipLineSplitPackage.CreatedByScreenID : Edm.String
PX.Objects.SO.SOShipLineSplitPackage.CreatedDateTime : Edm.DateTimeOffset
PX.Objects.SO.SOShipLineSplitPackage.LastModifiedByID : Edm.Guid "Last Modified By"
PX.Objects.SO.SOShipLineSplitPackage.LastModifiedByScreenID : Edm.String
PX.Objects.SO.SOShipLineSplitPackage.LastModifiedDateTime : Edm.DateTimeOffset
PX.Objects.SO.SOShipLineSplitPackage.tstamp : Edm.Binary
PX.Objects.SO.SOShipLineSplitPackage.InventoryItemByInventoryID -> PX.Objects.IN.InventoryItem (InventoryID=InventoryID)
PX.Objects.SO.SOShipLineSplitPackage.UsersByCreatedByID -> PX.SM.Users (CreatedByID=PKID)
PX.Objects.SO.SOShipLineSplitPackage.UsersByLastModifiedByID -> PX.SM.Users (LastModifiedByID=PKID)
PX.Objects.SO.SOShipLineSplitPackage.SOPackageDetailByPackageLineNbr -> PX.Objects.SO.SOPackageDetail (ShipmentNbr=ShipmentNbr, PackageLineNbr=LineNbr)
PX.Objects.SO.SOShipLineSplitPackage.SOShipLineByShipmentLineNbr -> PX.Objects.SO.SOShipLine (ShipmentNbr=ShipmentNbr, ShipmentLineNbr=LineNbr)
PX.Objects.SO.SOShipLineSplitPackage.SOShipLineSplitByShipmentSplitLineNbr -> PX.Objects.SO.SOShipLineSplit (ShipmentNbr=ShipmentNbr, ShipmentLineNbr=LineNbr, ShipmentSplitLineNbr=SplitLineNbr)
PX.Objects.SO.SOShipLineSplitPackage.SOShipmentByShipmentNbr -> PX.Objects.SO.SOShipment (ShipmentNbr=ShipmentNbr)
PX.Objects.SO.SOShipLineSplitPackage.INSubItemBySubItemID -> PX.Objects.IN.INSubItem
PX.Objects.SO.SOShipLineSplitPackage.INUnitByInventoryID -> PX.Objects.IN.INUnit (UOM=FromUnit, InventoryID=InventoryID)

# PX.Objects.SO.SOShipment (EntityType)

Label: "Shipment"
Key: ShipmentNbr
Entity sets: PX_Objects_SO_SOShipment, Shipment, SOShipment
Non-filterable, non-selectable: SiteBranchID, WillCall, NoteText, ConfirmedToVerify, BillingInOrders, RecalcPackagesReason, IsPackageContentDeleted, Hidden, BillSeparately, CreateARDoc, ShopForRatesErrorMessage, Excluded, ShipViaUpdateFromShopForRate, OrigDocumentNoteID, InvtDocType, InvtRefNbr, IsMaterialRelated, HasDeliverySettings, ExtCarrierServiceMethod, ShipperCountry, PJExternalStatus, ExtCarrierPlugIn, ExtIsExternalCarrierPlugIn, ExtUseScenario, CuryRate, CuryViewState

PX.Objects.SO.SOShipment.ShipmentNbr : Edm.String [key] "Shipment Nbr."
PX.Objects.SO.SOShipment.ShipDate : Edm.DateTimeOffset "Shipment Date"
PX.Objects.SO.SOShipment.Operation : Edm.String "Operation"
PX.Objects.SO.SOShipment.ShipmentType : Edm.String "Type"
PX.Objects.SO.SOShipment.CustomerID : Edm.Int32 "Customer"
PX.Objects.SO.SOShipment.CustomerOrderNbr : Edm.String "Customer Order Nbr."
PX.Objects.SO.SOShipment.SiteBranchID : Edm.Int32
PX.Objects.SO.SOShipment.DestinationSiteID : Edm.Int32 "To Warehouse"
PX.Objects.SO.SOShipment.ShipmentDesc : Edm.String "Description"
PX.Objects.SO.SOShipment.ShipAddressID : Edm.Int32 "Shipping Address"
PX.Objects.SO.SOShipment.ShipContactID : Edm.Int32
PX.Objects.SO.SOShipment.FOBPoint : Edm.String "FOB Point"
PX.Objects.SO.SOShipment.ShipVia : Edm.String "Ship Via"
PX.Objects.SO.SOShipment.WillCall : Edm.Boolean "Will Call"
PX.Objects.SO.SOShipment.UseCustomerAccount : Edm.Boolean [required] "Use Customer's Account"
PX.Objects.SO.SOShipment.Resedential : Edm.Boolean [required] "Residential Delivery"
PX.Objects.SO.SOShipment.SaturdayDelivery : Edm.Boolean [required] "Saturday Delivery"
PX.Objects.SO.SOShipment.Insurance : Edm.Boolean [required] "Insurance"
PX.Objects.SO.SOShipment.GroundCollect : Edm.Boolean [required] "Ground Collect"
PX.Objects.SO.SOShipment.LabelsPrinted : Edm.Boolean [required] "Labels Printed"
PX.Objects.SO.SOShipment.CommercialInvoicesPrinted : Edm.Boolean [required]
PX.Objects.SO.SOShipment.PickListPrinted : Edm.Boolean [required] "Pick List Printed"
PX.Objects.SO.SOShipment.ConfirmationPrinted : Edm.Boolean [required] "Shipment Confirmation Printed"
PX.Objects.SO.SOShipment.ShippedViaCarrier : Edm.Boolean [required]
PX.Objects.SO.SOShipment.ShipTermsID : Edm.String "Shipping Terms"
PX.Objects.SO.SOShipment.ShipZoneID : Edm.String "Shipping Zone ID"
PX.Objects.SO.SOShipment.LineTotal : Edm.Decimal [required] "Line Total"
PX.Objects.SO.SOShipment.CuryID : Edm.String "Freight Currency"
PX.Objects.SO.SOShipment.CuryInfoID : Edm.Int64
PX.Objects.SO.SOShipment.CuryFreightCost : Edm.Decimal [required] "Freight Cost"
PX.Objects.SO.SOShipment.FreightCost : Edm.Decimal "Freight Cost"
PX.Objects.SO.SOShipment.OverrideFreightAmount : Edm.Boolean [required] "Override Freight Price"
PX.Objects.SO.SOShipment.FreightAmountSource : Edm.String "Invoice Freight Price Based On"
PX.Objects.SO.SOShipment.CuryFreightAmt : Edm.Decimal [required] "Freight Price"
PX.Objects.SO.SOShipment.FreightAmt : Edm.Decimal "Freight Price"
PX.Objects.SO.SOShipment.CuryPremiumFreightAmt : Edm.Decimal [required] "Premium Freight Price"
PX.Objects.SO.SOShipment.PremiumFreightAmt : Edm.Decimal
PX.Objects.SO.SOShipment.CuryTotalFreightAmt : Edm.Decimal [required] "Total Freight Price"
PX.Objects.SO.SOShipment.TotalFreightAmt : Edm.Decimal "Total Freight Price"
PX.Objects.SO.SOShipment.TaxCategoryID : Edm.String "Tax Category"
PX.Objects.SO.SOShipment.NoteID : Edm.Guid
PX.Objects.SO.SOShipment.NoteText : Edm.String "Note Text"
PX.Objects.SO.SOShipment.Hold : Edm.Boolean "Hold"
PX.Objects.SO.SOShipment.Confirmed : Edm.Boolean "Confirmed"
PX.Objects.SO.SOShipment.ConfirmedToVerify : Edm.Boolean
PX.Objects.SO.SOShipment.Released : Edm.Boolean "Released"
PX.Objects.SO.SOShipment.Picked : Edm.Boolean [required] "Picked"
PX.Objects.SO.SOShipment.PickedViaWorksheet : Edm.Boolean [required] "Picked via Worksheet"
PX.Objects.SO.SOShipment.PickedQty : Edm.Decimal [required] "Picked Qty."
PX.Objects.SO.SOShipment.IsNonShippable : Edm.Boolean [required] "Non-Shippable"
PX.Objects.SO.SOShipment.PackedQty : Edm.Decimal [required] "Packed Qty."
PX.Objects.SO.SOShipment.Status : Edm.String "Status"
PX.Objects.SO.SOShipment.LineCntr : Edm.Int32
PX.Objects.SO.SOShipment.OrderCntr : Edm.Int32
PX.Objects.SO.SOShipment.BilledOrderCntr : Edm.Int32
PX.Objects.SO.SOShipment.BillSeparatelyCntr : Edm.Int32 [required]
PX.Objects.SO.SOShipment.BillingInOrders : Edm.String "Billing in Orders"
PX.Objects.SO.SOShipment.UnbilledOrderCntr : Edm.Int32
PX.Objects.SO.SOShipment.ReleasedOrderCntr : Edm.Int32
PX.Objects.SO.SOShipment.ControlQty : Edm.Decimal [required] "Control Quantity"
PX.Objects.SO.SOShipment.ShipmentQty : Edm.Decimal [required] "Shipped Quantity"
PX.Objects.SO.SOShipment.ShipmentWeight : Edm.Decimal [required] "Shipped Weight"
PX.Objects.SO.SOShipment.ShipmentVolume : Edm.Decimal [required] "Shipped Volume"
PX.Objects.SO.SOShipment.PackageLineCntr : Edm.Int32 [required]
PX.Objects.SO.SOShipment.PackageWeight : Edm.Decimal [required] "Package Weight"
PX.Objects.SO.SOShipment.IsPackageValid : Edm.Boolean [required]
PX.Objects.SO.SOShipment.RecalcPackagesReason : Edm.Int32
PX.Objects.SO.SOShipment.PackageCount : Edm.Int32 [required] "Packages"
PX.Objects.SO.SOShipment.IsManualPackage : Edm.Boolean "Manual Packaging"
PX.Objects.SO.SOShipment.IsPackageContentDeleted : Edm.Boolean
PX.Objects.SO.SOShipment.CreatedByID : Edm.Guid "Created By"
PX.Objects.SO.SOShipment.CreatedByScreenID : Edm.String
PX.Objects.SO.SOShipment.CreatedDateTime : Edm.DateTimeOffset "Created On"
PX.Objects.SO.SOShipment.LastModifiedByID : Edm.Guid "Last Modified By"
PX.Objects.SO.SOShipment.LastModifiedByScreenID : Edm.String
PX.Objects.SO.SOShipment.LastModifiedDateTime : Edm.DateTimeOffset "Last Modified On"
PX.Objects.SO.SOShipment.GotReadyForArchiveAt : Edm.DateTimeOffset
PX.Objects.SO.SOShipment.tstamp : Edm.Binary
PX.Objects.SO.SOShipment.Hidden : Edm.Boolean
PX.Objects.SO.SOShipment.WorkgroupID : Edm.Int32 "Workgroup"
PX.Objects.SO.SOShipment.OwnerID : Edm.Int32 "Owner"
PX.Objects.SO.SOShipment.FreeItemQtyTot : Edm.Decimal "Free Items Quantity Total"
PX.Objects.SO.SOShipment.StatusIsNull : Edm.String "Status"
PX.Objects.SO.SOShipment.BillSeparately : Edm.Boolean "Bill Separately"
PX.Objects.SO.SOShipment.ConfirmedByID : Edm.Guid "Confirmed By"
PX.Objects.SO.SOShipment.ConfirmedDateTime : Edm.DateTimeOffset "Confirmed On"
PX.Objects.SO.SOShipment.CreateARDoc : Edm.Boolean
PX.Objects.SO.SOShipment.CurrentWorksheetNbr : Edm.String "Worksheet Nbr."
PX.Objects.SO.SOShipment.UnlimitedPackages : Edm.Boolean [required] "Packaging Processed in External System"
PX.Objects.SO.SOShipment.ShopForRatesErrorMessage : Edm.String "ShopForRatesErrorMessage"
PX.Objects.SO.SOShipment.IsIntercompany : Edm.Boolean
PX.Objects.SO.SOShipment.Excluded : Edm.Boolean "Excluded"
PX.Objects.SO.SOShipment.ShipViaUpdateFromShopForRate : Edm.Boolean
PX.Objects.SO.SOShipment.OrderBranchID : Edm.Int32
PX.Objects.SO.SOShipment.FreightCostIsValid : Edm.Boolean [required]
PX.Objects.SO.SOShipment.OrigDocumentType : Edm.String "Source Document Type"
PX.Objects.SO.SOShipment.OrigDocumentNoteID : Edm.Guid
PX.Objects.SO.SOShipment.InvtDocType : Edm.String "Inventory Doc. Type"
PX.Objects.SO.SOShipment.InvtRefNbr : Edm.String "Inventory Ref. Nbr."
PX.Objects.SO.SOShipment.IsMaterialRelated : Edm.Boolean "IsMaterialRelated"
PX.Objects.SO.SOShipment.HasDeliverySettings : Edm.Boolean "HasDeliverySettings"
PX.Objects.SO.SOShipment.ExtCarrierServiceMethod : Edm.String
PX.Objects.SO.SOShipment.ShipperCountry : Edm.String
PX.Objects.SO.SOShipment.FreightClass : Edm.String "Freight Class"
PX.Objects.SO.SOShipment.SkipAddressVerification : Edm.Boolean [required] "Skip Address Verification"
PX.Objects.SO.SOShipment.ManifestNbr : Edm.String "Manifest number"
PX.Objects.SO.SOShipment.TermsOfSale : Edm.String "Terms of Sale (Incoterms)"
PX.Objects.SO.SOShipment.EndorsementService : Edm.String "Endorsement"
PX.Objects.SO.SOShipment.DeliveryConfirmation : Edm.String "Delivery Confirmation"
PX.Objects.SO.SOShipment.DHLBillingRef : Edm.String "Billing Reference # (DHL)"
PX.Objects.SO.SOShipment.BrokerContactID : Edm.Int32 "Broker"
PX.Objects.SO.SOShipment.RequireOldWorkflow : Edm.Boolean [required]
PX.Objects.SO.SOShipment.PJExternalStatus : Edm.String
PX.Objects.SO.SOShipment.ExtCarrierPlugIn : Edm.String
PX.Objects.SO.SOShipment.ExtIsExternalCarrierPlugIn : Edm.Boolean
PX.Objects.SO.SOShipment.ExtUseScenario : Edm.String
PX.Objects.SO.SOShipment.RequestDate : Edm.DateTimeOffset "Requested On"
PX.Objects.SO.SOShipment.ShipToAddressValidatedWithExternalCarrier : Edm.Boolean [required] "ShipToAddressValidatedWithExternalCarrier"
PX.Objects.SO.SOShipment.CuryRate : Edm.Decimal
PX.Objects.SO.SOShipment.CuryViewState : Edm.Boolean
PX.Objects.SO.SOShipment.SOAddressByShipAddressID -> PX.Objects.SO.SOAddress (ShipAddressID=AddressID)
PX.Objects.SO.SOShipment.SOContactByShipContactID -> PX.Objects.SO.SOContact (ShipContactID=ContactID)
PX.Objects.SO.SOShipment.BAccountByCustomerID -> PX.Objects.CR.BAccount (CustomerID=BAccountID)
PX.Objects.SO.SOShipment.CustomerByCustomerID -> PX.Objects.AR.Customer (CustomerID=BAccountID)
PX.Objects.SO.SOShipment.ContactByOwnerID -> PX.Objects.CR.Contact (OwnerID=ContactID)
PX.Objects.SO.SOShipment.ContactByBrokerContactID -> PX.Objects.CR.Contact (BrokerContactID=ContactID)
PX.Objects.SO.SOShipment.CurrencyInfoByCuryInfoID -> PX.Objects.CM.CurrencyInfo (CuryInfoID=CuryInfoID)
PX.Objects.SO.SOShipment.UsersByConfirmedByID -> PX.SM.Users (ConfirmedByID=PKID)
PX.Objects.SO.SOShipment.UsersByCreatedByID -> PX.SM.Users (CreatedByID=PKID)
PX.Objects.SO.SOShipment.UsersByLastModifiedByID -> PX.SM.Users (LastModifiedByID=PKID)
PX.Objects.SO.SOShipment.EPCompanyTreeByWorkgroupID -> PX.TM.EPCompanyTree (WorkgroupID=WorkGroupID)
PX.Objects.SO.SOShipment.TaxCategoryByTaxCategoryID -> PX.Objects.TX.TaxCategory (TaxCategoryID=TaxCategoryID)
PX.Objects.SO.SOShipment.SOPickingWorksheetByCurrentWorksheetNbr -> PX.Objects.SO.SOPickingWorksheet (CurrentWorksheetNbr=WorksheetNbr)
PX.Objects.SO.SOShipment.CarrierByShipVia -> PX.Objects.CS.Carrier (ShipVia=CarrierID)
PX.Objects.SO.SOShipment.FOBPointByFOBPoint -> PX.Objects.CS.FOBPoint (FOBPoint=FOBPointID)
PX.Objects.SO.SOShipment.ShippingZoneByShipZoneID -> PX.Objects.CS.ShippingZone (ShipZoneID=ZoneID)
PX.Objects.SO.SOShipment.ShipTermsByShipTermsID -> PX.Objects.CS.ShipTerms (ShipTermsID=ShipTermsID)
PX.Objects.SO.SOShipment.INSiteBySiteID -> PX.Objects.IN.INSite
PX.Objects.SO.SOShipment.INSiteByDestinationSiteID -> PX.Objects.IN.INSite (DestinationSiteID=SiteID)
PX.Objects.SO.SOShipment.CurrencyByCuryID -> PX.Objects.CM.Currency (CuryID=CuryID)
PX.Objects.SO.SOShipment.LocationByCustomerLocationID -> PX.Objects.CR.Location (CustomerID=BAccountID)
PX.Objects.SO.SOShipment.LocationByCustomerID -> PX.Objects.CR.Location (CustomerID=BAccountID)
PX.Objects.SO.SOShipment.SOPackageDetailCollection -> Collection(PX.Objects.SO.SOPackageDetail)
PX.Objects.SO.SOShipment.INTranCollection -> Collection(PX.Objects.IN.INTran)
PX.Objects.SO.SOShipment.INRegisterCollection -> Collection(PX.Objects.IN.INRegister)
PX.Objects.SO.SOShipment.POReceiptLineCollection -> Collection(PX.Objects.PO.POReceiptLine)
PX.Objects.SO.SOShipment.SOFreightDetailCollection -> Collection(PX.Objects.SO.SOFreightDetail)
PX.Objects.SO.SOShipment.SOLineSplitCollection -> Collection(PX.Objects.SO.SOLineSplit)
PX.Objects.SO.SOShipment.SOOrderShipmentCollection -> Collection(PX.Objects.SO.SOOrderShipment)
PX.Objects.SO.SOShipment.SOPickerListEntryCollection -> Collection(PX.Objects.SO.SOPickerListEntry)
PX.Objects.SO.SOShipment.SOPickerToShipmentLinkCollection -> Collection(PX.Objects.SO.SOPickerToShipmentLink)
PX.Objects.SO.SOShipment.SOPickingWorksheetCollection -> Collection(PX.Objects.SO.SOPickingWorksheet)
PX.Objects.SO.SOShipment.SOPickingWorksheetShipmentCollection -> Collection(PX.Objects.SO.SOPickingWorksheetShipment)
PX.Objects.SO.SOShipment.SOShipLineCollection -> Collection(PX.Objects.SO.SOShipLine)
PX.Objects.SO.SOShipment.SOShipLineSplitCollection -> Collection(PX.Objects.SO.SOShipLineSplit)
PX.Objects.SO.SOShipment.SOShipLineSplitPackageCollection -> Collection(PX.Objects.SO.SOShipLineSplitPackage)
PX.Objects.SO.SOShipment.SOShipmentDiscountDetailCollection -> Collection(PX.Objects.SO.SOShipmentDiscountDetail)
PX.Objects.SO.SOShipment.SOShipmentSplitToCartSplitLinkCollection -> Collection(PX.Objects.SO.SOShipmentSplitToCartSplitLink)
PX.Objects.SO.SOShipment.POReceiptCollection -> Collection(PX.Objects.PO.POReceipt)
PX.Objects.SO.SOShipment.POReceiptToShipmentLinkCollection -> Collection(PX.Objects.PO.POReceiptToShipmentLink)
PX.Objects.SO.SOShipment.MNMaterialListShipmentCollection -> Collection(PX.Objects.MN.MNMaterialListShipment)
PX.Objects.SO.SOShipment.INTransitLineCollection -> Collection(PX.Objects.IN.INTransitLine)
PX.Objects.SO.SOShipment.SOShipmentCarrierDataCollection -> Collection(PX.ExternalCarriersHelper.SOShipmentCarrierData)
PX.Objects.SO.SOShipment.FSSODetSplitCollection -> Collection(PX.Objects.FS.FSSODetSplit)
PX.Objects.SO.SOShipment.SOShipmentProcessedByUserCollection -> Collection(PX.Objects.SO.SOShipmentProcessedByUser)
PX.Objects.SO.SOShipment.IntercompanyReturnedGoodsInTransitResultCollection -> Collection(PX.Objects.IN.IntercompanyReturnedGoodsInTransitResult)
PX.Objects.SO.SOShipment.SOCartShipmentCollection -> Collection(PX.Objects.SO.SOCartShipment)
PX.Objects.SO.SOShipment.IntercompanyGoodsInTransitResultCollection -> Collection(PX.Objects.IN.IntercompanyGoodsInTransitResult)

# PX.Objects.SO.SOShipmentAddress (EntityType)

Label: "Shipment Address"
BaseType: PX.Objects.SO.SOAddress
Key: AddressID (inherited from PX.Objects.SO.SOAddress)
Entity sets: PX_Objects_SO_SOShipmentAddress, ShipmentAddress, SOShipmentAddress

# PX.Objects.SO.SOShipmentContact (EntityType)

Label: "Shipment Contact"
BaseType: PX.Objects.SO.SOContact
Key: ContactID (inherited from PX.Objects.SO.SOContact)
Entity sets: PX_Objects_SO_SOShipmentContact, ShipmentContact, SOShipmentContact

# PX.Objects.SO.SOShipmentDiscountDetail (EntityType)

Label: "Shipment Discount Detail"
Key: OrderNbr, OrderType, RecordID, ShipmentNbr, Type
Entity sets: PX_Objects_SO_SOShipmentDiscountDetail, ShipmentDiscountDetail, SOShipmentDiscountDetail
Non-filterable, non-selectable: IsOrigDocDiscount

PX.Objects.SO.SOShipmentDiscountDetail.RecordID : Edm.Int32 [key]
PX.Objects.SO.SOShipmentDiscountDetail.LineNbr : Edm.Int32
PX.Objects.SO.SOShipmentDiscountDetail.SkipDiscount : Edm.Boolean [required] "Skip Discount"
PX.Objects.SO.SOShipmentDiscountDetail.ShipmentNbr : Edm.String [key] "ShipmentNbr"
PX.Objects.SO.SOShipmentDiscountDetail.OrderType : Edm.String [key] "Order Type"
PX.Objects.SO.SOShipmentDiscountDetail.OrderNbr : Edm.String [key] "Order Nbr."
PX.Objects.SO.SOShipmentDiscountDetail.DiscountID : Edm.String "Discount ID"
PX.Objects.SO.SOShipmentDiscountDetail.DiscountSequenceID : Edm.String "Sequence ID"
PX.Objects.SO.SOShipmentDiscountDetail.Type : Edm.String [key] "Type"
PX.Objects.SO.SOShipmentDiscountDetail.DiscountableQty : Edm.Decimal "Discountable Qty."
PX.Objects.SO.SOShipmentDiscountDetail.FreeItemID : Edm.Int32 "Free Item"
PX.Objects.SO.SOShipmentDiscountDetail.FreeItemQty : Edm.Decimal "Free Item Qty."
PX.Objects.SO.SOShipmentDiscountDetail.IsManual : Edm.Boolean [required] "Manual Discount"
PX.Objects.SO.SOShipmentDiscountDetail.IsOrigDocDiscount : Edm.Boolean
PX.Objects.SO.SOShipmentDiscountDetail.ExtDiscCode : Edm.String "External Discount Code"
PX.Objects.SO.SOShipmentDiscountDetail.Description : Edm.String "Description"
PX.Objects.SO.SOShipmentDiscountDetail.tstamp : Edm.Binary
PX.Objects.SO.SOShipmentDiscountDetail.CreatedByID : Edm.Guid "Created By"
PX.Objects.SO.SOShipmentDiscountDetail.CreatedByScreenID : Edm.String
PX.Objects.SO.SOShipmentDiscountDetail.CreatedDateTime : Edm.DateTimeOffset
PX.Objects.SO.SOShipmentDiscountDetail.LastModifiedByID : Edm.Guid "Last Modified By"
PX.Objects.SO.SOShipmentDiscountDetail.LastModifiedByScreenID : Edm.String
PX.Objects.SO.SOShipmentDiscountDetail.LastModifiedDateTime : Edm.DateTimeOffset
PX.Objects.SO.SOShipmentDiscountDetail.InventoryItemByFreeItemID -> PX.Objects.IN.InventoryItem (FreeItemID=InventoryID)
PX.Objects.SO.SOShipmentDiscountDetail.SOOrderByOrderNbr -> PX.Objects.SO.SOOrder (OrderType=OrderType, OrderNbr=OrderNbr)
PX.Objects.SO.SOShipmentDiscountDetail.UsersByCreatedByID -> PX.SM.Users (CreatedByID=PKID)
PX.Objects.SO.SOShipmentDiscountDetail.UsersByLastModifiedByID -> PX.SM.Users (LastModifiedByID=PKID)
PX.Objects.SO.SOShipmentDiscountDetail.SOOrderTypeByOrderType -> PX.Objects.SO.SOOrderType (OrderType=OrderType)
PX.Objects.SO.SOShipmentDiscountDetail.SOShipmentByShipmentNbr -> PX.Objects.SO.SOShipment (ShipmentNbr=ShipmentNbr)
PX.Objects.SO.SOShipmentDiscountDetail.ARDiscountByDiscountID -> PX.Objects.AR.ARDiscount (DiscountID=DiscountID)
PX.Objects.SO.SOShipmentDiscountDetail.DiscountSequenceByDiscountSequenceID -> PX.Objects.AR.DiscountSequence (DiscountID=DiscountID, DiscountSequenceID=DiscountSequenceID)

# PX.Objects.SO.SOShipmentManifest (EntityType)

Label: "SOShipmentManifest"
Key: ManifestNbr
Entity sets: PX_Objects_SO_SOShipmentManifest, SOShipmentManifest
Non-filterable, non-selectable: NoteText

PX.Objects.SO.SOShipmentManifest.ManifestNbr : Edm.String [key]
PX.Objects.SO.SOShipmentManifest.CreatedByID : Edm.Guid "Created By"
PX.Objects.SO.SOShipmentManifest.CreatedByScreenID : Edm.String
PX.Objects.SO.SOShipmentManifest.CreatedDateTime : Edm.DateTimeOffset
PX.Objects.SO.SOShipmentManifest.NoteID : Edm.Guid
PX.Objects.SO.SOShipmentManifest.NoteText : Edm.String "Note Text"
PX.Objects.SO.SOShipmentManifest.tstamp : Edm.Binary
PX.Objects.SO.SOShipmentManifest.UsersByCreatedByID -> PX.SM.Users (CreatedByID=PKID)

# PX.Objects.SO.SOShipmentPlan (EntityType)

Key: OrderNbr, OrderType, PlanID
Entity sets: PX_Objects_SO_SOShipmentPlan

PX.Objects.SO.SOShipmentPlan.OrderType : Edm.String [key]
PX.Objects.SO.SOShipmentPlan.OrderNbr : Edm.String [key]
PX.Objects.SO.SOShipmentPlan.DestinationSiteID : Edm.Int32 "Destination Warehouse"
PX.Objects.SO.SOShipmentPlan.InventoryID : Edm.Int32 "Inventory ID"
PX.Objects.SO.SOShipmentPlan.SubItemID : Edm.Int32
PX.Objects.SO.SOShipmentPlan.SiteID : Edm.Int32
PX.Objects.SO.SOShipmentPlan.LotSerialNbr : Edm.String
PX.Objects.SO.SOShipmentPlan.PlanType : Edm.String
PX.Objects.SO.SOShipmentPlan.PlanDate : Edm.DateTimeOffset "Sched. Ship. Date"
PX.Objects.SO.SOShipmentPlan.PlanID : Edm.Int64 [key]
PX.Objects.SO.SOShipmentPlan.DemandPlanID : Edm.Int64
PX.Objects.SO.SOShipmentPlan.PlanQty : Edm.Decimal
PX.Objects.SO.SOShipmentPlan.Reverse : Edm.Boolean
PX.Objects.SO.SOShipmentPlan.InclQtySOBackOrdered : Edm.Int16
PX.Objects.SO.SOShipmentPlan.InclQtySOShipping : Edm.Int16
PX.Objects.SO.SOShipmentPlan.InclQtySOShipped : Edm.Int16
PX.Objects.SO.SOShipmentPlan.RequireAllocation : Edm.Boolean
PX.Objects.SO.SOShipmentPlan.IsManualPackage : Edm.Boolean
PX.Objects.SO.SOShipmentPlan.INSiteBySiteID -> PX.Objects.IN.INSite (SiteID=SiteID)
PX.Objects.SO.SOShipmentPlan.SOOrderTypeByOrderType -> PX.Objects.SO.SOOrderType (OrderType=OrderType)
PX.Objects.SO.SOShipmentPlan.SOOrderTypeByOrigOrderType -> PX.Objects.SO.SOOrderType
PX.Objects.SO.SOShipmentPlan.INItemPlanBySupplyPlanID -> PX.Objects.IN.INItemPlan
PX.Objects.SO.SOShipmentPlan.INItemPlanByPlanID -> PX.Objects.IN.INItemPlan (PlanID=DemandPlanID)
PX.Objects.SO.SOShipmentPlan.INSiteBySourceSiteID -> PX.Objects.IN.INSite
PX.Objects.SO.SOShipmentPlan.INSubItemBySubItemID -> PX.Objects.IN.INSubItem (SubItemID=SubItemID)
PX.Objects.SO.SOShipmentPlan.INPlanTypeByPlanType -> PX.Objects.IN.INPlanType (PlanType=PlanType)
PX.Objects.SO.SOShipmentPlan.INPlanTypeByOrigPlanType -> PX.Objects.IN.INPlanType
PX.Objects.SO.SOShipmentPlan.SOTaxTranCollection -> Collection(PX.Objects.SO.SOTaxTran)
PX.Objects.SO.SOShipmentPlan.SOBlanketOrderLinkCollection -> Collection(PX.Objects.SO.SOBlanketOrderLink)
PX.Objects.SO.SOShipmentPlan.SOPackageInfoCollection -> Collection(PX.Objects.SO.SOPackageInfo)
PX.Objects.SO.SOShipmentPlan.SOTaxCollection -> Collection(PX.Objects.SO.SOTax)
PX.Objects.SO.SOShipmentPlan.SOOrderCollection -> Collection(PX.Objects.SO.SOOrder)
PX.Objects.SO.SOShipmentPlan.POOrderCollection -> Collection(PX.Objects.PO.POOrder)
PX.Objects.SO.SOShipmentPlan.INTranCollection -> Collection(PX.Objects.IN.INTran)
PX.Objects.SO.SOShipmentPlan.INRegisterCollection -> Collection(PX.Objects.IN.INRegister)
PX.Objects.SO.SOShipmentPlan.ARAdjustCollection -> Collection(PX.Objects.AR.ARAdjust)
PX.Objects.SO.SOShipmentPlan.AMProdItemCollection -> Collection(PX.Objects.AM.AMProdItem)
PX.Objects.SO.SOShipmentPlan.AMFixedDemandCollection -> Collection(PX.Objects.AM.AMFixedDemand)
PX.Objects.SO.SOShipmentPlan.SOLineCollection -> Collection(PX.Objects.SO.SOLine)
PX.Objects.SO.SOShipmentPlan.FSEquipmentCollection -> Collection(PX.Objects.FS.FSEquipment)
PX.Objects.SO.SOShipmentPlan.POReceiptLineCollection -> Collection(PX.Objects.PO.POReceiptLine)
PX.Objects.SO.SOShipmentPlan.ARTranCollection -> Collection(PX.Objects.AR.ARTran)
PX.Objects.SO.SOShipmentPlan.SOAdjustCollection -> Collection(PX.Objects.SO.SOAdjust)
PX.Objects.SO.SOShipmentPlan.InvoiceSplitCollection -> Collection(PX.Objects.SO.DAC.Projections.InvoiceSplit)
PX.Objects.SO.SOShipmentPlan.CCPayLinkCollection -> Collection(PX.Objects.CC.CCPayLink)
PX.Objects.SO.SOShipmentPlan.SOFreightDetailCollection -> Collection(PX.Objects.SO.SOFreightDetail)
PX.Objects.SO.SOShipmentPlan.SOLineSplitCollection -> Collection(PX.Objects.SO.SOLineSplit)
PX.Objects.SO.SOShipmentPlan.SOOrderDiscountDetailCollection -> Collection(PX.Objects.SO.SOOrderDiscountDetail)
PX.Objects.SO.SOShipmentPlan.SOOrderShipmentCollection -> Collection(PX.Objects.SO.SOOrderShipment)
PX.Objects.SO.SOShipmentPlan.SOOrderSiteCollection -> Collection(PX.Objects.SO.SOOrderSite)
PX.Objects.SO.SOShipmentPlan.SOSalesPerTranCollection -> Collection(PX.Objects.SO.SOSalesPerTran)
PX.Objects.SO.SOShipmentPlan.SOShipLineCollection -> Collection(PX.Objects.SO.SOShipLine)
PX.Objects.SO.SOShipmentPlan.SOShipLineSplitCollection -> Collection(PX.Objects.SO.SOShipLineSplit)
PX.Objects.SO.SOShipmentPlan.SOShipmentDiscountDetailCollection -> Collection(PX.Objects.SO.SOShipmentDiscountDetail)
PX.Objects.SO.SOShipmentPlan.POReceiptCollection -> Collection(PX.Objects.PO.POReceipt)
PX.Objects.SO.SOShipmentPlan.POReceiptToShipmentLinkCollection -> Collection(PX.Objects.PO.POReceiptToShipmentLink)
PX.Objects.SO.SOShipmentPlan.INReplenishmentLineCollection -> Collection(PX.Objects.IN.INReplenishmentLine)
PX.Objects.SO.SOShipmentPlan.INTransitLineCollection -> Collection(PX.Objects.IN.INTransitLine)
PX.Objects.SO.SOShipmentPlan.RelatedItemHistoryCollection -> Collection(PX.Objects.IN.RelatedItems.RelatedItemHistory)
PX.Objects.SO.SOShipmentPlan.ARInvoiceDiscountDetailCollection -> Collection(PX.Objects.AR.ARInvoiceDiscountDetail)
PX.Objects.SO.SOShipmentPlan.ARPaymentTotalsCollection -> Collection(PX.Objects.AR.ARPaymentTotals)
PX.Objects.SO.SOShipmentPlan.SOOrderCarrierDataCollection -> Collection(PX.ExternalCarriersHelper.SOOrderCarrierData)
PX.Objects.SO.SOShipmentPlan.AMConfigurationResultsCollection -> Collection(PX.Objects.AM.AMConfigurationResults)
PX.Objects.SO.SOShipmentPlan.AMEstimateReferenceCollection -> Collection(PX.Objects.AM.AMEstimateReference)
PX.Objects.SO.SOShipmentPlan.FSEquipmentComponentCollection -> Collection(PX.Objects.FS.FSEquipmentComponent)
PX.Objects.SO.SOShipmentPlan.FSPostDetCollection -> Collection(PX.Objects.FS.FSPostDet)
PX.Objects.SO.SOShipmentPlan.FSPostInfoCollection -> Collection(PX.Objects.FS.FSPostInfo)
PX.Objects.SO.SOShipmentPlan.SchedulerWCOperationCollection -> Collection(PX.Objects.AM.SchedulerWCOperation)
PX.Objects.SO.SOShipmentPlan.SchedulerProductionOrderCollection -> Collection(PX.Objects.AM.SchedulerProductionOrder)
PX.Objects.SO.SOShipmentPlan.DropShipSOLineCollection -> Collection(PX.Objects.SO.DropShipSOLine)
PX.Objects.SO.SOShipmentPlan.RQRequisitionOrderCollection -> Collection(PX.Objects.RQ.RQRequisitionOrder)
PX.Objects.SO.SOShipmentPlan.DropShipPOLineCollection -> Collection(PX.Objects.PO.DropShipPOLine)
PX.Objects.SO.SOShipmentPlan.SOInvoiceCollection -> Collection(PX.Objects.SO.SOInvoice)
PX.Objects.SO.SOShipmentPlan.SalesAllocationCollection -> Collection(PX.Objects.SO.SalesAllocation)
PX.Objects.SO.SOShipmentPlan.SOLine2Collection -> Collection(PX.Objects.SO.SOLine2)
PX.Objects.SO.SOShipmentPlan.SOLine4Collection -> Collection(PX.Objects.SO.SOLine4)
PX.Objects.SO.SOShipmentPlan.SOMiscLine2Collection -> Collection(PX.Objects.SO.SOMiscLine2)
PX.Objects.SO.SOShipmentPlan.BlanketSOLineSplitCollection -> Collection(PX.Objects.SO.DAC.Projections.BlanketSOLineSplit)
PX.Objects.SO.SOShipmentPlan.IntercompanyReturnedGoodsInTransitResultCollection -> Collection(PX.Objects.IN.IntercompanyReturnedGoodsInTransitResult)
PX.Objects.SO.SOShipmentPlan.ExternalTransactionCollection -> Collection(PX.Objects.AR.ExternalTransaction)
PX.Objects.SO.SOShipmentPlan.SOOrderRisksCollection -> Collection(PX.Commerce.Objects.SOOrderRisks)
PX.Objects.SO.SOShipmentPlan.AMConfigurationKeysCollection -> Collection(PX.Objects.AM.AMConfigurationKeys)
PX.Objects.SO.SOShipmentPlan.SchedulerMachineOperationCollection -> Collection(PX.Objects.AM.SchedulerMachineOperation)
PX.Objects.SO.SOShipmentPlan.INItemPlanCollection -> Collection(PX.Objects.IN.INItemPlan)
PX.Objects.SO.SOShipmentPlan.AMRPDetailFPCollection -> Collection(PX.Objects.AM.AMRPDetailFP)
PX.Objects.SO.SOShipmentPlan.AMRPDetailPlanCollection -> Collection(PX.Objects.AM.AMRPDetailPlan)
PX.Objects.SO.SOShipmentPlan.POLineCollection -> Collection(PX.Objects.PO.POLine)
PX.Objects.SO.SOShipmentPlan.INTranSplitCollection -> Collection(PX.Objects.IN.INTranSplit)
PX.Objects.SO.SOShipmentPlan.POReceiptLineSplitCollection -> Collection(PX.Objects.PO.POReceiptLineSplit)
PX.Objects.SO.SOShipmentPlan.AMProdItemSplitCollection -> Collection(PX.Objects.AM.AMProdItemSplit)
PX.Objects.SO.SOShipmentPlan.AMProdMatlSplitCollection -> Collection(PX.Objects.AM.AMProdMatlSplit)
PX.Objects.SO.SOShipmentPlan.FSSODetSplitCollection -> Collection(PX.Objects.FS.FSSODetSplit)
PX.Objects.SO.SOShipmentPlan.INKitTranSplitCollection -> Collection(PX.Objects.IN.INKitTranSplit)
PX.Objects.SO.SOShipmentPlan.FSSODetFSSODetSplitCollection -> Collection(PX.Objects.FS.FSSODetFSSODetSplit)

# PX.Objects.SO.SOShipmentProcessedByUser (EntityType)

Label: "SO Shipment Processed by User"
Key: RecordID
Entity sets: PX_Objects_SO_SOShipmentProcessedByUser, SOShipmentProcessedbyUser
Non-filterable, non-selectable: PickListNbr

PX.Objects.SO.SOShipmentProcessedByUser.RecordID : Edm.Int32 [key]
PX.Objects.SO.SOShipmentProcessedByUser.JobType : Edm.String "Operation Type"
PX.Objects.SO.SOShipmentProcessedByUser.DocType : Edm.String
PX.Objects.SO.SOShipmentProcessedByUser.ShipmentNbr : Edm.String
PX.Objects.SO.SOShipmentProcessedByUser.WorksheetNbr : Edm.String
PX.Objects.SO.SOShipmentProcessedByUser.PickerNbr : Edm.Int32
PX.Objects.SO.SOShipmentProcessedByUser.PickListNbr : Edm.String "Pick List Nbr."
PX.Objects.SO.SOShipmentProcessedByUser.UserID : Edm.Guid
PX.Objects.SO.SOShipmentProcessedByUser.Confirmed : Edm.Boolean [required]
PX.Objects.SO.SOShipmentProcessedByUser.NumberOfScans : Edm.Int32 [required]
PX.Objects.SO.SOShipmentProcessedByUser.NumberOfFailedScans : Edm.Int32 [required]
PX.Objects.SO.SOShipmentProcessedByUser.OverallStartDateTime : Edm.DateTimeOffset
PX.Objects.SO.SOShipmentProcessedByUser.StartDateTime : Edm.DateTimeOffset
PX.Objects.SO.SOShipmentProcessedByUser.LastModifiedDateTime : Edm.DateTimeOffset
PX.Objects.SO.SOShipmentProcessedByUser.EndDateTime : Edm.DateTimeOffset
PX.Objects.SO.SOShipmentProcessedByUser.OverallEndDateTime : Edm.DateTimeOffset
PX.Objects.SO.SOShipmentProcessedByUser.UsersByUserID -> PX.SM.Users (UserID=PKID)
PX.Objects.SO.SOShipmentProcessedByUser.SOPickerByPickerNbr -> PX.Objects.SO.SOPicker (WorksheetNbr=WorksheetNbr, PickerNbr=PickerNbr)
PX.Objects.SO.SOShipmentProcessedByUser.SOPickingWorksheetByWorksheetNbr -> PX.Objects.SO.SOPickingWorksheet (WorksheetNbr=WorksheetNbr)
PX.Objects.SO.SOShipmentProcessedByUser.SOShipmentByShipmentNbr -> PX.Objects.SO.SOShipment (ShipmentNbr=ShipmentNbr)

# PX.Objects.SO.SOShipmentSplitToCartSplitLink (EntityType)

Label: "Shipment Line Split To Cart Split Link"
Key: CartID, CartSplitLineNbr, ShipmentLineNbr, ShipmentNbr, ShipmentSplitLineNbr, SiteID
Entity sets: PX_Objects_SO_SOShipmentSplitToCartSplitLink, ShipmentLineSplitToCartSplitLink, SOShipmentSplitToCartSplitLink

PX.Objects.SO.SOShipmentSplitToCartSplitLink.ShipmentNbr : Edm.String [key]
PX.Objects.SO.SOShipmentSplitToCartSplitLink.ShipmentLineNbr : Edm.Int32 [key]
PX.Objects.SO.SOShipmentSplitToCartSplitLink.ShipmentSplitLineNbr : Edm.Int32 [key]
PX.Objects.SO.SOShipmentSplitToCartSplitLink.SiteID : Edm.Int32 [key] "Warehouse"
PX.Objects.SO.SOShipmentSplitToCartSplitLink.CartID : Edm.Int32 [key]
PX.Objects.SO.SOShipmentSplitToCartSplitLink.CartSplitLineNbr : Edm.Int32 [key]
PX.Objects.SO.SOShipmentSplitToCartSplitLink.Qty : Edm.Decimal [required] "Quantity"
PX.Objects.SO.SOShipmentSplitToCartSplitLink.CreatedByID : Edm.Guid "Created By"
PX.Objects.SO.SOShipmentSplitToCartSplitLink.CreatedByScreenID : Edm.String
PX.Objects.SO.SOShipmentSplitToCartSplitLink.CreatedDateTime : Edm.DateTimeOffset
PX.Objects.SO.SOShipmentSplitToCartSplitLink.LastModifiedByID : Edm.Guid "Last Modified By"
PX.Objects.SO.SOShipmentSplitToCartSplitLink.LastModifiedByScreenID : Edm.String
PX.Objects.SO.SOShipmentSplitToCartSplitLink.LastModifiedDateTime : Edm.DateTimeOffset
PX.Objects.SO.SOShipmentSplitToCartSplitLink.tstamp : Edm.Binary
PX.Objects.SO.SOShipmentSplitToCartSplitLink.UsersByCreatedByID -> PX.SM.Users (CreatedByID=PKID)
PX.Objects.SO.SOShipmentSplitToCartSplitLink.UsersByLastModifiedByID -> PX.SM.Users (LastModifiedByID=PKID)
PX.Objects.SO.SOShipmentSplitToCartSplitLink.SOShipLineByShipmentLineNbr -> PX.Objects.SO.SOShipLine (ShipmentNbr=ShipmentNbr, ShipmentLineNbr=LineNbr)
PX.Objects.SO.SOShipmentSplitToCartSplitLink.SOShipLineSplitByShipmentSplitLineNbr -> PX.Objects.SO.SOShipLineSplit (ShipmentNbr=ShipmentNbr, ShipmentLineNbr=LineNbr, ShipmentSplitLineNbr=SplitLineNbr)
PX.Objects.SO.SOShipmentSplitToCartSplitLink.SOShipmentByShipmentNbr -> PX.Objects.SO.SOShipment (ShipmentNbr=ShipmentNbr)
PX.Objects.SO.SOShipmentSplitToCartSplitLink.INCartByCartID -> PX.Objects.IN.INCart (SiteID=SiteID, CartID=CartID)
PX.Objects.SO.SOShipmentSplitToCartSplitLink.INCartSplitByCartSplitLineNbr -> PX.Objects.IN.INCartSplit (SiteID=SiteID, CartID=CartID, CartSplitLineNbr=SplitLineNbr)
PX.Objects.SO.SOShipmentSplitToCartSplitLink.INSiteBySiteID -> PX.Objects.IN.INSite (SiteID=SiteID)

# PX.Objects.SO.SOShippingAddress (EntityType)

Label: "Shipping Address"
BaseType: PX.Objects.SO.SOAddress
Key: AddressID (inherited from PX.Objects.SO.SOAddress)
Entity sets: PX_Objects_SO_SOShippingAddress, ShippingAddress1, SOShippingAddress

# PX.Objects.SO.SOShippingContact (EntityType)

Label: "Shipping Contact"
BaseType: PX.Objects.SO.SOContact
Key: ContactID (inherited from PX.Objects.SO.SOContact)
Entity sets: PX_Objects_SO_SOShippingContact, ShippingContact1, SOShippingContact

# PX.Objects.SO.SOTax (EntityType)

Label: "SO Tax Detail"
Key: LineNbr, OrderNbr, OrderType, TaxID
Entity sets: PX_Objects_SO_SOTax, SOTaxDetail, SOTax
Non-filterable, non-selectable: NonDeductibleTaxRate, CuryID, CuryRate, CuryViewState

PX.Objects.SO.SOTax.TaxRate : Edm.Decimal [required] "Tax Rate"
PX.Objects.SO.SOTax.NonDeductibleTaxRate : Edm.Decimal "Deductible Tax Rate"
PX.Objects.SO.SOTax.ExpenseAmt : Edm.Decimal "Expense Amount"
PX.Objects.SO.SOTax.CreatedByID : Edm.Guid "Created By"
PX.Objects.SO.SOTax.CreatedByScreenID : Edm.String
PX.Objects.SO.SOTax.CreatedDateTime : Edm.DateTimeOffset
PX.Objects.SO.SOTax.LastModifiedByID : Edm.Guid "Last Modified By"
PX.Objects.SO.SOTax.LastModifiedByScreenID : Edm.String
PX.Objects.SO.SOTax.LastModifiedDateTime : Edm.DateTimeOffset
PX.Objects.SO.SOTax.OrderType : Edm.String [key]
PX.Objects.SO.SOTax.OrderNbr : Edm.String [key]
PX.Objects.SO.SOTax.LineNbr : Edm.Int32 [key] "Line Nbr."
PX.Objects.SO.SOTax.TaxID : Edm.String [key] "Tax ID"
PX.Objects.SO.SOTax.CuryInfoID : Edm.Int64
PX.Objects.SO.SOTax.CuryTaxableAmt : Edm.Decimal [required] "Taxable Amount"
PX.Objects.SO.SOTax.CuryUnshippedTaxableAmt : Edm.Decimal [required] "Unshipped Taxable Amount"
PX.Objects.SO.SOTax.CuryUnbilledTaxableAmt : Edm.Decimal [required] "Unbilled Taxable Amount"
PX.Objects.SO.SOTax.TaxableAmt : Edm.Decimal [required] "Taxable Amount"
PX.Objects.SO.SOTax.UnshippedTaxableAmt : Edm.Decimal [required]
PX.Objects.SO.SOTax.UnbilledTaxableAmt : Edm.Decimal [required]
PX.Objects.SO.SOTax.UnshippedTaxableQty : Edm.Decimal [required] "Unshipped Taxable Qty."
PX.Objects.SO.SOTax.UnbilledTaxableQty : Edm.Decimal [required] "Unbilled Taxable Qty."
PX.Objects.SO.SOTax.CuryTaxAmt : Edm.Decimal [required] "Tax Amount"
PX.Objects.SO.SOTax.CuryUnshippedTaxAmt : Edm.Decimal [required] "Unshipped Tax Amount"
PX.Objects.SO.SOTax.CuryUnbilledTaxAmt : Edm.Decimal [required] "Unbilled Tax Amount"
PX.Objects.SO.SOTax.TaxAmt : Edm.Decimal [required] "Tax Amount"
PX.Objects.SO.SOTax.CuryExpenseAmt : Edm.Decimal "Expense Amount"
PX.Objects.SO.SOTax.UnshippedTaxAmt : Edm.Decimal [required]
PX.Objects.SO.SOTax.UnbilledTaxAmt : Edm.Decimal [required]
PX.Objects.SO.SOTax.TaxZoneID : Edm.String
PX.Objects.SO.SOTax.CuryID : Edm.String "Currency"
PX.Objects.SO.SOTax.CuryRate : Edm.Decimal
PX.Objects.SO.SOTax.CuryViewState : Edm.Boolean
PX.Objects.SO.SOTax.SOOrderByOrderNbr -> PX.Objects.SO.SOOrder (OrderType=OrderType, OrderNbr=OrderNbr)
PX.Objects.SO.SOTax.CurrencyInfoByCuryInfoID -> PX.Objects.CM.CurrencyInfo (CuryInfoID=CuryInfoID)
PX.Objects.SO.SOTax.UsersByCreatedByID -> PX.SM.Users (CreatedByID=PKID)
PX.Objects.SO.SOTax.UsersByLastModifiedByID -> PX.SM.Users (LastModifiedByID=PKID)
PX.Objects.SO.SOTax.TaxByTaxID -> PX.Objects.TX.Tax (TaxID=TaxID)
PX.Objects.SO.SOTax.TaxZoneByTaxZoneID -> PX.Objects.TX.TaxZone (TaxZoneID=TaxZoneID)
PX.Objects.SO.SOTax.SOLineByLineNbr -> PX.Objects.SO.SOLine (OrderType=OrderType, OrderNbr=OrderNbr, LineNbr=LineNbr)
PX.Objects.SO.SOTax.SOOrderTypeByOrderType -> PX.Objects.SO.SOOrderType (OrderType=OrderType)
PX.Objects.SO.SOTax.INUnitByTaxUOM -> PX.Objects.IN.INUnit
PX.Objects.SO.SOTax.SOLine2ByLineNbr -> PX.Objects.SO.SOLine2 (OrderType=OrderType, OrderNbr=OrderNbr, LineNbr=LineNbr)
PX.Objects.SO.SOTax.SOLine4ByLineNbr -> PX.Objects.SO.SOLine4 (OrderType=OrderType, OrderNbr=OrderNbr, LineNbr=LineNbr)
PX.Objects.SO.SOTax.SOMiscLine2ByLineNbr -> PX.Objects.SO.SOMiscLine2 (OrderType=OrderType, OrderNbr=OrderNbr, LineNbr=LineNbr)
PX.Objects.SO.SOTax.BlanketSOLineByLineNbr -> PX.Objects.SO.DAC.Projections.BlanketSOLine (OrderType=OrderType, OrderNbr=OrderNbr, LineNbr=LineNbr)
PX.Objects.SO.SOTax.SOTaxTranCollection -> Collection(PX.Objects.SO.SOTaxTran)

# PX.Objects.SO.SOTaxTran (EntityType)

Label: "Sales Order Tax"
Key: LineNbr, OrderNbr, OrderType, RecordID, TaxID, TaxZoneID
Entity sets: PX_Objects_SO_SOTaxTran, SalesOrderTax, SOTaxTran
Non-filterable, non-selectable: NonDeductibleTaxRate, CuryID, CuryRate, CuryViewState

PX.Objects.SO.SOTaxTran.TaxRate : Edm.Decimal [required] "Tax Rate"
PX.Objects.SO.SOTaxTran.NonDeductibleTaxRate : Edm.Decimal "Deductible Tax Rate"
PX.Objects.SO.SOTaxTran.ExpenseAmt : Edm.Decimal "Expense Amount"
PX.Objects.SO.SOTaxTran.CreatedByID : Edm.Guid "Created By"
PX.Objects.SO.SOTaxTran.CreatedByScreenID : Edm.String
PX.Objects.SO.SOTaxTran.CreatedDateTime : Edm.DateTimeOffset
PX.Objects.SO.SOTaxTran.LastModifiedByID : Edm.Guid "Last Modified By"
PX.Objects.SO.SOTaxTran.LastModifiedByScreenID : Edm.String
PX.Objects.SO.SOTaxTran.LastModifiedDateTime : Edm.DateTimeOffset
PX.Objects.SO.SOTaxTran.OrderType : Edm.String [key] "Order Type"
PX.Objects.SO.SOTaxTran.OrderNbr : Edm.String [key] "Order Nbr."
PX.Objects.SO.SOTaxTran.LineNbr : Edm.Int32 [key required] "Line Nbr."
PX.Objects.SO.SOTaxTran.TaxID : Edm.String [key] "Tax ID"
PX.Objects.SO.SOTaxTran.RecordID : Edm.Int32 [key]
PX.Objects.SO.SOTaxTran.JurisType : Edm.String "Tax Jurisdiction Type"
PX.Objects.SO.SOTaxTran.JurisName : Edm.String "Tax Jurisdiction Name"
PX.Objects.SO.SOTaxTran.CuryInfoID : Edm.Int64
PX.Objects.SO.SOTaxTran.CuryTaxableAmt : Edm.Decimal [required] "Taxable Amount"
PX.Objects.SO.SOTaxTran.CuryUnshippedTaxableAmt : Edm.Decimal [required] "Unshipped Taxable Amount"
PX.Objects.SO.SOTaxTran.CuryUnbilledTaxableAmt : Edm.Decimal [required] "Unbilled Taxable Amount"
PX.Objects.SO.SOTaxTran.TaxableAmt : Edm.Decimal [required] "Taxable Amount"
PX.Objects.SO.SOTaxTran.UnshippedTaxableAmt : Edm.Decimal [required]
PX.Objects.SO.SOTaxTran.UnbilledTaxableAmt : Edm.Decimal [required]
PX.Objects.SO.SOTaxTran.CuryTaxAmt : Edm.Decimal [required] "Tax Amount"
PX.Objects.SO.SOTaxTran.CuryUnshippedTaxAmt : Edm.Decimal [required] "Unshipped Tax Amount"
PX.Objects.SO.SOTaxTran.CuryUnbilledTaxAmt : Edm.Decimal [required] "Unbilled Tax Amount"
PX.Objects.SO.SOTaxTran.UnshippedTaxableQty : Edm.Decimal [required] "Unshipped Taxable Qty."
PX.Objects.SO.SOTaxTran.UnbilledTaxableQty : Edm.Decimal [required] "Unbilled Taxable Qty."
PX.Objects.SO.SOTaxTran.TaxAmt : Edm.Decimal [required] "Tax Amount"
PX.Objects.SO.SOTaxTran.CuryExpenseAmt : Edm.Decimal "Expense Amount"
PX.Objects.SO.SOTaxTran.UnshippedTaxAmt : Edm.Decimal [required]
PX.Objects.SO.SOTaxTran.UnbilledTaxAmt : Edm.Decimal [required]
PX.Objects.SO.SOTaxTran.TaxZoneID : Edm.String [key] "Customer Tax Zone"
PX.Objects.SO.SOTaxTran.tstamp : Edm.Binary
PX.Objects.SO.SOTaxTran.IsTaxInclusive : Edm.Boolean [required] "Tax Inclusive"
PX.Objects.SO.SOTaxTran.CuryID : Edm.String "Currency"
PX.Objects.SO.SOTaxTran.CuryRate : Edm.Decimal
PX.Objects.SO.SOTaxTran.CuryViewState : Edm.Boolean
PX.Objects.SO.SOTaxTran.SOTaxByTaxID -> PX.Objects.SO.SOTax (OrderType=OrderType, OrderNbr=OrderNbr, LineNbr=LineNbr, TaxID=TaxID)
PX.Objects.SO.SOTaxTran.SOOrderByOrderNbr -> PX.Objects.SO.SOOrder (OrderType=OrderType, OrderNbr=OrderNbr)
PX.Objects.SO.SOTaxTran.CurrencyInfoByCuryInfoID -> PX.Objects.CM.CurrencyInfo (CuryInfoID=CuryInfoID)
PX.Objects.SO.SOTaxTran.UsersByCreatedByID -> PX.SM.Users (CreatedByID=PKID)
PX.Objects.SO.SOTaxTran.UsersByLastModifiedByID -> PX.SM.Users (LastModifiedByID=PKID)
PX.Objects.SO.SOTaxTran.TaxByTaxID -> PX.Objects.TX.Tax (TaxID=TaxID)
PX.Objects.SO.SOTaxTran.TaxZoneByTaxZoneID -> PX.Objects.TX.TaxZone (TaxZoneID=TaxZoneID)
PX.Objects.SO.SOTaxTran.SOLineByLineNbr -> PX.Objects.SO.SOLine (OrderType=OrderType, OrderNbr=OrderNbr, LineNbr=LineNbr)
PX.Objects.SO.SOTaxTran.INUnitByTaxUOM -> PX.Objects.IN.INUnit

# PX.Objects.SO.SOTaxTranImported (EntityType)

Label: "Sales Order Tax"
BaseType: PX.Objects.SO.SOTaxTran
Key: LineNbr, OrderNbr, OrderType, RecordID, TaxID, TaxZoneID (inherited from PX.Objects.SO.SOTaxTran)
Entity sets: PX_Objects_SO_SOTaxTranImported

# PX.Objects.SO.Standalone.SOOwner (EntityType)

Label: "Employee"
BaseType: PX.Objects.EP.EPEmployee
Key: AcctCD (inherited from PX.Objects.CR.BAccount)
Entity sets: PX_Objects_SO_Standalone_SOOwner, Employee2, SOOwner

# PX.Objects.SO.SupplyPOLine (EntityType)

Label: "Supply PO Line"
Key: LineNbr, OrderNbr, OrderType
Entity sets: PX_Objects_SO_SupplyPOLine, SupplyPOLine
Non-filterable, non-selectable: BaseDemandQty

PX.Objects.SO.SupplyPOLine.BaseDemandQty : Edm.Decimal
PX.Objects.SO.SupplyPOLine.OrderType : Edm.String [key] "PO Type"
PX.Objects.SO.SupplyPOLine.OrderNbr : Edm.String [key] "PO Nbr."
PX.Objects.SO.SupplyPOLine.LineNbr : Edm.Int32 [key] "PO Line Nbr."
PX.Objects.SO.SupplyPOLine.LineType : Edm.String "Line Type"
PX.Objects.SO.SupplyPOLine.InventoryID : Edm.Int32 "Inventory ID"
PX.Objects.SO.SupplyPOLine.PlanID : Edm.Int64 "PlanID"
PX.Objects.SO.SupplyPOLine.VendorID : Edm.Int32 "Vendor"
PX.Objects.SO.SupplyPOLine.VendorRefNbr : Edm.String "Vendor Ref."
PX.Objects.SO.SupplyPOLine.Hold : Edm.Boolean
PX.Objects.SO.SupplyPOLine.OrderDate : Edm.DateTimeOffset "Order Date"
PX.Objects.SO.SupplyPOLine.PromisedDate : Edm.DateTimeOffset "Promised"
PX.Objects.SO.SupplyPOLine.Cancelled : Edm.Boolean
PX.Objects.SO.SupplyPOLine.Completed : Edm.Boolean
PX.Objects.SO.SupplyPOLine.Closed : Edm.Boolean
PX.Objects.SO.SupplyPOLine.SiteID : Edm.Int32
PX.Objects.SO.SupplyPOLine.UOM : Edm.String "UOM"
PX.Objects.SO.SupplyPOLine.OrderQty : Edm.Decimal "Order Qty."
PX.Objects.SO.SupplyPOLine.BaseOrderQty : Edm.Decimal
PX.Objects.SO.SupplyPOLine.OpenQty : Edm.Decimal "Open Qty."
PX.Objects.SO.SupplyPOLine.BaseOpenQty : Edm.Decimal
PX.Objects.SO.SupplyPOLine.ReceivedQty : Edm.Decimal
PX.Objects.SO.SupplyPOLine.BaseReceivedQty : Edm.Decimal
PX.Objects.SO.SupplyPOLine.TranDesc : Edm.String "Line Description"
PX.Objects.SO.SupplyPOLine.ProjectID : Edm.Int32
PX.Objects.SO.SupplyPOLine.TaskID : Edm.Int32
PX.Objects.SO.SupplyPOLine.CostCodeID : Edm.Int32
PX.Objects.SO.SupplyPOLine.IsSpecialOrder : Edm.Boolean
PX.Objects.SO.SupplyPOLine.CostCenterID : Edm.Int32
PX.Objects.SO.SupplyPOLine.SODeleted : Edm.Boolean
PX.Objects.SO.SupplyPOLine.CuryID : Edm.String "Currency"
PX.Objects.SO.SupplyPOLine.CuryUnitCost : Edm.Decimal "Unit Cost"
PX.Objects.SO.SupplyPOLine.BaseBilledQty : Edm.Decimal
PX.Objects.SO.SupplyPOLine.MaterialListNoteID : Edm.Guid
PX.Objects.SO.SupplyPOLine.MaterialListLineNbr : Edm.Int32
PX.Objects.SO.SupplyPOLine.tstamp : Edm.Binary
PX.Objects.SO.SupplyPOLine.LastModifiedByID : Edm.Guid "Last Modified By"
PX.Objects.SO.SupplyPOLine.LastModifiedByScreenID : Edm.String
PX.Objects.SO.SupplyPOLine.LastModifiedDateTime : Edm.DateTimeOffset
PX.Objects.SO.SupplyPOLine.POOrderByOrderType -> PX.Objects.PO.POOrder (OrderNbr=OrderNbr, OrderType=OrderType)
PX.Objects.SO.SupplyPOLine.PMProjectByProjectID -> PX.Objects.PM.PMProject (ProjectID=ContractID)
PX.Objects.SO.SupplyPOLine.POOrderByOrderNbr -> PX.Objects.PO.POOrder (OrderType=OrderType, OrderNbr=OrderNbr)
PX.Objects.SO.SupplyPOLine.PMTaskByTaskID -> PX.Objects.PM.PMTask (ProjectID=ProjectID, TaskID=TaskID)
PX.Objects.SO.SupplyPOLine.PMTaskByProjectID -> PX.Objects.PM.PMTask (TaskID=TaskID, ProjectID=ProjectID)
PX.Objects.SO.SupplyPOLine.INItemPlanByPlanID -> PX.Objects.IN.INItemPlan (PlanID=PlanID)
PX.Objects.SO.SupplyPOLine.PMCostCodeByCostCodeID -> PX.Objects.PM.PMCostCode (CostCodeID=CostCodeID)
PX.Objects.SO.SupplyPOLine.INSiteBySiteID -> PX.Objects.IN.INSite (SiteID=SiteID)
PX.Objects.SO.SupplyPOLine.SOLineSplitCollection -> Collection(PX.Objects.SO.SOLineSplit)
PX.Objects.SO.SupplyPOLine.DropShipLinkCollection -> Collection(PX.Objects.Common.DAC.DropShipLink)
PX.Objects.SO.SupplyPOLine.POTaxTranCollection -> Collection(PX.Objects.PO.POTaxTran)
PX.Objects.SO.SupplyPOLine.POTaxCollection -> Collection(PX.Objects.PO.POTax)
PX.Objects.SO.SupplyPOLine.POReceiptLineCollection -> Collection(PX.Objects.PO.POReceiptLine)
PX.Objects.SO.SupplyPOLine.APTranCollection -> Collection(PX.Objects.AP.APTran)
PX.Objects.SO.SupplyPOLine.POAccrualStatusCollection -> Collection(PX.Objects.PO.POAccrualStatus)
PX.Objects.SO.SupplyPOLine.PMChangeOrderLineCollection -> Collection(PX.Objects.PM.PMChangeOrderLine)
PX.Objects.SO.SupplyPOLine.PMChangeRequestLineCollection -> Collection(PX.Objects.PM.PMChangeRequestLine)
PX.Objects.SO.SupplyPOLine.MNMaterialListLineSplitCollection -> Collection(PX.Objects.MN.MNMaterialListLineSplit)
PX.Objects.SO.SupplyPOLine.INReplenishmentLineCollection -> Collection(PX.Objects.IN.INReplenishmentLine)
PX.Objects.SO.SupplyPOLine.ComplianceDocumentCollection -> Collection(PX.Objects.CN.Compliance.CL.DAC.ComplianceDocument)
PX.Objects.SO.SupplyPOLine.FSApptLineSplitCollection -> Collection(PX.Objects.FS.FSApptLineSplit)
PX.Objects.SO.SupplyPOLine.FSSODetSplitCollection -> Collection(PX.Objects.FS.FSSODetSplit)
PX.Objects.SO.SupplyPOLine.POReceiptLineSCollection -> Collection(PX.Objects.PO.POReceiptLineS)

# PX.Objects.SO.Table.SOShipLineSplit (EntityType)

Key: LineNbr, ShipmentNbr, SplitLineNbr
Entity sets: PX_Objects_SO_Table_SOShipLineSplit
Non-filterable, non-selectable: TranType, LastLotSerialNbr, LotSerClassID, AssignedNbr, ProjectID, TaskID

PX.Objects.SO.Table.SOShipLineSplit.ShipmentNbr : Edm.String [key]
PX.Objects.SO.Table.SOShipLineSplit.LineNbr : Edm.Int32 [key]
PX.Objects.SO.Table.SOShipLineSplit.OrigOrderType : Edm.String
PX.Objects.SO.Table.SOShipLineSplit.OrigOrderNbr : Edm.String
PX.Objects.SO.Table.SOShipLineSplit.OrigLineNbr : Edm.Int32
PX.Objects.SO.Table.SOShipLineSplit.OrigSplitLineNbr : Edm.Int32
PX.Objects.SO.Table.SOShipLineSplit.OrigPlanType : Edm.String
PX.Objects.SO.Table.SOShipLineSplit.Operation : Edm.String
PX.Objects.SO.Table.SOShipLineSplit.SplitLineNbr : Edm.Int32 [key]
PX.Objects.SO.Table.SOShipLineSplit.InvtMult : Edm.Int16
PX.Objects.SO.Table.SOShipLineSplit.InventoryID : Edm.Int32 "Inventory ID"
PX.Objects.SO.Table.SOShipLineSplit.LineType : Edm.String
PX.Objects.SO.Table.SOShipLineSplit.IsStockItem : Edm.Boolean
PX.Objects.SO.Table.SOShipLineSplit.IsComponentItem : Edm.Boolean
PX.Objects.SO.Table.SOShipLineSplit.IsIntercompany : Edm.Boolean
PX.Objects.SO.Table.SOShipLineSplit.TranType : Edm.String
PX.Objects.SO.Table.SOShipLineSplit.PlanType : Edm.String
PX.Objects.SO.Table.SOShipLineSplit.PlanID : Edm.Int64
PX.Objects.SO.Table.SOShipLineSplit.LastLotSerialNbr : Edm.String
PX.Objects.SO.Table.SOShipLineSplit.LotSerClassID : Edm.String
PX.Objects.SO.Table.SOShipLineSplit.AssignedNbr : Edm.String
PX.Objects.SO.Table.SOShipLineSplit.HasGeneratedLotSerialNbr : Edm.Boolean [required]
PX.Objects.SO.Table.SOShipLineSplit.UOM : Edm.String "UOM"
PX.Objects.SO.Table.SOShipLineSplit.Qty : Edm.Decimal [required] "Quantity"
PX.Objects.SO.Table.SOShipLineSplit.BaseQty : Edm.Decimal
PX.Objects.SO.Table.SOShipLineSplit.PickedQty : Edm.Decimal [required] "Picked Quantity"
PX.Objects.SO.Table.SOShipLineSplit.BasePickedQty : Edm.Decimal
PX.Objects.SO.Table.SOShipLineSplit.PackedQty : Edm.Decimal [required] "Packed Quantity"
PX.Objects.SO.Table.SOShipLineSplit.BasePackedQty : Edm.Decimal
PX.Objects.SO.Table.SOShipLineSplit.ShipDate : Edm.DateTimeOffset
PX.Objects.SO.Table.SOShipLineSplit.Confirmed : Edm.Boolean "Confirmed"
PX.Objects.SO.Table.SOShipLineSplit.Released : Edm.Boolean "Released"
PX.Objects.SO.Table.SOShipLineSplit.IsUnassigned : Edm.Boolean
PX.Objects.SO.Table.SOShipLineSplit.ProjectID : Edm.Int32
PX.Objects.SO.Table.SOShipLineSplit.TaskID : Edm.Int32
PX.Objects.SO.Table.SOShipLineSplit.CreatedByID : Edm.Guid "Created By"
PX.Objects.SO.Table.SOShipLineSplit.CreatedByScreenID : Edm.String
PX.Objects.SO.Table.SOShipLineSplit.CreatedDateTime : Edm.DateTimeOffset
PX.Objects.SO.Table.SOShipLineSplit.LastModifiedByID : Edm.Guid "Last Modified By"
PX.Objects.SO.Table.SOShipLineSplit.LastModifiedByScreenID : Edm.String
PX.Objects.SO.Table.SOShipLineSplit.LastModifiedDateTime : Edm.DateTimeOffset
PX.Objects.SO.Table.SOShipLineSplit.tstamp : Edm.Binary
PX.Objects.SO.Table.SOShipLineSplit.BeforeChangeLotSerialNbr : Edm.String
PX.Objects.SO.Table.SOShipLineSplit.AllocationChangedDateTime : Edm.DateTimeOffset
PX.Objects.SO.Table.SOShipLineSplit.AllocationChangedUserID : Edm.Guid
PX.Objects.SO.Table.SOShipLineSplit.OriginalLotSerialNbr : Edm.String
PX.Objects.SO.Table.SOShipLineSplit.InventoryItemByInventoryID -> PX.Objects.IN.InventoryItem (InventoryID=InventoryID)
PX.Objects.SO.Table.SOShipLineSplit.SOOrderByOrigOrderNbr -> PX.Objects.SO.SOOrder (OrigOrderType=OrderType, OrigOrderNbr=OrderNbr)
PX.Objects.SO.Table.SOShipLineSplit.INItemPlanByPlanID -> PX.Objects.IN.INItemPlan (PlanID=PlanID)
PX.Objects.SO.Table.SOShipLineSplit.UsersByCreatedByID -> PX.SM.Users (CreatedByID=PKID)
PX.Objects.SO.Table.SOShipLineSplit.UsersByLastModifiedByID -> PX.SM.Users (LastModifiedByID=PKID)
PX.Objects.SO.Table.SOShipLineSplit.SOLineByOrigLineNbr -> PX.Objects.SO.SOLine (OrigOrderType=OrderType, OrigOrderNbr=OrderNbr, OrigLineNbr=LineNbr)
PX.Objects.SO.Table.SOShipLineSplit.SOLineSplitByOrigSplitLineNbr -> PX.Objects.SO.SOLineSplit (OrigOrderType=OrderType, OrigOrderNbr=OrderNbr, OrigLineNbr=LineNbr, OrigSplitLineNbr=SplitLineNbr)
PX.Objects.SO.Table.SOShipLineSplit.SOOrderTypeByOrigOrderType -> PX.Objects.SO.SOOrderType (OrigOrderType=OrderType)
PX.Objects.SO.Table.SOShipLineSplit.SOOrderTypeOperationByOperation -> PX.Objects.SO.SOOrderTypeOperation (OrigOrderType=OrderType, Operation=Operation)
PX.Objects.SO.Table.SOShipLineSplit.SOOrderTypeOperationByOrigOrderType -> PX.Objects.SO.SOOrderTypeOperation (Operation=Operation, OrigOrderType=OrderType)
PX.Objects.SO.Table.SOShipLineSplit.SOShipLineByLineNbr -> PX.Objects.SO.SOShipLine (ShipmentNbr=ShipmentNbr, LineNbr=LineNbr)
PX.Objects.SO.Table.SOShipLineSplit.SOShipmentByShipmentNbr -> PX.Objects.SO.SOShipment (ShipmentNbr=ShipmentNbr)
PX.Objects.SO.Table.SOShipLineSplit.INLocationByLocationID -> PX.Objects.IN.INLocation
PX.Objects.SO.Table.SOShipLineSplit.INLocationBySiteID -> PX.Objects.IN.INLocation
PX.Objects.SO.Table.SOShipLineSplit.INSiteBySiteID -> PX.Objects.IN.INSite
PX.Objects.SO.Table.SOShipLineSplit.INSubItemBySubItemID -> PX.Objects.IN.INSubItem
PX.Objects.SO.Table.SOShipLineSplit.INUnitByInventoryID -> PX.Objects.IN.INUnit (UOM=FromUnit, InventoryID=InventoryID)
PX.Objects.SO.Table.SOShipLineSplit.INSiteZoneByWarehouseZoneID -> PX.Objects.IN.DAC.INSiteZone
PX.Objects.SO.Table.SOShipLineSplit.INSiteZoneBySiteID -> PX.Objects.IN.DAC.INSiteZone
PX.Objects.SO.Table.SOShipLineSplit.INLotSerialStatusByCostCenterByLocationID -> PX.Objects.IN.INLotSerialStatusByCostCenter (InventoryID=InventoryID)
PX.Objects.SO.Table.SOShipLineSplit.INLocationStatusByLocationID -> PX.Objects.IN.INLocationStatus (InventoryID=InventoryID)
PX.Objects.SO.Table.SOShipLineSplit.INLotSerialStatusByLotSerialNbr -> PX.Objects.IN.INLotSerialStatus (InventoryID=InventoryID)
PX.Objects.SO.Table.SOShipLineSplit.INSiteStatusBySiteID -> PX.Objects.IN.INSiteStatus (InventoryID=InventoryID)
PX.Objects.SO.Table.SOShipLineSplit.INPlanTypeByPlanType -> PX.Objects.IN.INPlanType (PlanType=PlanType)
PX.Objects.SO.Table.SOShipLineSplit.INPlanTypeByOrigPlanType -> PX.Objects.IN.INPlanType (OrigPlanType=PlanType)
PX.Objects.SO.Table.SOShipLineSplit.SOShipLineSplitPackageCollection -> Collection(PX.Objects.SO.SOShipLineSplitPackage)
PX.Objects.SO.Table.SOShipLineSplit.SOShipmentSplitToCartSplitLinkCollection -> Collection(PX.Objects.SO.SOShipmentSplitToCartSplitLink)

# PX.Objects.SV.DACUnbound.SVWorkHistoryItem (EntityType)

Label: "Work History"
Key: NoteID, TicketNbr
Entity sets: PX_Objects_SV_DACUnbound_SVWorkHistoryItem, WorkHistory, SVWorkHistoryItem

PX.Objects.SV.DACUnbound.SVWorkHistoryItem.TicketNbr : Edm.String [key] "Work Ticket"
PX.Objects.SV.DACUnbound.SVWorkHistoryItem.Summary : Edm.String "Ticket Summary"
PX.Objects.SV.DACUnbound.SVWorkHistoryItem.DocDate : Edm.DateTimeOffset "Date"
PX.Objects.SV.DACUnbound.SVWorkHistoryItem.Status : Edm.String "Status"
PX.Objects.SV.DACUnbound.SVWorkHistoryItem.RefNoteIDType : Edm.String
PX.Objects.SV.DACUnbound.SVWorkHistoryItem.RefNoteID : Edm.Guid
PX.Objects.SV.DACUnbound.SVWorkHistoryItem.NoteID : Edm.Guid [key]
PX.Objects.SV.DACUnbound.SVWorkHistoryItem.SVTicketByTicketNbr -> PX.Objects.SV.SVTicket (TicketNbr=TicketNbr)
PX.Objects.SV.DACUnbound.SVWorkHistoryItem.SVTicketDetailCollection -> Collection(PX.Objects.SV.SVTicketDetail)
PX.Objects.SV.DACUnbound.SVWorkHistoryItem.SVOrderActualCollection -> Collection(PX.Objects.SV.SVOrderActual)
PX.Objects.SV.DACUnbound.SVWorkHistoryItem.SVWorkHistoryItemCollection -> Collection(PX.Objects.SV.DACUnbound.SVWorkHistoryItem)

# PX.Objects.SV.FSEmployeeSkill (EntityType)

Label: "Staff Skill"
Key: EmployeeID, SkillID
Entity sets: PX_Objects_SV_FSEmployeeSkill, StaffSkill, FSEmployeeSkill
Non-filterable, non-selectable: NoteText

PX.Objects.SV.FSEmployeeSkill.EmployeeID : Edm.Int32 [key] "Staff Member"
PX.Objects.SV.FSEmployeeSkill.SkillID : Edm.Int32 [key] "Skill ID"
PX.Objects.SV.FSEmployeeSkill.NoteID : Edm.Guid
PX.Objects.SV.FSEmployeeSkill.NoteText : Edm.String "Note Text"
PX.Objects.SV.FSEmployeeSkill.CreatedByID : Edm.Guid "Created By"
PX.Objects.SV.FSEmployeeSkill.CreatedByScreenID : Edm.String "CreatedByScreenID"
PX.Objects.SV.FSEmployeeSkill.CreatedDateTime : Edm.DateTimeOffset "CreatedDateTime"
PX.Objects.SV.FSEmployeeSkill.LastModifiedByID : Edm.Guid "Last Modified By"
PX.Objects.SV.FSEmployeeSkill.LastModifiedByScreenID : Edm.String "LastModifiedByScreenID"
PX.Objects.SV.FSEmployeeSkill.LastModifiedDateTime : Edm.DateTimeOffset "LastModifiedDateTime"
PX.Objects.SV.FSEmployeeSkill.tstamp : Edm.Binary
PX.Objects.SV.FSEmployeeSkill.EPEmployeeByEmployeeID -> PX.Objects.EP.EPEmployee (EmployeeID=BAccountID)
PX.Objects.SV.FSEmployeeSkill.VendorByEmployeeID -> PX.Objects.AP.Vendor (EmployeeID=BAccountID)
PX.Objects.SV.FSEmployeeSkill.FSSkillBySkillID -> PX.Objects.SV.FSSkill (SkillID=SkillID)
PX.Objects.SV.FSEmployeeSkill.UsersByCreatedByID -> PX.SM.Users (CreatedByID=PKID)
PX.Objects.SV.FSEmployeeSkill.UsersByLastModifiedByID -> PX.SM.Users (LastModifiedByID=PKID)

# PX.Objects.SV.FSGeoZone (EntityType)

Label: "Service Area"
Key: GeoZoneCD
Entity sets: PX_Objects_SV_FSGeoZone, ServiceArea1, FSGeoZone1
Non-filterable, non-selectable: NoteText

PX.Objects.SV.FSGeoZone.GeoZoneID : Edm.Int32
PX.Objects.SV.FSGeoZone.GeoZoneCD : Edm.String [key] "Service Area ID"
PX.Objects.SV.FSGeoZone.CountryID : Edm.String "Country"
PX.Objects.SV.FSGeoZone.Descr : Edm.String "Description"
PX.Objects.SV.FSGeoZone.NoteID : Edm.Guid "NoteID"
PX.Objects.SV.FSGeoZone.NoteText : Edm.String "Note Text"
PX.Objects.SV.FSGeoZone.CreatedByID : Edm.Guid "Created By"
PX.Objects.SV.FSGeoZone.CreatedByScreenID : Edm.String "Created By Screen ID"
PX.Objects.SV.FSGeoZone.CreatedDateTime : Edm.DateTimeOffset "Created On"
PX.Objects.SV.FSGeoZone.LastModifiedByID : Edm.Guid "Last Modified By"
PX.Objects.SV.FSGeoZone.LastModifiedByScreenID : Edm.String "Last Modified By Screen ID"
PX.Objects.SV.FSGeoZone.LastModifiedDateTime : Edm.DateTimeOffset "Last Modified On"
PX.Objects.SV.FSGeoZone.tstamp : Edm.Binary
PX.Objects.SV.FSGeoZone.UsersByCreatedByID -> PX.SM.Users (CreatedByID=PKID)
PX.Objects.SV.FSGeoZone.UsersByLastModifiedByID -> PX.SM.Users (LastModifiedByID=PKID)
PX.Objects.SV.FSGeoZone.CountryByCountryID -> PX.Objects.CS.Country (CountryID=CountryID)
PX.Objects.SV.FSGeoZone.FSGeoZonePostalCodeCollection -> Collection(PX.Objects.SV.FSGeoZonePostalCode)
PX.Objects.SV.FSGeoZone.FSGeoZoneEmpCollection -> Collection(PX.Objects.FS.FSGeoZoneEmp)
PX.Objects.SV.FSGeoZone.SVServiceLocationCollection -> Collection(PX.Objects.SV.SVServiceLocation)
PX.Objects.SV.FSGeoZone.RouteAppointmentInfoCollection -> Collection(PX.Objects.FS.RouteAppointmentInfo)
PX.Objects.SV.FSGeoZone.PostingBatchDetailCollection -> Collection(PX.Objects.FS.PostingBatchDetail)

# PX.Objects.SV.FSGeoZonePostalCode (EntityType)

Label: "Postal Code"
Key: GeoZoneID, PostalCode
Entity sets: PX_Objects_SV_FSGeoZonePostalCode, PostalCode, FSGeoZonePostalCode1

PX.Objects.SV.FSGeoZonePostalCode.GeoZoneID : Edm.Int32 [key] "Service Area"
PX.Objects.SV.FSGeoZonePostalCode.CountryID : Edm.String "Country"
PX.Objects.SV.FSGeoZonePostalCode.PostalCode : Edm.String [key] "Postal Code"
PX.Objects.SV.FSGeoZonePostalCode.CreatedByID : Edm.Guid "Created By"
PX.Objects.SV.FSGeoZonePostalCode.CreatedByScreenID : Edm.String "CreatedByScreenID"
PX.Objects.SV.FSGeoZonePostalCode.CreatedDateTime : Edm.DateTimeOffset "CreatedDateTime"
PX.Objects.SV.FSGeoZonePostalCode.LastModifiedByID : Edm.Guid "Last Modified By"
PX.Objects.SV.FSGeoZonePostalCode.LastModifiedByScreenID : Edm.String "LastModifiedByScreenID"
PX.Objects.SV.FSGeoZonePostalCode.LastModifiedDateTime : Edm.DateTimeOffset "LastModifiedDateTime"
PX.Objects.SV.FSGeoZonePostalCode.tstamp : Edm.Binary
PX.Objects.SV.FSGeoZonePostalCode.FSGeoZoneByGeoZoneID -> PX.Objects.SV.FSGeoZone (GeoZoneID=GeoZoneID)
PX.Objects.SV.FSGeoZonePostalCode.UsersByCreatedByID -> PX.SM.Users (CreatedByID=PKID)
PX.Objects.SV.FSGeoZonePostalCode.UsersByLastModifiedByID -> PX.SM.Users (LastModifiedByID=PKID)
PX.Objects.SV.FSGeoZonePostalCode.CountryByCountryID -> PX.Objects.CS.Country (CountryID=CountryID)

# PX.Objects.SV.FSLicense (EntityType)

Label: "Staff License"
Key: RefNbr
Entity sets: PX_Objects_SV_FSLicense, StaffLicense, FSLicense1
Non-filterable, non-selectable: NoteText

PX.Objects.SV.FSLicense.LicenseID : Edm.Int32
PX.Objects.SV.FSLicense.RefNbr : Edm.String [key] "License Nbr."
PX.Objects.SV.FSLicense.Descr : Edm.String "Description"
PX.Objects.SV.FSLicense.ExternalLicenseNbr : Edm.String "External License Nbr."
PX.Objects.SV.FSLicense.EmployeeID : Edm.Int32 "Staff Member"
PX.Objects.SV.FSLicense.ExpirationDate : Edm.DateTimeOffset "Expiration Date"
PX.Objects.SV.FSLicense.IssueDate : Edm.DateTimeOffset "Issue Date"
PX.Objects.SV.FSLicense.LicenseTypeID : Edm.Int32 "License Type"
PX.Objects.SV.FSLicense.NeverExpires : Edm.Boolean [required] "Never Expires"
PX.Objects.SV.FSLicense.NoteID : Edm.Guid "NoteID"
PX.Objects.SV.FSLicense.NoteText : Edm.String "Note Text"
PX.Objects.SV.FSLicense.CreatedByID : Edm.Guid "CreatedByID"
PX.Objects.SV.FSLicense.CreatedByScreenID : Edm.String "CreatedByScreenID"
PX.Objects.SV.FSLicense.CreatedDateTime : Edm.DateTimeOffset "CreatedDateTime"
PX.Objects.SV.FSLicense.LastModifiedByID : Edm.Guid "LastModifiedByID"
PX.Objects.SV.FSLicense.LastModifiedByScreenID : Edm.String "LastModifiedByScreenID"
PX.Objects.SV.FSLicense.LastModifiedDateTime : Edm.DateTimeOffset "LastModifiedDateTime"
PX.Objects.SV.FSLicense.tstamp : Edm.Binary
PX.Objects.SV.FSLicense.EPEmployeeByEmployeeID -> PX.Objects.EP.EPEmployee (EmployeeID=BAccountID)
PX.Objects.SV.FSLicense.VendorByEmployeeID -> PX.Objects.AP.Vendor (EmployeeID=BAccountID)
PX.Objects.SV.FSLicense.BAccountByEmployeeID -> PX.Objects.CR.BAccount (EmployeeID=BAccountID)
PX.Objects.SV.FSLicense.FSLicenseTypeByLicenseTypeID -> PX.Objects.SV.FSLicenseType (LicenseTypeID=LicenseTypeID)
PX.Objects.SV.FSLicense.UsersByCreatedByID -> PX.SM.Users (CreatedByID=PKID)
PX.Objects.SV.FSLicense.UsersByLastModifiedByID -> PX.SM.Users (LastModifiedByID=PKID)

# PX.Objects.SV.FSLicenseType (EntityType)

Label: "License Type"
Key: LicenseTypeCD
Entity sets: PX_Objects_SV_FSLicenseType, LicenseType1, FSLicenseType1
Non-filterable, non-selectable: NoteText, DeletedDatabaseRecord

PX.Objects.SV.FSLicenseType.LicenseTypeID : Edm.Int32
PX.Objects.SV.FSLicenseType.LicenseTypeCD : Edm.String [key] "License Type ID"
PX.Objects.SV.FSLicenseType.Descr : Edm.String "Description"
PX.Objects.SV.FSLicenseType.NoteID : Edm.Guid "NoteID"
PX.Objects.SV.FSLicenseType.NoteText : Edm.String "Note Text"
PX.Objects.SV.FSLicenseType.CreatedByID : Edm.Guid "CreatedByID"
PX.Objects.SV.FSLicenseType.CreatedByScreenID : Edm.String "CreatedByScreenID"
PX.Objects.SV.FSLicenseType.CreatedDateTime : Edm.DateTimeOffset "CreatedDateTime"
PX.Objects.SV.FSLicenseType.LastModifiedByID : Edm.Guid "LastModifiedByID"
PX.Objects.SV.FSLicenseType.LastModifiedByScreenID : Edm.String "LastModifiedByScreenID"
PX.Objects.SV.FSLicenseType.LastModifiedDateTime : Edm.DateTimeOffset "LastModifiedDateTime"
PX.Objects.SV.FSLicenseType.tstamp : Edm.Binary "tstamp"
PX.Objects.SV.FSLicenseType.DeletedDatabaseRecord : Edm.Boolean [required] "DeletedDatabaseRecord"
PX.Objects.SV.FSLicenseType.UsersByCreatedByID -> PX.SM.Users (CreatedByID=PKID)
PX.Objects.SV.FSLicenseType.UsersByLastModifiedByID -> PX.SM.Users (LastModifiedByID=PKID)
PX.Objects.SV.FSLicenseType.FSLicenseCollection -> Collection(PX.Objects.SV.FSLicense)
PX.Objects.SV.FSLicenseType.SVVendorLicenseCollection -> Collection(PX.Objects.SV.SVVendorLicense)
PX.Objects.SV.FSLicenseType.FSServiceLicenseTypeCollection -> Collection(PX.Objects.FS.FSServiceLicenseType)

# PX.Objects.SV.FSSetup (EntityType)

Label: "SV: Service Management Preferences"
Singletons: PX_Objects_SV_FSSetup, SVServiceManagementPreferences, FSSetup1

PX.Objects.SV.FSSetup.AppResizePrecision : Edm.Int32 [required] "Appointment Resize Precision"
PX.Objects.SV.FSSetup.CalendarID : Edm.String "Work Calendar"
PX.Objects.SV.FSSetup.ShowServiceOrderDaysGap : Edm.Int32 "Show Service Orders in a Period Of"
PX.Objects.SV.FSSetup.EmpSchedulePrecision : Edm.Int32 "Employee Schedule Precision"
PX.Objects.SV.FSSetup.InitialAppRefNbr : Edm.String "Initial Appointment Ref. Nbr."
PX.Objects.SV.FSSetup.DfltCalendarPageSize : Edm.Int32 "Number of Staff Members"
PX.Objects.SV.FSSetup.DaysAheadRecurringAppointments : Edm.Int32 [required] "Number of days ahead for recurring appointments"
PX.Objects.SV.FSSetup.EmpSchdlNumberingID : Edm.String "Staff Schedule Numbering Sequence"
PX.Objects.SV.FSSetup.LicenseNumberingID : Edm.String "License Numbering Sequence"
PX.Objects.SV.FSSetup.EquipmentNumberingID : Edm.String "Equipment Numbering Sequence"
PX.Objects.SV.FSSetup.ManageRooms : Edm.Boolean "Enable Rooms"
PX.Objects.SV.FSSetup.DfltBranchID : Edm.Int32
PX.Objects.SV.FSSetup.EnableEmpTimeCardIntegration : Edm.Boolean [required] "Enable Time & Expenses Integration"
PX.Objects.SV.FSSetup.PostBatchNumberingID : Edm.String "Batch Numbering Sequence"
PX.Objects.SV.FSSetup.ScheduleNumberingID : Edm.String "Service Contract Schedule Numbering Sequence"
PX.Objects.SV.FSSetup.ServiceContractNumberingID : Edm.String "Service Contract Numbering Sequence"
PX.Objects.SV.FSSetup.CustomerMultipleBillingOptions : Edm.Boolean [required] "Manage Multiple Billing Options per Customer"
PX.Objects.SV.FSSetup.AlertBeforeCloseServiceOrder : Edm.Boolean [required] "Alert About Open Appointments Before Service Orders Are Closed"
PX.Objects.SV.FSSetup.FilterInvoicingManually : Edm.Boolean [required] "Require Manual Filtering on Billing Forms"
PX.Objects.SV.FSSetup.EnableSeasonScheduleContract : Edm.Boolean [required] "Enable Seasons in Schedule Contracts"
PX.Objects.SV.FSSetup.DfltCalendarStartTime : Edm.DateTimeOffset "Day Start Time"
PX.Objects.SV.FSSetup.DfltCalendarEndTime : Edm.DateTimeOffset "Day End Time"
PX.Objects.SV.FSSetup.MapApiKey : Edm.String "Map API Key"
PX.Objects.SV.FSSetup.TrackAppointmentLocation : Edm.Boolean [required] "Track Start and Completion Appointment Locations"
PX.Objects.SV.FSSetup.EnableGPSTracking : Edm.Boolean [required] "Show Location Tracking"
PX.Objects.SV.FSSetup.GPSRefreshTrackingTime : Edm.Int32 [required] "Refresh GPS Locations Every"
PX.Objects.SV.FSSetup.HistoryDistanceAccuracy : Edm.Int32 [required] "History Distance Accuracy"
PX.Objects.SV.FSSetup.HistoryTimeAccuracy : Edm.Int32 [required] "History Time Accuracy"
PX.Objects.SV.FSSetup.DisableFixScheduleAction : Edm.Boolean [required] "Enable Fix Schedules Without Next Execution Date"
PX.Objects.SV.FSSetup.DfltContractTermIDARSO : Edm.String "Default Terms"
PX.Objects.SV.FSSetup.EnableContractPeriodWhenInvoice : Edm.Boolean [required] "Automatically Activate Upcoming Period"
PX.Objects.SV.FSSetup.ShowWorkflowStageField : Edm.Boolean [required] "Enable Workflow Stages"
PX.Objects.SV.FSSetup.CreatedByID : Edm.Guid "CreatedByID"
PX.Objects.SV.FSSetup.CreatedByScreenID : Edm.String "CreatedByScreenID"
PX.Objects.SV.FSSetup.CreatedDateTime : Edm.DateTimeOffset "CreatedDateTime"
PX.Objects.SV.FSSetup.LastModifiedByID : Edm.Guid "LastModifiedByID"
PX.Objects.SV.FSSetup.LastModifiedByScreenID : Edm.String "LastModifiedByScreenID"
PX.Objects.SV.FSSetup.LastModifiedDateTime : Edm.DateTimeOffset "LastModifiedDateTime"
PX.Objects.SV.FSSetup.tstamp : Edm.Binary "tstamp"
PX.Objects.SV.FSSetup.EnableAllTargetEquipment : Edm.Boolean [required] "Enable Service on All Target Equipment"
PX.Objects.SV.FSSetup.EnableDfltStaffOnServiceOrder : Edm.Boolean [required] "Enable Default Staff in Service Orders"
PX.Objects.SV.FSSetup.EnableDfltResEquipOnServiceOrder : Edm.Boolean [required] "Enable Default Resource Equipment in Service Orders"
PX.Objects.SV.FSSetup.ReadyToUpgradeTo2017R2 : Edm.Boolean [required]
PX.Objects.SV.FSSetup.NoteID : Edm.Guid
PX.Objects.SV.FSSetup.NoteText : Edm.String "Note Text"
PX.Objects.SV.FSSetup.CustomDfltCalendarStartTime : Edm.String
PX.Objects.SV.FSSetup.CustomDfltCalendarEndTime : Edm.String
PX.Objects.SV.FSSetup.UsersByCreatedByID -> PX.SM.Users (CreatedByID=PKID)
PX.Objects.SV.FSSetup.UsersByLastModifiedByID -> PX.SM.Users (LastModifiedByID=PKID)
PX.Objects.SV.FSSetup.NumberingByEmpSchdlNumberingID -> PX.Objects.CS.Numbering (EmpSchdlNumberingID=NumberingID)
PX.Objects.SV.FSSetup.NumberingByLicenseNumberingID -> PX.Objects.CS.Numbering (LicenseNumberingID=NumberingID)
PX.Objects.SV.FSSetup.NumberingByEquipmentNumberingID -> PX.Objects.CS.Numbering (EquipmentNumberingID=NumberingID)
PX.Objects.SV.FSSetup.NumberingByPostBatchNumberingID -> PX.Objects.CS.Numbering (PostBatchNumberingID=NumberingID)
PX.Objects.SV.FSSetup.NumberingByScheduleNumberingID -> PX.Objects.CS.Numbering (ScheduleNumberingID=NumberingID)
PX.Objects.SV.FSSetup.NumberingByServiceContractNumberingID -> PX.Objects.CS.Numbering (ServiceContractNumberingID=NumberingID)
PX.Objects.SV.FSSetup.TermsByDfltContractTermIDARSO -> PX.Objects.CS.Terms (DfltContractTermIDARSO=TermsID)
PX.Objects.SV.FSSetup.CSCalendarByCalendarID -> PX.Objects.CS.CSCalendar (CalendarID=CalendarID)

# PX.Objects.SV.FSSkill (EntityType)

Label: "Skill"
Key: SkillCD
Entity sets: PX_Objects_SV_FSSkill, Skill1, FSSkill1
Non-filterable, non-selectable: NoteText, DeletedDatabaseRecord

PX.Objects.SV.FSSkill.SkillID : Edm.Int32
PX.Objects.SV.FSSkill.SkillCD : Edm.String [key] "Skill ID"
PX.Objects.SV.FSSkill.Descr : Edm.String "Description"
PX.Objects.SV.FSSkill.IsDriverSkill : Edm.Boolean [required] "Driver Skill"
PX.Objects.SV.FSSkill.NoteID : Edm.Guid "NoteID"
PX.Objects.SV.FSSkill.NoteText : Edm.String "Note Text"
PX.Objects.SV.FSSkill.CreatedByID : Edm.Guid "CreatedByID"
PX.Objects.SV.FSSkill.CreatedByScreenID : Edm.String "CreatedByScreenID"
PX.Objects.SV.FSSkill.CreatedDateTime : Edm.DateTimeOffset "CreatedDateTime"
PX.Objects.SV.FSSkill.LastModifiedByID : Edm.Guid "LastModifiedByID"
PX.Objects.SV.FSSkill.LastModifiedByScreenID : Edm.String "LastModifiedByScreenID"
PX.Objects.SV.FSSkill.LastModifiedDateTime : Edm.DateTimeOffset "LastModifiedDateTime"
PX.Objects.SV.FSSkill.tstamp : Edm.Binary "tstamp"
PX.Objects.SV.FSSkill.DeletedDatabaseRecord : Edm.Boolean [required] "DeletedDatabaseRecord"
PX.Objects.SV.FSSkill.UsersByCreatedByID -> PX.SM.Users (CreatedByID=PKID)
PX.Objects.SV.FSSkill.UsersByLastModifiedByID -> PX.SM.Users (LastModifiedByID=PKID)
PX.Objects.SV.FSSkill.FSEmployeeSkillCollection -> Collection(PX.Objects.SV.FSEmployeeSkill)
PX.Objects.SV.FSSkill.SVWorkTaskLaborCollection -> Collection(PX.Objects.SV.SVWorkTaskLabor)
PX.Objects.SV.FSSkill.SVVendorSkillCollection -> Collection(PX.Objects.SV.SVVendorSkill)
PX.Objects.SV.FSSkill.FSServiceSkillCollection -> Collection(PX.Objects.FS.FSServiceSkill)

# PX.Objects.SV.PMActivityTotal (EntityType)

Label: "Activities Total"
Key: RefNoteId
Entity sets: PX_Objects_SV_PMActivityTotal, ActivitiesTotal, PMActivityTotal

PX.Objects.SV.PMActivityTotal.RefNoteId : Edm.Guid [key] "Document Nbr."
PX.Objects.SV.PMActivityTotal.TimeSpent : Edm.Int32 [required] "Time Spent"
PX.Objects.SV.PMActivityTotal.OvertimeSpent : Edm.Int32 [required] "Overtime Spent"
PX.Objects.SV.PMActivityTotal.TimeBillable : Edm.Int32 [required] "Billable Time"
PX.Objects.SV.PMActivityTotal.OvertimeBillable : Edm.Int32 [required] "Billable Overtime"

# PX.Objects.SV.Reports.APRegister (EntityType)

Key: DocType, RefNbr
Entity sets: PX_Objects_SV_Reports_APRegister
Non-filterable, non-selectable: DeletedDatabaseRecord

PX.Objects.SV.Reports.APRegister.DocType : Edm.String [key] "Type"
PX.Objects.SV.Reports.APRegister.RefNbr : Edm.String [key] "Reference Nbr."
PX.Objects.SV.Reports.APRegister.WorkOrderRefNbr : Edm.String
PX.Objects.SV.Reports.APRegister.FirstWorkOrderRefNbr : Edm.String
PX.Objects.SV.Reports.APRegister.DeletedDatabaseRecord : Edm.Boolean [required] "DeletedDatabaseRecord"
PX.Objects.SV.Reports.APRegister.PMProjectByProjectID -> PX.Objects.PM.PMProject
PX.Objects.SV.Reports.APRegister.VendorByEmployeeID -> PX.Objects.AP.Vendor
PX.Objects.SV.Reports.APRegister.VendorByVendorID -> PX.Objects.AP.Vendor
PX.Objects.SV.Reports.APRegister.BAccountByVendorID -> PX.Objects.CR.BAccount
PX.Objects.SV.Reports.APRegister.BatchByBatchNbr -> PX.Objects.GL.Batch
PX.Objects.SV.Reports.APRegister.BatchByPrebookBatchNbr -> PX.Objects.GL.Batch
PX.Objects.SV.Reports.APRegister.BatchByVoidBatchNbr -> PX.Objects.GL.Batch
PX.Objects.SV.Reports.APRegister.ContactByEmployeeID -> PX.Objects.CR.Contact
PX.Objects.SV.Reports.APRegister.APRegisterByRefNbr -> PX.Objects.AP.APRegister (RefNbr=OrigRefNbr)
PX.Objects.SV.Reports.APRegister.BranchByBranchID -> PX.Objects.GL.Branch
PX.Objects.SV.Reports.APRegister.CurrencyInfoByCuryInfoID -> PX.Objects.CM.CurrencyInfo
PX.Objects.SV.Reports.APRegister.UsersByCreatedByID -> PX.SM.Users
PX.Objects.SV.Reports.APRegister.UsersByLastModifiedByID -> PX.SM.Users
PX.Objects.SV.Reports.APRegister.EPCompanyTreeByEmployeeWorkgroupID -> PX.TM.EPCompanyTree
PX.Objects.SV.Reports.APRegister.INRegisterByTaxCostINAdjRefNbr -> PX.Objects.IN.INRegister
PX.Objects.SV.Reports.APRegister.CurrencyByCuryID -> PX.Objects.CM.Currency
PX.Objects.SV.Reports.APRegister.AccountByAPAccountID -> PX.Objects.GL.Account
PX.Objects.SV.Reports.APRegister.AccountByRetainageAcctID -> PX.Objects.GL.Account
PX.Objects.SV.Reports.APRegister.AccountByPrepaymentAccountID -> PX.Objects.GL.Account
PX.Objects.SV.Reports.APRegister.ScheduleByScheduleID -> PX.Objects.GL.Schedule
PX.Objects.SV.Reports.APRegister.SubByAPSubID -> PX.Objects.GL.Sub
PX.Objects.SV.Reports.APRegister.SubByRetainageSubID -> PX.Objects.GL.Sub
PX.Objects.SV.Reports.APRegister.SubByPrepaymentSubID -> PX.Objects.GL.Sub
PX.Objects.SV.Reports.APRegister.LocationByVendorLocationID -> PX.Objects.CR.Location
PX.Objects.SV.Reports.APRegister.LocationByVendorID -> PX.Objects.CR.Location
PX.Objects.SV.Reports.APRegister.APInvoiceCollection -> Collection(PX.Objects.AP.APInvoice)
PX.Objects.SV.Reports.APRegister.APAdjustCollection -> Collection(PX.Objects.AP.APAdjust)
PX.Objects.SV.Reports.APRegister.TaxTranCollection -> Collection(PX.Objects.TX.TaxTran)
PX.Objects.SV.Reports.APRegister.APTranCollection -> Collection(PX.Objects.AP.APTran)
PX.Objects.SV.Reports.APRegister.APPaymentChargeTranCollection -> Collection(PX.Objects.AP.APPaymentChargeTran)
PX.Objects.SV.Reports.APRegister.APTranPostCollection -> Collection(PX.Objects.AP.APTranPost)
PX.Objects.SV.Reports.APRegister.APTranPostGLCollection -> Collection(PX.Objects.AP.APTranPostGL)
PX.Objects.SV.Reports.APRegister.APPaymentCollection -> Collection(PX.Objects.AP.APPayment)
PX.Objects.SV.Reports.APRegister.POReceiptCollection -> Collection(PX.Objects.PO.POReceipt)
PX.Objects.SV.Reports.APRegister.FAServiceCollection -> Collection(PX.Objects.FA.FAService)
PX.Objects.SV.Reports.APRegister.ARTaxCollection -> Collection(PX.Objects.AR.ARTax)
PX.Objects.SV.Reports.APRegister.APRegisterCollection -> Collection(PX.Objects.AP.APRegister)
PX.Objects.SV.Reports.APRegister.APTaxCollection -> Collection(PX.Objects.AP.APTax)
PX.Objects.SV.Reports.APRegister.POOrderPrepaymentCollection -> Collection(PX.Objects.PO.POOrderPrepayment)
PX.Objects.SV.Reports.APRegister.APInvoiceDiscountDetailCollection -> Collection(PX.Objects.AP.APInvoiceDiscountDetail)
PX.Objects.SV.Reports.APRegister.PPExternalTranCollection -> Collection(PX.PaymentProcessor.ProcessorBase.DAC.PPExternalTran)
PX.Objects.SV.Reports.APRegister.PPBillcomBillCollection -> Collection(PX.PaymentProcessor.BillCom.DAC.PPBillcomBill)
PX.Objects.SV.Reports.APRegister.PPAvidChildPaymentCollection -> Collection(PX.PaymentProcessor.AvidXchange.DAC.PPAvidChildPayment)
PX.Objects.SV.Reports.APRegister.POBlanketOrderAPDocCollection -> Collection(PX.Objects.PO.DAC.Projections.POBlanketOrderAPDoc)
PX.Objects.SV.Reports.APRegister.APTranPostGLwithLinesCollection -> Collection(PX.Objects.AP.APTranPostGLwithLines)

# PX.Objects.SV.Reports.APRegisterServiceReport (EntityType)

BaseType: PX.Objects.SV.Reports.APRegister
Key: DocType, RefNbr (inherited from PX.Objects.SV.Reports.APRegister)
Entity sets: PX_Objects_SV_Reports_APRegisterServiceReport

# PX.Objects.SV.Reports.APTran (EntityType)

Key: RefNbr, TranType
Entity sets: PX_Objects_SV_Reports_APTran

PX.Objects.SV.Reports.APTran.RefNbr : Edm.String [key]
PX.Objects.SV.Reports.APTran.TranType : Edm.String [key]
PX.Objects.SV.Reports.APTran.WorkOrderNbr : Edm.String
PX.Objects.SV.Reports.APTran.PMProjectByProjectID -> PX.Objects.PM.PMProject
PX.Objects.SV.Reports.APTran.VendorByVendorID -> PX.Objects.AP.Vendor
PX.Objects.SV.Reports.APTran.APInvoiceByRefNbr -> PX.Objects.AP.APInvoice (TranType=DocType, RefNbr=RefNbr)
PX.Objects.SV.Reports.APTran.POLineByPOLineNbr -> PX.Objects.PO.POLine
PX.Objects.SV.Reports.APTran.POOrderByPONbr -> PX.Objects.PO.POOrder
PX.Objects.SV.Reports.APTran.POOrderByPOOrderType -> PX.Objects.PO.POOrder
PX.Objects.SV.Reports.APTran.PMTaskByProjectID -> PX.Objects.PM.PMTask
PX.Objects.SV.Reports.APTran.PMTaskByTaskID -> PX.Objects.PM.PMTask
PX.Objects.SV.Reports.APTran.BAccountByVendorID -> PX.Objects.CR.BAccount
PX.Objects.SV.Reports.APTran.APPaymentByRefNbr -> PX.Objects.AP.APPayment (TranType=DocType, RefNbr=RefNbr)
PX.Objects.SV.Reports.APTran.APRegisterByRefNbr -> PX.Objects.AP.APRegister (TranType=DocType, RefNbr=RefNbr)
PX.Objects.SV.Reports.APTran.InventoryItemByInventoryID -> PX.Objects.IN.InventoryItem
PX.Objects.SV.Reports.APTran.DRDeferredCodeByDeferredCode -> PX.Objects.DR.DRDeferredCode
PX.Objects.SV.Reports.APTran.BranchByBranchID -> PX.Objects.GL.Branch
PX.Objects.SV.Reports.APTran.CurrencyInfoByCuryInfoID -> PX.Objects.CM.CurrencyInfo
PX.Objects.SV.Reports.APTran.UsersByCreatedByID -> PX.SM.Users
PX.Objects.SV.Reports.APTran.UsersByLastModifiedByID -> PX.SM.Users
PX.Objects.SV.Reports.APTran.TaxByTaxID -> PX.Objects.TX.Tax
PX.Objects.SV.Reports.APTran.TaxCategoryByTaxCategoryID -> PX.Objects.TX.TaxCategory
PX.Objects.SV.Reports.APTran.LandedCostCodeByLandedCostCodeID -> PX.Objects.PO.LandedCostCode
PX.Objects.SV.Reports.APTran.POLandedCostDetailByLCLineNbr -> PX.Objects.PO.POLandedCostDetail
PX.Objects.SV.Reports.APTran.POLandedCostDetailByLCRefNbr -> PX.Objects.PO.POLandedCostDetail
PX.Objects.SV.Reports.APTran.POLandedCostDocByLCRefNbr -> PX.Objects.PO.POLandedCostDoc
PX.Objects.SV.Reports.APTran.POLandedCostDocByLCDocType -> PX.Objects.PO.POLandedCostDoc
PX.Objects.SV.Reports.APTran.POReceiptByReceiptNbr -> PX.Objects.PO.POReceipt
PX.Objects.SV.Reports.APTran.POReceiptByReceiptType -> PX.Objects.PO.POReceipt
PX.Objects.SV.Reports.APTran.POReceiptLineByReceiptLineNbr -> PX.Objects.PO.POReceiptLine
PX.Objects.SV.Reports.APTran.PMCostCodeByCostCodeID -> PX.Objects.PM.PMCostCode
PX.Objects.SV.Reports.APTran.DRScheduleByTranType -> PX.Objects.DR.DRSchedule (TranType=DocType)
PX.Objects.SV.Reports.APTran.INRegisterByPPVDocType -> PX.Objects.IN.INRegister
PX.Objects.SV.Reports.APTran.INSiteBySiteID -> PX.Objects.IN.INSite
PX.Objects.SV.Reports.APTran.INSubItemBySubItemID -> PX.Objects.IN.INSubItem
PX.Objects.SV.Reports.APTran.INUnitByInventoryID -> PX.Objects.IN.INUnit
PX.Objects.SV.Reports.APTran.AccountByAccountID -> PX.Objects.GL.Account
PX.Objects.SV.Reports.APTran.SubBySubID -> PX.Objects.GL.Sub
PX.Objects.SV.Reports.APTran.APDiscountByVendorID -> PX.Objects.AP.APDiscount
PX.Objects.SV.Reports.APTran.AP1099BoxByBox1099 -> PX.Objects.AP.AP1099Box
PX.Objects.SV.Reports.APTran.ARTaxCollection -> Collection(PX.Objects.AR.ARTax)
PX.Objects.SV.Reports.APTran.APAdjustCollection -> Collection(PX.Objects.AP.APAdjust)
PX.Objects.SV.Reports.APTran.APTaxCollection -> Collection(PX.Objects.AP.APTax)
PX.Objects.SV.Reports.APTran.DRScheduleCollection -> Collection(PX.Objects.DR.DRSchedule)
PX.Objects.SV.Reports.APTran.EPExpenseClaimDetailsCollection -> Collection(PX.Objects.EP.EPExpenseClaimDetails)
PX.Objects.SV.Reports.APTran.JointPayeeCollection -> Collection(PX.Objects.CN.JointChecks.JointPayee)
PX.Objects.SV.Reports.APTran.POAccrualDetailCollection -> Collection(PX.Objects.PO.POAccrualDetail)
PX.Objects.SV.Reports.APTran.POAccrualSplitCollection -> Collection(PX.Objects.PO.POAccrualSplit)
PX.Objects.SV.Reports.APTran.FSPostDetCollection -> Collection(PX.Objects.FS.FSPostDet)
PX.Objects.SV.Reports.APTran.FSPostInfoCollection -> Collection(PX.Objects.FS.FSPostInfo)

# PX.Objects.SV.Reports.APTran2 (EntityType)

BaseType: PX.Objects.SV.Reports.APTran
Key: RefNbr, TranType (inherited from PX.Objects.SV.Reports.APTran)
Entity sets: PX_Objects_SV_Reports_APTran2

# PX.Objects.SV.Reports.ARRegister (EntityType)

Key: DocType, RefNbr
Entity sets: PX_Objects_SV_Reports_ARRegister
Non-filterable, non-selectable: DeletedDatabaseRecord

PX.Objects.SV.Reports.ARRegister.DocType : Edm.String [key] "Type"
PX.Objects.SV.Reports.ARRegister.RefNbr : Edm.String [key] "Reference Nbr."
PX.Objects.SV.Reports.ARRegister.WorkOrderRefNbr : Edm.String
PX.Objects.SV.Reports.ARRegister.FirstWorkOrderRefNbr : Edm.String
PX.Objects.SV.Reports.ARRegister.DeletedDatabaseRecord : Edm.Boolean [required] "DeletedDatabaseRecord"
PX.Objects.SV.Reports.ARRegister.BAccountByCustomerID -> PX.Objects.CR.BAccount
PX.Objects.SV.Reports.ARRegister.CustomerByCustomerID -> PX.Objects.AR.Customer
PX.Objects.SV.Reports.ARRegister.BatchByBatchNbr -> PX.Objects.GL.Batch
PX.Objects.SV.Reports.ARRegister.ContactByApproverID -> PX.Objects.CR.Contact
PX.Objects.SV.Reports.ARRegister.ARRegisterByRefNbr -> PX.Objects.AR.ARRegister (RefNbr=OrigRefNbr)
PX.Objects.SV.Reports.ARRegister.BranchByBranchID -> PX.Objects.GL.Branch
PX.Objects.SV.Reports.ARRegister.CurrencyInfoByCuryInfoID -> PX.Objects.CM.CurrencyInfo
PX.Objects.SV.Reports.ARRegister.UsersByCreatedByID -> PX.SM.Users
PX.Objects.SV.Reports.ARRegister.UsersByLastModifiedByID -> PX.SM.Users
PX.Objects.SV.Reports.ARRegister.EPCompanyTreeByApproverWorkgroupID -> PX.TM.EPCompanyTree
PX.Objects.SV.Reports.ARRegister.CurrencyByCuryID -> PX.Objects.CM.Currency
PX.Objects.SV.Reports.ARRegister.AccountByARAccountID -> PX.Objects.GL.Account
PX.Objects.SV.Reports.ARRegister.AccountByRetainageAcctID -> PX.Objects.GL.Account
PX.Objects.SV.Reports.ARRegister.AccountByPrepaymentAccountID -> PX.Objects.GL.Account
PX.Objects.SV.Reports.ARRegister.ScheduleByScheduleID -> PX.Objects.GL.Schedule
PX.Objects.SV.Reports.ARRegister.SubByARSubID -> PX.Objects.GL.Sub
PX.Objects.SV.Reports.ARRegister.SubByRetainageSubID -> PX.Objects.GL.Sub
PX.Objects.SV.Reports.ARRegister.SubByPrepaymentSubID -> PX.Objects.GL.Sub
PX.Objects.SV.Reports.ARRegister.LocationByCustomerLocationID -> PX.Objects.CR.Location
PX.Objects.SV.Reports.ARRegister.LocationByCustomerID -> PX.Objects.CR.Location
PX.Objects.SV.Reports.ARRegister.SalesPersonBySalesPersonID -> PX.Objects.AR.SalesPerson
PX.Objects.SV.Reports.ARRegister.ARAdjustCollection -> Collection(PX.Objects.AR.ARAdjust)
PX.Objects.SV.Reports.ARRegister.TaxTranCollection -> Collection(PX.Objects.TX.TaxTran)
PX.Objects.SV.Reports.ARRegister.ARTaxCollection -> Collection(PX.Objects.AR.ARTax)
PX.Objects.SV.Reports.ARRegister.ARSalesPerTranCollection -> Collection(PX.Objects.AR.ARSalesPerTran)
PX.Objects.SV.Reports.ARRegister.ARTranCollection -> Collection(PX.Objects.AR.ARTran)
PX.Objects.SV.Reports.ARRegister.ARTranPostCollection -> Collection(PX.Objects.AR.ARTranPost)
PX.Objects.SV.Reports.ARRegister.ARPaymentChargeTranCollection -> Collection(PX.Objects.AR.ARPaymentChargeTran)
PX.Objects.SV.Reports.ARRegister.ARTranPostGLCollection -> Collection(PX.Objects.AR.ARTranPostGL)
PX.Objects.SV.Reports.ARRegister.ARPaymentCollection -> Collection(PX.Objects.AR.ARPayment)
PX.Objects.SV.Reports.ARRegister.ARInvoiceCollection -> Collection(PX.Objects.AR.ARInvoice)
PX.Objects.SV.Reports.ARRegister.ARRetainageWithApplicationsCollection -> Collection(PX.Objects.AR.ARRetainageWithApplications)
PX.Objects.SV.Reports.ARRegister.ARCashSaleCollection -> Collection(PX.Objects.AR.Standalone.ARCashSale)
PX.Objects.SV.Reports.ARRegister.ARRegisterCollection -> Collection(PX.Objects.AR.ARRegister)
PX.Objects.SV.Reports.ARRegister.INTranCollection -> Collection(PX.Objects.IN.INTran)
PX.Objects.SV.Reports.ARRegister.CCBatchTransactionCollection -> Collection(PX.Objects.CA.CCBatchTransaction)
PX.Objects.SV.Reports.ARRegister.SOOrderShipmentCollection -> Collection(PX.Objects.SO.SOOrderShipment)
PX.Objects.SV.Reports.ARRegister.ARInvoiceDiscountDetailCollection -> Collection(PX.Objects.AR.ARInvoiceDiscountDetail)
PX.Objects.SV.Reports.ARRegister.ARPaymentTotalsCollection -> Collection(PX.Objects.AR.ARPaymentTotals)
PX.Objects.SV.Reports.ARRegister.SOInvoiceCollection -> Collection(PX.Objects.SO.SOInvoice)
PX.Objects.SV.Reports.ARRegister.ExternalTransactionCollection -> Collection(PX.Objects.AR.ExternalTransaction)
PX.Objects.SV.Reports.ARRegister.ARTranAccrueCostCollection -> Collection(PX.Objects.AR.ARTranAccrueCost)

# PX.Objects.SV.Reports.ARRegisterServiceReport (EntityType)

BaseType: PX.Objects.SV.Reports.ARRegister
Key: DocType, RefNbr (inherited from PX.Objects.SV.Reports.ARRegister)
Entity sets: PX_Objects_SV_Reports_ARRegisterServiceReport

# PX.Objects.SV.Reports.ARTran (EntityType)

Key: RefNbr, TranType
Entity sets: PX_Objects_SV_Reports_ARTran

PX.Objects.SV.Reports.ARTran.RefNbr : Edm.String [key]
PX.Objects.SV.Reports.ARTran.TranType : Edm.String [key]
PX.Objects.SV.Reports.ARTran.WorkOrderNbr : Edm.String
PX.Objects.SV.Reports.ARTran.PMProjectByProjectID -> PX.Objects.PM.PMProject
PX.Objects.SV.Reports.ARTran.ARInvoiceByRefNbr -> PX.Objects.AR.ARInvoice (TranType=DocType, RefNbr=RefNbr)
PX.Objects.SV.Reports.ARTran.PMTaskByProjectID -> PX.Objects.PM.PMTask
PX.Objects.SV.Reports.ARTran.PMTaskByTaskID -> PX.Objects.PM.PMTask
PX.Objects.SV.Reports.ARTran.BAccountByCustomerID -> PX.Objects.CR.BAccount
PX.Objects.SV.Reports.ARTran.CustomerByCustomerID -> PX.Objects.AR.Customer
PX.Objects.SV.Reports.ARTran.ARPaymentByRefNbr -> PX.Objects.AR.ARPayment (TranType=DocType, RefNbr=RefNbr)
PX.Objects.SV.Reports.ARTran.InventoryItemByInventoryID -> PX.Objects.IN.InventoryItem
PX.Objects.SV.Reports.ARTran.DRDeferredCodeByDeferredCode -> PX.Objects.DR.DRDeferredCode
PX.Objects.SV.Reports.ARTran.SOOrderBySOOrderNbr -> PX.Objects.SO.SOOrder
PX.Objects.SV.Reports.ARTran.SOOrderBySOOrderType -> PX.Objects.SO.SOOrder
PX.Objects.SV.Reports.ARTran.SOOrderByBlanketType -> PX.Objects.SO.SOOrder
PX.Objects.SV.Reports.ARTran.ARRegisterByRefNbr -> PX.Objects.AR.ARRegister (TranType=DocType, RefNbr=RefNbr)
PX.Objects.SV.Reports.ARTran.BranchByBranchID -> PX.Objects.GL.Branch
PX.Objects.SV.Reports.ARTran.CurrencyInfoByCuryInfoID -> PX.Objects.CM.CurrencyInfo
PX.Objects.SV.Reports.ARTran.UsersByCreatedByID -> PX.SM.Users
PX.Objects.SV.Reports.ARTran.UsersByLastModifiedByID -> PX.SM.Users
PX.Objects.SV.Reports.ARTran.TaxByTaxID -> PX.Objects.TX.Tax
PX.Objects.SV.Reports.ARTran.TaxCategoryByTaxCategoryID -> PX.Objects.TX.TaxCategory
PX.Objects.SV.Reports.ARTran.SOBlanketOrderLinkBySOOrderNbr -> PX.Objects.SO.SOBlanketOrderLink
PX.Objects.SV.Reports.ARTran.SOLineBySOOrderLineNbr -> PX.Objects.SO.SOLine
PX.Objects.SV.Reports.ARTran.SOOrderShipmentBySOOrderNbr -> PX.Objects.SO.SOOrderShipment
PX.Objects.SV.Reports.ARTran.SOOrderShipmentBySOShipmentType -> PX.Objects.SO.SOOrderShipment
PX.Objects.SV.Reports.ARTran.SOOrderTypeBySOOrderType -> PX.Objects.SO.SOOrderType
PX.Objects.SV.Reports.ARTran.PMCostCodeByCostCodeID -> PX.Objects.PM.PMCostCode
PX.Objects.SV.Reports.ARTran.DRScheduleByTranType -> PX.Objects.DR.DRSchedule (TranType=DocType)
PX.Objects.SV.Reports.ARTran.ReasonCodeByReasonCode -> PX.Objects.CS.ReasonCode
PX.Objects.SV.Reports.ARTran.INLocationBySiteID -> PX.Objects.IN.INLocation
PX.Objects.SV.Reports.ARTran.INRegisterByInvtDocType -> PX.Objects.IN.INRegister
PX.Objects.SV.Reports.ARTran.INSiteBySiteID -> PX.Objects.IN.INSite
PX.Objects.SV.Reports.ARTran.INSubItemBySubItemID -> PX.Objects.IN.INSubItem
PX.Objects.SV.Reports.ARTran.INUnitByInventoryID -> PX.Objects.IN.INUnit
PX.Objects.SV.Reports.ARTran.AccountByAccountID -> PX.Objects.GL.Account
PX.Objects.SV.Reports.ARTran.AccountByExpenseAccrualAccountID -> PX.Objects.GL.Account
PX.Objects.SV.Reports.ARTran.AccountByExpenseAccountID -> PX.Objects.GL.Account
PX.Objects.SV.Reports.ARTran.SubBySubID -> PX.Objects.GL.Sub
PX.Objects.SV.Reports.ARTran.SubByExpenseAccrualSubID -> PX.Objects.GL.Sub
PX.Objects.SV.Reports.ARTran.SubByExpenseSubID -> PX.Objects.GL.Sub
PX.Objects.SV.Reports.ARTran.CRCaseByCaseCD -> PX.Objects.CR.CRCase
PX.Objects.SV.Reports.ARTran.ARDiscountByDiscountID -> PX.Objects.AR.ARDiscount
PX.Objects.SV.Reports.ARTran.ARSalesPerTranBySalesPersonID -> PX.Objects.AR.ARSalesPerTran (TranType=DocType, RefNbr=RefNbr)
PX.Objects.SV.Reports.ARTran.SalesPersonBySalesPersonID -> PX.Objects.AR.SalesPerson
PX.Objects.SV.Reports.ARTran.SOInvoiceByRefNbr -> PX.Objects.SO.SOInvoice (TranType=DocType, RefNbr=RefNbr)
PX.Objects.SV.Reports.ARTran.SOInvoiceByOrigInvoiceType -> PX.Objects.SO.SOInvoice
PX.Objects.SV.Reports.ARTran.INLotSerialStatusByCostCenterByLocationID -> PX.Objects.IN.INLotSerialStatusByCostCenter
PX.Objects.SV.Reports.ARTran.ARTaxCollection -> Collection(PX.Objects.AR.ARTax)
PX.Objects.SV.Reports.ARTran.INTranCollection -> Collection(PX.Objects.IN.INTran)
PX.Objects.SV.Reports.ARTran.ARAdjustCollection -> Collection(PX.Objects.AR.ARAdjust)
PX.Objects.SV.Reports.ARTran.DRScheduleCollection -> Collection(PX.Objects.DR.DRSchedule)
PX.Objects.SV.Reports.ARTran.SOLineCollection -> Collection(PX.Objects.SO.SOLine)
PX.Objects.SV.Reports.ARTran.RelatedItemHistoryCollection -> Collection(PX.Objects.IN.RelatedItems.RelatedItemHistory)
PX.Objects.SV.Reports.ARTran.FSPostDetCollection -> Collection(PX.Objects.FS.FSPostDet)
PX.Objects.SV.Reports.ARTran.FSPostInfoCollection -> Collection(PX.Objects.FS.FSPostInfo)
PX.Objects.SV.Reports.ARTran.ARFinChargeTranCollection -> Collection(PX.Objects.AR.ARFinChargeTran)

# PX.Objects.SV.Reports.ARTran2 (EntityType)

BaseType: PX.Objects.SV.Reports.ARTran
Key: RefNbr, TranType (inherited from PX.Objects.SV.Reports.ARTran)
Entity sets: PX_Objects_SV_Reports_ARTran2

# PX.Objects.SV.Reports.SVPrepaymentAdjust (EntityType)

BaseType: PX.Objects.SV.Reports.ARRegister
Key: DocType, RefNbr (inherited from PX.Objects.SV.Reports.ARRegister)
Entity sets: PX_Objects_SV_Reports_SVPrepaymentAdjust

# PX.Objects.SV.SVAccessibleCustomer (EntityType)

Label: "Customer"
Key: BAccountID
Entity sets: PX_Objects_SV_SVAccessibleCustomer, Customer4, SVAccessibleCustomer

PX.Objects.SV.SVAccessibleCustomer.BAccountID : Edm.Int32 [key]
PX.Objects.SV.SVAccessibleCustomer.AcctName : Edm.String "Customer Name"
PX.Objects.SV.SVAccessibleCustomer.ContactByDefBillContactID -> PX.Objects.CR.Contact
PX.Objects.SV.SVAccessibleCustomer.ContactByOwnerID -> PX.Objects.CR.Contact
PX.Objects.SV.SVAccessibleCustomer.LocationByDefLocationID -> PX.Objects.CR.Location (BAccountID=BAccountID)
PX.Objects.SV.SVAccessibleCustomer.LocationByBAccountID -> PX.Objects.CR.Location (BAccountID=BAccountID)
PX.Objects.SV.SVAccessibleCustomer.ARPaymentCollection -> Collection(PX.Objects.AR.ARPayment)
PX.Objects.SV.SVAccessibleCustomer.ARInvoiceCollection -> Collection(PX.Objects.AR.ARInvoice)
PX.Objects.SV.SVAccessibleCustomer.CustomerCollection -> Collection(PX.Objects.AR.Customer)
PX.Objects.SV.SVAccessibleCustomer.ARRegisterCollection -> Collection(PX.Objects.AR.ARRegister)
PX.Objects.SV.SVAccessibleCustomer.SOAddressCollection -> Collection(PX.Objects.SO.SOAddress)
PX.Objects.SV.SVAccessibleCustomer.SOContactCollection -> Collection(PX.Objects.SO.SOContact)
PX.Objects.SV.SVAccessibleCustomer.SOOrderCollection -> Collection(PX.Objects.SO.SOOrder)
PX.Objects.SV.SVAccessibleCustomer.ContractCollection -> Collection(PX.Objects.CT.Contract)
PX.Objects.SV.SVAccessibleCustomer.ARAdjustCollection -> Collection(PX.Objects.AR.ARAdjust)
PX.Objects.SV.SVAccessibleCustomer.ARAddressCollection -> Collection(PX.Objects.AR.ARAddress)
PX.Objects.SV.SVAccessibleCustomer.EPExpenseClaimCollection -> Collection(PX.Objects.EP.EPExpenseClaim)
PX.Objects.SV.SVAccessibleCustomer.EPExpenseClaimDetailsCollection -> Collection(PX.Objects.EP.EPExpenseClaimDetails)
PX.Objects.SV.SVAccessibleCustomer.SOLineCollection -> Collection(PX.Objects.SO.SOLine)
PX.Objects.SV.SVAccessibleCustomer.FSScheduleCollection -> Collection(PX.Objects.FS.FSSchedule)
PX.Objects.SV.SVAccessibleCustomer.FSServiceOrderCollection -> Collection(PX.Objects.FS.FSServiceOrder)
PX.Objects.SV.SVAccessibleCustomer.FSSODetCollection -> Collection(PX.Objects.FS.FSSODet)
PX.Objects.SV.SVAccessibleCustomer.FSAppointmentCollection -> Collection(PX.Objects.FS.FSAppointment)
PX.Objects.SV.SVAccessibleCustomer.POEnabledFSSODetCollection -> Collection(PX.Objects.FS.POEnabledFSSODet)
PX.Objects.SV.SVAccessibleCustomer.FSEquipmentCollection -> Collection(PX.Objects.FS.FSEquipment)
PX.Objects.SV.SVAccessibleCustomer.PMChangeOrderCollection -> Collection(PX.Objects.PM.PMChangeOrder)
PX.Objects.SV.SVAccessibleCustomer.ARSalesPriceCollection -> Collection(PX.Objects.AR.ARSalesPrice)
PX.Objects.SV.SVAccessibleCustomer.ARTranCollection -> Collection(PX.Objects.AR.ARTran)
PX.Objects.SV.SVAccessibleCustomer.SOAdjustCollection -> Collection(PX.Objects.SO.SOAdjust)
PX.Objects.SV.SVAccessibleCustomer.CustSalesPeopleCollection -> Collection(PX.Objects.AR.CustSalesPeople)
PX.Objects.SV.SVAccessibleCustomer.PostingBatchDetailCollection -> Collection(PX.Objects.FS.PostingBatchDetail)
PX.Objects.SV.SVAccessibleCustomer.CuryARHistoryCollection -> Collection(PX.Objects.AR.CuryARHistory)
PX.Objects.SV.SVAccessibleCustomer.ARHistoryCollection -> Collection(PX.Objects.AR.ARHistory)
PX.Objects.SV.SVAccessibleCustomer.ARTranPostCollection -> Collection(PX.Objects.AR.ARTranPost)
PX.Objects.SV.SVAccessibleCustomer.APHistoryCollection -> Collection(PX.Objects.AP.APHistory)
PX.Objects.SV.SVAccessibleCustomer.ARDunningLetterDetailCollection -> Collection(PX.Objects.AR.ARDunningLetterDetail)
PX.Objects.SV.SVAccessibleCustomer.SOOrderShipmentCollection -> Collection(PX.Objects.SO.SOOrderShipment)
PX.Objects.SV.SVAccessibleCustomer.SOShipLineCollection -> Collection(PX.Objects.SO.SOShipLine)
PX.Objects.SV.SVAccessibleCustomer.SOShipmentCollection -> Collection(PX.Objects.SO.SOShipment)
PX.Objects.SV.SVAccessibleCustomer.MNMaterialListCollection -> Collection(PX.Objects.MN.MNMaterialList)
PX.Objects.SV.SVAccessibleCustomer.ContractBillingScheduleCollection -> Collection(PX.Objects.CT.ContractBillingSchedule)
PX.Objects.SV.SVAccessibleCustomer.ARPriceWorksheetDetailCollection -> Collection(PX.Objects.AR.ARPriceWorksheetDetail)
PX.Objects.SV.SVAccessibleCustomer.ARStatementCollection -> Collection(PX.Objects.AR.ARStatement)
PX.Objects.SV.SVAccessibleCustomer.CustomerPaymentMethodCollection -> Collection(PX.Objects.AR.CustomerPaymentMethod)
PX.Objects.SV.SVAccessibleCustomer.DiscountCustomerCollection -> Collection(PX.Objects.AR.DiscountCustomer)
PX.Objects.SV.SVAccessibleCustomer.BCBindingExtCollection -> Collection(PX.Commerce.Objects.BCBindingExt)
PX.Objects.SV.SVAccessibleCustomer.AMConfigurationResultsCollection -> Collection(PX.Objects.AM.AMConfigurationResults)
PX.Objects.SV.SVAccessibleCustomer.AMForecastCollection -> Collection(PX.Objects.AM.AMForecast)
PX.Objects.SV.SVAccessibleCustomer.AMForecastStagingCollection -> Collection(PX.Objects.AM.AMForecastStaging)
PX.Objects.SV.SVAccessibleCustomer.FSCustomerBillingSetupCollection -> Collection(PX.Objects.FS.FSCustomerBillingSetup)
PX.Objects.SV.SVAccessibleCustomer.FSMasterContractCollection -> Collection(PX.Objects.FS.FSMasterContract)
PX.Objects.SV.SVAccessibleCustomer.FSServiceContractCollection -> Collection(PX.Objects.FS.FSServiceContract)
PX.Objects.SV.SVAccessibleCustomer.FSWrkProcessCollection -> Collection(PX.Objects.FS.FSWrkProcess)
PX.Objects.SV.SVAccessibleCustomer.SVAdjustCollection -> Collection(PX.Objects.SV.SVAdjust)
PX.Objects.SV.SVAccessibleCustomer.SVOrderCollection -> Collection(PX.Objects.SV.SVOrder)
PX.Objects.SV.SVAccessibleCustomer.SVOrderActualCollection -> Collection(PX.Objects.SV.SVOrderActual)
PX.Objects.SV.SVAccessibleCustomer.SVOrderDetailCollection -> Collection(PX.Objects.SV.SVOrderDetail)
PX.Objects.SV.SVAccessibleCustomer.BAccountLocationCollection -> Collection(PX.Objects.FS.BAccountLocation)
PX.Objects.SV.SVAccessibleCustomer.SOInvoiceCollection -> Collection(PX.Objects.SO.SOInvoice)
PX.Objects.SV.SVAccessibleCustomer.ARDunningLetterCollection -> Collection(PX.Objects.AR.ARDunningLetter)
PX.Objects.SV.SVAccessibleCustomer.ARTranPostGLCollection -> Collection(PX.Objects.AR.ARTranPostGL)
PX.Objects.SV.SVAccessibleCustomer.DRRevenueBalanceByPeriodCollection -> Collection(PX.Objects.DR.DRRevenueBalanceByPeriod)
PX.Objects.SV.SVAccessibleCustomer.DRRevenueProjectionCollection -> Collection(PX.Objects.DR.DRRevenueProjection)
PX.Objects.SV.SVAccessibleCustomer.ARSPCommnHistoryCollection -> Collection(PX.Objects.AR.ARSPCommnHistory)
PX.Objects.SV.SVAccessibleCustomer.ARStatementDetailCollection -> Collection(PX.Objects.AR.ARStatementDetail)
PX.Objects.SV.SVAccessibleCustomer.ARStatementDetailInfoCollection -> Collection(PX.Objects.AR.ARStatementDetailInfo)
PX.Objects.SV.SVAccessibleCustomer.ContractPostBatchDetailCollection -> Collection(PX.Objects.FS.ContractPostBatchDetail)
PX.Objects.SV.SVAccessibleCustomer.ContractPeriodToPostCollection -> Collection(PX.Objects.FS.ContractPeriodToPost)
PX.Objects.SV.SVAccessibleCustomer.CCSynchronizeCardCollection -> Collection(PX.Objects.CA.CCSynchronizeCard)
PX.Objects.SV.SVAccessibleCustomer.CustomerProcessingCenterIDCollection -> Collection(PX.Objects.CA.CustomerProcessingCenterID)
PX.Objects.SV.SVAccessibleCustomer.CustomerPaymentMethodInfoCollection -> Collection(PX.Objects.AR.CustomerPaymentMethodInfo)
PX.Objects.SV.SVAccessibleCustomer.FSRouteAppointmentForecastingCollection -> Collection(PX.Objects.FS.FSRouteAppointmentForecasting)
PX.Objects.SV.SVAccessibleCustomer.ARBalancesCollection -> Collection(PX.Objects.AR.ARBalances)
PX.Objects.SV.SVAccessibleCustomer.DRRevenueBalanceCollection -> Collection(PX.Objects.DR.DRRevenueBalance)
PX.Objects.SV.SVAccessibleCustomer.DRRevenueBalance2Collection -> Collection(PX.Objects.DR.DRRevenueBalance2)

# PX.Objects.SV.SVAddress (EntityType)

Label: "Address"
Key: AddressID
Entity sets: PX_Objects_SV_SVAddress, Address1, SVAddress
Non-filterable, non-selectable: OverrideAddress

PX.Objects.SV.SVAddress.AddressID : Edm.Int32 [key] "Address ID"
PX.Objects.SV.SVAddress.CustomerID : Edm.Int32
PX.Objects.SV.SVAddress.CustomerAddressID : Edm.Int32
PX.Objects.SV.SVAddress.IsDefaultAddress : Edm.Boolean [required] "Customer Default"
PX.Objects.SV.SVAddress.OverrideAddress : Edm.Boolean "Override Address"
PX.Objects.SV.SVAddress.RevisionID : Edm.Int32 [required]
PX.Objects.SV.SVAddress.AddressLine1 : Edm.String "Address Line 1"
PX.Objects.SV.SVAddress.AddressLine2 : Edm.String "Address Line 2"
PX.Objects.SV.SVAddress.AddressLine3 : Edm.String "Address Line 3"
PX.Objects.SV.SVAddress.City : Edm.String "City"
PX.Objects.SV.SVAddress.CountryID : Edm.String "Country"
PX.Objects.SV.SVAddress.State : Edm.String "State"
PX.Objects.SV.SVAddress.PostalCode : Edm.String "Postal Code"
PX.Objects.SV.SVAddress.Latitude : Edm.Decimal "Latitude"
PX.Objects.SV.SVAddress.Longitude : Edm.Decimal "Longitude"
PX.Objects.SV.SVAddress.DisplayName : Edm.String "Address"
PX.Objects.SV.SVAddress.NoteID : Edm.Guid
PX.Objects.SV.SVAddress.tstamp : Edm.Binary
PX.Objects.SV.SVAddress.CreatedByID : Edm.Guid "Created By"
PX.Objects.SV.SVAddress.CreatedByScreenID : Edm.String
PX.Objects.SV.SVAddress.CreatedDateTime : Edm.DateTimeOffset
PX.Objects.SV.SVAddress.LastModifiedByID : Edm.Guid "Last Modified By"
PX.Objects.SV.SVAddress.LastModifiedByScreenID : Edm.String
PX.Objects.SV.SVAddress.LastModifiedDateTime : Edm.DateTimeOffset
PX.Objects.SV.SVAddress.UsersByCreatedByID -> PX.SM.Users (CreatedByID=PKID)
PX.Objects.SV.SVAddress.UsersByLastModifiedByID -> PX.SM.Users (LastModifiedByID=PKID)
PX.Objects.SV.SVAddress.CountryByCountryID -> PX.Objects.CS.Country (CountryID=CountryID)
PX.Objects.SV.SVAddress.StateByCountryID -> PX.Objects.CS.State (State=StateID, CountryID=CountryID)
PX.Objects.SV.SVAddress.SVEventCollection -> Collection(PX.Objects.SV.SVEvent)
PX.Objects.SV.SVAddress.SVServiceLocationCollection -> Collection(PX.Objects.SV.SVServiceLocation)

# PX.Objects.SV.SVAdjust (EntityType)

Label: "Work Order Adjust"
Key: AdjdOrderNbr, AdjgDocType, AdjgRefNbr
Entity sets: PX_Objects_SV_SVAdjust, WorkOrderAdjust, SVAdjust
Non-filterable, non-selectable: CuryAdjgDiscAmt, CuryAdjdDiscAmt, AdjDiscAmt, CuryDocBal, DocBal, CuryInitialDocBal, CuryInitialDiscBal, CuryInitialWBal, NoteText

PX.Objects.SV.SVAdjust.Hold : Edm.Boolean [required]
PX.Objects.SV.SVAdjust.CustomerID : Edm.Int32
PX.Objects.SV.SVAdjust.AdjgDocType : Edm.String [key] "Doc. Type"
PX.Objects.SV.SVAdjust.AdjgRefNbr : Edm.String [key] "Reference Nbr."
PX.Objects.SV.SVAdjust.AdjdOrderNbr : Edm.String [key] "Work Order"
PX.Objects.SV.SVAdjust.CuryAdjgAmt : Edm.Decimal [required] "Applied to Work Order"
PX.Objects.SV.SVAdjust.AdjAmt : Edm.Decimal [required]
PX.Objects.SV.SVAdjust.CuryAdjdAmt : Edm.Decimal [required] "Applied to Work Order"
PX.Objects.SV.SVAdjust.CuryOrigAdjdAmt : Edm.Decimal
PX.Objects.SV.SVAdjust.OrigAdjAmt : Edm.Decimal
PX.Objects.SV.SVAdjust.CuryOrigAdjgAmt : Edm.Decimal
PX.Objects.SV.SVAdjust.CuryAdjgDiscAmt : Edm.Decimal
PX.Objects.SV.SVAdjust.CuryAdjdDiscAmt : Edm.Decimal
PX.Objects.SV.SVAdjust.AdjDiscAmt : Edm.Decimal
PX.Objects.SV.SVAdjust.AdjdOrigCuryInfoID : Edm.Int64
PX.Objects.SV.SVAdjust.AdjgCuryInfoID : Edm.Int64
PX.Objects.SV.SVAdjust.AdjdCuryInfoID : Edm.Int64
PX.Objects.SV.SVAdjust.AdjgDocDate : Edm.DateTimeOffset "Application Date"
PX.Objects.SV.SVAdjust.AdjdOrderDate : Edm.DateTimeOffset "Date"
PX.Objects.SV.SVAdjust.CuryAdjgBilledAmt : Edm.Decimal [required] "Applied to Invoice"
PX.Objects.SV.SVAdjust.AdjBilledAmt : Edm.Decimal [required]
PX.Objects.SV.SVAdjust.CuryAdjdBilledAmt : Edm.Decimal [required] "Applied to Invoice"
PX.Objects.SV.SVAdjust.CuryDocBal : Edm.Decimal "Remaining Balance"
PX.Objects.SV.SVAdjust.DocBal : Edm.Decimal
PX.Objects.SV.SVAdjust.CuryInitialDocBal : Edm.Decimal
PX.Objects.SV.SVAdjust.CuryInitialDiscBal : Edm.Decimal
PX.Objects.SV.SVAdjust.CuryInitialWBal : Edm.Decimal
PX.Objects.SV.SVAdjust.Voided : Edm.Boolean [required]
PX.Objects.SV.SVAdjust.NoteID : Edm.Guid
PX.Objects.SV.SVAdjust.NoteText : Edm.String "Note Text"
PX.Objects.SV.SVAdjust.tstamp : Edm.Binary
PX.Objects.SV.SVAdjust.CreatedByID : Edm.Guid "Created By"
PX.Objects.SV.SVAdjust.CreatedByScreenID : Edm.String
PX.Objects.SV.SVAdjust.CreatedDateTime : Edm.DateTimeOffset
PX.Objects.SV.SVAdjust.LastModifiedByID : Edm.Guid "Last Modified By"
PX.Objects.SV.SVAdjust.LastModifiedByScreenID : Edm.String
PX.Objects.SV.SVAdjust.LastModifiedDateTime : Edm.DateTimeOffset
PX.Objects.SV.SVAdjust.ARInvoiceByAdjgRefNbr -> PX.Objects.AR.ARInvoice (AdjgDocType=DocType, AdjgRefNbr=RefNbr)
PX.Objects.SV.SVAdjust.CustomerByCustomerID -> PX.Objects.AR.Customer (CustomerID=BAccountID)
PX.Objects.SV.SVAdjust.ARPaymentByAdjgRefNbr -> PX.Objects.AR.ARPayment (AdjgDocType=DocType, AdjgRefNbr=RefNbr)
PX.Objects.SV.SVAdjust.CurrencyInfoByAdjgCuryInfoID -> PX.Objects.CM.CurrencyInfo (AdjgCuryInfoID=CuryInfoID)
PX.Objects.SV.SVAdjust.CurrencyInfoByAdjdCuryInfoID -> PX.Objects.CM.CurrencyInfo (AdjdCuryInfoID=CuryInfoID)
PX.Objects.SV.SVAdjust.CurrencyInfoByAdjdOrigCuryInfoID -> PX.Objects.CM.CurrencyInfo (AdjdOrigCuryInfoID=CuryInfoID)
PX.Objects.SV.SVAdjust.UsersByCreatedByID -> PX.SM.Users (CreatedByID=PKID)
PX.Objects.SV.SVAdjust.UsersByLastModifiedByID -> PX.SM.Users (LastModifiedByID=PKID)
PX.Objects.SV.SVAdjust.ARPaymentTotalsByAdjgRefNbr -> PX.Objects.AR.ARPaymentTotals (AdjgDocType=DocType, AdjgRefNbr=RefNbr)
PX.Objects.SV.SVAdjust.SVOrderByAdjdOrderNbr -> PX.Objects.SV.SVOrder (AdjdOrderNbr=OrderNbr)

# PX.Objects.SV.SVContact (EntityType)

Label: "Contact"
Key: ContactID
Entity sets: PX_Objects_SV_SVContact, Contact3, SVContact
Non-filterable, non-selectable: OverrideContact

PX.Objects.SV.SVContact.ContactID : Edm.Int32 [key] "Contact ID"
PX.Objects.SV.SVContact.CustomerID : Edm.Int32
PX.Objects.SV.SVContact.CustomerContactID : Edm.Int32
PX.Objects.SV.SVContact.IsDefaultContact : Edm.Boolean [required] "Default Customer Contact"
PX.Objects.SV.SVContact.OverrideContact : Edm.Boolean "Override Contact"
PX.Objects.SV.SVContact.RevisionID : Edm.Int32
PX.Objects.SV.SVContact.Title : Edm.String "Title"
PX.Objects.SV.SVContact.Salutation : Edm.String "Job Title"
PX.Objects.SV.SVContact.Attention : Edm.String "Attention"
PX.Objects.SV.SVContact.FullName : Edm.String "Account Name"
PX.Objects.SV.SVContact.Email : Edm.String "Email"
PX.Objects.SV.SVContact.Fax : Edm.String "Fax"
PX.Objects.SV.SVContact.FaxType : Edm.String "Fax"
PX.Objects.SV.SVContact.Phone1 : Edm.String "Phone 1"
PX.Objects.SV.SVContact.Phone1Type : Edm.String "Phone 1"
PX.Objects.SV.SVContact.Phone2 : Edm.String "Phone 2"
PX.Objects.SV.SVContact.Phone2Type : Edm.String "Phone 2"
PX.Objects.SV.SVContact.Phone3 : Edm.String "Phone 3"
PX.Objects.SV.SVContact.Phone3Type : Edm.String "Phone 3"
PX.Objects.SV.SVContact.NoteID : Edm.Guid
PX.Objects.SV.SVContact.tstamp : Edm.Binary
PX.Objects.SV.SVContact.CreatedByID : Edm.Guid "Created By"
PX.Objects.SV.SVContact.CreatedByScreenID : Edm.String
PX.Objects.SV.SVContact.CreatedDateTime : Edm.DateTimeOffset
PX.Objects.SV.SVContact.LastModifiedByID : Edm.Guid "Last Modified By"
PX.Objects.SV.SVContact.LastModifiedByScreenID : Edm.String
PX.Objects.SV.SVContact.LastModifiedDateTime : Edm.DateTimeOffset
PX.Objects.SV.SVContact.UsersByCreatedByID -> PX.SM.Users (CreatedByID=PKID)
PX.Objects.SV.SVContact.UsersByLastModifiedByID -> PX.SM.Users (LastModifiedByID=PKID)

# PX.Objects.SV.SVEmployeeLicense (EntityType)

Label: "Staff License"
BaseType: PX.Objects.SV.FSLicense
Key: RefNbr (inherited from PX.Objects.SV.FSLicense)
Entity sets: PX_Objects_SV_SVEmployeeLicense, StaffLicense1, SVEmployeeLicense

# PX.Objects.SV.SVEmployeeServiceArea (EntityType)

Label: "Staff Service Area"
Key: EmployeeID, GeoZoneID
Entity sets: PX_Objects_SV_SVEmployeeServiceArea, StaffServiceArea, SVEmployeeServiceArea
Non-filterable, non-selectable: NoteText

PX.Objects.SV.SVEmployeeServiceArea.NoteID : Edm.Guid
PX.Objects.SV.SVEmployeeServiceArea.NoteText : Edm.String "Note Text"
PX.Objects.SV.SVEmployeeServiceArea.EmployeeID : Edm.Int32 [key] "Employee ID"
PX.Objects.SV.SVEmployeeServiceArea.GeoZoneID : Edm.Int32 [key] "Service Area ID"
PX.Objects.SV.SVEmployeeServiceArea.CreatedByID : Edm.Guid "Created By"
PX.Objects.SV.SVEmployeeServiceArea.CreatedByScreenID : Edm.String "Created By Screen ID"
PX.Objects.SV.SVEmployeeServiceArea.CreatedDateTime : Edm.DateTimeOffset "Created On"
PX.Objects.SV.SVEmployeeServiceArea.LastModifiedByID : Edm.Guid "Last Modified By"
PX.Objects.SV.SVEmployeeServiceArea.LastModifiedByScreenID : Edm.String "Last Modified By Screen ID"
PX.Objects.SV.SVEmployeeServiceArea.LastModifiedDateTime : Edm.DateTimeOffset "Last Modified On"
PX.Objects.SV.SVEmployeeServiceArea.tstamp : Edm.Binary

# PX.Objects.SV.SVEmployeeSkill (EntityType)

Label: "Staff Skill"
BaseType: PX.Objects.SV.FSEmployeeSkill
Key: EmployeeID, SkillID (inherited from PX.Objects.SV.FSEmployeeSkill)
Entity sets: PX_Objects_SV_SVEmployeeSkill, StaffSkill1, SVEmployeeSkill

# PX.Objects.SV.SVEvent (EntityType)

Label: "Work Event"
Key: NoteID
Entity sets: PX_Objects_SV_SVEvent, WorkEvent, SVEvent
Non-filterable, non-selectable: Location, NoteText

PX.Objects.SV.SVEvent.Summary : Edm.String "Summary"
PX.Objects.SV.SVEvent.Status : Edm.String "Status"
PX.Objects.SV.SVEvent.Confirmed : Edm.Boolean [required] "Confirmed"
PX.Objects.SV.SVEvent.Description : Edm.String "Description"
PX.Objects.SV.SVEvent.Duration : Edm.Int32 "Duration"
PX.Objects.SV.SVEvent.StartDate : Edm.DateTimeOffset "Start Time"
PX.Objects.SV.SVEvent.EndDate : Edm.DateTimeOffset "End Time"
PX.Objects.SV.SVEvent.AddressID : Edm.Int32
PX.Objects.SV.SVEvent.Location : Edm.String "Location"
PX.Objects.SV.SVEvent.LocationContactID : Edm.Int32 "Contact at Location"
PX.Objects.SV.SVEvent.LocationContactPhone : Edm.String "Phone"
PX.Objects.SV.SVEvent.RefNoteIDType : Edm.String "Related Entity Type"
PX.Objects.SV.SVEvent.RefNoteID : Edm.Guid "Related Document Nbr."
PX.Objects.SV.SVEvent.TicketNbr : Edm.String "Work Ticket Nbr."
PX.Objects.SV.SVEvent.LineCntr : Edm.Int32 [required]
PX.Objects.SV.SVEvent.LaborLineCntr : Edm.Int32 [required]
PX.Objects.SV.SVEvent.SetDurationManually : Edm.Boolean [required] "Set Duration Manually"
PX.Objects.SV.SVEvent.NoteID : Edm.Guid [key] "ID"
PX.Objects.SV.SVEvent.NoteText : Edm.String "Note Text"
PX.Objects.SV.SVEvent.tstamp : Edm.Binary
PX.Objects.SV.SVEvent.CreatedByID : Edm.Guid "Created By"
PX.Objects.SV.SVEvent.CreatedByScreenID : Edm.String
PX.Objects.SV.SVEvent.CreatedDateTime : Edm.DateTimeOffset
PX.Objects.SV.SVEvent.LastModifiedByID : Edm.Guid "Last Modified By"
PX.Objects.SV.SVEvent.LastModifiedByScreenID : Edm.String
PX.Objects.SV.SVEvent.LastModifiedDateTime : Edm.DateTimeOffset "Last Modified"
PX.Objects.SV.SVEvent.ContactByLocationContactID -> PX.Objects.CR.Contact (LocationContactID=ContactID)
PX.Objects.SV.SVEvent.UsersByCreatedByID -> PX.SM.Users (CreatedByID=PKID)
PX.Objects.SV.SVEvent.UsersByLastModifiedByID -> PX.SM.Users (LastModifiedByID=PKID)
PX.Objects.SV.SVEvent.SVAddressByAddressID -> PX.Objects.SV.SVAddress (AddressID=AddressID)
PX.Objects.SV.SVEvent.SVTicketCollection -> Collection(PX.Objects.SV.SVTicket)
PX.Objects.SV.SVEvent.SVEventLaborCollection -> Collection(PX.Objects.SV.SVEventLabor)
PX.Objects.SV.SVEvent.SVEventTaskCollection -> Collection(PX.Objects.SV.SVEventTask)

# PX.Objects.SV.SVEventLabor (EntityType)

Label: "Work Task Workforce"
Key: EventNoteID, LineNbr
Entity sets: PX_Objects_SV_SVEventLabor, WorkTaskWorkforce, SVEventLabor
Non-filterable, non-selectable: DatafeedRemoveEnabled, NoteText

PX.Objects.SV.SVEventLabor.EventNoteID : Edm.Guid [key] "Work Event"
PX.Objects.SV.SVEventLabor.LineNbr : Edm.Int32 [key] "Line Nbr."
PX.Objects.SV.SVEventLabor.ResourceNoteID : Edm.Guid "Resources"
PX.Objects.SV.SVEventLabor.Name : Edm.String "Name"
PX.Objects.SV.SVEventLabor.Position : Edm.String "Position"
PX.Objects.SV.SVEventLabor.PositionDescription : Edm.String "Position"
PX.Objects.SV.SVEventLabor.Subcontractor : Edm.String "Subcontractor"
PX.Objects.SV.SVEventLabor.DatafeedRemoveEnabled : Edm.Boolean
PX.Objects.SV.SVEventLabor.NoteID : Edm.Guid
PX.Objects.SV.SVEventLabor.NoteText : Edm.String "Note Text"
PX.Objects.SV.SVEventLabor.tstamp : Edm.Binary
PX.Objects.SV.SVEventLabor.CreatedByID : Edm.Guid "Created By"
PX.Objects.SV.SVEventLabor.CreatedByScreenID : Edm.String
PX.Objects.SV.SVEventLabor.CreatedDateTime : Edm.DateTimeOffset
PX.Objects.SV.SVEventLabor.LastModifiedByID : Edm.Guid "Last Modified By"
PX.Objects.SV.SVEventLabor.LastModifiedByScreenID : Edm.String
PX.Objects.SV.SVEventLabor.LastModifiedDateTime : Edm.DateTimeOffset "Last Modified"
PX.Objects.SV.SVEventLabor.UsersByCreatedByID -> PX.SM.Users (CreatedByID=PKID)
PX.Objects.SV.SVEventLabor.UsersByLastModifiedByID -> PX.SM.Users (LastModifiedByID=PKID)
PX.Objects.SV.SVEventLabor.SVEventByEventNoteID -> PX.Objects.SV.SVEvent (EventNoteID=NoteID)
PX.Objects.SV.SVEventLabor.SVResourceByResourceNoteID -> PX.Objects.SV.SVResource (ResourceNoteID=ResourceNoteID)

# PX.Objects.SV.SVEventProjection (EntityType)

Label: "Work Event"
Key: NoteID
Entity sets: PX_Objects_SV_SVEventProjection, WorkEvent1, SVEventProjection

PX.Objects.SV.SVEventProjection.Summary : Edm.String "Summary"
PX.Objects.SV.SVEventProjection.Status : Edm.String "Status"
PX.Objects.SV.SVEventProjection.StartDate : Edm.DateTimeOffset "Start Time"
PX.Objects.SV.SVEventProjection.EndDate : Edm.DateTimeOffset "End Time"
PX.Objects.SV.SVEventProjection.AddressID : Edm.Int32
PX.Objects.SV.SVEventProjection.Location : Edm.String "Location"
PX.Objects.SV.SVEventProjection.Duration : Edm.Int32 "Duration"
PX.Objects.SV.SVEventProjection.RefNoteIDType : Edm.String "Related Entity Type"
PX.Objects.SV.SVEventProjection.RefNoteID : Edm.Guid "Related Document Nbr."
PX.Objects.SV.SVEventProjection.CreatedDateTime : Edm.DateTimeOffset
PX.Objects.SV.SVEventProjection.NoteID : Edm.Guid [key] "ID"
PX.Objects.SV.SVEventProjection.SVAddressByAddressID -> PX.Objects.SV.SVAddress (AddressID=AddressID)
PX.Objects.SV.SVEventProjection.SVTicketCollection -> Collection(PX.Objects.SV.SVTicket)
PX.Objects.SV.SVEventProjection.SVEventLaborCollection -> Collection(PX.Objects.SV.SVEventLabor)
PX.Objects.SV.SVEventProjection.SVEventTaskCollection -> Collection(PX.Objects.SV.SVEventTask)

# PX.Objects.SV.SVEventStatusColor (EntityType)

Label: "Work Event Status Color"
Key: StatusID
Entity sets: PX_Objects_SV_SVEventStatusColor, WorkEventStatusColor, SVEventStatusColor

PX.Objects.SV.SVEventStatusColor.StatusID : Edm.String [key] "Status"
PX.Objects.SV.SVEventStatusColor.IsVisible : Edm.Boolean [required] "Visible"
PX.Objects.SV.SVEventStatusColor.BackgroundColor : Edm.String "Background Color"
PX.Objects.SV.SVEventStatusColor.TextColor : Edm.String "Text Color"
PX.Objects.SV.SVEventStatusColor.BandColor : Edm.String "Bar Color"
PX.Objects.SV.SVEventStatusColor.CreatedByID : Edm.Guid "Created By"
PX.Objects.SV.SVEventStatusColor.CreatedByScreenID : Edm.String
PX.Objects.SV.SVEventStatusColor.CreatedDateTime : Edm.DateTimeOffset
PX.Objects.SV.SVEventStatusColor.LastModifiedByID : Edm.Guid "Last Modified By"
PX.Objects.SV.SVEventStatusColor.LastModifiedByScreenID : Edm.String
PX.Objects.SV.SVEventStatusColor.LastModifiedDateTime : Edm.DateTimeOffset
PX.Objects.SV.SVEventStatusColor.Tstamp : Edm.Binary "Tstamp"
PX.Objects.SV.SVEventStatusColor.UsersByCreatedByID -> PX.SM.Users (CreatedByID=PKID)
PX.Objects.SV.SVEventStatusColor.UsersByLastModifiedByID -> PX.SM.Users (LastModifiedByID=PKID)

# PX.Objects.SV.SVEventTask (EntityType)

Label: "Work Event Task"
Key: EventNoteID, LineNbr
Entity sets: PX_Objects_SV_SVEventTask, WorkEventTask, SVEventTask
Non-filterable, non-selectable: NoteText, DatafeedRemoveEnabled

PX.Objects.SV.SVEventTask.EventNoteID : Edm.Guid [key] "Work Event"
PX.Objects.SV.SVEventTask.LineNbr : Edm.Int32 [key] "Line Nbr."
PX.Objects.SV.SVEventTask.TaskNoteID : Edm.Guid "Work Task"
PX.Objects.SV.SVEventTask.NoteID : Edm.Guid
PX.Objects.SV.SVEventTask.NoteText : Edm.String "Note Text"
PX.Objects.SV.SVEventTask.TaskStatus : Edm.String
PX.Objects.SV.SVEventTask.DatafeedRemoveEnabled : Edm.Boolean
PX.Objects.SV.SVEventTask.tstamp : Edm.Binary
PX.Objects.SV.SVEventTask.CreatedByID : Edm.Guid "Created By"
PX.Objects.SV.SVEventTask.CreatedByScreenID : Edm.String
PX.Objects.SV.SVEventTask.CreatedDateTime : Edm.DateTimeOffset
PX.Objects.SV.SVEventTask.LastModifiedByID : Edm.Guid "Last Modified By"
PX.Objects.SV.SVEventTask.LastModifiedByScreenID : Edm.String
PX.Objects.SV.SVEventTask.LastModifiedDateTime : Edm.DateTimeOffset "Last Modified"
PX.Objects.SV.SVEventTask.UsersByCreatedByID -> PX.SM.Users (CreatedByID=PKID)
PX.Objects.SV.SVEventTask.UsersByLastModifiedByID -> PX.SM.Users (LastModifiedByID=PKID)
PX.Objects.SV.SVEventTask.SVEventByEventNoteID -> PX.Objects.SV.SVEvent (EventNoteID=NoteID)
PX.Objects.SV.SVEventTask.SVWorkTaskByTaskNoteID -> PX.Objects.SV.SVWorkTask (TaskNoteID=NoteID)

# PX.Objects.SV.SVInvoice (EntityType)

Label: "Work Order Invoice"
Key: DocType, RefNbr
Entity sets: PX_Objects_SV_SVInvoice, WorkOrderInvoice, SVInvoice
Non-filterable, non-selectable: NoteText

PX.Objects.SV.SVInvoice.DocType : Edm.String [key] "Type"
PX.Objects.SV.SVInvoice.RefNbr : Edm.String [key] "Reference Nbr."
PX.Objects.SV.SVInvoice.ServiceLocationID : Edm.String "Service Location"
PX.Objects.SV.SVInvoice.NoteID : Edm.Guid
PX.Objects.SV.SVInvoice.NoteText : Edm.String "Note Text"
PX.Objects.SV.SVInvoice.tstamp : Edm.Binary
PX.Objects.SV.SVInvoice.CreatedByID : Edm.Guid "Created By"
PX.Objects.SV.SVInvoice.CreatedByScreenID : Edm.String
PX.Objects.SV.SVInvoice.CreatedDateTime : Edm.DateTimeOffset
PX.Objects.SV.SVInvoice.LastModifiedByID : Edm.Guid "Last Modified By"
PX.Objects.SV.SVInvoice.LastModifiedByScreenID : Edm.String
PX.Objects.SV.SVInvoice.LastModifiedDateTime : Edm.DateTimeOffset
PX.Objects.SV.SVInvoice.ARInvoiceByRefNbr -> PX.Objects.AR.ARInvoice (DocType=DocType, RefNbr=RefNbr)
PX.Objects.SV.SVInvoice.BranchByBranchID -> PX.Objects.GL.Branch
PX.Objects.SV.SVInvoice.UsersByCreatedByID -> PX.SM.Users (CreatedByID=PKID)
PX.Objects.SV.SVInvoice.UsersByLastModifiedByID -> PX.SM.Users (LastModifiedByID=PKID)
PX.Objects.SV.SVInvoice.SVServiceLocationByServiceLocationID -> PX.Objects.SV.SVServiceLocation (ServiceLocationID=ServiceLocationID)

# PX.Objects.SV.SVLicenseType (EntityType)

Label: "License Type"
BaseType: PX.Objects.SV.FSLicenseType
Key: LicenseTypeCD (inherited from PX.Objects.SV.FSLicenseType)
Entity sets: PX_Objects_SV_SVLicenseType, LicenseType2, SVLicenseType

# PX.Objects.SV.SVMarkup (EntityType)

Label: "Markup"
Key: MarkupID
Entity sets: PX_Objects_SV_SVMarkup, Markup, SVMarkup
Non-filterable, non-selectable: NoteText

PX.Objects.SV.SVMarkup.MarkupID : Edm.Int32 [key]
PX.Objects.SV.SVMarkup.MarkupType : Edm.String "Markup Type"
PX.Objects.SV.SVMarkup.TypePriority : Edm.Int32
PX.Objects.SV.SVMarkup.MarkupCode : Edm.String "Markup Code"
PX.Objects.SV.SVMarkup.PriceClassID : Edm.String "Item Price Class"
PX.Objects.SV.SVMarkup.PriceClassPriority : Edm.Int32
PX.Objects.SV.SVMarkup.Description : Edm.String "Description"
PX.Objects.SV.SVMarkup.BreakAmt : Edm.Decimal [required] "Cost Break Amount"
PX.Objects.SV.SVMarkup.MarkupPct : Edm.Decimal [required] "Markup %"
PX.Objects.SV.SVMarkup.EffectiveDate : Edm.DateTimeOffset "Effective Date"
PX.Objects.SV.SVMarkup.ExpirationDate : Edm.DateTimeOffset "Expiration Date"
PX.Objects.SV.SVMarkup.NoteID : Edm.Guid
PX.Objects.SV.SVMarkup.NoteText : Edm.String "Note Text"
PX.Objects.SV.SVMarkup.tstamp : Edm.Binary
PX.Objects.SV.SVMarkup.CreatedByID : Edm.Guid "Created By"
PX.Objects.SV.SVMarkup.CreatedByScreenID : Edm.String
PX.Objects.SV.SVMarkup.CreatedDateTime : Edm.DateTimeOffset
PX.Objects.SV.SVMarkup.LastModifiedByID : Edm.Guid "Last Modified By"
PX.Objects.SV.SVMarkup.LastModifiedByScreenID : Edm.String
PX.Objects.SV.SVMarkup.LastModifiedDateTime : Edm.DateTimeOffset
PX.Objects.SV.SVMarkup.UsersByCreatedByID -> PX.SM.Users (CreatedByID=PKID)
PX.Objects.SV.SVMarkup.UsersByLastModifiedByID -> PX.SM.Users (LastModifiedByID=PKID)
PX.Objects.SV.SVMarkup.INPriceClassByPriceClassID -> PX.Objects.IN.INPriceClass (PriceClassID=PriceClassID)

# PX.Objects.SV.SVMyDayReport (EntityType)

Label: "My Day Report"
Key: EmployeeID
Entity sets: PX_Objects_SV_SVMyDayReport, MyDayReport, SVMyDayReport
Non-filterable, non-selectable: Updated, NoteText

PX.Objects.SV.SVMyDayReport.EmployeeID : Edm.Int32 [key] "Employee"
PX.Objects.SV.SVMyDayReport.Report : Edm.String "My Day Report"
PX.Objects.SV.SVMyDayReport.Updated : Edm.String "Updated"
PX.Objects.SV.SVMyDayReport.NoteID : Edm.Guid
PX.Objects.SV.SVMyDayReport.NoteText : Edm.String "Note Text"
PX.Objects.SV.SVMyDayReport.tstamp : Edm.Binary
PX.Objects.SV.SVMyDayReport.CreatedByID : Edm.Guid "Created By"
PX.Objects.SV.SVMyDayReport.CreatedByScreenID : Edm.String
PX.Objects.SV.SVMyDayReport.CreatedDateTime : Edm.DateTimeOffset
PX.Objects.SV.SVMyDayReport.LastModifiedByID : Edm.Guid "Last Modified By"
PX.Objects.SV.SVMyDayReport.LastModifiedByScreenID : Edm.String
PX.Objects.SV.SVMyDayReport.LastModifiedDateTime : Edm.DateTimeOffset "Last Modified"
PX.Objects.SV.SVMyDayReport.VendorByEmployeeID -> PX.Objects.AP.Vendor (EmployeeID=BAccountID)
PX.Objects.SV.SVMyDayReport.UsersByCreatedByID -> PX.SM.Users (CreatedByID=PKID)
PX.Objects.SV.SVMyDayReport.UsersByLastModifiedByID -> PX.SM.Users (LastModifiedByID=PKID)

# PX.Objects.SV.SVNotification (EntityType)

Label: "Default Notification setup"
BaseType: PX.Objects.CS.NotificationSetup
Key: SetupID (inherited from PX.Objects.CS.NotificationSetup)
Entity sets: PX_Objects_SV_SVNotification

# PX.Objects.SV.SVOrder (EntityType)

Label: "Work Order"
Key: OrderNbr
Entity sets: PX_Objects_SV_SVOrder, WorkOrder, SVOrder
Non-filterable, non-selectable: LocationAddress, IsExpanded, CuryDocumentDiscountTotal, DocumentDiscountTotal, ReplaceTasksAfterSave, CuryDocBal, DocBal, NoteText, CuryRate

PX.Objects.SV.SVOrder.OrderNbr : Edm.String [key] "Work Order"
PX.Objects.SV.SVOrder.OrderType : Edm.String "Order Type"
PX.Objects.SV.SVOrder.Status : Edm.String "Status"
PX.Objects.SV.SVOrder.LineCntr : Edm.Int32 [required]
PX.Objects.SV.SVOrder.Summary : Edm.String "Summary"
PX.Objects.SV.SVOrder.Severity : Edm.String "Severity"
PX.Objects.SV.SVOrder.DocDate : Edm.DateTimeOffset "Date"
PX.Objects.SV.SVOrder.ExpectedDate : Edm.DateTimeOffset "Expected Date"
PX.Objects.SV.SVOrder.Priority : Edm.String "Priority"
PX.Objects.SV.SVOrder.ServiceLocationID : Edm.String "Service Location"
PX.Objects.SV.SVOrder.LocationAddress : Edm.String "Address"
PX.Objects.SV.SVOrder.ServiceLocationComment : Edm.String "Comment"
PX.Objects.SV.SVOrder.LocationContactID : Edm.Int32 "Contact at Location"
PX.Objects.SV.SVOrder.LocationContactEmail : Edm.String "Email"
PX.Objects.SV.SVOrder.LocationContactPhone : Edm.String "Phone"
PX.Objects.SV.SVOrder.CustomerID : Edm.Int32 "Customer"
PX.Objects.SV.SVOrder.CreditHold : Edm.Boolean [required] "Credit Hold"
PX.Objects.SV.SVOrder.CustomerOrderNbr : Edm.String "Customer Order Nbr."
PX.Objects.SV.SVOrder.CallerContactID : Edm.Int32 "Name"
PX.Objects.SV.SVOrder.CallerContactEmail : Edm.String "Email"
PX.Objects.SV.SVOrder.CallerContactPhone : Edm.String "Phone"
PX.Objects.SV.SVOrder.Description : Edm.String "Description"
PX.Objects.SV.SVOrder.CuryID : Edm.String "Currency"
PX.Objects.SV.SVOrder.CuryInfoID : Edm.Int64
PX.Objects.SV.SVOrder.TermsID : Edm.String "Credit Terms"
PX.Objects.SV.SVOrder.TaxZoneID : Edm.String "Tax Zone"
PX.Objects.SV.SVOrder.TaxCalcMode : Edm.String "Tax Calculation Mode"
PX.Objects.SV.SVOrder.AvalaraCustomerUsageType : Edm.String "Tax Exemption Type"
PX.Objects.SV.SVOrder.CuryVatExemptTotal : Edm.Decimal [required] "Tax Exempt Total"
PX.Objects.SV.SVOrder.VatExemptTotal : Edm.Decimal [required]
PX.Objects.SV.SVOrder.CuryVatTaxableTotal : Edm.Decimal [required] "Taxable Total"
PX.Objects.SV.SVOrder.VatTaxableTotal : Edm.Decimal [required]
PX.Objects.SV.SVOrder.ExternalTaxExemptionNumber : Edm.String "Tax Exemption Number"
PX.Objects.SV.SVOrder.DisableAutomaticDiscountCalculation : Edm.Boolean [required] "Disable Automatic Discount Update"
PX.Objects.SV.SVOrder.OrderedQty : Edm.Decimal [required] "Ordered Qty."
PX.Objects.SV.SVOrder.IsExpanded : Edm.Boolean
PX.Objects.SV.SVOrder.CuryExtPriceTotal : Edm.Decimal [required] "Price Total"
PX.Objects.SV.SVOrder.ExtPriceTotal : Edm.Decimal [required]
PX.Objects.SV.SVOrder.CuryLineTotal : Edm.Decimal "Line Total"
PX.Objects.SV.SVOrder.LineTotal : Edm.Decimal
PX.Objects.SV.SVOrder.CuryLineDiscTotal : Edm.Decimal [required] "Line Discount Total"
PX.Objects.SV.SVOrder.LineDiscTotal : Edm.Decimal [required] "Line Discounts"
PX.Objects.SV.SVOrder.CuryGroupDiscTotal : Edm.Decimal [required] "Group Discounts"
PX.Objects.SV.SVOrder.GroupDiscTotal : Edm.Decimal [required] "Group Discounts"
PX.Objects.SV.SVOrder.CuryDocumentDiscTotal : Edm.Decimal [required] "Document Discount"
PX.Objects.SV.SVOrder.DocumentDiscTotal : Edm.Decimal [required] "Document Discount"
PX.Objects.SV.SVOrder.CuryDiscTotal : Edm.Decimal [required] "Discount Total"
PX.Objects.SV.SVOrder.DiscTotal : Edm.Decimal [required]
PX.Objects.SV.SVOrder.CuryDocumentDiscountTotal : Edm.Decimal "Document Discount Total"
PX.Objects.SV.SVOrder.DocumentDiscountTotal : Edm.Decimal
PX.Objects.SV.SVOrder.IsTaxValid : Edm.Boolean "Tax Is Up to Date"
PX.Objects.SV.SVOrder.CuryTaxTotal : Edm.Decimal "Tax Total"
PX.Objects.SV.SVOrder.TaxTotal : Edm.Decimal
PX.Objects.SV.SVOrder.CuryOrderTotal : Edm.Decimal [required] "Order Total"
PX.Objects.SV.SVOrder.OrderTotal : Edm.Decimal [required]
PX.Objects.SV.SVOrder.Billed : Edm.Boolean [required] "Billed"
PX.Objects.SV.SVOrder.Hold : Edm.Boolean [required] "On Hold"
PX.Objects.SV.SVOrder.OpenDoc : Edm.Boolean "Open"
PX.Objects.SV.SVOrder.Completed : Edm.Boolean [required] "Completed"
PX.Objects.SV.SVOrder.Closed : Edm.Boolean [required] "Closed"
PX.Objects.SV.SVOrder.Canceled : Edm.Boolean [required] "Canceled"
PX.Objects.SV.SVOrder.ActualsLineCntr : Edm.Int32 [required]
PX.Objects.SV.SVOrder.CuryUnbilledOrderTotal : Edm.Decimal [required] "Remaining to Bill"
PX.Objects.SV.SVOrder.UnbilledOrderTotal : Edm.Decimal [required]
PX.Objects.SV.SVOrder.CuryBilledOrderTotal : Edm.Decimal [required] "Billed to Date"
PX.Objects.SV.SVOrder.BilledOrderTotal : Edm.Decimal [required]
PX.Objects.SV.SVOrder.CuryActualsTotal : Edm.Decimal [required] "Price Total"
PX.Objects.SV.SVOrder.ActualsTotal : Edm.Decimal [required]
PX.Objects.SV.SVOrder.CuryActualsExtCost : Edm.Decimal [required] "Cost Total"
PX.Objects.SV.SVOrder.ActualsExtCost : Edm.Decimal [required]
PX.Objects.SV.SVOrder.CuryProfitMargin : Edm.Decimal [required] "Profit Margin"
PX.Objects.SV.SVOrder.ProfitMargin : Edm.Decimal [required]
PX.Objects.SV.SVOrder.ProfitMarginPercent : Edm.Decimal [required] "Profit Margin (%)"
PX.Objects.SV.SVOrder.ReplaceTasksAfterSave : Edm.Boolean
PX.Objects.SV.SVOrder.SalesAcctDefault : Edm.String "Use Sales Account From"
PX.Objects.SV.SVOrder.ExpenseAcctDefault : Edm.String "Use Expense Account From"
PX.Objects.SV.SVOrder.StockItemsExpenseAcctDefault : Edm.String "Use Expense Account From"
PX.Objects.SV.SVOrder.CuryAppliedPaymentTotal : Edm.Decimal [required] "Applied to Work Order"
PX.Objects.SV.SVOrder.AppliedPaymentTotal : Edm.Decimal [required]
PX.Objects.SV.SVOrder.CuryBilledPaymentTotal : Edm.Decimal [required] "Applied to Invoice"
PX.Objects.SV.SVOrder.BilledPaymentTotal : Edm.Decimal [required]
PX.Objects.SV.SVOrder.CuryDocBal : Edm.Decimal
PX.Objects.SV.SVOrder.DocBal : Edm.Decimal
PX.Objects.SV.SVOrder.MaterialListLineCntr : Edm.Int32 [required]
PX.Objects.SV.SVOrder.NoteID : Edm.Guid
PX.Objects.SV.SVOrder.NoteText : Edm.String "Note Text"
PX.Objects.SV.SVOrder.tstamp : Edm.Binary
PX.Objects.SV.SVOrder.CreatedByID : Edm.Guid "Created By"
PX.Objects.SV.SVOrder.CreatedByScreenID : Edm.String
PX.Objects.SV.SVOrder.CreatedDateTime : Edm.DateTimeOffset
PX.Objects.SV.SVOrder.LastModifiedByID : Edm.Guid "Last Modified By"
PX.Objects.SV.SVOrder.LastModifiedByScreenID : Edm.String
PX.Objects.SV.SVOrder.LastModifiedDateTime : Edm.DateTimeOffset "Last Modified"
PX.Objects.SV.SVOrder.CuryRate : Edm.Decimal
PX.Objects.SV.SVOrder.BAccountByCustomerID -> PX.Objects.CR.BAccount (CustomerID=BAccountID)
PX.Objects.SV.SVOrder.CustomerByCustomerID -> PX.Objects.AR.Customer (CustomerID=BAccountID)
PX.Objects.SV.SVOrder.ContactByLocationContactID -> PX.Objects.CR.Contact (LocationContactID=ContactID)
PX.Objects.SV.SVOrder.ContactByCallerContactID -> PX.Objects.CR.Contact (CallerContactID=ContactID)
PX.Objects.SV.SVOrder.BranchByBranchID -> PX.Objects.GL.Branch
PX.Objects.SV.SVOrder.CurrencyInfoByCuryInfoID -> PX.Objects.CM.CurrencyInfo (CuryInfoID=CuryInfoID)
PX.Objects.SV.SVOrder.UsersByCreatedByID -> PX.SM.Users (CreatedByID=PKID)
PX.Objects.SV.SVOrder.UsersByLastModifiedByID -> PX.SM.Users (LastModifiedByID=PKID)
PX.Objects.SV.SVOrder.TaxZoneByTaxZoneID -> PX.Objects.TX.TaxZone (TaxZoneID=TaxZoneID)
PX.Objects.SV.SVOrder.TermsByTermsID -> PX.Objects.CS.Terms (TermsID=TermsID)
PX.Objects.SV.SVOrder.INSiteByProcurementSiteID -> PX.Objects.IN.INSite
PX.Objects.SV.SVOrder.CurrencyByCuryID -> PX.Objects.CM.Currency (CuryID=CuryID)
PX.Objects.SV.SVOrder.LocationByCustomerID -> PX.Objects.CR.Location (CustomerID=BAccountID)
PX.Objects.SV.SVOrder.LocationByCustomerLocationID -> PX.Objects.CR.Location (CustomerID=BAccountID)
PX.Objects.SV.SVOrder.SVOrderTypeByOrderType -> PX.Objects.SV.SVOrderType (OrderType=OrderType)
PX.Objects.SV.SVOrder.SVServiceLocationByServiceLocationID -> PX.Objects.SV.SVServiceLocation (ServiceLocationID=ServiceLocationID)
PX.Objects.SV.SVOrder.SVTaxCollection -> Collection(PX.Objects.SV.SVTax)
PX.Objects.SV.SVOrder.SVTaxTranCollection -> Collection(PX.Objects.SV.SVTaxTran)
PX.Objects.SV.SVOrder.SVAdjustCollection -> Collection(PX.Objects.SV.SVAdjust)
PX.Objects.SV.SVOrder.SVOrderActualCollection -> Collection(PX.Objects.SV.SVOrderActual)
PX.Objects.SV.SVOrder.SVOrderDetailCollection -> Collection(PX.Objects.SV.SVOrderDetail)
PX.Objects.SV.SVOrder.SVOrderDiscountDetailCollection -> Collection(PX.Objects.SV.SVOrderDiscountDetail)
PX.Objects.SV.SVOrder.SVOrderGLAccountCollection -> Collection(PX.Objects.SV.SVOrderGLAccount)

# PX.Objects.SV.SVOrderActual (EntityType)

Label: "Work Order Actuals"
Key: LineNbr, OrderNbr
Entity sets: PX_Objects_SV_SVOrderActual, WorkOrderActuals, SVOrderActual
Non-filterable, non-selectable: StkItem, ProfitMarginPercent, NoteText

PX.Objects.SV.SVOrderActual.OrderNbr : Edm.String [key] "Work Order"
PX.Objects.SV.SVOrderActual.LineNbr : Edm.Int32 [key] "Line Nbr."
PX.Objects.SV.SVOrderActual.TicketNbr : Edm.String "Work Ticket"
PX.Objects.SV.SVOrderActual.WorkDate : Edm.DateTimeOffset "Work Date"
PX.Objects.SV.SVOrderActual.InventoryID : Edm.Int32 "Inventory ID"
PX.Objects.SV.SVOrderActual.BillingCategory : Edm.String "Billing Category"
PX.Objects.SV.SVOrderActual.ItemType : Edm.String "Item Type"
PX.Objects.SV.SVOrderActual.Description : Edm.String "Description"
PX.Objects.SV.SVOrderActual.UOM : Edm.String "UOM"
PX.Objects.SV.SVOrderActual.StkItem : Edm.Boolean
PX.Objects.SV.SVOrderActual.PriceRule : Edm.String "Price Rule"
PX.Objects.SV.SVOrderActual.IsFree : Edm.Boolean [required] "Free Item"
PX.Objects.SV.SVOrderActual.IsUseMarkup : Edm.Boolean "Use Markup"
PX.Objects.SV.SVOrderActual.MarkupPct : Edm.Decimal [required] "Markup, %"
PX.Objects.SV.SVOrderActual.ManualMarkup : Edm.Boolean [required] "Manual Markup"
PX.Objects.SV.SVOrderActual.ActualQty : Edm.Decimal [required] "Actual Quantity"
PX.Objects.SV.SVOrderActual.BillableQty : Edm.Decimal "Billable Quantity"
PX.Objects.SV.SVOrderActual.CuryInfoID : Edm.Int64
PX.Objects.SV.SVOrderActual.OrigDocType : Edm.String "Orig. Doc. Type"
PX.Objects.SV.SVOrderActual.OrigNoteID : Edm.Guid "Orig. Doc. Nbr."
PX.Objects.SV.SVOrderActual.CuryStdCost : Edm.Decimal [required] "Standard Cost"
PX.Objects.SV.SVOrderActual.StdCost : Edm.Decimal [required] "Standard Cost in Base Currency"
PX.Objects.SV.SVOrderActual.CuryActualCost : Edm.Decimal [required] "Actual Cost"
PX.Objects.SV.SVOrderActual.ActualCost : Edm.Decimal [required] "Actual Cost in Base Currency"
PX.Objects.SV.SVOrderActual.CuryUnitCost : Edm.Decimal "Unit Cost"
PX.Objects.SV.SVOrderActual.UnitCost : Edm.Decimal [required] "Unit Cost in Base Currency"
PX.Objects.SV.SVOrderActual.CuryExtCost : Edm.Decimal [required] "Ext. Cost"
PX.Objects.SV.SVOrderActual.ExtCost : Edm.Decimal [required] "Ext. Cost in Base Currency"
PX.Objects.SV.SVOrderActual.CuryUnitPrice : Edm.Decimal [required] "Unit Price"
PX.Objects.SV.SVOrderActual.UnitPrice : Edm.Decimal "Unit Price in Base Currency"
PX.Objects.SV.SVOrderActual.ManualPrice : Edm.Boolean [required] "Manual Price"
PX.Objects.SV.SVOrderActual.CuryExtPrice : Edm.Decimal [required] "Ext. Price"
PX.Objects.SV.SVOrderActual.ExtPrice : Edm.Decimal [required] "Ext. Price in Base Currency"
PX.Objects.SV.SVOrderActual.CuryBilledAmt : Edm.Decimal "Billed Amount"
PX.Objects.SV.SVOrderActual.BilledAmt : Edm.Decimal [required] "Billed Amount in Base Currency"
PX.Objects.SV.SVOrderActual.Billed : Edm.Boolean [required] "Billed"
PX.Objects.SV.SVOrderActual.InvoiceType : Edm.String "Invoice Type"
PX.Objects.SV.SVOrderActual.InvoiceNbr : Edm.String "Invoice Nbr."
PX.Objects.SV.SVOrderActual.InvoiceLineNbr : Edm.Int32 "Invoice Line Nbr."
PX.Objects.SV.SVOrderActual.BranchID : Edm.Int32 "Branch"
PX.Objects.SV.SVOrderActual.EmployeeID : Edm.Int32 "Employee ID"
PX.Objects.SV.SVOrderActual.EmployeeName : Edm.String "Employee Name"
PX.Objects.SV.SVOrderActual.CustomerID : Edm.Int32 "Customer"
PX.Objects.SV.SVOrderActual.CustomerRefNbr : Edm.String "Customer Order Nbr."
PX.Objects.SV.SVOrderActual.BillingStatus : Edm.String "Billing Status"
PX.Objects.SV.SVOrderActual.TaxCategoryID : Edm.String "Tax Category"
PX.Objects.SV.SVOrderActual.ProfitMarginPercent : Edm.Decimal "Profit Margin (%)"
PX.Objects.SV.SVOrderActual.SortOrder : Edm.Int32
PX.Objects.SV.SVOrderActual.NoteID : Edm.Guid
PX.Objects.SV.SVOrderActual.NoteText : Edm.String "Note Text"
PX.Objects.SV.SVOrderActual.tstamp : Edm.Binary
PX.Objects.SV.SVOrderActual.CreatedByID : Edm.Guid "Created By"
PX.Objects.SV.SVOrderActual.CreatedByScreenID : Edm.String
PX.Objects.SV.SVOrderActual.CreatedDateTime : Edm.DateTimeOffset
PX.Objects.SV.SVOrderActual.LastModifiedByID : Edm.Guid "Last Modified By"
PX.Objects.SV.SVOrderActual.LastModifiedByScreenID : Edm.String
PX.Objects.SV.SVOrderActual.LastModifiedDateTime : Edm.DateTimeOffset
PX.Objects.SV.SVOrderActual.EPEmployeeByEmployeeID -> PX.Objects.EP.EPEmployee (EmployeeID=BAccountID)
PX.Objects.SV.SVOrderActual.BAccountByCustomerID -> PX.Objects.CR.BAccount (CustomerID=BAccountID)
PX.Objects.SV.SVOrderActual.CustomerByCustomerID -> PX.Objects.AR.Customer (CustomerID=BAccountID)
PX.Objects.SV.SVOrderActual.InventoryItemByInventoryID -> PX.Objects.IN.InventoryItem (InventoryID=InventoryID)
PX.Objects.SV.SVOrderActual.SVTicketByTicketNbr -> PX.Objects.SV.SVTicket (TicketNbr=TicketNbr)
PX.Objects.SV.SVOrderActual.BranchByBranchID -> PX.Objects.GL.Branch (BranchID=BranchID)
PX.Objects.SV.SVOrderActual.UsersByCreatedByID -> PX.SM.Users (CreatedByID=PKID)
PX.Objects.SV.SVOrderActual.UsersByLastModifiedByID -> PX.SM.Users (LastModifiedByID=PKID)
PX.Objects.SV.SVOrderActual.TaxCategoryByTaxCategoryID -> PX.Objects.TX.TaxCategory (TaxCategoryID=TaxCategoryID)
PX.Objects.SV.SVOrderActual.INLocationBySiteID -> PX.Objects.IN.INLocation
PX.Objects.SV.SVOrderActual.INSiteBySiteID -> PX.Objects.IN.INSite
PX.Objects.SV.SVOrderActual.INSubItemBySubItemID -> PX.Objects.IN.INSubItem
PX.Objects.SV.SVOrderActual.INUnitByInventoryID -> PX.Objects.IN.INUnit (UOM=FromUnit, InventoryID=InventoryID)
PX.Objects.SV.SVOrderActual.AccountBySalesAcctID -> PX.Objects.GL.Account
PX.Objects.SV.SVOrderActual.AccountByExpenseAcctID -> PX.Objects.GL.Account
PX.Objects.SV.SVOrderActual.SubBySalesSubID -> PX.Objects.GL.Sub
PX.Objects.SV.SVOrderActual.SubByExpenseSubID -> PX.Objects.GL.Sub
PX.Objects.SV.SVOrderActual.LocationByCustomerID -> PX.Objects.CR.Location (CustomerID=BAccountID)
PX.Objects.SV.SVOrderActual.SVOrderByOrderNbr -> PX.Objects.SV.SVOrder (OrderNbr=OrderNbr)

# PX.Objects.SV.SVOrderDetail (EntityType)

Label: "Work Order Estimate"
Key: LineNbr, OrderNbr
Entity sets: PX_Objects_SV_SVOrderDetail, WorkOrderEstimate, SVOrderDetail
Non-filterable, non-selectable: FreezeManualDisc, SkipDisc, StkItem, NoteText

PX.Objects.SV.SVOrderDetail.OrderNbr : Edm.String [key] "Order Nbr."
PX.Objects.SV.SVOrderDetail.LineNbr : Edm.Int32 [key] "Line Nbr."
PX.Objects.SV.SVOrderDetail.SortOrder : Edm.Int32 "Sort Order"
PX.Objects.SV.SVOrderDetail.ItemType : Edm.String "Item Type"
PX.Objects.SV.SVOrderDetail.BranchID : Edm.Int32 "Branch"
PX.Objects.SV.SVOrderDetail.CustomerID : Edm.Int32
PX.Objects.SV.SVOrderDetail.BillingCategory : Edm.String "Billing Category"
PX.Objects.SV.SVOrderDetail.PriceRule : Edm.String "Price Rule"
PX.Objects.SV.SVOrderDetail.InventoryID : Edm.Int32 "Inventory ID"
PX.Objects.SV.SVOrderDetail.TranDesc : Edm.String "Description"
PX.Objects.SV.SVOrderDetail.ManualPrice : Edm.Boolean [required] "Manual Price"
PX.Objects.SV.SVOrderDetail.UOM : Edm.String "UOM"
PX.Objects.SV.SVOrderDetail.CuryInfoID : Edm.Int64
PX.Objects.SV.SVOrderDetail.EstimatedQty : Edm.Decimal "Estimated Quantity"
PX.Objects.SV.SVOrderDetail.BaseEstimatedQty : Edm.Decimal
PX.Objects.SV.SVOrderDetail.CuryUnitCost : Edm.Decimal [required] "Estimated Unit Cost"
PX.Objects.SV.SVOrderDetail.UnitCost : Edm.Decimal [required]
PX.Objects.SV.SVOrderDetail.CuryExtCost : Edm.Decimal [required] "Estimated Ext. Cost"
PX.Objects.SV.SVOrderDetail.ExtCost : Edm.Decimal
PX.Objects.SV.SVOrderDetail.CuryUnitPrice : Edm.Decimal [required] "Unit Price"
PX.Objects.SV.SVOrderDetail.UnitPrice : Edm.Decimal [required]
PX.Objects.SV.SVOrderDetail.EstimatedDuration : Edm.Int32 "Estimated Duration"
PX.Objects.SV.SVOrderDetail.IsFree : Edm.Boolean [required] "Free Item"
PX.Objects.SV.SVOrderDetail.IsUseMarkup : Edm.Boolean "Use Markup"
PX.Objects.SV.SVOrderDetail.MarkupPct : Edm.Decimal "Markup, %"
PX.Objects.SV.SVOrderDetail.ManualMarkup : Edm.Boolean [required] "Manual Markup"
PX.Objects.SV.SVOrderDetail.ManualDisc : Edm.Boolean [required] "Manual Discount"
PX.Objects.SV.SVOrderDetail.DiscPct : Edm.Decimal "Discount, %"
PX.Objects.SV.SVOrderDetail.CuryDiscAmt : Edm.Decimal "Discount Amount"
PX.Objects.SV.SVOrderDetail.DiscAmt : Edm.Decimal
PX.Objects.SV.SVOrderDetail.CuryAmount : Edm.Decimal [required] "Amount"
PX.Objects.SV.SVOrderDetail.Amount : Edm.Decimal
PX.Objects.SV.SVOrderDetail.CuryExtPrice : Edm.Decimal [required] "Estimated Ext. Price"
PX.Objects.SV.SVOrderDetail.ExtPrice : Edm.Decimal [required]
PX.Objects.SV.SVOrderDetail.FreezeManualDisc : Edm.Boolean
PX.Objects.SV.SVOrderDetail.SkipDisc : Edm.Boolean
PX.Objects.SV.SVOrderDetail.GroupDiscountRate : Edm.Decimal
PX.Objects.SV.SVOrderDetail.DocumentDiscountRate : Edm.Decimal
PX.Objects.SV.SVOrderDetail.DiscountID : Edm.String "Discount Code"
PX.Objects.SV.SVOrderDetail.DiscountSequenceID : Edm.String "Discount Sequence"
PX.Objects.SV.SVOrderDetail.SkipLineDiscounts : Edm.Boolean [required] "Ignore Automatic Line Discounts"
PX.Objects.SV.SVOrderDetail.TaxCategoryID : Edm.String "Tax Category"
PX.Objects.SV.SVOrderDetail.StkItem : Edm.Boolean
PX.Objects.SV.SVOrderDetail.ProjectID : Edm.Int32 "ProjectID"
PX.Objects.SV.SVOrderDetail.NoteID : Edm.Guid
PX.Objects.SV.SVOrderDetail.NoteText : Edm.String "Note Text"
PX.Objects.SV.SVOrderDetail.tstamp : Edm.Binary
PX.Objects.SV.SVOrderDetail.CreatedByID : Edm.Guid "Created By"
PX.Objects.SV.SVOrderDetail.CreatedByScreenID : Edm.String
PX.Objects.SV.SVOrderDetail.CreatedDateTime : Edm.DateTimeOffset
PX.Objects.SV.SVOrderDetail.LastModifiedByID : Edm.Guid "Last Modified By"
PX.Objects.SV.SVOrderDetail.LastModifiedByScreenID : Edm.String
PX.Objects.SV.SVOrderDetail.LastModifiedDateTime : Edm.DateTimeOffset
PX.Objects.SV.SVOrderDetail.CuryTaxAmt : Edm.Decimal "Tax Amount"
PX.Objects.SV.SVOrderDetail.TaxAmt : Edm.Decimal "Tax Amount"
PX.Objects.SV.SVOrderDetail.PMProjectByProjectID -> PX.Objects.PM.PMProject (ProjectID=ContractID)
PX.Objects.SV.SVOrderDetail.PMTaskByProjectTaskID -> PX.Objects.PM.PMTask (ProjectID=ProjectID)
PX.Objects.SV.SVOrderDetail.PMTaskByProjectID -> PX.Objects.PM.PMTask (ProjectID=ProjectID)
PX.Objects.SV.SVOrderDetail.CustomerByCustomerID -> PX.Objects.AR.Customer (CustomerID=BAccountID)
PX.Objects.SV.SVOrderDetail.InventoryItemByInventoryID -> PX.Objects.IN.InventoryItem (InventoryID=InventoryID)
PX.Objects.SV.SVOrderDetail.BranchByBranchID -> PX.Objects.GL.Branch (BranchID=BranchID)
PX.Objects.SV.SVOrderDetail.UsersByCreatedByID -> PX.SM.Users (CreatedByID=PKID)
PX.Objects.SV.SVOrderDetail.UsersByLastModifiedByID -> PX.SM.Users (LastModifiedByID=PKID)
PX.Objects.SV.SVOrderDetail.TaxCategoryByTaxCategoryID -> PX.Objects.TX.TaxCategory (TaxCategoryID=TaxCategoryID)
PX.Objects.SV.SVOrderDetail.PMCostCodeByCostCodeID -> PX.Objects.PM.PMCostCode
PX.Objects.SV.SVOrderDetail.INSiteBySiteID -> PX.Objects.IN.INSite
PX.Objects.SV.SVOrderDetail.INUnitByInventoryID -> PX.Objects.IN.INUnit (UOM=FromUnit, InventoryID=InventoryID)
PX.Objects.SV.SVOrderDetail.AccountByAcctID -> PX.Objects.GL.Account
PX.Objects.SV.SVOrderDetail.SubBySubID -> PX.Objects.GL.Sub
PX.Objects.SV.SVOrderDetail.LocationByCustomerID -> PX.Objects.CR.Location (CustomerID=BAccountID)
PX.Objects.SV.SVOrderDetail.LocationByCustomerLocationID -> PX.Objects.CR.Location (CustomerID=BAccountID)
PX.Objects.SV.SVOrderDetail.ARDiscountByDiscountID -> PX.Objects.AR.ARDiscount (DiscountID=DiscountID)
PX.Objects.SV.SVOrderDetail.SVOrderByOrderNbr -> PX.Objects.SV.SVOrder (OrderNbr=OrderNbr)
PX.Objects.SV.SVOrderDetail.SVTaxCollection -> Collection(PX.Objects.SV.SVTax)
PX.Objects.SV.SVOrderDetail.SVTaxTranCollection -> Collection(PX.Objects.SV.SVTaxTran)

# PX.Objects.SV.SVOrderDiscountDetail (EntityType)

Label: "Work Order Discount"
Key: OrderNbr, RecordID, Type
Entity sets: PX_Objects_SV_SVOrderDiscountDetail, WorkOrderDiscount, SVOrderDiscountDetail
Non-filterable, non-selectable: IsOrigDocDiscount

PX.Objects.SV.SVOrderDiscountDetail.OrderNbr : Edm.String [key] "Order Nbr."
PX.Objects.SV.SVOrderDiscountDetail.RecordID : Edm.Int32 [key]
PX.Objects.SV.SVOrderDiscountDetail.LineNbr : Edm.Int32
PX.Objects.SV.SVOrderDiscountDetail.SkipDiscount : Edm.Boolean [required] "Skip Discount"
PX.Objects.SV.SVOrderDiscountDetail.DiscountID : Edm.String "Discount Code"
PX.Objects.SV.SVOrderDiscountDetail.DiscountSequenceID : Edm.String "Sequence ID"
PX.Objects.SV.SVOrderDiscountDetail.Type : Edm.String [key] "Type"
PX.Objects.SV.SVOrderDiscountDetail.CuryInfoID : Edm.Int64
PX.Objects.SV.SVOrderDiscountDetail.DiscountableAmt : Edm.Decimal
PX.Objects.SV.SVOrderDiscountDetail.CuryDiscountableAmt : Edm.Decimal "Discountable Amt."
PX.Objects.SV.SVOrderDiscountDetail.DiscountableQty : Edm.Decimal "Discountable Qty."
PX.Objects.SV.SVOrderDiscountDetail.DiscountAmt : Edm.Decimal
PX.Objects.SV.SVOrderDiscountDetail.CuryDiscountAmt : Edm.Decimal "Discount Amt."
PX.Objects.SV.SVOrderDiscountDetail.DiscountPct : Edm.Decimal "Discount Percent"
PX.Objects.SV.SVOrderDiscountDetail.FreeItemID : Edm.Int32 "Free Item"
PX.Objects.SV.SVOrderDiscountDetail.FreeItemQty : Edm.Decimal "Free Item Qty."
PX.Objects.SV.SVOrderDiscountDetail.IsManual : Edm.Boolean [required] "Manual Discount"
PX.Objects.SV.SVOrderDiscountDetail.IsOrigDocDiscount : Edm.Boolean
PX.Objects.SV.SVOrderDiscountDetail.ExtDiscCode : Edm.String "External Discount Code"
PX.Objects.SV.SVOrderDiscountDetail.Description : Edm.String "Description"
PX.Objects.SV.SVOrderDiscountDetail.tstamp : Edm.Binary
PX.Objects.SV.SVOrderDiscountDetail.CreatedByID : Edm.Guid "Created By"
PX.Objects.SV.SVOrderDiscountDetail.CreatedByScreenID : Edm.String
PX.Objects.SV.SVOrderDiscountDetail.CreatedDateTime : Edm.DateTimeOffset
PX.Objects.SV.SVOrderDiscountDetail.LastModifiedByID : Edm.Guid "Last Modified By"
PX.Objects.SV.SVOrderDiscountDetail.LastModifiedByScreenID : Edm.String
PX.Objects.SV.SVOrderDiscountDetail.LastModifiedDateTime : Edm.DateTimeOffset
PX.Objects.SV.SVOrderDiscountDetail.InventoryItemByFreeItemID -> PX.Objects.IN.InventoryItem (FreeItemID=InventoryID)
PX.Objects.SV.SVOrderDiscountDetail.CurrencyInfoByCuryInfoID -> PX.Objects.CM.CurrencyInfo (CuryInfoID=CuryInfoID)
PX.Objects.SV.SVOrderDiscountDetail.UsersByCreatedByID -> PX.SM.Users (CreatedByID=PKID)
PX.Objects.SV.SVOrderDiscountDetail.UsersByLastModifiedByID -> PX.SM.Users (LastModifiedByID=PKID)
PX.Objects.SV.SVOrderDiscountDetail.ARDiscountByDiscountID -> PX.Objects.AR.ARDiscount (DiscountID=DiscountID)
PX.Objects.SV.SVOrderDiscountDetail.DiscountSequenceByDiscountSequenceID -> PX.Objects.AR.DiscountSequence (DiscountID=DiscountID, DiscountSequenceID=DiscountSequenceID)
PX.Objects.SV.SVOrderDiscountDetail.DiscountSequenceByDiscountID -> PX.Objects.AR.DiscountSequence (DiscountSequenceID=DiscountSequenceID, DiscountID=DiscountID)
PX.Objects.SV.SVOrderDiscountDetail.SVOrderByOrderNbr -> PX.Objects.SV.SVOrder (OrderNbr=OrderNbr)

# PX.Objects.SV.SVOrderGLAccount (EntityType)

Label: "Work Order GL Accounts"
Key: BillingCategory, OrderNbr
Entity sets: PX_Objects_SV_SVOrderGLAccount, WorkOrderGLAccounts, SVOrderGLAccount
Non-filterable, non-selectable: SalesAcctCD, ExpenseAcctCD

PX.Objects.SV.SVOrderGLAccount.OrderNbr : Edm.String [key] "Order Nbr."
PX.Objects.SV.SVOrderGLAccount.BillingCategory : Edm.String [key] "Billing Category"
PX.Objects.SV.SVOrderGLAccount.SalesAcctCD : Edm.String "Sales Account Desc."
PX.Objects.SV.SVOrderGLAccount.ExpenseAcctCD : Edm.String "Expense Account Desc."
PX.Objects.SV.SVOrderGLAccount.tstamp : Edm.Binary
PX.Objects.SV.SVOrderGLAccount.CreatedByID : Edm.Guid "Created By"
PX.Objects.SV.SVOrderGLAccount.CreatedByScreenID : Edm.String
PX.Objects.SV.SVOrderGLAccount.CreatedDateTime : Edm.DateTimeOffset
PX.Objects.SV.SVOrderGLAccount.LastModifiedByID : Edm.Guid "Last Modified By"
PX.Objects.SV.SVOrderGLAccount.LastModifiedByScreenID : Edm.String
PX.Objects.SV.SVOrderGLAccount.LastModifiedDateTime : Edm.DateTimeOffset
PX.Objects.SV.SVOrderGLAccount.UsersByCreatedByID -> PX.SM.Users (CreatedByID=PKID)
PX.Objects.SV.SVOrderGLAccount.UsersByLastModifiedByID -> PX.SM.Users (LastModifiedByID=PKID)
PX.Objects.SV.SVOrderGLAccount.AccountBySalesAcctID -> PX.Objects.GL.Account
PX.Objects.SV.SVOrderGLAccount.AccountByExpenseAcctID -> PX.Objects.GL.Account
PX.Objects.SV.SVOrderGLAccount.SubBySalesSubID -> PX.Objects.GL.Sub
PX.Objects.SV.SVOrderGLAccount.SubByExpenseSubID -> PX.Objects.GL.Sub
PX.Objects.SV.SVOrderGLAccount.SVOrderByOrderNbr -> PX.Objects.SV.SVOrder (OrderNbr=OrderNbr)

# PX.Objects.SV.SVOrderProjection (EntityType)

Label: "Work Order"
Key: OrderNbr
Entity sets: PX_Objects_SV_SVOrderProjection, WorkOrder1, SVOrderProjection

PX.Objects.SV.SVOrderProjection.OrderNbr : Edm.String [key] "Order Nbr."
PX.Objects.SV.SVOrderProjection.NoteID : Edm.Guid
PX.Objects.SV.SVOrderProjection.CustomerID : Edm.Int32
PX.Objects.SV.SVOrderProjection.CustomerLocationID : Edm.Int32
PX.Objects.SV.SVOrderProjection.BranchID : Edm.Int32
PX.Objects.SV.SVOrderProjection.BAccountByCustomerID -> PX.Objects.CR.BAccount (CustomerID=BAccountID)
PX.Objects.SV.SVOrderProjection.CustomerByCustomerID -> PX.Objects.AR.Customer (CustomerID=BAccountID)
PX.Objects.SV.SVOrderProjection.BranchByBranchID -> PX.Objects.GL.Branch (BranchID=BranchID)
PX.Objects.SV.SVOrderProjection.LocationByCustomerID -> PX.Objects.CR.Location (CustomerLocationID=LocationID, CustomerID=BAccountID)
PX.Objects.SV.SVOrderProjection.LocationByCustomerLocationID -> PX.Objects.CR.Location (CustomerID=BAccountID, CustomerLocationID=LocationID)
PX.Objects.SV.SVOrderProjection.SVTaxCollection -> Collection(PX.Objects.SV.SVTax)
PX.Objects.SV.SVOrderProjection.SVTaxTranCollection -> Collection(PX.Objects.SV.SVTaxTran)
PX.Objects.SV.SVOrderProjection.SVAdjustCollection -> Collection(PX.Objects.SV.SVAdjust)
PX.Objects.SV.SVOrderProjection.SVOrderActualCollection -> Collection(PX.Objects.SV.SVOrderActual)
PX.Objects.SV.SVOrderProjection.SVOrderDetailCollection -> Collection(PX.Objects.SV.SVOrderDetail)
PX.Objects.SV.SVOrderProjection.SVOrderDiscountDetailCollection -> Collection(PX.Objects.SV.SVOrderDiscountDetail)
PX.Objects.SV.SVOrderProjection.SVOrderGLAccountCollection -> Collection(PX.Objects.SV.SVOrderGLAccount)

# PX.Objects.SV.SVOrderTask (EntityType)

Label: "Work Order Task"
Key: TaskID
Entity sets: PX_Objects_SV_SVOrderTask, WorkOrderTask, SVOrderTask
Non-filterable, non-selectable: SourceEventNoteID, Workforce, HasMoreEvents, EventStartDate, EventEndDate, EventDuration, EventStatus, EventSummary, EventCount, EventBandColor, DatafeedRemoveEnabled

PX.Objects.SV.SVOrderTask.TaskID : Edm.String [key] "Task ID"
PX.Objects.SV.SVOrderTask.Description : Edm.String "Description"
PX.Objects.SV.SVOrderTask.Summary : Edm.String "Summary"
PX.Objects.SV.SVOrderTask.TaskType : Edm.String "Task Type"
PX.Objects.SV.SVOrderTask.Status : Edm.String "Status"
PX.Objects.SV.SVOrderTask.Priority : Edm.String "Priority"
PX.Objects.SV.SVOrderTask.Severity : Edm.String "Severity"
PX.Objects.SV.SVOrderTask.RefNoteIDType : Edm.String "Related Document Type"
PX.Objects.SV.SVOrderTask.RefNoteID : Edm.Guid "Related Document Nbr."
PX.Objects.SV.SVOrderTask.StartDate : Edm.DateTimeOffset "Planned Start Date"
PX.Objects.SV.SVOrderTask.EndDate : Edm.DateTimeOffset "Due Date"
PX.Objects.SV.SVOrderTask.CompletedDate : Edm.DateTimeOffset "Completed On"
PX.Objects.SV.SVOrderTask.EstimatedDuration : Edm.Int32 "Estimated Duration"
PX.Objects.SV.SVOrderTask.PercentCompletion : Edm.Int32 "Completion (%)"
PX.Objects.SV.SVOrderTask.SchedulableItem : Edm.Boolean "Schedulable"
PX.Objects.SV.SVOrderTask.ActionLineCntr : Edm.Int32
PX.Objects.SV.SVOrderTask.LaborLineCntr : Edm.Int32
PX.Objects.SV.SVOrderTask.ResourcePropertyLineCntr : Edm.Int32
PX.Objects.SV.SVOrderTask.NoteID : Edm.Guid
PX.Objects.SV.SVOrderTask.IsScheduled : Edm.Boolean "Scheduled"
PX.Objects.SV.SVOrderTask.SourceEventNoteID : Edm.Guid
PX.Objects.SV.SVOrderTask.tstamp : Edm.Binary
PX.Objects.SV.SVOrderTask.CreatedByID : Edm.Guid "Created By"
PX.Objects.SV.SVOrderTask.CreatedByScreenID : Edm.String
PX.Objects.SV.SVOrderTask.CreatedDateTime : Edm.DateTimeOffset
PX.Objects.SV.SVOrderTask.LastModifiedByID : Edm.Guid "Last Modified By"
PX.Objects.SV.SVOrderTask.LastModifiedByScreenID : Edm.String
PX.Objects.SV.SVOrderTask.LastModifiedDateTime : Edm.DateTimeOffset
PX.Objects.SV.SVOrderTask.Workforce : Edm.String
PX.Objects.SV.SVOrderTask.HasMoreEvents : Edm.String "This task has more events"
PX.Objects.SV.SVOrderTask.EventStartDate : Edm.DateTimeOffset "Event Start Date"
PX.Objects.SV.SVOrderTask.EventEndDate : Edm.DateTimeOffset "Event End Date"
PX.Objects.SV.SVOrderTask.EventDuration : Edm.Int32 "Duration"
PX.Objects.SV.SVOrderTask.EventStatus : Edm.String "Event Status"
PX.Objects.SV.SVOrderTask.EventSummary : Edm.String "Event Summary"
PX.Objects.SV.SVOrderTask.EventCount : Edm.Int32
PX.Objects.SV.SVOrderTask.EventBandColor : Edm.String
PX.Objects.SV.SVOrderTask.DatafeedRemoveEnabled : Edm.Boolean
PX.Objects.SV.SVOrderTask.SVWorkTaskByTaskID -> PX.Objects.SV.SVWorkTask (TaskID=TaskID)
PX.Objects.SV.SVOrderTask.SVWorkTaskLaborCollection -> Collection(PX.Objects.SV.SVWorkTaskLabor)
PX.Objects.SV.SVOrderTask.SVEventTaskCollection -> Collection(PX.Objects.SV.SVEventTask)
PX.Objects.SV.SVOrderTask.SVWorkTaskActionCollection -> Collection(PX.Objects.SV.SVWorkTaskAction)
PX.Objects.SV.SVOrderTask.SVWorkTaskResourcePropertyCollection -> Collection(PX.Objects.SV.SVWorkTaskResourceProperty)
PX.Objects.SV.SVOrderTask.SVOrderTaskCollection -> Collection(PX.Objects.SV.SVOrderTask)

# PX.Objects.SV.SVOrderType (EntityType)

Label: "Work Order Type"
Key: OrderType
Entity sets: PX_Objects_SV_SVOrderType, WorkOrderType, SVOrderType
Non-filterable, non-selectable: TotalEstDuration, NoteText

PX.Objects.SV.SVOrderType.OrderType : Edm.String [key] "Order Type"
PX.Objects.SV.SVOrderType.Description : Edm.String "Description"
PX.Objects.SV.SVOrderType.Active : Edm.Boolean [required] "Active"
PX.Objects.SV.SVOrderType.DefaultBillingStatus : Edm.String "Default Billing Status"
PX.Objects.SV.SVOrderType.SalesAcctDefault : Edm.String "Use Sales Account From"
PX.Objects.SV.SVOrderType.ExpenseAcctDefault : Edm.String "Use Expense Account From"
PX.Objects.SV.SVOrderType.StockItemsExpenseAcctDefault : Edm.String "Use Expense Account From"
PX.Objects.SV.SVOrderType.TotalEstDuration : Edm.Int32 "Total Estimated Duration"
PX.Objects.SV.SVOrderType.IsTicketSignRequired : Edm.Boolean [required] "Require Signature on Work Summary Report"
PX.Objects.SV.SVOrderType.NoteID : Edm.Guid
PX.Objects.SV.SVOrderType.NoteText : Edm.String "Note Text"
PX.Objects.SV.SVOrderType.tstamp : Edm.Binary
PX.Objects.SV.SVOrderType.CreatedByID : Edm.Guid "Created By"
PX.Objects.SV.SVOrderType.CreatedByScreenID : Edm.String
PX.Objects.SV.SVOrderType.CreatedDateTime : Edm.DateTimeOffset
PX.Objects.SV.SVOrderType.LastModifiedByID : Edm.Guid "Last Modified By"
PX.Objects.SV.SVOrderType.LastModifiedByScreenID : Edm.String
PX.Objects.SV.SVOrderType.LastModifiedDateTime : Edm.DateTimeOffset
PX.Objects.SV.SVOrderType.UsersByCreatedByID -> PX.SM.Users (CreatedByID=PKID)
PX.Objects.SV.SVOrderType.UsersByLastModifiedByID -> PX.SM.Users (LastModifiedByID=PKID)
PX.Objects.SV.SVOrderType.AccountBySalesAcctDefault -> PX.Objects.GL.Account (SalesAcctDefault=AccountID)
PX.Objects.SV.SVOrderType.SVOrderCollection -> Collection(PX.Objects.SV.SVOrder)
PX.Objects.SV.SVOrderType.SVOrderTypeGLAccountCollection -> Collection(PX.Objects.SV.SVOrderTypeGLAccount)
PX.Objects.SV.SVOrderType.SVOrderTypeTaskTemplateCollection -> Collection(PX.Objects.SV.SVOrderTypeTaskTemplate)
PX.Objects.SV.SVOrderType.SVSetupCollection -> Collection(PX.Objects.SV.SVSetup)

# PX.Objects.SV.SVOrderTypeGLAccount (EntityType)

Label: "Work Order Type GL Accounts"
Key: BillingCategory, OrderType
Entity sets: PX_Objects_SV_SVOrderTypeGLAccount, WorkOrderTypeGLAccounts, SVOrderTypeGLAccount
Non-filterable, non-selectable: SalesAcctCD, ExpenseAcctCD

PX.Objects.SV.SVOrderTypeGLAccount.OrderType : Edm.String [key] "Order Type"
PX.Objects.SV.SVOrderTypeGLAccount.BillingCategory : Edm.String [key] "Billing Category"
PX.Objects.SV.SVOrderTypeGLAccount.SalesAcctCD : Edm.String "Sales Account Desc."
PX.Objects.SV.SVOrderTypeGLAccount.ExpenseAcctCD : Edm.String "Expense Account Desc."
PX.Objects.SV.SVOrderTypeGLAccount.tstamp : Edm.Binary
PX.Objects.SV.SVOrderTypeGLAccount.CreatedByID : Edm.Guid "Created By"
PX.Objects.SV.SVOrderTypeGLAccount.CreatedByScreenID : Edm.String
PX.Objects.SV.SVOrderTypeGLAccount.CreatedDateTime : Edm.DateTimeOffset
PX.Objects.SV.SVOrderTypeGLAccount.LastModifiedByID : Edm.Guid "Last Modified By"
PX.Objects.SV.SVOrderTypeGLAccount.LastModifiedByScreenID : Edm.String
PX.Objects.SV.SVOrderTypeGLAccount.LastModifiedDateTime : Edm.DateTimeOffset
PX.Objects.SV.SVOrderTypeGLAccount.UsersByCreatedByID -> PX.SM.Users (CreatedByID=PKID)
PX.Objects.SV.SVOrderTypeGLAccount.UsersByLastModifiedByID -> PX.SM.Users (LastModifiedByID=PKID)
PX.Objects.SV.SVOrderTypeGLAccount.AccountBySalesAcctID -> PX.Objects.GL.Account
PX.Objects.SV.SVOrderTypeGLAccount.AccountByExpenseAcctID -> PX.Objects.GL.Account
PX.Objects.SV.SVOrderTypeGLAccount.SubBySalesSubID -> PX.Objects.GL.Sub
PX.Objects.SV.SVOrderTypeGLAccount.SubByExpenseSubID -> PX.Objects.GL.Sub
PX.Objects.SV.SVOrderTypeGLAccount.SVOrderTypeByOrderType -> PX.Objects.SV.SVOrderType (OrderType=OrderType)

# PX.Objects.SV.SVOrderTypeTaskTemplate (EntityType)

Label: "Task Templates tab"
Key: NoteID, OrderType
Entity sets: PX_Objects_SV_SVOrderTypeTaskTemplate, TaskTemplatestab, SVOrderTypeTaskTemplate
Non-filterable, non-selectable: NoteText

PX.Objects.SV.SVOrderTypeTaskTemplate.OrderType : Edm.String [key] "Order Type ID"
PX.Objects.SV.SVOrderTypeTaskTemplate.TaskTemplateID : Edm.String "Task Template ID"
PX.Objects.SV.SVOrderTypeTaskTemplate.IsDefault : Edm.Boolean [required] "Default"
PX.Objects.SV.SVOrderTypeTaskTemplate.NoteID : Edm.Guid [key]
PX.Objects.SV.SVOrderTypeTaskTemplate.NoteText : Edm.String "Note Text"
PX.Objects.SV.SVOrderTypeTaskTemplate.tstamp : Edm.Binary
PX.Objects.SV.SVOrderTypeTaskTemplate.CreatedByID : Edm.Guid "Created By"
PX.Objects.SV.SVOrderTypeTaskTemplate.CreatedByScreenID : Edm.String
PX.Objects.SV.SVOrderTypeTaskTemplate.CreatedDateTime : Edm.DateTimeOffset
PX.Objects.SV.SVOrderTypeTaskTemplate.LastModifiedByID : Edm.Guid "Last Modified By"
PX.Objects.SV.SVOrderTypeTaskTemplate.LastModifiedByScreenID : Edm.String
PX.Objects.SV.SVOrderTypeTaskTemplate.LastModifiedDateTime : Edm.DateTimeOffset
PX.Objects.SV.SVOrderTypeTaskTemplate.UsersByCreatedByID -> PX.SM.Users (CreatedByID=PKID)
PX.Objects.SV.SVOrderTypeTaskTemplate.UsersByLastModifiedByID -> PX.SM.Users (LastModifiedByID=PKID)
PX.Objects.SV.SVOrderTypeTaskTemplate.SVOrderTypeByOrderType -> PX.Objects.SV.SVOrderType (OrderType=OrderType)
PX.Objects.SV.SVOrderTypeTaskTemplate.SVWorkTaskTemplateByTaskTemplateID -> PX.Objects.SV.SVWorkTaskTemplate (TaskTemplateID=TaskTemplateID)

# PX.Objects.SV.SVPostalCode (EntityType)

Label: "Postal Code"
BaseType: PX.Objects.SV.FSGeoZonePostalCode
Key: GeoZoneID, PostalCode (inherited from PX.Objects.SV.FSGeoZonePostalCode)
Entity sets: PX_Objects_SV_SVPostalCode, PostalCode1, SVPostalCode

# PX.Objects.SV.SVResource (EntityType)

Label: "Resource"
Key: ResourceClassID, ResourceNoteID
Entity sets: PX_Objects_SV_SVResource, Resource, SVResource

PX.Objects.SV.SVResource.ResourceNoteID : Edm.Guid [key]
PX.Objects.SV.SVResource.ResourceClassID : Edm.String [key] "Resource Class"
PX.Objects.SV.SVResource.IsActive : Edm.Boolean [required] "Active"
PX.Objects.SV.SVResource.tstamp : Edm.Binary
PX.Objects.SV.SVResource.CreatedByID : Edm.Guid "Created By"
PX.Objects.SV.SVResource.CreatedByScreenID : Edm.String
PX.Objects.SV.SVResource.CreatedDateTime : Edm.DateTimeOffset
PX.Objects.SV.SVResource.LastModifiedByID : Edm.Guid "Last Modified By"
PX.Objects.SV.SVResource.LastModifiedByScreenID : Edm.String
PX.Objects.SV.SVResource.LastModifiedDateTime : Edm.DateTimeOffset
PX.Objects.SV.SVResource.UsersByCreatedByID -> PX.SM.Users (CreatedByID=PKID)
PX.Objects.SV.SVResource.UsersByLastModifiedByID -> PX.SM.Users (LastModifiedByID=PKID)
PX.Objects.SV.SVResource.SVResourceClassByResourceClassID -> PX.Objects.SV.SVResourceClass (ResourceClassID=ResourceClassID)
PX.Objects.SV.SVResource.SVEventLaborCollection -> Collection(PX.Objects.SV.SVEventLabor)
PX.Objects.SV.SVResource.SVWorkTaskLaborCollection -> Collection(PX.Objects.SV.SVWorkTaskLabor)
PX.Objects.SV.SVResource.SVWorkTaskTemplateLaborCollection -> Collection(PX.Objects.SV.SVWorkTaskTemplateLabor)

# PX.Objects.SV.SVResourceClass (EntityType)

Label: "Resource Class"
Key: ResourceClassID
Entity sets: PX_Objects_SV_SVResourceClass, ResourceClass, SVResourceClass
Non-filterable, non-selectable: NoteText

PX.Objects.SV.SVResourceClass.ResourceClassID : Edm.String [key] "Class ID"
PX.Objects.SV.SVResourceClass.Name : Edm.String "Class Name"
PX.Objects.SV.SVResourceClass.NoteID : Edm.Guid
PX.Objects.SV.SVResourceClass.NoteText : Edm.String "Note Text"
PX.Objects.SV.SVResourceClass.tstamp : Edm.Binary
PX.Objects.SV.SVResourceClass.CreatedByID : Edm.Guid "Created By"
PX.Objects.SV.SVResourceClass.CreatedByScreenID : Edm.String
PX.Objects.SV.SVResourceClass.CreatedDateTime : Edm.DateTimeOffset
PX.Objects.SV.SVResourceClass.LastModifiedByID : Edm.Guid "Last Modified By"
PX.Objects.SV.SVResourceClass.LastModifiedByScreenID : Edm.String
PX.Objects.SV.SVResourceClass.LastModifiedDateTime : Edm.DateTimeOffset
PX.Objects.SV.SVResourceClass.UsersByCreatedByID -> PX.SM.Users (CreatedByID=PKID)
PX.Objects.SV.SVResourceClass.UsersByLastModifiedByID -> PX.SM.Users (LastModifiedByID=PKID)
PX.Objects.SV.SVResourceClass.SVResourceCollection -> Collection(PX.Objects.SV.SVResource)
PX.Objects.SV.SVResourceClass.SVResourceClassPropertyCollection -> Collection(PX.Objects.SV.SVResourceClassProperty)
PX.Objects.SV.SVResourceClass.SVResourcePropertyCollection -> Collection(PX.Objects.SV.SVResourceProperty)
PX.Objects.SV.SVResourceClass.SVResourcePropertyMappingCollection -> Collection(PX.Objects.SV.SVResourcePropertyMapping)

# PX.Objects.SV.SVResourceClassProperty (EntityType)

Label: "Resource Class Property"
Key: ClassPropertyID, ResourceClassID
Entity sets: PX_Objects_SV_SVResourceClassProperty, ResourceClassProperty, SVResourceClassProperty

PX.Objects.SV.SVResourceClassProperty.ResourceClassID : Edm.String [key]
PX.Objects.SV.SVResourceClassProperty.ClassPropertyID : Edm.String [key]
PX.Objects.SV.SVResourceClassProperty.Name : Edm.String "Property Name"
PX.Objects.SV.SVResourceClassProperty.IsInfo : Edm.Boolean [required]
PX.Objects.SV.SVResourceClassProperty.tstamp : Edm.Binary
PX.Objects.SV.SVResourceClassProperty.CreatedByID : Edm.Guid "Created By"
PX.Objects.SV.SVResourceClassProperty.CreatedByScreenID : Edm.String
PX.Objects.SV.SVResourceClassProperty.CreatedDateTime : Edm.DateTimeOffset
PX.Objects.SV.SVResourceClassProperty.LastModifiedByID : Edm.Guid "Last Modified By"
PX.Objects.SV.SVResourceClassProperty.LastModifiedByScreenID : Edm.String
PX.Objects.SV.SVResourceClassProperty.LastModifiedDateTime : Edm.DateTimeOffset
PX.Objects.SV.SVResourceClassProperty.UsersByCreatedByID -> PX.SM.Users (CreatedByID=PKID)
PX.Objects.SV.SVResourceClassProperty.UsersByLastModifiedByID -> PX.SM.Users (LastModifiedByID=PKID)
PX.Objects.SV.SVResourceClassProperty.SVResourceClassByResourceClassID -> PX.Objects.SV.SVResourceClass (ResourceClassID=ResourceClassID)

# PX.Objects.SV.SVResourceProperty (EntityType)

Label: "Resource Property"
Key: ClassPropertyID, PropertySourceID, ResourceNoteID, ResourceValue
Entity sets: PX_Objects_SV_SVResourceProperty, ResourceProperty, SVResourceProperty

PX.Objects.SV.SVResourceProperty.ResourceNoteID : Edm.Guid [key]
PX.Objects.SV.SVResourceProperty.PropertySourceID : Edm.Guid [key]
PX.Objects.SV.SVResourceProperty.ResourceValue : Edm.String [key required] "Value"
PX.Objects.SV.SVResourceProperty.ClassPropertyID : Edm.String [key] "Property ID"
PX.Objects.SV.SVResourceProperty.ResourceClassID : Edm.String "Resource Class"
PX.Objects.SV.SVResourceProperty.IssueDate : Edm.DateTimeOffset "Issue Date"
PX.Objects.SV.SVResourceProperty.ExpryDate : Edm.DateTimeOffset "Expiry Date"
PX.Objects.SV.SVResourceProperty.tstamp : Edm.Binary
PX.Objects.SV.SVResourceProperty.CreatedByID : Edm.Guid "Created By"
PX.Objects.SV.SVResourceProperty.CreatedByScreenID : Edm.String
PX.Objects.SV.SVResourceProperty.CreatedDateTime : Edm.DateTimeOffset
PX.Objects.SV.SVResourceProperty.LastModifiedByID : Edm.Guid "Last Modified By"
PX.Objects.SV.SVResourceProperty.LastModifiedByScreenID : Edm.String
PX.Objects.SV.SVResourceProperty.LastModifiedDateTime : Edm.DateTimeOffset
PX.Objects.SV.SVResourceProperty.UsersByCreatedByID -> PX.SM.Users (CreatedByID=PKID)
PX.Objects.SV.SVResourceProperty.UsersByLastModifiedByID -> PX.SM.Users (LastModifiedByID=PKID)
PX.Objects.SV.SVResourceProperty.SVResourceClassByResourceClassID -> PX.Objects.SV.SVResourceClass (ResourceClassID=ResourceClassID)

# PX.Objects.SV.SVResourcePropertyMapping (EntityType)

Label: "Resource Property Mapping"
Key: ClassPropertyID, ResourceClassID
Entity sets: PX_Objects_SV_SVResourcePropertyMapping, ResourcePropertyMapping, SVResourcePropertyMapping

PX.Objects.SV.SVResourcePropertyMapping.ResourceClassID : Edm.String [key] "Resource Class"
PX.Objects.SV.SVResourcePropertyMapping.ClassPropertyID : Edm.String [key] "Property ID"
PX.Objects.SV.SVResourcePropertyMapping.GraphType : Edm.String "Graph"
PX.Objects.SV.SVResourcePropertyMapping.SourceView : Edm.String "View"
PX.Objects.SV.SVResourcePropertyMapping.SourceTable : Edm.String "Table"
PX.Objects.SV.SVResourcePropertyMapping.SourceField : Edm.String "Field"
PX.Objects.SV.SVResourcePropertyMapping.IssueDateField : Edm.String "Issue Date Field"
PX.Objects.SV.SVResourcePropertyMapping.ExpryDateField : Edm.String "Expiry Date Field"
PX.Objects.SV.SVResourcePropertyMapping.tstamp : Edm.Binary
PX.Objects.SV.SVResourcePropertyMapping.CreatedByID : Edm.Guid "Created By"
PX.Objects.SV.SVResourcePropertyMapping.CreatedByScreenID : Edm.String
PX.Objects.SV.SVResourcePropertyMapping.CreatedDateTime : Edm.DateTimeOffset
PX.Objects.SV.SVResourcePropertyMapping.LastModifiedByID : Edm.Guid "Last Modified By"
PX.Objects.SV.SVResourcePropertyMapping.LastModifiedByScreenID : Edm.String
PX.Objects.SV.SVResourcePropertyMapping.LastModifiedDateTime : Edm.DateTimeOffset
PX.Objects.SV.SVResourcePropertyMapping.UsersByCreatedByID -> PX.SM.Users (CreatedByID=PKID)
PX.Objects.SV.SVResourcePropertyMapping.UsersByLastModifiedByID -> PX.SM.Users (LastModifiedByID=PKID)
PX.Objects.SV.SVResourcePropertyMapping.SVResourceClassByResourceClassID -> PX.Objects.SV.SVResourceClass (ResourceClassID=ResourceClassID)

# PX.Objects.SV.SVSchedulingSetup (EntityType)

Label: "Scheduling Preferences"
Singletons: PX_Objects_SV_SVSchedulingSetup, SchedulingPreferences, SVSchedulingSetup

PX.Objects.SV.SVSchedulingSetup.CalendarRefreshTime : Edm.Int32 "Refresh Calendar Every"
PX.Objects.SV.SVSchedulingSetup.CalendarID : Edm.String "Work Calendar"
PX.Objects.SV.SVSchedulingSetup.DefaultTimeslotDuration : Edm.Int32 "Default Duration"
PX.Objects.SV.SVSchedulingSetup.EventResizePrecision : Edm.Int32 "Resize Precision"
PX.Objects.SV.SVSchedulingSetup.EventAutoConfirmGap : Edm.Int32 "Auto-Confirm Time"
PX.Objects.SV.SVSchedulingSetup.EnableAutoConfirm : Edm.Boolean [required] "Auto-Confirm Time"
PX.Objects.SV.SVSchedulingSetup.DenyWarnByProperties : Edm.String "Validate Workforce Properties"
PX.Objects.SV.SVSchedulingSetup.AllowOverlappingEvents : Edm.Boolean "Allow Overlapping of Events"
PX.Objects.SV.SVSchedulingSetup.MapApiKey : Edm.String "Map API Key"
PX.Objects.SV.SVSchedulingSetup.GPSRefreshTrackingTime : Edm.Int32 "Refresh GPS Locations Every"
PX.Objects.SV.SVSchedulingSetup.EnableGPSTracking : Edm.Boolean "Show Location Tracking"
PX.Objects.SV.SVSchedulingSetup.WorkTaskStatus : Edm.String "Show Additional Statuses"
PX.Objects.SV.SVSchedulingSetup.tstamp : Edm.Binary
PX.Objects.SV.SVSchedulingSetup.CreatedByID : Edm.Guid "Created By"
PX.Objects.SV.SVSchedulingSetup.CreatedByScreenID : Edm.String
PX.Objects.SV.SVSchedulingSetup.CreatedDateTime : Edm.DateTimeOffset
PX.Objects.SV.SVSchedulingSetup.LastModifiedByID : Edm.Guid "Last Modified By"
PX.Objects.SV.SVSchedulingSetup.LastModifiedByScreenID : Edm.String
PX.Objects.SV.SVSchedulingSetup.LastModifiedDateTime : Edm.DateTimeOffset
PX.Objects.SV.SVSchedulingSetup.UsersByCreatedByID -> PX.SM.Users (CreatedByID=PKID)
PX.Objects.SV.SVSchedulingSetup.UsersByLastModifiedByID -> PX.SM.Users (LastModifiedByID=PKID)
PX.Objects.SV.SVSchedulingSetup.CSCalendarByCalendarID -> PX.Objects.CS.CSCalendar (CalendarID=CalendarID)

# PX.Objects.SV.SVServiceArea (EntityType)

Label: "Service Area"
BaseType: PX.Objects.SV.FSGeoZone
Key: GeoZoneCD (inherited from PX.Objects.SV.FSGeoZone)
Entity sets: PX_Objects_SV_SVServiceArea, ServiceArea2, SVServiceArea

# PX.Objects.SV.SVServiceLocation (EntityType)

Label: "Service Location"
Key: ServiceLocationID
Entity sets: PX_Objects_SV_SVServiceLocation, ServiceLocation, SVServiceLocation
Non-filterable, non-selectable: TaxRegistrationID, NoteText

PX.Objects.SV.SVServiceLocation.ServiceLocationID : Edm.String [key] "Service Location ID"
PX.Objects.SV.SVServiceLocation.Descr : Edm.String "Service Location Name"
PX.Objects.SV.SVServiceLocation.ServiceAreaID : Edm.Int32 "Service Area"
PX.Objects.SV.SVServiceLocation.IsActive : Edm.Boolean "Active"
PX.Objects.SV.SVServiceLocation.AddressID : Edm.Int32 "Address"
PX.Objects.SV.SVServiceLocation.TaxRegistrationID : Edm.String "Tax Registration ID"
PX.Objects.SV.SVServiceLocation.TaxZoneID : Edm.String "Tax Zone"
PX.Objects.SV.SVServiceLocation.TaxExemptionNumber : Edm.String "Tax Exemption Number"
PX.Objects.SV.SVServiceLocation.TaxExemptionType : Edm.String "Tax Exemption Type"
PX.Objects.SV.SVServiceLocation.IsTicketSignRequired : Edm.Boolean [required] "Require Signature on Work Summary Report"
PX.Objects.SV.SVServiceLocation.NoteID : Edm.Guid
PX.Objects.SV.SVServiceLocation.NoteText : Edm.String "Note Text"
PX.Objects.SV.SVServiceLocation.tstamp : Edm.Binary
PX.Objects.SV.SVServiceLocation.CreatedByID : Edm.Guid "Created By"
PX.Objects.SV.SVServiceLocation.CreatedByScreenID : Edm.String
PX.Objects.SV.SVServiceLocation.CreatedDateTime : Edm.DateTimeOffset
PX.Objects.SV.SVServiceLocation.LastModifiedByID : Edm.Guid "Last Modified By"
PX.Objects.SV.SVServiceLocation.LastModifiedByScreenID : Edm.String
PX.Objects.SV.SVServiceLocation.LastModifiedDateTime : Edm.DateTimeOffset
PX.Objects.SV.SVServiceLocation.FSGeoZoneByServiceAreaID -> PX.Objects.SV.FSGeoZone (ServiceAreaID=GeoZoneID)
PX.Objects.SV.SVServiceLocation.BranchByBranchID -> PX.Objects.GL.Branch
PX.Objects.SV.SVServiceLocation.UsersByCreatedByID -> PX.SM.Users (CreatedByID=PKID)
PX.Objects.SV.SVServiceLocation.UsersByLastModifiedByID -> PX.SM.Users (LastModifiedByID=PKID)
PX.Objects.SV.SVServiceLocation.TaxZoneByTaxZoneID -> PX.Objects.TX.TaxZone (TaxZoneID=TaxZoneID)
PX.Objects.SV.SVServiceLocation.SVAddressByAddressID -> PX.Objects.SV.SVAddress (AddressID=AddressID)
PX.Objects.SV.SVServiceLocation.SVInvoiceCollection -> Collection(PX.Objects.SV.SVInvoice)
PX.Objects.SV.SVServiceLocation.SVOrderCollection -> Collection(PX.Objects.SV.SVOrder)
PX.Objects.SV.SVServiceLocation.SVServiceLocationContactCollection -> Collection(PX.Objects.SV.SVServiceLocationContact)
PX.Objects.SV.SVServiceLocation.SVServiceLocationCustomerCollection -> Collection(PX.Objects.SV.SVServiceLocationCustomer)

# PX.Objects.SV.SVServiceLocationContact (EntityType)

Label: "Service Location Contact"
Key: ServiceLocationContactID
Entity sets: PX_Objects_SV_SVServiceLocationContact, ServiceLocationContact, SVServiceLocationContact

PX.Objects.SV.SVServiceLocationContact.ServiceLocationContactID : Edm.Int32 [key]
PX.Objects.SV.SVServiceLocationContact.ServiceLocationId : Edm.String
PX.Objects.SV.SVServiceLocationContact.ContactID : Edm.Int32 "Contact"
PX.Objects.SV.SVServiceLocationContact.IsPrimary : Edm.Boolean "Is Primary"
PX.Objects.SV.SVServiceLocationContact.tstamp : Edm.Binary
PX.Objects.SV.SVServiceLocationContact.CreatedByID : Edm.Guid "Created By"
PX.Objects.SV.SVServiceLocationContact.CreatedByScreenID : Edm.String
PX.Objects.SV.SVServiceLocationContact.CreatedDateTime : Edm.DateTimeOffset
PX.Objects.SV.SVServiceLocationContact.LastModifiedByID : Edm.Guid "Last Modified By"
PX.Objects.SV.SVServiceLocationContact.LastModifiedByScreenID : Edm.String
PX.Objects.SV.SVServiceLocationContact.LastModifiedDateTime : Edm.DateTimeOffset
PX.Objects.SV.SVServiceLocationContact.ContactByContactID -> PX.Objects.CR.Contact (ContactID=ContactID)
PX.Objects.SV.SVServiceLocationContact.UsersByCreatedByID -> PX.SM.Users (CreatedByID=PKID)
PX.Objects.SV.SVServiceLocationContact.UsersByLastModifiedByID -> PX.SM.Users (LastModifiedByID=PKID)
PX.Objects.SV.SVServiceLocationContact.SVServiceLocationByServiceLocationId -> PX.Objects.SV.SVServiceLocation (ServiceLocationId=ServiceLocationID)

# PX.Objects.SV.SVServiceLocationCustomer (EntityType)

Label: "Service Location Customer"
Key: ServiceLocationCustomerID
Entity sets: PX_Objects_SV_SVServiceLocationCustomer, ServiceLocationCustomer, SVServiceLocationCustomer

PX.Objects.SV.SVServiceLocationCustomer.ServiceLocationCustomerID : Edm.Int32 [key]
PX.Objects.SV.SVServiceLocationCustomer.ServiceLocationId : Edm.String
PX.Objects.SV.SVServiceLocationCustomer.CustomerID : Edm.Int32 "Customer"
PX.Objects.SV.SVServiceLocationCustomer.IsDefault : Edm.Boolean "Default"
PX.Objects.SV.SVServiceLocationCustomer.tstamp : Edm.Binary
PX.Objects.SV.SVServiceLocationCustomer.CreatedByID : Edm.Guid "Created By"
PX.Objects.SV.SVServiceLocationCustomer.CreatedByScreenID : Edm.String
PX.Objects.SV.SVServiceLocationCustomer.CreatedDateTime : Edm.DateTimeOffset
PX.Objects.SV.SVServiceLocationCustomer.LastModifiedByID : Edm.Guid "Last Modified By"
PX.Objects.SV.SVServiceLocationCustomer.LastModifiedByScreenID : Edm.String
PX.Objects.SV.SVServiceLocationCustomer.LastModifiedDateTime : Edm.DateTimeOffset
PX.Objects.SV.SVServiceLocationCustomer.BAccountByCustomerID -> PX.Objects.CR.BAccount (CustomerID=BAccountID)
PX.Objects.SV.SVServiceLocationCustomer.UsersByCreatedByID -> PX.SM.Users (CreatedByID=PKID)
PX.Objects.SV.SVServiceLocationCustomer.UsersByLastModifiedByID -> PX.SM.Users (LastModifiedByID=PKID)
PX.Objects.SV.SVServiceLocationCustomer.LocationByCustomerID -> PX.Objects.CR.Location (CustomerID=BAccountID)
PX.Objects.SV.SVServiceLocationCustomer.LocationByCustomerLocationID -> PX.Objects.CR.Location (CustomerID=BAccountID)
PX.Objects.SV.SVServiceLocationCustomer.SVServiceLocationByServiceLocationId -> PX.Objects.SV.SVServiceLocation (ServiceLocationId=ServiceLocationID)

# PX.Objects.SV.SVSetup (EntityType)

Label: "Work Order Preferences"
Singletons: PX_Objects_SV_SVSetup, WorkOrderPreferences, SVSetup

PX.Objects.SV.SVSetup.OrderNumberingID : Edm.String "Numbering Sequence"
PX.Objects.SV.SVSetup.InvoiceNumberingID : Edm.String "Numbering Sequence"
PX.Objects.SV.SVSetup.ServiceLocationNumberingID : Edm.String "Service Location Numbering Sequence"
PX.Objects.SV.SVSetup.WorkTaskNumberingID : Edm.String "Work Task Numbering Sequence"
PX.Objects.SV.SVSetup.LicenseNumberingID : Edm.String "License Numbering Sequence"
PX.Objects.SV.SVSetup.DefaultOrderType : Edm.String "Default Work Order Type"
PX.Objects.SV.SVSetup.InvoiceHoldEntry : Edm.Boolean [required] "Hold Invoices on Entry"
PX.Objects.SV.SVSetup.UpdateCostsForClosedOrders : Edm.Boolean [required] "Update Costs for Closed Orders"
PX.Objects.SV.SVSetup.AutomaticallyReleaseINDocuments : Edm.Boolean [required] "Automatically Release IN Documents"
PX.Objects.SV.SVSetup.OrderHoldEntry : Edm.Boolean [required] "Hold Orders on Entry"
PX.Objects.SV.SVSetup.CreditHoldEntry : Edm.Boolean [required] "Hold Document on Failed Credit Check"
PX.Objects.SV.SVSetup.DefaultBillingCategory : Edm.String "Default Billing Category"
PX.Objects.SV.SVSetup.DefaultPriceRule : Edm.String "Default Price Rule"
PX.Objects.SV.SVSetup.tstamp : Edm.Binary
PX.Objects.SV.SVSetup.CreatedByID : Edm.Guid "Created By"
PX.Objects.SV.SVSetup.CreatedByScreenID : Edm.String
PX.Objects.SV.SVSetup.CreatedDateTime : Edm.DateTimeOffset
PX.Objects.SV.SVSetup.LastModifiedByID : Edm.Guid "Last Modified By"
PX.Objects.SV.SVSetup.LastModifiedByScreenID : Edm.String
PX.Objects.SV.SVSetup.LastModifiedDateTime : Edm.DateTimeOffset
PX.Objects.SV.SVSetup.UsersByCreatedByID -> PX.SM.Users (CreatedByID=PKID)
PX.Objects.SV.SVSetup.UsersByLastModifiedByID -> PX.SM.Users (LastModifiedByID=PKID)
PX.Objects.SV.SVSetup.NumberingByOrderNumberingID -> PX.Objects.CS.Numbering (OrderNumberingID=NumberingID)
PX.Objects.SV.SVSetup.NumberingByInvoiceNumberingID -> PX.Objects.CS.Numbering (InvoiceNumberingID=NumberingID)
PX.Objects.SV.SVSetup.NumberingByServiceLocationNumberingID -> PX.Objects.CS.Numbering (ServiceLocationNumberingID=NumberingID)
PX.Objects.SV.SVSetup.NumberingByWorkTaskNumberingID -> PX.Objects.CS.Numbering (WorkTaskNumberingID=NumberingID)
PX.Objects.SV.SVSetup.NumberingByLicenseNumberingID -> PX.Objects.CS.Numbering (LicenseNumberingID=NumberingID)
PX.Objects.SV.SVSetup.SVOrderTypeByDefaultOrderType -> PX.Objects.SV.SVOrderType (DefaultOrderType=OrderType)

# PX.Objects.SV.SVSetupInvoiceApproval (EntityType)

Label: "Work Order Invoice Approval"
Key: ApprovalID
Entity sets: PX_Objects_SV_SVSetupInvoiceApproval, WorkOrderInvoiceApproval, SVSetupInvoiceApproval

PX.Objects.SV.SVSetupInvoiceApproval.DocType : Edm.String "Type"
PX.Objects.SV.SVSetupInvoiceApproval.IsActive : Edm.Boolean [required] "Active"
PX.Objects.SV.SVSetupInvoiceApproval.ApprovalID : Edm.Int32 [key]
PX.Objects.SV.SVSetupInvoiceApproval.AssignmentMapID : Edm.Int32 "Approval Map"
PX.Objects.SV.SVSetupInvoiceApproval.AssignmentNotificationID : Edm.Int32 "Pending Approval Notification"
PX.Objects.SV.SVSetupInvoiceApproval.tstamp : Edm.Binary
PX.Objects.SV.SVSetupInvoiceApproval.CreatedByID : Edm.Guid "Created By"
PX.Objects.SV.SVSetupInvoiceApproval.CreatedByScreenID : Edm.String
PX.Objects.SV.SVSetupInvoiceApproval.CreatedDateTime : Edm.DateTimeOffset
PX.Objects.SV.SVSetupInvoiceApproval.LastModifiedByID : Edm.Guid "Last Modified By"
PX.Objects.SV.SVSetupInvoiceApproval.LastModifiedByScreenID : Edm.String
PX.Objects.SV.SVSetupInvoiceApproval.LastModifiedDateTime : Edm.DateTimeOffset
PX.Objects.SV.SVSetupInvoiceApproval.UsersByCreatedByID -> PX.SM.Users (CreatedByID=PKID)
PX.Objects.SV.SVSetupInvoiceApproval.UsersByLastModifiedByID -> PX.SM.Users (LastModifiedByID=PKID)
PX.Objects.SV.SVSetupInvoiceApproval.NotificationByAssignmentNotificationID -> PX.SM.Notification (AssignmentNotificationID=NotificationID)
PX.Objects.SV.SVSetupInvoiceApproval.EPAssignmentMapByAssignmentMapID -> PX.Objects.EP.EPAssignmentMap (AssignmentMapID=AssignmentMapID)

# PX.Objects.SV.SVSiteStatusSelected (EntityType)

Key: InventoryID
Entity sets: PX_Objects_SV_SVSiteStatusSelected
Non-filterable, non-selectable: CuryID, CuryInfoID, CuryUnitPrice, QtySelected, CuryRate, CuryViewState

PX.Objects.SV.SVSiteStatusSelected.InventoryID : Edm.Int32 [key] "Inventory ID"
PX.Objects.SV.SVSiteStatusSelected.InventoryCD : Edm.String "Inventory ID"
PX.Objects.SV.SVSiteStatusSelected.Descr : Edm.String "Description"
PX.Objects.SV.SVSiteStatusSelected.ItemClassID : Edm.Int32 "Item Class ID"
PX.Objects.SV.SVSiteStatusSelected.ItemClassCD : Edm.String
PX.Objects.SV.SVSiteStatusSelected.ItemClassDescription : Edm.String "Item Class Description"
PX.Objects.SV.SVSiteStatusSelected.ItemType : Edm.String "Type"
PX.Objects.SV.SVSiteStatusSelected.PriceClassID : Edm.String "Price Class ID"
PX.Objects.SV.SVSiteStatusSelected.PriceClassDescription : Edm.String "Price Class Description"
PX.Objects.SV.SVSiteStatusSelected.CuryID : Edm.String "Currency"
PX.Objects.SV.SVSiteStatusSelected.CuryInfoID : Edm.Int64
PX.Objects.SV.SVSiteStatusSelected.SalesUnit : Edm.String "UOM"
PX.Objects.SV.SVSiteStatusSelected.BillingCategory : Edm.String "Billing Category"
PX.Objects.SV.SVSiteStatusSelected.PriceRule : Edm.String "Price Rule"
PX.Objects.SV.SVSiteStatusSelected.UnitPrice : Edm.Decimal
PX.Objects.SV.SVSiteStatusSelected.CuryUnitPrice : Edm.Decimal "Unit Price"
PX.Objects.SV.SVSiteStatusSelected.QtySelected : Edm.Decimal "Qty. Selected"
PX.Objects.SV.SVSiteStatusSelected.NoteID : Edm.Guid
PX.Objects.SV.SVSiteStatusSelected.CuryRate : Edm.Decimal
PX.Objects.SV.SVSiteStatusSelected.CuryViewState : Edm.Boolean
PX.Objects.SV.SVSiteStatusSelected.InventoryItemByInventoryID -> PX.Objects.IN.InventoryItem (InventoryID=InventoryID)
PX.Objects.SV.SVSiteStatusSelected.INItemClassByItemClassID -> PX.Objects.IN.INItemClass (ItemClassID=ItemClassID)
PX.Objects.SV.SVSiteStatusSelected.INPriceClassByPriceClassID -> PX.Objects.IN.INPriceClass (PriceClassID=PriceClassID)
PX.Objects.SV.SVSiteStatusSelected.CSAnswersByNoteID -> PX.Objects.CS.CSAnswers (NoteID=RefNoteID)
PX.Objects.SV.SVSiteStatusSelected.POFixedDemandCollection -> Collection(PX.Objects.PO.POFixedDemand)

# PX.Objects.SV.SVSkill (EntityType)

Label: "Skill"
BaseType: PX.Objects.SV.FSSkill
Key: SkillCD (inherited from PX.Objects.SV.FSSkill)
Entity sets: PX_Objects_SV_SVSkill, Skill2, SVSkill

# PX.Objects.SV.SVStagingWarehouse (EntityType)

Label: "Staging Warehouse"
Key: BranchID
Entity sets: PX_Objects_SV_SVStagingWarehouse, StagingWarehouse, SVStagingWarehouse
Non-filterable, non-selectable: BranchCuryID

PX.Objects.SV.SVStagingWarehouse.BranchID : Edm.Int32 [key] "Branch"
PX.Objects.SV.SVStagingWarehouse.BranchCuryID : Edm.String
PX.Objects.SV.SVStagingWarehouse.tstamp : Edm.Binary
PX.Objects.SV.SVStagingWarehouse.CreatedByID : Edm.Guid "Created By"
PX.Objects.SV.SVStagingWarehouse.CreatedByScreenID : Edm.String
PX.Objects.SV.SVStagingWarehouse.CreatedDateTime : Edm.DateTimeOffset
PX.Objects.SV.SVStagingWarehouse.LastModifiedByID : Edm.Guid "Last Modified By"
PX.Objects.SV.SVStagingWarehouse.LastModifiedByScreenID : Edm.String
PX.Objects.SV.SVStagingWarehouse.LastModifiedDateTime : Edm.DateTimeOffset
PX.Objects.SV.SVStagingWarehouse.BranchByBranchID -> PX.Objects.GL.Branch (BranchID=BranchID)
PX.Objects.SV.SVStagingWarehouse.UsersByCreatedByID -> PX.SM.Users (CreatedByID=PKID)
PX.Objects.SV.SVStagingWarehouse.UsersByLastModifiedByID -> PX.SM.Users (LastModifiedByID=PKID)
PX.Objects.SV.SVStagingWarehouse.INLocationByDefaultStagingSiteID -> PX.Objects.IN.INLocation
PX.Objects.SV.SVStagingWarehouse.INSiteByDefaultStagingSiteID -> PX.Objects.IN.INSite

# PX.Objects.SV.SVTax (EntityType)

Label: "Work Order Tax Detail"
Key: LineNbr, OrderNbr, TaxID
Entity sets: PX_Objects_SV_SVTax, WorkOrderTaxDetail, SVTax
Non-filterable, non-selectable: NonDeductibleTaxRate, ExpenseAmt

PX.Objects.SV.SVTax.TaxRate : Edm.Decimal [required] "Tax Rate"
PX.Objects.SV.SVTax.NonDeductibleTaxRate : Edm.Decimal "Deductible Tax Rate"
PX.Objects.SV.SVTax.ExpenseAmt : Edm.Decimal "Expense Amount"
PX.Objects.SV.SVTax.CuryExpenseAmt : Edm.Decimal "Expense Amount"
PX.Objects.SV.SVTax.CreatedByID : Edm.Guid "Created By"
PX.Objects.SV.SVTax.CreatedByScreenID : Edm.String
PX.Objects.SV.SVTax.CreatedDateTime : Edm.DateTimeOffset
PX.Objects.SV.SVTax.LastModifiedByID : Edm.Guid "Last Modified By"
PX.Objects.SV.SVTax.LastModifiedByScreenID : Edm.String
PX.Objects.SV.SVTax.LastModifiedDateTime : Edm.DateTimeOffset
PX.Objects.SV.SVTax.OrderNbr : Edm.String [key] "Order Nbr."
PX.Objects.SV.SVTax.LineNbr : Edm.Int32 [key] "Line Nbr."
PX.Objects.SV.SVTax.TaxID : Edm.String [key] "Tax ID"
PX.Objects.SV.SVTax.CuryInfoID : Edm.Int64
PX.Objects.SV.SVTax.CuryTaxableAmt : Edm.Decimal [required] "Taxable Amount"
PX.Objects.SV.SVTax.TaxableAmt : Edm.Decimal [required] "Taxable Amount"
PX.Objects.SV.SVTax.CuryTaxAmt : Edm.Decimal [required] "Tax Amount"
PX.Objects.SV.SVTax.TaxAmt : Edm.Decimal [required] "Tax Amount"
PX.Objects.SV.SVTax.TaxZoneID : Edm.String
PX.Objects.SV.SVTax.CurrencyInfoByCuryInfoID -> PX.Objects.CM.CurrencyInfo (CuryInfoID=CuryInfoID)
PX.Objects.SV.SVTax.UsersByCreatedByID -> PX.SM.Users (CreatedByID=PKID)
PX.Objects.SV.SVTax.UsersByLastModifiedByID -> PX.SM.Users (LastModifiedByID=PKID)
PX.Objects.SV.SVTax.TaxByTaxID -> PX.Objects.TX.Tax (TaxID=TaxID)
PX.Objects.SV.SVTax.TaxZoneByTaxZoneID -> PX.Objects.TX.TaxZone (TaxZoneID=TaxZoneID)
PX.Objects.SV.SVTax.INUnitByTaxUOM -> PX.Objects.IN.INUnit
PX.Objects.SV.SVTax.SVOrderByOrderNbr -> PX.Objects.SV.SVOrder (OrderNbr=OrderNbr)
PX.Objects.SV.SVTax.SVOrderDetailByLineNbr -> PX.Objects.SV.SVOrderDetail (OrderNbr=OrderNbr, LineNbr=LineNbr)
PX.Objects.SV.SVTax.SVTaxTranCollection -> Collection(PX.Objects.SV.SVTaxTran)

# PX.Objects.SV.SVTaxTran (EntityType)

Label: "Work Order Tax"
Key: LineNbr, OrderNbr, RecordID, TaxID
Entity sets: PX_Objects_SV_SVTaxTran, WorkOrderTax, SVTaxTran
Non-filterable, non-selectable: TaxRate, NonDeductibleTaxRate, ExpenseAmt, CuryExpenseAmt, TaxZoneID, IsTaxInclusive

PX.Objects.SV.SVTaxTran.TaxRate : Edm.Decimal [required] "Tax Rate"
PX.Objects.SV.SVTaxTran.NonDeductibleTaxRate : Edm.Decimal "Deductible Tax Rate"
PX.Objects.SV.SVTaxTran.ExpenseAmt : Edm.Decimal "Expense Amount"
PX.Objects.SV.SVTaxTran.CuryExpenseAmt : Edm.Decimal "Expense Amount"
PX.Objects.SV.SVTaxTran.CreatedByID : Edm.Guid "Created By"
PX.Objects.SV.SVTaxTran.CreatedByScreenID : Edm.String
PX.Objects.SV.SVTaxTran.CreatedDateTime : Edm.DateTimeOffset
PX.Objects.SV.SVTaxTran.LastModifiedByID : Edm.Guid "Last Modified By"
PX.Objects.SV.SVTaxTran.LastModifiedByScreenID : Edm.String
PX.Objects.SV.SVTaxTran.LastModifiedDateTime : Edm.DateTimeOffset
PX.Objects.SV.SVTaxTran.RecordID : Edm.Int32 [key]
PX.Objects.SV.SVTaxTran.OrderNbr : Edm.String [key] "Order Nbr."
PX.Objects.SV.SVTaxTran.LineNbr : Edm.Int32 [key required] "Line Nbr."
PX.Objects.SV.SVTaxTran.TaxID : Edm.String [key] "Tax ID"
PX.Objects.SV.SVTaxTran.JurisType : Edm.String "Tax Jurisdiction Type"
PX.Objects.SV.SVTaxTran.JurisName : Edm.String "Tax Jurisdiction Name"
PX.Objects.SV.SVTaxTran.CuryInfoID : Edm.Int64
PX.Objects.SV.SVTaxTran.CuryTaxableAmt : Edm.Decimal [required] "Taxable Amount"
PX.Objects.SV.SVTaxTran.TaxableAmt : Edm.Decimal [required] "Taxable Amount"
PX.Objects.SV.SVTaxTran.CuryTaxAmt : Edm.Decimal [required] "Tax Amount"
PX.Objects.SV.SVTaxTran.TaxAmt : Edm.Decimal [required] "Tax Amount"
PX.Objects.SV.SVTaxTran.TaxZoneID : Edm.String
PX.Objects.SV.SVTaxTran.IsTaxInclusive : Edm.Boolean
PX.Objects.SV.SVTaxTran.SVTaxByTaxID -> PX.Objects.SV.SVTax (OrderNbr=OrderNbr, LineNbr=LineNbr, TaxID=TaxID)
PX.Objects.SV.SVTaxTran.CurrencyInfoByCuryInfoID -> PX.Objects.CM.CurrencyInfo (CuryInfoID=CuryInfoID)
PX.Objects.SV.SVTaxTran.UsersByCreatedByID -> PX.SM.Users (CreatedByID=PKID)
PX.Objects.SV.SVTaxTran.UsersByLastModifiedByID -> PX.SM.Users (LastModifiedByID=PKID)
PX.Objects.SV.SVTaxTran.TaxByTaxID -> PX.Objects.TX.Tax (TaxID=TaxID)
PX.Objects.SV.SVTaxTran.INUnitByTaxUOM -> PX.Objects.IN.INUnit
PX.Objects.SV.SVTaxTran.SVOrderByOrderNbr -> PX.Objects.SV.SVOrder (OrderNbr=OrderNbr)
PX.Objects.SV.SVTaxTran.SVOrderDetailByLineNbr -> PX.Objects.SV.SVOrderDetail (OrderNbr=OrderNbr, LineNbr=LineNbr)

# PX.Objects.SV.SVTicket (EntityType)

Label: "Work Ticket"
Key: TicketNbr
Entity sets: PX_Objects_SV_SVTicket, WorkTicket, SVTicket
Non-filterable, non-selectable: NoteText, BranchID, CuryRate, CuryViewState

PX.Objects.SV.SVTicket.TicketNbr : Edm.String [key] "Work Ticket"
PX.Objects.SV.SVTicket.RefNoteIDType : Edm.String "Ref. Doc. Type"
PX.Objects.SV.SVTicket.RefNoteID : Edm.Guid "Work Order"
PX.Objects.SV.SVTicket.Status : Edm.String "Status"
PX.Objects.SV.SVTicket.DocDate : Edm.DateTimeOffset "Date"
PX.Objects.SV.SVTicket.MaterialLineCntr : Edm.Int32 [required]
PX.Objects.SV.SVTicket.Summary : Edm.String "Summary"
PX.Objects.SV.SVTicket.Descr : Edm.String "Resolution"
PX.Objects.SV.SVTicket.CuryID : Edm.String "Currency"
PX.Objects.SV.SVTicket.CuryInfoID : Edm.Int64
PX.Objects.SV.SVTicket.EventNoteID : Edm.Guid "Work Event"
PX.Objects.SV.SVTicket.NoteID : Edm.Guid
PX.Objects.SV.SVTicket.NoteText : Edm.String "Note Text"
PX.Objects.SV.SVTicket.IsOpen : Edm.Boolean [required] "Open"
PX.Objects.SV.SVTicket.Completing : Edm.Boolean [required] "Completing"
PX.Objects.SV.SVTicket.Completed : Edm.Boolean [required] "Completed"
PX.Objects.SV.SVTicket.Canceled : Edm.Boolean [required] "Canceled"
PX.Objects.SV.SVTicket.BranchID : Edm.Int32
PX.Objects.SV.SVTicket.CustomerSigned : Edm.Boolean [required] "Signed by Customer"
PX.Objects.SV.SVTicket.SignedReportID : Edm.Guid "Signed Report ID"
PX.Objects.SV.SVTicket.tstamp : Edm.Binary
PX.Objects.SV.SVTicket.CreatedByID : Edm.Guid "Created By"
PX.Objects.SV.SVTicket.CreatedByScreenID : Edm.String
PX.Objects.SV.SVTicket.CreatedDateTime : Edm.DateTimeOffset
PX.Objects.SV.SVTicket.LastModifiedByID : Edm.Guid "Last Modified By"
PX.Objects.SV.SVTicket.LastModifiedByScreenID : Edm.String
PX.Objects.SV.SVTicket.LastModifiedDateTime : Edm.DateTimeOffset
PX.Objects.SV.SVTicket.CuryRate : Edm.Decimal
PX.Objects.SV.SVTicket.CuryViewState : Edm.Boolean
PX.Objects.SV.SVTicket.UsersByCreatedByID -> PX.SM.Users (CreatedByID=PKID)
PX.Objects.SV.SVTicket.UsersByLastModifiedByID -> PX.SM.Users (LastModifiedByID=PKID)
PX.Objects.SV.SVTicket.CurrencyByCuryID -> PX.Objects.CM.Currency (CuryID=CuryID)
PX.Objects.SV.SVTicket.SVEventByEventNoteID -> PX.Objects.SV.SVEvent (EventNoteID=NoteID)
PX.Objects.SV.SVTicket.SVTicketDetailCollection -> Collection(PX.Objects.SV.SVTicketDetail)
PX.Objects.SV.SVTicket.SVOrderActualCollection -> Collection(PX.Objects.SV.SVOrderActual)
PX.Objects.SV.SVTicket.SVWorkHistoryItemCollection -> Collection(PX.Objects.SV.DACUnbound.SVWorkHistoryItem)

# PX.Objects.SV.SVTicketDetail (EntityType)

Label: "Work Ticket Detail"
Key: NoteID, TicketNbr
Entity sets: PX_Objects_SV_SVTicketDetail, WorkTicketDetail, SVTicketDetail
Non-filterable, non-selectable: EmployeeName, IsCorrectionLocked, NoteText, CuryID, CuryRate, CuryViewState

PX.Objects.SV.SVTicketDetail.RefNoteID : Edm.Guid
PX.Objects.SV.SVTicketDetail.TicketNbr : Edm.String [key] "Work Ticket Nbr."
PX.Objects.SV.SVTicketDetail.ItemType : Edm.String "Item Type"
PX.Objects.SV.SVTicketDetail.InventoryID : Edm.Int32 "Inventory ID"
PX.Objects.SV.SVTicketDetail.TranDesc : Edm.String "Description"
PX.Objects.SV.SVTicketDetail.UOM : Edm.String "UOM"
PX.Objects.SV.SVTicketDetail.CuryInfoID : Edm.Int64
PX.Objects.SV.SVTicketDetail.ActualQty : Edm.Decimal "Actual Quantity"
PX.Objects.SV.SVTicketDetail.BaseActualQty : Edm.Decimal
PX.Objects.SV.SVTicketDetail.EmployeeID : Edm.Int32 "Employee ID"
PX.Objects.SV.SVTicketDetail.EmployeeName : Edm.String "Employee Name"
PX.Objects.SV.SVTicketDetail.CorrectionLockReason : Edm.String
PX.Objects.SV.SVTicketDetail.IsCorrectionLocked : Edm.Boolean
PX.Objects.SV.SVTicketDetail.NoteID : Edm.Guid [key]
PX.Objects.SV.SVTicketDetail.NoteText : Edm.String "Note Text"
PX.Objects.SV.SVTicketDetail.tstamp : Edm.Binary
PX.Objects.SV.SVTicketDetail.CreatedByID : Edm.Guid "Created By"
PX.Objects.SV.SVTicketDetail.CreatedByScreenID : Edm.String
PX.Objects.SV.SVTicketDetail.CreatedDateTime : Edm.DateTimeOffset
PX.Objects.SV.SVTicketDetail.LastModifiedByID : Edm.Guid "Last Modified By"
PX.Objects.SV.SVTicketDetail.LastModifiedByScreenID : Edm.String
PX.Objects.SV.SVTicketDetail.LastModifiedDateTime : Edm.DateTimeOffset
PX.Objects.SV.SVTicketDetail.CuryID : Edm.String "Currency"
PX.Objects.SV.SVTicketDetail.CuryRate : Edm.Decimal
PX.Objects.SV.SVTicketDetail.CuryViewState : Edm.Boolean
PX.Objects.SV.SVTicketDetail.EPEmployeeByEmployeeID -> PX.Objects.EP.EPEmployee (EmployeeID=BAccountID)
PX.Objects.SV.SVTicketDetail.VendorByEmployeeID -> PX.Objects.AP.Vendor (EmployeeID=BAccountID)
PX.Objects.SV.SVTicketDetail.InventoryItemByInventoryID -> PX.Objects.IN.InventoryItem (InventoryID=InventoryID)
PX.Objects.SV.SVTicketDetail.SVTicketByTicketNbr -> PX.Objects.SV.SVTicket (TicketNbr=TicketNbr)
PX.Objects.SV.SVTicketDetail.UsersByCreatedByID -> PX.SM.Users (CreatedByID=PKID)
PX.Objects.SV.SVTicketDetail.UsersByLastModifiedByID -> PX.SM.Users (LastModifiedByID=PKID)
PX.Objects.SV.SVTicketDetail.INSiteBySiteID -> PX.Objects.IN.INSite
PX.Objects.SV.SVTicketDetail.INUnitByInventoryID -> PX.Objects.IN.INUnit (UOM=FromUnit, InventoryID=InventoryID)

# PX.Objects.SV.SVTicketEmployeeGroup (ComplexType)


PX.Objects.SV.SVTicketEmployeeGroup.TicketNbr : Edm.String
PX.Objects.SV.SVTicketEmployeeGroup.EmployeeID : Edm.Int32

# PX.Objects.SV.SVTicketLabor (EntityType)

Label: "Ticket Labor Employee"
Key: EmployeeID, TicketNbr
Entity sets: PX_Objects_SV_SVTicketLabor, TicketLaborEmployee, SVTicketLabor

PX.Objects.SV.SVTicketLabor.TicketNbr : Edm.String [key] "Work Ticket Nbr."
PX.Objects.SV.SVTicketLabor.EmployeeID : Edm.Int32 [key]
PX.Objects.SV.SVTicketLabor.SVTicketDetailCollection -> Collection(PX.Objects.SV.SVTicketDetail)
PX.Objects.SV.SVTicketLabor.SVOrderActualCollection -> Collection(PX.Objects.SV.SVOrderActual)
PX.Objects.SV.SVTicketLabor.SVWorkHistoryItemCollection -> Collection(PX.Objects.SV.DACUnbound.SVWorkHistoryItem)

# PX.Objects.SV.SVVendorLicense (EntityType)

Label: "Vendor License"
Key: LicenseID
Entity sets: PX_Objects_SV_SVVendorLicense, VendorLicense, SVVendorLicense

PX.Objects.SV.SVVendorLicense.LicenseID : Edm.Int32 [key]
PX.Objects.SV.SVVendorLicense.RefNbr : Edm.String "License Nbr."
PX.Objects.SV.SVVendorLicense.Descr : Edm.String "Description"
PX.Objects.SV.SVVendorLicense.ExternalLicenseNbr : Edm.String "External License Nbr."
PX.Objects.SV.SVVendorLicense.EmployeeID : Edm.Int32 "Vendor ID"
PX.Objects.SV.SVVendorLicense.ExpirationDate : Edm.DateTimeOffset "Expiration Date"
PX.Objects.SV.SVVendorLicense.IssueDate : Edm.DateTimeOffset "Issue Date"
PX.Objects.SV.SVVendorLicense.LicenseTypeID : Edm.Int32 "License Type"
PX.Objects.SV.SVVendorLicense.NeverExpires : Edm.Boolean "Never Expires"
PX.Objects.SV.SVVendorLicense.NoteID : Edm.Guid
PX.Objects.SV.SVVendorLicense.CreatedByID : Edm.Guid "Created By"
PX.Objects.SV.SVVendorLicense.CreatedByScreenID : Edm.String
PX.Objects.SV.SVVendorLicense.CreatedDateTime : Edm.DateTimeOffset
PX.Objects.SV.SVVendorLicense.LastModifiedByID : Edm.Guid "Last Modified By"
PX.Objects.SV.SVVendorLicense.LastModifiedByScreenID : Edm.String
PX.Objects.SV.SVVendorLicense.LastModifiedDateTime : Edm.DateTimeOffset
PX.Objects.SV.SVVendorLicense.tstamp : Edm.Binary
PX.Objects.SV.SVVendorLicense.VendorByEmployeeID -> PX.Objects.AP.Vendor (EmployeeID=BAccountID)
PX.Objects.SV.SVVendorLicense.FSLicenseTypeByLicenseTypeID -> PX.Objects.SV.FSLicenseType (LicenseTypeID=LicenseTypeID)

# PX.Objects.SV.SVVendorServiceArea (EntityType)

Label: "Vendor Service Area"
Key: EmployeeID, GeoZoneID
Entity sets: PX_Objects_SV_SVVendorServiceArea, VendorServiceArea, SVVendorServiceArea
Non-filterable, non-selectable: NoteText

PX.Objects.SV.SVVendorServiceArea.NoteID : Edm.Guid
PX.Objects.SV.SVVendorServiceArea.NoteText : Edm.String "Note Text"
PX.Objects.SV.SVVendorServiceArea.EmployeeID : Edm.Int32 [key] "Vendor ID"
PX.Objects.SV.SVVendorServiceArea.GeoZoneID : Edm.Int32 [key] "Service Area ID"
PX.Objects.SV.SVVendorServiceArea.CreatedByID : Edm.Guid "Created By"
PX.Objects.SV.SVVendorServiceArea.CreatedByScreenID : Edm.String "Created By Screen ID"
PX.Objects.SV.SVVendorServiceArea.CreatedDateTime : Edm.DateTimeOffset "Created On"
PX.Objects.SV.SVVendorServiceArea.LastModifiedByID : Edm.Guid "Last Modified By"
PX.Objects.SV.SVVendorServiceArea.LastModifiedByScreenID : Edm.String "Last Modified By Screen ID"
PX.Objects.SV.SVVendorServiceArea.LastModifiedDateTime : Edm.DateTimeOffset "Last Modified On"
PX.Objects.SV.SVVendorServiceArea.tstamp : Edm.Binary

# PX.Objects.SV.SVVendorSkill (EntityType)

Label: "Vendor Skill"
Key: EmployeeID, SkillID
Entity sets: PX_Objects_SV_SVVendorSkill, VendorSkill, SVVendorSkill

PX.Objects.SV.SVVendorSkill.EmployeeID : Edm.Int32 [key] "Vendor ID"
PX.Objects.SV.SVVendorSkill.SkillID : Edm.Int32 [key] "Skill ID"
PX.Objects.SV.SVVendorSkill.NoteID : Edm.Guid
PX.Objects.SV.SVVendorSkill.CreatedByID : Edm.Guid "Created By"
PX.Objects.SV.SVVendorSkill.CreatedByScreenID : Edm.String
PX.Objects.SV.SVVendorSkill.CreatedDateTime : Edm.DateTimeOffset
PX.Objects.SV.SVVendorSkill.LastModifiedByID : Edm.Guid "Last Modified By"
PX.Objects.SV.SVVendorSkill.LastModifiedByScreenID : Edm.String
PX.Objects.SV.SVVendorSkill.LastModifiedDateTime : Edm.DateTimeOffset
PX.Objects.SV.SVVendorSkill.tstamp : Edm.Binary
PX.Objects.SV.SVVendorSkill.VendorByEmployeeID -> PX.Objects.AP.Vendor (EmployeeID=BAccountID)
PX.Objects.SV.SVVendorSkill.FSSkillBySkillID -> PX.Objects.SV.FSSkill (SkillID=SkillID)

# PX.Objects.SV.SVWorkDetailsTicket (EntityType)

Label: "Work Details"
BaseType: PX.Objects.SV.SVTicket
Key: TicketNbr (inherited from PX.Objects.SV.SVTicket)
Entity sets: PX_Objects_SV_SVWorkDetailsTicket, WorkDetails, SVWorkDetailsTicket

# PX.Objects.SV.SVWorkforceResource (EntityType)

Label: "Workforce Resource"
BaseType: PX.Objects.SV.SVResource
Key: ResourceClassID, ResourceNoteID (inherited from PX.Objects.SV.SVResource)
Entity sets: PX_Objects_SV_SVWorkforceResource, WorkforceResource, SVWorkforceResource

PX.Objects.SV.SVWorkforceResource.Name : Edm.String "Name"
PX.Objects.SV.SVWorkforceResource.Position : Edm.String "Position"
PX.Objects.SV.SVWorkforceResource.PositionDescription : Edm.String "Position"
PX.Objects.SV.SVWorkforceResource.Phone1 : Edm.String "Phone 1"
PX.Objects.SV.SVWorkforceResource.Phone2 : Edm.String "Phone 2"
PX.Objects.SV.SVWorkforceResource.Department : Edm.String "Department"
PX.Objects.SV.SVWorkforceResource.Address : Edm.String "Address"
PX.Objects.SV.SVWorkforceResource.Subcontractor : Edm.String "Subcontractor"

# PX.Objects.SV.SVWorkTask (EntityType)

Label: "Work Task"
Key: TaskID
Entity sets: PX_Objects_SV_SVWorkTask, WorkTask, SVWorkTask
Non-filterable, non-selectable: NoteText, SourceEventNoteID

PX.Objects.SV.SVWorkTask.TaskID : Edm.String [key] "Task ID"
PX.Objects.SV.SVWorkTask.TaskTemplateID : Edm.String "Task Template ID"
PX.Objects.SV.SVWorkTask.Description : Edm.String "Description"
PX.Objects.SV.SVWorkTask.Summary : Edm.String "Summary"
PX.Objects.SV.SVWorkTask.TaskType : Edm.String "Task Type"
PX.Objects.SV.SVWorkTask.Status : Edm.String "Status"
PX.Objects.SV.SVWorkTask.Priority : Edm.String "Priority"
PX.Objects.SV.SVWorkTask.Severity : Edm.String "Severity"
PX.Objects.SV.SVWorkTask.RefNoteIDType : Edm.String "Related Document Type"
PX.Objects.SV.SVWorkTask.RefNoteID : Edm.Guid "Related Document Nbr."
PX.Objects.SV.SVWorkTask.StartDate : Edm.DateTimeOffset "Planned Start Date"
PX.Objects.SV.SVWorkTask.EndDate : Edm.DateTimeOffset "Due Date"
PX.Objects.SV.SVWorkTask.CompletedDate : Edm.DateTimeOffset "Completed On"
PX.Objects.SV.SVWorkTask.EstimatedDuration : Edm.Int32 "Estimated Duration"
PX.Objects.SV.SVWorkTask.PercentCompletion : Edm.Int32 "Completion (%)"
PX.Objects.SV.SVWorkTask.SchedulableItem : Edm.Boolean [required] "Schedulable"
PX.Objects.SV.SVWorkTask.ActionLineCntr : Edm.Int32 [required]
PX.Objects.SV.SVWorkTask.LaborLineCntr : Edm.Int32 [required]
PX.Objects.SV.SVWorkTask.ResourcePropertyLineCntr : Edm.Int32 [required]
PX.Objects.SV.SVWorkTask.NoteID : Edm.Guid
PX.Objects.SV.SVWorkTask.NoteText : Edm.String "Note Text"
PX.Objects.SV.SVWorkTask.IsScheduled : Edm.Boolean "Scheduled"
PX.Objects.SV.SVWorkTask.SourceEventNoteID : Edm.Guid
PX.Objects.SV.SVWorkTask.tstamp : Edm.Binary
PX.Objects.SV.SVWorkTask.CreatedByID : Edm.Guid "Created By"
PX.Objects.SV.SVWorkTask.CreatedByScreenID : Edm.String
PX.Objects.SV.SVWorkTask.CreatedDateTime : Edm.DateTimeOffset
PX.Objects.SV.SVWorkTask.LastModifiedByID : Edm.Guid "Last Modified By"
PX.Objects.SV.SVWorkTask.LastModifiedByScreenID : Edm.String
PX.Objects.SV.SVWorkTask.LastModifiedDateTime : Edm.DateTimeOffset
PX.Objects.SV.SVWorkTask.UsersByCreatedByID -> PX.SM.Users (CreatedByID=PKID)
PX.Objects.SV.SVWorkTask.UsersByLastModifiedByID -> PX.SM.Users (LastModifiedByID=PKID)
PX.Objects.SV.SVWorkTask.SVWorkTaskTemplateByTaskTemplateID -> PX.Objects.SV.SVWorkTaskTemplate (TaskTemplateID=TaskTemplateID)
PX.Objects.SV.SVWorkTask.SVWorkTaskLaborCollection -> Collection(PX.Objects.SV.SVWorkTaskLabor)
PX.Objects.SV.SVWorkTask.SVEventTaskCollection -> Collection(PX.Objects.SV.SVEventTask)
PX.Objects.SV.SVWorkTask.SVWorkTaskActionCollection -> Collection(PX.Objects.SV.SVWorkTaskAction)
PX.Objects.SV.SVWorkTask.SVWorkTaskResourcePropertyCollection -> Collection(PX.Objects.SV.SVWorkTaskResourceProperty)
PX.Objects.SV.SVWorkTask.SVOrderTaskCollection -> Collection(PX.Objects.SV.SVOrderTask)

# PX.Objects.SV.SVWorkTaskAction (EntityType)

Label: "Work Task Action"
Key: LineNbr, ParentNoteID
Entity sets: PX_Objects_SV_SVWorkTaskAction, WorkTaskAction, SVWorkTaskAction

PX.Objects.SV.SVWorkTaskAction.ParentNoteID : Edm.Guid [key]
PX.Objects.SV.SVWorkTaskAction.LineNbr : Edm.Int32 [key]
PX.Objects.SV.SVWorkTaskAction.Completed : Edm.Boolean "Completed"
PX.Objects.SV.SVWorkTaskAction.Description : Edm.String "Action Description"
PX.Objects.SV.SVWorkTaskAction.Comment : Edm.String "Comment"
PX.Objects.SV.SVWorkTaskAction.SortOrder : Edm.Int32
PX.Objects.SV.SVWorkTaskAction.CompletedOn : Edm.DateTimeOffset "Completed On"
PX.Objects.SV.SVWorkTaskAction.tstamp : Edm.Binary
PX.Objects.SV.SVWorkTaskAction.CreatedByID : Edm.Guid "Created By"
PX.Objects.SV.SVWorkTaskAction.CreatedByScreenID : Edm.String
PX.Objects.SV.SVWorkTaskAction.CreatedDateTime : Edm.DateTimeOffset
PX.Objects.SV.SVWorkTaskAction.LastModifiedByID : Edm.Guid "Last Modified By"
PX.Objects.SV.SVWorkTaskAction.LastModifiedByScreenID : Edm.String
PX.Objects.SV.SVWorkTaskAction.LastModifiedDateTime : Edm.DateTimeOffset
PX.Objects.SV.SVWorkTaskAction.UsersByCreatedByID -> PX.SM.Users (CreatedByID=PKID)
PX.Objects.SV.SVWorkTaskAction.UsersByLastModifiedByID -> PX.SM.Users (LastModifiedByID=PKID)
PX.Objects.SV.SVWorkTaskAction.SVWorkTaskByParentNoteID -> PX.Objects.SV.SVWorkTask (ParentNoteID=NoteID)

# PX.Objects.SV.SVWorkTaskEvent (EntityType)

Label: "Work Task Event"
BaseType: PX.Objects.SV.SVEvent
Key: NoteID (inherited from PX.Objects.SV.SVEvent)
Entity sets: PX_Objects_SV_SVWorkTaskEvent, WorkTaskEvent, SVWorkTaskEvent
Non-filterable, non-selectable: BandColor

PX.Objects.SV.SVWorkTaskEvent.WorkforceList : Edm.String "Workforce"
PX.Objects.SV.SVWorkTaskEvent.BandColor : Edm.String

# PX.Objects.SV.SVWorkTaskLabor (EntityType)

Label: "Work Task Workforce"
Key: LineNbr, TaskID
Entity sets: PX_Objects_SV_SVWorkTaskLabor, WorkTaskWorkforce1, SVWorkTaskLabor
Non-filterable, non-selectable: DatafeedRemoveEnabled, NoteText

PX.Objects.SV.SVWorkTaskLabor.TaskID : Edm.String [key] "Work Task"
PX.Objects.SV.SVWorkTaskLabor.LineNbr : Edm.Int32 [key] "Line Nbr."
PX.Objects.SV.SVWorkTaskLabor.ResourceNoteID : Edm.Guid "Resources"
PX.Objects.SV.SVWorkTaskLabor.Name : Edm.String "Name"
PX.Objects.SV.SVWorkTaskLabor.Position : Edm.String "Position"
PX.Objects.SV.SVWorkTaskLabor.PositionDescription : Edm.String "Position"
PX.Objects.SV.SVWorkTaskLabor.Phone1 : Edm.String "Phone 1"
PX.Objects.SV.SVWorkTaskLabor.Phone2 : Edm.String "Phone 2"
PX.Objects.SV.SVWorkTaskLabor.SkillID : Edm.String "Skill ID"
PX.Objects.SV.SVWorkTaskLabor.SkillDescription : Edm.String "Skill Description"
PX.Objects.SV.SVWorkTaskLabor.Subcontractor : Edm.String "Subcontractor"
PX.Objects.SV.SVWorkTaskLabor.DatafeedRemoveEnabled : Edm.Boolean
PX.Objects.SV.SVWorkTaskLabor.NoteID : Edm.Guid
PX.Objects.SV.SVWorkTaskLabor.NoteText : Edm.String "Note Text"
PX.Objects.SV.SVWorkTaskLabor.tstamp : Edm.Binary
PX.Objects.SV.SVWorkTaskLabor.CreatedByID : Edm.Guid "Created By"
PX.Objects.SV.SVWorkTaskLabor.CreatedByScreenID : Edm.String
PX.Objects.SV.SVWorkTaskLabor.CreatedDateTime : Edm.DateTimeOffset
PX.Objects.SV.SVWorkTaskLabor.LastModifiedByID : Edm.Guid "Last Modified By"
PX.Objects.SV.SVWorkTaskLabor.LastModifiedByScreenID : Edm.String
PX.Objects.SV.SVWorkTaskLabor.LastModifiedDateTime : Edm.DateTimeOffset "Last Modified"
PX.Objects.SV.SVWorkTaskLabor.FSSkillBySkillID -> PX.Objects.SV.FSSkill (SkillID=SkillID)
PX.Objects.SV.SVWorkTaskLabor.UsersByCreatedByID -> PX.SM.Users (CreatedByID=PKID)
PX.Objects.SV.SVWorkTaskLabor.UsersByLastModifiedByID -> PX.SM.Users (LastModifiedByID=PKID)
PX.Objects.SV.SVWorkTaskLabor.EPPositionByPosition -> PX.Objects.EP.EPPosition (Position=PositionID)
PX.Objects.SV.SVWorkTaskLabor.SVResourceByResourceNoteID -> PX.Objects.SV.SVResource (ResourceNoteID=ResourceNoteID)
PX.Objects.SV.SVWorkTaskLabor.SVWorkTaskByTaskID -> PX.Objects.SV.SVWorkTask (TaskID=TaskID)

# PX.Objects.SV.SVWorkTaskResourceProperty (EntityType)

Label: "Work Task Template Workforce"
Key: LineNbr, TaskID
Entity sets: PX_Objects_SV_SVWorkTaskResourceProperty, WorkTaskTemplateWorkforce, SVWorkTaskResourceProperty
Non-filterable, non-selectable: ResourceClassPropertyName, DatafeedRemoveEnabled

PX.Objects.SV.SVWorkTaskResourceProperty.TaskID : Edm.String [key] "Work Task"
PX.Objects.SV.SVWorkTaskResourceProperty.LineNbr : Edm.Int32 [key] "Line Nbr."
PX.Objects.SV.SVWorkTaskResourceProperty.ResourceClassID : Edm.String "Resource Class"
PX.Objects.SV.SVWorkTaskResourceProperty.ClassPropertyID : Edm.String "Property ID"
PX.Objects.SV.SVWorkTaskResourceProperty.PropertyValue : Edm.String "Property Value"
PX.Objects.SV.SVWorkTaskResourceProperty.Description : Edm.String "Description"
PX.Objects.SV.SVWorkTaskResourceProperty.ResourceClassPropertyName : Edm.String "Resource Class Property Name"
PX.Objects.SV.SVWorkTaskResourceProperty.DatafeedRemoveEnabled : Edm.Boolean
PX.Objects.SV.SVWorkTaskResourceProperty.tstamp : Edm.Binary
PX.Objects.SV.SVWorkTaskResourceProperty.CreatedByID : Edm.Guid "Created By"
PX.Objects.SV.SVWorkTaskResourceProperty.CreatedByScreenID : Edm.String
PX.Objects.SV.SVWorkTaskResourceProperty.CreatedDateTime : Edm.DateTimeOffset
PX.Objects.SV.SVWorkTaskResourceProperty.LastModifiedByID : Edm.Guid "Last Modified By"
PX.Objects.SV.SVWorkTaskResourceProperty.LastModifiedByScreenID : Edm.String
PX.Objects.SV.SVWorkTaskResourceProperty.LastModifiedDateTime : Edm.DateTimeOffset "Last Modified"
PX.Objects.SV.SVWorkTaskResourceProperty.UsersByCreatedByID -> PX.SM.Users (CreatedByID=PKID)
PX.Objects.SV.SVWorkTaskResourceProperty.UsersByLastModifiedByID -> PX.SM.Users (LastModifiedByID=PKID)
PX.Objects.SV.SVWorkTaskResourceProperty.SVWorkTaskByTaskID -> PX.Objects.SV.SVWorkTask (TaskID=TaskID)

# PX.Objects.SV.SVWorkTaskTemplate (EntityType)

Label: "Work Task Template"
Key: TaskTemplateID
Entity sets: PX_Objects_SV_SVWorkTaskTemplate, WorkTaskTemplate, SVWorkTaskTemplate

PX.Objects.SV.SVWorkTaskTemplate.TaskTemplateID : Edm.String [key] "Task Template ID"
PX.Objects.SV.SVWorkTaskTemplate.TaskType : Edm.String "Task Type"
PX.Objects.SV.SVWorkTaskTemplate.Summary : Edm.String "Summary"
PX.Objects.SV.SVWorkTaskTemplate.EstDuration : Edm.Int32 "Estimated Duration"
PX.Objects.SV.SVWorkTaskTemplate.IsActive : Edm.Boolean [required] "Active"
PX.Objects.SV.SVWorkTaskTemplate.SchedulableItem : Edm.Boolean [required] "Schedulable"
PX.Objects.SV.SVWorkTaskTemplate.Description : Edm.String "Description"
PX.Objects.SV.SVWorkTaskTemplate.ActionLineCntr : Edm.Int32 [required]
PX.Objects.SV.SVWorkTaskTemplate.LaborLineCntr : Edm.Int32 [required]
PX.Objects.SV.SVWorkTaskTemplate.ResourcePropertyLineCntr : Edm.Int32 [required]
PX.Objects.SV.SVWorkTaskTemplate.tstamp : Edm.Binary
PX.Objects.SV.SVWorkTaskTemplate.CreatedByID : Edm.Guid "Created By"
PX.Objects.SV.SVWorkTaskTemplate.CreatedByScreenID : Edm.String
PX.Objects.SV.SVWorkTaskTemplate.CreatedDateTime : Edm.DateTimeOffset
PX.Objects.SV.SVWorkTaskTemplate.LastModifiedByID : Edm.Guid "Last Modified By"
PX.Objects.SV.SVWorkTaskTemplate.LastModifiedByScreenID : Edm.String
PX.Objects.SV.SVWorkTaskTemplate.LastModifiedDateTime : Edm.DateTimeOffset
PX.Objects.SV.SVWorkTaskTemplate.UsersByCreatedByID -> PX.SM.Users (CreatedByID=PKID)
PX.Objects.SV.SVWorkTaskTemplate.UsersByLastModifiedByID -> PX.SM.Users (LastModifiedByID=PKID)
PX.Objects.SV.SVWorkTaskTemplate.SVOrderTypeTaskTemplateCollection -> Collection(PX.Objects.SV.SVOrderTypeTaskTemplate)
PX.Objects.SV.SVWorkTaskTemplate.SVWorkTaskCollection -> Collection(PX.Objects.SV.SVWorkTask)
PX.Objects.SV.SVWorkTaskTemplate.SVWorkTaskTemplateActionCollection -> Collection(PX.Objects.SV.SVWorkTaskTemplateAction)
PX.Objects.SV.SVWorkTaskTemplate.SVWorkTaskTemplateLaborCollection -> Collection(PX.Objects.SV.SVWorkTaskTemplateLabor)
PX.Objects.SV.SVWorkTaskTemplate.SVWorkTaskTemplateResourcePropertyCollection -> Collection(PX.Objects.SV.SVWorkTaskTemplateResourceProperty)

# PX.Objects.SV.SVWorkTaskTemplateAction (EntityType)

Label: "Checklist tab"
Key: LineNbr, TaskTemplateID
Entity sets: PX_Objects_SV_SVWorkTaskTemplateAction, Checklisttab, SVWorkTaskTemplateAction

PX.Objects.SV.SVWorkTaskTemplateAction.TaskTemplateID : Edm.String [key] "Task Template ID"
PX.Objects.SV.SVWorkTaskTemplateAction.LineNbr : Edm.Int32 [key] "Line Nbr."
PX.Objects.SV.SVWorkTaskTemplateAction.Description : Edm.String "Action Description"
PX.Objects.SV.SVWorkTaskTemplateAction.Comment : Edm.String "Comment"
PX.Objects.SV.SVWorkTaskTemplateAction.SortOrder : Edm.Int32
PX.Objects.SV.SVWorkTaskTemplateAction.tstamp : Edm.Binary
PX.Objects.SV.SVWorkTaskTemplateAction.CreatedByID : Edm.Guid "Created By"
PX.Objects.SV.SVWorkTaskTemplateAction.CreatedByScreenID : Edm.String
PX.Objects.SV.SVWorkTaskTemplateAction.CreatedDateTime : Edm.DateTimeOffset
PX.Objects.SV.SVWorkTaskTemplateAction.LastModifiedByID : Edm.Guid "Last Modified By"
PX.Objects.SV.SVWorkTaskTemplateAction.LastModifiedByScreenID : Edm.String
PX.Objects.SV.SVWorkTaskTemplateAction.LastModifiedDateTime : Edm.DateTimeOffset
PX.Objects.SV.SVWorkTaskTemplateAction.UsersByCreatedByID -> PX.SM.Users (CreatedByID=PKID)
PX.Objects.SV.SVWorkTaskTemplateAction.UsersByLastModifiedByID -> PX.SM.Users (LastModifiedByID=PKID)
PX.Objects.SV.SVWorkTaskTemplateAction.SVWorkTaskTemplateByTaskTemplateID -> PX.Objects.SV.SVWorkTaskTemplate (TaskTemplateID=TaskTemplateID)

# PX.Objects.SV.SVWorkTaskTemplateLabor (EntityType)

Label: "Work Task Template Workforce"
Key: LineNbr, TaskTemplateID
Entity sets: PX_Objects_SV_SVWorkTaskTemplateLabor, WorkTaskTemplateWorkforce1, SVWorkTaskTemplateLabor
Non-filterable, non-selectable: NoteText

PX.Objects.SV.SVWorkTaskTemplateLabor.TaskTemplateID : Edm.String [key] "Task Template"
PX.Objects.SV.SVWorkTaskTemplateLabor.LineNbr : Edm.Int32 [key] "Line Nbr."
PX.Objects.SV.SVWorkTaskTemplateLabor.ResourceNoteID : Edm.Guid "Resources"
PX.Objects.SV.SVWorkTaskTemplateLabor.Name : Edm.String "Name"
PX.Objects.SV.SVWorkTaskTemplateLabor.Position : Edm.String "Position"
PX.Objects.SV.SVWorkTaskTemplateLabor.Phone1 : Edm.String "Phone 1"
PX.Objects.SV.SVWorkTaskTemplateLabor.Phone2 : Edm.String "Phone 2"
PX.Objects.SV.SVWorkTaskTemplateLabor.NoteID : Edm.Guid
PX.Objects.SV.SVWorkTaskTemplateLabor.NoteText : Edm.String "Note Text"
PX.Objects.SV.SVWorkTaskTemplateLabor.tstamp : Edm.Binary
PX.Objects.SV.SVWorkTaskTemplateLabor.CreatedByID : Edm.Guid "Created By"
PX.Objects.SV.SVWorkTaskTemplateLabor.CreatedByScreenID : Edm.String
PX.Objects.SV.SVWorkTaskTemplateLabor.CreatedDateTime : Edm.DateTimeOffset
PX.Objects.SV.SVWorkTaskTemplateLabor.LastModifiedByID : Edm.Guid "Last Modified By"
PX.Objects.SV.SVWorkTaskTemplateLabor.LastModifiedByScreenID : Edm.String
PX.Objects.SV.SVWorkTaskTemplateLabor.LastModifiedDateTime : Edm.DateTimeOffset "Last Modified"
PX.Objects.SV.SVWorkTaskTemplateLabor.UsersByCreatedByID -> PX.SM.Users (CreatedByID=PKID)
PX.Objects.SV.SVWorkTaskTemplateLabor.UsersByLastModifiedByID -> PX.SM.Users (LastModifiedByID=PKID)
PX.Objects.SV.SVWorkTaskTemplateLabor.EPPositionByPosition -> PX.Objects.EP.EPPosition (Position=PositionID)
PX.Objects.SV.SVWorkTaskTemplateLabor.SVResourceByResourceNoteID -> PX.Objects.SV.SVResource (ResourceNoteID=ResourceNoteID)
PX.Objects.SV.SVWorkTaskTemplateLabor.SVWorkTaskTemplateByTaskTemplateID -> PX.Objects.SV.SVWorkTaskTemplate (TaskTemplateID=TaskTemplateID)

# PX.Objects.SV.SVWorkTaskTemplateResourceProperty (EntityType)

Label: "Work Task Template Workforce"
Key: LineNbr, TaskTemplateID
Entity sets: PX_Objects_SV_SVWorkTaskTemplateResourceProperty, WorkTaskTemplateWorkforce2, SVWorkTaskTemplateResourceProperty
Non-filterable, non-selectable: ResourceClassDescription, ResourceClassPropertyName

PX.Objects.SV.SVWorkTaskTemplateResourceProperty.TaskTemplateID : Edm.String [key] "Task Template"
PX.Objects.SV.SVWorkTaskTemplateResourceProperty.LineNbr : Edm.Int32 [key] "Line Nbr."
PX.Objects.SV.SVWorkTaskTemplateResourceProperty.ResourceClassID : Edm.String "Resource Class"
PX.Objects.SV.SVWorkTaskTemplateResourceProperty.ClassPropertyID : Edm.String "Property ID"
PX.Objects.SV.SVWorkTaskTemplateResourceProperty.PropertyValue : Edm.String "Property Value"
PX.Objects.SV.SVWorkTaskTemplateResourceProperty.Description : Edm.String "Description"
PX.Objects.SV.SVWorkTaskTemplateResourceProperty.ResourceClassDescription : Edm.String "Resource Class Description"
PX.Objects.SV.SVWorkTaskTemplateResourceProperty.ResourceClassPropertyName : Edm.String "Resource Class Property Name"
PX.Objects.SV.SVWorkTaskTemplateResourceProperty.tstamp : Edm.Binary
PX.Objects.SV.SVWorkTaskTemplateResourceProperty.CreatedByID : Edm.Guid "Created By"
PX.Objects.SV.SVWorkTaskTemplateResourceProperty.CreatedByScreenID : Edm.String
PX.Objects.SV.SVWorkTaskTemplateResourceProperty.CreatedDateTime : Edm.DateTimeOffset
PX.Objects.SV.SVWorkTaskTemplateResourceProperty.LastModifiedByID : Edm.Guid "Last Modified By"
PX.Objects.SV.SVWorkTaskTemplateResourceProperty.LastModifiedByScreenID : Edm.String
PX.Objects.SV.SVWorkTaskTemplateResourceProperty.LastModifiedDateTime : Edm.DateTimeOffset "Last Modified"
PX.Objects.SV.SVWorkTaskTemplateResourceProperty.UsersByCreatedByID -> PX.SM.Users (CreatedByID=PKID)
PX.Objects.SV.SVWorkTaskTemplateResourceProperty.UsersByLastModifiedByID -> PX.SM.Users (LastModifiedByID=PKID)
PX.Objects.SV.SVWorkTaskTemplateResourceProperty.SVWorkTaskTemplateByTaskTemplateID -> PX.Objects.SV.SVWorkTaskTemplate (TaskTemplateID=TaskTemplateID)

# PX.Objects.SV.SVWorkTaskTotal (EntityType)

Label: "Time Widget"
Key: RefNoteId
Entity sets: PX_Objects_SV_SVWorkTaskTotal, TimeWidget, SVWorkTaskTotal

PX.Objects.SV.SVWorkTaskTotal.RefNoteId : Edm.Guid [key] "Work Order Nbr."
PX.Objects.SV.SVWorkTaskTotal.EstimatedDuration : Edm.Int32 [required] "Total Time"

# PX.Objects.TX.DAC.TaxTranForReporting (EntityType)

Label: "Tax Transaction"
BaseType: PX.Objects.TX.TaxTran
Key: Module, RecordID (inherited from PX.Objects.TX.TaxTran)
Entity sets: PX_Objects_TX_DAC_TaxTranForReporting
Non-filterable, non-selectable: Sign

PX.Objects.TX.DAC.TaxTranForReporting.TranTypeInvoiceDiscriminated : Edm.String "Tran. Type"
PX.Objects.TX.DAC.TaxTranForReporting.Sign : Edm.Decimal

# PX.Objects.TX.SVATConversionHist (EntityType)

Label: "SVAT Conversion History"
Key: AdjdDocType, AdjdLineNbr, AdjdRefNbr, AdjgDocType, AdjgRefNbr, AdjNbr, Module, TaxID
Entity sets: PX_Objects_TX_SVATConversionHist, SVATConversionHistory, SVATConversionHist

PX.Objects.TX.SVATConversionHist.Module : Edm.String [key] "Module"
PX.Objects.TX.SVATConversionHist.AdjdDocType : Edm.String [key] "Type"
PX.Objects.TX.SVATConversionHist.AdjdRefNbr : Edm.String [key] "Reference Nbr."
PX.Objects.TX.SVATConversionHist.AdjdLineNbr : Edm.Int32 [key required] "Line Nbr."
PX.Objects.TX.SVATConversionHist.AdjgDocType : Edm.String [key] "AdjgDocType"
PX.Objects.TX.SVATConversionHist.AdjgRefNbr : Edm.String [key] "AdjgRefNbr"
PX.Objects.TX.SVATConversionHist.AdjNbr : Edm.Int32 [key required] "Adjustment Nbr."
PX.Objects.TX.SVATConversionHist.AdjdDocDate : Edm.DateTimeOffset "Date"
PX.Objects.TX.SVATConversionHist.AdjdFinPeriodID : Edm.String "Post Period"
PX.Objects.TX.SVATConversionHist.AdjdTranPeriodID : Edm.String
PX.Objects.TX.SVATConversionHist.AdjgFinPeriodID : Edm.String "Application Period"
PX.Objects.TX.SVATConversionHist.AdjgTranPeriodID : Edm.String
PX.Objects.TX.SVATConversionHist.AdjBatchNbr : Edm.String "Batch Number"
PX.Objects.TX.SVATConversionHist.TaxRecordID : Edm.Int32
PX.Objects.TX.SVATConversionHist.TaxID : Edm.String [key] "Tax ID"
PX.Objects.TX.SVATConversionHist.TaxType : Edm.String
PX.Objects.TX.SVATConversionHist.TaxRate : Edm.Decimal "Tax Rate"
PX.Objects.TX.SVATConversionHist.VendorID : Edm.Int32
PX.Objects.TX.SVATConversionHist.TaxInvoiceNbr : Edm.String "Tax Doc. Nbr"
PX.Objects.TX.SVATConversionHist.TaxInvoiceDate : Edm.DateTimeOffset "Tax Doc. Date"
PX.Objects.TX.SVATConversionHist.ReversalMethod : Edm.String "VAT Recognition Method"
PX.Objects.TX.SVATConversionHist.CuryInfoID : Edm.Int64
PX.Objects.TX.SVATConversionHist.CuryTaxableAmt : Edm.Decimal "Taxable Amount"
PX.Objects.TX.SVATConversionHist.TaxableAmt : Edm.Decimal "Taxable Amount"
PX.Objects.TX.SVATConversionHist.CuryTaxAmt : Edm.Decimal "Tax Amount"
PX.Objects.TX.SVATConversionHist.TaxAmt : Edm.Decimal "Tax Amount"
PX.Objects.TX.SVATConversionHist.CuryUnrecognizedTaxAmt : Edm.Decimal "Unrecognized VAT"
PX.Objects.TX.SVATConversionHist.UnrecognizedTaxAmt : Edm.Decimal "Unrecognized VAT"
PX.Objects.TX.SVATConversionHist.Processed : Edm.Boolean [required]
PX.Objects.TX.SVATConversionHist.tstamp : Edm.Binary
PX.Objects.TX.SVATConversionHist.CreatedByID : Edm.Guid "Created By"
PX.Objects.TX.SVATConversionHist.CreatedByScreenID : Edm.String
PX.Objects.TX.SVATConversionHist.CreatedDateTime : Edm.DateTimeOffset
PX.Objects.TX.SVATConversionHist.LastModifiedByID : Edm.Guid "Last Modified By"
PX.Objects.TX.SVATConversionHist.LastModifiedByScreenID : Edm.String
PX.Objects.TX.SVATConversionHist.LastModifiedDateTime : Edm.DateTimeOffset
PX.Objects.TX.SVATConversionHist.CuryTaxableAmtBalance : Edm.Decimal
PX.Objects.TX.SVATConversionHist.TaxableAmtBalance : Edm.Decimal
PX.Objects.TX.SVATConversionHist.CuryTaxAmtBalance : Edm.Decimal
PX.Objects.TX.SVATConversionHist.TaxAmtBalance : Edm.Decimal
PX.Objects.TX.SVATConversionHist.VendorByVendorID -> PX.Objects.AP.Vendor (VendorID=BAccountID)
PX.Objects.TX.SVATConversionHist.BatchByAdjBatchNbr -> PX.Objects.GL.Batch (AdjBatchNbr=BatchNbr)
PX.Objects.TX.SVATConversionHist.BranchByAdjdBranchID -> PX.Objects.GL.Branch
PX.Objects.TX.SVATConversionHist.CurrencyInfoByCuryInfoID -> PX.Objects.CM.CurrencyInfo (CuryInfoID=CuryInfoID)
PX.Objects.TX.SVATConversionHist.UsersByCreatedByID -> PX.SM.Users (CreatedByID=PKID)
PX.Objects.TX.SVATConversionHist.UsersByLastModifiedByID -> PX.SM.Users (LastModifiedByID=PKID)
PX.Objects.TX.SVATConversionHist.TaxByTaxID -> PX.Objects.TX.Tax (TaxID=TaxID)

# PX.Objects.TX.SVATConversionHistExt (EntityType)

Label: "SVAT Conversion History"
BaseType: PX.Objects.TX.SVATConversionHist
Key: AdjdDocType, AdjdLineNbr, AdjdRefNbr, AdjgDocType, AdjgRefNbr, AdjNbr, Module, TaxID (inherited from PX.Objects.TX.SVATConversionHist)
Entity sets: PX_Objects_TX_SVATConversionHistExt
Non-filterable, non-selectable: DisplayDocType

PX.Objects.TX.SVATConversionHistExt.Status : Edm.String "Status"
PX.Objects.TX.SVATConversionHistExt.DisplayDocType : Edm.String "Type"
PX.Objects.TX.SVATConversionHistExt.DisplayCounterPartyID : Edm.Int32 "Customer/Vendor"
PX.Objects.TX.SVATConversionHistExt.DisplayDescription : Edm.String "Description"
PX.Objects.TX.SVATConversionHistExt.DisplayDocRef : Edm.String "Document Ref. / Customer Order Nbr."
PX.Objects.TX.SVATConversionHistExt.DisplayTaxEntryRefNbr : Edm.String
PX.Objects.TX.SVATConversionHistExt.DisplayOrigDocAmt : Edm.Decimal "Amount"
PX.Objects.TX.SVATConversionHistExt.DisplayDocBal : Edm.Decimal "Balance"
PX.Objects.TX.SVATConversionHistExt.BAccountByDisplayCounterPartyID -> PX.Objects.CR.BAccount (DisplayCounterPartyID=BAccountID)

# PX.Objects.TX.Tax (EntityType)

Label: "Tax"
Key: TaxID
Entity sets: PX_Objects_TX_Tax, Tax
Non-filterable, non-selectable: NoteText

PX.Objects.TX.Tax.TaxID : Edm.String [key] "Tax ID"
PX.Objects.TX.Tax.Descr : Edm.String "Description"
PX.Objects.TX.Tax.TaxType : Edm.String "Tax Type"
PX.Objects.TX.Tax.TaxCalcType : Edm.String
PX.Objects.TX.Tax.TaxCalcLevel : Edm.String
PX.Objects.TX.Tax.TaxCalcRule : Edm.String "Calculation Rule"
PX.Objects.TX.Tax.TaxCalcLevel2Exclude : Edm.Boolean [required] "Exclude from Tax-on-Tax Calculation"
PX.Objects.TX.Tax.TaxApplyTermsDisc : Edm.String "Cash Discount"
PX.Objects.TX.Tax.PendingTax : Edm.Boolean [required] "Pending VAT"
PX.Objects.TX.Tax.ReverseTax : Edm.Boolean [required] "Reverse VAT"
PX.Objects.TX.Tax.IncludeInTaxable : Edm.Boolean [required] "Include in VAT Taxable Total"
PX.Objects.TX.Tax.ExemptTax : Edm.Boolean [required] "Include in VAT Exempt Total"
PX.Objects.TX.Tax.StatisticalTax : Edm.Boolean [required] "Statistical VAT"
PX.Objects.TX.Tax.DirectTax : Edm.Boolean [required] "Direct-Entry Tax"
PX.Objects.TX.Tax.DeductibleVAT : Edm.Boolean [required] "Partially Deductible VAT"
PX.Objects.TX.Tax.ReportExpenseToSingleAccount : Edm.Boolean [required] "Use Tax Expense Account"
PX.Objects.TX.Tax.PerUnitTaxPostMode : Edm.String "Post To"
PX.Objects.TX.Tax.ShortPrintingLabel : Edm.String "Short Printing Label"
PX.Objects.TX.Tax.LongPrintingLabel : Edm.String "Long Printing Label"
PX.Objects.TX.Tax.PrintingSequence : Edm.Int32 "Printing Sequence"
PX.Objects.TX.Tax.TaxVendorID : Edm.Int32 "Tax Agency"
PX.Objects.TX.Tax.Outdated : Edm.Boolean "Is Blocked"
PX.Objects.TX.Tax.OutDate : Edm.DateTimeOffset "Not Valid After"
PX.Objects.TX.Tax.IsImported : Edm.Boolean [required]
PX.Objects.TX.Tax.IsExternal : Edm.Boolean [required]
PX.Objects.TX.Tax.ZeroTaxable : Edm.Boolean [required]
PX.Objects.TX.Tax.NoteID : Edm.Guid
PX.Objects.TX.Tax.NoteText : Edm.String "Note Text"
PX.Objects.TX.Tax.tstamp : Edm.Binary
PX.Objects.TX.Tax.CreatedByID : Edm.Guid "Created By"
PX.Objects.TX.Tax.CreatedByScreenID : Edm.String
PX.Objects.TX.Tax.CreatedDateTime : Edm.DateTimeOffset "Created On"
PX.Objects.TX.Tax.LastModifiedByID : Edm.Guid "Last Modified By"
PX.Objects.TX.Tax.LastModifiedByScreenID : Edm.String
PX.Objects.TX.Tax.LastModifiedDateTime : Edm.DateTimeOffset "Last Modified On"
PX.Objects.TX.Tax.VendorByTaxVendorID -> PX.Objects.AP.Vendor (TaxVendorID=BAccountID)
PX.Objects.TX.Tax.BAccountByTaxVendorID -> PX.Objects.CR.BAccount (TaxVendorID=BAccountID)
PX.Objects.TX.Tax.UsersByCreatedByID -> PX.SM.Users (CreatedByID=PKID)
PX.Objects.TX.Tax.UsersByLastModifiedByID -> PX.SM.Users (LastModifiedByID=PKID)
PX.Objects.TX.Tax.INUnitByTaxUOM -> PX.Objects.IN.INUnit
PX.Objects.TX.Tax.AccountBySalesTaxAcctID -> PX.Objects.GL.Account
PX.Objects.TX.Tax.AccountByPurchTaxAcctID -> PX.Objects.GL.Account
PX.Objects.TX.Tax.AccountByPendingSalesTaxAcctID -> PX.Objects.GL.Account
PX.Objects.TX.Tax.AccountByPendingPurchTaxAcctID -> PX.Objects.GL.Account
PX.Objects.TX.Tax.AccountByOnARPrepaymentTaxAcctID -> PX.Objects.GL.Account
PX.Objects.TX.Tax.AccountByOnAPPrepaymentTaxAcctID -> PX.Objects.GL.Account
PX.Objects.TX.Tax.AccountByExpenseAccountID -> PX.Objects.GL.Account
PX.Objects.TX.Tax.AccountByRetainageTaxPayableAcctID -> PX.Objects.GL.Account
PX.Objects.TX.Tax.AccountByRetainageTaxClaimableAcctID -> PX.Objects.GL.Account
PX.Objects.TX.Tax.SubBySalesTaxSubID -> PX.Objects.GL.Sub
PX.Objects.TX.Tax.SubByPurchTaxSubID -> PX.Objects.GL.Sub
PX.Objects.TX.Tax.SubByPendingSalesTaxSubID -> PX.Objects.GL.Sub
PX.Objects.TX.Tax.SubByPendingPurchTaxSubID -> PX.Objects.GL.Sub
PX.Objects.TX.Tax.SubByOnARPrepaymentTaxSubID -> PX.Objects.GL.Sub
PX.Objects.TX.Tax.SubByOnAPPrepaymentTaxSubID -> PX.Objects.GL.Sub
PX.Objects.TX.Tax.SubByExpenseSubID -> PX.Objects.GL.Sub
PX.Objects.TX.Tax.SubByRetainageTaxPayableSubID -> PX.Objects.GL.Sub
PX.Objects.TX.Tax.SubByRetainageTaxClaimableSubID -> PX.Objects.GL.Sub
PX.Objects.TX.Tax.DiscrepancyByAccountEnqResultCollection -> Collection(ReconciliationTools.DiscrepancyByAccountEnqResult)
PX.Objects.TX.Tax.TaxTranCollection -> Collection(PX.Objects.TX.TaxTran)
PX.Objects.TX.Tax.SOTaxTranCollection -> Collection(PX.Objects.SO.SOTaxTran)
PX.Objects.TX.Tax.POTaxTranCollection -> Collection(PX.Objects.PO.POTaxTran)
PX.Objects.TX.Tax.PMChangeRequestTaxCollection -> Collection(PX.Objects.PM.PMChangeRequestTax)
PX.Objects.TX.Tax.PMChangeRequestTaxTranCollection -> Collection(PX.Objects.PM.PMChangeRequestTaxTran)
PX.Objects.TX.Tax.GLTaxCollection -> Collection(PX.Objects.GL.GLTax)
PX.Objects.TX.Tax.ARTaxCollection -> Collection(PX.Objects.AR.ARTax)
PX.Objects.TX.Tax.FSAppointmentTaxCollection -> Collection(PX.Objects.FS.FSAppointmentTax)
PX.Objects.TX.Tax.FSServiceOrderTaxCollection -> Collection(PX.Objects.FS.FSServiceOrderTax)
PX.Objects.TX.Tax.SVATConversionHistCollection -> Collection(PX.Objects.TX.SVATConversionHist)
PX.Objects.TX.Tax.SOTaxCollection -> Collection(PX.Objects.SO.SOTax)
PX.Objects.TX.Tax.POLandedCostTaxCollection -> Collection(PX.Objects.PO.POLandedCostTax)
PX.Objects.TX.Tax.POLandedCostTaxTranCollection -> Collection(PX.Objects.PO.POLandedCostTaxTran)
PX.Objects.TX.Tax.POTaxCollection -> Collection(PX.Objects.PO.POTax)
PX.Objects.TX.Tax.PMChangeOrderTaxCollection -> Collection(PX.Objects.PM.PMChangeOrderTax)
PX.Objects.TX.Tax.POLineCollection -> Collection(PX.Objects.PO.POLine)
PX.Objects.TX.Tax.PMChangeOrderTaxTranCollection -> Collection(PX.Objects.PM.PMChangeOrderTaxTran)
PX.Objects.TX.Tax.PMTaxCollection -> Collection(PX.Objects.PM.PMTax)
PX.Objects.TX.Tax.PMTaxTranCollection -> Collection(PX.Objects.PM.PMTaxTran)
PX.Objects.TX.Tax.GLTranCollection -> Collection(PX.Objects.GL.GLTran)
PX.Objects.TX.Tax.CABankChargeTaxCollection -> Collection(PX.Objects.CA.CABankChargeTax)
PX.Objects.TX.Tax.CABankTaxCollection -> Collection(PX.Objects.CA.CABankTax)
PX.Objects.TX.Tax.CABankTaxTranCollection -> Collection(PX.Objects.CA.CABankTaxTran)
PX.Objects.TX.Tax.CABankTaxTranMatchCollection -> Collection(PX.Objects.CA.CABankTaxTranMatch)
PX.Objects.TX.Tax.CAExpenseTaxCollection -> Collection(PX.Objects.CA.CAExpenseTax)
PX.Objects.TX.Tax.CATaxCollection -> Collection(PX.Objects.CA.CATax)
PX.Objects.TX.Tax.CROpportunityTaxCollection -> Collection(PX.Objects.CR.CROpportunityTax)
PX.Objects.TX.Tax.CRTaxTranCollection -> Collection(PX.Objects.CR.CRTaxTran)
PX.Objects.TX.Tax.EPTaxCollection -> Collection(PX.Objects.EP.EPTax)
PX.Objects.TX.Tax.EPTaxAggregateCollection -> Collection(PX.Objects.EP.EPTaxAggregate)
PX.Objects.TX.Tax.EPTaxTranCollection -> Collection(PX.Objects.EP.EPTaxTran)
PX.Objects.TX.Tax.APTaxCollection -> Collection(PX.Objects.AP.APTax)
PX.Objects.TX.Tax.FSAppointmentTaxTranCollection -> Collection(PX.Objects.FS.FSAppointmentTaxTran)
PX.Objects.TX.Tax.FSServiceOrderTaxTranCollection -> Collection(PX.Objects.FS.FSServiceOrderTaxTran)
PX.Objects.TX.Tax.SVTaxCollection -> Collection(PX.Objects.SV.SVTax)
PX.Objects.TX.Tax.SVTaxTranCollection -> Collection(PX.Objects.SV.SVTaxTran)
PX.Objects.TX.Tax.APTranCollection -> Collection(PX.Objects.AP.APTran)
PX.Objects.TX.Tax.ARSalesPriceCollection -> Collection(PX.Objects.AR.ARSalesPrice)
PX.Objects.TX.Tax.ARTranCollection -> Collection(PX.Objects.AR.ARTran)
PX.Objects.TX.Tax.GLTranDocCollection -> Collection(PX.Objects.GL.GLTranDoc)
PX.Objects.TX.Tax.TaxCategoryDetCollection -> Collection(PX.Objects.TX.TaxCategoryDet)
PX.Objects.TX.Tax.TaxRevCollection -> Collection(PX.Objects.TX.TaxRev)
PX.Objects.TX.Tax.TaxZoneCollection -> Collection(PX.Objects.TX.TaxZone)
PX.Objects.TX.Tax.TaxZoneDetCollection -> Collection(PX.Objects.TX.TaxZoneDet)
PX.Objects.TX.Tax.ARPriceWorksheetDetailCollection -> Collection(PX.Objects.AR.ARPriceWorksheetDetail)
PX.Objects.TX.Tax.APPriceWorksheetDetailCollection -> Collection(PX.Objects.AP.APPriceWorksheetDetail)
PX.Objects.TX.Tax.BCAmazonTaxMappingCollection -> Collection(PX.Commerce.Amazon.BCAmazonTaxMapping)
PX.Objects.TX.Tax.TaxRegistrationCollection -> Collection(PX.Objects.Localizations.CA.TaxRegistration)
PX.Objects.TX.Tax.CISSubcontractorCollection -> Collection(PX.Objects.Localizations.GB.CISSubcontractor)
PX.Objects.TX.Tax.POLineRSCollection -> Collection(PX.Objects.PO.POLineRS)
PX.Objects.TX.Tax.POLineSCollection -> Collection(PX.Objects.PO.POLineS)
PX.Objects.TX.Tax.POReceiptLineSCollection -> Collection(PX.Objects.PO.POReceiptLineS)
PX.Objects.TX.Tax.TaxDetailByGLReportCollection -> Collection(PX.Objects.TX.TaxDetailByGLReport)

# PX.Objects.TX.TaxAdjustment (EntityType)

Label: "Tax Adjustment"
Key: DocType, RefNbr
Entity sets: PX_Objects_TX_TaxAdjustment, TaxAdjustment
Non-filterable, non-selectable: NoteText, CuryRate

PX.Objects.TX.TaxAdjustment.DocType : Edm.String [key required] "Type"
PX.Objects.TX.TaxAdjustment.RefNbr : Edm.String [key] "Reference Nbr."
PX.Objects.TX.TaxAdjustment.OrigRefNbr : Edm.String "Orig. Ref. Nbr."
PX.Objects.TX.TaxAdjustment.DocDate : Edm.DateTimeOffset "Date"
PX.Objects.TX.TaxAdjustment.FinPeriodID : Edm.String "Post Period"
PX.Objects.TX.TaxAdjustment.TranPeriodID : Edm.String "Master Period"
PX.Objects.TX.TaxAdjustment.VendorID : Edm.Int32 "Tax Agency"
PX.Objects.TX.TaxAdjustment.TaxPeriod : Edm.String "Tax Period"
PX.Objects.TX.TaxAdjustment.CuryID : Edm.String "Currency"
PX.Objects.TX.TaxAdjustment.LineCntr : Edm.Int32 [required]
PX.Objects.TX.TaxAdjustment.CuryInfoID : Edm.Int64
PX.Objects.TX.TaxAdjustment.CuryOrigDocAmt : Edm.Decimal [required] "Amount"
PX.Objects.TX.TaxAdjustment.OrigDocAmt : Edm.Decimal [required]
PX.Objects.TX.TaxAdjustment.CuryDocBal : Edm.Decimal [required] "Balance"
PX.Objects.TX.TaxAdjustment.DocBal : Edm.Decimal [required]
PX.Objects.TX.TaxAdjustment.DocDesc : Edm.String "Description"
PX.Objects.TX.TaxAdjustment.CreatedByID : Edm.Guid "Created By"
PX.Objects.TX.TaxAdjustment.CreatedByScreenID : Edm.String
PX.Objects.TX.TaxAdjustment.CreatedDateTime : Edm.DateTimeOffset "Created On"
PX.Objects.TX.TaxAdjustment.LastModifiedByID : Edm.Guid "Last Modified By"
PX.Objects.TX.TaxAdjustment.LastModifiedByScreenID : Edm.String
PX.Objects.TX.TaxAdjustment.LastModifiedDateTime : Edm.DateTimeOffset "Last Modified On"
PX.Objects.TX.TaxAdjustment.tstamp : Edm.Binary
PX.Objects.TX.TaxAdjustment.BatchNbr : Edm.String "Batch Nbr."
PX.Objects.TX.TaxAdjustment.Status : Edm.String "Status"
PX.Objects.TX.TaxAdjustment.Released : Edm.Boolean [required]
PX.Objects.TX.TaxAdjustment.Hold : Edm.Boolean [required] "Hold"
PX.Objects.TX.TaxAdjustment.NoteID : Edm.Guid
PX.Objects.TX.TaxAdjustment.NoteText : Edm.String "Note Text"
PX.Objects.TX.TaxAdjustment.CuryRate : Edm.Decimal
PX.Objects.TX.TaxAdjustment.VendorByVendorID -> PX.Objects.AP.Vendor (VendorID=BAccountID)
PX.Objects.TX.TaxAdjustment.BAccountByVendorID -> PX.Objects.CR.BAccount (VendorID=BAccountID)
PX.Objects.TX.TaxAdjustment.BatchByBatchNbr -> PX.Objects.GL.Batch (BatchNbr=BatchNbr)
PX.Objects.TX.TaxAdjustment.BranchByBranchID -> PX.Objects.GL.Branch
PX.Objects.TX.TaxAdjustment.CurrencyInfoByCuryInfoID -> PX.Objects.CM.CurrencyInfo (CuryInfoID=CuryInfoID)
PX.Objects.TX.TaxAdjustment.UsersByCreatedByID -> PX.SM.Users (CreatedByID=PKID)
PX.Objects.TX.TaxAdjustment.UsersByLastModifiedByID -> PX.SM.Users (LastModifiedByID=PKID)
PX.Objects.TX.TaxAdjustment.CurrencyByCuryID -> PX.Objects.CM.Currency (CuryID=CuryID)
PX.Objects.TX.TaxAdjustment.AccountByAdjAccountID -> PX.Objects.GL.Account
PX.Objects.TX.TaxAdjustment.SubByAdjSubID -> PX.Objects.GL.Sub
PX.Objects.TX.TaxAdjustment.LocationByVendorLocationID -> PX.Objects.CR.Location (VendorID=BAccountID)
PX.Objects.TX.TaxAdjustment.LocationByVendorID -> PX.Objects.CR.Location (VendorID=BAccountID)
PX.Objects.TX.TaxAdjustment.TaxPeriodByVendorID -> PX.Objects.TX.TaxPeriod (TaxPeriod=TaxPeriodID, VendorID=VendorID)
PX.Objects.TX.TaxAdjustment.TaxTranCollection -> Collection(PX.Objects.TX.TaxTran)

# PX.Objects.TX.TaxBucket (EntityType)

Label: "Tax Group"
Key: BucketID, VendorID
Entity sets: PX_Objects_TX_TaxBucket, TaxGroup, TaxBucket

PX.Objects.TX.TaxBucket.VendorID : Edm.Int32 [key]
PX.Objects.TX.TaxBucket.BucketID : Edm.Int32 [key] "Reporting Group"
PX.Objects.TX.TaxBucket.BucketType : Edm.String "Group Type"
PX.Objects.TX.TaxBucket.Name : Edm.String "Name"
PX.Objects.TX.TaxBucket.CreatedByID : Edm.Guid "Created By"
PX.Objects.TX.TaxBucket.CreatedByScreenID : Edm.String
PX.Objects.TX.TaxBucket.CreatedDateTime : Edm.DateTimeOffset
PX.Objects.TX.TaxBucket.LastModifiedByID : Edm.Guid "Last Modified By"
PX.Objects.TX.TaxBucket.LastModifiedByScreenID : Edm.String
PX.Objects.TX.TaxBucket.LastModifiedDateTime : Edm.DateTimeOffset
PX.Objects.TX.TaxBucket.tstamp : Edm.Binary
PX.Objects.TX.TaxBucket.VendorByVendorID -> PX.Objects.AP.Vendor (VendorID=BAccountID)
PX.Objects.TX.TaxBucket.UsersByCreatedByID -> PX.SM.Users (CreatedByID=PKID)
PX.Objects.TX.TaxBucket.UsersByLastModifiedByID -> PX.SM.Users (LastModifiedByID=PKID)
PX.Objects.TX.TaxBucket.TaxTranCollection -> Collection(PX.Objects.TX.TaxTran)
PX.Objects.TX.TaxBucket.TaxBucketLineCollection -> Collection(PX.Objects.TX.TaxBucketLine)
PX.Objects.TX.TaxBucket.TaxRevCollection -> Collection(PX.Objects.TX.TaxRev)

# PX.Objects.TX.TaxBucketLine (EntityType)

Label: "Tax Group Line"
Key: BucketID, LineNbr, TaxReportRevisionID, VendorID
Entity sets: PX_Objects_TX_TaxBucketLine, TaxGroupLine, TaxBucketLine

PX.Objects.TX.TaxBucketLine.VendorID : Edm.Int32 [key]
PX.Objects.TX.TaxBucketLine.BucketID : Edm.Int32 [key]
PX.Objects.TX.TaxBucketLine.TaxReportRevisionID : Edm.Int32 [key] "Report Version"
PX.Objects.TX.TaxBucketLine.LineNbr : Edm.Int32 [key] "Report Line"
PX.Objects.TX.TaxBucketLine.CreatedByID : Edm.Guid "Created By"
PX.Objects.TX.TaxBucketLine.CreatedByScreenID : Edm.String
PX.Objects.TX.TaxBucketLine.CreatedDateTime : Edm.DateTimeOffset
PX.Objects.TX.TaxBucketLine.LastModifiedByID : Edm.Guid "Last Modified By"
PX.Objects.TX.TaxBucketLine.LastModifiedByScreenID : Edm.String
PX.Objects.TX.TaxBucketLine.LastModifiedDateTime : Edm.DateTimeOffset
PX.Objects.TX.TaxBucketLine.tstamp : Edm.Binary
PX.Objects.TX.TaxBucketLine.VendorByVendorID -> PX.Objects.AP.Vendor (VendorID=BAccountID)
PX.Objects.TX.TaxBucketLine.UsersByCreatedByID -> PX.SM.Users (CreatedByID=PKID)
PX.Objects.TX.TaxBucketLine.UsersByLastModifiedByID -> PX.SM.Users (LastModifiedByID=PKID)
PX.Objects.TX.TaxBucketLine.TaxBucketByBucketID -> PX.Objects.TX.TaxBucket (VendorID=VendorID, BucketID=BucketID)
PX.Objects.TX.TaxBucketLine.TaxReportLineByLineNbr -> PX.Objects.TX.TaxReportLine (VendorID=VendorID, TaxReportRevisionID=TaxReportRevisionID, LineNbr=LineNbr)
PX.Objects.TX.TaxBucketLine.TaxReportLineByTaxReportRevisionID -> PX.Objects.TX.TaxReportLine (LineNbr=LineNbr, VendorID=VendorID, TaxReportRevisionID=TaxReportRevisionID)

# PX.Objects.TX.TaxCategory (EntityType)

Label: "Tax Category"
Key: TaxCategoryID
Entity sets: PX_Objects_TX_TaxCategory, TaxCategory
Non-filterable, non-selectable: NoteText

PX.Objects.TX.TaxCategory.TaxCategoryID : Edm.String [key] "Tax Category ID"
PX.Objects.TX.TaxCategory.Descr : Edm.String "Description"
PX.Objects.TX.TaxCategory.TaxCatFlag : Edm.Boolean [required] "Exclude Listed Taxes"
PX.Objects.TX.TaxCategory.Active : Edm.Boolean [required] "Active"
PX.Objects.TX.TaxCategory.NoteID : Edm.Guid
PX.Objects.TX.TaxCategory.NoteText : Edm.String "Note Text"
PX.Objects.TX.TaxCategory.CreatedByID : Edm.Guid "Created By"
PX.Objects.TX.TaxCategory.CreatedByScreenID : Edm.String
PX.Objects.TX.TaxCategory.CreatedDateTime : Edm.DateTimeOffset
PX.Objects.TX.TaxCategory.LastModifiedByID : Edm.Guid "Last Modified By"
PX.Objects.TX.TaxCategory.LastModifiedByScreenID : Edm.String
PX.Objects.TX.TaxCategory.LastModifiedDateTime : Edm.DateTimeOffset
PX.Objects.TX.TaxCategory.UsersByCreatedByID -> PX.SM.Users (CreatedByID=PKID)
PX.Objects.TX.TaxCategory.UsersByLastModifiedByID -> PX.SM.Users (LastModifiedByID=PKID)
PX.Objects.TX.TaxCategory.DiscrepancyByAccountEnqResultCollection -> Collection(ReconciliationTools.DiscrepancyByAccountEnqResult)
PX.Objects.TX.TaxCategory.SOOrderCollection -> Collection(PX.Objects.SO.SOOrder)
PX.Objects.TX.TaxCategory.POLineCollection -> Collection(PX.Objects.PO.POLine)
PX.Objects.TX.TaxCategory.PMBudgetCollection -> Collection(PX.Objects.PM.PMBudget)
PX.Objects.TX.TaxCategory.PMChangeOrderBudgetCollection -> Collection(PX.Objects.PM.PMChangeOrderBudget)
PX.Objects.TX.TaxCategory.PMProformaLineCollection -> Collection(PX.Objects.PM.PMProformaLine)
PX.Objects.TX.TaxCategory.PMTaskCollection -> Collection(PX.Objects.PM.PMTask)
PX.Objects.TX.TaxCategory.INItemClassCollection -> Collection(PX.Objects.IN.INItemClass)
PX.Objects.TX.TaxCategory.InventoryItemCollection -> Collection(PX.Objects.IN.InventoryItem)
PX.Objects.TX.TaxCategory.GLTranCollection -> Collection(PX.Objects.GL.GLTran)
PX.Objects.TX.TaxCategory.EPExpenseClaimDetailsCollection -> Collection(PX.Objects.EP.EPExpenseClaimDetails)
PX.Objects.TX.TaxCategory.SOLineCollection -> Collection(PX.Objects.SO.SOLine)
PX.Objects.TX.TaxCategory.FSAppointmentDetCollection -> Collection(PX.Objects.FS.FSAppointmentDet)
PX.Objects.TX.TaxCategory.FSSODetCollection -> Collection(PX.Objects.FS.FSSODet)
PX.Objects.TX.TaxCategory.APTranCollection -> Collection(PX.Objects.AP.APTran)
PX.Objects.TX.TaxCategory.AccountCollection -> Collection(PX.Objects.GL.Account)
PX.Objects.TX.TaxCategory.ARTranCollection -> Collection(PX.Objects.AR.ARTran)
PX.Objects.TX.TaxCategory.GLTranDocCollection -> Collection(PX.Objects.GL.GLTranDoc)
PX.Objects.TX.TaxCategory.CROpportunityProductsCollection -> Collection(PX.Objects.CR.CROpportunityProducts)
PX.Objects.TX.TaxCategory.TaxCategoryDetCollection -> Collection(PX.Objects.TX.TaxCategoryDet)
PX.Objects.TX.TaxCategory.TaxZoneCollection -> Collection(PX.Objects.TX.TaxZone)
PX.Objects.TX.TaxCategory.SOFreightDetailCollection -> Collection(PX.Objects.SO.SOFreightDetail)
PX.Objects.TX.TaxCategory.SOShipmentCollection -> Collection(PX.Objects.SO.SOShipment)
PX.Objects.TX.TaxCategory.LandedCostCodeCollection -> Collection(PX.Objects.PO.LandedCostCode)
PX.Objects.TX.TaxCategory.POLandedCostDetailCollection -> Collection(PX.Objects.PO.POLandedCostDetail)
PX.Objects.TX.TaxCategory.PMChangeOrderLineCollection -> Collection(PX.Objects.PM.PMChangeOrderLine)
PX.Objects.TX.TaxCategory.PMMarkupCollection -> Collection(PX.Objects.PM.PMMarkup)
PX.Objects.TX.TaxCategory.PMQuoteTaskCollection -> Collection(PX.Objects.PM.PMQuoteTask)
PX.Objects.TX.TaxCategory.CarrierCollection -> Collection(PX.Objects.CS.Carrier)
PX.Objects.TX.TaxCategory.CABankTranDetailCollection -> Collection(PX.Objects.CA.CABankTranDetail)
PX.Objects.TX.TaxCategory.CAExpenseCollection -> Collection(PX.Objects.CA.CAExpense)
PX.Objects.TX.TaxCategory.CASplitCollection -> Collection(PX.Objects.CA.CASplit)
PX.Objects.TX.TaxCategory.ARFinChargeCollection -> Collection(PX.Objects.AR.ARFinCharge)
PX.Objects.TX.TaxCategory.AMEstimateClassCollection -> Collection(PX.Objects.AM.AMEstimateClass)
PX.Objects.TX.TaxCategory.AMEstimateReferenceCollection -> Collection(PX.Objects.AM.AMEstimateReference)
PX.Objects.TX.TaxCategory.SVOrderActualCollection -> Collection(PX.Objects.SV.SVOrderActual)
PX.Objects.TX.TaxCategory.SVOrderDetailCollection -> Collection(PX.Objects.SV.SVOrderDetail)
PX.Objects.TX.TaxCategory.POLineRSCollection -> Collection(PX.Objects.PO.POLineRS)
PX.Objects.TX.TaxCategory.POLineSCollection -> Collection(PX.Objects.PO.POLineS)
PX.Objects.TX.TaxCategory.POReceiptLineSCollection -> Collection(PX.Objects.PO.POReceiptLineS)
PX.Objects.TX.TaxCategory.POLandedCostDetailSCollection -> Collection(PX.Objects.PO.POLandedCostDetailS)
PX.Objects.TX.TaxCategory.TXImportSettingsCollection -> Collection(PX.Objects.TX.TXImportSettings)

# PX.Objects.TX.TaxCategoryDet (EntityType)

Label: "Tax Category Detail"
Key: TaxCategoryID, TaxID
Entity sets: PX_Objects_TX_TaxCategoryDet, TaxCategoryDetail, TaxCategoryDet

PX.Objects.TX.TaxCategoryDet.TaxCategoryID : Edm.String [key] "Tax Category"
PX.Objects.TX.TaxCategoryDet.TaxID : Edm.String [key] "Tax ID"
PX.Objects.TX.TaxCategoryDet.IsImported : Edm.Boolean [required]
PX.Objects.TX.TaxCategoryDet.CreatedByID : Edm.Guid "Created By"
PX.Objects.TX.TaxCategoryDet.CreatedByScreenID : Edm.String
PX.Objects.TX.TaxCategoryDet.CreatedDateTime : Edm.DateTimeOffset
PX.Objects.TX.TaxCategoryDet.LastModifiedByID : Edm.Guid "Last Modified By"
PX.Objects.TX.TaxCategoryDet.LastModifiedByScreenID : Edm.String
PX.Objects.TX.TaxCategoryDet.LastModifiedDateTime : Edm.DateTimeOffset
PX.Objects.TX.TaxCategoryDet.UsersByCreatedByID -> PX.SM.Users (CreatedByID=PKID)
PX.Objects.TX.TaxCategoryDet.UsersByLastModifiedByID -> PX.SM.Users (LastModifiedByID=PKID)
PX.Objects.TX.TaxCategoryDet.TaxByTaxID -> PX.Objects.TX.Tax (TaxID=TaxID)
PX.Objects.TX.TaxCategoryDet.TaxCategoryByTaxCategoryID -> PX.Objects.TX.TaxCategory (TaxCategoryID=TaxCategoryID)

# PX.Objects.TX.TaxDetailByGLReport (EntityType)

Label: "Tax Report Detail"
Key: Module, RecordID, RefNbr, TaxID, TranType
Entity sets: PX_Objects_TX_TaxDetailByGLReport, TaxReportDetail, TaxDetailByGLReport

PX.Objects.TX.TaxDetailByGLReport.Module : Edm.String [key]
PX.Objects.TX.TaxDetailByGLReport.TranType : Edm.String [key]
PX.Objects.TX.TaxDetailByGLReport.TranTypeInvoiceDiscriminated : Edm.String
PX.Objects.TX.TaxDetailByGLReport.RefNbr : Edm.String [key]
PX.Objects.TX.TaxDetailByGLReport.RecordID : Edm.Int32 [key]
PX.Objects.TX.TaxDetailByGLReport.Released : Edm.Boolean
PX.Objects.TX.TaxDetailByGLReport.Voided : Edm.Boolean
PX.Objects.TX.TaxDetailByGLReport.TaxPeriodID : Edm.String
PX.Objects.TX.TaxDetailByGLReport.TaxID : Edm.String [key]
PX.Objects.TX.TaxDetailByGLReport.VendorID : Edm.Int32 "Vendor"
PX.Objects.TX.TaxDetailByGLReport.TaxZoneID : Edm.String
PX.Objects.TX.TaxDetailByGLReport.TranDate : Edm.DateTimeOffset
PX.Objects.TX.TaxDetailByGLReport.TaxType : Edm.String
PX.Objects.TX.TaxDetailByGLReport.TaxRate : Edm.Decimal
PX.Objects.TX.TaxDetailByGLReport.TaxableAmt : Edm.Decimal
PX.Objects.TX.TaxDetailByGLReport.TaxAmt : Edm.Decimal
PX.Objects.TX.TaxDetailByGLReport.TaxableAmtIO : Edm.Decimal
PX.Objects.TX.TaxDetailByGLReport.TaxAmtIO : Edm.Decimal
PX.Objects.TX.TaxDetailByGLReport.TaxByTaxID -> PX.Objects.TX.Tax (TaxID=TaxID)
PX.Objects.TX.TaxDetailByGLReport.APRegisterByRefNbr -> PX.Objects.AP.APRegister (TranType=DocType, RefNbr=RefNbr)
PX.Objects.TX.TaxDetailByGLReport.ARRegisterByRefNbr -> PX.Objects.AR.ARRegister (TranType=DocType, RefNbr=RefNbr)
PX.Objects.TX.TaxDetailByGLReport.TaxAdjustmentByRefNbr -> PX.Objects.TX.TaxAdjustment (TranType=DocType, RefNbr=RefNbr)
PX.Objects.TX.TaxDetailByGLReport.TaxZoneByTaxZoneID -> PX.Objects.TX.TaxZone (TaxZoneID=TaxZoneID)
PX.Objects.TX.TaxDetailByGLReport.CAAdjByRefNbr -> PX.Objects.CA.CAAdj (TranType=AdjTranType, RefNbr=AdjRefNbr)

# PX.Objects.TX.TaxDetailReport (EntityType)

Label: "Tax Report Detail"
Key: LineNbr, Module, RecordID, RefNbr, TaxID, TranType
Entity sets: PX_Objects_TX_TaxDetailReport, TaxReportDetail1, TaxDetailReport

PX.Objects.TX.TaxDetailReport.LineNbr : Edm.Int32 [key]
PX.Objects.TX.TaxDetailReport.LineMult : Edm.Int16
PX.Objects.TX.TaxDetailReport.LineType : Edm.String
PX.Objects.TX.TaxDetailReport.Module : Edm.String [key]
PX.Objects.TX.TaxDetailReport.TranType : Edm.String [key]
PX.Objects.TX.TaxDetailReport.TranTypeInvoiceDiscriminated : Edm.String
PX.Objects.TX.TaxDetailReport.RefNbr : Edm.String [key]
PX.Objects.TX.TaxDetailReport.RecordID : Edm.Int32 [key]
PX.Objects.TX.TaxDetailReport.Released : Edm.Boolean
PX.Objects.TX.TaxDetailReport.Voided : Edm.Boolean
PX.Objects.TX.TaxDetailReport.TaxPeriodID : Edm.String
PX.Objects.TX.TaxDetailReport.TaxID : Edm.String [key]
PX.Objects.TX.TaxDetailReport.VendorID : Edm.Int32 "Vendor"
PX.Objects.TX.TaxDetailReport.TaxZoneID : Edm.String
PX.Objects.TX.TaxDetailReport.TranDate : Edm.DateTimeOffset
PX.Objects.TX.TaxDetailReport.TaxType : Edm.String
PX.Objects.TX.TaxDetailReport.TaxRate : Edm.Decimal
PX.Objects.TX.TaxDetailReport.ReportTaxableAmt : Edm.Decimal
PX.Objects.TX.TaxDetailReport.ReportExemptedAmt : Edm.Decimal
PX.Objects.TX.TaxDetailReport.ReportTaxAmt : Edm.Decimal
PX.Objects.TX.TaxDetailReport.APRegisterByRefNbr -> PX.Objects.AP.APRegister (TranType=DocType, RefNbr=RefNbr)
PX.Objects.TX.TaxDetailReport.ARRegisterByRefNbr -> PX.Objects.AR.ARRegister (TranType=DocType, RefNbr=RefNbr)
PX.Objects.TX.TaxDetailReport.TaxByTaxID -> PX.Objects.TX.Tax (TaxID=TaxID)
PX.Objects.TX.TaxDetailReport.TaxAdjustmentByRefNbr -> PX.Objects.TX.TaxAdjustment (TranType=DocType, RefNbr=RefNbr)
PX.Objects.TX.TaxDetailReport.TaxZoneByTaxZoneID -> PX.Objects.TX.TaxZone (TaxZoneID=TaxZoneID)
PX.Objects.TX.TaxDetailReport.CAAdjByRefNbr -> PX.Objects.CA.CAAdj (TranType=AdjTranType, RefNbr=AdjRefNbr)

# PX.Objects.TX.TaxDetailReportCurrency (EntityType)

Label: "Tax Detail Report Currency"
Key: LineNbr, Module, RecordID, RefNbr, TaxID, TranType
Entity sets: PX_Objects_TX_TaxDetailReportCurrency, TaxDetailReportCurrency

PX.Objects.TX.TaxDetailReportCurrency.LineNbr : Edm.Int32 [key]
PX.Objects.TX.TaxDetailReportCurrency.LineMult : Edm.Int16
PX.Objects.TX.TaxDetailReportCurrency.LineType : Edm.String
PX.Objects.TX.TaxDetailReportCurrency.Module : Edm.String [key]
PX.Objects.TX.TaxDetailReportCurrency.TranType : Edm.String [key]
PX.Objects.TX.TaxDetailReportCurrency.RefNbr : Edm.String [key]
PX.Objects.TX.TaxDetailReportCurrency.RecordID : Edm.Int32 [key]
PX.Objects.TX.TaxDetailReportCurrency.Released : Edm.Boolean
PX.Objects.TX.TaxDetailReportCurrency.Voided : Edm.Boolean
PX.Objects.TX.TaxDetailReportCurrency.TaxPeriodID : Edm.String
PX.Objects.TX.TaxDetailReportCurrency.TaxID : Edm.String [key]
PX.Objects.TX.TaxDetailReportCurrency.VendorID : Edm.Int32 "Vendor"
PX.Objects.TX.TaxDetailReportCurrency.TaxZoneID : Edm.String
PX.Objects.TX.TaxDetailReportCurrency.TranDate : Edm.DateTimeOffset
PX.Objects.TX.TaxDetailReportCurrency.TaxType : Edm.String
PX.Objects.TX.TaxDetailReportCurrency.TaxRate : Edm.Decimal
PX.Objects.TX.TaxDetailReportCurrency.TaxableAmt : Edm.Decimal
PX.Objects.TX.TaxDetailReportCurrency.TaxAmt : Edm.Decimal
PX.Objects.TX.TaxDetailReportCurrency.VendorCuryID : Edm.String
PX.Objects.TX.TaxDetailReportCurrency.VendorCuryRateType : Edm.String
PX.Objects.TX.TaxDetailReportCurrency.CuryRate : Edm.Decimal
PX.Objects.TX.TaxDetailReportCurrency.CuryMultDiv : Edm.String
PX.Objects.TX.TaxDetailReportCurrency.APRegisterByRefNbr -> PX.Objects.AP.APRegister (TranType=DocType, RefNbr=RefNbr)
PX.Objects.TX.TaxDetailReportCurrency.ARRegisterByRefNbr -> PX.Objects.AR.ARRegister (TranType=DocType, RefNbr=RefNbr)
PX.Objects.TX.TaxDetailReportCurrency.TaxByTaxID -> PX.Objects.TX.Tax (TaxID=TaxID)
PX.Objects.TX.TaxDetailReportCurrency.TaxAdjustmentByRefNbr -> PX.Objects.TX.TaxAdjustment (TranType=DocType, RefNbr=RefNbr)
PX.Objects.TX.TaxDetailReportCurrency.TaxZoneByTaxZoneID -> PX.Objects.TX.TaxZone (TaxZoneID=TaxZoneID)
PX.Objects.TX.TaxDetailReportCurrency.CAAdjByRefNbr -> PX.Objects.CA.CAAdj (TranType=AdjTranType, RefNbr=AdjRefNbr)

# PX.Objects.TX.TaxHistory (EntityType)

Label: "Tax History"
Key: AccountID, BranchID, LineNbr, RevisionID, SubID, TaxID, TaxPeriodID, TaxReportRevisionID, VendorID
Entity sets: PX_Objects_TX_TaxHistory, TaxHistory

PX.Objects.TX.TaxHistory.BranchID : Edm.Int32 [key]
PX.Objects.TX.TaxHistory.AccountID : Edm.Int32 [key]
PX.Objects.TX.TaxHistory.SubID : Edm.Int32 [key]
PX.Objects.TX.TaxHistory.VendorID : Edm.Int32 [key]
PX.Objects.TX.TaxHistory.TaxReportRevisionID : Edm.Int32 [key required]
PX.Objects.TX.TaxHistory.TaxID : Edm.String [key]
PX.Objects.TX.TaxHistory.TaxPeriodID : Edm.String [key]
PX.Objects.TX.TaxHistory.LineNbr : Edm.Int32 [key]
PX.Objects.TX.TaxHistory.RevisionID : Edm.Int32 [key] "Revision ID"
PX.Objects.TX.TaxHistory.CuryID : Edm.String "Currency"
PX.Objects.TX.TaxHistory.FiledAmt : Edm.Decimal [required] "Amount"
PX.Objects.TX.TaxHistory.UnfiledAmt : Edm.Decimal [required] "Amount"
PX.Objects.TX.TaxHistory.ReportFiledAmt : Edm.Decimal [required] "Amount"
PX.Objects.TX.TaxHistory.ReportUnfiledAmt : Edm.Decimal [required] "Amount"
PX.Objects.TX.TaxHistory.tstamp : Edm.Binary
PX.Objects.TX.TaxHistory.VendorByVendorID -> PX.Objects.AP.Vendor (VendorID=BAccountID)
PX.Objects.TX.TaxHistory.BranchByBranchID -> PX.Objects.GL.Branch (BranchID=BranchID)
PX.Objects.TX.TaxHistory.CurrencyByCuryID -> PX.Objects.CM.Currency (CuryID=CuryID)
PX.Objects.TX.TaxHistory.AccountByAccountID -> PX.Objects.GL.Account (AccountID=AccountID)
PX.Objects.TX.TaxHistory.SubBySubID -> PX.Objects.GL.Sub (SubID=SubID)

# PX.Objects.TX.TaxHistorySum (EntityType)

Label: "Tax History Sum"
Key: BranchID, LineNbr, RevisionID, TaxPeriodID, TaxReportRevisionID, VendorID
Entity sets: PX_Objects_TX_TaxHistorySum, TaxHistorySum

PX.Objects.TX.TaxHistorySum.BranchID : Edm.Int32 [key]
PX.Objects.TX.TaxHistorySum.VendorID : Edm.Int32 [key]
PX.Objects.TX.TaxHistorySum.TaxReportRevisionID : Edm.Int32 [key]
PX.Objects.TX.TaxHistorySum.TaxPeriodID : Edm.String [key]
PX.Objects.TX.TaxHistorySum.RevisionID : Edm.Int32 [key] "Revision ID"
PX.Objects.TX.TaxHistorySum.LineNbr : Edm.Int32 [key]
PX.Objects.TX.TaxHistorySum.FiledAmt : Edm.Decimal "Amount"
PX.Objects.TX.TaxHistorySum.UnfiledAmt : Edm.Decimal "Amount"
PX.Objects.TX.TaxHistorySum.ReportFiledAmt : Edm.Decimal "Amount"
PX.Objects.TX.TaxHistorySum.ReportUnfiledAmt : Edm.Decimal "Amount"
PX.Objects.TX.TaxHistorySum.VendorByVendorID -> PX.Objects.AP.Vendor (VendorID=BAccountID)
PX.Objects.TX.TaxHistorySum.BranchByBranchID -> PX.Objects.GL.Branch (BranchID=BranchID)

# PX.Objects.TX.TaxPeriod (EntityType)

Label: "Tax Period"
Key: OrganizationID, TaxPeriodID, VendorID
Entity sets: PX_Objects_TX_TaxPeriod, TaxPeriod
Non-filterable, non-selectable: StartDateUI, EndDateUI

PX.Objects.TX.TaxPeriod.OrganizationID : Edm.Int32 [key] "Company"
PX.Objects.TX.TaxPeriod.VendorID : Edm.Int32 [key]
PX.Objects.TX.TaxPeriod.TaxPeriodID : Edm.String [key] "Tax Period"
PX.Objects.TX.TaxPeriod.TaxYear : Edm.String
PX.Objects.TX.TaxPeriod.StartDate : Edm.DateTimeOffset "Start Date"
PX.Objects.TX.TaxPeriod.EndDate : Edm.DateTimeOffset "To"
PX.Objects.TX.TaxPeriod.StartDateUI : Edm.DateTimeOffset "Start Date"
PX.Objects.TX.TaxPeriod.EndDateUI : Edm.DateTimeOffset "End Date"
PX.Objects.TX.TaxPeriod.Status : Edm.String "Status"
PX.Objects.TX.TaxPeriod.Filed : Edm.Boolean [required]
PX.Objects.TX.TaxPeriod.tstamp : Edm.Binary
PX.Objects.TX.TaxPeriod.VendorByVendorID -> PX.Objects.AP.Vendor (VendorID=BAccountID)
PX.Objects.TX.TaxPeriod.BAccountByVendorID -> PX.Objects.CR.BAccount (VendorID=BAccountID)
PX.Objects.TX.TaxPeriod.OrganizationByOrganizationID -> PX.Objects.GL.DAC.Organization (OrganizationID=OrganizationID)
PX.Objects.TX.TaxPeriod.TaxYearByTaxYear -> PX.Objects.TX.TaxYear (OrganizationID=OrganizationID, VendorID=VendorID, TaxYear=Year)
PX.Objects.TX.TaxPeriod.TaxTranCollection -> Collection(PX.Objects.TX.TaxTran)
PX.Objects.TX.TaxPeriod.TaxAdjustmentCollection -> Collection(PX.Objects.TX.TaxAdjustment)
PX.Objects.TX.TaxPeriod.TaxPeriodForReportShowingCollection -> Collection(PX.Objects.TX.TaxPeriodForReportShowing)

# PX.Objects.TX.TaxPeriodEffective (ComplexType)


PX.Objects.TX.TaxPeriodEffective.OrganizationID : Edm.Int32
PX.Objects.TX.TaxPeriodEffective.VendorID : Edm.Int32
PX.Objects.TX.TaxPeriodEffective.TaxPeriodID : Edm.String
PX.Objects.TX.TaxPeriodEffective.Status : Edm.String
PX.Objects.TX.TaxPeriodEffective.EndDate : Edm.DateTimeOffset
PX.Objects.TX.TaxPeriodEffective.RevisionID : Edm.Int32

# PX.Objects.TX.TaxPeriodForReportShowing (EntityType)

Key: OrganizationID, TaxPeriodID, VendorID
Entity sets: PX_Objects_TX_TaxPeriodForReportShowing
Non-filterable, non-selectable: RevisionID

PX.Objects.TX.TaxPeriodForReportShowing.OrganizationID : Edm.Int32 [key] "Company"
PX.Objects.TX.TaxPeriodForReportShowing.VendorID : Edm.Int32 [key] "Tax Agency"
PX.Objects.TX.TaxPeriodForReportShowing.TaxPeriodID : Edm.String [key] "Tax Period"
PX.Objects.TX.TaxPeriodForReportShowing.Status : Edm.String "Status"
PX.Objects.TX.TaxPeriodForReportShowing.EndDate : Edm.DateTimeOffset
PX.Objects.TX.TaxPeriodForReportShowing.RevisionID : Edm.Int32 "Revision ID"
PX.Objects.TX.TaxPeriodForReportShowing.TaxPeriodByVendorID -> PX.Objects.TX.TaxPeriod (TaxPeriodID=TaxPeriodID, OrganizationID=OrganizationID, VendorID=VendorID)

# PX.Objects.TX.TaxPlugin (EntityType)

Label: "Tax Plug-in"
Key: TaxPluginID
Entity sets: PX_Objects_TX_TaxPlugin, TaxPlugin
Non-filterable, non-selectable: NoteText

PX.Objects.TX.TaxPlugin.TaxPluginID : Edm.String [key] "Provider ID"
PX.Objects.TX.TaxPlugin.Description : Edm.String "Description"
PX.Objects.TX.TaxPlugin.PluginTypeName : Edm.String "Plug-In (Type)"
PX.Objects.TX.TaxPlugin.IsActive : Edm.Boolean [required] "Active"
PX.Objects.TX.TaxPlugin.TaxCalcMode : Edm.String "Default Tax Calculation Mode"
PX.Objects.TX.TaxPlugin.NoteID : Edm.Guid
PX.Objects.TX.TaxPlugin.NoteText : Edm.String "Note Text"
PX.Objects.TX.TaxPlugin.tstamp : Edm.Binary
PX.Objects.TX.TaxPlugin.CreatedByID : Edm.Guid "Created By"
PX.Objects.TX.TaxPlugin.CreatedByScreenID : Edm.String
PX.Objects.TX.TaxPlugin.CreatedDateTime : Edm.DateTimeOffset "Created On"
PX.Objects.TX.TaxPlugin.LastModifiedByID : Edm.Guid "Last Modified By"
PX.Objects.TX.TaxPlugin.LastModifiedByScreenID : Edm.String
PX.Objects.TX.TaxPlugin.LastModifiedDateTime : Edm.DateTimeOffset "Last Modified On"
PX.Objects.TX.TaxPlugin.UsersByCreatedByID -> PX.SM.Users (CreatedByID=PKID)
PX.Objects.TX.TaxPlugin.UsersByLastModifiedByID -> PX.SM.Users (LastModifiedByID=PKID)
PX.Objects.TX.TaxPlugin.TaxPluginDetailCollection -> Collection(PX.Objects.TX.TaxPluginDetail)
PX.Objects.TX.TaxPlugin.TaxPluginMappingCollection -> Collection(PX.Objects.TX.TaxPluginMapping)
PX.Objects.TX.TaxPlugin.TaxZoneCollection -> Collection(PX.Objects.TX.TaxZone)

# PX.Objects.TX.TaxPluginDetail (EntityType)

Label: "Tax Plug-in Details"
Key: SettingID, TaxPluginID
Entity sets: PX_Objects_TX_TaxPluginDetail, TaxPluginDetails, TaxPluginDetail

PX.Objects.TX.TaxPluginDetail.TaxPluginID : Edm.String [key]
PX.Objects.TX.TaxPluginDetail.SettingID : Edm.String [key] "ID"
PX.Objects.TX.TaxPluginDetail.SortOrder : Edm.Int32
PX.Objects.TX.TaxPluginDetail.Description : Edm.String "Description"
PX.Objects.TX.TaxPluginDetail.Value : Edm.String "Value"
PX.Objects.TX.TaxPluginDetail.ControlTypeValue : Edm.Int32 [required] "Control Type"
PX.Objects.TX.TaxPluginDetail.ComboValuesStr : Edm.String
PX.Objects.TX.TaxPluginDetail.CreatedByID : Edm.Guid "Created By"
PX.Objects.TX.TaxPluginDetail.CreatedByScreenID : Edm.String
PX.Objects.TX.TaxPluginDetail.CreatedDateTime : Edm.DateTimeOffset
PX.Objects.TX.TaxPluginDetail.LastModifiedByID : Edm.Guid "Last Modified By"
PX.Objects.TX.TaxPluginDetail.LastModifiedByScreenID : Edm.String
PX.Objects.TX.TaxPluginDetail.LastModifiedDateTime : Edm.DateTimeOffset
PX.Objects.TX.TaxPluginDetail.tstamp : Edm.Binary
PX.Objects.TX.TaxPluginDetail.UsersByCreatedByID -> PX.SM.Users (CreatedByID=PKID)
PX.Objects.TX.TaxPluginDetail.UsersByLastModifiedByID -> PX.SM.Users (LastModifiedByID=PKID)
PX.Objects.TX.TaxPluginDetail.TaxPluginByTaxPluginID -> PX.Objects.TX.TaxPlugin (TaxPluginID=TaxPluginID)

# PX.Objects.TX.TaxPluginMapping (EntityType)

Label: "Tax Plug-in Mapping"
Key: BranchID, TaxPluginID
Entity sets: PX_Objects_TX_TaxPluginMapping, TaxPluginMapping

PX.Objects.TX.TaxPluginMapping.TaxPluginID : Edm.String [key] "Tax Plug-in"
PX.Objects.TX.TaxPluginMapping.BranchID : Edm.Int32 [key] "Branch"
PX.Objects.TX.TaxPluginMapping.CompanyCode : Edm.String "Company Code"
PX.Objects.TX.TaxPluginMapping.ExternalCompanyID : Edm.String
PX.Objects.TX.TaxPluginMapping.CreatedByID : Edm.Guid "Created By"
PX.Objects.TX.TaxPluginMapping.CreatedByScreenID : Edm.String
PX.Objects.TX.TaxPluginMapping.CreatedDateTime : Edm.DateTimeOffset
PX.Objects.TX.TaxPluginMapping.LastModifiedByID : Edm.Guid "Last Modified By"
PX.Objects.TX.TaxPluginMapping.LastModifiedByScreenID : Edm.String
PX.Objects.TX.TaxPluginMapping.LastModifiedDateTime : Edm.DateTimeOffset
PX.Objects.TX.TaxPluginMapping.tstamp : Edm.Binary
PX.Objects.TX.TaxPluginMapping.BranchByBranchID -> PX.Objects.GL.Branch (BranchID=BranchID)
PX.Objects.TX.TaxPluginMapping.UsersByCreatedByID -> PX.SM.Users (CreatedByID=PKID)
PX.Objects.TX.TaxPluginMapping.UsersByLastModifiedByID -> PX.SM.Users (LastModifiedByID=PKID)
PX.Objects.TX.TaxPluginMapping.TaxPluginByTaxPluginID -> PX.Objects.TX.TaxPlugin (TaxPluginID=TaxPluginID)

# PX.Objects.TX.TaxReport (EntityType)

Label: "Tax Report"
Key: RevisionID, VendorID
Entity sets: PX_Objects_TX_TaxReport, TaxReport
Non-filterable, non-selectable: ShowNoTemp, NoteText, NotePopupText

PX.Objects.TX.TaxReport.VendorID : Edm.Int32 [key] "Tax Agency"
PX.Objects.TX.TaxReport.RevisionID : Edm.Int32 [key] "Report Version"
PX.Objects.TX.TaxReport.ValidFrom : Edm.DateTimeOffset "Valid From"
PX.Objects.TX.TaxReport.ValidTo : Edm.DateTimeOffset "Valid To"
PX.Objects.TX.TaxReport.ShowNoTemp : Edm.Boolean "Show Tax Zones"
PX.Objects.TX.TaxReport.LineCntr : Edm.Int32
PX.Objects.TX.TaxReport.NoteID : Edm.Guid
PX.Objects.TX.TaxReport.NoteText : Edm.String "Note Text"
PX.Objects.TX.TaxReport.NotePopupText : Edm.String "Note Text"
PX.Objects.TX.TaxReport.CreatedByID : Edm.Guid "Created By"
PX.Objects.TX.TaxReport.CreatedByScreenID : Edm.String
PX.Objects.TX.TaxReport.CreatedDateTime : Edm.DateTimeOffset
PX.Objects.TX.TaxReport.LastModifiedByID : Edm.Guid "Last Modified By"
PX.Objects.TX.TaxReport.LastModifiedByScreenID : Edm.String
PX.Objects.TX.TaxReport.LastModifiedDateTime : Edm.DateTimeOffset
PX.Objects.TX.TaxReport.tstamp : Edm.Binary
PX.Objects.TX.TaxReport.VendorByVendorID -> PX.Objects.AP.Vendor (VendorID=BAccountID)
PX.Objects.TX.TaxReport.BAccountByVendorID -> PX.Objects.CR.BAccount (VendorID=BAccountID)
PX.Objects.TX.TaxReport.UsersByCreatedByID -> PX.SM.Users (CreatedByID=PKID)
PX.Objects.TX.TaxReport.UsersByLastModifiedByID -> PX.SM.Users (LastModifiedByID=PKID)
PX.Objects.TX.TaxReport.TaxTranCollection -> Collection(PX.Objects.TX.TaxTran)
PX.Objects.TX.TaxReport.TaxReportLineCollection -> Collection(PX.Objects.TX.TaxReportLine)

# PX.Objects.TX.TaxReportLine (EntityType)

Label: "Tax Report Line"
Key: LineNbr, TaxReportRevisionID, VendorID
Entity sets: PX_Objects_TX_TaxReportLine, TaxReportLine
Non-filterable, non-selectable: BucketSum

PX.Objects.TX.TaxReportLine.VendorID : Edm.Int32 [key]
PX.Objects.TX.TaxReportLine.TaxReportRevisionID : Edm.Int32 [key required] "Report Version"
PX.Objects.TX.TaxReportLine.LineNbr : Edm.Int32 [key] "Report Line Nbr."
PX.Objects.TX.TaxReportLine.LineType : Edm.String "Update With"
PX.Objects.TX.TaxReportLine.LineMult : Edm.Int16 [required] "Update Rule"
PX.Objects.TX.TaxReportLine.TaxZoneID : Edm.String "Tax Zone ID"
PX.Objects.TX.TaxReportLine.NetTax : Edm.Boolean [required] "Net Tax"
PX.Objects.TX.TaxReportLine.TempLine : Edm.Boolean [required] "Detail by Tax Zones"
PX.Objects.TX.TaxReportLine.TempLineNbr : Edm.Int32 "Parent Line"
PX.Objects.TX.TaxReportLine.Descr : Edm.String "Description"
PX.Objects.TX.TaxReportLine.ReportLineNbr : Edm.String "Tax Box Number"
PX.Objects.TX.TaxReportLine.BucketSum : Edm.String "Calc. Rule"
PX.Objects.TX.TaxReportLine.HideReportLine : Edm.Boolean [required] "Hide Report Line"
PX.Objects.TX.TaxReportLine.SortOrder : Edm.Int32 "Report Line Order"
PX.Objects.TX.TaxReportLine.CreatedByID : Edm.Guid "Created By"
PX.Objects.TX.TaxReportLine.CreatedByScreenID : Edm.String
PX.Objects.TX.TaxReportLine.CreatedDateTime : Edm.DateTimeOffset
PX.Objects.TX.TaxReportLine.LastModifiedByID : Edm.Guid "Last Modified By"
PX.Objects.TX.TaxReportLine.LastModifiedByScreenID : Edm.String
PX.Objects.TX.TaxReportLine.LastModifiedDateTime : Edm.DateTimeOffset
PX.Objects.TX.TaxReportLine.tstamp : Edm.Binary
PX.Objects.TX.TaxReportLine.VendorByVendorID -> PX.Objects.AP.Vendor (VendorID=BAccountID)
PX.Objects.TX.TaxReportLine.UsersByCreatedByID -> PX.SM.Users (CreatedByID=PKID)
PX.Objects.TX.TaxReportLine.UsersByLastModifiedByID -> PX.SM.Users (LastModifiedByID=PKID)
PX.Objects.TX.TaxReportLine.TaxReportByTaxReportRevisionID -> PX.Objects.TX.TaxReport (VendorID=VendorID, TaxReportRevisionID=RevisionID)
PX.Objects.TX.TaxReportLine.TaxZoneByTaxZoneID -> PX.Objects.TX.TaxZone (TaxZoneID=TaxZoneID)
PX.Objects.TX.TaxReportLine.TaxBucketLineCollection -> Collection(PX.Objects.TX.TaxBucketLine)

# PX.Objects.TX.TaxReportSummary (EntityType)

Label: "Tax Report Summary"
Key: BranchID, LineNbr, RevisionID
Entity sets: PX_Objects_TX_TaxReportSummary, TaxReportSummary

PX.Objects.TX.TaxReportSummary.LineNbr : Edm.Int32 [key]
PX.Objects.TX.TaxReportSummary.LineMult : Edm.Int16
PX.Objects.TX.TaxReportSummary.LineType : Edm.String
PX.Objects.TX.TaxReportSummary.TaxPeriodID : Edm.String
PX.Objects.TX.TaxReportSummary.VendorID : Edm.Int32 "Vendor"
PX.Objects.TX.TaxReportSummary.RevisionID : Edm.Int32 [key] "Revision ID"
PX.Objects.TX.TaxReportSummary.BranchID : Edm.Int32 [key] "Branch"
PX.Objects.TX.TaxReportSummary.FiledAmt : Edm.Decimal "Amount"
PX.Objects.TX.TaxReportSummary.UnfiledAmt : Edm.Decimal "Amount"
PX.Objects.TX.TaxReportSummary.ReportFiledAmt : Edm.Decimal "Amount"
PX.Objects.TX.TaxReportSummary.ReportUnfiledAmt : Edm.Decimal "Amount"

# PX.Objects.TX.TaxRev (EntityType)

Label: "Tax Revision"
Key: RevisionID, TaxID
Entity sets: PX_Objects_TX_TaxRev, TaxRevision, TaxRev

PX.Objects.TX.TaxRev.TaxID : Edm.String [key] "Tax ID"
PX.Objects.TX.TaxRev.TaxVendorID : Edm.Int32
PX.Objects.TX.TaxRev.RevisionID : Edm.Int32 [key] "RevisionID"
PX.Objects.TX.TaxRev.StartDate : Edm.DateTimeOffset [required] "Start Date"
PX.Objects.TX.TaxRev.EndDate : Edm.DateTimeOffset [required]
PX.Objects.TX.TaxRev.TaxRate : Edm.Decimal "Tax Rate"
PX.Objects.TX.TaxRev.NonDeductibleTaxRate : Edm.Decimal "Deductible Tax Rate"
PX.Objects.TX.TaxRev.TaxableMin : Edm.Decimal "Min. Taxable Amount"
PX.Objects.TX.TaxRev.TaxableMax : Edm.Decimal "Max. Taxable Amount"
PX.Objects.TX.TaxRev.Outdated : Edm.Boolean "Not Valid"
PX.Objects.TX.TaxRev.TaxType : Edm.String "Group Type"
PX.Objects.TX.TaxRev.TaxBucketID : Edm.Int32 "Reporting Group"
PX.Objects.TX.TaxRev.IsImported : Edm.Boolean [required]
PX.Objects.TX.TaxRev.CreatedByID : Edm.Guid "Created By"
PX.Objects.TX.TaxRev.CreatedByScreenID : Edm.String
PX.Objects.TX.TaxRev.CreatedDateTime : Edm.DateTimeOffset
PX.Objects.TX.TaxRev.LastModifiedByID : Edm.Guid "Last Modified By"
PX.Objects.TX.TaxRev.LastModifiedByScreenID : Edm.String
PX.Objects.TX.TaxRev.LastModifiedDateTime : Edm.DateTimeOffset
PX.Objects.TX.TaxRev.tstamp : Edm.Binary
PX.Objects.TX.TaxRev.VendorByTaxVendorID -> PX.Objects.AP.Vendor (TaxVendorID=BAccountID)
PX.Objects.TX.TaxRev.UsersByCreatedByID -> PX.SM.Users (CreatedByID=PKID)
PX.Objects.TX.TaxRev.UsersByLastModifiedByID -> PX.SM.Users (LastModifiedByID=PKID)
PX.Objects.TX.TaxRev.TaxByTaxID -> PX.Objects.TX.Tax (TaxID=TaxID)
PX.Objects.TX.TaxRev.TaxBucketByTaxBucketID -> PX.Objects.TX.TaxBucket (TaxVendorID=VendorID, TaxBucketID=BucketID)

# PX.Objects.TX.TaxTran (EntityType)

Label: "Tax Transaction"
Key: Module, RecordID
Entity sets: PX_Objects_TX_TaxTran, TaxTransaction, TaxTran
Non-filterable, non-selectable: CuryEffDate

PX.Objects.TX.TaxTran.CreatedByID : Edm.Guid "Created By"
PX.Objects.TX.TaxTran.CreatedByScreenID : Edm.String
PX.Objects.TX.TaxTran.CreatedDateTime : Edm.DateTimeOffset
PX.Objects.TX.TaxTran.LastModifiedByID : Edm.Guid "Last Modified By"
PX.Objects.TX.TaxTran.LastModifiedByScreenID : Edm.String
PX.Objects.TX.TaxTran.LastModifiedDateTime : Edm.DateTimeOffset
PX.Objects.TX.TaxTran.Module : Edm.String [key required] "Module"
PX.Objects.TX.TaxTran.TranType : Edm.String "Tran. Type"
PX.Objects.TX.TaxTran.RefNbr : Edm.String "Ref. Nbr."
PX.Objects.TX.TaxTran.LineRefNbr : Edm.String "Line Ref. Number"
PX.Objects.TX.TaxTran.OrigTranType : Edm.String "Orig. Tran. Type"
PX.Objects.TX.TaxTran.OrigRefNbr : Edm.String "Orig. Doc. Number"
PX.Objects.TX.TaxTran.LineNbr : Edm.Int32
PX.Objects.TX.TaxTran.Released : Edm.Boolean [required]
PX.Objects.TX.TaxTran.Voided : Edm.Boolean [required]
PX.Objects.TX.TaxTran.FinPeriodID : Edm.String
PX.Objects.TX.TaxTran.FinDate : Edm.DateTimeOffset
PX.Objects.TX.TaxTran.TaxPeriodID : Edm.String
PX.Objects.TX.TaxTran.TaxID : Edm.String "Tax ID"
PX.Objects.TX.TaxTran.RecordID : Edm.Int32 [key]
PX.Objects.TX.TaxTran.JurisType : Edm.String "Tax Jurisdiction Type"
PX.Objects.TX.TaxTran.JurisName : Edm.String "Tax Jurisdiction Name"
PX.Objects.TX.TaxTran.VendorID : Edm.Int32
PX.Objects.TX.TaxTran.RevisionID : Edm.Int32
PX.Objects.TX.TaxTran.BAccountID : Edm.Int32
PX.Objects.TX.TaxTran.TaxZoneID : Edm.String "Tax Zone"
PX.Objects.TX.TaxTran.TranDate : Edm.DateTimeOffset "Tran. Date"
PX.Objects.TX.TaxTran.TaxInvoiceNbr : Edm.String "Tax Invoice Nbr."
PX.Objects.TX.TaxTran.TaxInvoiceDate : Edm.DateTimeOffset "Tax Invoice Date"
PX.Objects.TX.TaxTran.TaxType : Edm.String
PX.Objects.TX.TaxTran.TaxBucketID : Edm.Int32
PX.Objects.TX.TaxTran.TaxRate : Edm.Decimal "Tax Rate"
PX.Objects.TX.TaxTran.CuryInfoID : Edm.Int64
PX.Objects.TX.TaxTran.CuryOrigTaxableAmt : Edm.Decimal "Orig. Taxable Amount"
PX.Objects.TX.TaxTran.OrigTaxableAmt : Edm.Decimal "Orig. Taxable Amount"
PX.Objects.TX.TaxTran.CuryTaxableAmt : Edm.Decimal "Taxable Amount"
PX.Objects.TX.TaxTran.TaxableAmt : Edm.Decimal "Taxable Amount"
PX.Objects.TX.TaxTran.CuryTaxAmt : Edm.Decimal "Tax Amount"
PX.Objects.TX.TaxTran.TaxAmt : Edm.Decimal "Tax Amount"
PX.Objects.TX.TaxTran.CuryTaxAmtSumm : Edm.Decimal [required]
PX.Objects.TX.TaxTran.TaxAmtSumm : Edm.Decimal [required]
PX.Objects.TX.TaxTran.CuryID : Edm.String "Currency"
PX.Objects.TX.TaxTran.ReportCuryID : Edm.String "Report Currency"
PX.Objects.TX.TaxTran.ReportCuryRateTypeID : Edm.String "Report Currency Rate Type"
PX.Objects.TX.TaxTran.ReportCuryEffDate : Edm.DateTimeOffset "Report Effective Date"
PX.Objects.TX.TaxTran.ReportCuryMultDiv : Edm.String "Report Mult Div"
PX.Objects.TX.TaxTran.ReportCuryRate : Edm.Decimal
PX.Objects.TX.TaxTran.ReportTaxableAmt : Edm.Decimal "Report Taxable Amount"
PX.Objects.TX.TaxTran.ReportTaxAmt : Edm.Decimal "Report Tax Amount"
PX.Objects.TX.TaxTran.NonDeductibleTaxRate : Edm.Decimal "Deductible Tax Rate"
PX.Objects.TX.TaxTran.ExpenseAmt : Edm.Decimal "Expense Amount"
PX.Objects.TX.TaxTran.CuryExpenseAmt : Edm.Decimal "Expense Amount"
PX.Objects.TX.TaxTran.CuryEffDate : Edm.DateTimeOffset
PX.Objects.TX.TaxTran.AdjdDocType : Edm.String
PX.Objects.TX.TaxTran.AdjdRefNbr : Edm.String
PX.Objects.TX.TaxTran.AdjNbr : Edm.Int32
PX.Objects.TX.TaxTran.Description : Edm.String "Description"
PX.Objects.TX.TaxTran.tstamp : Edm.Binary
PX.Objects.TX.TaxTran.CuryRetainedTaxableAmt : Edm.Decimal [required] "Retained Taxable Amount"
PX.Objects.TX.TaxTran.RetainedTaxableAmt : Edm.Decimal [required] "Retained Taxable Amount"
PX.Objects.TX.TaxTran.CuryRetainedTaxAmtSumm : Edm.Decimal [required]
PX.Objects.TX.TaxTran.RetainedTaxAmtSumm : Edm.Decimal [required]
PX.Objects.TX.TaxTran.CuryAdjustedTaxableAmt : Edm.Decimal [required] "Adj. Taxable Amount"
PX.Objects.TX.TaxTran.AdjustedTaxableAmt : Edm.Decimal [required]
PX.Objects.TX.TaxTran.CuryAdjustedTaxAmt : Edm.Decimal [required] "Adj. Tax Amount"
PX.Objects.TX.TaxTran.AdjustedTaxAmt : Edm.Decimal [required]
PX.Objects.TX.TaxTran.IsTaxInclusive : Edm.Boolean [required] "Tax Inclusive"
PX.Objects.TX.TaxTran.VendorByVendorID -> PX.Objects.AP.Vendor (VendorID=BAccountID)
PX.Objects.TX.TaxTran.VendorByBAccountID -> PX.Objects.AP.Vendor (BAccountID=BAccountID)
PX.Objects.TX.TaxTran.BAccountByBAccountID -> PX.Objects.CR.BAccount (BAccountID=BAccountID)
PX.Objects.TX.TaxTran.BAccountByVendorID -> PX.Objects.CR.BAccount (VendorID=BAccountID)
PX.Objects.TX.TaxTran.APRegisterByRefNbr -> PX.Objects.AP.APRegister (TranType=DocType, RefNbr=RefNbr)
PX.Objects.TX.TaxTran.ARRegisterByRefNbr -> PX.Objects.AR.ARRegister (TranType=DocType, RefNbr=RefNbr)
PX.Objects.TX.TaxTran.BranchByBranchID -> PX.Objects.GL.Branch
PX.Objects.TX.TaxTran.CurrencyInfoByCuryInfoID -> PX.Objects.CM.CurrencyInfo (CuryInfoID=CuryInfoID)
PX.Objects.TX.TaxTran.UsersByCreatedByID -> PX.SM.Users (CreatedByID=PKID)
PX.Objects.TX.TaxTran.UsersByLastModifiedByID -> PX.SM.Users (LastModifiedByID=PKID)
PX.Objects.TX.TaxTran.TaxByTaxID -> PX.Objects.TX.Tax (TaxID=TaxID)
PX.Objects.TX.TaxTran.TaxAdjustmentByRefNbr -> PX.Objects.TX.TaxAdjustment (TranType=DocType, RefNbr=RefNbr)
PX.Objects.TX.TaxTran.TaxBucketByTaxBucketID -> PX.Objects.TX.TaxBucket (VendorID=VendorID, TaxBucketID=BucketID)
PX.Objects.TX.TaxTran.TaxReportByRevisionID -> PX.Objects.TX.TaxReport (VendorID=VendorID, RevisionID=RevisionID)
PX.Objects.TX.TaxTran.TaxZoneByTaxZoneID -> PX.Objects.TX.TaxZone (TaxZoneID=TaxZoneID)
PX.Objects.TX.TaxTran.INUnitByTaxUOM -> PX.Objects.IN.INUnit
PX.Objects.TX.TaxTran.CurrencyByCuryID -> PX.Objects.CM.Currency (CuryID=CuryID)
PX.Objects.TX.TaxTran.CurrencyByReportCuryID -> PX.Objects.CM.Currency (ReportCuryID=CuryID)
PX.Objects.TX.TaxTran.CurrencyRateTypeByReportCuryRateTypeID -> PX.Objects.CM.CurrencyRateType (ReportCuryRateTypeID=CuryRateTypeID)
PX.Objects.TX.TaxTran.AccountByAccountID -> PX.Objects.GL.Account
PX.Objects.TX.TaxTran.SubBySubID -> PX.Objects.GL.Sub
PX.Objects.TX.TaxTran.CAAdjByRefNbr -> PX.Objects.CA.CAAdj (TranType=AdjTranType, RefNbr=AdjRefNbr)
PX.Objects.TX.TaxTran.CAExpenseByLineNbr -> PX.Objects.CA.CAExpense (RefNbr=RefNbr, LineNbr=LineNbr)
PX.Objects.TX.TaxTran.TaxPeriodByTaxPeriodID -> PX.Objects.TX.TaxPeriod (TaxPeriodID=TaxPeriodID)

# PX.Objects.TX.TaxTranReport (EntityType)

Label: "Tax Transaction for Report"
BaseType: PX.Objects.TX.TaxTran
Key: Module, RecordID (inherited from PX.Objects.TX.TaxTran)
Entity sets: PX_Objects_TX_TaxTranReport, TaxTransactionforReport, TaxTranReport
Non-filterable, non-selectable: Sign

PX.Objects.TX.TaxTranReport.TranTypeInvoiceDiscriminated : Edm.String "Tran. Type"
PX.Objects.TX.TaxTranReport.Sign : Edm.Decimal

# PX.Objects.TX.TaxYear (EntityType)

Label: "Tax Year"
Key: OrganizationID, VendorID, Year
Entity sets: PX_Objects_TX_TaxYear, TaxYear

PX.Objects.TX.TaxYear.OrganizationID : Edm.Int32 [key] "Company"
PX.Objects.TX.TaxYear.VendorID : Edm.Int32 [key] "Tax Agency"
PX.Objects.TX.TaxYear.Year : Edm.String [key] "Tax Year"
PX.Objects.TX.TaxYear.StartDate : Edm.DateTimeOffset "Start Date"
PX.Objects.TX.TaxYear.Filed : Edm.Boolean [required]
PX.Objects.TX.TaxYear.PeriodsCount : Edm.Int32
PX.Objects.TX.TaxYear.PlanPeriodsCount : Edm.Int32
PX.Objects.TX.TaxYear.TaxPeriodType : Edm.String "Tax Period Type"
PX.Objects.TX.TaxYear.tstamp : Edm.Binary
PX.Objects.TX.TaxYear.VendorByVendorID -> PX.Objects.AP.Vendor (VendorID=BAccountID)
PX.Objects.TX.TaxYear.BAccountByVendorID -> PX.Objects.CR.BAccount (VendorID=BAccountID)
PX.Objects.TX.TaxYear.OrganizationByOrganizationID -> PX.Objects.GL.DAC.Organization (OrganizationID=OrganizationID)
PX.Objects.TX.TaxYear.TaxPeriodCollection -> Collection(PX.Objects.TX.TaxPeriod)

# PX.Objects.TX.TaxZone (EntityType)

Label: "Tax Zone"
Key: TaxZoneID
Entity sets: PX_Objects_TX_TaxZone, TaxZone
Non-filterable, non-selectable: ShowTaxTabExpr, NoteText

PX.Objects.TX.TaxZone.TaxZoneID : Edm.String [key] "Tax Zone ID"
PX.Objects.TX.TaxZone.Descr : Edm.String "Description"
PX.Objects.TX.TaxZone.DfltTaxCategoryID : Edm.String "Default Tax Category"
PX.Objects.TX.TaxZone.IsImported : Edm.Boolean [required]
PX.Objects.TX.TaxZone.IsExternal : Edm.Boolean [required] "External Tax Provider"
PX.Objects.TX.TaxZone.TaxPluginID : Edm.String "Provider ID"
PX.Objects.TX.TaxZone.TaxVendorID : Edm.Int32 "Tax Agency ID"
PX.Objects.TX.TaxZone.ShowTaxTabExpr : Edm.Boolean "ShowTaxTabExpr"
PX.Objects.TX.TaxZone.TaxID : Edm.String "Tax ID"
PX.Objects.TX.TaxZone.MappingType : Edm.String "Tax Zone Is Based On"
PX.Objects.TX.TaxZone.CountryID : Edm.String "Country"
PX.Objects.TX.TaxZone.NoteID : Edm.Guid
PX.Objects.TX.TaxZone.NoteText : Edm.String "Note Text"
PX.Objects.TX.TaxZone.CreatedByID : Edm.Guid "Created By"
PX.Objects.TX.TaxZone.CreatedByScreenID : Edm.String
PX.Objects.TX.TaxZone.CreatedDateTime : Edm.DateTimeOffset
PX.Objects.TX.TaxZone.LastModifiedByID : Edm.Guid "Last Modified By"
PX.Objects.TX.TaxZone.LastModifiedByScreenID : Edm.String
PX.Objects.TX.TaxZone.LastModifiedDateTime : Edm.DateTimeOffset
PX.Objects.TX.TaxZone.ExternalAPTaxType : Edm.String "Calculate in AP"
PX.Objects.TX.TaxZone.VendorByTaxVendorID -> PX.Objects.AP.Vendor (TaxVendorID=BAccountID)
PX.Objects.TX.TaxZone.BAccountByTaxVendorID -> PX.Objects.CR.BAccount (TaxVendorID=BAccountID)
PX.Objects.TX.TaxZone.UsersByCreatedByID -> PX.SM.Users (CreatedByID=PKID)
PX.Objects.TX.TaxZone.UsersByLastModifiedByID -> PX.SM.Users (LastModifiedByID=PKID)
PX.Objects.TX.TaxZone.TaxByTaxID -> PX.Objects.TX.Tax (TaxID=TaxID)
PX.Objects.TX.TaxZone.TaxCategoryByDfltTaxCategoryID -> PX.Objects.TX.TaxCategory (DfltTaxCategoryID=TaxCategoryID)
PX.Objects.TX.TaxZone.TaxCategoryByTaxPluginID -> PX.Objects.TX.TaxCategory (TaxPluginID=TaxCategoryID)
PX.Objects.TX.TaxZone.TaxPluginByTaxPluginID -> PX.Objects.TX.TaxPlugin (TaxPluginID=TaxPluginID)
PX.Objects.TX.TaxZone.CountryByCountryID -> PX.Objects.CS.Country (CountryID=CountryID)
PX.Objects.TX.TaxZone.TaxTranCollection -> Collection(PX.Objects.TX.TaxTran)
PX.Objects.TX.TaxZone.SOTaxTranCollection -> Collection(PX.Objects.SO.SOTaxTran)
PX.Objects.TX.TaxZone.PMProjectCollection -> Collection(PX.Objects.PM.PMProject)
PX.Objects.TX.TaxZone.POTaxTranCollection -> Collection(PX.Objects.PO.POTaxTran)
PX.Objects.TX.TaxZone.ARInvoiceCollection -> Collection(PX.Objects.AR.ARInvoice)
PX.Objects.TX.TaxZone.APInvoiceCollection -> Collection(PX.Objects.AP.APInvoice)
PX.Objects.TX.TaxZone.ARCashSaleCollection -> Collection(PX.Objects.AR.Standalone.ARCashSale)
PX.Objects.TX.TaxZone.APQuickCheckCollection -> Collection(PX.Objects.AP.Standalone.APQuickCheck)
PX.Objects.TX.TaxZone.SOTaxCollection -> Collection(PX.Objects.SO.SOTax)
PX.Objects.TX.TaxZone.SOOrderCollection -> Collection(PX.Objects.SO.SOOrder)
PX.Objects.TX.TaxZone.POLandedCostTaxTranCollection -> Collection(PX.Objects.PO.POLandedCostTaxTran)
PX.Objects.TX.TaxZone.POTaxCollection -> Collection(PX.Objects.PO.POTax)
PX.Objects.TX.TaxZone.POOrderCollection -> Collection(PX.Objects.PO.POOrder)
PX.Objects.TX.TaxZone.LocationExtAddressCollection -> Collection(PX.Objects.CR.LocationExtAddress)
PX.Objects.TX.TaxZone.EPEmployeeClassCollection -> Collection(PX.Objects.EP.EPEmployeeClass)
PX.Objects.TX.TaxZone.EPExpenseClaimCollection -> Collection(PX.Objects.EP.EPExpenseClaim)
PX.Objects.TX.TaxZone.CABankTranCollection -> Collection(PX.Objects.CA.CABankTran)
PX.Objects.TX.TaxZone.EPExpenseClaimDetailsCollection -> Collection(PX.Objects.EP.EPExpenseClaimDetails)
PX.Objects.TX.TaxZone.SOLineCollection -> Collection(PX.Objects.SO.SOLine)
PX.Objects.TX.TaxZone.FSServiceOrderCollection -> Collection(PX.Objects.FS.FSServiceOrder)
PX.Objects.TX.TaxZone.FSAppointmentCollection -> Collection(PX.Objects.FS.FSAppointment)
PX.Objects.TX.TaxZone.SVTaxCollection -> Collection(PX.Objects.SV.SVTax)
PX.Objects.TX.TaxZone.PMChangeOrderCollection -> Collection(PX.Objects.PM.PMChangeOrder)
PX.Objects.TX.TaxZone.LocationCollection -> Collection(PX.Objects.CR.Location)
PX.Objects.TX.TaxZone.VendorClassCollection -> Collection(PX.Objects.AP.VendorClass)
PX.Objects.TX.TaxZone.GLTranDocCollection -> Collection(PX.Objects.GL.GLTranDoc)
PX.Objects.TX.TaxZone.TaxReportLineCollection -> Collection(PX.Objects.TX.TaxReportLine)
PX.Objects.TX.TaxZone.TaxZoneAddressMappingCollection -> Collection(PX.Objects.TX.TaxZoneAddressMapping)
PX.Objects.TX.TaxZone.TaxZoneDetCollection -> Collection(PX.Objects.TX.TaxZoneDet)
PX.Objects.TX.TaxZone.POLandedCostDocCollection -> Collection(PX.Objects.PO.POLandedCostDoc)
PX.Objects.TX.TaxZone.POLandedCostDocSCollection -> Collection(PX.Objects.PO.POLandedCostDocS)
PX.Objects.TX.TaxZone.PMChangeRequestCollection -> Collection(PX.Objects.PM.PMChangeRequest)
PX.Objects.TX.TaxZone.PMProformaCollection -> Collection(PX.Objects.PM.PMProforma)
PX.Objects.TX.TaxZone.CAAdjCollection -> Collection(PX.Objects.CA.CAAdj)
PX.Objects.TX.TaxZone.CAExpenseCollection -> Collection(PX.Objects.CA.CAExpense)
PX.Objects.TX.TaxZone.CashAccountETDetailCollection -> Collection(PX.Objects.CA.CashAccountETDetail)
PX.Objects.TX.TaxZone.CROpportunityRevisionCollection -> Collection(PX.Objects.CR.Standalone.CROpportunityRevision)
PX.Objects.TX.TaxZone.CustomerClassCollection -> Collection(PX.Objects.AR.CustomerClass)
PX.Objects.TX.TaxZone.BCAmazonTaxMappingCollection -> Collection(PX.Commerce.Amazon.BCAmazonTaxMapping)
PX.Objects.TX.TaxZone.BCBindingExtCollection -> Collection(PX.Commerce.Objects.BCBindingExt)
PX.Objects.TX.TaxZone.SVOrderCollection -> Collection(PX.Objects.SV.SVOrder)
PX.Objects.TX.TaxZone.SVServiceLocationCollection -> Collection(PX.Objects.SV.SVServiceLocation)
PX.Objects.TX.TaxZone.CROpportunityCollection -> Collection(PX.Objects.CR.CROpportunity)
PX.Objects.TX.TaxZone.PMQuoteCollection -> Collection(PX.Objects.PM.PMQuote)
PX.Objects.TX.TaxZone.CRQuoteCollection -> Collection(PX.Objects.CR.CRQuote)
PX.Objects.TX.TaxZone.POLineRSCollection -> Collection(PX.Objects.PO.POLineRS)

# PX.Objects.TX.TaxZoneAddressMapping (EntityType)

Label: "Tax Zone Address Mapping"
Key: CountryID, FromPostalCode, StateID, TaxZoneID
Entity sets: PX_Objects_TX_TaxZoneAddressMapping, TaxZoneAddressMapping
Non-filterable, non-selectable: Description

PX.Objects.TX.TaxZoneAddressMapping.TaxZoneID : Edm.String [key]
PX.Objects.TX.TaxZoneAddressMapping.CountryID : Edm.String [key] "Country"
PX.Objects.TX.TaxZoneAddressMapping.StateID : Edm.String [key required] "State"
PX.Objects.TX.TaxZoneAddressMapping.Description : Edm.String "Name"
PX.Objects.TX.TaxZoneAddressMapping.FromPostalCode : Edm.String [key required] "From Postal Code"
PX.Objects.TX.TaxZoneAddressMapping.ToPostalCode : Edm.String "To Postal Code"
PX.Objects.TX.TaxZoneAddressMapping.ToPostalCodeSuffixed : Edm.String
PX.Objects.TX.TaxZoneAddressMapping.tstamp : Edm.Binary
PX.Objects.TX.TaxZoneAddressMapping.CreatedByID : Edm.Guid "Created By"
PX.Objects.TX.TaxZoneAddressMapping.CreatedByScreenID : Edm.String
PX.Objects.TX.TaxZoneAddressMapping.CreatedDateTime : Edm.DateTimeOffset
PX.Objects.TX.TaxZoneAddressMapping.LastModifiedByID : Edm.Guid "Last Modified By"
PX.Objects.TX.TaxZoneAddressMapping.LastModifiedByScreenID : Edm.String
PX.Objects.TX.TaxZoneAddressMapping.LastModifiedDateTime : Edm.DateTimeOffset
PX.Objects.TX.TaxZoneAddressMapping.UsersByCreatedByID -> PX.SM.Users (CreatedByID=PKID)
PX.Objects.TX.TaxZoneAddressMapping.UsersByLastModifiedByID -> PX.SM.Users (LastModifiedByID=PKID)
PX.Objects.TX.TaxZoneAddressMapping.TaxZoneByTaxZoneID -> PX.Objects.TX.TaxZone (TaxZoneID=TaxZoneID)
PX.Objects.TX.TaxZoneAddressMapping.CountryByCountryID -> PX.Objects.CS.Country (CountryID=CountryID)
PX.Objects.TX.TaxZoneAddressMapping.StateByCountryID -> PX.Objects.CS.State (StateID=StateID, CountryID=CountryID)

# PX.Objects.TX.TaxZoneDet (EntityType)

Label: "Tax Zone Detail"
Key: TaxID, TaxZoneID
Entity sets: PX_Objects_TX_TaxZoneDet, TaxZoneDetail, TaxZoneDet

PX.Objects.TX.TaxZoneDet.TaxZoneID : Edm.String [key] "Tax Zone ID"
PX.Objects.TX.TaxZoneDet.TaxID : Edm.String [key] "Tax ID"
PX.Objects.TX.TaxZoneDet.IsImported : Edm.Boolean [required]
PX.Objects.TX.TaxZoneDet.CreatedByID : Edm.Guid "Created By"
PX.Objects.TX.TaxZoneDet.CreatedByScreenID : Edm.String
PX.Objects.TX.TaxZoneDet.CreatedDateTime : Edm.DateTimeOffset
PX.Objects.TX.TaxZoneDet.LastModifiedByID : Edm.Guid "Last Modified By"
PX.Objects.TX.TaxZoneDet.LastModifiedByScreenID : Edm.String
PX.Objects.TX.TaxZoneDet.LastModifiedDateTime : Edm.DateTimeOffset
PX.Objects.TX.TaxZoneDet.UsersByCreatedByID -> PX.SM.Users (CreatedByID=PKID)
PX.Objects.TX.TaxZoneDet.UsersByLastModifiedByID -> PX.SM.Users (LastModifiedByID=PKID)
PX.Objects.TX.TaxZoneDet.TaxByTaxID -> PX.Objects.TX.Tax (TaxID=TaxID)
PX.Objects.TX.TaxZoneDet.TaxZoneByTaxZoneID -> PX.Objects.TX.TaxZone (TaxZoneID=TaxZoneID)

# PX.Objects.TX.TXImportFileData (EntityType)

Key: RecordID
Entity sets: PX_Objects_TX_TXImportFileData

PX.Objects.TX.TXImportFileData.RecordID : Edm.Int32 [key] "RecordID"
PX.Objects.TX.TXImportFileData.StateCode : Edm.String "StateCode"
PX.Objects.TX.TXImportFileData.StateName : Edm.String "StateName"
PX.Objects.TX.TXImportFileData.CityName : Edm.String "CityName"
PX.Objects.TX.TXImportFileData.CountyName : Edm.String "CountyName"
PX.Objects.TX.TXImportFileData.ZipCode : Edm.String "ZipCode"
PX.Objects.TX.TXImportFileData.Origin : Edm.String "Origin"
PX.Objects.TX.TXImportFileData.TaxFreight : Edm.String "TaxFreight"
PX.Objects.TX.TXImportFileData.TaxServices : Edm.String "TaxServices"
PX.Objects.TX.TXImportFileData.SignatureCode : Edm.String "SignatureCode"
PX.Objects.TX.TXImportFileData.StateSalesTaxRate : Edm.Decimal [required] "StateSalesTaxRate"
PX.Objects.TX.TXImportFileData.StateSalesTaxRateEffectiveDate : Edm.DateTimeOffset "StateSalesTaxRateEffectiveDate"
PX.Objects.TX.TXImportFileData.StateSalesTaxPreviousRate : Edm.Decimal [required] "StateSalesTaxPreviousRate"
PX.Objects.TX.TXImportFileData.StateUseTaxRate : Edm.Decimal [required] "StateUseTaxRate"
PX.Objects.TX.TXImportFileData.StateUseTaxRateEffectiveDate : Edm.DateTimeOffset "StateUseTaxRateEffectiveDate"
PX.Objects.TX.TXImportFileData.StateUseTaxPreviousRate : Edm.Decimal [required] "StateUseTaxPreviousRate"
PX.Objects.TX.TXImportFileData.StateTaxableMaximum : Edm.Decimal [required] "StateTaxableMaximum"
PX.Objects.TX.TXImportFileData.StateTaxOverMaximumRate : Edm.Decimal [required] "StateTaxOverMaximumRate"
PX.Objects.TX.TXImportFileData.SignatureCodeCity : Edm.String "SignatureCodeCity"
PX.Objects.TX.TXImportFileData.CityTaxCodeAssignedByState : Edm.String "CityTaxCodeAssignedByState"
PX.Objects.TX.TXImportFileData.CityLocalRegister : Edm.String "CityLocalRegister"
PX.Objects.TX.TXImportFileData.CitySalesTaxRate : Edm.Decimal [required] "CitySalesTaxRate"
PX.Objects.TX.TXImportFileData.CitySalesTaxRateEffectiveDate : Edm.DateTimeOffset "CitySalesTaxRateEffectiveDate"
PX.Objects.TX.TXImportFileData.CitySalesTaxPreviousRate : Edm.Decimal [required] "CitySalesTaxPreviousRate"
PX.Objects.TX.TXImportFileData.CityUseTaxRate : Edm.Decimal [required] "CityUseTaxRate"
PX.Objects.TX.TXImportFileData.CityUseTaxRateEffectiveDate : Edm.DateTimeOffset "CityUseTaxRateEffectiveDate"
PX.Objects.TX.TXImportFileData.CityUseTaxPreviousRate : Edm.Decimal [required] "CityUseTaxPreviousRate"
PX.Objects.TX.TXImportFileData.CityTaxableMaximum : Edm.Decimal [required] "CityTaxableMaximum"
PX.Objects.TX.TXImportFileData.CityTaxOverMaximumRate : Edm.Decimal [required] "CityTaxOverMaximumRate"
PX.Objects.TX.TXImportFileData.SignatureCodeCounty : Edm.String "SignatureCodeCounty"
PX.Objects.TX.TXImportFileData.CountyTaxCodeAssignedByState : Edm.String "CountyTaxCodeAssignedByState"
PX.Objects.TX.TXImportFileData.CountyLocalRegister : Edm.String "CountyLocalRegister"
PX.Objects.TX.TXImportFileData.CountySalesTaxRate : Edm.Decimal [required] "CountySalesTaxRate"
PX.Objects.TX.TXImportFileData.CountySalesTaxRateEffectiveDate : Edm.DateTimeOffset "CountySalesTaxRateEffectiveDate"
PX.Objects.TX.TXImportFileData.CountySalesTaxPreviousRate : Edm.Decimal [required] "CountySalesTaxPreviousRate"
PX.Objects.TX.TXImportFileData.CountyUseTaxRate : Edm.Decimal [required] "CountyUseTaxRate"
PX.Objects.TX.TXImportFileData.CountyUseTaxRateEffectiveDate : Edm.DateTimeOffset "CountyUseTaxRateEffectiveDate"
PX.Objects.TX.TXImportFileData.CountyUseTaxPreviousRate : Edm.Decimal [required] "CountyUseTaxPreviousRate"
PX.Objects.TX.TXImportFileData.CountyTaxableMaximum : Edm.Decimal [required] "CountyTaxableMaximum"
PX.Objects.TX.TXImportFileData.CountyTaxOverMaximumRate : Edm.Decimal [required] "CountyTaxOverMaximumRate"
PX.Objects.TX.TXImportFileData.SignatureCodeTransit : Edm.String "SignatureCodeTransit"
PX.Objects.TX.TXImportFileData.TransitTaxCodeAssignedByState : Edm.String "TransitTaxCodeAssignedByState"
PX.Objects.TX.TXImportFileData.TransitSalesTaxRate : Edm.Decimal [required] "TransitSalesTaxRate"
PX.Objects.TX.TXImportFileData.TransitSalesTaxRateEffectiveDate : Edm.DateTimeOffset "TransitSalesTaxRateEffectiveDate"
PX.Objects.TX.TXImportFileData.TransitSalesTaxPreviousRate : Edm.Decimal [required] "TransitSalesTaxPreviousRate"
PX.Objects.TX.TXImportFileData.TransitUseTaxRate : Edm.Decimal [required] "TransitUseTaxRate"
PX.Objects.TX.TXImportFileData.TransitUseTaxRateEffectiveDate : Edm.DateTimeOffset "TransitUseTaxRateEffectiveDate"
PX.Objects.TX.TXImportFileData.TransitUseTaxPreviousRate : Edm.Decimal [required] "TransitUseTaxPreviousRate"
PX.Objects.TX.TXImportFileData.TransitTaxIsCity : Edm.String "TransitTaxIsCity"
PX.Objects.TX.TXImportFileData.SignatureCodeOther1 : Edm.String "SignatureCodeOther1"
PX.Objects.TX.TXImportFileData.OtherTaxCode1AssignedByState : Edm.String "OtherTaxCode1AssignedByState"
PX.Objects.TX.TXImportFileData.Other1SalesTaxRate : Edm.Decimal [required] "Other1SalesTaxRate"
PX.Objects.TX.TXImportFileData.Other1SalesTaxRateEffectiveDate : Edm.DateTimeOffset "Other1SalesTaxRateEffectiveDate"
PX.Objects.TX.TXImportFileData.Other1SalesTaxPreviousRate : Edm.Decimal [required] "Other1SalesTaxPreviousRate"
PX.Objects.TX.TXImportFileData.Other1UseTaxRate : Edm.Decimal [required] "Other1UseTaxRate"
PX.Objects.TX.TXImportFileData.Other1UseTaxRateEffectiveDate : Edm.DateTimeOffset "Other1UseTaxRateEffectiveDate"
PX.Objects.TX.TXImportFileData.Other1UseTaxPreviousRate : Edm.Decimal [required] "Other1UseTaxPreviousRate"
PX.Objects.TX.TXImportFileData.Other1TaxIsCity : Edm.String "Other1TaxIsCity"
PX.Objects.TX.TXImportFileData.SignatureCodeOther2 : Edm.String "SignatureCodeOther2"
PX.Objects.TX.TXImportFileData.OtherTaxCode2AssignedByState : Edm.String "OtherTaxCode2AssignedByState"
PX.Objects.TX.TXImportFileData.Other2SalesTaxRate : Edm.Decimal [required] "Other2SalesTaxRate"
PX.Objects.TX.TXImportFileData.Other2SalesTaxRateEffectiveDate : Edm.DateTimeOffset "Other2SalesTaxRateEffectiveDate"
PX.Objects.TX.TXImportFileData.Other2SalesTaxPreviousRate : Edm.Decimal [required] "Other2SalesTaxPreviousRate"
PX.Objects.TX.TXImportFileData.Other2UseTaxRate : Edm.Decimal [required] "Other2UseTaxRate"
PX.Objects.TX.TXImportFileData.Other2UseTaxRateEffectiveDate : Edm.DateTimeOffset "Other2UseTaxRateEffectiveDate"
PX.Objects.TX.TXImportFileData.Other2UseTaxPreviousRate : Edm.Decimal [required] "Other2UseTaxPreviousRate"
PX.Objects.TX.TXImportFileData.Other2TaxIsCity : Edm.String "Other2TaxIsCity"
PX.Objects.TX.TXImportFileData.SignatureCodeOther3 : Edm.String "SignatureCodeOther3"
PX.Objects.TX.TXImportFileData.OtherTaxCode3AssignedByState : Edm.String "OtherTaxCode3AssignedByState"
PX.Objects.TX.TXImportFileData.Other3SalesTaxRate : Edm.Decimal [required] "Other3SalesTaxRate"
PX.Objects.TX.TXImportFileData.Other3SalesTaxRateEffectiveDate : Edm.DateTimeOffset "Other3SalesTaxRateEffectiveDate"
PX.Objects.TX.TXImportFileData.Other3SalesTaxPreviousRate : Edm.Decimal [required] "Other3SalesTaxPreviousRate"
PX.Objects.TX.TXImportFileData.Other3UseTaxRate : Edm.Decimal [required] "Other3UseTaxRate"
PX.Objects.TX.TXImportFileData.Other3UseTaxRateEffectiveDate : Edm.DateTimeOffset "Other3UseTaxRateEffectiveDate"
PX.Objects.TX.TXImportFileData.Other3UseTaxPreviousRate : Edm.Decimal [required] "Other3UseTaxPreviousRate"
PX.Objects.TX.TXImportFileData.Other3TaxIsCity : Edm.String "Other3TaxIsCity"
PX.Objects.TX.TXImportFileData.SignatureCodeOther4 : Edm.String "SignatureCodeOther4"
PX.Objects.TX.TXImportFileData.OtherTaxCode4AssignedByState : Edm.String "OtherTaxCode4AssignedByState"
PX.Objects.TX.TXImportFileData.Other4SalesTaxRate : Edm.Decimal [required] "Other4SalesTaxRate"
PX.Objects.TX.TXImportFileData.Other4SalesTaxRateEffectiveDate : Edm.DateTimeOffset "Other4SalesTaxRateEffectiveDate"
PX.Objects.TX.TXImportFileData.Other4SalesTaxPreviousRate : Edm.Decimal [required] "Other4SalesTaxPreviousRate"
PX.Objects.TX.TXImportFileData.Other4UseTaxRate : Edm.Decimal [required] "Other4UseTaxRate"
PX.Objects.TX.TXImportFileData.Other4UseTaxRateEffectiveDate : Edm.DateTimeOffset "Other4UseTaxRateEffectiveDate"
PX.Objects.TX.TXImportFileData.Other4UseTaxPreviousRate : Edm.Decimal [required] "Other4UseTaxPreviousRate"
PX.Objects.TX.TXImportFileData.Other4TaxIsCity : Edm.String "Other4TaxIsCity"
PX.Objects.TX.TXImportFileData.CombinedSalesTaxRate : Edm.Decimal [required] "CombinedSalesTaxRate"
PX.Objects.TX.TXImportFileData.CombinedSalesTaxRateEffectiveDate : Edm.DateTimeOffset "CombinedSalesTaxRateEffectiveDate"
PX.Objects.TX.TXImportFileData.CombinedSalesTaxPreviousRate : Edm.Decimal [required] "CombinedSalesTaxPreviousRate"
PX.Objects.TX.TXImportFileData.CombinedUseTaxRate : Edm.Decimal [required] "CombinedUseTaxRate"
PX.Objects.TX.TXImportFileData.CombinedUseTaxRateEffectiveDate : Edm.DateTimeOffset "CombinedUseTaxRateEffectiveDate"
PX.Objects.TX.TXImportFileData.CombinedUseTaxPreviousRate : Edm.Decimal [required] "CombinedUseTaxPreviousRate"
PX.Objects.TX.TXImportFileData.DateLastUpdated : Edm.DateTimeOffset "DateLastUpdated"
PX.Objects.TX.TXImportFileData.DeleteCode : Edm.String "DeleteCode"

# PX.Objects.TX.TXImportSettings (EntityType)

Singletons: PX_Objects_TX_TXImportSettings

PX.Objects.TX.TXImportSettings.TaxableCategoryID : Edm.String "Tax Taxable Category"
PX.Objects.TX.TXImportSettings.FreightCategoryID : Edm.String "Tax Freight Category"
PX.Objects.TX.TXImportSettings.ServiceCategoryID : Edm.String "Tax Service Category"
PX.Objects.TX.TXImportSettings.LaborCategoryID : Edm.String "Tax Labor Category"
PX.Objects.TX.TXImportSettings.TaxCategoryByTaxableCategoryID -> PX.Objects.TX.TaxCategory (TaxableCategoryID=TaxCategoryID)
PX.Objects.TX.TXImportSettings.TaxCategoryByFreightCategoryID -> PX.Objects.TX.TaxCategory (FreightCategoryID=TaxCategoryID)
PX.Objects.TX.TXImportSettings.TaxCategoryByServiceCategoryID -> PX.Objects.TX.TaxCategory (ServiceCategoryID=TaxCategoryID)
PX.Objects.TX.TXImportSettings.TaxCategoryByLaborCategoryID -> PX.Objects.TX.TaxCategory (LaborCategoryID=TaxCategoryID)

# PX.Objects.TX.TXImportState (EntityType)

Key: StateCode
Entity sets: PX_Objects_TX_TXImportState

PX.Objects.TX.TXImportState.StateCode : Edm.String [key] "State Code"
PX.Objects.TX.TXImportState.StateName : Edm.String "State Name"
PX.Objects.TX.TXImportState.CreatedByID : Edm.Guid "Created By"
PX.Objects.TX.TXImportState.CreatedByScreenID : Edm.String
PX.Objects.TX.TXImportState.CreatedDateTime : Edm.DateTimeOffset
PX.Objects.TX.TXImportState.LastModifiedByID : Edm.Guid "Last Modified By"
PX.Objects.TX.TXImportState.LastModifiedByScreenID : Edm.String
PX.Objects.TX.TXImportState.LastModifiedDateTime : Edm.DateTimeOffset
PX.Objects.TX.TXImportState.tstamp : Edm.Binary
PX.Objects.TX.TXImportState.UsersByCreatedByID -> PX.SM.Users (CreatedByID=PKID)
PX.Objects.TX.TXImportState.UsersByLastModifiedByID -> PX.SM.Users (LastModifiedByID=PKID)
PX.Objects.TX.TXImportState.AccountByAccountID -> PX.Objects.GL.Account
PX.Objects.TX.TXImportState.SubBySubID -> PX.Objects.GL.Sub

# PX.Objects.TX.TXImportZipFileData (EntityType)

Key: RecordID
Entity sets: PX_Objects_TX_TXImportZipFileData

PX.Objects.TX.TXImportZipFileData.RecordID : Edm.Int32 [key]
PX.Objects.TX.TXImportZipFileData.ZipCode : Edm.String "Zip Code"
PX.Objects.TX.TXImportZipFileData.StateCode : Edm.String "State"
PX.Objects.TX.TXImportZipFileData.CountyName : Edm.String "Country Name"
PX.Objects.TX.TXImportZipFileData.Plus4PortionOfZipCode : Edm.Int32 [required] "Zip Plus Min."
PX.Objects.TX.TXImportZipFileData.Plus4PortionOfZipCode2 : Edm.Int32 [required] "Zip Plus Max."

# PX.Objects.TX.TXSetup (EntityType)

Label: "Tax Preferences"
Singletons: PX_Objects_TX_TXSetup, TaxPreferences, TXSetup

PX.Objects.TX.TXSetup.TaxAdjustmentNumberingID : Edm.String "Tax Adjustment Numbering Sequence"
PX.Objects.TX.TXSetup.ECMProvider : Edm.String "ECM Provider"
PX.Objects.TX.TXSetup.tstamp : Edm.Binary
PX.Objects.TX.TXSetup.CreatedByID : Edm.Guid "Created By"
PX.Objects.TX.TXSetup.CreatedByScreenID : Edm.String
PX.Objects.TX.TXSetup.CreatedDateTime : Edm.DateTimeOffset
PX.Objects.TX.TXSetup.LastModifiedByID : Edm.Guid "Last Modified By"
PX.Objects.TX.TXSetup.LastModifiedByScreenID : Edm.String
PX.Objects.TX.TXSetup.LastModifiedDateTime : Edm.DateTimeOffset
PX.Objects.TX.TXSetup.UsersByCreatedByID -> PX.SM.Users (CreatedByID=PKID)
PX.Objects.TX.TXSetup.UsersByLastModifiedByID -> PX.SM.Users (LastModifiedByID=PKID)
PX.Objects.TX.TXSetup.NumberingByTaxAdjustmentNumberingID -> PX.Objects.CS.Numbering (TaxAdjustmentNumberingID=NumberingID)
PX.Objects.TX.TXSetup.AccountByTaxRoundingGainAcctID -> PX.Objects.GL.Account
PX.Objects.TX.TXSetup.AccountByTaxRoundingLossAcctID -> PX.Objects.GL.Account
PX.Objects.TX.TXSetup.SubByTaxRoundingGainSubID -> PX.Objects.GL.Sub
PX.Objects.TX.TXSetup.SubByTaxRoundingLossSubID -> PX.Objects.GL.Sub

# PX.Objects.WZ.PendingWZScenario (EntityType)

Label: "Wizard Scenario"
Key: ScenarioID
Entity sets: PX_Objects_WZ_PendingWZScenario
Non-filterable, non-selectable: WorkgroupID, OwnerID, TasksCompleted

PX.Objects.WZ.PendingWZScenario.ScenarioID : Edm.Guid [key] "Scenario ID"
PX.Objects.WZ.PendingWZScenario.Name : Edm.String "Scenario Name"
PX.Objects.WZ.PendingWZScenario.Status : Edm.String "Status"
PX.Objects.WZ.PendingWZScenario.ExecutionDate : Edm.DateTimeOffset "Execution Date"
PX.Objects.WZ.PendingWZScenario.ExecutionPeriodID : Edm.String "Execution Period"
PX.Objects.WZ.PendingWZScenario.Rolename : Edm.String "Role Name"
PX.Objects.WZ.PendingWZScenario.NodeID : Edm.Guid "Site Map Location"
PX.Objects.WZ.PendingWZScenario.ScheduleID : Edm.String "Schedule ID"
PX.Objects.WZ.PendingWZScenario.Scheduled : Edm.Boolean
PX.Objects.WZ.PendingWZScenario.ScenarioOrder : Edm.Int32 "Order"
PX.Objects.WZ.PendingWZScenario.AssignmentMapID : Edm.Int32 "Assignment Map"
PX.Objects.WZ.PendingWZScenario.WorkgroupID : Edm.Int32 "Workgroup ID"
PX.Objects.WZ.PendingWZScenario.OwnerID : Edm.Int32 "Assignee"
PX.Objects.WZ.PendingWZScenario.TasksCompleted : Edm.String "Tasks Completed"
PX.Objects.WZ.PendingWZScenario.tstamp : Edm.Binary
PX.Objects.WZ.PendingWZScenario.CreatedByID : Edm.Guid "Created By"
PX.Objects.WZ.PendingWZScenario.CreatedByScreenID : Edm.String
PX.Objects.WZ.PendingWZScenario.CreatedDateTime : Edm.DateTimeOffset
PX.Objects.WZ.PendingWZScenario.LastModifiedByID : Edm.Guid "Last Modified By"
PX.Objects.WZ.PendingWZScenario.LastModifiedByScreenID : Edm.String
PX.Objects.WZ.PendingWZScenario.LastModifiedDateTime : Edm.DateTimeOffset
PX.Objects.WZ.PendingWZScenario.WorkspaceID : Edm.Guid "Workspace"
PX.Objects.WZ.PendingWZScenario.SubcategoryID : Edm.Guid "Category"

# PX.Objects.WZ.WZSubTask (EntityType)

Key: TaskID
Entity sets: PX_Objects_WZ_WZSubTask
Non-filterable, non-selectable: Order, Offset, NoteText

PX.Objects.WZ.WZSubTask.ScenarioID : Edm.Guid
PX.Objects.WZ.WZSubTask.TaskID : Edm.Guid [key] "TaskID"
PX.Objects.WZ.WZSubTask.Position : Edm.Int32
PX.Objects.WZ.WZSubTask.Order : Edm.Int32
PX.Objects.WZ.WZSubTask.Offset : Edm.Int32
PX.Objects.WZ.WZSubTask.Type : Edm.String "Type"
PX.Objects.WZ.WZSubTask.Details : Edm.String "Details"
PX.Objects.WZ.WZSubTask.ScreenID : Edm.String "Screen Name"
PX.Objects.WZ.WZSubTask.ImportScenarioID : Edm.Guid "Import Scenario"
PX.Objects.WZ.WZSubTask.AssignedDate : Edm.DateTimeOffset
PX.Objects.WZ.WZSubTask.StartedDate : Edm.DateTimeOffset "Started"
PX.Objects.WZ.WZSubTask.CompletedBy : Edm.Int32 "Completed By"
PX.Objects.WZ.WZSubTask.CompletedDate : Edm.DateTimeOffset "Completed"
PX.Objects.WZ.WZSubTask.tstamp : Edm.Binary
PX.Objects.WZ.WZSubTask.CreatedByID : Edm.Guid "Created By"
PX.Objects.WZ.WZSubTask.CreatedByScreenID : Edm.String
PX.Objects.WZ.WZSubTask.CreatedDateTime : Edm.DateTimeOffset
PX.Objects.WZ.WZSubTask.LastModifiedByID : Edm.Guid "Last Modified By"
PX.Objects.WZ.WZSubTask.LastModifiedByScreenID : Edm.String
PX.Objects.WZ.WZSubTask.LastModifiedDateTime : Edm.DateTimeOffset
PX.Objects.WZ.WZSubTask.NoteID : Edm.Guid
PX.Objects.WZ.WZSubTask.NoteText : Edm.String "Note Text"
PX.Objects.WZ.WZSubTask.Name : Edm.String "Name"
PX.Objects.WZ.WZSubTask.ParentTaskID : Edm.Guid "Parent Task"
PX.Objects.WZ.WZSubTask.IsOptional : Edm.Boolean "Optional"
PX.Objects.WZ.WZSubTask.AssignedTo : Edm.Int32 "Assigned To"
PX.Objects.WZ.WZSubTask.Status : Edm.String "Status"

# PX.OidcClient.GraphExtensions.OidcUser (EntityType)

Label: "External Identities"
Key: ProviderID, ProviderName, UserID
Entity sets: PX_OidcClient_GraphExtensions_OidcUser, ExternalIdentities, OidcUser

PX.OidcClient.GraphExtensions.OidcUser.UserID : Edm.Guid [key] "User ID"
PX.OidcClient.GraphExtensions.OidcUser.ProviderID : Edm.Guid [key] "User ID"
PX.OidcClient.GraphExtensions.OidcUser.ProviderName : Edm.String [key] "Provider Name"
PX.OidcClient.GraphExtensions.OidcUser.Active : Edm.Boolean "Active"
PX.OidcClient.GraphExtensions.OidcUser.UserKey : Edm.String "User Key"
PX.OidcClient.GraphExtensions.OidcUser.UserIdentityClaimType : Edm.String "Identity Claim Type"
PX.OidcClient.GraphExtensions.OidcUser.UsersByUserID -> PX.SM.Users (UserID=PKID)

# PX.Olap.Maintenance.PivotField (EntityType)

Label: "Pivot Field"
Key: PivotFieldID, PivotTableID, ScreenID
Entity sets: PX_Olap_Maintenance_PivotField, PivotField
Non-filterable, non-selectable: FieldName, NoteText, Cumulative, DatePartMode, Mode, SegmentNumber

PX.Olap.Maintenance.PivotField.ScreenID : Edm.String [key]
PX.Olap.Maintenance.PivotField.PivotTableID : Edm.Int32 [key]
PX.Olap.Maintenance.PivotField.PivotFieldID : Edm.Int32 [key]
PX.Olap.Maintenance.PivotField.Type : Edm.Int32 [required]
PX.Olap.Maintenance.PivotField.Expression : Edm.String "Expression"
PX.Olap.Maintenance.PivotField.Transformation : Edm.String
PX.Olap.Maintenance.PivotField.Order : Edm.Int32
PX.Olap.Maintenance.PivotField.FieldName : Edm.String "Field Name"
PX.Olap.Maintenance.PivotField.Caption : Edm.String "Caption"
PX.Olap.Maintenance.PivotField.Aggregate : Edm.Int32 "Aggregate"
PX.Olap.Maintenance.PivotField.SortOrder : Edm.Int32 [required] "Sort Order"
PX.Olap.Maintenance.PivotField.SortType : Edm.Int32 [required] "Sort By"
PX.Olap.Maintenance.PivotField.CalculationType : Edm.Int32 [required] "Show Value As"
PX.Olap.Maintenance.PivotField.ShowTotal : Edm.Boolean [required] "Show Total"
PX.Olap.Maintenance.PivotField.Collapsed : Edm.Boolean [required] "Collapsed"
PX.Olap.Maintenance.PivotField.TotalLabel : Edm.String "Total Label"
PX.Olap.Maintenance.PivotField.NullLabel : Edm.String "Show Empty Value As"
PX.Olap.Maintenance.PivotField.Width : Edm.Int32 [required] "Width"
PX.Olap.Maintenance.PivotField.Format : Edm.String "Format"
PX.Olap.Maintenance.PivotField.Filter : Edm.String
PX.Olap.Maintenance.PivotField.CreatedByID : Edm.Guid "Created By"
PX.Olap.Maintenance.PivotField.CreatedByScreenID : Edm.String
PX.Olap.Maintenance.PivotField.CreatedDateTime : Edm.DateTimeOffset
PX.Olap.Maintenance.PivotField.LastModifiedByID : Edm.Guid "Last Modified By"
PX.Olap.Maintenance.PivotField.LastModifiedByScreenID : Edm.String
PX.Olap.Maintenance.PivotField.LastModifiedDateTime : Edm.DateTimeOffset
PX.Olap.Maintenance.PivotField.NoteID : Edm.Guid
PX.Olap.Maintenance.PivotField.NoteText : Edm.String "Note Text"
PX.Olap.Maintenance.PivotField.Cumulative : Edm.Int32 "Cumulative"
PX.Olap.Maintenance.PivotField.DatePartMode : Edm.Int32 "Date Part"
PX.Olap.Maintenance.PivotField.Mode : Edm.Int32 "Round to"
PX.Olap.Maintenance.PivotField.SegmentNumber : Edm.Int32 "Segment"
PX.Olap.Maintenance.PivotField.SiteMapByScreenID -> PX.SM.SiteMap (ScreenID=ScreenID)
PX.Olap.Maintenance.PivotField.UsersByCreatedByID -> PX.SM.Users (CreatedByID=PKID)
PX.Olap.Maintenance.PivotField.UsersByLastModifiedByID -> PX.SM.Users (LastModifiedByID=PKID)
PX.Olap.Maintenance.PivotField.PivotTableByPivotTableID -> PX.Olap.Maintenance.PivotTable (ScreenID=ScreenID, PivotTableID=PivotTableID)
PX.Olap.Maintenance.PivotField.PivotFieldPreferencesCollection -> Collection(PX.Olap.Maintenance.PivotFieldPreferences)

# PX.Olap.Maintenance.PivotFieldPreferences (EntityType)

Label: "Pivot Field Preferences"
Key: OwnerName, PivotFieldID, PivotTableID, ScreenID
Entity sets: PX_Olap_Maintenance_PivotFieldPreferences, PivotFieldPreferences

PX.Olap.Maintenance.PivotFieldPreferences.ScreenID : Edm.String [key]
PX.Olap.Maintenance.PivotFieldPreferences.PivotTableID : Edm.Int32 [key]
PX.Olap.Maintenance.PivotFieldPreferences.PivotFieldID : Edm.Int32 [key]
PX.Olap.Maintenance.PivotFieldPreferences.OwnerName : Edm.String [key]
PX.Olap.Maintenance.PivotFieldPreferences.Filter : Edm.String
PX.Olap.Maintenance.PivotFieldPreferences.SortOrder : Edm.Int32 [required] "Sort Order"
PX.Olap.Maintenance.PivotFieldPreferences.Width : Edm.Int32 [required] "Width"
PX.Olap.Maintenance.PivotFieldPreferences.SiteMapByScreenID -> PX.SM.SiteMap (ScreenID=ScreenID)
PX.Olap.Maintenance.PivotFieldPreferences.UsersByOwnerName -> PX.SM.Users (OwnerName=Username)
PX.Olap.Maintenance.PivotFieldPreferences.PivotFieldByPivotFieldID -> PX.Olap.Maintenance.PivotField (ScreenID=ScreenID, PivotTableID=PivotTableID, PivotFieldID=PivotFieldID)
PX.Olap.Maintenance.PivotFieldPreferences.PivotTableByPivotTableID -> PX.Olap.Maintenance.PivotTable (ScreenID=ScreenID, PivotTableID=PivotTableID)

# PX.Olap.Maintenance.PivotTable (EntityType)

Label: "Pivot Table"
Key: PivotTableID, ScreenID
Entity sets: PX_Olap_Maintenance_PivotTable, PivotTable
Non-filterable, non-selectable: SitemapTitle, NoteText, WorkspaceID, SubcategoryID

PX.Olap.Maintenance.PivotTable.ScreenID : Edm.String [key] "Screen ID"
PX.Olap.Maintenance.PivotTable.PivotTableID : Edm.Int32 [key] "Pivot Table ID"
PX.Olap.Maintenance.PivotTable.Name : Edm.String "Name"
PX.Olap.Maintenance.PivotTable.SitemapTitle : Edm.String "Site Map Title"
PX.Olap.Maintenance.PivotTable.FilterID : Edm.Guid "Shared Filter to Apply"
PX.Olap.Maintenance.PivotTable.CreatedByID : Edm.Guid "Created By"
PX.Olap.Maintenance.PivotTable.CreatedByScreenID : Edm.String
PX.Olap.Maintenance.PivotTable.CreatedDateTime : Edm.DateTimeOffset "Creation Date"
PX.Olap.Maintenance.PivotTable.LastModifiedByID : Edm.Guid "Last Modified By"
PX.Olap.Maintenance.PivotTable.LastModifiedByScreenID : Edm.String
PX.Olap.Maintenance.PivotTable.LastModifiedDateTime : Edm.DateTimeOffset
PX.Olap.Maintenance.PivotTable.NoteID : Edm.Guid
PX.Olap.Maintenance.PivotTable.NoteText : Edm.String "Note Text"
PX.Olap.Maintenance.PivotTable.WorkspaceID : Edm.Guid "Workspace"
PX.Olap.Maintenance.PivotTable.SubcategoryID : Edm.Guid "Category"
PX.Olap.Maintenance.PivotTable.SiteMapByScreenID -> PX.SM.SiteMap (ScreenID=ScreenID)
PX.Olap.Maintenance.PivotTable.UsersByCreatedByID -> PX.SM.Users (CreatedByID=PKID)
PX.Olap.Maintenance.PivotTable.UsersByLastModifiedByID -> PX.SM.Users (LastModifiedByID=PKID)
PX.Olap.Maintenance.PivotTable.PivotFieldCollection -> Collection(PX.Olap.Maintenance.PivotField)
PX.Olap.Maintenance.PivotTable.PivotFieldPreferencesCollection -> Collection(PX.Olap.Maintenance.PivotFieldPreferences)

# PX.PaymentProcessor.AvidXchange.DAC.PPAvidChildPayment (EntityType)

Label: "Avid Child Payment"
Key: ChildPaymentID, DocType, RefNbr
Entity sets: PX_PaymentProcessor_AvidXchange_DAC_PPAvidChildPayment, AvidChildPayment, PPAvidChildPayment
Non-filterable, non-selectable: ProofOfPayment

PX.PaymentProcessor.AvidXchange.DAC.PPAvidChildPayment.DocType : Edm.String [key] "Doc Type"
PX.PaymentProcessor.AvidXchange.DAC.PPAvidChildPayment.RefNbr : Edm.String [key] "Ref Nbr"
PX.PaymentProcessor.AvidXchange.DAC.PPAvidChildPayment.ChildPaymentID : Edm.String [key] "Child Payment ID"
PX.PaymentProcessor.AvidXchange.DAC.PPAvidChildPayment.ParentPaymentID : Edm.String "Parent Payment ID"
PX.PaymentProcessor.AvidXchange.DAC.PPAvidChildPayment.Status : Edm.String "Processing Status"
PX.PaymentProcessor.AvidXchange.DAC.PPAvidChildPayment.DisbursementType : Edm.String "Disbursement Method"
PX.PaymentProcessor.AvidXchange.DAC.PPAvidChildPayment.Amount : Edm.Decimal "Amount"
PX.PaymentProcessor.AvidXchange.DAC.PPAvidChildPayment.CheckNumber : Edm.String "Check Number"
PX.PaymentProcessor.AvidXchange.DAC.PPAvidChildPayment.UpdatedDate : Edm.DateTimeOffset "Updated On"
PX.PaymentProcessor.AvidXchange.DAC.PPAvidChildPayment.ClearedDate : Edm.DateTimeOffset "Cleared Date"
PX.PaymentProcessor.AvidXchange.DAC.PPAvidChildPayment.ProofOfPayment : Edm.Boolean "Proof Of Payment"
PX.PaymentProcessor.AvidXchange.DAC.PPAvidChildPayment.CreatedByID : Edm.Guid "Created By"
PX.PaymentProcessor.AvidXchange.DAC.PPAvidChildPayment.CreatedByScreenID : Edm.String
PX.PaymentProcessor.AvidXchange.DAC.PPAvidChildPayment.CreatedDateTime : Edm.DateTimeOffset
PX.PaymentProcessor.AvidXchange.DAC.PPAvidChildPayment.LastModifiedDateTime : Edm.DateTimeOffset
PX.PaymentProcessor.AvidXchange.DAC.PPAvidChildPayment.LastModifiedByScreenID : Edm.String
PX.PaymentProcessor.AvidXchange.DAC.PPAvidChildPayment.LastModifiedByID : Edm.Guid "Last Modified By"
PX.PaymentProcessor.AvidXchange.DAC.PPAvidChildPayment.Tstamp : Edm.Binary
PX.PaymentProcessor.AvidXchange.DAC.PPAvidChildPayment.APRegisterByRefNbr -> PX.Objects.AP.APRegister (DocType=DocType, RefNbr=RefNbr)
PX.PaymentProcessor.AvidXchange.DAC.PPAvidChildPayment.UsersByCreatedByID -> PX.SM.Users (CreatedByID=PKID)
PX.PaymentProcessor.AvidXchange.DAC.PPAvidChildPayment.UsersByLastModifiedByID -> PX.SM.Users (LastModifiedByID=PKID)

# PX.PaymentProcessor.AvidXchange.DAC.PPAvidFundingAccount (EntityType)

Label: "Avid Funding Account"
Key: ExternalPaymentProcessorID, RecordID
Entity sets: PX_PaymentProcessor_AvidXchange_DAC_PPAvidFundingAccount, AvidFundingAccount, PPAvidFundingAccount
Non-filterable, non-selectable: CanBeOnboarded, NoteText

PX.PaymentProcessor.AvidXchange.DAC.PPAvidFundingAccount.ExternalPaymentProcessorID : Edm.String [key]
PX.PaymentProcessor.AvidXchange.DAC.PPAvidFundingAccount.RecordID : Edm.Int32 [key]
PX.PaymentProcessor.AvidXchange.DAC.PPAvidFundingAccount.ExternalAccountID : Edm.String "External Account ID"
PX.PaymentProcessor.AvidXchange.DAC.PPAvidFundingAccount.AccountNumber : Edm.String "Account Number"
PX.PaymentProcessor.AvidXchange.DAC.PPAvidFundingAccount.RoutingNumber : Edm.String "Routing Number"
PX.PaymentProcessor.AvidXchange.DAC.PPAvidFundingAccount.BeneficiaryName : Edm.String "Account Holder"
PX.PaymentProcessor.AvidXchange.DAC.PPAvidFundingAccount.BankName : Edm.String "Bank Name"
PX.PaymentProcessor.AvidXchange.DAC.PPAvidFundingAccount.Status : Edm.String "Status"
PX.PaymentProcessor.AvidXchange.DAC.PPAvidFundingAccount.CheckSerialNbr : Edm.String "Payment Serial Number"
PX.PaymentProcessor.AvidXchange.DAC.PPAvidFundingAccount.CanBeOnboarded : Edm.Boolean "CanBeOnboarded"
PX.PaymentProcessor.AvidXchange.DAC.PPAvidFundingAccount.Tstamp : Edm.Binary
PX.PaymentProcessor.AvidXchange.DAC.PPAvidFundingAccount.CreatedByID : Edm.Guid "Created By"
PX.PaymentProcessor.AvidXchange.DAC.PPAvidFundingAccount.CreatedByScreenID : Edm.String
PX.PaymentProcessor.AvidXchange.DAC.PPAvidFundingAccount.CreatedDateTime : Edm.DateTimeOffset
PX.PaymentProcessor.AvidXchange.DAC.PPAvidFundingAccount.LastModifiedByID : Edm.Guid "Last Modified By"
PX.PaymentProcessor.AvidXchange.DAC.PPAvidFundingAccount.LastModifiedByScreenID : Edm.String
PX.PaymentProcessor.AvidXchange.DAC.PPAvidFundingAccount.LastModifiedDateTime : Edm.DateTimeOffset
PX.PaymentProcessor.AvidXchange.DAC.PPAvidFundingAccount.NoteID : Edm.Guid
PX.PaymentProcessor.AvidXchange.DAC.PPAvidFundingAccount.NoteText : Edm.String "Note Text"
PX.PaymentProcessor.AvidXchange.DAC.PPAvidFundingAccount.UsersByCreatedByID -> PX.SM.Users (CreatedByID=PKID)
PX.PaymentProcessor.AvidXchange.DAC.PPAvidFundingAccount.UsersByLastModifiedByID -> PX.SM.Users (LastModifiedByID=PKID)
PX.PaymentProcessor.AvidXchange.DAC.PPAvidFundingAccount.CashAccountByCashAccountID -> PX.Objects.CA.CashAccount
PX.PaymentProcessor.AvidXchange.DAC.PPAvidFundingAccount.PPExternalByExternalPaymentProcessorID -> PX.PaymentProcessorCommon.DAC.PPExternal (ExternalPaymentProcessorID=ExternalPaymentProcessorID)

# PX.PaymentProcessor.AvidXchange.DAC.PPAvidSetting (EntityType)

Label: "Avid Processor Setting"
Key: ExternalPaymentProcessorID
Entity sets: PX_PaymentProcessor_AvidXchange_DAC_PPAvidSetting, AvidProcessorSetting, PPAvidSetting
Non-filterable, non-selectable: NoteText

PX.PaymentProcessor.AvidXchange.DAC.PPAvidSetting.ExternalPaymentProcessorID : Edm.String [key]
PX.PaymentProcessor.AvidXchange.DAC.PPAvidSetting.OrganizationID : Edm.String "Organization ID"
PX.PaymentProcessor.AvidXchange.DAC.PPAvidSetting.OrganizationName : Edm.String "Organization"
PX.PaymentProcessor.AvidXchange.DAC.PPAvidSetting.ApplicationID : Edm.String "Application ID"
PX.PaymentProcessor.AvidXchange.DAC.PPAvidSetting.TenantID : Edm.String "Tenant ID"
PX.PaymentProcessor.AvidXchange.DAC.PPAvidSetting.Status : Edm.String "Status"
PX.PaymentProcessor.AvidXchange.DAC.PPAvidSetting.Reason : Edm.String "Onboarding Status"
PX.PaymentProcessor.AvidXchange.DAC.PPAvidSetting.WebhookID : Edm.Guid "Webhook ID"
PX.PaymentProcessor.AvidXchange.DAC.PPAvidSetting.WebhookSecurityKey : Edm.String "Webhook Security Key"
PX.PaymentProcessor.AvidXchange.DAC.PPAvidSetting.Tstamp : Edm.Binary
PX.PaymentProcessor.AvidXchange.DAC.PPAvidSetting.CreatedByID : Edm.Guid "Created By"
PX.PaymentProcessor.AvidXchange.DAC.PPAvidSetting.CreatedByScreenID : Edm.String
PX.PaymentProcessor.AvidXchange.DAC.PPAvidSetting.CreatedDateTime : Edm.DateTimeOffset
PX.PaymentProcessor.AvidXchange.DAC.PPAvidSetting.LastModifiedByID : Edm.Guid "Last Modified By"
PX.PaymentProcessor.AvidXchange.DAC.PPAvidSetting.LastModifiedByScreenID : Edm.String
PX.PaymentProcessor.AvidXchange.DAC.PPAvidSetting.LastModifiedDateTime : Edm.DateTimeOffset
PX.PaymentProcessor.AvidXchange.DAC.PPAvidSetting.NoteID : Edm.Guid
PX.PaymentProcessor.AvidXchange.DAC.PPAvidSetting.NoteText : Edm.String "Note Text"
PX.PaymentProcessor.AvidXchange.DAC.PPAvidSetting.UsersByCreatedByID -> PX.SM.Users (CreatedByID=PKID)
PX.PaymentProcessor.AvidXchange.DAC.PPAvidSetting.UsersByLastModifiedByID -> PX.SM.Users (LastModifiedByID=PKID)
PX.PaymentProcessor.AvidXchange.DAC.PPAvidSetting.PPExternalByExternalPaymentProcessorID -> PX.PaymentProcessorCommon.DAC.PPExternal (ExternalPaymentProcessorID=ExternalPaymentProcessorID)

# PX.PaymentProcessor.BillCom.DAC.PPBillcomBill (EntityType)

Label: "Payment Processor BILL Bills"
Key: DocType, ExternalPaymentProcessorID, OrganizationID, RefNbr
Entity sets: PX_PaymentProcessor_BillCom_DAC_PPBillcomBill, PaymentProcessorBILLBills, PPBillcomBill

PX.PaymentProcessor.BillCom.DAC.PPBillcomBill.DocType : Edm.String [key] "Type"
PX.PaymentProcessor.BillCom.DAC.PPBillcomBill.ExternalPaymentProcessorID : Edm.String [key]
PX.PaymentProcessor.BillCom.DAC.PPBillcomBill.OrganizationID : Edm.Int32 [key] "Organization"
PX.PaymentProcessor.BillCom.DAC.PPBillcomBill.RefNbr : Edm.String [key] "Reference Nbr."
PX.PaymentProcessor.BillCom.DAC.PPBillcomBill.ExternalBillID : Edm.String "External Bill ID"
PX.PaymentProcessor.BillCom.DAC.PPBillcomBill.CreatedByID : Edm.Guid "Created By"
PX.PaymentProcessor.BillCom.DAC.PPBillcomBill.CreatedByScreenID : Edm.String
PX.PaymentProcessor.BillCom.DAC.PPBillcomBill.CreatedDateTime : Edm.DateTimeOffset "Created Date Time"
PX.PaymentProcessor.BillCom.DAC.PPBillcomBill.LastModifiedByID : Edm.Guid "Last Modified By"
PX.PaymentProcessor.BillCom.DAC.PPBillcomBill.LastModifiedByScreenID : Edm.String
PX.PaymentProcessor.BillCom.DAC.PPBillcomBill.LastModifiedDateTime : Edm.DateTimeOffset "Last Modified Date Time"
PX.PaymentProcessor.BillCom.DAC.PPBillcomBill.Tstamp : Edm.Binary "Tstamp"
PX.PaymentProcessor.BillCom.DAC.PPBillcomBill.APRegisterByRefNbr -> PX.Objects.AP.APRegister (DocType=DocType, RefNbr=RefNbr)
PX.PaymentProcessor.BillCom.DAC.PPBillcomBill.UsersByCreatedByID -> PX.SM.Users (CreatedByID=PKID)
PX.PaymentProcessor.BillCom.DAC.PPBillcomBill.UsersByLastModifiedByID -> PX.SM.Users (LastModifiedByID=PKID)
PX.PaymentProcessor.BillCom.DAC.PPBillcomBill.OrganizationByOrganizationID -> PX.Objects.GL.DAC.Organization (OrganizationID=OrganizationID)
PX.PaymentProcessor.BillCom.DAC.PPBillcomBill.PPExternalSettingByOrganizationID -> PX.PaymentProcessor.BillCom.DAC.PPExternalSetting (ExternalPaymentProcessorID=ExternalPaymentProcessorID, OrganizationID=OrganizationID)
PX.PaymentProcessor.BillCom.DAC.PPBillcomBill.PPExternalByExternalPaymentProcessorID -> PX.PaymentProcessorCommon.DAC.PPExternal (ExternalPaymentProcessorID=ExternalPaymentProcessorID)

# PX.PaymentProcessor.BillCom.DAC.PPBillcomFundingAccount (EntityType)

Label: "Payment Processor BILL Funding Accounts"
Key: ExternalAccountID, ExternalPaymentProcessorID, OrganizationID
Entity sets: PX_PaymentProcessor_BillCom_DAC_PPBillcomFundingAccount, PaymentProcessorBILLFundingAccounts, PPBillcomFundingAccount
Non-filterable, non-selectable: CanBeDisabled, NoteText

PX.PaymentProcessor.BillCom.DAC.PPBillcomFundingAccount.ExternalPaymentProcessorID : Edm.String [key]
PX.PaymentProcessor.BillCom.DAC.PPBillcomFundingAccount.OrganizationID : Edm.Int32 [key] "Company ID"
PX.PaymentProcessor.BillCom.DAC.PPBillcomFundingAccount.ExternalAccountID : Edm.String [key] "External Account ID"
PX.PaymentProcessor.BillCom.DAC.PPBillcomFundingAccount.ExternalAccountBank : Edm.String "Bank"
PX.PaymentProcessor.BillCom.DAC.PPBillcomFundingAccount.ExternalAccountType : Edm.String "Account Type"
PX.PaymentProcessor.BillCom.DAC.PPBillcomFundingAccount.ExternalAccountName : Edm.String "Account Holder"
PX.PaymentProcessor.BillCom.DAC.PPBillcomFundingAccount.ExternalAccountRoutingNumber : Edm.String "Routing Number"
PX.PaymentProcessor.BillCom.DAC.PPBillcomFundingAccount.ExternalAccountNumber : Edm.String "Account Number"
PX.PaymentProcessor.BillCom.DAC.PPBillcomFundingAccount.Status : Edm.String "Status"
PX.PaymentProcessor.BillCom.DAC.PPBillcomFundingAccount.IsActive : Edm.Boolean [required] "Active"
PX.PaymentProcessor.BillCom.DAC.PPBillcomFundingAccount.CanBeDisabled : Edm.Boolean "Can Be Disabled"
PX.PaymentProcessor.BillCom.DAC.PPBillcomFundingAccount.CreatedByID : Edm.Guid "Created By"
PX.PaymentProcessor.BillCom.DAC.PPBillcomFundingAccount.CreatedByScreenID : Edm.String
PX.PaymentProcessor.BillCom.DAC.PPBillcomFundingAccount.CreatedDateTime : Edm.DateTimeOffset "Created Date Time"
PX.PaymentProcessor.BillCom.DAC.PPBillcomFundingAccount.LastModifiedByID : Edm.Guid "Last Modified By"
PX.PaymentProcessor.BillCom.DAC.PPBillcomFundingAccount.LastModifiedByScreenID : Edm.String
PX.PaymentProcessor.BillCom.DAC.PPBillcomFundingAccount.LastModifiedDateTime : Edm.DateTimeOffset "Last Modified Date Time"
PX.PaymentProcessor.BillCom.DAC.PPBillcomFundingAccount.Noteid : Edm.Guid "Noteid"
PX.PaymentProcessor.BillCom.DAC.PPBillcomFundingAccount.NoteText : Edm.String "Note Text"
PX.PaymentProcessor.BillCom.DAC.PPBillcomFundingAccount.Tstamp : Edm.Binary "Tstamp"
PX.PaymentProcessor.BillCom.DAC.PPBillcomFundingAccount.UsersByCreatedByID -> PX.SM.Users (CreatedByID=PKID)
PX.PaymentProcessor.BillCom.DAC.PPBillcomFundingAccount.UsersByLastModifiedByID -> PX.SM.Users (LastModifiedByID=PKID)
PX.PaymentProcessor.BillCom.DAC.PPBillcomFundingAccount.OrganizationByOrganizationID -> PX.Objects.GL.DAC.Organization (OrganizationID=OrganizationID)
PX.PaymentProcessor.BillCom.DAC.PPBillcomFundingAccount.CashAccountByCashAccountID -> PX.Objects.CA.CashAccount
PX.PaymentProcessor.BillCom.DAC.PPBillcomFundingAccount.PPExternalSettingByOrganizationID -> PX.PaymentProcessor.BillCom.DAC.PPExternalSetting (ExternalPaymentProcessorID=ExternalPaymentProcessorID, OrganizationID=OrganizationID)
PX.PaymentProcessor.BillCom.DAC.PPBillcomFundingAccount.PPExternalByExternalPaymentProcessorID -> PX.PaymentProcessorCommon.DAC.PPExternal (ExternalPaymentProcessorID=ExternalPaymentProcessorID)
PX.PaymentProcessor.BillCom.DAC.PPBillcomFundingAccount.PPBillcomFundingAccountUserCollection -> Collection(PX.PaymentProcessor.BillCom.DAC.PPBillcomFundingAccountUser)

# PX.PaymentProcessor.BillCom.DAC.PPBillcomFundingAccountUser (EntityType)

Label: "Payment Processor Account User"
Key: ExternalID, ExternalPaymentProcessorID, OrganizationID
Entity sets: PX_PaymentProcessor_BillCom_DAC_PPBillcomFundingAccountUser, PaymentProcessorAccountUser, PPBillcomFundingAccountUser
Non-filterable, non-selectable: ExternalAccountStatus, Status, CanBeDisabled, NoteText

PX.PaymentProcessor.BillCom.DAC.PPBillcomFundingAccountUser.ExternalPaymentProcessorID : Edm.String [key]
PX.PaymentProcessor.BillCom.DAC.PPBillcomFundingAccountUser.OrganizationID : Edm.Int32 [key] "Company ID"
PX.PaymentProcessor.BillCom.DAC.PPBillcomFundingAccountUser.ExternalID : Edm.String [key] "External ID"
PX.PaymentProcessor.BillCom.DAC.PPBillcomFundingAccountUser.ExternalAccountID : Edm.String "External Account ID"
PX.PaymentProcessor.BillCom.DAC.PPBillcomFundingAccountUser.ExternalAccountStatus : Edm.String "Account Status"
PX.PaymentProcessor.BillCom.DAC.PPBillcomFundingAccountUser.ExternalUserID : Edm.String "External User ID"
PX.PaymentProcessor.BillCom.DAC.PPBillcomFundingAccountUser.VerificationStatus : Edm.String "Verification status"
PX.PaymentProcessor.BillCom.DAC.PPBillcomFundingAccountUser.Status : Edm.String "Verification Status"
PX.PaymentProcessor.BillCom.DAC.PPBillcomFundingAccountUser.CanBeDisabled : Edm.Boolean "CanBeDisabled"
PX.PaymentProcessor.BillCom.DAC.PPBillcomFundingAccountUser.CreatedByID : Edm.Guid "Created By"
PX.PaymentProcessor.BillCom.DAC.PPBillcomFundingAccountUser.CreatedByScreenID : Edm.String
PX.PaymentProcessor.BillCom.DAC.PPBillcomFundingAccountUser.CreatedDateTime : Edm.DateTimeOffset "Created Date Time"
PX.PaymentProcessor.BillCom.DAC.PPBillcomFundingAccountUser.LastModifiedByID : Edm.Guid "Last Modified By"
PX.PaymentProcessor.BillCom.DAC.PPBillcomFundingAccountUser.LastModifiedByScreenID : Edm.String
PX.PaymentProcessor.BillCom.DAC.PPBillcomFundingAccountUser.LastModifiedDateTime : Edm.DateTimeOffset "Last Modified Date Time"
PX.PaymentProcessor.BillCom.DAC.PPBillcomFundingAccountUser.Noteid : Edm.Guid "Noteid"
PX.PaymentProcessor.BillCom.DAC.PPBillcomFundingAccountUser.NoteText : Edm.String "Note Text"
PX.PaymentProcessor.BillCom.DAC.PPBillcomFundingAccountUser.Tstamp : Edm.Binary "Tstamp"
PX.PaymentProcessor.BillCom.DAC.PPBillcomFundingAccountUser.UsersByCreatedByID -> PX.SM.Users (CreatedByID=PKID)
PX.PaymentProcessor.BillCom.DAC.PPBillcomFundingAccountUser.UsersByLastModifiedByID -> PX.SM.Users (LastModifiedByID=PKID)
PX.PaymentProcessor.BillCom.DAC.PPBillcomFundingAccountUser.OrganizationByOrganizationID -> PX.Objects.GL.DAC.Organization (OrganizationID=OrganizationID)
PX.PaymentProcessor.BillCom.DAC.PPBillcomFundingAccountUser.PPBillcomFundingAccountByExternalAccountID -> PX.PaymentProcessor.BillCom.DAC.PPBillcomFundingAccount (ExternalAccountID=ExternalAccountID)
PX.PaymentProcessor.BillCom.DAC.PPBillcomFundingAccountUser.PPExternalSettingByOrganizationID -> PX.PaymentProcessor.BillCom.DAC.PPExternalSetting (ExternalPaymentProcessorID=ExternalPaymentProcessorID, OrganizationID=OrganizationID)
PX.PaymentProcessor.BillCom.DAC.PPBillcomFundingAccountUser.PPExternalByExternalPaymentProcessorID -> PX.PaymentProcessorCommon.DAC.PPExternal (ExternalPaymentProcessorID=ExternalPaymentProcessorID)

# PX.PaymentProcessor.BillCom.DAC.PPBillcomUser (EntityType)

Label: "Payment Processor BILL Users"
Key: ExternalPaymentProcessorID, OrganizationID, UserID
Entity sets: PX_PaymentProcessor_BillCom_DAC_PPBillcomUser, PaymentProcessorBILLUsers, PPBillcomUser
Non-filterable, non-selectable: CanBeOnboarded, CanBeEnabled, CanBeDisabled, NoteText

PX.PaymentProcessor.BillCom.DAC.PPBillcomUser.ExternalPaymentProcessorID : Edm.String [key]
PX.PaymentProcessor.BillCom.DAC.PPBillcomUser.OrganizationID : Edm.Int32 [key] "Company ID"
PX.PaymentProcessor.BillCom.DAC.PPBillcomUser.UserID : Edm.Guid [key] "Username"
PX.PaymentProcessor.BillCom.DAC.PPBillcomUser.Status : Edm.String "Status"
PX.PaymentProcessor.BillCom.DAC.PPBillcomUser.ExternalUserID : Edm.String "External User ID"
PX.PaymentProcessor.BillCom.DAC.PPBillcomUser.CanBeOnboarded : Edm.Boolean "Can Be Onboarded"
PX.PaymentProcessor.BillCom.DAC.PPBillcomUser.CanBeEnabled : Edm.Boolean "Can Be Enabled"
PX.PaymentProcessor.BillCom.DAC.PPBillcomUser.CanBeDisabled : Edm.Boolean "CanBeDisabled"
PX.PaymentProcessor.BillCom.DAC.PPBillcomUser.CreatedByID : Edm.Guid "Created By"
PX.PaymentProcessor.BillCom.DAC.PPBillcomUser.CreatedByScreenID : Edm.String
PX.PaymentProcessor.BillCom.DAC.PPBillcomUser.CreatedDateTime : Edm.DateTimeOffset "Created Date Time"
PX.PaymentProcessor.BillCom.DAC.PPBillcomUser.LastModifiedByID : Edm.Guid "Last Modified By"
PX.PaymentProcessor.BillCom.DAC.PPBillcomUser.LastModifiedByScreenID : Edm.String
PX.PaymentProcessor.BillCom.DAC.PPBillcomUser.LastModifiedDateTime : Edm.DateTimeOffset "Last Modified Date Time"
PX.PaymentProcessor.BillCom.DAC.PPBillcomUser.NoteID : Edm.Guid "NoteID"
PX.PaymentProcessor.BillCom.DAC.PPBillcomUser.NoteText : Edm.String "Note Text"
PX.PaymentProcessor.BillCom.DAC.PPBillcomUser.Tstamp : Edm.Binary "Tstamp"
PX.PaymentProcessor.BillCom.DAC.PPBillcomUser.UsersByUserID -> PX.SM.Users (UserID=PKID)
PX.PaymentProcessor.BillCom.DAC.PPBillcomUser.UsersByCreatedByID -> PX.SM.Users (CreatedByID=PKID)
PX.PaymentProcessor.BillCom.DAC.PPBillcomUser.UsersByLastModifiedByID -> PX.SM.Users (LastModifiedByID=PKID)
PX.PaymentProcessor.BillCom.DAC.PPBillcomUser.OrganizationByOrganizationID -> PX.Objects.GL.DAC.Organization (OrganizationID=OrganizationID)
PX.PaymentProcessor.BillCom.DAC.PPBillcomUser.PPExternalSettingByOrganizationID -> PX.PaymentProcessor.BillCom.DAC.PPExternalSetting (ExternalPaymentProcessorID=ExternalPaymentProcessorID, OrganizationID=OrganizationID)
PX.PaymentProcessor.BillCom.DAC.PPBillcomUser.PPExternalByExternalPaymentProcessorID -> PX.PaymentProcessorCommon.DAC.PPExternal (ExternalPaymentProcessorID=ExternalPaymentProcessorID)

# PX.PaymentProcessor.BillCom.DAC.PPBillcomVendor (EntityType)

Label: "Payment Processor BILL Vendors"
Key: BAccountID, ExternalPaymentProcessorID, LocationID, OrganizationID
Entity sets: PX_PaymentProcessor_BillCom_DAC_PPBillcomVendor, PaymentProcessorBILLVendors, PPBillcomVendor
Non-filterable, non-selectable: NetworkType, RemittanceInformationMessage, IsUSVendor, IsUSDtoUSD, IsUSDtoFC, IsFCtoFC, IsFCtoUSD

PX.PaymentProcessor.BillCom.DAC.PPBillcomVendor.ExternalPaymentProcessorID : Edm.String [key]
PX.PaymentProcessor.BillCom.DAC.PPBillcomVendor.OrganizationID : Edm.Int32 [key] "Organization"
PX.PaymentProcessor.BillCom.DAC.PPBillcomVendor.BAccountID : Edm.Int32 [key] "BAccountID"
PX.PaymentProcessor.BillCom.DAC.PPBillcomVendor.IsRemittanceAddressChanged : Edm.Boolean [required] "Remittance Address Changed"
PX.PaymentProcessor.BillCom.DAC.PPBillcomVendor.IsBankDetailsChanged : Edm.Boolean [required] "Bank Details Changed"
PX.PaymentProcessor.BillCom.DAC.PPBillcomVendor.LocationID : Edm.Int32 [key] "LocationID"
PX.PaymentProcessor.BillCom.DAC.PPBillcomVendor.ExternalVendorID : Edm.String "External Vendor ID"
PX.PaymentProcessor.BillCom.DAC.PPBillcomVendor.NetworkStatus : Edm.String "BILL Status"
PX.PaymentProcessor.BillCom.DAC.PPBillcomVendor.PayByType : Edm.String "Preferred Disbursement Method"
PX.PaymentProcessor.BillCom.DAC.PPBillcomVendor.PaymentNetworkID : Edm.String "Payment Network ID"
PX.PaymentProcessor.BillCom.DAC.PPBillcomVendor.NetworkType : Edm.String "NetworkType"
PX.PaymentProcessor.BillCom.DAC.PPBillcomVendor.RemittanceInformationMessage : Edm.String "RemittanceInformationMessage"
PX.PaymentProcessor.BillCom.DAC.PPBillcomVendor.BillCuryID : Edm.String "Bill Currency"
PX.PaymentProcessor.BillCom.DAC.PPBillcomVendor.PaymentCuryID : Edm.String "Payment Currency"
PX.PaymentProcessor.BillCom.DAC.PPBillcomVendor.BankAccountNbr : Edm.String "Bank Account"
PX.PaymentProcessor.BillCom.DAC.PPBillcomVendor.BankRoutingNumber : Edm.String "Bank Routing Number"
PX.PaymentProcessor.BillCom.DAC.PPBillcomVendor.BankName : Edm.String "Financial Institution"
PX.PaymentProcessor.BillCom.DAC.PPBillcomVendor.RemitCountryID : Edm.String
PX.PaymentProcessor.BillCom.DAC.PPBillcomVendor.IsUSVendor : Edm.Boolean
PX.PaymentProcessor.BillCom.DAC.PPBillcomVendor.IsUSDtoUSD : Edm.Boolean
PX.PaymentProcessor.BillCom.DAC.PPBillcomVendor.IsUSDtoFC : Edm.Boolean
PX.PaymentProcessor.BillCom.DAC.PPBillcomVendor.IsFCtoFC : Edm.Boolean
PX.PaymentProcessor.BillCom.DAC.PPBillcomVendor.IsFCtoUSD : Edm.Boolean
PX.PaymentProcessor.BillCom.DAC.PPBillcomVendor.CreatedByID : Edm.Guid "Created By"
PX.PaymentProcessor.BillCom.DAC.PPBillcomVendor.CreatedByScreenID : Edm.String
PX.PaymentProcessor.BillCom.DAC.PPBillcomVendor.CreatedDateTime : Edm.DateTimeOffset "Created Date Time"
PX.PaymentProcessor.BillCom.DAC.PPBillcomVendor.LastModifiedByID : Edm.Guid "Last Modified By"
PX.PaymentProcessor.BillCom.DAC.PPBillcomVendor.LastModifiedByScreenID : Edm.String
PX.PaymentProcessor.BillCom.DAC.PPBillcomVendor.LastModifiedDateTime : Edm.DateTimeOffset "Last Modified Date Time"
PX.PaymentProcessor.BillCom.DAC.PPBillcomVendor.Tstamp : Edm.Binary "Tstamp"
PX.PaymentProcessor.BillCom.DAC.PPBillcomVendor.BAccountByBAccountID -> PX.Objects.CR.BAccount (BAccountID=BAccountID)
PX.PaymentProcessor.BillCom.DAC.PPBillcomVendor.UsersByCreatedByID -> PX.SM.Users (CreatedByID=PKID)
PX.PaymentProcessor.BillCom.DAC.PPBillcomVendor.UsersByLastModifiedByID -> PX.SM.Users (LastModifiedByID=PKID)
PX.PaymentProcessor.BillCom.DAC.PPBillcomVendor.OrganizationByOrganizationID -> PX.Objects.GL.DAC.Organization (OrganizationID=OrganizationID)
PX.PaymentProcessor.BillCom.DAC.PPBillcomVendor.LocationByLocationID -> PX.Objects.CR.Location (BAccountID=BAccountID, LocationID=LocationID)
PX.PaymentProcessor.BillCom.DAC.PPBillcomVendor.PPExternalSettingByOrganizationID -> PX.PaymentProcessor.BillCom.DAC.PPExternalSetting (ExternalPaymentProcessorID=ExternalPaymentProcessorID, OrganizationID=OrganizationID)
PX.PaymentProcessor.BillCom.DAC.PPBillcomVendor.PPExternalByExternalPaymentProcessorID -> PX.PaymentProcessorCommon.DAC.PPExternal (ExternalPaymentProcessorID=ExternalPaymentProcessorID)

# PX.PaymentProcessor.BillCom.DAC.PPBillcomVendorLocation (EntityType)

Label: "Payment Processor Vendors"
BaseType: PX.PaymentProcessor.BillCom.DAC.PPBillcomVendor
Key: BAccountID, ExternalPaymentProcessorID, LocationID, OrganizationID (inherited from PX.PaymentProcessor.BillCom.DAC.PPBillcomVendor)
Entity sets: PX_PaymentProcessor_BillCom_DAC_PPBillcomVendorLocation, PaymentProcessorVendors, PPBillcomVendorLocation

PX.PaymentProcessor.BillCom.DAC.PPBillcomVendorLocation.LocationCD : Edm.String "Vendor Location"
PX.PaymentProcessor.BillCom.DAC.PPBillcomVendorLocation.LocationName : Edm.String "Location Name"
PX.PaymentProcessor.BillCom.DAC.PPBillcomVendorLocation.OrganizationCD : Edm.String "Company"
PX.PaymentProcessor.BillCom.DAC.PPBillcomVendorLocation.OrganizationName : Edm.String "Company Name"
PX.PaymentProcessor.BillCom.DAC.PPBillcomVendorLocation.VRemitAddressID : Edm.Int32 "VRemitAddressID"
PX.PaymentProcessor.BillCom.DAC.PPBillcomVendorLocation.VRemitContactID : Edm.Int32 "VRemitContactID"
PX.PaymentProcessor.BillCom.DAC.PPBillcomVendorLocation.ContactByDefContactID -> PX.Objects.CR.Contact
PX.PaymentProcessor.BillCom.DAC.PPBillcomVendorLocation.ContactByVRemitContactID -> PX.Objects.CR.Contact (VRemitContactID=ContactID)
PX.PaymentProcessor.BillCom.DAC.PPBillcomVendorLocation.AddressByDefAddressID -> PX.Objects.CR.Address
PX.PaymentProcessor.BillCom.DAC.PPBillcomVendorLocation.AddressByVRemitAddressID -> PX.Objects.CR.Address (VRemitAddressID=AddressID)

# PX.PaymentProcessor.BillCom.DAC.PPExternalSetting (EntityType)

Label: "Payment Processor BILL Setting"
Key: ExternalPaymentProcessorID, OrganizationID
Entity sets: PX_PaymentProcessor_BillCom_DAC_PPExternalSetting, PaymentProcessorBILLSetting, PPExternalSetting
Non-filterable, non-selectable: CanBeOnboarded, CanSubscribe, CanUnSubscribe, NoteText

PX.PaymentProcessor.BillCom.DAC.PPExternalSetting.ExternalPaymentProcessorID : Edm.String [key]
PX.PaymentProcessor.BillCom.DAC.PPExternalSetting.OrganizationID : Edm.Int32 [key] "Company ID"
PX.PaymentProcessor.BillCom.DAC.PPExternalSetting.IsOnboarded : Edm.Boolean [required] "Onboarded"
PX.PaymentProcessor.BillCom.DAC.PPExternalSetting.CanBeOnboarded : Edm.Boolean "CanBeOnboarded"
PX.PaymentProcessor.BillCom.DAC.PPExternalSetting.ExternalOrganizationID : Edm.String "External Org. ID"
PX.PaymentProcessor.BillCom.DAC.PPExternalSetting.WebhookID : Edm.Guid "Webhook"
PX.PaymentProcessor.BillCom.DAC.PPExternalSetting.ExternalWebhookID : Edm.String
PX.PaymentProcessor.BillCom.DAC.PPExternalSetting.WebhookSecurityKey : Edm.String
PX.PaymentProcessor.BillCom.DAC.PPExternalSetting.UpdateInExternalProcessor : Edm.Boolean [required] "UpdateInExternalProcessor"
PX.PaymentProcessor.BillCom.DAC.PPExternalSetting.CanSubscribe : Edm.Boolean "CanSubscribe"
PX.PaymentProcessor.BillCom.DAC.PPExternalSetting.CanUnSubscribe : Edm.Boolean "CanUnSubscribe"
PX.PaymentProcessor.BillCom.DAC.PPExternalSetting.CreatedByID : Edm.Guid "Created By"
PX.PaymentProcessor.BillCom.DAC.PPExternalSetting.CreatedByScreenID : Edm.String
PX.PaymentProcessor.BillCom.DAC.PPExternalSetting.CreatedDateTime : Edm.DateTimeOffset "Created Date Time"
PX.PaymentProcessor.BillCom.DAC.PPExternalSetting.LastModifiedByID : Edm.Guid "Last Modified By"
PX.PaymentProcessor.BillCom.DAC.PPExternalSetting.LastModifiedByScreenID : Edm.String
PX.PaymentProcessor.BillCom.DAC.PPExternalSetting.LastModifiedDateTime : Edm.DateTimeOffset "Last Modified Date Time"
PX.PaymentProcessor.BillCom.DAC.PPExternalSetting.Noteid : Edm.Guid "Noteid"
PX.PaymentProcessor.BillCom.DAC.PPExternalSetting.NoteText : Edm.String "Note Text"
PX.PaymentProcessor.BillCom.DAC.PPExternalSetting.Tstamp : Edm.Binary "Tstamp"
PX.PaymentProcessor.BillCom.DAC.PPExternalSetting.UsersByCreatedByID -> PX.SM.Users (CreatedByID=PKID)
PX.PaymentProcessor.BillCom.DAC.PPExternalSetting.UsersByLastModifiedByID -> PX.SM.Users (LastModifiedByID=PKID)
PX.PaymentProcessor.BillCom.DAC.PPExternalSetting.OrganizationByOrganizationID -> PX.Objects.GL.DAC.Organization (OrganizationID=OrganizationID)
PX.PaymentProcessor.BillCom.DAC.PPExternalSetting.WebHookByWebhookID -> PX.Api.Webhooks.DAC.WebHook (WebhookID=WebHookID)
PX.PaymentProcessor.BillCom.DAC.PPExternalSetting.PPExternalByExternalPaymentProcessorID -> PX.PaymentProcessorCommon.DAC.PPExternal (ExternalPaymentProcessorID=ExternalPaymentProcessorID)
PX.PaymentProcessor.BillCom.DAC.PPExternalSetting.PPBillcomVendorCollection -> Collection(PX.PaymentProcessor.BillCom.DAC.PPBillcomVendor)
PX.PaymentProcessor.BillCom.DAC.PPExternalSetting.PPBillcomBillCollection -> Collection(PX.PaymentProcessor.BillCom.DAC.PPBillcomBill)
PX.PaymentProcessor.BillCom.DAC.PPExternalSetting.PPBillcomFundingAccountCollection -> Collection(PX.PaymentProcessor.BillCom.DAC.PPBillcomFundingAccount)
PX.PaymentProcessor.BillCom.DAC.PPExternalSetting.PPBillcomFundingAccountUserCollection -> Collection(PX.PaymentProcessor.BillCom.DAC.PPBillcomFundingAccountUser)
PX.PaymentProcessor.BillCom.DAC.PPExternalSetting.PPBillcomUserCollection -> Collection(PX.PaymentProcessor.BillCom.DAC.PPBillcomUser)

# PX.PaymentProcessor.ProcessorBase.DAC.APExternalPayment (EntityType)

Label: "APExternalPayment"
BaseType: PX.Objects.AP.APPayment
Key: DocType, RefNbr (inherited from PX.Objects.AP.APRegister)
Entity sets: PX_PaymentProcessor_ProcessorBase_DAC_APExternalPayment, APExternalPayment

PX.PaymentProcessor.ProcessorBase.DAC.APExternalPayment.CashAccountCD : Edm.String "Cash Account"
PX.PaymentProcessor.ProcessorBase.DAC.APExternalPayment.VendorCD : Edm.String "Vendor ID"
PX.PaymentProcessor.ProcessorBase.DAC.APExternalPayment.VendorName : Edm.String "Vendor"

# PX.PaymentProcessor.ProcessorBase.DAC.PPExternalTran (EntityType)

Label: "External Payment Processor Transaction History"
Key: TranNbr
Entity sets: PX_PaymentProcessor_ProcessorBase_DAC_PPExternalTran, ExternalPaymentProcessorTransactionHistory, PPExternalTran

PX.PaymentProcessor.ProcessorBase.DAC.PPExternalTran.TranNbr : Edm.Int32 [key] "Tran. Nbr."
PX.PaymentProcessor.ProcessorBase.DAC.PPExternalTran.ExternalPaymentProcessorID : Edm.String "Processor ID"
PX.PaymentProcessor.ProcessorBase.DAC.PPExternalTran.DocType : Edm.String "Doc Type"
PX.PaymentProcessor.ProcessorBase.DAC.PPExternalTran.RefNbr : Edm.String "Ref Nbr"
PX.PaymentProcessor.ProcessorBase.DAC.PPExternalTran.ExternalPaymentID : Edm.String "Payment ID"
PX.PaymentProcessor.ProcessorBase.DAC.PPExternalTran.Status : Edm.String "Processing Status"
PX.PaymentProcessor.ProcessorBase.DAC.PPExternalTran.TransactionState : Edm.String "Transaction State"
PX.PaymentProcessor.ProcessorBase.DAC.PPExternalTran.ExternalUserID : Edm.String "User ID"
PX.PaymentProcessor.ProcessorBase.DAC.PPExternalTran.ProcessDate : Edm.DateTimeOffset "Process Date"
PX.PaymentProcessor.ProcessorBase.DAC.PPExternalTran.FundingAcctID : Edm.String "Funding Account"
PX.PaymentProcessor.ProcessorBase.DAC.PPExternalTran.DisbursementAcctNbr : Edm.String "Disbursement Account Nbr."
PX.PaymentProcessor.ProcessorBase.DAC.PPExternalTran.FundingCuryID : Edm.String "Funding Currency"
PX.PaymentProcessor.ProcessorBase.DAC.PPExternalTran.DisbursementType : Edm.String "Disbursement Method"
PX.PaymentProcessor.ProcessorBase.DAC.PPExternalTran.DisbursementAmount : Edm.Decimal "Disbursement Amount"
PX.PaymentProcessor.ProcessorBase.DAC.PPExternalTran.DisbursementCuryID : Edm.String "Disbursement Currency"
PX.PaymentProcessor.ProcessorBase.DAC.PPExternalTran.DisbursementArriveDate : Edm.DateTimeOffset "Arrives by Date"
PX.PaymentProcessor.ProcessorBase.DAC.PPExternalTran.ExternalVendorID : Edm.String "Vendor ID"
PX.PaymentProcessor.ProcessorBase.DAC.PPExternalTran.BillingType : Edm.String "Billing Type"
PX.PaymentProcessor.ProcessorBase.DAC.PPExternalTran.TransactionNumber : Edm.String "Transaction Number"
PX.PaymentProcessor.ProcessorBase.DAC.PPExternalTran.ExternalUpdatedDateTime : Edm.DateTimeOffset "Updated At"
PX.PaymentProcessor.ProcessorBase.DAC.PPExternalTran.ExternalComment : Edm.String "Response Comment"
PX.PaymentProcessor.ProcessorBase.DAC.PPExternalTran.CreatedByID : Edm.Guid "Created By"
PX.PaymentProcessor.ProcessorBase.DAC.PPExternalTran.CreatedByScreenID : Edm.String
PX.PaymentProcessor.ProcessorBase.DAC.PPExternalTran.CreatedDateTime : Edm.DateTimeOffset
PX.PaymentProcessor.ProcessorBase.DAC.PPExternalTran.Tstamp : Edm.Binary "Tstamp"
PX.PaymentProcessor.ProcessorBase.DAC.PPExternalTran.APRegisterByRefNbr -> PX.Objects.AP.APRegister (DocType=DocType, RefNbr=RefNbr)
PX.PaymentProcessor.ProcessorBase.DAC.PPExternalTran.UsersByCreatedByID -> PX.SM.Users (CreatedByID=PKID)
PX.PaymentProcessor.ProcessorBase.DAC.PPExternalTran.PPExternalByExternalPaymentProcessorID -> PX.PaymentProcessorCommon.DAC.PPExternal (ExternalPaymentProcessorID=ExternalPaymentProcessorID)

# PX.PaymentProcessorCommon.DAC.PPExternal (EntityType)

Label: "External Payment Processor"
Key: ExternalPaymentProcessorID
Entity sets: PX_PaymentProcessorCommon_DAC_PPExternal, ExternalPaymentProcessor, PPExternal
Non-filterable, non-selectable: DisclaimerMessage, NoteText

PX.PaymentProcessorCommon.DAC.PPExternal.ExternalPaymentProcessorID : Edm.String [key] "Payment Processor ID"
PX.PaymentProcessorCommon.DAC.PPExternal.Name : Edm.String "Name"
PX.PaymentProcessorCommon.DAC.PPExternal.Type : Edm.String "Plug-In"
PX.PaymentProcessorCommon.DAC.PPExternal.IsActive : Edm.Boolean [required] "Active"
PX.PaymentProcessorCommon.DAC.PPExternal.IsProduction : Edm.Boolean [required] "For Production Use"
PX.PaymentProcessorCommon.DAC.PPExternal.FileUploadTagID : Edm.Guid "Bill Upload Tag"
PX.PaymentProcessorCommon.DAC.PPExternal.UploadUntaggedSingleFile : Edm.Boolean [required] "Upload Untagged Single File"
PX.PaymentProcessorCommon.DAC.PPExternal.DisclaimerMessage : Edm.String "Disclaimer Message"
PX.PaymentProcessorCommon.DAC.PPExternal.SandboxVendorEmail : Edm.String "Sandbox Vendor Email"
PX.PaymentProcessorCommon.DAC.PPExternal.CreatedByID : Edm.Guid "Created By"
PX.PaymentProcessorCommon.DAC.PPExternal.CreatedByScreenID : Edm.String
PX.PaymentProcessorCommon.DAC.PPExternal.CreatedDateTime : Edm.DateTimeOffset "Created Date Time"
PX.PaymentProcessorCommon.DAC.PPExternal.LastModifiedByID : Edm.Guid "Last Modified By"
PX.PaymentProcessorCommon.DAC.PPExternal.LastModifiedByScreenID : Edm.String
PX.PaymentProcessorCommon.DAC.PPExternal.LastModifiedDateTime : Edm.DateTimeOffset "Last Modified Date Time"
PX.PaymentProcessorCommon.DAC.PPExternal.Noteid : Edm.Guid "Noteid"
PX.PaymentProcessorCommon.DAC.PPExternal.NoteText : Edm.String "Note Text"
PX.PaymentProcessorCommon.DAC.PPExternal.Tstamp : Edm.Binary "Tstamp"
PX.PaymentProcessorCommon.DAC.PPExternal.UsersByCreatedByID -> PX.SM.Users (CreatedByID=PKID)
PX.PaymentProcessorCommon.DAC.PPExternal.UsersByLastModifiedByID -> PX.SM.Users (LastModifiedByID=PKID)
PX.PaymentProcessorCommon.DAC.PPExternal.PPBillcomVendorCollection -> Collection(PX.PaymentProcessor.BillCom.DAC.PPBillcomVendor)
PX.PaymentProcessorCommon.DAC.PPExternal.PaymentMethodCollection -> Collection(PX.Objects.CA.PaymentMethod)
PX.PaymentProcessorCommon.DAC.PPExternal.PPExternalTranCollection -> Collection(PX.PaymentProcessor.ProcessorBase.DAC.PPExternalTran)
PX.PaymentProcessorCommon.DAC.PPExternal.PPBillcomBillCollection -> Collection(PX.PaymentProcessor.BillCom.DAC.PPBillcomBill)
PX.PaymentProcessorCommon.DAC.PPExternal.PPBillcomFundingAccountCollection -> Collection(PX.PaymentProcessor.BillCom.DAC.PPBillcomFundingAccount)
PX.PaymentProcessorCommon.DAC.PPExternal.PPBillcomFundingAccountUserCollection -> Collection(PX.PaymentProcessor.BillCom.DAC.PPBillcomFundingAccountUser)
PX.PaymentProcessorCommon.DAC.PPExternal.PPBillcomUserCollection -> Collection(PX.PaymentProcessor.BillCom.DAC.PPBillcomUser)
PX.PaymentProcessorCommon.DAC.PPExternal.PPExternalSettingCollection -> Collection(PX.PaymentProcessor.BillCom.DAC.PPExternalSetting)
PX.PaymentProcessorCommon.DAC.PPExternal.PPAvidFundingAccountCollection -> Collection(PX.PaymentProcessor.AvidXchange.DAC.PPAvidFundingAccount)
PX.PaymentProcessorCommon.DAC.PPExternal.PPAvidSettingCollection -> Collection(PX.PaymentProcessor.AvidXchange.DAC.PPAvidSetting)

# PX.PushNotifications.UI.DAC.DispatcherSettings (EntityType)

Singletons: PX_PushNotifications_UI_DAC_DispatcherSettings

PX.PushNotifications.UI.DAC.DispatcherSettings.NqdLongProcessingThreshold : Edm.Decimal "Processing Time Threshold (s)"
PX.PushNotifications.UI.DAC.DispatcherSettings.EqdLongProcessingThreshold : Edm.Decimal "Processing Time Threshold (s)"
PX.PushNotifications.UI.DAC.DispatcherSettings.NqdLogMaxLength : Edm.Int32 "Number of Records in Detailed Log"
PX.PushNotifications.UI.DAC.DispatcherSettings.EqdLogMaxLength : Edm.Int32 "Number of Records in Detailed Log"
PX.PushNotifications.UI.DAC.DispatcherSettings.KeepStatisticsForPeriod : Edm.Int32 "Keep Statistics and Logs For (Days)"
PX.PushNotifications.UI.DAC.DispatcherSettings.LogDetails : Edm.Boolean "Log Trigger Details"
PX.PushNotifications.UI.DAC.DispatcherSettings.CqdLongProcessingThreshold : Edm.Decimal "Processing Time Threshold (s)"
PX.PushNotifications.UI.DAC.DispatcherSettings.CqdLogMaxLength : Edm.Int32 "Number of Records in Detailed Log"

# PX.PushNotifications.UI.DAC.DispatcherStatisticQueryDetail (EntityType)

Label: "DispatcherStatisticQueryDetail"
Key: Field, Id, Query
Entity sets: PX_PushNotifications_UI_DAC_DispatcherStatisticQueryDetail, DispatcherStatisticQueryDetail

PX.PushNotifications.UI.DAC.DispatcherStatisticQueryDetail.Id : Edm.Guid [key] "ID"
PX.PushNotifications.UI.DAC.DispatcherStatisticQueryDetail.Query : Edm.String [key] "Handler Definition"
PX.PushNotifications.UI.DAC.DispatcherStatisticQueryDetail.Field : Edm.String [key] "Field"
PX.PushNotifications.UI.DAC.DispatcherStatisticQueryDetail.Count : Edm.Int32 [required] "Messages"

# PX.PushNotifications.UI.DAC.DispatcherStatistics (EntityType)

Label: "DispatcherStatistics"
Key: Date, Hour, Id, Minute, QueueType, WebsiteId
Entity sets: PX_PushNotifications_UI_DAC_DispatcherStatistics, DispatcherStatistics

PX.PushNotifications.UI.DAC.DispatcherStatistics.Id : Edm.Guid [key] "ID"
PX.PushNotifications.UI.DAC.DispatcherStatistics.QueueType : Edm.String [key] "Queue Type"
PX.PushNotifications.UI.DAC.DispatcherStatistics.WebsiteId : Edm.String [key] "Node ID"
PX.PushNotifications.UI.DAC.DispatcherStatistics.Date : Edm.DateTimeOffset [key] "Date"
PX.PushNotifications.UI.DAC.DispatcherStatistics.Hour : Edm.Int32 [key] "Hour"
PX.PushNotifications.UI.DAC.DispatcherStatistics.Minute : Edm.Int32 [key] "Minute"
PX.PushNotifications.UI.DAC.DispatcherStatistics.Queued : Edm.Int32 "Queued"
PX.PushNotifications.UI.DAC.DispatcherStatistics.Processed : Edm.Int32 "Processed"
PX.PushNotifications.UI.DAC.DispatcherStatistics.QueueSize : Edm.Int64 "Max. Queue Size (KB)"
PX.PushNotifications.UI.DAC.DispatcherStatistics.MaxQueueSize : Edm.Int64 "Queue Size Limit (KB)"
PX.PushNotifications.UI.DAC.DispatcherStatistics.AverageProcessingTime : Edm.Decimal "Avg Processing Time (ms)"
PX.PushNotifications.UI.DAC.DispatcherStatistics.MaxProcessingTime : Edm.Decimal "Max. Processing Time (ms)"
PX.PushNotifications.UI.DAC.DispatcherStatistics.CreatedDateTime : Edm.DateTimeOffset "Date"

# PX.PushNotifications.UI.DAC.DispatcherStatisticSourceDetail (EntityType)

Label: "DispatcherStatisticSourceDetail"
Key: Id, ScreenID, TableName
Entity sets: PX_PushNotifications_UI_DAC_DispatcherStatisticSourceDetail, DispatcherStatisticSourceDetail

PX.PushNotifications.UI.DAC.DispatcherStatisticSourceDetail.Id : Edm.Guid [key] "ID"
PX.PushNotifications.UI.DAC.DispatcherStatisticSourceDetail.ScreenID : Edm.String [key] "Screen"
PX.PushNotifications.UI.DAC.DispatcherStatisticSourceDetail.TableName : Edm.String [key] "DAC"
PX.PushNotifications.UI.DAC.DispatcherStatisticSourceDetail.Count : Edm.Int32 [required] "Messages"

# PX.PushNotifications.UI.DAC.DispatcherStatisticsPerHour (EntityType)

Label: "DispatcherStatisticsPerHour"
BaseType: PX.PushNotifications.UI.DAC.DispatcherStatistics
Key: Date, Hour, Id, Minute, QueueType, WebsiteId (inherited from PX.PushNotifications.UI.DAC.DispatcherStatistics)
Entity sets: PX_PushNotifications_UI_DAC_DispatcherStatisticsPerHour, DispatcherStatisticsPerHour

# PX.PushNotifications.UI.DAC.PushNotificationsErrors (EntityType)

Key: HookId, TransactionId
Entity sets: PX_PushNotifications_UI_DAC_PushNotificationsErrors

PX.PushNotifications.UI.DAC.PushNotificationsErrors.TransactionId : Edm.Guid [key] "Transaction ID"
PX.PushNotifications.UI.DAC.PushNotificationsErrors.TimeStamp : Edm.Int64 "Date"
PX.PushNotifications.UI.DAC.PushNotificationsErrors.HookId : Edm.Guid [key] "Destination ID"
PX.PushNotifications.UI.DAC.PushNotificationsErrors.Source : Edm.String "Notification Source"
PX.PushNotifications.UI.DAC.PushNotificationsErrors.SourceEvent : Edm.String "Internal Source Event"
PX.PushNotifications.UI.DAC.PushNotificationsErrors.ErrorMessage : Edm.String "Error"

# PX.PushNotifications.UI.DAC.PushNotificationsFailedToSend (EntityType)

Label: "Push Notifications Failed To Send"
Key: HookId, Id, TransactionId
Entity sets: PX_PushNotifications_UI_DAC_PushNotificationsFailedToSend, PushNotificationsFailedToSend
Non-filterable, non-selectable: DateTimeStamp

PX.PushNotifications.UI.DAC.PushNotificationsFailedToSend.Id : Edm.Guid [key]
PX.PushNotifications.UI.DAC.PushNotificationsFailedToSend.TransactionId : Edm.Guid [key] "TransactionId"
PX.PushNotifications.UI.DAC.PushNotificationsFailedToSend.TimeStamp : Edm.Int64 "Date"
PX.PushNotifications.UI.DAC.PushNotificationsFailedToSend.DateTimeStamp : Edm.DateTimeOffset "Date"
PX.PushNotifications.UI.DAC.PushNotificationsFailedToSend.HookId : Edm.Guid [key] "Destination Name"
PX.PushNotifications.UI.DAC.PushNotificationsFailedToSend.Source : Edm.String "Source Name"
PX.PushNotifications.UI.DAC.PushNotificationsFailedToSend.Notification : Edm.String "Notification Body"
PX.PushNotifications.UI.DAC.PushNotificationsFailedToSend.ErrorMessage : Edm.String "Error"
PX.PushNotifications.UI.DAC.PushNotificationsFailedToSend.Truncated : Edm.Boolean "Truncated"
PX.PushNotifications.UI.DAC.PushNotificationsFailedToSend.PushNotificationsHookByHookId -> PX.PushNotifications.UI.DAC.PushNotificationsHook (HookId=HookId)

# PX.PushNotifications.UI.DAC.PushNotificationsHook (EntityType)

Label: "Push Notifications Hook"
Key: Name
Entity sets: PX_PushNotifications_UI_DAC_PushNotificationsHook, PushNotificationsHook

PX.PushNotifications.UI.DAC.PushNotificationsHook.HookId : Edm.Guid "HookId"
PX.PushNotifications.UI.DAC.PushNotificationsHook.Active : Edm.Boolean [required] "Active"
PX.PushNotifications.UI.DAC.PushNotificationsHook.Name : Edm.String [key] "Destination Name"
PX.PushNotifications.UI.DAC.PushNotificationsHook.Type : Edm.String "Destination Type"
PX.PushNotifications.UI.DAC.PushNotificationsHook.Address : Edm.String "Address"
PX.PushNotifications.UI.DAC.PushNotificationsHook.HeaderName : Edm.String "Header Name"
PX.PushNotifications.UI.DAC.PushNotificationsHook.HeaderValue : Edm.String "Header Value"
PX.PushNotifications.UI.DAC.PushNotificationsHook.PushNotificationsSourceCollection -> Collection(PX.PushNotifications.UI.DAC.PushNotificationsSource)
PX.PushNotifications.UI.DAC.PushNotificationsHook.PushNotificationsFailedToSendCollection -> Collection(PX.PushNotifications.UI.DAC.PushNotificationsFailedToSend)
PX.PushNotifications.UI.DAC.PushNotificationsHook.PushNotificationsTrackingFieldCollection -> Collection(PX.PushNotifications.UI.DAC.PushNotificationsTrackingField)

# PX.PushNotifications.UI.DAC.PushNotificationsSource (EntityType)

Label: "Push Notifications Source"
Key: HookId, LineNbr
Entity sets: PX_PushNotifications_UI_DAC_PushNotificationsSource, PushNotificationsSource

PX.PushNotifications.UI.DAC.PushNotificationsSource.HookId : Edm.Guid [key]
PX.PushNotifications.UI.DAC.PushNotificationsSource.Active : Edm.Boolean [required] "Active"
PX.PushNotifications.UI.DAC.PushNotificationsSource.LineNbr : Edm.Int32 [key] "LineNbr"
PX.PushNotifications.UI.DAC.PushNotificationsSource.SourceType : Edm.String "SourceType"
PX.PushNotifications.UI.DAC.PushNotificationsSource.DesignID : Edm.Guid "Inquiry Title"
PX.PushNotifications.UI.DAC.PushNotificationsSource.EndpointName : Edm.String "Endpoint Name"
PX.PushNotifications.UI.DAC.PushNotificationsSource.EndpointVersion : Edm.String "Endpoint Version"
PX.PushNotifications.UI.DAC.PushNotificationsSource.ObjectName : Edm.String "ObjectName"
PX.PushNotifications.UI.DAC.PushNotificationsSource.InCodeClass : Edm.String "Class Name"
PX.PushNotifications.UI.DAC.PushNotificationsSource.FilterId : Edm.Guid
PX.PushNotifications.UI.DAC.PushNotificationsSource.TrackAllFields : Edm.Boolean "Track All Fields"
PX.PushNotifications.UI.DAC.PushNotificationsSource.GIDesignByDesignID -> PX.Data.Maintenance.GI.GIDesign (DesignID=DesignID)
PX.PushNotifications.UI.DAC.PushNotificationsSource.PushNotificationsHookByHookId -> PX.PushNotifications.UI.DAC.PushNotificationsHook (HookId=HookId)
PX.PushNotifications.UI.DAC.PushNotificationsSource.PushNotificationsTrackingFieldCollection -> Collection(PX.PushNotifications.UI.DAC.PushNotificationsTrackingField)

# PX.PushNotifications.UI.DAC.PushNotificationsSourceGI (EntityType)

Label: "Push Notifications Source"
BaseType: PX.PushNotifications.UI.DAC.PushNotificationsSource
Key: HookId, LineNbr (inherited from PX.PushNotifications.UI.DAC.PushNotificationsSource)
Entity sets: PX_PushNotifications_UI_DAC_PushNotificationsSourceGI

# PX.PushNotifications.UI.DAC.PushNotificationsSourceIC (EntityType)

Label: "Push Notifications Source"
BaseType: PX.PushNotifications.UI.DAC.PushNotificationsSource
Key: HookId, LineNbr (inherited from PX.PushNotifications.UI.DAC.PushNotificationsSource)
Entity sets: PX_PushNotifications_UI_DAC_PushNotificationsSourceIC

# PX.PushNotifications.UI.DAC.PushNotificationsTrackingField (EntityType)

Label: "Push Notification Tracked Field"
Key: FieldID, HookId, LineNbr, SourceType
Entity sets: PX_PushNotifications_UI_DAC_PushNotificationsTrackingField, PushNotificationTrackedField, PushNotificationsTrackingField

PX.PushNotifications.UI.DAC.PushNotificationsTrackingField.HookId : Edm.Guid [key]
PX.PushNotifications.UI.DAC.PushNotificationsTrackingField.LineNbr : Edm.Int32 [key]
PX.PushNotifications.UI.DAC.PushNotificationsTrackingField.SourceType : Edm.String [key]
PX.PushNotifications.UI.DAC.PushNotificationsTrackingField.FieldID : Edm.Int32 [key]
PX.PushNotifications.UI.DAC.PushNotificationsTrackingField.TableName : Edm.String "Table Name"
PX.PushNotifications.UI.DAC.PushNotificationsTrackingField.FieldName : Edm.String "Field Name"
PX.PushNotifications.UI.DAC.PushNotificationsTrackingField.PushNotificationsSourceBySourceType -> PX.PushNotifications.UI.DAC.PushNotificationsSource (HookId=HookId, LineNbr=LineNbr, SourceType=SourceType)
PX.PushNotifications.UI.DAC.PushNotificationsTrackingField.PushNotificationsHookByHookId -> PX.PushNotifications.UI.DAC.PushNotificationsHook (HookId=HookId)

# PX.PushNotifications.UI.DAC.PushNotificationsTrackingFieldGI (EntityType)

Label: "Push Notification Tracked Field"
BaseType: PX.PushNotifications.UI.DAC.PushNotificationsTrackingField
Key: FieldID, HookId, LineNbr, SourceType (inherited from PX.PushNotifications.UI.DAC.PushNotificationsTrackingField)
Entity sets: PX_PushNotifications_UI_DAC_PushNotificationsTrackingFieldGI, PushNotificationTrackedField1, PushNotificationsTrackingFieldGI

# PX.PushNotifications.UI.DAC.PushNotificationsTrackingFieldIC (EntityType)

Label: "Push Notification Tracked Field"
BaseType: PX.PushNotifications.UI.DAC.PushNotificationsTrackingField
Key: FieldID, HookId, LineNbr, SourceType (inherited from PX.PushNotifications.UI.DAC.PushNotificationsTrackingField)
Entity sets: PX_PushNotifications_UI_DAC_PushNotificationsTrackingFieldIC, PushNotificationTrackedField2, PushNotificationsTrackingFieldIC

# PX.Salesforce.SFEntitySetup (EntityType)

Key: EntityType
Entity sets: PX_Salesforce_SFEntitySetup
Non-filterable, non-selectable: LastNotification, LastNotificationTime, NoteText

PX.Salesforce.SFEntitySetup.EntityType : Edm.Int32 [key] "Entity"
PX.Salesforce.SFEntitySetup.ImportScenario : Edm.String "Import Scenario"
PX.Salesforce.SFEntitySetup.ExportScenario : Edm.String "Export Scenario"
PX.Salesforce.SFEntitySetup.ProcStatus : Edm.Int32 "Status"
PX.Salesforce.SFEntitySetup.LastNotification : Edm.Int32 "Last Notification"
PX.Salesforce.SFEntitySetup.LastNotificationTime : Edm.Int32 "Last DateTime"
PX.Salesforce.SFEntitySetup.TimerThreadGuid : Edm.Guid
PX.Salesforce.SFEntitySetup.ErrorThreadGuid : Edm.Guid
PX.Salesforce.SFEntitySetup.TopicThreadGuid : Edm.Guid
PX.Salesforce.SFEntitySetup.LastFullSyncDateTime : Edm.DateTimeOffset "Latest Full Data Resync Attempt"
PX.Salesforce.SFEntitySetup.LastMissedSyncDateTime : Edm.DateTimeOffset "Latest Failed & Missed Data Resync Attempt"
PX.Salesforce.SFEntitySetup.MaxAttemptCount : Edm.Int32 "Number of Attempts"
PX.Salesforce.SFEntitySetup.SyncSortOrder : Edm.Int32 "Sync Order"
PX.Salesforce.SFEntitySetup.NoteID : Edm.Guid "NoteID"
PX.Salesforce.SFEntitySetup.NoteText : Edm.String "Note Text"
PX.Salesforce.SFEntitySetup.ReplayID : Edm.Int64 "Replay ID"
PX.Salesforce.SFEntitySetup.LastRemoteEventDateTime : Edm.DateTimeOffset "Last Remote Event Date Time"
PX.Salesforce.SFEntitySetup.SYMappingByImportScenario -> PX.Api.SYMapping (ImportScenario=Name)
PX.Salesforce.SFEntitySetup.SYMappingByExportScenario -> PX.Api.SYMapping (ExportScenario=Name)

# PX.Salesforce.SFSyncRecord (EntityType)

Key: SyncRecordID
Entity sets: PX_Salesforce_SFSyncRecord
Non-filterable, non-selectable: DisplayName, DeletedDatabaseRecord

PX.Salesforce.SFSyncRecord.SyncRecordID : Edm.Int32 [key] "Sync Record ID"
PX.Salesforce.SFSyncRecord.RemoteID : Edm.String "Ext. Ref."
PX.Salesforce.SFSyncRecord.LocalGuid : Edm.Guid "Note ID"
PX.Salesforce.SFSyncRecord.LocalID : Edm.String "Record ID"
PX.Salesforce.SFSyncRecord.EntityType : Edm.Int32 "Entity"
PX.Salesforce.SFSyncRecord.LocalTS : Edm.DateTimeOffset "Modified"
PX.Salesforce.SFSyncRecord.RemoteTS : Edm.DateTimeOffset "Ext. Modified"
PX.Salesforce.SFSyncRecord.PendingSync : Edm.Boolean "Pending Sync"
PX.Salesforce.SFSyncRecord.LastErrorMessage : Edm.String "Error"
PX.Salesforce.SFSyncRecord.Operation : Edm.Int32 "Last Operation"
PX.Salesforce.SFSyncRecord.Status : Edm.Int32 "Status"
PX.Salesforce.SFSyncRecord.LastOperation : Edm.Int32 "Last Operation"
PX.Salesforce.SFSyncRecord.AttemptCount : Edm.Int32 "Attempts Made"
PX.Salesforce.SFSyncRecord.LastAttemptTS : Edm.DateTimeOffset "Last Sync Attempt"
PX.Salesforce.SFSyncRecord.DisplayName : Edm.String "Document"
PX.Salesforce.SFSyncRecord.DeletedDatabaseRecord : Edm.Boolean [required] "DeletedDatabaseRecord"

# PX.ScreenPreferences.DAC.GridDataPresentation (EntityType)

Key: PresentationID
Entity sets: PX_ScreenPreferences_DAC_GridDataPresentation
Non-filterable, non-selectable: NoteText

PX.ScreenPreferences.DAC.GridDataPresentation.PresentationID : Edm.Guid [key] "PresentationID"
PX.ScreenPreferences.DAC.GridDataPresentation.ScreenID : Edm.String "Screen ID"
PX.ScreenPreferences.DAC.GridDataPresentation.GraphViewName : Edm.String "View Name"
PX.ScreenPreferences.DAC.GridDataPresentation.Name : Edm.String "Display Name"
PX.ScreenPreferences.DAC.GridDataPresentation.Type : Edm.String "Presentation Type"
PX.ScreenPreferences.DAC.GridDataPresentation.UserName : Edm.String
PX.ScreenPreferences.DAC.GridDataPresentation.IsShared : Edm.Boolean [required] "Is Shared"
PX.ScreenPreferences.DAC.GridDataPresentation.IsDefault : Edm.Boolean [required] "Is Default"
PX.ScreenPreferences.DAC.GridDataPresentation.NoteID : Edm.Guid
PX.ScreenPreferences.DAC.GridDataPresentation.NoteText : Edm.String "Note Text"
PX.ScreenPreferences.DAC.GridDataPresentation.RefNoteID : Edm.Guid "Grid Presentation View"
PX.ScreenPreferences.DAC.GridDataPresentation.FilterID : Edm.Guid "Default Filter"
PX.ScreenPreferences.DAC.GridDataPresentation.CreatedByScreenID : Edm.String "Created by Screen ID"
PX.ScreenPreferences.DAC.GridDataPresentation.CreatedByID : Edm.Guid "Created By"
PX.ScreenPreferences.DAC.GridDataPresentation.CreatedDateTime : Edm.DateTimeOffset "Created On"
PX.ScreenPreferences.DAC.GridDataPresentation.LastModifiedByID : Edm.Guid "Last Modified By"
PX.ScreenPreferences.DAC.GridDataPresentation.LastModifiedDateTime : Edm.DateTimeOffset "Last Modified On"
PX.ScreenPreferences.DAC.GridDataPresentation.LastModifiedByScreenID : Edm.String "Last Modified by Screen ID"
PX.ScreenPreferences.DAC.GridDataPresentation.TStamp : Edm.Binary
PX.ScreenPreferences.DAC.GridDataPresentation.UsersByCreatedByID -> PX.SM.Users (CreatedByID=PKID)
PX.ScreenPreferences.DAC.GridDataPresentation.UsersByLastModifiedByID -> PX.SM.Users (LastModifiedByID=PKID)

# PX.SiteMap.DAC.SiteMap (EntityType)

Label: "Site Map"
BaseType: PX.SM.SiteMap
Key: NodeID (inherited from PX.SM.SiteMap)
Entity sets: PX_SiteMap_DAC_SiteMap
Non-filterable, non-selectable: Workspaces, Category, External

PX.SiteMap.DAC.SiteMap.Workspaces : Edm.String "Workspaces"
PX.SiteMap.DAC.SiteMap.Category : Edm.String "Category"
PX.SiteMap.DAC.SiteMap.ListIsEntryPoint : Edm.Boolean "Is Substitute"
PX.SiteMap.DAC.SiteMap.External : Edm.Boolean "External"

# PX.SM.Alias.CustProject (EntityType)

Key: Name
Entity sets: PX_SM_Alias_CustProject

PX.SM.Alias.CustProject.ProjID : Edm.Guid "ProjID"
PX.SM.Alias.CustProject.Name : Edm.String [key] "Project Name"
PX.SM.Alias.CustProject.ParentID : Edm.Guid
PX.SM.Alias.CustProject.Description : Edm.String "Description"
PX.SM.Alias.CustProject.UsersByCreatedByID -> PX.SM.Users
PX.SM.Alias.CustProject.UsersByLastModifiedByID -> PX.SM.Users
PX.SM.Alias.CustProject.UPPackageTablesCollection -> Collection(PX.SM.UPPackageTables)

# PX.SM.AU.SMEmail (EntityType)

Key: NoteID
Entity sets: PX_SM_AU_SMEmail
Non-filterable, non-selectable: NoteText, DeletedDatabaseRecord

PX.SM.AU.SMEmail.NoteID : Edm.Guid [key]
PX.SM.AU.SMEmail.RefNoteID : Edm.Guid
PX.SM.AU.SMEmail.NoteText : Edm.String "Note Text"
PX.SM.AU.SMEmail.Subject : Edm.String "Summary"
PX.SM.AU.SMEmail.Body : Edm.String "Activity Details"
PX.SM.AU.SMEmail.MPStatus : Edm.String "Email Status"
PX.SM.AU.SMEmail.IsArchived : Edm.Boolean
PX.SM.AU.SMEmail.ImcUID : Edm.Guid "ImcUID"
PX.SM.AU.SMEmail.Pop3UID : Edm.String "Pop3UID"
PX.SM.AU.SMEmail.ImapUID : Edm.Int32 "ImapUID"
PX.SM.AU.SMEmail.MailDate : Edm.DateTimeOffset
PX.SM.AU.SMEmail.MailAccountID : Edm.Int32 "From"
PX.SM.AU.SMEmail.MailFrom : Edm.String "From"
PX.SM.AU.SMEmail.MailReply : Edm.String "Reply"
PX.SM.AU.SMEmail.MailTo : Edm.String "To"
PX.SM.AU.SMEmail.MailCc : Edm.String "CC"
PX.SM.AU.SMEmail.MailBcc : Edm.String "BCC"
PX.SM.AU.SMEmail.RetryCount : Edm.Int32 [required] "RetryCount"
PX.SM.AU.SMEmail.MessageId : Edm.String "MessageId"
PX.SM.AU.SMEmail.MessageReference : Edm.String "MessageReference"
PX.SM.AU.SMEmail.Exception : Edm.String "Error Message"
PX.SM.AU.SMEmail.Format : Edm.String "Format"
PX.SM.AU.SMEmail.ReportFormat : Edm.String "Format"
PX.SM.AU.SMEmail.TrackingID : Edm.String "TrackingID"
PX.SM.AU.SMEmail.Ticket : Edm.String "Ticket"
PX.SM.AU.SMEmail.IsIncome : Edm.Boolean "Is Income"
PX.SM.AU.SMEmail.CreatedByID : Edm.Guid "Created By"
PX.SM.AU.SMEmail.CreatedByScreenID : Edm.String
PX.SM.AU.SMEmail.CreatedDateTime : Edm.DateTimeOffset "Created At"
PX.SM.AU.SMEmail.LastModifiedByID : Edm.Guid "Last Modified By"
PX.SM.AU.SMEmail.LastModifiedByScreenID : Edm.String
PX.SM.AU.SMEmail.LastModifiedDateTime : Edm.DateTimeOffset
PX.SM.AU.SMEmail.tstamp : Edm.Binary
PX.SM.AU.SMEmail.DeletedDatabaseRecord : Edm.Boolean [required] "DeletedDatabaseRecord"
PX.SM.AU.SMEmail.CRActivityByRefNoteID -> PX.Objects.CR.CRActivity (RefNoteID=NoteID)
PX.SM.AU.SMEmail.UsersByCreatedByID -> PX.SM.Users (CreatedByID=PKID)
PX.SM.AU.SMEmail.UsersByLastModifiedByID -> PX.SM.Users (LastModifiedByID=PKID)
PX.SM.AU.SMEmail.EMailAccountByMailAccountID -> PX.SM.EMailAccount (MailAccountID=EmailAccountID)
PX.SM.AU.SMEmail.CRSMEmailCollection -> Collection(PX.Objects.CR.CRSMEmail)
PX.SM.AU.SMEmail.SMSendGridRecipientCollection -> Collection(PX.DataSync.SendGrid.SMSendGridRecipient)
PX.SM.AU.SMEmail.EmailLogCollection -> Collection(PX.Mail.Log.DAC.EmailLog)

# PX.SM.AUAction (EntityType)

Key: ActionName, MenuText, ScreenID
Entity sets: PX_SM_AUAction

PX.SM.AUAction.ScreenID : Edm.String [key]
PX.SM.AUAction.ActionName : Edm.String [key]
PX.SM.AUAction.MenuText : Edm.String [key] "Menu Text"
PX.SM.AUAction.MenuIcon : Edm.String "Icon"
PX.SM.AUAction.RefCntr : Edm.Int16 [required]
PX.SM.AUAction.RowNbr : Edm.Int16
PX.SM.AUAction.OrderNbr : Edm.Int16
PX.SM.AUAction.CreatedByID : Edm.Guid "Created By"
PX.SM.AUAction.CreatedByScreenID : Edm.String
PX.SM.AUAction.CreatedDateTime : Edm.DateTimeOffset
PX.SM.AUAction.LastModifiedByID : Edm.Guid "Last Modified By"
PX.SM.AUAction.LastModifiedByScreenID : Edm.String
PX.SM.AUAction.LastModifiedDateTime : Edm.DateTimeOffset
PX.SM.AUAction.TStamp : Edm.Binary
PX.SM.AUAction.UsersByCreatedByID -> PX.SM.Users (CreatedByID=PKID)
PX.SM.AUAction.UsersByLastModifiedByID -> PX.SM.Users (LastModifiedByID=PKID)

# PX.SM.AUArchivingRule (EntityType)

Label: "Archiving Rule"
Key: PrimaryType, ScreenID, TableType
Entity sets: PX_SM_AUArchivingRule, ArchivingRule, AUArchivingRule

PX.SM.AUArchivingRule.IsActive : Edm.Boolean [required] "Active"
PX.SM.AUArchivingRule.IsSystem : Edm.Boolean [required] "System"
PX.SM.AUArchivingRule.ScreenID : Edm.String [key]
PX.SM.AUArchivingRule.PrimaryType : Edm.String [key]
PX.SM.AUArchivingRule.TableType : Edm.String [key]
PX.SM.AUArchivingRule.ReferStrategy : Edm.Int32
PX.SM.AUArchivingRule.FKType : Edm.String
PX.SM.AUArchivingRule.SelectType : Edm.String
PX.SM.AUArchivingRule.IsParentToPrimary : Edm.Boolean

# PX.SM.AUAuditField (EntityType)

Key: FieldName, ScreenID, TableName
Entity sets: PX_SM_AUAuditField
Non-filterable, non-selectable: IsInserted, FieldType, FieldDisplayName

PX.SM.AUAuditField.IsActive : Edm.Boolean [required] "Active"
PX.SM.AUAuditField.ScreenID : Edm.String [key] "Screen Name"
PX.SM.AUAuditField.TableName : Edm.String [key] "Table Name"
PX.SM.AUAuditField.FieldName : Edm.String [key] "Field Name"
PX.SM.AUAuditField.IsInserted : Edm.Boolean
PX.SM.AUAuditField.FieldType : Edm.Int32
PX.SM.AUAuditField.FieldDisplayName : Edm.String "Field"
PX.SM.AUAuditField.AUAuditTableByTableName -> PX.SM.AUAuditTable (ScreenID=ScreenID, TableName=TableName)

# PX.SM.AUAuditHistoryStatistics (EntityType)

Label: "Audit History Statistics"
Key: TableName
Entity sets: PX_SM_AUAuditHistoryStatistics, AuditHistoryStatistics, AUAuditHistoryStatistics
Non-filterable, non-selectable: NoteText

PX.SM.AUAuditHistoryStatistics.TableName : Edm.String [key] "Table Name"
PX.SM.AUAuditHistoryStatistics.ScreenNames : Edm.String "Screen IDs"
PX.SM.AUAuditHistoryStatistics.HistoryRecordQuantity : Edm.Int32 "Latest History Record Count"
PX.SM.AUAuditHistoryStatistics.LastPurgedBefore : Edm.DateTimeOffset "Purged Up To"
PX.SM.AUAuditHistoryStatistics.LastPurgedOn : Edm.DateTimeOffset "Last Purged On"
PX.SM.AUAuditHistoryStatistics.LastPurgedBy : Edm.Guid "Last Purged By"
PX.SM.AUAuditHistoryStatistics.NoteID : Edm.Guid
PX.SM.AUAuditHistoryStatistics.NoteText : Edm.String "Note Text"
PX.SM.AUAuditHistoryStatistics.UsersByLastPurgedBy -> PX.SM.Users (LastPurgedBy=PKID)

# PX.SM.AUAuditHistoryStatisticsCalculationHistory (EntityType)

Label: "Audit History Statistics Calculation History"
Singletons: PX_SM_AUAuditHistoryStatisticsCalculationHistory, AuditHistoryStatisticsCalculationHistory, AUAuditHistoryStatisticsCalculationHistory

PX.SM.AUAuditHistoryStatisticsCalculationHistory.LastCalculated : Edm.DateTimeOffset "History Last Calculated On"

# PX.SM.AUAuditSetup (EntityType)

Key: ScreenID
Entity sets: PX_SM_AUAuditSetup
Non-filterable, non-selectable: ScreenName, VirtualScreenID

PX.SM.AUAuditSetup.ScreenID : Edm.String [key] "Audited Screen ID"
PX.SM.AUAuditSetup.IsActive : Edm.Boolean [required] "Active"
PX.SM.AUAuditSetup.Description : Edm.String "Description"
PX.SM.AUAuditSetup.ShowFieldsType : Edm.Int32 "Show Fields"
PX.SM.AUAuditSetup.CreatedByID : Edm.Guid "Created By"
PX.SM.AUAuditSetup.CreatedByScreenID : Edm.String
PX.SM.AUAuditSetup.CreatedDateTime : Edm.DateTimeOffset "Created On"
PX.SM.AUAuditSetup.LastModifiedByID : Edm.Guid "Last Modified By"
PX.SM.AUAuditSetup.LastModifiedByScreenID : Edm.String
PX.SM.AUAuditSetup.LastModifiedDateTime : Edm.DateTimeOffset
PX.SM.AUAuditSetup.ScreenName : Edm.String "Screen Name"
PX.SM.AUAuditSetup.VirtualScreenID : Edm.String "Screen ID"
PX.SM.AUAuditSetup.UsersByCreatedByID -> PX.SM.Users (CreatedByID=PKID)
PX.SM.AUAuditSetup.UsersByLastModifiedByID -> PX.SM.Users (LastModifiedByID=PKID)
PX.SM.AUAuditSetup.AUAuditTableCollection -> Collection(PX.SM.AUAuditTable)

# PX.SM.AUAuditTable (EntityType)

Key: ScreenID, TableName
Entity sets: PX_SM_AUAuditTable
Non-filterable, non-selectable: IsInserted, TableDisplayName

PX.SM.AUAuditTable.IsActive : Edm.Boolean [required] "Active"
PX.SM.AUAuditTable.ScreenID : Edm.String [key] "Screen Name"
PX.SM.AUAuditTable.TableName : Edm.String [key] "Table"
PX.SM.AUAuditTable.ShowFieldsType : Edm.Int32 [required] "Show Fields"
PX.SM.AUAuditTable.TableType : Edm.String
PX.SM.AUAuditTable.Keys : Edm.String
PX.SM.AUAuditTable.IsInserted : Edm.Boolean
PX.SM.AUAuditTable.TableDisplayName : Edm.String "Description"
PX.SM.AUAuditTable.AUAuditSetupByScreenID -> PX.SM.AUAuditSetup (ScreenID=ScreenID)
PX.SM.AUAuditTable.AUAuditFieldCollection -> Collection(PX.SM.AUAuditField)

# PX.SM.AUAuditValues (EntityType)

BaseType: PX.SM.AuditHistory
Key: BatchID, ChangeID (inherited from PX.SM.AuditHistory)
Entity sets: PX_SM_AUAuditValues
Filterable: false (fields declared in this DAC cannot be used in $filter or $select; inherited ones can)

PX.SM.AUAuditValues.UserName : Edm.String "User Name"

# PX.SM.AUCombo (EntityType)

Key: FieldName, TableName, Value
Entity sets: PX_SM_AUCombo

PX.SM.AUCombo.TableName : Edm.String [key]
PX.SM.AUCombo.FieldName : Edm.String [key]
PX.SM.AUCombo.IsExplicit : Edm.Boolean [required] "Explicit"
PX.SM.AUCombo.Value : Edm.String [key]
PX.SM.AUCombo.Description : Edm.String
PX.SM.AUCombo.RefCntr : Edm.Int16 [required]
PX.SM.AUCombo.RowNbr : Edm.Int16
PX.SM.AUCombo.CreatedByID : Edm.Guid "Created By"
PX.SM.AUCombo.CreatedByScreenID : Edm.String
PX.SM.AUCombo.CreatedDateTime : Edm.DateTimeOffset
PX.SM.AUCombo.LastModifiedByID : Edm.Guid "Last Modified By"
PX.SM.AUCombo.LastModifiedByScreenID : Edm.String
PX.SM.AUCombo.LastModifiedDateTime : Edm.DateTimeOffset
PX.SM.AUCombo.TStamp : Edm.Binary
PX.SM.AUCombo.UsersByCreatedByID -> PX.SM.Users (CreatedByID=PKID)
PX.SM.AUCombo.UsersByLastModifiedByID -> PX.SM.Users (LastModifiedByID=PKID)

# PX.SM.AUDefinition (EntityType)

Key: DefinitionID
Entity sets: PX_SM_AUDefinition
Non-filterable, non-selectable: NoteText

PX.SM.AUDefinition.DefinitionID : Edm.String [key] "Definition ID"
PX.SM.AUDefinition.Description : Edm.String "Description"
PX.SM.AUDefinition.DetailsXml : Edm.String "Definition Details"
PX.SM.AUDefinition.NoteID : Edm.Guid
PX.SM.AUDefinition.NoteText : Edm.String "Note Text"
PX.SM.AUDefinition.CreatedByID : Edm.Guid "Created By"
PX.SM.AUDefinition.CreatedByScreenID : Edm.String
PX.SM.AUDefinition.CreatedDateTime : Edm.DateTimeOffset
PX.SM.AUDefinition.LastModifiedByID : Edm.Guid "Last Modified By"
PX.SM.AUDefinition.LastModifiedByScreenID : Edm.String
PX.SM.AUDefinition.LastModifiedDateTime : Edm.DateTimeOffset
PX.SM.AUDefinition.TStamp : Edm.Binary
PX.SM.AUDefinition.UsersByCreatedByID -> PX.SM.Users (CreatedByID=PKID)
PX.SM.AUDefinition.UsersByLastModifiedByID -> PX.SM.Users (LastModifiedByID=PKID)

# PX.SM.AUDefinitionDetail (EntityType)

Key: DefinitionID, ScreenID
Entity sets: PX_SM_AUDefinitionDetail
Non-filterable, non-selectable: NoteText

PX.SM.AUDefinitionDetail.DefinitionID : Edm.String [key]
PX.SM.AUDefinitionDetail.ScreenID : Edm.String [key] "Screen ID"
PX.SM.AUDefinitionDetail.TableName : Edm.String
PX.SM.AUDefinitionDetail.Steps : Edm.String "Steps"
PX.SM.AUDefinitionDetail.Content : Edm.String
PX.SM.AUDefinitionDetail.NoteID : Edm.Guid
PX.SM.AUDefinitionDetail.NoteText : Edm.String "Note Text"
PX.SM.AUDefinitionDetail.CreatedByID : Edm.Guid "Created By"
PX.SM.AUDefinitionDetail.CreatedByScreenID : Edm.String
PX.SM.AUDefinitionDetail.CreatedDateTime : Edm.DateTimeOffset
PX.SM.AUDefinitionDetail.LastModifiedByID : Edm.Guid "Last Modified By"
PX.SM.AUDefinitionDetail.LastModifiedByScreenID : Edm.String
PX.SM.AUDefinitionDetail.LastModifiedDateTime : Edm.DateTimeOffset
PX.SM.AUDefinitionDetail.TStamp : Edm.Binary
PX.SM.AUDefinitionDetail.UsersByCreatedByID -> PX.SM.Users (CreatedByID=PKID)
PX.SM.AUDefinitionDetail.UsersByLastModifiedByID -> PX.SM.Users (LastModifiedByID=PKID)

# PX.SM.AuditHistory (EntityType)

Key: BatchID, ChangeID
Entity sets: PX_SM_AuditHistory

PX.SM.AuditHistory.BatchID : Edm.Int64 [key] "Batch ID"
PX.SM.AuditHistory.ChangeID : Edm.Int64 [key] "Change ID"
PX.SM.AuditHistory.ScreenID : Edm.String "Screen Name"
PX.SM.AuditHistory.UserID : Edm.Guid "User"
PX.SM.AuditHistory.ChangeDate : Edm.DateTimeOffset "Date and Time"
PX.SM.AuditHistory.Operation : Edm.String "Operation"
PX.SM.AuditHistory.TableName : Edm.String "TableName"
PX.SM.AuditHistory.CombinedKey : Edm.String
PX.SM.AuditHistory.ModifiedFields : Edm.String
PX.SM.AuditHistory.UsersByUserID -> PX.SM.Users (UserID=PKID)

# PX.SM.AUNotification (EntityType)

Key: NotificationID, ScreenID
Entity sets: PX_SM_AUNotification
Non-filterable, non-selectable: NoteText, DeletedDatabaseRecord

PX.SM.AUNotification.ScreenID : Edm.String [key] "Screen ID"
PX.SM.AUNotification.NotificationID : Edm.Int32 [key] "Notification ID"
PX.SM.AUNotification.ParentNotificationID : Edm.Int32 "Parent Notification ID"
PX.SM.AUNotification.Description : Edm.String "Description"
PX.SM.AUNotification.IsActive : Edm.Boolean [required] "Active"
PX.SM.AUNotification.IsPublic : Edm.Boolean [required] "Public"
PX.SM.AUNotification.Subject : Edm.String "Subject"
PX.SM.AUNotification.Body : Edm.String "Body"
PX.SM.AUNotification.CreationMethod : Edm.String "Data Source"
PX.SM.AUNotification.ReportID : Edm.String "Report ID"
PX.SM.AUNotification.ReportFormat : Edm.String "Report Format"
PX.SM.AUNotification.IsEmbeded : Edm.Boolean [required] "Embedded"
PX.SM.AUNotification.ActionName : Edm.String "Action Name"
PX.SM.AUNotification.MenuText : Edm.String "Menu Text"
PX.SM.AUNotification.GraphName : Edm.String
PX.SM.AUNotification.ViewName : Edm.String
PX.SM.AUNotification.TableName : Edm.String
PX.SM.AUNotification.BqlTableName : Edm.String
PX.SM.AUNotification.FilterCntr : Edm.Int16 [required]
PX.SM.AUNotification.ContentCntr : Edm.Int16 [required]
PX.SM.AUNotification.AddressCntr : Edm.Int16 [required]
PX.SM.AUNotification.ParameterCntr : Edm.Int16 [required]
PX.SM.AUNotification.NoteID : Edm.Guid
PX.SM.AUNotification.NoteText : Edm.String "Note Text"
PX.SM.AUNotification.CreatedByID : Edm.Guid "Created By"
PX.SM.AUNotification.CreatedByScreenID : Edm.String
PX.SM.AUNotification.CreatedDateTime : Edm.DateTimeOffset
PX.SM.AUNotification.LastModifiedByID : Edm.Guid "Last Modified By"
PX.SM.AUNotification.LastModifiedByScreenID : Edm.String
PX.SM.AUNotification.LastModifiedDateTime : Edm.DateTimeOffset
PX.SM.AUNotification.TStamp : Edm.Binary
PX.SM.AUNotification.DeletedDatabaseRecord : Edm.Boolean [required] "DeletedDatabaseRecord"
PX.SM.AUNotification.UsersByCreatedByID -> PX.SM.Users (CreatedByID=PKID)
PX.SM.AUNotification.UsersByLastModifiedByID -> PX.SM.Users (LastModifiedByID=PKID)
PX.SM.AUNotification.AUNotificationByParentNotificationID -> PX.SM.AUNotification (ParentNotificationID=NotificationID)
PX.SM.AUNotification.AUNotificationCollection -> Collection(PX.SM.AUNotification)
PX.SM.AUNotification.AUNotificationFieldCollection -> Collection(PX.SM.AUNotificationField)
PX.SM.AUNotification.AUNotificationFilterCollection -> Collection(PX.SM.AUNotificationFilter)
PX.SM.AUNotification.AUNotificationParameterCollection -> Collection(PX.SM.AUNotificationParameter)
PX.SM.AUNotification.AUNotificationHistoryCollection -> Collection(PX.SM.AUNotificationHistory)
PX.SM.AUNotification.AUNotificationTemplateCollection -> Collection(PX.SM.AUNotificationTemplate)

# PX.SM.AUNotificationField (EntityType)

Key: NotificationID, RowNbr, ScreenID
Entity sets: PX_SM_AUNotificationField
Non-filterable, non-selectable: NoteText

PX.SM.AUNotificationField.ScreenID : Edm.String [key]
PX.SM.AUNotificationField.NotificationID : Edm.Int32 [key]
PX.SM.AUNotificationField.RowNbr : Edm.Int16 [key]
PX.SM.AUNotificationField.IsActive : Edm.Boolean [required] "Active"
PX.SM.AUNotificationField.FieldName : Edm.String "Field Name"
PX.SM.AUNotificationField.NoteID : Edm.Guid
PX.SM.AUNotificationField.NoteText : Edm.String "Note Text"
PX.SM.AUNotificationField.CreatedByID : Edm.Guid "Created By"
PX.SM.AUNotificationField.CreatedByScreenID : Edm.String
PX.SM.AUNotificationField.CreatedDateTime : Edm.DateTimeOffset
PX.SM.AUNotificationField.LastModifiedByID : Edm.Guid "Last Modified By"
PX.SM.AUNotificationField.LastModifiedByScreenID : Edm.String
PX.SM.AUNotificationField.LastModifiedDateTime : Edm.DateTimeOffset
PX.SM.AUNotificationField.TStamp : Edm.Binary
PX.SM.AUNotificationField.UsersByCreatedByID -> PX.SM.Users (CreatedByID=PKID)
PX.SM.AUNotificationField.UsersByLastModifiedByID -> PX.SM.Users (LastModifiedByID=PKID)
PX.SM.AUNotificationField.AUNotificationByNotificationID -> PX.SM.AUNotification (ScreenID=ScreenID, NotificationID=NotificationID)

# PX.SM.AUNotificationFilter (EntityType)

Key: NotificationID, RowNbr, ScreenID
Entity sets: PX_SM_AUNotificationFilter
Non-filterable, non-selectable: NoteText

PX.SM.AUNotificationFilter.ScreenID : Edm.String [key]
PX.SM.AUNotificationFilter.NotificationID : Edm.Int32 [key]
PX.SM.AUNotificationFilter.RowNbr : Edm.Int16 [key]
PX.SM.AUNotificationFilter.IsActive : Edm.Boolean [required] "Active"
PX.SM.AUNotificationFilter.OpenBrackets : Edm.Int32 [required] "Brackets"
PX.SM.AUNotificationFilter.FieldName : Edm.String "Field Name"
PX.SM.AUNotificationFilter.Condition : Edm.Int32 [required] "Condition"
PX.SM.AUNotificationFilter.IsRelative : Edm.Boolean [required] "Is Relative"
PX.SM.AUNotificationFilter.Value : Edm.String "Value"
PX.SM.AUNotificationFilter.Value2 : Edm.String "Value 2"
PX.SM.AUNotificationFilter.CloseBrackets : Edm.Int32 [required] "Brackets"
PX.SM.AUNotificationFilter.Operator : Edm.Int32 [required] "Operator"
PX.SM.AUNotificationFilter.RefNoteID : Edm.Guid
PX.SM.AUNotificationFilter.NoteID : Edm.Guid
PX.SM.AUNotificationFilter.NoteText : Edm.String "Note Text"
PX.SM.AUNotificationFilter.CreatedByID : Edm.Guid "Created By"
PX.SM.AUNotificationFilter.CreatedByScreenID : Edm.String
PX.SM.AUNotificationFilter.CreatedDateTime : Edm.DateTimeOffset
PX.SM.AUNotificationFilter.LastModifiedByID : Edm.Guid "Last Modified By"
PX.SM.AUNotificationFilter.LastModifiedByScreenID : Edm.String
PX.SM.AUNotificationFilter.LastModifiedDateTime : Edm.DateTimeOffset
PX.SM.AUNotificationFilter.TStamp : Edm.Binary
PX.SM.AUNotificationFilter.UsersByCreatedByID -> PX.SM.Users (CreatedByID=PKID)
PX.SM.AUNotificationFilter.UsersByLastModifiedByID -> PX.SM.Users (LastModifiedByID=PKID)
PX.SM.AUNotificationFilter.AUNotificationByNotificationID -> PX.SM.AUNotification (ScreenID=ScreenID, NotificationID=NotificationID)

# PX.SM.AUNotificationHistory (EntityType)

Key: ExecutionDate, NotificationID, RefNoteID, ScreenID, Ticks
Entity sets: PX_SM_AUNotificationHistory
Non-filterable, non-selectable: Ticks, BodyVirtual

PX.SM.AUNotificationHistory.ScreenID : Edm.String [key]
PX.SM.AUNotificationHistory.NotificationID : Edm.Int32 [key] "Notification ID"
PX.SM.AUNotificationHistory.Exception : Edm.String "Error Message"
PX.SM.AUNotificationHistory.ExecutionDate : Edm.DateTimeOffset [key] "Execution Date"
PX.SM.AUNotificationHistory.Status : Edm.String "Status"
PX.SM.AUNotificationHistory.DateSent : Edm.DateTimeOffset "Date Sent"
PX.SM.AUNotificationHistory.RefNoteID : Edm.Guid [key]
PX.SM.AUNotificationHistory.FieldValues : Edm.String "Field Values"
PX.SM.AUNotificationHistory.MailDate : Edm.DateTimeOffset
PX.SM.AUNotificationHistory.MailAccountID : Edm.Int32 "From"
PX.SM.AUNotificationHistory.MailFrom : Edm.String "From"
PX.SM.AUNotificationHistory.MailTo : Edm.String "To"
PX.SM.AUNotificationHistory.MailCc : Edm.String "Cc"
PX.SM.AUNotificationHistory.MailBcc : Edm.String "Bcc"
PX.SM.AUNotificationHistory.MailReply : Edm.String "Reply"
PX.SM.AUNotificationHistory.Subject : Edm.String "Subject"
PX.SM.AUNotificationHistory.Body : Edm.String "Body"
PX.SM.AUNotificationHistory.MessageId : Edm.String "MessageId"
PX.SM.AUNotificationHistory.ReportID : Edm.String "Report ID"
PX.SM.AUNotificationHistory.ReportFormat : Edm.String "Report Format"
PX.SM.AUNotificationHistory.Resultset : Edm.String "Resultset"
PX.SM.AUNotificationHistory.Ticks : Edm.Int64 [key] "Ticks"
PX.SM.AUNotificationHistory.BodyVirtual : Edm.String "Body"
PX.SM.AUNotificationHistory.SMEmailNoteID : Edm.Guid
PX.SM.AUNotificationHistory.EmailRefNoteID : Edm.Guid
PX.SM.AUNotificationHistory.EmailReportFormat : Edm.String
PX.SM.AUNotificationHistory.EmailNoteID : Edm.Guid
PX.SM.AUNotificationHistory.RetryCount : Edm.Int32 "RetryCount"
PX.SM.AUNotificationHistory.MPStatus : Edm.String "Mail Status"
PX.SM.AUNotificationHistory.ImcUID : Edm.Guid "ImcUID"
PX.SM.AUNotificationHistory.CreatedByID : Edm.Guid "Created By"
PX.SM.AUNotificationHistory.CreatedByScreenID : Edm.String
PX.SM.AUNotificationHistory.CreatedDateTime : Edm.DateTimeOffset "Created At"
PX.SM.AUNotificationHistory.LastModifiedByID : Edm.Guid "Last Modified By"
PX.SM.AUNotificationHistory.LastModifiedByScreenID : Edm.String
PX.SM.AUNotificationHistory.LastModifiedDateTime : Edm.DateTimeOffset
PX.SM.AUNotificationHistory.AUNotificationByScreenID -> PX.SM.AUNotification (NotificationID=NotificationID, ScreenID=ScreenID)
PX.SM.AUNotificationHistory.AUNotificationByNotificationID -> PX.SM.AUNotification (NotificationID=NotificationID)

# PX.SM.AUNotificationParameter (EntityType)

Key: NotificationID, RowNbr, ScreenID
Entity sets: PX_SM_AUNotificationParameter
Non-filterable, non-selectable: NoteText

PX.SM.AUNotificationParameter.ScreenID : Edm.String [key]
PX.SM.AUNotificationParameter.NotificationID : Edm.Int32 [key]
PX.SM.AUNotificationParameter.RowNbr : Edm.Int16 [key]
PX.SM.AUNotificationParameter.IsActive : Edm.Boolean [required] "Active"
PX.SM.AUNotificationParameter.ParameterName : Edm.String "Parameter Name"
PX.SM.AUNotificationParameter.Value : Edm.String "Value"
PX.SM.AUNotificationParameter.NoteID : Edm.Guid
PX.SM.AUNotificationParameter.NoteText : Edm.String "Note Text"
PX.SM.AUNotificationParameter.CreatedByID : Edm.Guid "Created By"
PX.SM.AUNotificationParameter.CreatedByScreenID : Edm.String
PX.SM.AUNotificationParameter.CreatedDateTime : Edm.DateTimeOffset
PX.SM.AUNotificationParameter.LastModifiedByID : Edm.Guid "Last Modified By"
PX.SM.AUNotificationParameter.LastModifiedByScreenID : Edm.String
PX.SM.AUNotificationParameter.LastModifiedDateTime : Edm.DateTimeOffset
PX.SM.AUNotificationParameter.TStamp : Edm.Binary
PX.SM.AUNotificationParameter.UsersByCreatedByID -> PX.SM.Users (CreatedByID=PKID)
PX.SM.AUNotificationParameter.UsersByLastModifiedByID -> PX.SM.Users (LastModifiedByID=PKID)
PX.SM.AUNotificationParameter.AUNotificationByNotificationID -> PX.SM.AUNotification (ScreenID=ScreenID, NotificationID=NotificationID)

# PX.SM.AUNotificationTemplate (EntityType)

Key: ExecutionDate, NotificationID, RefNoteID, ScreenID
Entity sets: PX_SM_AUNotificationTemplate
Non-filterable, non-selectable: Ticks

PX.SM.AUNotificationTemplate.ScreenID : Edm.String [key]
PX.SM.AUNotificationTemplate.NotificationID : Edm.Int32 [key] "Notification ID"
PX.SM.AUNotificationTemplate.ExecutionDate : Edm.DateTimeOffset [key] "Execution Date"
PX.SM.AUNotificationTemplate.Status : Edm.String "Status"
PX.SM.AUNotificationTemplate.DateSent : Edm.DateTimeOffset "Date Sent"
PX.SM.AUNotificationTemplate.RefNoteID : Edm.Guid [key]
PX.SM.AUNotificationTemplate.ReportID : Edm.String "Report ID"
PX.SM.AUNotificationTemplate.ReportFormat : Edm.String "Report Format"
PX.SM.AUNotificationTemplate.Resultset : Edm.String "Resultset"
PX.SM.AUNotificationTemplate.FieldValues : Edm.String "Field Values"
PX.SM.AUNotificationTemplate.Ticks : Edm.Int64 "Ticks"
PX.SM.AUNotificationTemplate.TStamp : Edm.Binary
PX.SM.AUNotificationTemplate.EmailNoteID : Edm.Guid
PX.SM.AUNotificationTemplate.AUNotificationByNotificationID -> PX.SM.AUNotification (NotificationID=NotificationID)

# PX.SM.AUReportLink (EntityType)

Label: "Report Link"
Key: RowNbr, ScheduleID, TemplateID
Entity sets: PX_SM_AUReportLink, ReportLink, AUReportLink

PX.SM.AUReportLink.TemplateID : Edm.Guid [key]
PX.SM.AUReportLink.ScheduleID : Edm.Int32 [key]
PX.SM.AUReportLink.RowNbr : Edm.Int16 [key]
PX.SM.AUReportLink.AUScheduleByScheduleID -> PX.SM.AUSchedule (ScheduleID=ScheduleID)

# PX.SM.AUSchedule (EntityType)

Label: "Schedule"
Key: ScheduleID
Entity sets: PX_SM_AUSchedule, Schedule1, AUSchedule
Non-filterable, non-selectable: DailyLabel, WeeklyLabel, MonthlyLabel, PeriodLabel, LastRunStatus, NoteText, ShowEventsTabExpr, ShowConditionsTabExpr, ShowEmailNotificationsTabExpr, CreatedFromBusinessEvent, NextRunDateTime, IsCreatedFromNotification, DeletedDatabaseRecord

PX.SM.AUSchedule.ScreenID : Edm.String "Screen ID"
PX.SM.AUSchedule.ScheduleID : Edm.Int32 [key] "Schedule ID"
PX.SM.AUSchedule.Description : Edm.String "Description"
PX.SM.AUSchedule.GraphName : Edm.String
PX.SM.AUSchedule.ViewName : Edm.String
PX.SM.AUSchedule.FilterName : Edm.String
PX.SM.AUSchedule.TableName : Edm.String
PX.SM.AUSchedule.FilterCntr : Edm.Int16 [required]
PX.SM.AUSchedule.FillCntr : Edm.Int16 [required]
PX.SM.AUSchedule.AbortCntr : Edm.Int16 [required]
PX.SM.AUSchedule.MaxAbortCount : Edm.Int16 [required] "Max Consecutive Aborted Executions"
PX.SM.AUSchedule.DoNotDeactivate : Edm.Boolean [required] "Do Not Deactivate"
PX.SM.AUSchedule.IsActive : Edm.Boolean [required] "Active"
PX.SM.AUSchedule.Action : Edm.String "Action"
PX.SM.AUSchedule.ActionName : Edm.String "Action Name"
PX.SM.AUSchedule.TimeZoneID : Edm.String "Time Zone"
PX.SM.AUSchedule.ScheduleType : Edm.String "Frequency"
PX.SM.AUSchedule.DailyFrequency : Edm.Int16 [required] "Every"
PX.SM.AUSchedule.DailyLabel : Edm.String "Day(s)"
PX.SM.AUSchedule.WeeklyFrequency : Edm.Int16 [required] "Every"
PX.SM.AUSchedule.WeeklyLabel : Edm.String "Week(s)"
PX.SM.AUSchedule.WeeklyOnDay1 : Edm.Boolean [required] "Sunday"
PX.SM.AUSchedule.WeeklyOnDay2 : Edm.Boolean [required] "Monday"
PX.SM.AUSchedule.WeeklyOnDay3 : Edm.Boolean [required] "Tuesday"
PX.SM.AUSchedule.WeeklyOnDay4 : Edm.Boolean [required] "Wednesday"
PX.SM.AUSchedule.WeeklyOnDay5 : Edm.Boolean [required] "Thursday"
PX.SM.AUSchedule.WeeklyOnDay6 : Edm.Boolean [required] "Friday"
PX.SM.AUSchedule.WeeklyOnDay7 : Edm.Boolean [required] "Saturday"
PX.SM.AUSchedule.MonthlyFrequency : Edm.Int16 [required] "Every"
PX.SM.AUSchedule.MonthlyLabel : Edm.String "Month(s)"
PX.SM.AUSchedule.MonthlyDaySel : Edm.String "Day Based On"
PX.SM.AUSchedule.MonthlyOnDay : Edm.Int16 [required] "On Day"
PX.SM.AUSchedule.MonthlyOnWeek : Edm.Int16 [required] "On the"
PX.SM.AUSchedule.MonthlyOnDayOfWeek : Edm.Int16 [required] "Day Of Week"
PX.SM.AUSchedule.PeriodFrequency : Edm.Int16 [required] "Every"
PX.SM.AUSchedule.PeriodLabel : Edm.String "Period(s)"
PX.SM.AUSchedule.PeriodDateSel : Edm.String "Date Based On"
PX.SM.AUSchedule.PeriodFixedDay : Edm.Int16 [required] "Fixed Day of the Period"
PX.SM.AUSchedule.StartDate : Edm.DateTimeOffset "Starts On"
PX.SM.AUSchedule.NoEndDate : Edm.Boolean [required] "No Expiration Date"
PX.SM.AUSchedule.EndDate : Edm.DateTimeOffset "Expires On"
PX.SM.AUSchedule.NoRunLimit : Edm.Boolean [required] "No Execution Limit"
PX.SM.AUSchedule.RunLimit : Edm.Int16 "Execution Limit"
PX.SM.AUSchedule.RunCntr : Edm.Int32 [required] "Executed"
PX.SM.AUSchedule.NextRunDate : Edm.DateTimeOffset "Next Execution Date"
PX.SM.AUSchedule.LastRunDate : Edm.DateTimeOffset "Last Executed"
PX.SM.AUSchedule.LastRunStatus : Edm.String "Status"
PX.SM.AUSchedule.LastRunErrorLevel : Edm.Int16 [required]
PX.SM.AUSchedule.LastRunResult : Edm.String "Last Execution Result"
PX.SM.AUSchedule.StartTime : Edm.DateTimeOffset "Start Time"
PX.SM.AUSchedule.EndTime : Edm.DateTimeOffset "Stop Time"
PX.SM.AUSchedule.Interval : Edm.Int16 [required] "Every (hh:mm)"
PX.SM.AUSchedule.NextRunTime : Edm.DateTimeOffset "Next Execution Time"
PX.SM.AUSchedule.TemplateScreenID : Edm.String "Screen ID"
PX.SM.AUSchedule.ExactTime : Edm.Boolean [required] "Exact Time"
PX.SM.AUSchedule.NoteID : Edm.Guid
PX.SM.AUSchedule.NoteText : Edm.String "Note Text"
PX.SM.AUSchedule.CreatedByID : Edm.Guid "Created By"
PX.SM.AUSchedule.CreatedByScreenID : Edm.String
PX.SM.AUSchedule.CreatedDateTime : Edm.DateTimeOffset
PX.SM.AUSchedule.LastModifiedByID : Edm.Guid "Last Modified By"
PX.SM.AUSchedule.LastModifiedByScreenID : Edm.String
PX.SM.AUSchedule.LastModifiedDateTime : Edm.DateTimeOffset
PX.SM.AUSchedule.TStamp : Edm.Binary
PX.SM.AUSchedule.HistoryRetainCount : Edm.Int16 "Executions to Keep in History"
PX.SM.AUSchedule.KeepFullHistory : Edm.Boolean [required] "Keep Full History"
PX.SM.AUSchedule.ShowEventsTabExpr : Edm.Boolean "ShowEventsTabExpr"
PX.SM.AUSchedule.ShowConditionsTabExpr : Edm.Boolean
PX.SM.AUSchedule.ShowEmailNotificationsTabExpr : Edm.Boolean
PX.SM.AUSchedule.CreatedFromBusinessEvent : Edm.Boolean
PX.SM.AUSchedule.NextRunDateTime : Edm.DateTimeOffset "Next Execution"
PX.SM.AUSchedule.IsCreatedFromNotification : Edm.Boolean
PX.SM.AUSchedule.DeletedDatabaseRecord : Edm.Boolean [required] "DeletedDatabaseRecord"
PX.SM.AUSchedule.SiteMapByScreenID -> PX.SM.SiteMap (ScreenID=ScreenID)
PX.SM.AUSchedule.BAccountByBranchID -> PX.Objects.CR.BAccount
PX.SM.AUSchedule.BranchByBranchID -> PX.Objects.GL.Branch
PX.SM.AUSchedule.UsersByCreatedByID -> PX.SM.Users (CreatedByID=PKID)
PX.SM.AUSchedule.UsersByLastModifiedByID -> PX.SM.Users (LastModifiedByID=PKID)
PX.SM.AUSchedule.AUScheduleFillCollection -> Collection(PX.SM.AUScheduleFill)
PX.SM.AUSchedule.AUScheduleFilterCollection -> Collection(PX.SM.AUScheduleFilter)
PX.SM.AUSchedule.NotificationScheduleCollection -> Collection(PX.Data.Maintenance.SM.SendRecurringNotifications.NotificationSchedule)
PX.SM.AUSchedule.AUReportLinkCollection -> Collection(PX.SM.AUReportLink)
PX.SM.AUSchedule.AUScheduleExecutionCollection -> Collection(PX.SM.AUScheduleExecution)
PX.SM.AUSchedule.AUScheduleHistoryCollection -> Collection(PX.SM.AUScheduleHistory)
PX.SM.AUSchedule.BPEventScheduleCollection -> Collection(PX.BusinessProcess.DAC.BPEventSchedule)

# PX.SM.AUScheduleExecution (EntityType)

Key: ExecutionDate, ScheduleID
Entity sets: PX_SM_AUScheduleExecution
Non-filterable, non-selectable: ExecutionDateToDisplay, Status, Result

PX.SM.AUScheduleExecution.ScreenID : Edm.String "Screen ID"
PX.SM.AUScheduleExecution.ScheduleID : Edm.Int32 [key] "Schedule"
PX.SM.AUScheduleExecution.ExecutionDate : Edm.DateTimeOffset [key] "Execution Date"
PX.SM.AUScheduleExecution.ExecutionDateToDisplay : Edm.DateTimeOffset "Execution Date"
PX.SM.AUScheduleExecution.ProcessedCount : Edm.Int32 "Processed"
PX.SM.AUScheduleExecution.WarningsCount : Edm.Int32 "Warnings"
PX.SM.AUScheduleExecution.ErrorsCount : Edm.Int32 "Errors"
PX.SM.AUScheduleExecution.TotalCount : Edm.Int32 "Total Records"
PX.SM.AUScheduleExecution.TStamp : Edm.Binary
PX.SM.AUScheduleExecution.Status : Edm.String "Status"
PX.SM.AUScheduleExecution.Result : Edm.String "Execution Result"
PX.SM.AUScheduleExecution.AUScheduleByScheduleID -> PX.SM.AUSchedule (ScheduleID=ScheduleID)

# PX.SM.AUScheduleFill (EntityType)

Label: "Schedule Filter Values"
Key: RowNbr, ScheduleID
Entity sets: PX_SM_AUScheduleFill, ScheduleFilterValues, AUScheduleFill
Non-filterable, non-selectable: NoteText

PX.SM.AUScheduleFill.ScreenID : Edm.String
PX.SM.AUScheduleFill.ScheduleID : Edm.Int32 [key]
PX.SM.AUScheduleFill.RowNbr : Edm.Int16 [key]
PX.SM.AUScheduleFill.IsActive : Edm.Boolean [required] "Active"
PX.SM.AUScheduleFill.FieldName : Edm.String "Field Name"
PX.SM.AUScheduleFill.Value : Edm.String "Value"
PX.SM.AUScheduleFill.IgnoreError : Edm.Boolean [required] "Ignore Error"
PX.SM.AUScheduleFill.NoteID : Edm.Guid
PX.SM.AUScheduleFill.NoteText : Edm.String "Note Text"
PX.SM.AUScheduleFill.CreatedByID : Edm.Guid "Created By"
PX.SM.AUScheduleFill.CreatedByScreenID : Edm.String
PX.SM.AUScheduleFill.CreatedDateTime : Edm.DateTimeOffset
PX.SM.AUScheduleFill.LastModifiedByID : Edm.Guid "Last Modified By"
PX.SM.AUScheduleFill.LastModifiedByScreenID : Edm.String
PX.SM.AUScheduleFill.LastModifiedDateTime : Edm.DateTimeOffset
PX.SM.AUScheduleFill.TStamp : Edm.Binary
PX.SM.AUScheduleFill.SiteMapByScreenID -> PX.SM.SiteMap (ScreenID=ScreenID)
PX.SM.AUScheduleFill.UsersByCreatedByID -> PX.SM.Users (CreatedByID=PKID)
PX.SM.AUScheduleFill.UsersByLastModifiedByID -> PX.SM.Users (LastModifiedByID=PKID)
PX.SM.AUScheduleFill.AUScheduleByScheduleID -> PX.SM.AUSchedule (ScheduleID=ScheduleID)

# PX.SM.AUScheduleFilter (EntityType)

Label: "Schedule Filter"
Key: RowNbr, ScheduleID
Entity sets: PX_SM_AUScheduleFilter, ScheduleFilter, AUScheduleFilter
Non-filterable, non-selectable: NoteText

PX.SM.AUScheduleFilter.ScreenID : Edm.String
PX.SM.AUScheduleFilter.ScheduleID : Edm.Int32 [key]
PX.SM.AUScheduleFilter.RowNbr : Edm.Int16 [key]
PX.SM.AUScheduleFilter.IsActive : Edm.Boolean [required] "Active"
PX.SM.AUScheduleFilter.OpenBrackets : Edm.Int32 [required] "Brackets"
PX.SM.AUScheduleFilter.FieldName : Edm.String "Field Name"
PX.SM.AUScheduleFilter.Condition : Edm.Int32 [required] "Condition"
PX.SM.AUScheduleFilter.Value : Edm.String "Value"
PX.SM.AUScheduleFilter.Value2 : Edm.String "Value 2"
PX.SM.AUScheduleFilter.CloseBrackets : Edm.Int32 [required] "Brackets"
PX.SM.AUScheduleFilter.Operator : Edm.Int32 [required] "Operator"
PX.SM.AUScheduleFilter.NoteID : Edm.Guid
PX.SM.AUScheduleFilter.NoteText : Edm.String "Note Text"
PX.SM.AUScheduleFilter.CreatedByID : Edm.Guid "Created By"
PX.SM.AUScheduleFilter.CreatedByScreenID : Edm.String
PX.SM.AUScheduleFilter.CreatedDateTime : Edm.DateTimeOffset
PX.SM.AUScheduleFilter.LastModifiedByID : Edm.Guid "Last Modified By"
PX.SM.AUScheduleFilter.LastModifiedByScreenID : Edm.String
PX.SM.AUScheduleFilter.LastModifiedDateTime : Edm.DateTimeOffset
PX.SM.AUScheduleFilter.TStamp : Edm.Binary
PX.SM.AUScheduleFilter.SiteMapByScreenID -> PX.SM.SiteMap (ScreenID=ScreenID)
PX.SM.AUScheduleFilter.UsersByCreatedByID -> PX.SM.Users (CreatedByID=PKID)
PX.SM.AUScheduleFilter.UsersByLastModifiedByID -> PX.SM.Users (LastModifiedByID=PKID)
PX.SM.AUScheduleFilter.AUScheduleByScheduleID -> PX.SM.AUSchedule (ScheduleID=ScheduleID)

# PX.SM.AUScheduleHistory (EntityType)

Key: ExecutionDate, RefNoteID, ScheduleID
Entity sets: PX_SM_AUScheduleHistory
Non-filterable, non-selectable: ExecutionDateToDisplay, ExecutionStatus, Ticks

PX.SM.AUScheduleHistory.ScreenID : Edm.String
PX.SM.AUScheduleHistory.ScheduleID : Edm.Int32 [key] "Schedule ID"
PX.SM.AUScheduleHistory.ExecutionDate : Edm.DateTimeOffset [key] "Execution Date"
PX.SM.AUScheduleHistory.ExecutionDateToDisplay : Edm.DateTimeOffset "Execution Date"
PX.SM.AUScheduleHistory.RefNoteID : Edm.Guid [key]
PX.SM.AUScheduleHistory.ErrorLevel : Edm.Int16 [required] "ErrorLevel"
PX.SM.AUScheduleHistory.ExecutionResult : Edm.String "Execution Result"
PX.SM.AUScheduleHistory.TStamp : Edm.Binary
PX.SM.AUScheduleHistory.ExecutionStatus : Edm.String "Status"
PX.SM.AUScheduleHistory.Ticks : Edm.Int64 "Ticks"
PX.SM.AUScheduleHistory.AUScheduleByScheduleID -> PX.SM.AUSchedule (ScheduleID=ScheduleID)

# PX.SM.AUScheduleTemplate (EntityType)

Key: ScheduleID, TemplateID
Entity sets: PX_SM_AUScheduleTemplate
Non-filterable, non-selectable: NoteText

PX.SM.AUScheduleTemplate.ScreenID : Edm.String
PX.SM.AUScheduleTemplate.ScheduleID : Edm.Int32 [key]
PX.SM.AUScheduleTemplate.TemplateID : Edm.Int32 [key] "Template ID"
PX.SM.AUScheduleTemplate.IgnoreError : Edm.Boolean [required] "Ignore Error"
PX.SM.AUScheduleTemplate.ActionName : Edm.String "Action Name"
PX.SM.AUScheduleTemplate.NoteID : Edm.Guid
PX.SM.AUScheduleTemplate.NoteText : Edm.String "Note Text"
PX.SM.AUScheduleTemplate.CreatedByID : Edm.Guid "Created By"
PX.SM.AUScheduleTemplate.CreatedByScreenID : Edm.String
PX.SM.AUScheduleTemplate.CreatedDateTime : Edm.DateTimeOffset
PX.SM.AUScheduleTemplate.LastModifiedByID : Edm.Guid "Last Modified By"
PX.SM.AUScheduleTemplate.LastModifiedByScreenID : Edm.String
PX.SM.AUScheduleTemplate.LastModifiedDateTime : Edm.DateTimeOffset
PX.SM.AUScheduleTemplate.TStamp : Edm.Binary
PX.SM.AUScheduleTemplate.UsersByCreatedByID -> PX.SM.Users (CreatedByID=PKID)
PX.SM.AUScheduleTemplate.UsersByLastModifiedByID -> PX.SM.Users (LastModifiedByID=PKID)

# PX.SM.AUScreenAction (EntityType)

BaseType: PX.SM.AUScreenItem
Key: ItemCD, ItemType, ParentID, ProjectID, ScreenID (inherited from PX.SM.AUScreenItem)
Entity sets: PX_SM_AUScreenAction

# PX.SM.AUScreenActionBaseState (EntityType)

Key: ActionName, ScreenID
Entity sets: PX_SM_AUScreenActionBaseState

PX.SM.AUScreenActionBaseState.IsActive : Edm.Boolean "Active"
PX.SM.AUScreenActionBaseState.IsSystem : Edm.Boolean "System"
PX.SM.AUScreenActionBaseState.ScreenID : Edm.String [key]
PX.SM.AUScreenActionBaseState.ActionName : Edm.String [key] "Action Name"
PX.SM.AUScreenActionBaseState.DataMember : Edm.String "View"
PX.SM.AUScreenActionBaseState.DisplayName : Edm.String "Display Name"
PX.SM.AUScreenActionBaseState.ActionFolderType : Edm.Int32
PX.SM.AUScreenActionBaseState.MenuFolderType : Edm.Int32
PX.SM.AUScreenActionBaseState.MenuFolder : Edm.String
PX.SM.AUScreenActionBaseState.IsTopLevel : Edm.Boolean
PX.SM.AUScreenActionBaseState.Before : Edm.String
PX.SM.AUScreenActionBaseState.After : Edm.String
PX.SM.AUScreenActionBaseState.PlacementInCategory : Edm.Byte
PX.SM.AUScreenActionBaseState.AfterInMenu : Edm.String
PX.SM.AUScreenActionBaseState.IsEnabled : Edm.Boolean
PX.SM.AUScreenActionBaseState.EnableCondition : Edm.String
PX.SM.AUScreenActionBaseState.IsVisible : Edm.Boolean
PX.SM.AUScreenActionBaseState.VisibleCondition : Edm.String
PX.SM.AUScreenActionBaseState.DisableCondition : Edm.String
PX.SM.AUScreenActionBaseState.HideCondition : Edm.String
PX.SM.AUScreenActionBaseState.Form : Edm.String "Dialog Box"
PX.SM.AUScreenActionBaseState.MassProcessingScreen : Edm.String "Mass Processing Screen"
PX.SM.AUScreenActionBaseState.DisablePersist : Edm.Boolean
PX.SM.AUScreenActionBaseState.BatchMode : Edm.Boolean
PX.SM.AUScreenActionBaseState.MapEnableRights : Edm.Byte
PX.SM.AUScreenActionBaseState.MapViewRights : Edm.Byte
PX.SM.AUScreenActionBaseState.Category : Edm.String
PX.SM.AUScreenActionBaseState.ExposedToMobile : Edm.Boolean
PX.SM.AUScreenActionBaseState.IsLockedOnToolbar : Edm.Boolean
PX.SM.AUScreenActionBaseState.IgnoresArchiveDisabling : Edm.Boolean
PX.SM.AUScreenActionBaseState.Connotation : Edm.String
PX.SM.AUScreenActionBaseState.DisplayNameCustomized : Edm.Boolean
PX.SM.AUScreenActionBaseState.ActionFolderTypeCustomized : Edm.Boolean
PX.SM.AUScreenActionBaseState.MenuFolderTypeCustomized : Edm.Boolean
PX.SM.AUScreenActionBaseState.MenuFolderCustomized : Edm.Boolean
PX.SM.AUScreenActionBaseState.IsTopLevelCustomized : Edm.Boolean
PX.SM.AUScreenActionBaseState.BeforeCustomized : Edm.Boolean
PX.SM.AUScreenActionBaseState.AfterCustomized : Edm.Boolean
PX.SM.AUScreenActionBaseState.PlacementInCategoryCustomized : Edm.Boolean
PX.SM.AUScreenActionBaseState.AfterInMenuCustomized : Edm.Boolean
PX.SM.AUScreenActionBaseState.DisableConditionCustomized : Edm.Boolean
PX.SM.AUScreenActionBaseState.HideConditionCustomized : Edm.Boolean
PX.SM.AUScreenActionBaseState.FormCustomized : Edm.Boolean
PX.SM.AUScreenActionBaseState.MassProcessingScreenCustomized : Edm.Boolean
PX.SM.AUScreenActionBaseState.DisablePersistCustomized : Edm.Boolean
PX.SM.AUScreenActionBaseState.BatchModeCustomized : Edm.Boolean
PX.SM.AUScreenActionBaseState.MapEnableRightsCustomized : Edm.Boolean
PX.SM.AUScreenActionBaseState.MapViewRightsCustomized : Edm.Boolean
PX.SM.AUScreenActionBaseState.ExposedToMobileCustomized : Edm.Boolean
PX.SM.AUScreenActionBaseState.CategoryCustomized : Edm.Boolean
PX.SM.AUScreenActionBaseState.IsLockedOnToolbarCustomized : Edm.Boolean
PX.SM.AUScreenActionBaseState.IgnoresArchiveDisablingCustomized : Edm.Boolean
PX.SM.AUScreenActionBaseState.ConnotationCustomized : Edm.Boolean
PX.SM.AUScreenActionBaseState.AUWorkflowActionUpdateFieldCollection -> Collection(PX.SM.AUWorkflowActionUpdateField)
PX.SM.AUScreenActionBaseState.AUWorkflowActionParamCollection -> Collection(PX.SM.AUWorkflowActionParam)
PX.SM.AUScreenActionBaseState.AUWorkflowActionSequenceCollection -> Collection(PX.SM.AUWorkflowActionSequence)
PX.SM.AUScreenActionBaseState.AUWorkflowStateActionFieldCollection -> Collection(PX.SM.AUWorkflowStateActionField)
PX.SM.AUScreenActionBaseState.AUWorkflowStateActionParamCollection -> Collection(PX.SM.AUWorkflowStateActionParam)

# PX.SM.AUScreenActionProp (EntityType)

BaseType: PX.SM.AUScreenItemProp
Key: ItemID, ProjectID, PropertyID, PropertyType, ScreenID (inherited from PX.SM.AUScreenItemProp)
Entity sets: PX_SM_AUScreenActionProp

# PX.SM.AUScreenActionState (EntityType)

BaseType: PX.SM.AUScreenActionBaseState
Key: ActionName, ScreenID (inherited from PX.SM.AUScreenActionBaseState)
Entity sets: PX_SM_AUScreenActionState

PX.SM.AUScreenActionState.Method : Edm.String "Method"

# PX.SM.AUScreenCondition (EntityType)

BaseType: PX.SM.AUScreenItem
Key: ItemCD, ItemType, ParentID, ProjectID, ScreenID (inherited from PX.SM.AUScreenItem)
Entity sets: PX_SM_AUScreenCondition

# PX.SM.AUScreenConditionFilter (EntityType)

Key: ConditionID, ProjectID, RowNbr, ScreenID
Entity sets: PX_SM_AUScreenConditionFilter

PX.SM.AUScreenConditionFilter.ScreenID : Edm.String [key]
PX.SM.AUScreenConditionFilter.ProjectID : Edm.Guid [key]
PX.SM.AUScreenConditionFilter.ConditionID : Edm.String [key]
PX.SM.AUScreenConditionFilter.RowNbr : Edm.Int32 [key]
PX.SM.AUScreenConditionFilter.EventStateType : Edm.String
PX.SM.AUScreenConditionFilter.IsActive : Edm.Boolean [required] "Active"
PX.SM.AUScreenConditionFilter.OpenBrackets : Edm.Int32 [required] "Brackets"
PX.SM.AUScreenConditionFilter.FieldName : Edm.String "Field Name"
PX.SM.AUScreenConditionFilter.Condition : Edm.Int32 [required] "Condition"
PX.SM.AUScreenConditionFilter.Value : Edm.String "Value"
PX.SM.AUScreenConditionFilter.Value2 : Edm.String "Value 2"
PX.SM.AUScreenConditionFilter.CloseBrackets : Edm.Int32 [required] "Brackets"
PX.SM.AUScreenConditionFilter.Operator : Edm.Int32 [required] "Operator"
PX.SM.AUScreenConditionFilter.CreatedByID : Edm.Guid "Created By"
PX.SM.AUScreenConditionFilter.CreatedByScreenID : Edm.String
PX.SM.AUScreenConditionFilter.CreatedDateTime : Edm.DateTimeOffset
PX.SM.AUScreenConditionFilter.LastModifiedByID : Edm.Guid "Last Modified By"
PX.SM.AUScreenConditionFilter.LastModifiedByScreenID : Edm.String
PX.SM.AUScreenConditionFilter.LastModifiedDateTime : Edm.DateTimeOffset
PX.SM.AUScreenConditionFilter.TStamp : Edm.Binary
PX.SM.AUScreenConditionFilter.AUScreenItemByConditionID -> PX.SM.AUScreenItem (ScreenID=ScreenID, ProjectID=ProjectID, ConditionID=ItemCD)
PX.SM.AUScreenConditionFilter.UsersByCreatedByID -> PX.SM.Users (CreatedByID=PKID)
PX.SM.AUScreenConditionFilter.UsersByLastModifiedByID -> PX.SM.Users (LastModifiedByID=PKID)

# PX.SM.AUScreenConditionLineState (EntityType)

Key: ConditionID, LineNbr, ScreenID
Entity sets: PX_SM_AUScreenConditionLineState

PX.SM.AUScreenConditionLineState.ScreenID : Edm.String [key]
PX.SM.AUScreenConditionLineState.ConditionID : Edm.Guid [key]
PX.SM.AUScreenConditionLineState.LineNbr : Edm.Int32 [key]
PX.SM.AUScreenConditionLineState.IsActive : Edm.Boolean [required] "Active"
PX.SM.AUScreenConditionLineState.OpenBrackets : Edm.Int32 [required] "Brackets"
PX.SM.AUScreenConditionLineState.FieldName : Edm.String "Field Name"
PX.SM.AUScreenConditionLineState.Condition : Edm.Int32 [required] "Condition"
PX.SM.AUScreenConditionLineState.IsFromScheme : Edm.Boolean [required] "From Schema"
PX.SM.AUScreenConditionLineState.Value : Edm.String "Value"
PX.SM.AUScreenConditionLineState.Value2 : Edm.String "Value 2"
PX.SM.AUScreenConditionLineState.CloseBrackets : Edm.Int32 [required] "Brackets"
PX.SM.AUScreenConditionLineState.Operator : Edm.Int32 [required] "Operator"
PX.SM.AUScreenConditionLineState.AUScreenConditionStateByConditionID -> PX.SM.AUScreenConditionState (ScreenID=ScreenID, ConditionID=ConditionID)

# PX.SM.AUScreenConditionState (EntityType)

Key: ConditionID, ScreenID
Entity sets: PX_SM_AUScreenConditionState
Non-filterable, non-selectable: Order, IsSystem, Expression, CalcStatus

PX.SM.AUScreenConditionState.ScreenID : Edm.String [key]
PX.SM.AUScreenConditionState.ConditionID : Edm.Guid [key]
PX.SM.AUScreenConditionState.ConditionName : Edm.String "Condition Name"
PX.SM.AUScreenConditionState.ParentCondition : Edm.String "System Condition"
PX.SM.AUScreenConditionState.Order : Edm.Int32
PX.SM.AUScreenConditionState.IsSystem : Edm.Boolean "IsSystem"
PX.SM.AUScreenConditionState.Expression : Edm.String "Expression"
PX.SM.AUScreenConditionState.AppendSystemCondition : Edm.Boolean "Append System Condition"
PX.SM.AUScreenConditionState.JoinMethod : Edm.String "Operator"
PX.SM.AUScreenConditionState.InvertCondition : Edm.Boolean "Inverted"
PX.SM.AUScreenConditionState.CalcStatus : Edm.String "Status"
PX.SM.AUScreenConditionState.AUScreenConditionLineStateCollection -> Collection(PX.SM.AUScreenConditionLineState)

# PX.SM.AUScreenDefinition (EntityType)

Key: ProjectID, ScreenID
Entity sets: PX_SM_AUScreenDefinition

PX.SM.AUScreenDefinition.ScreenID : Edm.String [key] "Screen ID"
PX.SM.AUScreenDefinition.ProjectID : Edm.Guid [key] "Project"
PX.SM.AUScreenDefinition.GraphName : Edm.String
PX.SM.AUScreenDefinition.ViewName : Edm.String
PX.SM.AUScreenDefinition.TableName : Edm.String
PX.SM.AUScreenDefinition.BqlTableName : Edm.String
PX.SM.AUScreenDefinition.TimeStampName : Edm.String
PX.SM.AUScreenDefinition.IsWorkflowEnabled : Edm.Boolean [required] "Workflow Enabled"
PX.SM.AUScreenDefinition.IsFlowIdentifierRequired : Edm.Boolean [required] "Flow Identifier Required"
PX.SM.AUScreenDefinition.FlowIdentifier : Edm.String "Flow Identifier"
PX.SM.AUScreenDefinition.StateIdentifier : Edm.String "State Identifier"
PX.SM.AUScreenDefinition.CreatedByID : Edm.Guid "Created By"
PX.SM.AUScreenDefinition.CreatedByScreenID : Edm.String
PX.SM.AUScreenDefinition.CreatedDateTime : Edm.DateTimeOffset "Created On"
PX.SM.AUScreenDefinition.LastModifiedByID : Edm.Guid "Last Modified By"
PX.SM.AUScreenDefinition.LastModifiedByScreenID : Edm.String
PX.SM.AUScreenDefinition.LastModifiedDateTime : Edm.DateTimeOffset "Last Modified On"
PX.SM.AUScreenDefinition.TStamp : Edm.Binary
PX.SM.AUScreenDefinition.UsersByCreatedByID -> PX.SM.Users (CreatedByID=PKID)
PX.SM.AUScreenDefinition.UsersByLastModifiedByID -> PX.SM.Users (LastModifiedByID=PKID)
PX.SM.AUScreenDefinition.AUScreenItemCollection -> Collection(PX.SM.AUScreenItem)

# PX.SM.AUScreenEvent (EntityType)

BaseType: PX.SM.AUScreenItem
Key: ItemCD, ItemType, ParentID, ProjectID, ScreenID (inherited from PX.SM.AUScreenItem)
Entity sets: PX_SM_AUScreenEvent
Filterable: false (fields declared in this DAC cannot be used in $filter or $select; inherited ones can)

PX.SM.AUScreenEvent.Entity : Edm.String "Entity"

# PX.SM.AUScreenEventDef (EntityType)

BaseType: PX.SM.AUScreenItem
Key: ItemCD, ItemType, ParentID, ProjectID, ScreenID (inherited from PX.SM.AUScreenItem)
Entity sets: PX_SM_AUScreenEventDef

# PX.SM.AUScreenEventEndCondition (EntityType)

BaseType: PX.SM.AUScreenConditionFilter
Key: ConditionID, ProjectID, RowNbr, ScreenID (inherited from PX.SM.AUScreenConditionFilter)
Entity sets: PX_SM_AUScreenEventEndCondition

# PX.SM.AUScreenEventProp (EntityType)

BaseType: PX.SM.AUScreenItemProp
Key: ItemID, ProjectID, PropertyID, PropertyType, ScreenID (inherited from PX.SM.AUScreenItemProp)
Entity sets: PX_SM_AUScreenEventProp

# PX.SM.AUScreenEventStartCondition (EntityType)

BaseType: PX.SM.AUScreenConditionFilter
Key: ConditionID, ProjectID, RowNbr, ScreenID (inherited from PX.SM.AUScreenConditionFilter)
Entity sets: PX_SM_AUScreenEventStartCondition

# PX.SM.AUScreenEventSubscriber (EntityType)

BaseType: PX.SM.AUScreenItem
Key: ItemCD, ItemType, ParentID, ProjectID, ScreenID (inherited from PX.SM.AUScreenItem)
Entity sets: PX_SM_AUScreenEventSubscriber
Filterable: false (fields declared in this DAC cannot be used in $filter or $select; inherited ones can)

PX.SM.AUScreenEventSubscriber.SubscriberType : Edm.String "Type"
PX.SM.AUScreenEventSubscriber.NotificationTemplate : Edm.Int32 "Notification Template"
PX.SM.AUScreenEventSubscriber.ActivityTemplate : Edm.String "Activity Template"
PX.SM.AUScreenEventSubscriber.Action : Edm.String "Action"
PX.SM.AUScreenEventSubscriber.Active : Edm.Boolean "Active"
PX.SM.AUScreenEventSubscriber.Entity : Edm.String "Entity"

# PX.SM.AUScreenEventSubscriberDef (EntityType)

BaseType: PX.SM.AUScreenItem
Key: ItemCD, ItemType, ParentID, ProjectID, ScreenID (inherited from PX.SM.AUScreenItem)
Entity sets: PX_SM_AUScreenEventSubscriberDef

# PX.SM.AUScreenEventSubscriberExecCondition (EntityType)

BaseType: PX.SM.AUScreenConditionFilter
Key: ConditionID, ProjectID, RowNbr, ScreenID (inherited from PX.SM.AUScreenConditionFilter)
Entity sets: PX_SM_AUScreenEventSubscriberExecCondition

# PX.SM.AUScreenEventSubscriberProp (EntityType)

BaseType: PX.SM.AUScreenItemProp
Key: ItemID, ProjectID, PropertyID, PropertyType, ScreenID (inherited from PX.SM.AUScreenItemProp)
Entity sets: PX_SM_AUScreenEventSubscriberProp

# PX.SM.AUScreenExtraAction (EntityType)

Key: ActionName, ScreenID
Entity sets: PX_SM_AUScreenExtraAction

PX.SM.AUScreenExtraAction.ScreenID : Edm.String [key]
PX.SM.AUScreenExtraAction.ActionName : Edm.String [key] "Action Name"
PX.SM.AUScreenExtraAction.DisplayName : Edm.String "Display Name"
PX.SM.AUScreenExtraAction.DisplayOnMainToolbar : Edm.Boolean
PX.SM.AUScreenExtraAction.MapEnableRights : Edm.Byte
PX.SM.AUScreenExtraAction.MapViewRights : Edm.Byte
PX.SM.AUScreenExtraAction.Category : Edm.String
PX.SM.AUScreenExtraAction.ExposedToMobile : Edm.Boolean
PX.SM.AUScreenExtraAction.IsLockedOnToolbar : Edm.Boolean
PX.SM.AUScreenExtraAction.DisablePersist : Edm.Boolean
PX.SM.AUScreenExtraAction.Connotation : Edm.String
PX.SM.AUScreenExtraAction.IsActive : Edm.Boolean "Active"
PX.SM.AUScreenExtraAction.ActionDiscriminator : Edm.String "Extra Action Type"
PX.SM.AUScreenExtraAction.BeforeRunForm : Edm.String "Dialog Box Before Action Execution"
PX.SM.AUScreenExtraAction.AfterRunForm : Edm.String "Dialog Box After Action Execution"
PX.SM.AUScreenExtraAction.Settings : Edm.String "Action Parameters"

# PX.SM.AUScreenFieldForm (EntityType)

BaseType: PX.SM.AUScreenItem
Key: ItemCD, ItemType, ParentID, ProjectID, ScreenID (inherited from PX.SM.AUScreenItem)
Entity sets: PX_SM_AUScreenFieldForm

# PX.SM.AUScreenFieldFormProp (EntityType)

BaseType: PX.SM.AUScreenItemProp
Key: ItemID, ProjectID, PropertyID, PropertyType, ScreenID (inherited from PX.SM.AUScreenItemProp)
Entity sets: PX_SM_AUScreenFieldFormProp

# PX.SM.AUScreenFieldState (EntityType)

Key: FieldName, ScreenID, TableName
Entity sets: PX_SM_AUScreenFieldState

PX.SM.AUScreenFieldState.IsActive : Edm.Boolean "Active"
PX.SM.AUScreenFieldState.IsSystem : Edm.Boolean "System"
PX.SM.AUScreenFieldState.ScreenID : Edm.String [key]
PX.SM.AUScreenFieldState.TableName : Edm.String [key]
PX.SM.AUScreenFieldState.FieldName : Edm.String [key]
PX.SM.AUScreenFieldState.DisplayName : Edm.String "Display Name"
PX.SM.AUScreenFieldState.IsEnabled : Edm.Boolean
PX.SM.AUScreenFieldState.EnableCondition : Edm.String
PX.SM.AUScreenFieldState.IsVisible : Edm.Boolean
PX.SM.AUScreenFieldState.VisibleCondition : Edm.String
PX.SM.AUScreenFieldState.DisableCondition : Edm.String "Disable Condition"
PX.SM.AUScreenFieldState.HideCondition : Edm.String "Hide Condition"
PX.SM.AUScreenFieldState.IsRequired : Edm.Boolean "Required"
PX.SM.AUScreenFieldState.RequiredCondition : Edm.String "Required Condition"
PX.SM.AUScreenFieldState.ComboBoxValues : Edm.String "Combo Box Values"
PX.SM.AUScreenFieldState.IsFromSchema : Edm.Boolean "From Schema"
PX.SM.AUScreenFieldState.DefaultValue : Edm.String "Default Value"
PX.SM.AUScreenFieldState.DisplayNameCustomized : Edm.Boolean
PX.SM.AUScreenFieldState.DisableConditionCustomized : Edm.Boolean
PX.SM.AUScreenFieldState.HideConditionCustomized : Edm.Boolean
PX.SM.AUScreenFieldState.IsRequiredCustomized : Edm.Boolean
PX.SM.AUScreenFieldState.RequiredConditionCustomized : Edm.Boolean
PX.SM.AUScreenFieldState.ComboBoxValuesCustomized : Edm.Boolean
PX.SM.AUScreenFieldState.IsFromSchemaCustomized : Edm.Boolean
PX.SM.AUScreenFieldState.DefaultValueCustomized : Edm.Boolean

# PX.SM.AUScreenForm (EntityType)

BaseType: PX.SM.AUScreenItem
Key: ItemCD, ItemType, ParentID, ProjectID, ScreenID (inherited from PX.SM.AUScreenItem)
Entity sets: PX_SM_AUScreenForm
Filterable: false (fields declared in this DAC cannot be used in $filter or $select; inherited ones can)

PX.SM.AUScreenForm.Caption : Edm.String "Caption"
PX.SM.AUScreenForm.Customized : Edm.Boolean "Customized"
PX.SM.AUScreenForm.IsVisible : Edm.Boolean "Visible"

# PX.SM.AUScreenFormProp (EntityType)

BaseType: PX.SM.AUScreenItemProp
Key: ItemID, ProjectID, PropertyID, PropertyType, ScreenID (inherited from PX.SM.AUScreenItemProp)
Entity sets: PX_SM_AUScreenFormProp

# PX.SM.AUScreenInquiry (EntityType)

BaseType: PX.SM.AUScreenItem
Key: ItemCD, ItemType, ParentID, ProjectID, ScreenID (inherited from PX.SM.AUScreenItem)
Entity sets: PX_SM_AUScreenInquiry

# PX.SM.AUScreenInquiryNavProp (EntityType)

BaseType: PX.SM.AUScreenItemProp
Key: ItemID, ProjectID, PropertyID, PropertyType, ScreenID (inherited from PX.SM.AUScreenItemProp)
Entity sets: PX_SM_AUScreenInquiryNavProp

# PX.SM.AUScreenInquiryProp (EntityType)

BaseType: PX.SM.AUScreenItemProp
Key: ItemID, ProjectID, PropertyID, PropertyType, ScreenID (inherited from PX.SM.AUScreenItemProp)
Entity sets: PX_SM_AUScreenInquiryProp

# PX.SM.AUScreenItem (EntityType)

Key: ItemCD, ItemType, ParentID, ProjectID, ScreenID
Entity sets: PX_SM_AUScreenItem
Non-filterable, non-selectable: Inherit, SortOrder

PX.SM.AUScreenItem.ScreenID : Edm.String [key]
PX.SM.AUScreenItem.ProjectID : Edm.Guid [key]
PX.SM.AUScreenItem.ItemType : Edm.String [key]
PX.SM.AUScreenItem.ItemCD : Edm.String [key]
PX.SM.AUScreenItem.ParentID : Edm.String [key required]
PX.SM.AUScreenItem.ItemID : Edm.String
PX.SM.AUScreenItem.ChildRowCntr : Edm.Int32 [required]
PX.SM.AUScreenItem.IsOverride : Edm.Boolean "Override"
PX.SM.AUScreenItem.Inherit : Edm.Boolean
PX.SM.AUScreenItem.SortOrder : Edm.Int32
PX.SM.AUScreenItem.Description : Edm.String
PX.SM.AUScreenItem.IsActive : Edm.Boolean
PX.SM.AUScreenItem.CreatedByID : Edm.Guid "Created By"
PX.SM.AUScreenItem.CreatedByScreenID : Edm.String
PX.SM.AUScreenItem.CreatedDateTime : Edm.DateTimeOffset
PX.SM.AUScreenItem.LastModifiedByID : Edm.Guid "Last Modified By"
PX.SM.AUScreenItem.LastModifiedByScreenID : Edm.String
PX.SM.AUScreenItem.LastModifiedDateTime : Edm.DateTimeOffset
PX.SM.AUScreenItem.TStamp : Edm.Binary
PX.SM.AUScreenItem.AUScreenItemByParentID -> PX.SM.AUScreenItem (ParentID=ItemID)
PX.SM.AUScreenItem.UsersByCreatedByID -> PX.SM.Users (CreatedByID=PKID)
PX.SM.AUScreenItem.UsersByLastModifiedByID -> PX.SM.Users (LastModifiedByID=PKID)
PX.SM.AUScreenItem.AUScreenDefinitionByProjectID -> PX.SM.AUScreenDefinition (ScreenID=ScreenID, ProjectID=ProjectID)
PX.SM.AUScreenItem.AUScreenItemPropCollection -> Collection(PX.SM.AUScreenItemProp)
PX.SM.AUScreenItem.AUScreenConditionFilterCollection -> Collection(PX.SM.AUScreenConditionFilter)
PX.SM.AUScreenItem.AUScreenItemCollection -> Collection(PX.SM.AUScreenItem)

# PX.SM.AUScreenItemProp (EntityType)

Key: ItemID, ProjectID, PropertyID, PropertyType, ScreenID
Entity sets: PX_SM_AUScreenItemProp
Non-filterable, non-selectable: PropertyName, OriginalValue, OverrideValue, Inherit, SortOrder

PX.SM.AUScreenItemProp.ScreenID : Edm.String [key]
PX.SM.AUScreenItemProp.ProjectID : Edm.Guid [key]
PX.SM.AUScreenItemProp.ItemID : Edm.String [key]
PX.SM.AUScreenItemProp.PropertyType : Edm.String [key required]
PX.SM.AUScreenItemProp.PropertyID : Edm.String [key]
PX.SM.AUScreenItemProp.PropertyName : Edm.String "Property"
PX.SM.AUScreenItemProp.OriginalValue : Edm.String "Original"
PX.SM.AUScreenItemProp.OverrideValue : Edm.String "Override"
PX.SM.AUScreenItemProp.PropertyValue : Edm.String
PX.SM.AUScreenItemProp.IsOverride : Edm.Boolean "Override"
PX.SM.AUScreenItemProp.Inherit : Edm.Boolean
PX.SM.AUScreenItemProp.SortOrder : Edm.Int32
PX.SM.AUScreenItemProp.CreatedByID : Edm.Guid "Created By"
PX.SM.AUScreenItemProp.CreatedByScreenID : Edm.String
PX.SM.AUScreenItemProp.CreatedDateTime : Edm.DateTimeOffset
PX.SM.AUScreenItemProp.LastModifiedByID : Edm.Guid "Last Modified By"
PX.SM.AUScreenItemProp.LastModifiedByScreenID : Edm.String
PX.SM.AUScreenItemProp.LastModifiedDateTime : Edm.DateTimeOffset
PX.SM.AUScreenItemProp.TStamp : Edm.Binary
PX.SM.AUScreenItemProp.AUScreenItemByItemID -> PX.SM.AUScreenItem (ScreenID=ScreenID, ProjectID=ProjectID, ItemID=ItemID)
PX.SM.AUScreenItemProp.UsersByCreatedByID -> PX.SM.Users (CreatedByID=PKID)
PX.SM.AUScreenItemProp.UsersByLastModifiedByID -> PX.SM.Users (LastModifiedByID=PKID)

# PX.SM.AUScreenNavigationActionState (EntityType)

BaseType: PX.SM.AUScreenActionBaseState
Key: ActionName, ScreenID (inherited from PX.SM.AUScreenActionBaseState)
Entity sets: PX_SM_AUScreenNavigationActionState

PX.SM.AUScreenNavigationActionState.DestinationScreenID : Edm.String
PX.SM.AUScreenNavigationActionState.WindowMode : Edm.String
PX.SM.AUScreenNavigationActionState.Icon : Edm.String
PX.SM.AUScreenNavigationActionState.DestinationScreenIDCustomized : Edm.Boolean
PX.SM.AUScreenNavigationActionState.WindowModeCustomized : Edm.Boolean
PX.SM.AUScreenNavigationActionState.IconCustomized : Edm.Boolean

# PX.SM.AUScreenNavigationParameterState (EntityType)

Key: ActionName, FieldName, ScreenID
Entity sets: PX_SM_AUScreenNavigationParameterState

PX.SM.AUScreenNavigationParameterState.IsActive : Edm.Boolean "Active"
PX.SM.AUScreenNavigationParameterState.IsSystem : Edm.Boolean "System"
PX.SM.AUScreenNavigationParameterState.ScreenID : Edm.String [key]
PX.SM.AUScreenNavigationParameterState.ActionName : Edm.String [key]
PX.SM.AUScreenNavigationParameterState.FieldName : Edm.String [key]
PX.SM.AUScreenNavigationParameterState.Value : Edm.String
PX.SM.AUScreenNavigationParameterState.IsFromSchema : Edm.Boolean [required]
PX.SM.AUScreenNavigationParameterState.ValueCustomized : Edm.Boolean
PX.SM.AUScreenNavigationParameterState.IsFromSchemaCustomized : Edm.Boolean

# PX.SM.AUScreenPopup (EntityType)

BaseType: PX.SM.AUScreenItem
Key: ItemCD, ItemType, ParentID, ProjectID, ScreenID (inherited from PX.SM.AUScreenItem)
Entity sets: PX_SM_AUScreenPopup

# PX.SM.AUScreenPopupField (EntityType)

BaseType: PX.SM.AUScreenItem
Key: ItemCD, ItemType, ParentID, ProjectID, ScreenID (inherited from PX.SM.AUScreenItem)
Entity sets: PX_SM_AUScreenPopupField

# PX.SM.AUScreenPopupFieldProp (EntityType)

BaseType: PX.SM.AUScreenItemProp
Key: ItemID, ProjectID, PropertyID, PropertyType, ScreenID (inherited from PX.SM.AUScreenItemProp)
Entity sets: PX_SM_AUScreenPopupFieldProp

# PX.SM.AUScreenPopupProp (EntityType)

BaseType: PX.SM.AUScreenItemProp
Key: ItemID, ProjectID, PropertyID, PropertyType, ScreenID (inherited from PX.SM.AUScreenItemProp)
Entity sets: PX_SM_AUScreenPopupProp

# PX.SM.AUScreenReport (EntityType)

BaseType: PX.SM.AUScreenItem
Key: ItemCD, ItemType, ParentID, ProjectID, ScreenID (inherited from PX.SM.AUScreenItem)
Entity sets: PX_SM_AUScreenReport

# PX.SM.AUScreenReportProp (EntityType)

BaseType: PX.SM.AUScreenItemProp
Key: ItemID, ProjectID, PropertyID, PropertyType, ScreenID (inherited from PX.SM.AUScreenItemProp)
Entity sets: PX_SM_AUScreenReportProp

# PX.SM.AUStep (EntityType)

Key: ScreenID, StepID
Entity sets: PX_SM_AUStep
Non-filterable, non-selectable: ActionName, MenuText, FieldTableName, FieldOrigTableName, FieldName, NoteText

PX.SM.AUStep.ScreenID : Edm.String [key] "Screen ID"
PX.SM.AUStep.StepID : Edm.String [key] "Step ID"
PX.SM.AUStep.Description : Edm.String "Description"
PX.SM.AUStep.GraphName : Edm.String
PX.SM.AUStep.ViewName : Edm.String
PX.SM.AUStep.TableName : Edm.String
PX.SM.AUStep.BqlTableName : Edm.String
PX.SM.AUStep.TimeStampName : Edm.String
PX.SM.AUStep.IsActive : Edm.Boolean [required] "Active"
PX.SM.AUStep.IsStart : Edm.Boolean [required] "Start Point"
PX.SM.AUStep.FilterCntr : Edm.Int16 [required]
PX.SM.AUStep.FieldCntr : Edm.Int16 [required]
PX.SM.AUStep.ActionCntr : Edm.Int16 [required]
PX.SM.AUStep.ActionName : Edm.String
PX.SM.AUStep.MenuText : Edm.String
PX.SM.AUStep.FieldTableName : Edm.String
PX.SM.AUStep.FieldOrigTableName : Edm.String
PX.SM.AUStep.FieldName : Edm.String
PX.SM.AUStep.NoteID : Edm.Guid
PX.SM.AUStep.NoteText : Edm.String "Note Text"
PX.SM.AUStep.CreatedByID : Edm.Guid "Created By"
PX.SM.AUStep.CreatedByScreenID : Edm.String
PX.SM.AUStep.CreatedDateTime : Edm.DateTimeOffset
PX.SM.AUStep.LastModifiedByID : Edm.Guid "Last Modified By"
PX.SM.AUStep.LastModifiedByScreenID : Edm.String
PX.SM.AUStep.LastModifiedDateTime : Edm.DateTimeOffset
PX.SM.AUStep.TStamp : Edm.Binary
PX.SM.AUStep.UsersByCreatedByID -> PX.SM.Users (CreatedByID=PKID)
PX.SM.AUStep.UsersByLastModifiedByID -> PX.SM.Users (LastModifiedByID=PKID)
PX.SM.AUStep.AUStepActionCollection -> Collection(PX.SM.AUStepAction)
PX.SM.AUStep.AUStepComboCollection -> Collection(PX.SM.AUStepCombo)
PX.SM.AUStep.AUStepFieldCollection -> Collection(PX.SM.AUStepField)
PX.SM.AUStep.AUStepFillCollection -> Collection(PX.SM.AUStepFill)
PX.SM.AUStep.AUStepFilterCollection -> Collection(PX.SM.AUStepFilter)

# PX.SM.AUStepAction (EntityType)

Key: RowNbr, ScreenID, StepID
Entity sets: PX_SM_AUStepAction
Non-filterable, non-selectable: MenuIcon, RetryCntr, NoteText

PX.SM.AUStepAction.ScreenID : Edm.String [key]
PX.SM.AUStepAction.StepID : Edm.String [key]
PX.SM.AUStepAction.RowNbr : Edm.Int16 [key]
PX.SM.AUStepAction.IsActive : Edm.Boolean [required] "Active"
PX.SM.AUStepAction.ActionName : Edm.String "Action Name"
PX.SM.AUStepAction.IsAutomatic : Edm.Boolean [required] "Run Auto"
PX.SM.AUStepAction.IsDefault : Edm.Boolean [required] "Is Default"
PX.SM.AUStepAction.IsDisabled : Edm.Boolean [required] "Disable"
PX.SM.AUStepAction.BatchMode : Edm.Boolean [required] "Batch Mode"
PX.SM.AUStepAction.MenuText : Edm.String "Menu Text"
PX.SM.AUStepAction.AutoSave : Edm.Int16 [required] "Save Auto"
PX.SM.AUStepAction.MenuIcon : Edm.String "Menu Icon"
PX.SM.AUStepAction.ProcessingScreenID : Edm.String "Screen ID"
PX.SM.AUStepAction.ProcessingGraphName : Edm.String
PX.SM.AUStepAction.SplitByValues : Edm.Boolean [required] "Split by Values"
PX.SM.AUStepAction.IsRetryActive : Edm.Boolean [required] "Active"
PX.SM.AUStepAction.RetryScreenID : Edm.String "Screen ID"
PX.SM.AUStepAction.RetryStepID : Edm.String "Step ID"
PX.SM.AUStepAction.RetryActionName : Edm.String "Action Name"
PX.SM.AUStepAction.RetryCntr : Edm.Int16 [required] "Count"
PX.SM.AUStepAction.IsSuccessActive : Edm.Boolean [required] "Active"
PX.SM.AUStepAction.SuccessScreenID : Edm.String "Screen ID"
PX.SM.AUStepAction.SuccessStepID : Edm.String "Step ID"
PX.SM.AUStepAction.SuccessActionName : Edm.String "Action Name"
PX.SM.AUStepAction.IsFailActive : Edm.Boolean [required] "Active"
PX.SM.AUStepAction.FailScreenID : Edm.String "Screen ID"
PX.SM.AUStepAction.FailStepID : Edm.String "Step ID"
PX.SM.AUStepAction.FailActionName : Edm.String "Action Name"
PX.SM.AUStepAction.NoteID : Edm.Guid
PX.SM.AUStepAction.NoteText : Edm.String "Note Text"
PX.SM.AUStepAction.CreatedByID : Edm.Guid "Created By"
PX.SM.AUStepAction.CreatedByScreenID : Edm.String
PX.SM.AUStepAction.CreatedDateTime : Edm.DateTimeOffset
PX.SM.AUStepAction.LastModifiedByID : Edm.Guid "Last Modified By"
PX.SM.AUStepAction.LastModifiedByScreenID : Edm.String
PX.SM.AUStepAction.LastModifiedDateTime : Edm.DateTimeOffset
PX.SM.AUStepAction.TStamp : Edm.Binary
PX.SM.AUStepAction.UsersByCreatedByID -> PX.SM.Users (CreatedByID=PKID)
PX.SM.AUStepAction.UsersByLastModifiedByID -> PX.SM.Users (LastModifiedByID=PKID)
PX.SM.AUStepAction.AUStepByStepID -> PX.SM.AUStep (ScreenID=ScreenID, StepID=StepID)
PX.SM.AUStepAction.AUStepByRetryScreenID -> PX.SM.AUStep (RetryStepID=StepID, RetryScreenID=ScreenID)
PX.SM.AUStepAction.AUStepBySuccessScreenID -> PX.SM.AUStep (SuccessStepID=StepID, SuccessScreenID=ScreenID)
PX.SM.AUStepAction.AUStepByFailScreenID -> PX.SM.AUStep (FailStepID=StepID, FailScreenID=ScreenID)

# PX.SM.AUStepCombo (EntityType)

Key: FieldName, RowNbr, ScreenID, StepID, TableName
Entity sets: PX_SM_AUStepCombo
Non-filterable, non-selectable: IsExplicit, Description

PX.SM.AUStepCombo.ScreenID : Edm.String [key]
PX.SM.AUStepCombo.StepID : Edm.String [key]
PX.SM.AUStepCombo.TableName : Edm.String [key]
PX.SM.AUStepCombo.FieldName : Edm.String [key]
PX.SM.AUStepCombo.RowNbr : Edm.Int16 [key]
PX.SM.AUStepCombo.IsActive : Edm.Boolean [required] "Active"
PX.SM.AUStepCombo.IsExplicit : Edm.Boolean "Explicit"
PX.SM.AUStepCombo.Value : Edm.String "Value"
PX.SM.AUStepCombo.Description : Edm.String "Description"
PX.SM.AUStepCombo.CreatedByID : Edm.Guid "Created By"
PX.SM.AUStepCombo.CreatedByScreenID : Edm.String
PX.SM.AUStepCombo.CreatedDateTime : Edm.DateTimeOffset
PX.SM.AUStepCombo.LastModifiedByID : Edm.Guid "Last Modified By"
PX.SM.AUStepCombo.LastModifiedByScreenID : Edm.String
PX.SM.AUStepCombo.LastModifiedDateTime : Edm.DateTimeOffset
PX.SM.AUStepCombo.TStamp : Edm.Binary
PX.SM.AUStepCombo.UsersByCreatedByID -> PX.SM.Users (CreatedByID=PKID)
PX.SM.AUStepCombo.UsersByLastModifiedByID -> PX.SM.Users (LastModifiedByID=PKID)
PX.SM.AUStepCombo.AUStepByStepID -> PX.SM.AUStep (ScreenID=ScreenID, StepID=StepID)

# PX.SM.AUStepField (EntityType)

Key: RowNbr, ScreenID, StepID
Entity sets: PX_SM_AUStepField
Non-filterable, non-selectable: NoteText

PX.SM.AUStepField.ScreenID : Edm.String [key]
PX.SM.AUStepField.StepID : Edm.String [key]
PX.SM.AUStepField.RowNbr : Edm.Int16 [key]
PX.SM.AUStepField.IsActive : Edm.Boolean [required] "Active"
PX.SM.AUStepField.TableName : Edm.String "Table Name"
PX.SM.AUStepField.FieldName : Edm.String "Field Name"
PX.SM.AUStepField.UseSavedState : Edm.Boolean [required] "Use Saved State"
PX.SM.AUStepField.IsDisabled : Edm.Boolean [required] "Disable"
PX.SM.AUStepField.IsInvisible : Edm.Boolean [required] "Hidden"
PX.SM.AUStepField.IsRelative : Edm.Boolean [required] "Is Relative"
PX.SM.AUStepField.MinValue : Edm.String "Min Value"
PX.SM.AUStepField.MaxValue : Edm.String "Max Value"
PX.SM.AUStepField.DefaultValue : Edm.String "Default Value"
PX.SM.AUStepField.InputMask : Edm.String "Input Mask"
PX.SM.AUStepField.NoteID : Edm.Guid
PX.SM.AUStepField.NoteText : Edm.String "Note Text"
PX.SM.AUStepField.CreatedByID : Edm.Guid "Created By"
PX.SM.AUStepField.CreatedByScreenID : Edm.String
PX.SM.AUStepField.CreatedDateTime : Edm.DateTimeOffset
PX.SM.AUStepField.LastModifiedByID : Edm.Guid "Last Modified By"
PX.SM.AUStepField.LastModifiedByScreenID : Edm.String
PX.SM.AUStepField.LastModifiedDateTime : Edm.DateTimeOffset
PX.SM.AUStepField.TStamp : Edm.Binary
PX.SM.AUStepField.UsersByCreatedByID -> PX.SM.Users (CreatedByID=PKID)
PX.SM.AUStepField.UsersByLastModifiedByID -> PX.SM.Users (LastModifiedByID=PKID)
PX.SM.AUStepField.AUStepByStepID -> PX.SM.AUStep (ScreenID=ScreenID, StepID=StepID)

# PX.SM.AUStepFill (EntityType)

Key: ActionName, MenuText, RowNbr, ScreenID, StepID
Entity sets: PX_SM_AUStepFill

PX.SM.AUStepFill.ScreenID : Edm.String [key]
PX.SM.AUStepFill.StepID : Edm.String [key]
PX.SM.AUStepFill.ActionName : Edm.String [key]
PX.SM.AUStepFill.MenuText : Edm.String [key]
PX.SM.AUStepFill.RowNbr : Edm.Int16 [key]
PX.SM.AUStepFill.IsActive : Edm.Boolean [required] "Active"
PX.SM.AUStepFill.FieldName : Edm.String "Field Name"
PX.SM.AUStepFill.IsRelative : Edm.Boolean [required] "Is Relative"
PX.SM.AUStepFill.Value : Edm.String "Value"
PX.SM.AUStepFill.IsDelayed : Edm.Boolean [required] "Is Delayed"
PX.SM.AUStepFill.IgnoreError : Edm.Boolean [required] "Ignore Error"
PX.SM.AUStepFill.CreatedByID : Edm.Guid "Created By"
PX.SM.AUStepFill.CreatedByScreenID : Edm.String
PX.SM.AUStepFill.CreatedDateTime : Edm.DateTimeOffset
PX.SM.AUStepFill.LastModifiedByID : Edm.Guid "Last Modified By"
PX.SM.AUStepFill.LastModifiedByScreenID : Edm.String
PX.SM.AUStepFill.LastModifiedDateTime : Edm.DateTimeOffset
PX.SM.AUStepFill.TStamp : Edm.Binary
PX.SM.AUStepFill.UsersByCreatedByID -> PX.SM.Users (CreatedByID=PKID)
PX.SM.AUStepFill.UsersByLastModifiedByID -> PX.SM.Users (LastModifiedByID=PKID)
PX.SM.AUStepFill.AUStepByStepID -> PX.SM.AUStep (ScreenID=ScreenID, StepID=StepID)

# PX.SM.AUStepFilter (EntityType)

Key: RowNbr, ScreenID, StepID
Entity sets: PX_SM_AUStepFilter
Non-filterable, non-selectable: NoteText

PX.SM.AUStepFilter.ScreenID : Edm.String [key]
PX.SM.AUStepFilter.StepID : Edm.String [key]
PX.SM.AUStepFilter.RowNbr : Edm.Int16 [key]
PX.SM.AUStepFilter.IsActive : Edm.Boolean [required] "Active"
PX.SM.AUStepFilter.OpenBrackets : Edm.Int32 [required] "Brackets"
PX.SM.AUStepFilter.FieldName : Edm.String "Field Name"
PX.SM.AUStepFilter.Condition : Edm.Int32 [required] "Condition"
PX.SM.AUStepFilter.IsRelative : Edm.Boolean [required] "Is Relative"
PX.SM.AUStepFilter.Value : Edm.String "Value"
PX.SM.AUStepFilter.Value2 : Edm.String "Value 2"
PX.SM.AUStepFilter.CloseBrackets : Edm.Int32 [required] "Brackets"
PX.SM.AUStepFilter.Operator : Edm.Int32 [required] "Operator"
PX.SM.AUStepFilter.NoteID : Edm.Guid
PX.SM.AUStepFilter.NoteText : Edm.String "Note Text"
PX.SM.AUStepFilter.CreatedByID : Edm.Guid "Created By"
PX.SM.AUStepFilter.CreatedByScreenID : Edm.String
PX.SM.AUStepFilter.CreatedDateTime : Edm.DateTimeOffset
PX.SM.AUStepFilter.LastModifiedByID : Edm.Guid "Last Modified By"
PX.SM.AUStepFilter.LastModifiedByScreenID : Edm.String
PX.SM.AUStepFilter.LastModifiedDateTime : Edm.DateTimeOffset
PX.SM.AUStepFilter.TStamp : Edm.Binary
PX.SM.AUStepFilter.UsersByCreatedByID -> PX.SM.Users (CreatedByID=PKID)
PX.SM.AUStepFilter.UsersByLastModifiedByID -> PX.SM.Users (LastModifiedByID=PKID)
PX.SM.AUStepFilter.AUStepByStepID -> PX.SM.AUStep (ScreenID=ScreenID, StepID=StepID)

# PX.SM.AUTableDefinition (EntityType)

Key: ProjectID, TableName
Entity sets: PX_SM_AUTableDefinition

PX.SM.AUTableDefinition.TableName : Edm.String [key] "Table Name"
PX.SM.AUTableDefinition.ProjectID : Edm.Guid [key] "Project"
PX.SM.AUTableDefinition.Description : Edm.String "Description"
PX.SM.AUTableDefinition.IsActive : Edm.Boolean [required] "Active"
PX.SM.AUTableDefinition.CreatedByID : Edm.Guid "Created By"
PX.SM.AUTableDefinition.CreatedByScreenID : Edm.String
PX.SM.AUTableDefinition.CreatedDateTime : Edm.DateTimeOffset "Created On"
PX.SM.AUTableDefinition.LastModifiedByID : Edm.Guid "Last Modified By"
PX.SM.AUTableDefinition.LastModifiedByScreenID : Edm.String
PX.SM.AUTableDefinition.LastModifiedDateTime : Edm.DateTimeOffset "Last Modified On"
PX.SM.AUTableDefinition.TStamp : Edm.Binary
PX.SM.AUTableDefinition.UsersByCreatedByID -> PX.SM.Users (CreatedByID=PKID)
PX.SM.AUTableDefinition.UsersByLastModifiedByID -> PX.SM.Users (LastModifiedByID=PKID)
PX.SM.AUTableDefinition.AUTableExtensionCollection -> Collection(PX.SM.AUTableExtension)

# PX.SM.AUTableExtension (EntityType)

Key: FieldName, ProjectID, TableName
Entity sets: PX_SM_AUTableExtension
Non-filterable, non-selectable: Inherit, SortOrder

PX.SM.AUTableExtension.TableName : Edm.String [key]
PX.SM.AUTableExtension.ProjectID : Edm.Guid [key]
PX.SM.AUTableExtension.FieldName : Edm.String [key] "Field Name"
PX.SM.AUTableExtension.StorageType : Edm.Int32 [required] "Storage Type"
PX.SM.AUTableExtension.IsOverride : Edm.Boolean "Override"
PX.SM.AUTableExtension.Inherit : Edm.Boolean
PX.SM.AUTableExtension.SortOrder : Edm.Int32
PX.SM.AUTableExtension.CreatedByID : Edm.Guid "Created By"
PX.SM.AUTableExtension.CreatedByScreenID : Edm.String
PX.SM.AUTableExtension.CreatedDateTime : Edm.DateTimeOffset
PX.SM.AUTableExtension.LastModifiedByID : Edm.Guid "Last Modified By"
PX.SM.AUTableExtension.LastModifiedByScreenID : Edm.String
PX.SM.AUTableExtension.LastModifiedDateTime : Edm.DateTimeOffset
PX.SM.AUTableExtension.TStamp : Edm.Binary
PX.SM.AUTableExtension.UsersByCreatedByID -> PX.SM.Users (CreatedByID=PKID)
PX.SM.AUTableExtension.UsersByLastModifiedByID -> PX.SM.Users (LastModifiedByID=PKID)
PX.SM.AUTableExtension.AUTableDefinitionByProjectID -> PX.SM.AUTableDefinition (TableName=TableName, ProjectID=ProjectID)

# PX.SM.AUTableExtensionState (EntityType)

Key: FieldName, StateID, TableName
Entity sets: PX_SM_AUTableExtensionState
Non-filterable, non-selectable: ComboValues, ComboXml, DefaultValue, DefaultXml, Selector, SelectorXml

PX.SM.AUTableExtensionState.StateID : Edm.Guid [key]
PX.SM.AUTableExtensionState.TableName : Edm.String [key] "Table Name"
PX.SM.AUTableExtensionState.FieldName : Edm.String [key] "Field Name"
PX.SM.AUTableExtensionState.StorageType : Edm.Int32 "Storage Type"
PX.SM.AUTableExtensionState.ControlType : Edm.Int32 "Control Type"
PX.SM.AUTableExtensionState.DataType : Edm.Int32 "Data Type"
PX.SM.AUTableExtensionState.Length : Edm.String "Length"
PX.SM.AUTableExtensionState.DisplayMask : Edm.String "Display Mask"
PX.SM.AUTableExtensionState.DisplayName : Edm.String "Display Name"
PX.SM.AUTableExtensionState.ComboValues : Edm.String "Combo Values"
PX.SM.AUTableExtensionState.ComboXml : Edm.String "Combo Xml"
PX.SM.AUTableExtensionState.ComboAttr : Edm.String "Combo Attr"
PX.SM.AUTableExtensionState.DefaultValue : Edm.String "Default Value"
PX.SM.AUTableExtensionState.DefaultXml : Edm.String "Default Xml"
PX.SM.AUTableExtensionState.DefaultAttr : Edm.String "Default Attribute"
PX.SM.AUTableExtensionState.Selector : Edm.String "Lookup"
PX.SM.AUTableExtensionState.SelectorXml : Edm.String "Selector Xml"
PX.SM.AUTableExtensionState.SelectorAttr : Edm.String "Selector Attr"
PX.SM.AUTableExtensionState.IsRequired : Edm.Boolean [required] "Required"
PX.SM.AUTableExtensionState.IsVisible : Edm.Boolean [required] "Visible"
PX.SM.AUTableExtensionState.IsEnable : Edm.Boolean [required] "Enable"
PX.SM.AUTableExtensionState.MappedToTable : Edm.String "Mapped to Table"
PX.SM.AUTableExtensionState.MappedToField : Edm.String "Mapped to Field"
PX.SM.AUTableExtensionState.CustomAttribute : Edm.String "Custom Attribute"

# PX.SM.AUTemplate (EntityType)

Key: TemplateID
Entity sets: PX_SM_AUTemplate
Non-filterable, non-selectable: Graph, NoteText

PX.SM.AUTemplate.ScreenID : Edm.String "Screen ID"
PX.SM.AUTemplate.Graph : Edm.String "Graph"
PX.SM.AUTemplate.TemplateID : Edm.Int32 [key] "Template ID"
PX.SM.AUTemplate.Description : Edm.String "Description"
PX.SM.AUTemplate.NoteID : Edm.Guid
PX.SM.AUTemplate.NoteText : Edm.String "Note Text"
PX.SM.AUTemplate.CreatedByID : Edm.Guid "Created By"
PX.SM.AUTemplate.CreatedByScreenID : Edm.String
PX.SM.AUTemplate.CreatedDateTime : Edm.DateTimeOffset
PX.SM.AUTemplate.LastModifiedByID : Edm.Guid "Last Modified By"
PX.SM.AUTemplate.LastModifiedByScreenID : Edm.String
PX.SM.AUTemplate.LastModifiedDateTime : Edm.DateTimeOffset
PX.SM.AUTemplate.TStamp : Edm.Binary
PX.SM.AUTemplate.UsersByCreatedByID -> PX.SM.Users (CreatedByID=PKID)
PX.SM.AUTemplate.UsersByLastModifiedByID -> PX.SM.Users (LastModifiedByID=PKID)
PX.SM.AUTemplate.AUTemplateDataCollection -> Collection(PX.SM.AUTemplateData)

# PX.SM.AUTemplateData (EntityType)

Key: OrderId, TemplateId
Entity sets: PX_SM_AUTemplateData
Non-filterable, non-selectable: View, RowType

PX.SM.AUTemplateData.TemplateId : Edm.Int32 [key] "TemplateId"
PX.SM.AUTemplateData.OrderId : Edm.Int32 [key]
PX.SM.AUTemplateData.Active : Edm.Boolean "Active"
PX.SM.AUTemplateData.Line : Edm.Int32 "Line"
PX.SM.AUTemplateData.Container : Edm.String "Container"
PX.SM.AUTemplateData.View : Edm.String "View"
PX.SM.AUTemplateData.RowType : Edm.String "Type"
PX.SM.AUTemplateData.Field : Edm.String "Field"
PX.SM.AUTemplateData.Value : Edm.String "Value"
PX.SM.AUTemplateData.FieldId : Edm.String "FieldId"
PX.SM.AUTemplateData.AUTemplateByTemplateId -> PX.SM.AUTemplate (TemplateId=TemplateID)

# PX.SM.AUWorkflow (EntityType)

Label: "Workflow"
Key: ScreenID, WorkflowGUID
Entity sets: PX_SM_AUWorkflow, Workflow, AUWorkflow

PX.SM.AUWorkflow.IsActive : Edm.Boolean [required] "Active"
PX.SM.AUWorkflow.IsSystem : Edm.Boolean [required] "System"
PX.SM.AUWorkflow.ScreenID : Edm.String [key]
PX.SM.AUWorkflow.WorkflowGUID : Edm.String [key]
PX.SM.AUWorkflow.LineNbr : Edm.Int32
PX.SM.AUWorkflow.WorkflowID : Edm.String "Workflow Type"
PX.SM.AUWorkflow.WorkflowSubID : Edm.String "Workflow Subtype"
PX.SM.AUWorkflow.Description : Edm.String "Workflow Name"
PX.SM.AUWorkflow.LayoutClient : Edm.String "Layout"
PX.SM.AUWorkflow.LineNbrCustomized : Edm.Boolean
PX.SM.AUWorkflow.DescriptionCustomized : Edm.Boolean
PX.SM.AUWorkflow.LayoutClientCustomized : Edm.Boolean
PX.SM.AUWorkflow.WorkflowSubIDCustomized : Edm.Boolean
PX.SM.AUWorkflow.AUWorkflowDefinitionByScreenID -> PX.SM.AUWorkflowDefinition (ScreenID=ScreenID)
PX.SM.AUWorkflow.AUWorkflowStateCollection -> Collection(PX.SM.AUWorkflowState)

# PX.SM.AUWorkflowActionParam (EntityType)

Label: "Workflow Action Parameter"
Key: ActionName, Parameter, ScreenID
Entity sets: PX_SM_AUWorkflowActionParam, WorkflowActionParameter, AUWorkflowActionParam

PX.SM.AUWorkflowActionParam.IsActive : Edm.Boolean [required] "Active"
PX.SM.AUWorkflowActionParam.IsSystem : Edm.Boolean [required] "System"
PX.SM.AUWorkflowActionParam.ScreenID : Edm.String [key]
PX.SM.AUWorkflowActionParam.ActionName : Edm.String [key] "Action"
PX.SM.AUWorkflowActionParam.Parameter : Edm.String [key] "Parameter"
PX.SM.AUWorkflowActionParam.StateActionParamLineNbr : Edm.Int32
PX.SM.AUWorkflowActionParam.IsFromScheme : Edm.Boolean [required] "From Schema"
PX.SM.AUWorkflowActionParam.Value : Edm.String "Value"
PX.SM.AUWorkflowActionParam.StateActionParamLineNbrCustomized : Edm.Boolean
PX.SM.AUWorkflowActionParam.IsFromSchemeCustomized : Edm.Boolean
PX.SM.AUWorkflowActionParam.ValueCustomized : Edm.Boolean
PX.SM.AUWorkflowActionParam.AUScreenActionBaseStateByScreenID -> PX.SM.AUScreenActionBaseState (ActionName=ActionName, ScreenID=ScreenID)

# PX.SM.AUWorkflowActionSequence (EntityType)

Label: "Workflow Action Sequence"
Key: Condition, NextActionName, PrevActionName, ScreenID
Entity sets: PX_SM_AUWorkflowActionSequence, WorkflowActionSequence, AUWorkflowActionSequence

PX.SM.AUWorkflowActionSequence.IsActive : Edm.Boolean [required] "Active"
PX.SM.AUWorkflowActionSequence.IsSystem : Edm.Boolean [required] "System"
PX.SM.AUWorkflowActionSequence.ScreenID : Edm.String [key]
PX.SM.AUWorkflowActionSequence.PrevActionName : Edm.String [key] "Action Name"
PX.SM.AUWorkflowActionSequence.NextActionName : Edm.String [key] "Action Name"
PX.SM.AUWorkflowActionSequence.Condition : Edm.String [key] "Execution Condition"
PX.SM.AUWorkflowActionSequence.LineNbr : Edm.Int32
PX.SM.AUWorkflowActionSequence.StopOnError : Edm.Boolean [required] "Stop on Error"
PX.SM.AUWorkflowActionSequence.LineNbrCustomized : Edm.Boolean
PX.SM.AUWorkflowActionSequence.StopOnErrorCustomized : Edm.Boolean
PX.SM.AUWorkflowActionSequence.AUScreenActionBaseStateByPrevActionName -> PX.SM.AUScreenActionBaseState (ScreenID=ScreenID, PrevActionName=ActionName)

# PX.SM.AUWorkflowActionSequenceFormFieldValue (EntityType)

Label: "Dialog Box Value"
Key: Condition, FieldName, NextActionName, PrevActionName, ScreenID
Entity sets: PX_SM_AUWorkflowActionSequenceFormFieldValue, DialogBoxValue, AUWorkflowActionSequenceFormFieldValue

PX.SM.AUWorkflowActionSequenceFormFieldValue.IsActive : Edm.Boolean [required] "Active"
PX.SM.AUWorkflowActionSequenceFormFieldValue.IsSystem : Edm.Boolean [required] "System"
PX.SM.AUWorkflowActionSequenceFormFieldValue.ScreenID : Edm.String [key]
PX.SM.AUWorkflowActionSequenceFormFieldValue.PrevActionName : Edm.String [key] "Action Name"
PX.SM.AUWorkflowActionSequenceFormFieldValue.NextActionName : Edm.String [key] "Action Name"
PX.SM.AUWorkflowActionSequenceFormFieldValue.Condition : Edm.String [key] "Condition"
PX.SM.AUWorkflowActionSequenceFormFieldValue.FieldName : Edm.String [key] "Field Name"
PX.SM.AUWorkflowActionSequenceFormFieldValue.IsFromScheme : Edm.Boolean [required] "From Schema"
PX.SM.AUWorkflowActionSequenceFormFieldValue.Value : Edm.String "New Value"
PX.SM.AUWorkflowActionSequenceFormFieldValue.IsFromSchemeCustomized : Edm.Boolean
PX.SM.AUWorkflowActionSequenceFormFieldValue.ValueCustomized : Edm.Boolean

# PX.SM.AUWorkflowActionUpdateField (EntityType)

Label: "Workflow Action Field"
Key: ActionName, FieldName, ScreenID
Entity sets: PX_SM_AUWorkflowActionUpdateField, WorkflowActionField, AUWorkflowActionUpdateField

PX.SM.AUWorkflowActionUpdateField.IsActive : Edm.Boolean [required] "Active"
PX.SM.AUWorkflowActionUpdateField.IsSystem : Edm.Boolean [required] "System"
PX.SM.AUWorkflowActionUpdateField.ScreenID : Edm.String [key]
PX.SM.AUWorkflowActionUpdateField.ActionName : Edm.String [key] "Action"
PX.SM.AUWorkflowActionUpdateField.FieldName : Edm.String [key] "Field"
PX.SM.AUWorkflowActionUpdateField.StateActionFieldLineNbr : Edm.Int32
PX.SM.AUWorkflowActionUpdateField.IsFromScheme : Edm.Boolean [required] "From Schema"
PX.SM.AUWorkflowActionUpdateField.Value : Edm.String "New Value"
PX.SM.AUWorkflowActionUpdateField.StateActionFieldLineNbrCustomized : Edm.Boolean
PX.SM.AUWorkflowActionUpdateField.IsFromSchemeCustomized : Edm.Boolean
PX.SM.AUWorkflowActionUpdateField.ValueCustomized : Edm.Boolean
PX.SM.AUWorkflowActionUpdateField.AUScreenActionBaseStateByScreenID -> PX.SM.AUScreenActionBaseState (ActionName=ActionName, ScreenID=ScreenID)

# PX.SM.AUWorkflowDefinition (EntityType)

Label: "Workflow Definition"
Key: ScreenID
Entity sets: PX_SM_AUWorkflowDefinition, WorkflowDefinition, AUWorkflowDefinition
Non-filterable, non-selectable: AllowWorkflowCustomization

PX.SM.AUWorkflowDefinition.ScreenID : Edm.String [key]
PX.SM.AUWorkflowDefinition.StateField : Edm.String "State Identifier"
PX.SM.AUWorkflowDefinition.FlowTypeField : Edm.String "Type Identifier"
PX.SM.AUWorkflowDefinition.EnableWorkflowIDField : Edm.Boolean [required] "Allow Users to Modify Type"
PX.SM.AUWorkflowDefinition.FlowSubTypeField : Edm.String "Subtype Identifier"
PX.SM.AUWorkflowDefinition.EnableWorkflowSubTypeField : Edm.Boolean "Allow Users to Modify Subtype"
PX.SM.AUWorkflowDefinition.AutoSaveDefault : Edm.Boolean
PX.SM.AUWorkflowDefinition.AllowWorkflowCustomization : Edm.Boolean
PX.SM.AUWorkflowDefinition.StateFieldCustomized : Edm.Boolean
PX.SM.AUWorkflowDefinition.FlowTypeFieldCustomized : Edm.Boolean
PX.SM.AUWorkflowDefinition.EnableWorkflowIDFieldCustomized : Edm.Boolean
PX.SM.AUWorkflowDefinition.FlowSubTypeFieldCustomized : Edm.Boolean
PX.SM.AUWorkflowDefinition.EnableWorkflowSubTypeFieldCustomized : Edm.Boolean
PX.SM.AUWorkflowDefinition.AUWorkflowCollection -> Collection(PX.SM.AUWorkflow)

# PX.SM.AUWorkflowForm (EntityType)

Key: FormName, Screen
Entity sets: PX_SM_AUWorkflowForm

PX.SM.AUWorkflowForm.IsActive : Edm.Boolean [required] "Active"
PX.SM.AUWorkflowForm.IsSystem : Edm.Boolean [required] "System"
PX.SM.AUWorkflowForm.Screen : Edm.String [key] "Screen"
PX.SM.AUWorkflowForm.FormName : Edm.String [key] "Dialog Box Name"
PX.SM.AUWorkflowForm.DisplayName : Edm.String "Title"
PX.SM.AUWorkflowForm.Columns : Edm.Int32 "Number of Columns"
PX.SM.AUWorkflowForm.DacType : Edm.String "Dac Type"
PX.SM.AUWorkflowForm.DisplayNameCustomized : Edm.Boolean
PX.SM.AUWorkflowForm.ColumnsCustomized : Edm.Boolean
PX.SM.AUWorkflowForm.DacTypeCustomized : Edm.Boolean

# PX.SM.AUWorkflowFormField (EntityType)

Label: "Workflow Form Field"
Key: FieldName, FormName, Screen
Entity sets: PX_SM_AUWorkflowFormField, WorkflowFormField, AUWorkflowFormField

PX.SM.AUWorkflowFormField.IsActive : Edm.Boolean [required] "Active"
PX.SM.AUWorkflowFormField.IsSystem : Edm.Boolean [required] "System"
PX.SM.AUWorkflowFormField.Screen : Edm.String [key] "Screen"
PX.SM.AUWorkflowFormField.FormName : Edm.String [key] "Dialog Box Name"
PX.SM.AUWorkflowFormField.FieldName : Edm.String [key] "Field Name"
PX.SM.AUWorkflowFormField.LineNumber : Edm.Int32 "Column Span"
PX.SM.AUWorkflowFormField.DisplayName : Edm.String "Display Name"
PX.SM.AUWorkflowFormField.SchemaField : Edm.String "Schema Field"
PX.SM.AUWorkflowFormField.FromScheme : Edm.Boolean [required] "From Schema"
PX.SM.AUWorkflowFormField.DefaultValue : Edm.String "Value"
PX.SM.AUWorkflowFormField.Required : Edm.Boolean [required]
PX.SM.AUWorkflowFormField.RequiredCondition : Edm.String "Required"
PX.SM.AUWorkflowFormField.HideCondition : Edm.String "Hidden"
PX.SM.AUWorkflowFormField.ColumnSpan : Edm.Int32 "Column Span"
PX.SM.AUWorkflowFormField.ControlSize : Edm.String "Control Size"
PX.SM.AUWorkflowFormField.AvailableValues : Edm.String "Available Values"
PX.SM.AUWorkflowFormField.ComboBoxValues : Edm.String "Combo Box Values"
PX.SM.AUWorkflowFormField.ComboBoxValuesSource : Edm.String "Combo Box Values Source"
PX.SM.AUWorkflowFormField.ComboboxAndDefaultSourceField : Edm.String "Source Field Name"
PX.SM.AUWorkflowFormField.DefaultValueSource : Edm.String "Combo Box Source Field Name"
PX.SM.AUWorkflowFormField.LineNumberCustomized : Edm.Boolean
PX.SM.AUWorkflowFormField.DisplayNameCustomized : Edm.Boolean
PX.SM.AUWorkflowFormField.SchemaFieldCustomized : Edm.Boolean
PX.SM.AUWorkflowFormField.FromSchemeCustomized : Edm.Boolean
PX.SM.AUWorkflowFormField.DefaultValueCustomized : Edm.Boolean
PX.SM.AUWorkflowFormField.RequiredCustomized : Edm.Boolean
PX.SM.AUWorkflowFormField.RequiredConditionCustomized : Edm.Boolean
PX.SM.AUWorkflowFormField.ColumnSpanCustomized : Edm.Boolean
PX.SM.AUWorkflowFormField.ControlSizeCustomized : Edm.Boolean
PX.SM.AUWorkflowFormField.AvailableValuesCustomized : Edm.Boolean
PX.SM.AUWorkflowFormField.ComboBoxValuesCustomized : Edm.Boolean
PX.SM.AUWorkflowFormField.HideConditionCustomized : Edm.Boolean
PX.SM.AUWorkflowFormField.ComboBoxValuesSourceCustomized : Edm.Boolean
PX.SM.AUWorkflowFormField.ComboboxAndDefaultSourceFieldCustomized : Edm.Boolean
PX.SM.AUWorkflowFormField.DefaultValueSourceCustomized : Edm.Boolean

# PX.SM.AUWorkflowHandler (EntityType)

Label: "Workflow Handler"
Key: HandlerName, ScreenID
Entity sets: PX_SM_AUWorkflowHandler, WorkflowHandler, AUWorkflowHandler

PX.SM.AUWorkflowHandler.IsActive : Edm.Boolean [required] "Active"
PX.SM.AUWorkflowHandler.IsSystem : Edm.Boolean [required] "System"
PX.SM.AUWorkflowHandler.ScreenID : Edm.String [key]
PX.SM.AUWorkflowHandler.HandlerName : Edm.String [key] "Action Name"
PX.SM.AUWorkflowHandler.DisplayName : Edm.String "Display Name"
PX.SM.AUWorkflowHandler.EventName : Edm.String "Event Name"
PX.SM.AUWorkflowHandler.EventContainerName : Edm.String "Event Container Name"
PX.SM.AUWorkflowHandler.Condition : Edm.String "Condition"
PX.SM.AUWorkflowHandler.SelectType : Edm.String "Select Type"
PX.SM.AUWorkflowHandler.AllowMultipleSelect : Edm.Boolean [required] "Allow Multiple Select"
PX.SM.AUWorkflowHandler.UseParameterAsPrimarySource : Edm.Boolean [required] "Use Parameter As Primary Source"
PX.SM.AUWorkflowHandler.UseTargetAsPrimarySource : Edm.Boolean [required] "Use Target As Primary Source"
PX.SM.AUWorkflowHandler.SelectIsCommand : Edm.Boolean
PX.SM.AUWorkflowHandler.UpcastType : Edm.String
PX.SM.AUWorkflowHandler.ConditionCustomized : Edm.Boolean
PX.SM.AUWorkflowHandler.SelectTypeCustomized : Edm.Boolean
PX.SM.AUWorkflowHandler.AllowMultipleSelectCustomized : Edm.Boolean
PX.SM.AUWorkflowHandler.UseParameterAsPrimarySourceCustomized : Edm.Boolean
PX.SM.AUWorkflowHandler.UseTargetAsPrimarySourceCustomized : Edm.Boolean
PX.SM.AUWorkflowHandler.SelectIsCommandCustomized : Edm.Boolean
PX.SM.AUWorkflowHandler.DisplayNameCustomized : Edm.Boolean
PX.SM.AUWorkflowHandler.EventNameCustomized : Edm.Boolean
PX.SM.AUWorkflowHandler.AUWorkflowHandlerUpdateFieldCollection -> Collection(PX.SM.AUWorkflowHandlerUpdateField)

# PX.SM.AUWorkflowHandlerUpdateField (EntityType)

Label: "Workflow Handler Field"
Key: FieldName, HandlerName, ScreenID
Entity sets: PX_SM_AUWorkflowHandlerUpdateField, WorkflowHandlerField, AUWorkflowHandlerUpdateField

PX.SM.AUWorkflowHandlerUpdateField.IsActive : Edm.Boolean [required] "Active"
PX.SM.AUWorkflowHandlerUpdateField.IsSystem : Edm.Boolean [required] "System"
PX.SM.AUWorkflowHandlerUpdateField.ScreenID : Edm.String [key]
PX.SM.AUWorkflowHandlerUpdateField.HandlerName : Edm.String [key] "Action Name"
PX.SM.AUWorkflowHandlerUpdateField.FieldName : Edm.String [key] "Field"
PX.SM.AUWorkflowHandlerUpdateField.HandlerFieldLineNbr : Edm.Int32
PX.SM.AUWorkflowHandlerUpdateField.IsFromScheme : Edm.Boolean [required] "From Schema"
PX.SM.AUWorkflowHandlerUpdateField.Value : Edm.String "New Value"
PX.SM.AUWorkflowHandlerUpdateField.AUWorkflowHandlerByScreenID -> PX.SM.AUWorkflowHandler (HandlerName=HandlerName, ScreenID=ScreenID)

# PX.SM.AUWorkflowOnEnterStateField (EntityType)

Label: "Workflow Update Field On Enter State"
Key: FieldName, ScreenID, StateName, WorkflowGUID
Entity sets: PX_SM_AUWorkflowOnEnterStateField, WorkflowUpdateFieldOnEnterState, AUWorkflowOnEnterStateField

PX.SM.AUWorkflowOnEnterStateField.IsActive : Edm.Boolean [required] "Active"
PX.SM.AUWorkflowOnEnterStateField.IsSystem : Edm.Boolean [required] "System"
PX.SM.AUWorkflowOnEnterStateField.ScreenID : Edm.String [key]
PX.SM.AUWorkflowOnEnterStateField.WorkflowGUID : Edm.String [key]
PX.SM.AUWorkflowOnEnterStateField.StateName : Edm.String [key] "State"
PX.SM.AUWorkflowOnEnterStateField.FieldName : Edm.String [key] "Field Name"
PX.SM.AUWorkflowOnEnterStateField.OnEnterStateFieldLineNbr : Edm.Int32
PX.SM.AUWorkflowOnEnterStateField.IsFromScheme : Edm.Boolean [required] "From Schema"
PX.SM.AUWorkflowOnEnterStateField.Value : Edm.String "New Value"
PX.SM.AUWorkflowOnEnterStateField.OnEnterStateFieldLineNbrCustomized : Edm.Boolean
PX.SM.AUWorkflowOnEnterStateField.IsFromSchemeCustomized : Edm.Boolean
PX.SM.AUWorkflowOnEnterStateField.ValueCustomized : Edm.Boolean
PX.SM.AUWorkflowOnEnterStateField.AUWorkflowStateByScreenID -> PX.SM.AUWorkflowState (StateName=Identifier, WorkflowGUID=WorkflowGUID, ScreenID=ScreenID)

# PX.SM.AUWorkflowOnLeaveStateField (EntityType)

Label: "Workflow Update Field On Leave State"
Key: FieldName, ScreenID, StateName, WorkflowGUID
Entity sets: PX_SM_AUWorkflowOnLeaveStateField, WorkflowUpdateFieldOnLeaveState, AUWorkflowOnLeaveStateField

PX.SM.AUWorkflowOnLeaveStateField.IsActive : Edm.Boolean [required] "Active"
PX.SM.AUWorkflowOnLeaveStateField.IsSystem : Edm.Boolean [required] "System"
PX.SM.AUWorkflowOnLeaveStateField.ScreenID : Edm.String [key]
PX.SM.AUWorkflowOnLeaveStateField.WorkflowGUID : Edm.String [key]
PX.SM.AUWorkflowOnLeaveStateField.StateName : Edm.String [key] "State"
PX.SM.AUWorkflowOnLeaveStateField.FieldName : Edm.String [key] "Field Name"
PX.SM.AUWorkflowOnLeaveStateField.OnLeaveStateFieldLineNbr : Edm.Int32
PX.SM.AUWorkflowOnLeaveStateField.IsFromScheme : Edm.Boolean [required] "From Schema"
PX.SM.AUWorkflowOnLeaveStateField.Value : Edm.String "New Value"
PX.SM.AUWorkflowOnLeaveStateField.OnLeaveStateFieldLineNbrCustomized : Edm.Boolean
PX.SM.AUWorkflowOnLeaveStateField.IsFromSchemeCustomized : Edm.Boolean
PX.SM.AUWorkflowOnLeaveStateField.ValueCustomized : Edm.Boolean
PX.SM.AUWorkflowOnLeaveStateField.AUWorkflowStateByScreenID -> PX.SM.AUWorkflowState (StateName=Identifier, WorkflowGUID=WorkflowGUID, ScreenID=ScreenID)

# PX.SM.AUWorkflowState (EntityType)

Label: "Workflow State"
Key: Identifier, ScreenID, WorkflowGUID
Entity sets: PX_SM_AUWorkflowState, WorkflowState, AUWorkflowState

PX.SM.AUWorkflowState.IsActive : Edm.Boolean [required] "Active"
PX.SM.AUWorkflowState.IsSystem : Edm.Boolean [required] "System"
PX.SM.AUWorkflowState.ScreenID : Edm.String [key]
PX.SM.AUWorkflowState.WorkflowGUID : Edm.String [key]
PX.SM.AUWorkflowState.Identifier : Edm.String [key] "Identifier"
PX.SM.AUWorkflowState.StateLineNbr : Edm.Int32
PX.SM.AUWorkflowState.IsInitial : Edm.Boolean [required] "Initial State of the Workflow"
PX.SM.AUWorkflowState.Layout : Edm.String "Layout"
PX.SM.AUWorkflowState.Description : Edm.String "Description"
PX.SM.AUWorkflowState.NextState : Edm.String "Next State"
PX.SM.AUWorkflowState.StateType : Edm.String "State Type"
PX.SM.AUWorkflowState.ParentState : Edm.String "Parent State"
PX.SM.AUWorkflowState.SkipConditionID : Edm.Guid "Skip Condition"
PX.SM.AUWorkflowState.StateLineNbrCustomized : Edm.Boolean
PX.SM.AUWorkflowState.IsInitialCustomized : Edm.Boolean
PX.SM.AUWorkflowState.LayoutCustomized : Edm.Boolean
PX.SM.AUWorkflowState.DescriptionCustomized : Edm.Boolean
PX.SM.AUWorkflowState.NextStateCustomized : Edm.Boolean
PX.SM.AUWorkflowState.StateTypeCustomized : Edm.Boolean
PX.SM.AUWorkflowState.ParentStateCustomized : Edm.Boolean
PX.SM.AUWorkflowState.SkipConditionIDCustomized : Edm.Boolean
PX.SM.AUWorkflowState.AUWorkflowByScreenID -> PX.SM.AUWorkflow (WorkflowGUID=WorkflowGUID, ScreenID=ScreenID)
PX.SM.AUWorkflowState.AUWorkflowStateActionCollection -> Collection(PX.SM.AUWorkflowStateAction)
PX.SM.AUWorkflowState.AUWorkflowStateEventHandlerCollection -> Collection(PX.SM.AUWorkflowStateEventHandler)
PX.SM.AUWorkflowState.AUWorkflowTransitionCollection -> Collection(PX.SM.AUWorkflowTransition)
PX.SM.AUWorkflowState.AUWorkflowOnEnterStateFieldCollection -> Collection(PX.SM.AUWorkflowOnEnterStateField)
PX.SM.AUWorkflowState.AUWorkflowStatePropertyCollection -> Collection(PX.SM.AUWorkflowStateProperty)
PX.SM.AUWorkflowState.AUWorkflowOnLeaveStateFieldCollection -> Collection(PX.SM.AUWorkflowOnLeaveStateField)
PX.SM.AUWorkflowState.AUWorkflowStateStatusConditionCollection -> Collection(PX.SM.AUWorkflowStateStatusCondition)

# PX.SM.AUWorkflowStateAction (EntityType)

Label: "State Action"
Key: ActionName, ScreenID, StateName, WorkflowGUID
Entity sets: PX_SM_AUWorkflowStateAction, StateAction, AUWorkflowStateAction

PX.SM.AUWorkflowStateAction.IsActive : Edm.Boolean [required] "Active"
PX.SM.AUWorkflowStateAction.IsSystem : Edm.Boolean [required] "System"
PX.SM.AUWorkflowStateAction.ScreenID : Edm.String [key]
PX.SM.AUWorkflowStateAction.WorkflowGUID : Edm.String [key]
PX.SM.AUWorkflowStateAction.StateName : Edm.String [key] "State"
PX.SM.AUWorkflowStateAction.ActionName : Edm.String [key] "Action"
PX.SM.AUWorkflowStateAction.StateActionLineNbr : Edm.Int32
PX.SM.AUWorkflowStateAction.IsTopLevel : Edm.Boolean [required] "Top Level"
PX.SM.AUWorkflowStateAction.IsDisabled : Edm.Boolean [required] "Disabled"
PX.SM.AUWorkflowStateAction.IsHide : Edm.Boolean [required] "Hidden"
PX.SM.AUWorkflowStateAction.AutoRun : Edm.String "Auto-Run Action"
PX.SM.AUWorkflowStateAction.Connotation : Edm.String "Connotation"
PX.SM.AUWorkflowStateAction.StateActionLineNbrCustomized : Edm.Boolean
PX.SM.AUWorkflowStateAction.IsTopLevelCustomized : Edm.Boolean
PX.SM.AUWorkflowStateAction.IsDisabledCustomized : Edm.Boolean
PX.SM.AUWorkflowStateAction.IsHideCustomized : Edm.Boolean
PX.SM.AUWorkflowStateAction.AutoRunCustomized : Edm.Boolean
PX.SM.AUWorkflowStateAction.ConnotationCustomized : Edm.Boolean
PX.SM.AUWorkflowStateAction.AUWorkflowStateByScreenID -> PX.SM.AUWorkflowState (StateName=Identifier, WorkflowGUID=WorkflowGUID, ScreenID=ScreenID)

# PX.SM.AUWorkflowStateActionField (EntityType)

Label: "Workflow Action Field"
Key: ActionName, FieldName, ScreenID
Entity sets: PX_SM_AUWorkflowStateActionField, WorkflowActionField1, AUWorkflowStateActionField

PX.SM.AUWorkflowStateActionField.IsActive : Edm.Boolean [required] "Active"
PX.SM.AUWorkflowStateActionField.IsSystem : Edm.Boolean [required] "System"
PX.SM.AUWorkflowStateActionField.ScreenID : Edm.String [key]
PX.SM.AUWorkflowStateActionField.ActionName : Edm.String [key] "Action"
PX.SM.AUWorkflowStateActionField.FieldName : Edm.String [key] "Field"
PX.SM.AUWorkflowStateActionField.StateActionFieldLineNbr : Edm.Int32
PX.SM.AUWorkflowStateActionField.IsFromScheme : Edm.Boolean [required] "From Schema"
PX.SM.AUWorkflowStateActionField.Value : Edm.String "New Value"
PX.SM.AUWorkflowStateActionField.StateActionFieldLineNbrCustomized : Edm.Boolean
PX.SM.AUWorkflowStateActionField.IsFromSchemeCustomized : Edm.Boolean
PX.SM.AUWorkflowStateActionField.ValueCustomized : Edm.Boolean
PX.SM.AUWorkflowStateActionField.AUScreenActionBaseStateByScreenID -> PX.SM.AUScreenActionBaseState (ActionName=ActionName, ScreenID=ScreenID)

# PX.SM.AUWorkflowStateActionParam (EntityType)

Label: "Workflow Action Parameter"
Key: ActionName, Parameter, ScreenID
Entity sets: PX_SM_AUWorkflowStateActionParam, WorkflowActionParameter1, AUWorkflowStateActionParam

PX.SM.AUWorkflowStateActionParam.IsActive : Edm.Boolean [required] "Active"
PX.SM.AUWorkflowStateActionParam.IsSystem : Edm.Boolean [required] "System"
PX.SM.AUWorkflowStateActionParam.ScreenID : Edm.String [key]
PX.SM.AUWorkflowStateActionParam.ActionName : Edm.String [key] "Action"
PX.SM.AUWorkflowStateActionParam.Parameter : Edm.String [key] "Parameter"
PX.SM.AUWorkflowStateActionParam.StateActionParamLineNbr : Edm.Int32
PX.SM.AUWorkflowStateActionParam.IsFromScheme : Edm.Boolean [required] "From Schema"
PX.SM.AUWorkflowStateActionParam.Value : Edm.String "Value"
PX.SM.AUWorkflowStateActionParam.StateActionParamLineNbrCustomized : Edm.Boolean
PX.SM.AUWorkflowStateActionParam.IsFromSchemeCustomized : Edm.Boolean
PX.SM.AUWorkflowStateActionParam.ValueCustomized : Edm.Boolean
PX.SM.AUWorkflowStateActionParam.AUScreenActionBaseStateByScreenID -> PX.SM.AUScreenActionBaseState (ActionName=ActionName, ScreenID=ScreenID)

# PX.SM.AUWorkflowStateEventHandler (EntityType)

Label: "State Event Handler"
Key: HandlerName, ScreenID, StateName, WorkflowGUID
Entity sets: PX_SM_AUWorkflowStateEventHandler, StateEventHandler, AUWorkflowStateEventHandler

PX.SM.AUWorkflowStateEventHandler.IsActive : Edm.Boolean [required] "Active"
PX.SM.AUWorkflowStateEventHandler.IsSystem : Edm.Boolean [required] "System"
PX.SM.AUWorkflowStateEventHandler.ScreenID : Edm.String [key]
PX.SM.AUWorkflowStateEventHandler.WorkflowGUID : Edm.String [key]
PX.SM.AUWorkflowStateEventHandler.StateName : Edm.String [key] "State"
PX.SM.AUWorkflowStateEventHandler.HandlerName : Edm.String [key] "Handler Name"
PX.SM.AUWorkflowStateEventHandler.StateHandlerLineNbr : Edm.Int32
PX.SM.AUWorkflowStateEventHandler.StateHandlerLineNbrCustomized : Edm.Boolean
PX.SM.AUWorkflowStateEventHandler.AUWorkflowStateByScreenID -> PX.SM.AUWorkflowState (StateName=Identifier, WorkflowGUID=WorkflowGUID, ScreenID=ScreenID)

# PX.SM.AUWorkflowStateProperty (EntityType)

Label: "State Property"
Key: FieldName, ObjectName, ScreenID, StateName, WorkflowGUID
Entity sets: PX_SM_AUWorkflowStateProperty, StateProperty, AUWorkflowStateProperty

PX.SM.AUWorkflowStateProperty.IsActive : Edm.Boolean [required] "Active"
PX.SM.AUWorkflowStateProperty.IsSystem : Edm.Boolean [required] "System"
PX.SM.AUWorkflowStateProperty.ScreenID : Edm.String [key]
PX.SM.AUWorkflowStateProperty.WorkflowGUID : Edm.String [key]
PX.SM.AUWorkflowStateProperty.StateName : Edm.String [key] "State"
PX.SM.AUWorkflowStateProperty.ObjectName : Edm.String [key] "Table Name"
PX.SM.AUWorkflowStateProperty.FieldName : Edm.String [key] "Field Name"
PX.SM.AUWorkflowStateProperty.StatePropertyLineNbr : Edm.Int32
PX.SM.AUWorkflowStateProperty.IsDisabled : Edm.Boolean [required] "Disabled"
PX.SM.AUWorkflowStateProperty.IsHide : Edm.Boolean [required] "Hidden"
PX.SM.AUWorkflowStateProperty.IsRequired : Edm.Boolean [required] "Required"
PX.SM.AUWorkflowStateProperty.DefaultValue : Edm.String "Default Value"
PX.SM.AUWorkflowStateProperty.ComboBoxValues : Edm.String "Combo Box Values"
PX.SM.AUWorkflowStateProperty.StatePropertyLineNbrCustomized : Edm.Boolean
PX.SM.AUWorkflowStateProperty.IsDisabledCustomized : Edm.Boolean
PX.SM.AUWorkflowStateProperty.IsHideCustomized : Edm.Boolean
PX.SM.AUWorkflowStateProperty.IsRequiredCustomized : Edm.Boolean
PX.SM.AUWorkflowStateProperty.DefaultValueCustomized : Edm.Boolean
PX.SM.AUWorkflowStateProperty.ComboBoxValuesCustomized : Edm.Boolean
PX.SM.AUWorkflowStateProperty.AUWorkflowStateByScreenID -> PX.SM.AUWorkflowState (StateName=Identifier, WorkflowGUID=WorkflowGUID, ScreenID=ScreenID)

# PX.SM.AUWorkflowStateStatusCondition (EntityType)

Label: "State Status Condition"
Key: Condition, ScreenID, StateName, WorkflowGUID
Entity sets: PX_SM_AUWorkflowStateStatusCondition, StateStatusCondition, AUWorkflowStateStatusCondition

PX.SM.AUWorkflowStateStatusCondition.IsActive : Edm.Boolean [required] "Active"
PX.SM.AUWorkflowStateStatusCondition.IsSystem : Edm.Boolean [required] "System"
PX.SM.AUWorkflowStateStatusCondition.ScreenID : Edm.String [key]
PX.SM.AUWorkflowStateStatusCondition.WorkflowGUID : Edm.String [key]
PX.SM.AUWorkflowStateStatusCondition.StateName : Edm.String [key] "State"
PX.SM.AUWorkflowStateStatusCondition.Condition : Edm.String [key] "Condition"
PX.SM.AUWorkflowStateStatusCondition.StateStatusConditionLineNbr : Edm.Int32
PX.SM.AUWorkflowStateStatusCondition.ErrorMessage : Edm.String "Error Message"
PX.SM.AUWorkflowStateStatusCondition.StateStatusConditionLineNbrCustomized : Edm.Boolean
PX.SM.AUWorkflowStateStatusCondition.ErrorMessageCustomized : Edm.Boolean
PX.SM.AUWorkflowStateStatusCondition.AUWorkflowStateByScreenID -> PX.SM.AUWorkflowState (StateName=Identifier, WorkflowGUID=WorkflowGUID, ScreenID=ScreenID)

# PX.SM.AUWorkflowTransition (EntityType)

Label: "Workflow Transition"
Key: ScreenID, TransitionID, WorkflowGUID
Entity sets: PX_SM_AUWorkflowTransition, WorkflowTransition, AUWorkflowTransition

PX.SM.AUWorkflowTransition.IsActive : Edm.Boolean [required] "Active"
PX.SM.AUWorkflowTransition.IsSystem : Edm.Boolean [required] "System"
PX.SM.AUWorkflowTransition.ScreenID : Edm.String [key]
PX.SM.AUWorkflowTransition.WorkflowGUID : Edm.String [key]
PX.SM.AUWorkflowTransition.TransitionID : Edm.Guid [key] "Transition ID"
PX.SM.AUWorkflowTransition.FromStateName : Edm.String "Original State"
PX.SM.AUWorkflowTransition.TransitionLineNbr : Edm.Int32
PX.SM.AUWorkflowTransition.TargetStateName : Edm.String "Target State"
PX.SM.AUWorkflowTransition.DisplayName : Edm.String "Display Name"
PX.SM.AUWorkflowTransition.ConditionID : Edm.Guid "Condition"
PX.SM.AUWorkflowTransition.ActionName : Edm.String "Action Name"
PX.SM.AUWorkflowTransition.DisablePersist : Edm.Boolean "Disable Persist"
PX.SM.AUWorkflowTransition.TriggeredBy : Edm.Int32
PX.SM.AUWorkflowTransition.Layout : Edm.String "Layout"
PX.SM.AUWorkflowTransition.FromStateNameCustomized : Edm.Boolean
PX.SM.AUWorkflowTransition.TransitionLineNbrCustomized : Edm.Boolean
PX.SM.AUWorkflowTransition.TargetStateNameCustomized : Edm.Boolean
PX.SM.AUWorkflowTransition.DisplayNameCustomized : Edm.Boolean
PX.SM.AUWorkflowTransition.ConditionIDCustomized : Edm.Boolean
PX.SM.AUWorkflowTransition.ActionNameCustomized : Edm.Boolean
PX.SM.AUWorkflowTransition.DisablePersistCustomized : Edm.Boolean
PX.SM.AUWorkflowTransition.TriggeredByCustomized : Edm.Boolean
PX.SM.AUWorkflowTransition.LayoutCustomized : Edm.Boolean
PX.SM.AUWorkflowTransition.AUWorkflowStateByScreenID -> PX.SM.AUWorkflowState (FromStateName=Identifier, WorkflowGUID=WorkflowGUID, ScreenID=ScreenID)
PX.SM.AUWorkflowTransition.AUWorkflowTransitionFieldCollection -> Collection(PX.SM.AUWorkflowTransitionField)

# PX.SM.AUWorkflowTransitionField (EntityType)

Label: "Transition Update Fields After"
Key: FieldName, ScreenID, TransitionID, WorkflowGUID
Entity sets: PX_SM_AUWorkflowTransitionField, TransitionUpdateFieldsAfter, AUWorkflowTransitionField

PX.SM.AUWorkflowTransitionField.IsActive : Edm.Boolean [required] "Active"
PX.SM.AUWorkflowTransitionField.IsSystem : Edm.Boolean [required] "System"
PX.SM.AUWorkflowTransitionField.ScreenID : Edm.String [key]
PX.SM.AUWorkflowTransitionField.WorkflowGUID : Edm.String [key]
PX.SM.AUWorkflowTransitionField.TransitionID : Edm.Guid [key] "Transition ID"
PX.SM.AUWorkflowTransitionField.FieldName : Edm.String [key] "Field Name"
PX.SM.AUWorkflowTransitionField.TransitionFieldLineNbr : Edm.Int32
PX.SM.AUWorkflowTransitionField.IsFromScheme : Edm.Boolean [required] "From Schema"
PX.SM.AUWorkflowTransitionField.Value : Edm.String "New Value"
PX.SM.AUWorkflowTransitionField.TransitionFieldLineNbrCustomized : Edm.Boolean
PX.SM.AUWorkflowTransitionField.IsFromSchemeCustomized : Edm.Boolean
PX.SM.AUWorkflowTransitionField.ValueCustomized : Edm.Boolean
PX.SM.AUWorkflowTransitionField.AUWorkflowTransitionByScreenID -> PX.SM.AUWorkflowTransition (TransitionID=TransitionID, WorkflowGUID=WorkflowGUID, ScreenID=ScreenID)

# PX.SM.BlobProviderSettings (EntityType)

Key: Name
Entity sets: PX_SM_BlobProviderSettings

PX.SM.BlobProviderSettings.Name : Edm.String [key] "Name"
PX.SM.BlobProviderSettings.Value : Edm.String "Value"

# PX.SM.BlobStorageConfig (EntityType)

Singletons: PX_SM_BlobStorageConfig

PX.SM.BlobStorageConfig.Provider : Edm.String "Provider"
PX.SM.BlobStorageConfig.AllowWrite : Edm.Boolean "Allow Saving Files"
PX.SM.BlobStorageConfig.IsActive : Edm.Boolean "IsActive"

# PX.SM.BPEventInProject (EntityType)

Label: "Business Process Event"
BaseType: PX.BusinessProcess.DAC.BPEvent
Key: Name (inherited from PX.BusinessProcess.DAC.BPEvent)
Entity sets: PX_SM_BPEventInProject

PX.SM.BPEventInProject.CompanyID : Edm.Int32 "CompanyId"

# PX.SM.Branch (EntityType)

Key: BranchCD, RoleName
Entity sets: PX_SM_Branch
Non-filterable, non-selectable: DeletedDatabaseRecord

PX.SM.Branch.BranchID : Edm.Int32
PX.SM.Branch.BranchCD : Edm.String [key] "Branch"
PX.SM.Branch.RoleName : Edm.String [key] "Role Name"
PX.SM.Branch.LogoName : Edm.String
PX.SM.Branch.MainLogoName : Edm.String
PX.SM.Branch.OrganizationID : Edm.Int32
PX.SM.Branch.tstamp : Edm.Binary
PX.SM.Branch.DeletedDatabaseRecord : Edm.Boolean [required] "DeletedDatabaseRecord"
PX.SM.Branch.BAccountByBAccountID -> PX.Objects.CR.BAccount
PX.SM.Branch.RolesByRoleName -> PX.SM.Roles (RoleName=Rolename)
PX.SM.Branch.SMPrinterByDefaultPrinterID -> PX.SM.SMPrinter
PX.SM.Branch.OrganizationByOrganizationID -> PX.Objects.GL.DAC.Organization (OrganizationID=OrganizationID)
PX.SM.Branch.CountryByCountryID -> PX.Objects.CS.Country
PX.SM.Branch.CurrencyByBaseCuryID -> PX.Objects.CM.Currency
PX.SM.Branch.CurrencyListByBaseCuryID -> PX.Objects.CM.CurrencyList
PX.SM.Branch.LedgerByLedgerID -> PX.Objects.GL.Ledger
PX.SM.Branch.EPEmployeeCollection -> Collection(PX.Objects.EP.EPEmployee)
PX.SM.Branch.PRDeductionDetailCollection -> Collection(PX.Objects.PR.PRDeductionDetail)
PX.SM.Branch.PRBenefitDetailCollection -> Collection(PX.Objects.PR.PRBenefitDetail)
PX.SM.Branch.PRTaxDetailCollection -> Collection(PX.Objects.PR.PRTaxDetail)
PX.SM.Branch.PREarningDetailCollection -> Collection(PX.Objects.PR.PREarningDetail)
PX.SM.Branch.PRPaymentCollection -> Collection(PX.Objects.PR.PRPayment)
PX.SM.Branch.PRPaymentWCPremiumCollection -> Collection(PX.Objects.PR.PRPaymentWCPremium)
PX.SM.Branch.PRPTODetailCollection -> Collection(PX.Objects.PR.PRPTODetail)
PX.SM.Branch.PRWorkCompensationBenefitRateCollection -> Collection(PX.Objects.PR.PRWorkCompensationBenefitRate)
PX.SM.Branch.ARRetainageWithApplicationsCollection -> Collection(PX.Objects.AR.ARRetainageWithApplications)
PX.SM.Branch.DiscrepancyByAccountEnqResultCollection -> Collection(ReconciliationTools.DiscrepancyByAccountEnqResult)
PX.SM.Branch.TaxTranCollection -> Collection(PX.Objects.TX.TaxTran)
PX.SM.Branch.ARPaymentCollection -> Collection(PX.Objects.AR.ARPayment)
PX.SM.Branch.PMProjectCollection -> Collection(PX.Objects.PM.PMProject)
PX.SM.Branch.ARInvoiceCollection -> Collection(PX.Objects.AR.ARInvoice)
PX.SM.Branch.EPActivityReleaseCollection -> Collection(PX.Objects.EP.EPActivityRelease)
PX.SM.Branch.EPActivityApprove2Collection -> Collection(PX.Objects.EP.EPActivityApprove2)
PX.SM.Branch.APInvoiceCollection -> Collection(PX.Objects.AP.APInvoice)
PX.SM.Branch.APPaymentCollection -> Collection(PX.Objects.AP.APPayment)
PX.SM.Branch.GLHistoryCollection -> Collection(PX.Objects.GL.GLHistory)
PX.SM.Branch.ARRegisterCollection -> Collection(PX.Objects.AR.ARRegister)
PX.SM.Branch.SVATConversionHistCollection -> Collection(PX.Objects.TX.SVATConversionHist)
PX.SM.Branch.NotificationSetupCollection -> Collection(PX.Objects.CS.NotificationSetup)
PX.SM.Branch.SOOrderCollection -> Collection(PX.Objects.SO.SOOrder)
PX.SM.Branch.RQRequisitionLineCollection -> Collection(PX.Objects.RQ.RQRequisitionLine)
PX.SM.Branch.RQRequestLineCollection -> Collection(PX.Objects.RQ.RQRequestLine)
PX.SM.Branch.POLineCollection -> Collection(PX.Objects.PO.POLine)
PX.SM.Branch.POOrderCollection -> Collection(PX.Objects.PO.POOrder)
PX.SM.Branch.PMProformaLineCollection -> Collection(PX.Objects.PM.PMProformaLine)
PX.SM.Branch.PMTaskCollection -> Collection(PX.Objects.PM.PMTask)
PX.SM.Branch.FixedAssetCollection -> Collection(PX.Objects.FA.FixedAsset)
PX.SM.Branch.FATranCollection -> Collection(PX.Objects.FA.FATran)
PX.SM.Branch.ContractCollection -> Collection(PX.Objects.CT.Contract)
PX.SM.Branch.INTranCollection -> Collection(PX.Objects.IN.INTran)
PX.SM.Branch.INRegisterCollection -> Collection(PX.Objects.IN.INRegister)
PX.SM.Branch.GLTranCollection -> Collection(PX.Objects.GL.GLTran)
PX.SM.Branch.INSiteCollection -> Collection(PX.Objects.IN.INSite)
PX.SM.Branch.BatchCollection -> Collection(PX.Objects.GL.Batch)
PX.SM.Branch.OrganizationCollection -> Collection(PX.Objects.GL.DAC.Organization)
PX.SM.Branch.CABankTaxTranCollection -> Collection(PX.Objects.CA.CABankTaxTran)
PX.SM.Branch.CABankTaxTranMatchCollection -> Collection(PX.Objects.CA.CABankTaxTranMatch)
PX.SM.Branch.APAdjustCollection -> Collection(PX.Objects.AP.APAdjust)
PX.SM.Branch.CATranCollection -> Collection(PX.Objects.CA.CATran)
PX.SM.Branch.ARAdjustCollection -> Collection(PX.Objects.AR.ARAdjust)
PX.SM.Branch.APRegisterCollection -> Collection(PX.Objects.AP.APRegister)
PX.SM.Branch.PMTimeActivityCollection -> Collection(PX.Objects.CR.PMTimeActivity)
PX.SM.Branch.EPExpenseClaimCollection -> Collection(PX.Objects.EP.EPExpenseClaim)
PX.SM.Branch.RQRequisitionCollection -> Collection(PX.Objects.RQ.RQRequisition)
PX.SM.Branch.DRScheduleDetailCollection -> Collection(PX.Objects.DR.DRScheduleDetail)
PX.SM.Branch.GLAllocationCollection -> Collection(PX.Objects.GL.GLAllocation)
PX.SM.Branch.GLTrialBalanceImportDetailsCollection -> Collection(PX.Objects.GL.GLTrialBalanceImportDetails)
PX.SM.Branch.ARSalesPerTranCollection -> Collection(PX.Objects.AR.ARSalesPerTran)
PX.SM.Branch.EPExpenseClaimDetailsCollection -> Collection(PX.Objects.EP.EPExpenseClaimDetails)
PX.SM.Branch.AMProdItemCollection -> Collection(PX.Objects.AM.AMProdItem)
PX.SM.Branch.AMMTranCollection -> Collection(PX.Objects.AM.AMMTran)
PX.SM.Branch.SOLineCollection -> Collection(PX.Objects.SO.SOLine)
PX.SM.Branch.FSScheduleCollection -> Collection(PX.Objects.FS.FSSchedule)
PX.SM.Branch.FSAppointmentDetCollection -> Collection(PX.Objects.FS.FSAppointmentDet)
PX.SM.Branch.FSServiceOrderCollection -> Collection(PX.Objects.FS.FSServiceOrder)
PX.SM.Branch.FSSODetCollection -> Collection(PX.Objects.FS.FSSODet)
PX.SM.Branch.FSAppointmentCollection -> Collection(PX.Objects.FS.FSAppointment)
PX.SM.Branch.POEnabledFSSODetCollection -> Collection(PX.Objects.FS.POEnabledFSSODet)
PX.SM.Branch.FSEquipmentCollection -> Collection(PX.Objects.FS.FSEquipment)
PX.SM.Branch.EPEquipmentDetailCollection -> Collection(PX.Objects.EP.EPEquipmentDetail)
PX.SM.Branch.CABatchCollection -> Collection(PX.Objects.CA.CABatch)
PX.SM.Branch.POReceiptLineCollection -> Collection(PX.Objects.PO.POReceiptLine)
PX.SM.Branch.APTranCollection -> Collection(PX.Objects.AP.APTran)
PX.SM.Branch.GLBudgetLineCollection -> Collection(PX.Objects.GL.GLBudgetLine)
PX.SM.Branch.CashAccountCollection -> Collection(PX.Objects.CA.CashAccount)
PX.SM.Branch.LocationCollection -> Collection(PX.Objects.CR.Location)
PX.SM.Branch.PMCommitmentCollection -> Collection(PX.Objects.PM.PMCommitment)
PX.SM.Branch.ARTranCollection -> Collection(PX.Objects.AR.ARTran)
PX.SM.Branch.PMTranCollection -> Collection(PX.Objects.PM.PMTran)
PX.SM.Branch.PMRecurringItemCollection -> Collection(PX.Objects.PM.PMRecurringItem)
PX.SM.Branch.GLTranDocCollection -> Collection(PX.Objects.GL.GLTranDoc)
PX.SM.Branch.AMBatchCollection -> Collection(PX.Objects.AM.AMBatch)
PX.SM.Branch.SPPortalCollection -> Collection(PX.Objects.Portals.SPPortal)
PX.SM.Branch.MISC1099EFileProcessingInfoRawCollection -> Collection(PX.Objects.AP.MISC1099EFileProcessingInfoRaw)
PX.SM.Branch.AP1099HistoryCollection -> Collection(PX.Objects.AP.AP1099History)
PX.SM.Branch.CuryAPHistoryCollection -> Collection(PX.Objects.AP.CuryAPHistory)
PX.SM.Branch.CuryARHistoryCollection -> Collection(PX.Objects.AR.CuryARHistory)
PX.SM.Branch.ARHistoryCollection -> Collection(PX.Objects.AR.ARHistory)
PX.SM.Branch.ARTranPostCollection -> Collection(PX.Objects.AR.ARTranPost)
PX.SM.Branch.APHistoryCollection -> Collection(PX.Objects.AP.APHistory)
PX.SM.Branch.AMEstimateItemCollection -> Collection(PX.Objects.AM.AMEstimateItem)
PX.SM.Branch.TaxAdjustmentCollection -> Collection(PX.Objects.TX.TaxAdjustment)
PX.SM.Branch.TaxPluginMappingCollection -> Collection(PX.Objects.TX.TaxPluginMapping)
PX.SM.Branch.SOPickPackShipSetupCollection -> Collection(PX.Objects.SO.SOPickPackShipSetup)
PX.SM.Branch.RQRequestCollection -> Collection(PX.Objects.RQ.RQRequest)
PX.SM.Branch.POAccrualDetailCollection -> Collection(PX.Objects.PO.POAccrualDetail)
PX.SM.Branch.POLandedCostDetailCollection -> Collection(PX.Objects.PO.POLandedCostDetail)
PX.SM.Branch.POLandedCostDocCollection -> Collection(PX.Objects.PO.POLandedCostDoc)
PX.SM.Branch.POLandedCostReceiptLineCollection -> Collection(PX.Objects.PO.POLandedCostReceiptLine)
PX.SM.Branch.POReceiptCollection -> Collection(PX.Objects.PO.POReceipt)
PX.SM.Branch.POLandedCostDocSCollection -> Collection(PX.Objects.PO.POLandedCostDocS)
PX.SM.Branch.PMAllocationDetailCollection -> Collection(PX.Objects.PM.PMAllocationDetail)
PX.SM.Branch.PMBillingRuleCollection -> Collection(PX.Objects.PM.PMBillingRule)
PX.SM.Branch.PMProformaCollection -> Collection(PX.Objects.PM.PMProforma)
PX.SM.Branch.PMWipAdjustmentCollection -> Collection(PX.Objects.PM.PMWipAdjustment)
PX.SM.Branch.MNMaterialListCollection -> Collection(PX.Objects.MN.MNMaterialList)
PX.SM.Branch.MNMaterialListLineCollection -> Collection(PX.Objects.MN.MNMaterialListLine)
PX.SM.Branch.FAAccrualTranCollection -> Collection(PX.Objects.FA.FAAccrualTran)
PX.SM.Branch.FALocationHistoryCollection -> Collection(PX.Objects.FA.FALocationHistory)
PX.SM.Branch.FARegisterCollection -> Collection(PX.Objects.FA.FARegister)
PX.SM.Branch.DRScheduleTranCollection -> Collection(PX.Objects.DR.DRScheduleTran)
PX.SM.Branch.NotificationSourceCollection -> Collection(PX.Objects.CS.NotificationSource)
PX.SM.Branch.NumberingSequenceCollection -> Collection(PX.Objects.CS.NumberingSequence)
PX.SM.Branch.INScanSetupCollection -> Collection(PX.Objects.IN.INScanSetup)
PX.SM.Branch.INSetupCollection -> Collection(PX.Objects.IN.INSetup)
PX.SM.Branch.INSiteBuildingCollection -> Collection(PX.Objects.IN.INSiteBuilding)
PX.SM.Branch.INTurnoverCalcCollection -> Collection(PX.Objects.IN.Turnover.INTurnoverCalc)
PX.SM.Branch.INTurnoverCalcItemCollection -> Collection(PX.Objects.IN.Turnover.INTurnoverCalcItem)
PX.SM.Branch.TranslationHistoryCollection -> Collection(PX.Objects.CM.TranslationHistory)
PX.SM.Branch.TranslationHistoryDetailsCollection -> Collection(PX.Objects.CM.TranslationHistoryDetails)
PX.SM.Branch.TranslDefCollection -> Collection(PX.Objects.CM.TranslDef)
PX.SM.Branch.TranslDefDetCollection -> Collection(PX.Objects.CM.TranslDefDet)
PX.SM.Branch.GLAllocationDestinationCollection -> Collection(PX.Objects.GL.GLAllocationDestination)
PX.SM.Branch.GLAllocationSourceCollection -> Collection(PX.Objects.GL.GLAllocationSource)
PX.SM.Branch.GLBudgetCollection -> Collection(PX.Objects.GL.GLBudget)
PX.SM.Branch.GLBudgetLineDetailCollection -> Collection(PX.Objects.GL.GLBudgetLineDetail)
PX.SM.Branch.GLDocBatchCollection -> Collection(PX.Objects.GL.GLDocBatch)
PX.SM.Branch.CAAdjCollection -> Collection(PX.Objects.CA.CAAdj)
PX.SM.Branch.CABankTranAdjustmentCollection -> Collection(PX.Objects.CA.CABankTranAdjustment)
PX.SM.Branch.CABankTranDetailCollection -> Collection(PX.Objects.CA.CABankTranDetail)
PX.SM.Branch.CACorpCardCollection -> Collection(PX.Objects.CA.CACorpCard)
PX.SM.Branch.CADepositCollection -> Collection(PX.Objects.CA.CADeposit)
PX.SM.Branch.CAEntryTypeCollection -> Collection(PX.Objects.CA.CAEntryType)
PX.SM.Branch.CAExpenseCollection -> Collection(PX.Objects.CA.CAExpense)
PX.SM.Branch.CashAccountETDetailCollection -> Collection(PX.Objects.CA.CashAccountETDetail)
PX.SM.Branch.CASplitCollection -> Collection(PX.Objects.CA.CASplit)
PX.SM.Branch.CATransferCollection -> Collection(PX.Objects.CA.CATransfer)
PX.SM.Branch.CCProcessingCenterPmntMethodBranchCollection -> Collection(PX.Objects.CA.CCProcessingCenterPmntMethodBranch)
PX.SM.Branch.BuildingCollection -> Collection(PX.Objects.CR.Building)
PX.SM.Branch.CROpportunityRevisionCollection -> Collection(PX.Objects.CR.Standalone.CROpportunityRevision)
PX.SM.Branch.ARPaymentChargeTranCollection -> Collection(PX.Objects.AR.ARPaymentChargeTran)
PX.SM.Branch.ARSetupCollection -> Collection(PX.Objects.AR.ARSetup)
PX.SM.Branch.ARStatementCollection -> Collection(PX.Objects.AR.ARStatement)
PX.SM.Branch.DiscountBranchCollection -> Collection(PX.Objects.AR.DiscountBranch)
PX.SM.Branch.BCBindingCollection -> Collection(PX.Commerce.Core.BCBinding)
PX.SM.Branch.AMClockItemCollection -> Collection(PX.Objects.AM.AMClockItem)
PX.SM.Branch.AMClockTranCollection -> Collection(PX.Objects.AM.AMClockTran)
PX.SM.Branch.AMForecastCollection -> Collection(PX.Objects.AM.AMForecast)
PX.SM.Branch.AMForecastStagingCollection -> Collection(PX.Objects.AM.AMForecastStaging)
PX.SM.Branch.AMMPSCollection -> Collection(PX.Objects.AM.AMMPS)
PX.SM.Branch.AMRPDetailCollection -> Collection(PX.Objects.AM.AMRPDetail)
PX.SM.Branch.AMVendorShipmentCollection -> Collection(PX.Objects.AM.AMVendorShipment)
PX.SM.Branch.FSBranchLocationCollection -> Collection(PX.Objects.FS.FSBranchLocation)
PX.SM.Branch.FSMasterContractCollection -> Collection(PX.Objects.FS.FSMasterContract)
PX.SM.Branch.FSRouteCollection -> Collection(PX.Objects.FS.FSRoute)
PX.SM.Branch.FSRouteDocumentCollection -> Collection(PX.Objects.FS.FSRouteDocument)
PX.SM.Branch.FSServiceContractCollection -> Collection(PX.Objects.FS.FSServiceContract)
PX.SM.Branch.FSWrkProcessCollection -> Collection(PX.Objects.FS.FSWrkProcess)
PX.SM.Branch.T4AMasterTableCollection -> Collection(PX.Objects.Localizations.CA.T4AMasterTable)
PX.SM.Branch.PRLocationCollection -> Collection(PX.Objects.PR.PRLocation)
PX.SM.Branch.PRPaymentBatchExportDetailsCollection -> Collection(PX.Objects.PR.PRPaymentBatchExportDetails)
PX.SM.Branch.PRRecordOfEmploymentCollection -> Collection(PX.Objects.PR.PRRecordOfEmployment)
PX.SM.Branch.SVInvoiceCollection -> Collection(PX.Objects.SV.SVInvoice)
PX.SM.Branch.SVOrderCollection -> Collection(PX.Objects.SV.SVOrder)
PX.SM.Branch.SVOrderActualCollection -> Collection(PX.Objects.SV.SVOrderActual)
PX.SM.Branch.SVOrderDetailCollection -> Collection(PX.Objects.SV.SVOrderDetail)
PX.SM.Branch.SVServiceLocationCollection -> Collection(PX.Objects.SV.SVServiceLocation)
PX.SM.Branch.SVStagingWarehouseCollection -> Collection(PX.Objects.SV.SVStagingWarehouse)
PX.SM.Branch.INKitRegisterCollection -> Collection(PX.Objects.IN.INKitRegister)
PX.SM.Branch.AMRPExceptionsCollection -> Collection(PX.Objects.AM.AMRPExceptions)
PX.SM.Branch.SchedulerServiceOrderCollection -> Collection(PX.Objects.FS.SchedulerServiceOrder)
PX.SM.Branch.POLineRSCollection -> Collection(PX.Objects.PO.POLineRS)
PX.SM.Branch.POLineSCollection -> Collection(PX.Objects.PO.POLineS)
PX.SM.Branch.POReceiptLineSCollection -> Collection(PX.Objects.PO.POReceiptLineS)
PX.SM.Branch.AMRPDetailFPCollection -> Collection(PX.Objects.AM.AMRPDetailFP)
PX.SM.Branch.AMRPDetailPlanCollection -> Collection(PX.Objects.AM.AMRPDetailPlan)
PX.SM.Branch.ARDunningLetterCollection -> Collection(PX.Objects.AR.ARDunningLetter)
PX.SM.Branch.ARTranPostGLCollection -> Collection(PX.Objects.AR.ARTranPostGL)
PX.SM.Branch.RMDataSourceCollection -> Collection(PX.CS.RMDataSource)
PX.SM.Branch.TaxHistoryCollection -> Collection(PX.Objects.TX.TaxHistory)
PX.SM.Branch.TaxHistorySumCollection -> Collection(PX.Objects.TX.TaxHistorySum)
PX.SM.Branch.PMPOHistoryByDateCollection -> Collection(PX.Objects.PM.PMPOHistoryByDate)
PX.SM.Branch.FAProjectedGLTranCollection -> Collection(PX.Objects.FA.FAProjectedGLTran)
PX.SM.Branch.DRExpenseBalanceByPeriodCollection -> Collection(PX.Objects.DR.DRExpenseBalanceByPeriod)
PX.SM.Branch.DRExpenseProjectionCollection -> Collection(PX.Objects.DR.DRExpenseProjection)
PX.SM.Branch.DRRevenueBalanceByPeriodCollection -> Collection(PX.Objects.DR.DRRevenueBalanceByPeriod)
PX.SM.Branch.DRRevenueProjectionCollection -> Collection(PX.Objects.DR.DRRevenueProjection)
PX.SM.Branch.ArmGLHistoryByPeriodCollection -> Collection(PX.Objects.CS.ArmGLHistoryByPeriod)
PX.SM.Branch.INOverheadTranCollection -> Collection(PX.Objects.IN.INOverheadTran)
PX.SM.Branch.CCProcessingCenterBranchCollection -> Collection(PX.Objects.CC.CCProcessingCenterBranch)
PX.SM.Branch.BranchAcctMapFromCollection -> Collection(PX.Objects.GL.BranchAcctMapFrom)
PX.SM.Branch.BranchAcctMapToCollection -> Collection(PX.Objects.GL.BranchAcctMapTo)
PX.SM.Branch.GLAllocationAccountHistoryCollection -> Collection(PX.Objects.GL.GLAllocationAccountHistory)
PX.SM.Branch.GLConsolSetupCollection -> Collection(PX.Objects.GL.GLConsolSetup)
PX.SM.Branch.GLHistorySummaryCollection -> Collection(PX.Objects.GL.GLHistorySummary)
PX.SM.Branch.GLHistoryByPeriodCollection -> Collection(PX.Objects.GL.GLHistoryByPeriod)
PX.SM.Branch.GLHistoryByCurrentPeriodCollection -> Collection(PX.Objects.GL.GLHistoryByCurrentPeriod)
PX.SM.Branch.GLHistoryByPeriodCurrentCollection -> Collection(PX.Objects.GL.GLHistoryByPeriodCurrent)
PX.SM.Branch.GLHistoryByPeriodMasterCurrentCollection -> Collection(PX.Objects.GL.GLHistoryByPeriodMasterCurrent)
PX.SM.Branch.GLHistoryLastRevaluationCollection -> Collection(PX.Objects.GL.GLHistoryLastRevaluation)
PX.SM.Branch.PaymentMethodAccountCollection -> Collection(PX.Objects.CA.PaymentMethodAccount)
PX.SM.Branch.ARSPCommnHistoryCollection -> Collection(PX.Objects.AR.ARSPCommnHistory)
PX.SM.Branch.ARStatementDetailCollection -> Collection(PX.Objects.AR.ARStatementDetail)
PX.SM.Branch.ARStatementDetailInfoCollection -> Collection(PX.Objects.AR.ARStatementDetailInfo)
PX.SM.Branch.APHistoryByPeriodCollection -> Collection(PX.Objects.AP.APHistoryByPeriod)
PX.SM.Branch.BaseAPHistoryByPeriodCollection -> Collection(PX.Objects.AP.BaseAPHistoryByPeriod)
PX.SM.Branch.APTranPostCollection -> Collection(PX.Objects.AP.APTranPost)
PX.SM.Branch.APTranPostGLCollection -> Collection(PX.Objects.AP.APTranPostGL)
PX.SM.Branch.AMRPPlanCollection -> Collection(PX.Objects.AM.AMRPPlan)
PX.SM.Branch.ContractPostBatchDetailCollection -> Collection(PX.Objects.FS.ContractPostBatchDetail)
PX.SM.Branch.ContractPeriodToPostCollection -> Collection(PX.Objects.FS.ContractPeriodToPost)
PX.SM.Branch.ARBalancesCollection -> Collection(PX.Objects.AR.ARBalances)
PX.SM.Branch.DRExpenseBalanceCollection -> Collection(PX.Objects.DR.DRExpenseBalance)
PX.SM.Branch.DRExpenseBalance2Collection -> Collection(PX.Objects.DR.DRExpenseBalance2)
PX.SM.Branch.DRRevenueBalanceCollection -> Collection(PX.Objects.DR.DRRevenueBalance)
PX.SM.Branch.DRRevenueBalance2Collection -> Collection(PX.Objects.DR.DRRevenueBalance2)
PX.SM.Branch.AUScheduleCollection -> Collection(PX.SM.AUSchedule)
PX.SM.Branch.UserPreferencesCollection -> Collection(PX.SM.UserPreferences)
PX.SM.Branch.FSTimeSlotCollection -> Collection(PX.Objects.FS.FSTimeSlot)

# PX.SM.Certificate (EntityType)

Label: "Certificate"
Key: Name
Entity sets: PX_SM_Certificate, Certificate
Non-filterable, non-selectable: NoteText

PX.SM.Certificate.Name : Edm.String [key] "Name"
PX.SM.Certificate.Password : Edm.String "Password"
PX.SM.Certificate.NoteID : Edm.Guid
PX.SM.Certificate.NoteText : Edm.String "Note Text"
PX.SM.Certificate.PMLinkedFileCollection -> Collection(PX.Objects.PM.ProjectFiles.FileEntryForms.PMLinkedFile)
PX.SM.Certificate.UploadFileWithIDSelectorCollection -> Collection(PX.SM.UploadFileWithIDSelector)
PX.SM.Certificate.UploadFileCollection -> Collection(PX.SM.UploadFile)
PX.SM.Certificate.UserPreferencesCollection -> Collection(PX.SM.UserPreferences)
PX.SM.Certificate.PreferencesSecurityCollection -> Collection(PX.SM.PreferencesSecurity)
PX.SM.Certificate.CABankFeedCollection -> Collection(PX.Objects.CA.CABankFeed)

# PX.SM.CetrificateFile (EntityType)

Label: "Certificate"
BaseType: PX.SM.Certificate
Key: Name (inherited from PX.SM.Certificate)
Entity sets: PX_SM_CetrificateFile

PX.SM.CetrificateFile.FileID : Edm.Guid

# PX.SM.CompanyByTableSize (EntityType)

Label: "Table Size"
BaseType: PX.SM.TableSize
Key: Company, TableName (inherited from PX.SM.TableSize)
Entity sets: PX_SM_CompanyByTableSize
Filterable: false (fields declared in this DAC cannot be used in $filter or $select; inherited ones can)

PX.SM.CompanyByTableSize.Type : Edm.String "Type"
PX.SM.CompanyByTableSize.Name : Edm.String "Name"
PX.SM.CompanyByTableSize.Size : Edm.Decimal "Size in DB"

# PX.SM.CustMobileSiteMap (EntityType)

BaseType: PX.SM.CustObject
Key: ObjectID (inherited from PX.SM.CustObject)
Entity sets: PX_SM_CustMobileSiteMap
Filterable: false (fields declared in this DAC cannot be used in $filter or $select; inherited ones can)

PX.SM.CustMobileSiteMap.Operation : Edm.String "Operation"
PX.SM.CustMobileSiteMap.Title : Edm.String "Title"

# PX.SM.CustObject (EntityType)

Key: ObjectID
Entity sets: PX_SM_CustObject
Non-filterable, non-selectable: ObjectName, NoteText, IsThirdParty, AccessRightsMergeRule, ScreenId, IsReadOnly

PX.SM.CustObject.ProjectID : Edm.Guid
PX.SM.CustObject.ObjectID : Edm.Guid [key] "ObjectID"
PX.SM.CustObject.Name : Edm.String "Object Name"
PX.SM.CustObject.ObjectName : Edm.String "Object Name"
PX.SM.CustObject.Type : Edm.String "Type"
PX.SM.CustObject.Label : Edm.String "Label"
PX.SM.CustObject.Content : Edm.String "Content"
PX.SM.CustObject.Description : Edm.String "Description"
PX.SM.CustObject.IsDisabled : Edm.Boolean [required] "Excluded"
PX.SM.CustObject.CreatedByID : Edm.Guid "Created By"
PX.SM.CustObject.CreatedDateTime : Edm.DateTimeOffset "Creation Date"
PX.SM.CustObject.LastModifiedByID : Edm.Guid "Last Modified By"
PX.SM.CustObject.LastModifiedDateTime : Edm.DateTimeOffset "Last Modified On"
PX.SM.CustObject.NoteID : Edm.Guid
PX.SM.CustObject.NoteText : Edm.String "Note Text"
PX.SM.CustObject.IsThirdParty : Edm.Boolean "Third Party Assembly"
PX.SM.CustObject.AccessRightsMergeRule : Edm.String "Merge Rule"
PX.SM.CustObject.ScreenId : Edm.String "Screen ID"
PX.SM.CustObject.IsReadOnly : Edm.Boolean "Read Only"
PX.SM.CustObject.UsersByCreatedByID -> PX.SM.Users (CreatedByID=PKID)
PX.SM.CustObject.UsersByLastModifiedByID -> PX.SM.Users (LastModifiedByID=PKID)

# PX.SM.CustObjectMaint (EntityType)

BaseType: PX.SM.CustObject
Key: ObjectID (inherited from PX.SM.CustObject)
Entity sets: PX_SM_CustObjectMaint
Non-filterable, non-selectable: ShortName, UserFriendlyType, CustType, Priority

PX.SM.CustObjectMaint.ShortName : Edm.String "Object Name"
PX.SM.CustObjectMaint.UserFriendlyType : Edm.String "Type"
PX.SM.CustObjectMaint.ProjectRevisionID : Edm.Guid "ProjectRevisionID"
PX.SM.CustObjectMaint.LastRevisionID : Edm.Guid "LastRevisionID"
PX.SM.CustObjectMaint.ParentID : Edm.Guid "ParentID"
PX.SM.CustObjectMaint.tstamp : Edm.Binary
PX.SM.CustObjectMaint.CustType : PX.SM.CustObjectTypes [required] "CustType"
PX.SM.CustObjectMaint.Priority : Edm.Int32 "Priority"

# PX.SM.CustProject (EntityType)

Label: "Edit Project Items"
Key: Name
Entity sets: PX_SM_CustProject, EditProjectItems, CustProject
Non-filterable, non-selectable: Initials, NoteText, ScreenNames, IsPublished, UpdateSnapshot

PX.SM.CustProject.ProjID : Edm.Guid "ProjID"
PX.SM.CustProject.Name : Edm.String [key] "Project Name"
PX.SM.CustProject.IsWorking : Edm.Boolean [required] "Selected"
PX.SM.CustProject.Description : Edm.String "Description"
PX.SM.CustProject.CreatedByID : Edm.Guid "Owner"
PX.SM.CustProject.CertificationStatus : Edm.String "Certification Status"
PX.SM.CustProject.CertificationWarning : Edm.String
PX.SM.CustProject.DevelopedBy : Edm.String
PX.SM.CustProject.Initials : Edm.String "Initials"
PX.SM.CustProject.CertificationStatusDateTime : Edm.DateTimeOffset "Certification Status Date"
PX.SM.CustProject.CreatedDateTime : Edm.DateTimeOffset "Creation Date"
PX.SM.CustProject.LastModifiedByID : Edm.Guid "Last Modified By"
PX.SM.CustProject.LastModifiedDateTime : Edm.DateTimeOffset "Last Modified On"
PX.SM.CustProject.ParentID : Edm.Guid
PX.SM.CustProject.NoteID : Edm.Guid
PX.SM.CustProject.NoteText : Edm.String "Note Text"
PX.SM.CustProject.SnapshotID : Edm.Guid
PX.SM.CustProject.ScreenNames : Edm.String "Screen Names"
PX.SM.CustProject.IsPublished : Edm.Boolean "Published"
PX.SM.CustProject.Level : Edm.Int32 "Level"
PX.SM.CustProject.UpdateSnapshot : Edm.Boolean
PX.SM.CustProject.UsersByCreatedByID -> PX.SM.Users (CreatedByID=PKID)
PX.SM.CustProject.UsersByLastModifiedByID -> PX.SM.Users (LastModifiedByID=PKID)
PX.SM.CustProject.UPPackageTablesCollection -> Collection(PX.SM.UPPackageTables)

# PX.SM.CustScreen (EntityType)

BaseType: PX.SM.CustObject
Key: ObjectID (inherited from PX.SM.CustObject)
Entity sets: PX_SM_CustScreen
Filterable: false (fields declared in this DAC cannot be used in $filter or $select; inherited ones can)

PX.SM.CustScreen.Title : Edm.String "Title"
PX.SM.CustScreen.IsNew : Edm.Boolean "Is New"

# PX.SM.CustScreenConfiguration (EntityType)

BaseType: PX.SM.CustObject
Key: ObjectID (inherited from PX.SM.CustObject)
Entity sets: PX_SM_CustScreenConfiguration
Filterable: false (fields declared in this DAC cannot be used in $filter or $select; inherited ones can)

PX.SM.CustScreenConfiguration.Title : Edm.String "Screen Name"
PX.SM.CustScreenConfiguration.UserDefinedFields : Edm.String "User-Defined Fields"

# PX.SM.CustUserFieldsObject (EntityType)

BaseType: PX.SM.CustObject
Key: ObjectID (inherited from PX.SM.CustObject)
Entity sets: PX_SM_CustUserFieldsObject
Filterable: false (fields declared in this DAC cannot be used in $filter or $select; inherited ones can)

PX.SM.CustUserFieldsObject.AttributeID : Edm.String "Attribute ID"
PX.SM.CustUserFieldsObject.TypeValues : Collection(Edm.String) "Entity Type"

# PX.SM.DashboardInProject (EntityType)

Label: "Dashboard"
BaseType: PX.Dashboards.DAC.Dashboard
Key: Name (inherited from PX.Dashboards.DAC.Dashboard)
Entity sets: PX_SM_DashboardInProject

PX.SM.DashboardInProject.CompanyID : Edm.Int32 "CompanyId"

# PX.SM.DashboardV2InProject (EntityType)

Label: "Dashboard"
BaseType: PX.Dashboards.DAC.DashboardV2
Key: Name (inherited from PX.Dashboards.DAC.DashboardV2)
Entity sets: PX_SM_DashboardV2InProject

PX.SM.DashboardV2InProject.CompanyID : Edm.Int32 "CompanyId"

# PX.SM.DateInfo (EntityType)

Label: "Date Info"
Key: Date
Entity sets: PX_SM_DateInfo, DateInfo
Non-filterable, non-selectable: MonthName, MonthInCalendar, QuarterInCalendar, DayInWeek, DayOfWeekName, WeekEnding

PX.SM.DateInfo.Date : Edm.DateTimeOffset [key] "Date"
PX.SM.DateInfo.Year : Edm.Int32 "Year"
PX.SM.DateInfo.Quarter : Edm.Int32 "Quarter Of Year"
PX.SM.DateInfo.Month : Edm.Int32 "Month Of Year"
PX.SM.DateInfo.Day : Edm.Int32 "Day Of Month"
PX.SM.DateInfo.DateInt : Edm.Int32 "Date (Integer)"
PX.SM.DateInfo.MonthName : Edm.String "Month Name"
PX.SM.DateInfo.MonthInCalendar : Edm.String "Month In Calendar"
PX.SM.DateInfo.QuarterInCalendar : Edm.String "Quarter"
PX.SM.DateInfo.DayInWeek : Edm.Int32 "Day In Week"
PX.SM.DateInfo.DayOfWeekName : Edm.String "Day Of Week (Name)"
PX.SM.DateInfo.WeekEnding : Edm.DateTimeOffset "Week Ending"

# PX.SM.EMailAccount (EntityType)

Label: "Email Account"
Key: EmailAccountID
Entity sets: PX_SM_EMailAccount, EmailAccount
Non-filterable, non-selectable: IsOfPluginType, PasswordIsDecrypted, OutcomingAuthenticationRequest, OutcomingAuthenticationDifferent, SupportReceiving, SupportSending, Included, InboxCount, OutboxCount, NoteText, CanUpdatePassword, CanSignIn, CanSignOut, Secured

PX.SM.EMailAccount.EmailAccountID : Edm.Int32 [key] "Email Account ID"
PX.SM.EMailAccount.Address : Edm.String "Email Address"
PX.SM.EMailAccount.Description : Edm.String "Account Name"
PX.SM.EMailAccount.DisplayEmailAddress : Edm.String "Account Name"
PX.SM.EMailAccount.IsActive : Edm.Boolean [required] "Active"
PX.SM.EMailAccount.EmailAccountType : Edm.String "Email Account Type"
PX.SM.EMailAccount.UserID : Edm.Guid "Personal Account For"
PX.SM.EMailAccount.ReplyAddress : Edm.String "Reply Address"
PX.SM.EMailAccount.PluginTypeName : Edm.String "Email Service Plug-In"
PX.SM.EMailAccount.IsOfPluginType : Edm.Boolean "IsOfPluginType"
PX.SM.EMailAccount.SenderDisplayNameSource : Edm.String "Name Source"
PX.SM.EMailAccount.AccountDisplayName : Edm.String "Sender Name"
PX.SM.EMailAccount.AuthenticationType : Edm.Int32
PX.SM.EMailAccount.AuthenticationMethod : Edm.String "Authentication Method"
PX.SM.EMailAccount.OAuthApplicationID : Edm.Int32 "External Application"
PX.SM.EMailAccount.OAuthScopes : Edm.String "OAuth2 Scopes"
PX.SM.EMailAccount.OAuthParameters : Edm.String "OAuth2 Parameters"
PX.SM.EMailAccount.AzureTenantID : Edm.String "Azure Tenant ID"
PX.SM.EMailAccount.LoginName : Edm.String "Incoming Mail Username"
PX.SM.EMailAccount.Password : Edm.String "Incoming Mail Password"
PX.SM.EMailAccount.PasswordIsDecrypted : Edm.Boolean
PX.SM.EMailAccount.OutcomingHostName : Edm.String "Outgoing Mail Server"
PX.SM.EMailAccount.OutcomingAuthenticationRequest : Edm.Boolean "My Outgoing Server Requires Authentication"
PX.SM.EMailAccount.OutcomingAuthenticationDifferent : Edm.Boolean "Log on Using"
PX.SM.EMailAccount.OutgoingConnectionEncryption : Edm.Int32 "Outgoing Connection Encryption"
PX.SM.EMailAccount.OutcomingLoginName : Edm.String "Outgoing Mail Username"
PX.SM.EMailAccount.OutcomingPassword : Edm.String "Outgoing Mail Password"
PX.SM.EMailAccount.OutcomingPort : Edm.Int32 "Outgoing Mail Port"
PX.SM.EMailAccount.OutcomingMailSender : Edm.Int32 "Outcoming Mail Sender"
PX.SM.EMailAccount.IncomingHostProtocol : Edm.Int32 "Protocol"
PX.SM.EMailAccount.IncomingProcessing : Edm.Boolean "Incoming Mail Processing"
PX.SM.EMailAccount.AddIncomingProcessingTags : Edm.Boolean "Add Tags for the Incoming Processing"
PX.SM.EMailAccount.IncomingHostName : Edm.String "Incoming Mail Server"
PX.SM.EMailAccount.IncomingConnectionEncryption : Edm.Int32 "Incoming Connection Encryption"
PX.SM.EMailAccount.IncomingPort : Edm.Int32 "Incoming Mail Port"
PX.SM.EMailAccount.SupportReceiving : Edm.Boolean
PX.SM.EMailAccount.SupportSending : Edm.Boolean
PX.SM.EMailAccount.SendGroupMails : Edm.Int32 [required] "Group Mails"
PX.SM.EMailAccount.AutoReceiveDelay : Edm.Int32 "Receive Mail Every"
PX.SM.EMailAccount.ImapRootFolder : Edm.String "Root Folder"
PX.SM.EMailAccount.ValidateFrom : Edm.Boolean "Server Validates From Address"
PX.SM.EMailAccount.Timeout : Edm.Int32 [required] "Connection Timeout"
PX.SM.EMailAccount.FetchingBehavior : Edm.Int32 "After Receiving"
PX.SM.EMailAccount.IncomingDelSuccess : Edm.Boolean "Remove Read Messages from Server"
PX.SM.EMailAccount.IncomingAttachmentType : Edm.String "Allowed Attachment Type"
PX.SM.EMailAccount.DeleteUnProcessed : Edm.Boolean "Delete Emails"
PX.SM.EMailAccount.ProcessUnassigned : Edm.Boolean "Reply to Unassigned Emails"
PX.SM.EMailAccount.ResponseNotificationID : Edm.Int32 "Reply Template"
PX.SM.EMailAccount.ConfirmReceipt : Edm.Boolean "Confirm Receipt"
PX.SM.EMailAccount.ConfirmReceiptNotificationID : Edm.Int32 "Confirmation Template"
PX.SM.EMailAccount.ProcessScenarioID : Edm.Guid "Scenario ID"
PX.SM.EMailAccount.ForbidRouting : Edm.Boolean "Forbid Routing"
PX.SM.EMailAccount.Included : Edm.Boolean "Included"
PX.SM.EMailAccount.InboxCount : Edm.Int32 "Inbox"
PX.SM.EMailAccount.OutboxCount : Edm.Int32 "Outbox"
PX.SM.EMailAccount.CreateCase : Edm.Boolean "Create New Case"
PX.SM.EMailAccount.CreateCaseClassID : Edm.String "New Case Class"
PX.SM.EMailAccount.RouteEmployeeEmails : Edm.Boolean "Route Employee Emails"
PX.SM.EMailAccount.CreateActivity : Edm.Boolean "Associate with Contact"
PX.SM.EMailAccount.CreateLead : Edm.Boolean "Create New Lead"
PX.SM.EMailAccount.CreateLeadClassID : Edm.String "New Lead Class"
PX.SM.EMailAccount.AddUpInformation : Edm.Boolean "Add Brief Information About References"
PX.SM.EMailAccount.TypeDelete : Edm.Int32
PX.SM.EMailAccount.DeletedDatabaseRecord : Edm.Boolean [required]
PX.SM.EMailAccount.DefaultWorkgroupID : Edm.Int32 "Default Email Workgroup"
PX.SM.EMailAccount.DefaultOwnerID : Edm.Int32 "Default Email Owner"
PX.SM.EMailAccount.DefaultEmailAssignmentMapID : Edm.Int32 "Email Assignment Map"
PX.SM.EMailAccount.EnableImapEnvelope : Edm.Boolean [required] "Enable IMAP Envelope"
PX.SM.EMailAccount.NoteID : Edm.Guid
PX.SM.EMailAccount.NoteText : Edm.String "Note Text"
PX.SM.EMailAccount.CreatedByID : Edm.Guid "Created By"
PX.SM.EMailAccount.CreatedByScreenID : Edm.String
PX.SM.EMailAccount.CreatedDateTime : Edm.DateTimeOffset
PX.SM.EMailAccount.LastModifiedByID : Edm.Guid "Last Modified By"
PX.SM.EMailAccount.LastModifiedByScreenID : Edm.String
PX.SM.EMailAccount.LastModifiedDateTime : Edm.DateTimeOffset
PX.SM.EMailAccount.tstamp : Edm.Binary
PX.SM.EMailAccount.CanUpdatePassword : Edm.Boolean "Can Update Password"
PX.SM.EMailAccount.CanSignIn : Edm.Boolean "Can Sign In"
PX.SM.EMailAccount.CanSignOut : Edm.Boolean "Can Sign Out"
PX.SM.EMailAccount.Secured : Edm.Boolean "Secured"
PX.SM.EMailAccount.VendorByDefaultOwnerID -> PX.Objects.AP.Vendor (DefaultOwnerID=DefContactID)
PX.SM.EMailAccount.ContactByDefaultOwnerID -> PX.Objects.CR.Contact (DefaultOwnerID=ContactID)
PX.SM.EMailAccount.CRLeadClassByCreateLeadClassID -> PX.Objects.CR.CRLeadClass (CreateLeadClassID=ClassID)
PX.SM.EMailAccount.OAuthApplicationByOAuthApplicationID -> PX.OAuthClient.DAC.OAuthApplication (OAuthApplicationID=ApplicationID)
PX.SM.EMailAccount.UsersByDefaultOwnerID -> PX.SM.Users (DefaultOwnerID=PKID)
PX.SM.EMailAccount.UsersByUserID -> PX.SM.Users (UserID=PKID)
PX.SM.EMailAccount.UsersByCreatedByID -> PX.SM.Users (CreatedByID=PKID)
PX.SM.EMailAccount.UsersByLastModifiedByID -> PX.SM.Users (LastModifiedByID=PKID)
PX.SM.EMailAccount.NotificationByResponseNotificationID -> PX.SM.Notification (ResponseNotificationID=NotificationID)
PX.SM.EMailAccount.NotificationByConfirmReceiptNotificationID -> PX.SM.Notification (ConfirmReceiptNotificationID=NotificationID)
PX.SM.EMailAccount.EPCompanyTreeByDefaultWorkgroupID -> PX.TM.EPCompanyTree (DefaultWorkgroupID=WorkGroupID)
PX.SM.EMailAccount.CRCaseClassByCreateCaseClassID -> PX.Objects.CR.CRCaseClass (CreateCaseClassID=CaseClassID)
PX.SM.EMailAccount.EPAssignmentMapByDefaultEmailAssignmentMapID -> PX.Objects.EP.EPAssignmentMap (DefaultEmailAssignmentMapID=AssignmentMapID)
PX.SM.EMailAccount.WikiNotificationTemplateCollection -> Collection(PX.SM.WikiNotificationTemplate)
PX.SM.EMailAccount.CRSMEmailCollection -> Collection(PX.Objects.CR.CRSMEmail)
PX.SM.EMailAccount.NotificationSetupCollection -> Collection(PX.Objects.CS.NotificationSetup)
PX.SM.EMailAccount.CRContactClassCollection -> Collection(PX.Objects.CR.CRContactClass)
PX.SM.EMailAccount.CRCustomerClassCollection -> Collection(PX.Objects.CR.CRCustomerClass)
PX.SM.EMailAccount.CRLeadClassCollection -> Collection(PX.Objects.CR.CRLeadClass)
PX.SM.EMailAccount.CROpportunityClassCollection -> Collection(PX.Objects.CR.CROpportunityClass)
PX.SM.EMailAccount.UserPreferencesCollection -> Collection(PX.SM.UserPreferences)
PX.SM.EMailAccount.NotificationCollection -> Collection(PX.SM.Notification)
PX.SM.EMailAccount.PreferencesEmailCollection -> Collection(PX.SM.PreferencesEmail)
PX.SM.EMailAccount.SMEmailCollection -> Collection(PX.Objects.CR.SMEmail)
PX.SM.EMailAccount.NotificationSourceCollection -> Collection(PX.Objects.CS.NotificationSource)
PX.SM.EMailAccount.CRCaseClassCollection -> Collection(PX.Objects.CR.CRCaseClass)
PX.SM.EMailAccount.CRMassMailCollection -> Collection(PX.Objects.CR.CRMassMail)
PX.SM.EMailAccount.EMailSyncAccountCollection -> Collection(PX.SM.EMailSyncAccount)
PX.SM.EMailAccount.EMailAccountStatisticsCollection -> Collection(PX.SM.EMailAccountStatistics)
PX.SM.EMailAccount.EmailLogCollection -> Collection(PX.Mail.Log.DAC.EmailLog)

# PX.SM.EMailAccountStatistics (EntityType)

Label: "Email Account Statistics"
Key: EmailAccountID
Entity sets: PX_SM_EMailAccountStatistics, EmailAccountStatistics

PX.SM.EMailAccountStatistics.EmailAccountID : Edm.Int32 [key] "Email Account ID"
PX.SM.EMailAccountStatistics.LastSendDateTime : Edm.DateTimeOffset "Last Email Sent On"
PX.SM.EMailAccountStatistics.LastReceiveDateTime : Edm.DateTimeOffset "Last Email Received On"
PX.SM.EMailAccountStatistics.EMailAccountByEmailAccountID -> PX.SM.EMailAccount (EmailAccountID=EmailAccountID)

# PX.SM.EMailSyncAccount (EntityType)

Key: EmployeeID, ServerID
Entity sets: PX_SM_EMailSyncAccount
Non-filterable, non-selectable: SyncAccount, TimeZone, IsVitrual, IsContactsReset, IsEmailsReset, IsTasksReset, IsEventsReset, NoteText

PX.SM.EMailSyncAccount.ServerID : Edm.Int32 [key] "Server ID"
PX.SM.EMailSyncAccount.EmployeeID : Edm.Int32 [key] "Employee ID"
PX.SM.EMailSyncAccount.Address : Edm.String "Email Address"
PX.SM.EMailSyncAccount.EmailAccountID : Edm.Int32 "Email Account"
PX.SM.EMailSyncAccount.SyncAccount : Edm.Boolean "Sync Account"
PX.SM.EMailSyncAccount.PolicyName : Edm.String "Policy Name"
PX.SM.EMailSyncAccount.EmployeeCD : Edm.String "Employee Name"
PX.SM.EMailSyncAccount.OwnerID : Edm.Int32 "Owner ID"
PX.SM.EMailSyncAccount.EmployeeStatus : Edm.String "Status"
PX.SM.EMailSyncAccount.TimeZone : Edm.String "Time Zone"
PX.SM.EMailSyncAccount.IsVitrual : Edm.Boolean
PX.SM.EMailSyncAccount.ToReinitialize : Edm.Boolean [required]
PX.SM.EMailSyncAccount.IsReset : Edm.Boolean [required]
PX.SM.EMailSyncAccount.HasErrors : Edm.Boolean [required]
PX.SM.EMailSyncAccount.ContactsExportDate : Edm.DateTimeOffset "Contacts Export Date"
PX.SM.EMailSyncAccount.ContactsExportFolder : Edm.String
PX.SM.EMailSyncAccount.ContactsImportDate : Edm.DateTimeOffset "Contacts Import Date"
PX.SM.EMailSyncAccount.ContactsImportFolder : Edm.String
PX.SM.EMailSyncAccount.IsContactsReset : Edm.Boolean
PX.SM.EMailSyncAccount.EmailsExportDate : Edm.DateTimeOffset "Emails Export Date"
PX.SM.EMailSyncAccount.EmailsExportFolder : Edm.String
PX.SM.EMailSyncAccount.EmailsImportDate : Edm.DateTimeOffset "Emails Import Date"
PX.SM.EMailSyncAccount.EmailsImportFolder : Edm.String
PX.SM.EMailSyncAccount.IsEmailsReset : Edm.Boolean
PX.SM.EMailSyncAccount.TasksExportDate : Edm.DateTimeOffset "Tasks Export Date"
PX.SM.EMailSyncAccount.TasksExportFolder : Edm.String
PX.SM.EMailSyncAccount.TasksImportDate : Edm.DateTimeOffset "Tasks Import Date"
PX.SM.EMailSyncAccount.TasksImportFolder : Edm.String
PX.SM.EMailSyncAccount.IsTasksReset : Edm.Boolean
PX.SM.EMailSyncAccount.EventsExportDate : Edm.DateTimeOffset "Events Export Date"
PX.SM.EMailSyncAccount.EventsExportFolder : Edm.String
PX.SM.EMailSyncAccount.EventsImportDate : Edm.DateTimeOffset "Events Import Date"
PX.SM.EMailSyncAccount.EventsImportFolder : Edm.String
PX.SM.EMailSyncAccount.IsEventsReset : Edm.Boolean
PX.SM.EMailSyncAccount.NoteID : Edm.Guid
PX.SM.EMailSyncAccount.NoteText : Edm.String "Note Text"
PX.SM.EMailSyncAccount.EMailAccountByEmailAccountID -> PX.SM.EMailAccount (EmailAccountID=EmailAccountID)
PX.SM.EMailSyncAccount.EMailSyncPolicyByPolicyName -> PX.SM.EMailSyncPolicy (PolicyName=PolicyName)
PX.SM.EMailSyncAccount.EMailSyncServerByServerID -> PX.SM.EMailSyncServer (ServerID=AccountID)

# PX.SM.EMailSyncAccountPreferences (EntityType)

Key: EmployeeID, PolicyName
Entity sets: PX_SM_EMailSyncAccountPreferences

PX.SM.EMailSyncAccountPreferences.PolicyName : Edm.String [key] "Policy Name"
PX.SM.EMailSyncAccountPreferences.EmployeeID : Edm.Int32 [key] "Employee ID"
PX.SM.EMailSyncAccountPreferences.Address : Edm.String "Email Address"
PX.SM.EMailSyncAccountPreferences.EmployeeCD : Edm.String "Employee Name"
PX.SM.EMailSyncAccountPreferences.VendorByEmployeeID -> PX.Objects.AP.Vendor (EmployeeID=BAccountID)
PX.SM.EMailSyncAccountPreferences.EMailSyncPolicyByPolicyName -> PX.SM.EMailSyncPolicy (PolicyName=PolicyName)

# PX.SM.EMailSyncLog (EntityType)

Key: EventID
Entity sets: PX_SM_EMailSyncLog

PX.SM.EMailSyncLog.EventID : Edm.Int32 [key]
PX.SM.EMailSyncLog.ServerID : Edm.Int32 "ServerID"
PX.SM.EMailSyncLog.Address : Edm.String "Email Address"
PX.SM.EMailSyncLog.Level : Edm.Byte "Level"
PX.SM.EMailSyncLog.Date : Edm.DateTimeOffset "Operation Date"
PX.SM.EMailSyncLog.Message : Edm.String "Message"
PX.SM.EMailSyncLog.Details : Edm.String "Details"
PX.SM.EMailSyncLog.EMailSyncServerByServerID -> PX.SM.EMailSyncServer (ServerID=AccountID)

# PX.SM.EMailSyncPolicy (EntityType)

Key: PolicyName
Entity sets: PX_SM_EMailSyncPolicy

PX.SM.EMailSyncPolicy.PolicyName : Edm.String [key] "Policy Name"
PX.SM.EMailSyncPolicy.Description : Edm.String "Description"
PX.SM.EMailSyncPolicy.Category : Edm.String "Category Name"
PX.SM.EMailSyncPolicy.LinkTemplate : Edm.String "External Link Template"
PX.SM.EMailSyncPolicy.Priority : Edm.String "Conflict Resolution Priority"
PX.SM.EMailSyncPolicy.Color : Edm.String "Category Color"
PX.SM.EMailSyncPolicy.SkipError : Edm.Boolean [required] "Continue on Error"
PX.SM.EMailSyncPolicy.ContactsSync : Edm.Boolean [required] "Synchronize Contacts"
PX.SM.EMailSyncPolicy.ContactsDirection : Edm.String "Direction"
PX.SM.EMailSyncPolicy.ContactsFolder : Edm.String "Folder Name"
PX.SM.EMailSyncPolicy.ContactsSeparated : Edm.Boolean "Use Separate Folder for Contacts"
PX.SM.EMailSyncPolicy.ContactsMerge : Edm.Boolean "Merge contacts by email"
PX.SM.EMailSyncPolicy.ContactsFilter : Edm.String "Filter"
PX.SM.EMailSyncPolicy.ContactsClass : Edm.String "Contact Class"
PX.SM.EMailSyncPolicy.ContactsSkipCategory : Edm.Boolean "Synchronize New Items without Category"
PX.SM.EMailSyncPolicy.ContactsGenerateLink : Edm.Boolean "Use Hyperlink to System Contact as Web Page Address"
PX.SM.EMailSyncPolicy.EmailsSync : Edm.Boolean [required] "Synchronize Emails"
PX.SM.EMailSyncPolicy.EmailsDirection : Edm.String "Direction"
PX.SM.EMailSyncPolicy.EmailsFolder : Edm.String "Folder Name"
PX.SM.EMailSyncPolicy.EmailsAttachments : Edm.Boolean "Synchronize Attachments"
PX.SM.EMailSyncPolicy.EmailsValidateContact : Edm.Boolean "Create Contact if Not Found"
PX.SM.EMailSyncPolicy.TasksSync : Edm.Boolean [required] "Synchronize Tasks"
PX.SM.EMailSyncPolicy.TasksFolder : Edm.String "Folder Name"
PX.SM.EMailSyncPolicy.TasksSeparated : Edm.Boolean "Use Separate Folder for Tasks"
PX.SM.EMailSyncPolicy.TasksDirection : Edm.String "Direction"
PX.SM.EMailSyncPolicy.TasksSkipCategory : Edm.Boolean "Synchronize New Items without Category"
PX.SM.EMailSyncPolicy.EventsSync : Edm.Boolean [required] "Synchronize Events"
PX.SM.EMailSyncPolicy.EventsFolder : Edm.String "Folder Name"
PX.SM.EMailSyncPolicy.EventsSeparated : Edm.Boolean "Use Separate Folder for Events"
PX.SM.EMailSyncPolicy.EventsDirection : Edm.String "Direction"
PX.SM.EMailSyncPolicy.EventsSkipCategory : Edm.Boolean "Synchronize New Items without Category"
PX.SM.EMailSyncPolicy.CreatedByID : Edm.Guid "Created By"
PX.SM.EMailSyncPolicy.CreatedByScreenID : Edm.String
PX.SM.EMailSyncPolicy.CreatedDateTime : Edm.DateTimeOffset
PX.SM.EMailSyncPolicy.LastModifiedByID : Edm.Guid "Last Modified By"
PX.SM.EMailSyncPolicy.LastModifiedByScreenID : Edm.String
PX.SM.EMailSyncPolicy.LastModifiedDateTime : Edm.DateTimeOffset
PX.SM.EMailSyncPolicy.CRContactClassByContactsClass -> PX.Objects.CR.CRContactClass (ContactsClass=ClassID)
PX.SM.EMailSyncPolicy.UsersByCreatedByID -> PX.SM.Users (CreatedByID=PKID)
PX.SM.EMailSyncPolicy.UsersByLastModifiedByID -> PX.SM.Users (LastModifiedByID=PKID)
PX.SM.EMailSyncPolicy.EMailSyncAccountCollection -> Collection(PX.SM.EMailSyncAccount)
PX.SM.EMailSyncPolicy.EMailSyncAccountPreferencesCollection -> Collection(PX.SM.EMailSyncAccountPreferences)
PX.SM.EMailSyncPolicy.EMailSyncServerCollection -> Collection(PX.SM.EMailSyncServer)

# PX.SM.EMailSyncReference (EntityType)

Key: Address, NoteID, ServerID
Entity sets: PX_SM_EMailSyncReference

PX.SM.EMailSyncReference.ServerID : Edm.Int32 [key] "Server ID"
PX.SM.EMailSyncReference.Address : Edm.String [key] "Email Address"
PX.SM.EMailSyncReference.NoteID : Edm.Guid [key]
PX.SM.EMailSyncReference.Conversation : Edm.String
PX.SM.EMailSyncReference.Hash : Edm.String
PX.SM.EMailSyncReference.IsSynchronized : Edm.Boolean
PX.SM.EMailSyncReference.MigratedGraphStatus : Edm.String "Migrated Status"
PX.SM.EMailSyncReference.EMailSyncServerByServerID -> PX.SM.EMailSyncServer (ServerID=AccountID)

# PX.SM.EMailSyncServer (EntityType)

Key: AccountCD
Entity sets: PX_SM_EMailSyncServer

PX.SM.EMailSyncServer.AccountID : Edm.Int32
PX.SM.EMailSyncServer.AccountCD : Edm.String [key] "Name"
PX.SM.EMailSyncServer.ServerType : Edm.String "Web Services"
PX.SM.EMailSyncServer.IsActive : Edm.Boolean [required] "Is Active"
PX.SM.EMailSyncServer.Address : Edm.String "Username"
PX.SM.EMailSyncServer.Password : Edm.String "Password"
PX.SM.EMailSyncServer.AuthenticationMethod : Edm.Int32 [required] "Authentication Method"
PX.SM.EMailSyncServer.OAuthApplicationID : Edm.Int32 "External Application"
PX.SM.EMailSyncServer.AzureTenantID : Edm.String "Azure Tenant ID"
PX.SM.EMailSyncServer.ServerUrl : Edm.String "Mail Server (Optional)"
PX.SM.EMailSyncServer.SyncSelectBatch : Edm.Int32 "Select Batch Size"
PX.SM.EMailSyncServer.SyncUpdateBatch : Edm.Int32 "Update Batch Size"
PX.SM.EMailSyncServer.SyncProcBatch : Edm.Int32 "Accounts in Batch"
PX.SM.EMailSyncServer.SyncAttachmentSize : Edm.Int32 "Max Attachment Size, KB"
PX.SM.EMailSyncServer.DefaultPolicyName : Edm.String "Default Sync Policy"
PX.SM.EMailSyncServer.ConnectionMode : Edm.String "Connection Mode"
PX.SM.EMailSyncServer.LoggingLevel : Edm.String "Logging Level"
PX.SM.EMailSyncServer.IsMigratedGraphContacts : Edm.Boolean [required] "Migrated Contacts"
PX.SM.EMailSyncServer.IsMigratedGraphEmails : Edm.Boolean [required] "Migrated Emails"
PX.SM.EMailSyncServer.IsMigratedGraphTasks : Edm.Boolean [required] "Migrated Tasks"
PX.SM.EMailSyncServer.IsMigratedGraphEvents : Edm.Boolean [required] "Migrated Events"
PX.SM.EMailSyncServer.OAuthApplicationByOAuthApplicationID -> PX.OAuthClient.DAC.OAuthApplication (OAuthApplicationID=ApplicationID)
PX.SM.EMailSyncServer.EMailSyncPolicyByDefaultPolicyName -> PX.SM.EMailSyncPolicy (DefaultPolicyName=PolicyName)
PX.SM.EMailSyncServer.EMailSyncAccountCollection -> Collection(PX.SM.EMailSyncAccount)
PX.SM.EMailSyncServer.EMailSyncLogCollection -> Collection(PX.SM.EMailSyncLog)
PX.SM.EMailSyncServer.EMailSyncReferenceCollection -> Collection(PX.SM.EMailSyncReference)

# PX.SM.EntityEndpointInProject (EntityType)

Key: GateVersion, InterfaceName
Entity sets: PX_SM_EntityEndpointInProject

PX.SM.EntityEndpointInProject.CompanyID : Edm.Int32 "CompanyId"
PX.SM.EntityEndpointInProject.InterfaceName : Edm.String [key] "Endpoint Name"
PX.SM.EntityEndpointInProject.GateVersion : Edm.String [key] "Endpoint Version"
PX.SM.EntityEndpointInProject.ExtendsVersion : Edm.String "Base Endpoint Version"
PX.SM.EntityEndpointInProject.ExtendsName : Edm.String "Base Endpoint Name"
PX.SM.EntityEndpointInProject.SystemContractVersion : Edm.Int32 "System Contract"
PX.SM.EntityEndpointInProject.BCBindingCollection -> Collection(PX.Commerce.Core.BCBinding)
PX.SM.EntityEndpointInProject.LLMPromptToolCBApiCurrentCollection -> Collection(PX.AIStudio.DAC.LLMPromptToolCBApiCurrent)

# PX.SM.EulaStatus (EntityType)

Singletons: PX_SM_EulaStatus

PX.SM.EulaStatus.PKID : Edm.Guid "PKID"
PX.SM.EulaStatus.IPAddress : Edm.String "IP address"
PX.SM.EulaStatus.Date : Edm.DateTimeOffset "Date"

# PX.SM.GiDesignInProject (EntityType)

Label: "Generic Inquiry"
BaseType: PX.Data.Maintenance.GI.GIDesign
Key: Name (inherited from PX.Data.Maintenance.GI.GIDesign)
Entity sets: PX_SM_GiDesignInProject

PX.SM.GiDesignInProject.CompanyID : Edm.Int32 "CompanyId"

# PX.SM.Instance (EntityType)

Label: "Application"
Key: InstallationID
Entity sets: PX_SM_Instance, Application, Instance

PX.SM.Instance.InstallationID : Edm.String [key]
PX.SM.Instance.DatabaseInfo : Edm.String
PX.SM.Instance.Date : Edm.DateTimeOffset

# PX.SM.KBFeedback (EntityType)

Key: FeedbackID
Entity sets: PX_SM_KBFeedback
Non-filterable, non-selectable: PageID

PX.SM.KBFeedback.FeedbackID : Edm.Int32 [key] "FeedbackID"
PX.SM.KBFeedback.IsFind : Edm.String "A user found what he or she had been looking for"
PX.SM.KBFeedback.Satisfaction : Edm.String "Overall satisfaction with Self-Service Portal"
PX.SM.KBFeedback.Summary : Edm.String "Other user comments and suggestions"
PX.SM.KBFeedback.UserID : Edm.Guid "User ID"
PX.SM.KBFeedback.PageID : Edm.Guid "Page ID"
PX.SM.KBFeedback.Date : Edm.DateTimeOffset "Date"
PX.SM.KBFeedback.CreatedByScreenID : Edm.String
PX.SM.KBFeedback.CreatedByID : Edm.Guid "Created By"
PX.SM.KBFeedback.CreatedDateTime : Edm.DateTimeOffset
PX.SM.KBFeedback.LastModifiedByID : Edm.Guid "Last Modified By"
PX.SM.KBFeedback.LastModifiedByScreenID : Edm.String
PX.SM.KBFeedback.LastModifiedDateTime : Edm.DateTimeOffset
PX.SM.KBFeedback.tstamp : Edm.Binary
PX.SM.KBFeedback.UsersByCreatedByID -> PX.SM.Users (CreatedByID=PKID)
PX.SM.KBFeedback.UsersByLastModifiedByID -> PX.SM.Users (LastModifiedByID=PKID)

# PX.SM.KBResponse (EntityType)

Key: ResponseID
Entity sets: PX_SM_KBResponse

PX.SM.KBResponse.ResponseID : Edm.Int32 [key] "ResponseID"
PX.SM.KBResponse.PageID : Edm.Guid "Article"
PX.SM.KBResponse.UserID : Edm.Guid "User ID"
PX.SM.KBResponse.RevisionID : Edm.Int32 [required] "Revision"
PX.SM.KBResponse.Date : Edm.DateTimeOffset "Date"
PX.SM.KBResponse.Summary : Edm.String "Summary"
PX.SM.KBResponse.NewMark : Edm.Int32 "Mark"
PX.SM.KBResponse.OldMark : Edm.Int32 "Mark"
PX.SM.KBResponse.CreatedByScreenID : Edm.String
PX.SM.KBResponse.CreatedByID : Edm.Guid "Created By"
PX.SM.KBResponse.CreatedDateTime : Edm.DateTimeOffset
PX.SM.KBResponse.LastModifiedByID : Edm.Guid "Last Modified By"
PX.SM.KBResponse.LastModifiedByScreenID : Edm.String
PX.SM.KBResponse.LastModifiedDateTime : Edm.DateTimeOffset
PX.SM.KBResponse.tstamp : Edm.Binary
PX.SM.KBResponse.WikiPageByPageID -> PX.SM.WikiPage (PageID=PageID)
PX.SM.KBResponse.UsersByCreatedByID -> PX.SM.Users (CreatedByID=PKID)
PX.SM.KBResponse.UsersByLastModifiedByID -> PX.SM.Users (LastModifiedByID=PKID)

# PX.SM.KBResponseMark (EntityType)

Key: Mark
Entity sets: PX_SM_KBResponseMark

PX.SM.KBResponseMark.Mark : Edm.Int32 [key] "Value"
PX.SM.KBResponseMark.Name : Edm.String "Name"
PX.SM.KBResponseMark.CreatedByScreenID : Edm.String
PX.SM.KBResponseMark.CreatedByID : Edm.Guid "Created By"
PX.SM.KBResponseMark.CreatedDateTime : Edm.DateTimeOffset
PX.SM.KBResponseMark.LastModifiedByID : Edm.Guid "Last Modified By"
PX.SM.KBResponseMark.LastModifiedByScreenID : Edm.String
PX.SM.KBResponseMark.LastModifiedDateTime : Edm.DateTimeOffset
PX.SM.KBResponseMark.tstamp : Edm.Binary
PX.SM.KBResponseMark.UsersByCreatedByID -> PX.SM.Users (CreatedByID=PKID)
PX.SM.KBResponseMark.UsersByLastModifiedByID -> PX.SM.Users (LastModifiedByID=PKID)

# PX.SM.KBResponseSummary (EntityType)

Key: PageID
Entity sets: PX_SM_KBResponseSummary

PX.SM.KBResponseSummary.PageID : Edm.Guid [key] "Article"
PX.SM.KBResponseSummary.Markcount : Edm.Int32 "Mark Count"
PX.SM.KBResponseSummary.Marksummary : Edm.Int32 "Mark Summary"
PX.SM.KBResponseSummary.Views : Edm.Int32 "Views"
PX.SM.KBResponseSummary.AvRate : Edm.Double "Average Rate"
PX.SM.KBResponseSummary.CreatedByScreenID : Edm.String
PX.SM.KBResponseSummary.CreatedByID : Edm.Guid "Created By"
PX.SM.KBResponseSummary.CreatedDateTime : Edm.DateTimeOffset
PX.SM.KBResponseSummary.LastModifiedByID : Edm.Guid "Last Modified By"
PX.SM.KBResponseSummary.LastModifiedByScreenID : Edm.String
PX.SM.KBResponseSummary.LastModifiedDateTime : Edm.DateTimeOffset
PX.SM.KBResponseSummary.tstamp : Edm.Binary
PX.SM.KBResponseSummary.WikiPageByPageID -> PX.SM.WikiPage (PageID=PageID)
PX.SM.KBResponseSummary.UsersByCreatedByID -> PX.SM.Users (CreatedByID=PKID)
PX.SM.KBResponseSummary.UsersByLastModifiedByID -> PX.SM.Users (LastModifiedByID=PKID)

# PX.SM.Licensing (EntityType)

Singletons: PX_SM_Licensing

PX.SM.Licensing.InstallationID : Edm.String "Installation ID"
PX.SM.Licensing.LicensingKey : Edm.String "Licensing Key"
PX.SM.Licensing.Signature : Edm.String
PX.SM.Licensing.Restriction : Edm.String
PX.SM.Licensing.Date : Edm.DateTimeOffset "Date"
PX.SM.Licensing.Activity : Edm.DateTimeOffset
PX.SM.Licensing.Status : Edm.String

# PX.SM.Locale (EntityType)

Label: "Locale"
Key: LocaleName
Entity sets: PX_SM_Locale, Locale
Non-filterable, non-selectable: CultureReadableName

PX.SM.Locale.LocaleName : Edm.String [key] "Locale Name"
PX.SM.Locale.Description : Edm.String "Description"
PX.SM.Locale.TranslatedName : Edm.String "Locale Name in Locale Language"
PX.SM.Locale.ShowValidationWarnings : Edm.Boolean "Show Validation Warnings"
PX.SM.Locale.Number : Edm.Int16 "Sequence"
PX.SM.Locale.IsActive : Edm.Boolean [required] "Active"
PX.SM.Locale.CultureReadableName : Edm.String "English Name"
PX.SM.Locale.FormatID : Edm.Int32
PX.SM.Locale.IsDefault : Edm.Boolean [required] "Default Language"
PX.SM.Locale.IsAlternative : Edm.Boolean [required] "Alternative Language"
PX.SM.Locale.EPEmployeeCollection -> Collection(PX.Objects.EP.EPEmployee)
PX.SM.Locale.VendorCollection -> Collection(PX.Objects.AP.Vendor)
PX.SM.Locale.CustomerCollection -> Collection(PX.Objects.AR.Customer)
PX.SM.Locale.SYMappingCollection -> Collection(PX.Api.SYMapping)
PX.SM.Locale.BAccountCollection -> Collection(PX.Objects.CR.BAccount)
PX.SM.Locale.ContactCollection -> Collection(PX.Objects.CR.Contact)
PX.SM.Locale.CRLeadCollection -> Collection(PX.Objects.CR.CRLead)
PX.SM.Locale.EPEmployeeClassCollection -> Collection(PX.Objects.EP.EPEmployeeClass)
PX.SM.Locale.VendorClassCollection -> Collection(PX.Objects.AP.VendorClass)
PX.SM.Locale.NotificationCollection -> Collection(PX.SM.Notification)
PX.SM.Locale.TaskTemplateCollection -> Collection(PX.SM.TaskTemplate)
PX.SM.Locale.CountryCollection -> Collection(PX.Objects.CS.Country)
PX.SM.Locale.CROpportunityRevisionCollection -> Collection(PX.Objects.CR.Standalone.CROpportunityRevision)
PX.SM.Locale.CustomerClassCollection -> Collection(PX.Objects.AR.CustomerClass)
PX.SM.Locale.MobileNotificationCollection -> Collection(PX.BusinessProcess.DAC.MobileNotification)
PX.SM.Locale.BCBindingCollection -> Collection(PX.Commerce.Core.BCBinding)
PX.SM.Locale.SMTeamsNotificationCollection -> Collection(PX.MSTeams.DAC.SM.SMTeamsNotification)
PX.SM.Locale.LocaleFormatCollection -> Collection(PX.SM.LocaleFormat)
PX.SM.Locale.CROpportunityCollection -> Collection(PX.Objects.CR.CROpportunity)

# PX.SM.LocaleFormat (EntityType)

Label: "Custom Locale Format"
Key: FormatID
Entity sets: PX_SM_LocaleFormat, CustomLocaleFormat, LocaleFormat

PX.SM.LocaleFormat.FormatID : Edm.Int32 [key]
PX.SM.LocaleFormat.TemplateLocale : Edm.String "Format"
PX.SM.LocaleFormat.NumberDecimalSeporator : Edm.String "Decimal Symbol"
PX.SM.LocaleFormat.NumberGroupSeparator : Edm.String "Digit Grouping Symbol"
PX.SM.LocaleFormat.DateTimePattern : Edm.String "Date Time"
PX.SM.LocaleFormat.TimeShortPattern : Edm.String "Short Time"
PX.SM.LocaleFormat.TimeLongPattern : Edm.String "Long Time"
PX.SM.LocaleFormat.DateShortPattern : Edm.String "Short Date"
PX.SM.LocaleFormat.DateLongPattern : Edm.String "Long Date"
PX.SM.LocaleFormat.AMDesignator : Edm.String "AM Symbol"
PX.SM.LocaleFormat.PMDesignator : Edm.String "PM Symbol"
PX.SM.LocaleFormat.LocaleByTemplateLocale -> PX.SM.Locale (TemplateLocale=LocaleName)

# PX.SM.LoginTrace (EntityType)

Label: "Login Trace"
Key: LoginTraceID
Entity sets: PX_SM_LoginTrace, LoginTrace

PX.SM.LoginTrace.LoginTraceID : Edm.Int32 [key]
PX.SM.LoginTrace.ApplicationName : Edm.String
PX.SM.LoginTrace.Host : Edm.String "Host"
PX.SM.LoginTrace.Date : Edm.DateTimeOffset "Date"
PX.SM.LoginTrace.Username : Edm.String "Username"
PX.SM.LoginTrace.Operation : Edm.Int32 "Operation"
PX.SM.LoginTrace.IPAddress : Edm.String "IP address"
PX.SM.LoginTrace.ScreenID : Edm.String "Screen ID"
PX.SM.LoginTrace.Comment : Edm.String "Comment"
PX.SM.LoginTrace.NoteID : Edm.Guid
PX.SM.LoginTrace.SiteMapByScreenID -> PX.SM.SiteMap (ScreenID=ScreenID)
PX.SM.LoginTrace.UsersByUsername -> PX.SM.Users (Username=Username)

# PX.SM.MobileSiteMap (EntityType)

Label: "Mobile Site Map"
Key: ScreenID, Type
Entity sets: PX_SM_MobileSiteMap, MobileSiteMap

PX.SM.MobileSiteMap.ScreenID : Edm.String [key] "Screen ID"
PX.SM.MobileSiteMap.Script : Edm.String "Script"
PX.SM.MobileSiteMap.Type : Edm.String [key] "Type"
PX.SM.MobileSiteMap.IsConverted : Edm.Boolean [required]
PX.SM.MobileSiteMap.CreatedByID : Edm.Guid "Created By"
PX.SM.MobileSiteMap.CreatedByScreenID : Edm.String
PX.SM.MobileSiteMap.CreatedDateTime : Edm.DateTimeOffset
PX.SM.MobileSiteMap.LastModifiedByID : Edm.Guid "Last Modified By"
PX.SM.MobileSiteMap.LastModifiedByScreenID : Edm.String
PX.SM.MobileSiteMap.LastModifiedDateTime : Edm.DateTimeOffset "Last Modified On"
PX.SM.MobileSiteMap.UsersByCreatedByID -> PX.SM.Users (CreatedByID=PKID)
PX.SM.MobileSiteMap.UsersByLastModifiedByID -> PX.SM.Users (LastModifiedByID=PKID)

# PX.SM.MobileSiteMapInProject (EntityType)

Label: "Mobile Site Map"
BaseType: PX.SM.MobileSiteMap
Key: ScreenID, Type (inherited from PX.SM.MobileSiteMap)
Entity sets: PX_SM_MobileSiteMapInProject

PX.SM.MobileSiteMapInProject.CompanyID : Edm.Int32 "CompanyId"

# PX.SM.MobileSiteMapWorkspacesInProject (EntityType)

Key: Name
Entity sets: PX_SM_MobileSiteMapWorkspacesInProject

PX.SM.MobileSiteMapWorkspacesInProject.MobileWorkspaceID : Edm.Guid
PX.SM.MobileSiteMapWorkspacesInProject.Owner : Edm.String
PX.SM.MobileSiteMapWorkspacesInProject.Name : Edm.String [key] "Workspace ID"
PX.SM.MobileSiteMapWorkspacesInProject.DisplayName : Edm.String "Display Name"
PX.SM.MobileSiteMapWorkspacesInProject.Icon : Edm.String "Icon"
PX.SM.MobileSiteMapWorkspacesInProject.SortOrder : Edm.Int32 "SortOrder"
PX.SM.MobileSiteMapWorkspacesInProject.IsActive : Edm.Boolean "Active"
PX.SM.MobileSiteMapWorkspacesInProject.CompanyID : Edm.Int32 "CompanyId"

# PX.SM.MUIScreenInProject (EntityType)

Label: "Screen"
BaseType: PX.Web.UI.Frameset.Model.DAC.MUIScreen
Key: IsPortal, NodeID, WorkspaceID (inherited from PX.Web.UI.Frameset.Model.DAC.MUIScreen)
Entity sets: PX_SM_MUIScreenInProject

PX.SM.MUIScreenInProject.CompanyID : Edm.Int32 "CompanyId"

# PX.SM.MUITileInProject (EntityType)

Label: "Tile"
BaseType: PX.Web.UI.Frameset.Model.DAC.MUITile
Key: IsPortal, TileID (inherited from PX.Web.UI.Frameset.Model.DAC.MUITile)
Entity sets: PX_SM_MUITileInProject

PX.SM.MUITileInProject.CompanyID : Edm.Int32 "CompanyId"

# PX.SM.Neighbour (EntityType)

Key: LeftEntityType, RightEntityType
Entity sets: PX_SM_Neighbour

PX.SM.Neighbour.LeftEntityType : Edm.String [key]
PX.SM.Neighbour.RightEntityType : Edm.String [key]
PX.SM.Neighbour.CoverageMask : Edm.Binary
PX.SM.Neighbour.InverseMask : Edm.Binary
PX.SM.Neighbour.WinCoverageMask : Edm.Binary
PX.SM.Neighbour.WinInverseMask : Edm.Binary

# PX.SM.Notification (EntityType)

Label: "Notification"
Key: NotificationID
Entity sets: PX_SM_Notification, Notification
Non-filterable, non-selectable: NoteText, CreatedFromReport

PX.SM.Notification.NotificationID : Edm.Int32 [key] "Notification ID"
PX.SM.Notification.Name : Edm.String "Description"
PX.SM.Notification.NFrom : Edm.Int32 "From"
PX.SM.Notification.NTo : Edm.String "To"
PX.SM.Notification.NCc : Edm.String "CC"
PX.SM.Notification.NBcc : Edm.String "BCC"
PX.SM.Notification.Subject : Edm.String "Subject"
PX.SM.Notification.ScreenID : Edm.String "Screen"
PX.SM.Notification.Body : Edm.String "Body"
PX.SM.Notification.LocaleName : Edm.String "Locale"
PX.SM.Notification.NoteID : Edm.Guid
PX.SM.Notification.NoteText : Edm.String "Note Text"
PX.SM.Notification.CreatedByID : Edm.Guid "Created By"
PX.SM.Notification.CreatedByScreenID : Edm.String
PX.SM.Notification.CreatedDateTime : Edm.DateTimeOffset "Created On"
PX.SM.Notification.LastModifiedByID : Edm.Guid "Last Modified By"
PX.SM.Notification.LastModifiedByScreenID : Edm.String
PX.SM.Notification.LastModifiedDateTime : Edm.DateTimeOffset "Last Modified On"
PX.SM.Notification.tstamp : Edm.Binary
PX.SM.Notification.BAccountID : Edm.String "Link-To Account"
PX.SM.Notification.ContactID : Edm.String "Link-To Contact"
PX.SM.Notification.RefNoteID : Edm.String "Link-To Entity"
PX.SM.Notification.ReportAction : Edm.String "Attach Report Opened by Action"
PX.SM.Notification.AttachActivity : Edm.Boolean [required] "Attach Activity"
PX.SM.Notification.Type : Edm.String "Activity Type"
PX.SM.Notification.CreatedFromReport : Edm.Boolean
PX.SM.Notification.UsersByCreatedByID -> PX.SM.Users (CreatedByID=PKID)
PX.SM.Notification.UsersByLastModifiedByID -> PX.SM.Users (LastModifiedByID=PKID)
PX.SM.Notification.EMailAccountByNfrom -> PX.SM.EMailAccount
PX.SM.Notification.EPActivityTypeByType -> PX.Objects.EP.EPActivityType (Type=Type)
PX.SM.Notification.LocaleByLocaleName -> PX.SM.Locale (LocaleName=LocaleName)
PX.SM.Notification.ProjectManagementSetupCollection -> Collection(PX.Objects.PJ.ProjectManagement.PJ.DAC.ProjectManagementSetup)
PX.SM.Notification.ContactNotificationCollection -> Collection(PX.Objects.CR.ContactNotification)
PX.SM.Notification.NotificationSetupCollection -> Collection(PX.Objects.CS.NotificationSetup)
PX.SM.Notification.SCSetupCollection -> Collection(PX.Objects.CN.SCSetup)
PX.SM.Notification.PMSetupCollection -> Collection(PX.Objects.PM.PMSetup)
PX.SM.Notification.CRSetupCollection -> Collection(PX.Objects.CR.CRSetup)
PX.SM.Notification.EPSetupCollection -> Collection(PX.Objects.EP.EPSetup)
PX.SM.Notification.SPPortalCollection -> Collection(PX.Objects.Portals.SPPortal)
PX.SM.Notification.EMailAccountCollection -> Collection(PX.SM.EMailAccount)
PX.SM.Notification.PreferencesEmailCollection -> Collection(PX.SM.PreferencesEmail)
PX.SM.Notification.SOSetupApprovalCollection -> Collection(PX.Objects.SO.SOSetupApproval)
PX.SM.Notification.SOSetupInvoiceApprovalCollection -> Collection(PX.Objects.SO.SOSetupInvoiceApproval)
PX.SM.Notification.RQSetupApprovalCollection -> Collection(PX.Objects.RQ.RQSetupApproval)
PX.SM.Notification.POSetupApprovalCollection -> Collection(PX.Objects.PO.POSetupApproval)
PX.SM.Notification.CarrierPluginCollection -> Collection(PX.Objects.CS.CarrierPlugin)
PX.SM.Notification.NotificationSourceCollection -> Collection(PX.Objects.CS.NotificationSource)
PX.SM.Notification.INSetupApprovalCollection -> Collection(PX.Objects.IN.DAC.INSetupApproval)
PX.SM.Notification.GLSetupApprovalCollection -> Collection(PX.Objects.GL.GLSetupApproval)
PX.SM.Notification.CASetupApprovalCollection -> Collection(PX.Objects.CA.CASetupApproval)
PX.SM.Notification.ARSetupApprovalCollection -> Collection(PX.Objects.AR.ARSetupApproval)
PX.SM.Notification.APSetupApprovalCollection -> Collection(PX.Objects.AP.APSetupApproval)
PX.SM.Notification.QueueNotificationSettingsCollection -> Collection(PX.BusinessProcess.DAC.QueueNotificationSettings)
PX.SM.Notification.AMECOSetupApprovalCollection -> Collection(PX.Objects.AM.AMECOSetupApproval)
PX.SM.Notification.AMECRSetupApprovalCollection -> Collection(PX.Objects.AM.AMECRSetupApproval)
PX.SM.Notification.SVSetupInvoiceApprovalCollection -> Collection(PX.Objects.SV.SVSetupInvoiceApproval)
PX.SM.Notification.NotificationReportCollection -> Collection(PX.SM.NotificationReport)
PX.SM.Notification.MLCrossSalesSetupCollection -> Collection(PX.ML.CrossSales.DAC.MLCrossSalesSetup)
PX.SM.Notification.NotificationScheduleCollection -> Collection(PX.Data.Maintenance.SM.SendRecurringNotifications.NotificationSchedule)
PX.SM.Notification.BPEventSubscriberCollection -> Collection(PX.BusinessProcess.DAC.BPEventSubscriber)

# PX.SM.NotificationReport (EntityType)

Label: "Notification Report"
Key: ReportID
Entity sets: PX_SM_NotificationReport, NotificationReport
Non-filterable, non-selectable: Title, PassData

PX.SM.NotificationReport.ReportID : Edm.Guid [key]
PX.SM.NotificationReport.NotificationID : Edm.Int32 "Notification ID"
PX.SM.NotificationReport.ScreenID : Edm.String "Report ID"
PX.SM.NotificationReport.Title : Edm.String "Title"
PX.SM.NotificationReport.Format : Edm.Byte "Report Format"
PX.SM.NotificationReport.Embedded : Edm.Boolean "Embedded"
PX.SM.NotificationReport.CreatedDateTime : Edm.DateTimeOffset "Creation Date"
PX.SM.NotificationReport.DataToPass : Edm.Byte
PX.SM.NotificationReport.PassData : Edm.Boolean "Use Event as Data Source"
PX.SM.NotificationReport.TableToPass : Edm.String "Source Table"
PX.SM.NotificationReport.ReportTemplateID : Edm.Guid "Report Template"
PX.SM.NotificationReport.SiteMapByScreenID -> PX.SM.SiteMap (ScreenID=ScreenID)
PX.SM.NotificationReport.NotificationByNotificationID -> PX.SM.Notification (NotificationID=NotificationID)
PX.SM.NotificationReport.NotificationReportParameterCollection -> Collection(PX.SM.NotificationReportParameter)

# PX.SM.NotificationReportParameter (EntityType)

Label: "Notification Report Parameter"
Key: Name, ReportID
Entity sets: PX_SM_NotificationReportParameter, NotificationReportParameter
Non-filterable, non-selectable: IsOverride, FromDB, ScreenID

PX.SM.NotificationReportParameter.ReportID : Edm.Guid [key] "ReportID"
PX.SM.NotificationReportParameter.Name : Edm.String [key] "Parameter Name"
PX.SM.NotificationReportParameter.Value : Edm.String "Parameter Value"
PX.SM.NotificationReportParameter.FromSchema : Edm.Boolean "From Schema"
PX.SM.NotificationReportParameter.IsOverride : Edm.Boolean "Overridden"
PX.SM.NotificationReportParameter.FromDB : Edm.Boolean
PX.SM.NotificationReportParameter.ScreenID : Edm.String
PX.SM.NotificationReportParameter.NotificationReportByReportID -> PX.SM.NotificationReport (ReportID=ReportID)

# PX.SM.OAuthClient (EntityType)

Key: ClientID
Entity sets: PX_SM_OAuthClient
Non-filterable, non-selectable: FullClientID

PX.SM.OAuthClient.CompanyID : Edm.Int32 "CompanyId"
PX.SM.OAuthClient.ClientID : Edm.Guid [key] "Client ID"
PX.SM.OAuthClient.FullClientID : Edm.String "Client ID"
PX.SM.OAuthClient.ClientName : Edm.String "Client Name"
PX.SM.OAuthClient.Enabled : Edm.Boolean [required] "Active"
PX.SM.OAuthClient.ClientUri : Edm.String
PX.SM.OAuthClient.LogoUri : Edm.String
PX.SM.OAuthClient.Flow : Edm.String "Flow"
PX.SM.OAuthClient.Plugin : Edm.String "Plug-In"

# PX.SM.PortalMap (EntityType)

Label: "Portal Map"
BaseType: PX.SM.SiteMap
Key: NodeID (inherited from PX.SM.SiteMap)
Entity sets: PX_SM_PortalMap, PortalMap

# PX.SM.PreferencesEmail (EntityType)

Singletons: PX_SM_PreferencesEmail

PX.SM.PreferencesEmail.DefaultEMailAccountID : Edm.Int32 "Default Email Account"
PX.SM.PreferencesEmail.SupportEMailAccount : Edm.String "Support Email Account"
PX.SM.PreferencesEmail.EmailTagPrefix : Edm.String "Email Tag Prefix"
PX.SM.PreferencesEmail.EmailTagSuffix : Edm.String "Email Tag Suffix"
PX.SM.PreferencesEmail.ArchiveEmailsOlderThan : Edm.Int32 "Archive Emails"
PX.SM.PreferencesEmail.RepeatOnErrorSending : Edm.Int32 [required] "Automatic Resend Attempts"
PX.SM.PreferencesEmail.SuspendEmailProcessing : Edm.Boolean "Suspend Email Processing"
PX.SM.PreferencesEmail.SendUserEmailsImmediately : Edm.Boolean [required] "Send User Emails Immediately"
PX.SM.PreferencesEmail.EmailProcessingLogging : Edm.Int32 [required] "Email Processing Logging"
PX.SM.PreferencesEmail.EmailProcessingLoggingRetentionPeriod : Edm.String "Keep Email Logs For"
PX.SM.PreferencesEmail.UserWelcomeNotificationId : Edm.Int32 "New User Welcome Email Template"
PX.SM.PreferencesEmail.PortalUserWelcomeNotificationId : Edm.Int32 "Welcome Email Template (New Portal User)"
PX.SM.PreferencesEmail.PasswordChangedNotificationId : Edm.Int32 "Password Changed Email Template"
PX.SM.PreferencesEmail.LoginRecoveryNotificationId : Edm.Int32 "Login Recovery Email Template"
PX.SM.PreferencesEmail.PasswordRecoveryNotificationId : Edm.Int32 "Password Recovery Email Template"
PX.SM.PreferencesEmail.PortalPasswordRecoveryNotificationId : Edm.Int32 "Password Recovery Email Template (Portal)"
PX.SM.PreferencesEmail.TwoFactorNewDeviceNotificationId : Edm.Int32 "New Device Code Email Template"
PX.SM.PreferencesEmail.TwoFactorCodeByNotificationId : Edm.Int32 "Two-Factor Access Code Email Template"
PX.SM.PreferencesEmail.NotificationSiteUrl : Edm.String "URL to be used in Notifications"
PX.SM.PreferencesEmail.CreatedByID : Edm.Guid "Created By"
PX.SM.PreferencesEmail.CreatedByScreenID : Edm.String
PX.SM.PreferencesEmail.CreatedDateTime : Edm.DateTimeOffset
PX.SM.PreferencesEmail.LastModifiedByID : Edm.Guid "Last Modified By"
PX.SM.PreferencesEmail.LastModifiedByScreenID : Edm.String
PX.SM.PreferencesEmail.LastModifiedDateTime : Edm.DateTimeOffset
PX.SM.PreferencesEmail.UsersByCreatedByID -> PX.SM.Users (CreatedByID=PKID)
PX.SM.PreferencesEmail.UsersByLastModifiedByID -> PX.SM.Users (LastModifiedByID=PKID)
PX.SM.PreferencesEmail.NotificationByUserWelcomeNotificationId -> PX.SM.Notification (UserWelcomeNotificationId=NotificationID)
PX.SM.PreferencesEmail.NotificationByPortalUserWelcomeNotificationId -> PX.SM.Notification (PortalUserWelcomeNotificationId=NotificationID)
PX.SM.PreferencesEmail.NotificationByPasswordChangedNotificationId -> PX.SM.Notification (PasswordChangedNotificationId=NotificationID)
PX.SM.PreferencesEmail.NotificationByLoginRecoveryNotificationId -> PX.SM.Notification (LoginRecoveryNotificationId=NotificationID)
PX.SM.PreferencesEmail.NotificationByPasswordRecoveryNotificationId -> PX.SM.Notification (PasswordRecoveryNotificationId=NotificationID)
PX.SM.PreferencesEmail.NotificationByPortalPasswordRecoveryNotificationId -> PX.SM.Notification (PortalPasswordRecoveryNotificationId=NotificationID)
PX.SM.PreferencesEmail.NotificationByTwoFactorNewDeviceNotificationId -> PX.SM.Notification (TwoFactorNewDeviceNotificationId=NotificationID)
PX.SM.PreferencesEmail.NotificationByTwoFactorCodeByNotificationId -> PX.SM.Notification (TwoFactorCodeByNotificationId=NotificationID)
PX.SM.PreferencesEmail.EMailAccountByDefaultEMailAccountID -> PX.SM.EMailAccount (DefaultEMailAccountID=EmailAccountID)

# PX.SM.PreferencesGeneral (EntityType)

Label: "General Preferences"
Singletons: PX_SM_PreferencesGeneral, GeneralPreferences, PreferencesGeneral

PX.SM.PreferencesGeneral.MapViewer : Edm.Int32 "Map Viewer"
PX.SM.PreferencesGeneral.GridActionsText : Edm.Boolean "Show Tooltips for Table Toolbar Buttons"
PX.SM.PreferencesGeneral.GridFastFilterCondition : Edm.Int32 [required] "Search Condition"
PX.SM.PreferencesGeneral.GridFastFilterMaxLength : Edm.Int32 [required] "Max. Length of Search String"
PX.SM.PreferencesGeneral.TimeZone : Edm.String "Login Time Zone"
PX.SM.PreferencesGeneral.MaxUploadSize : Edm.Int32 [required] "Maximum File Upload Size in KB"
PX.SM.PreferencesGeneral.GetLinkTemplate : Edm.Guid "Template for External Links"
PX.SM.PreferencesGeneral.HeaderFont : Edm.String "Font"
PX.SM.PreferencesGeneral.HeaderFontSize : Edm.Int16 "Size"
PX.SM.PreferencesGeneral.HeaderFontColor : Edm.String "Font Color"
PX.SM.PreferencesGeneral.HeaderFillColor : Edm.String "Fill Color"
PX.SM.PreferencesGeneral.HeaderFontType : Edm.String "Style"
PX.SM.PreferencesGeneral.BodyFont : Edm.String "Font"
PX.SM.PreferencesGeneral.BodyFontSize : Edm.Int16 "Size"
PX.SM.PreferencesGeneral.BodyFontColor : Edm.String "Font Color"
PX.SM.PreferencesGeneral.BodyFillColor : Edm.String "Fill Color"
PX.SM.PreferencesGeneral.BodyFontType : Edm.String "Style"
PX.SM.PreferencesGeneral.Border : Edm.Boolean "Draw Border"
PX.SM.PreferencesGeneral.BorderColor : Edm.String "Border Color"
PX.SM.PreferencesGeneral.HiddenSkip : Edm.Boolean "Skip Hidden Fields"
PX.SM.PreferencesGeneral.EditorFontName : Edm.String "Editor Font"
PX.SM.PreferencesGeneral.EditorFontSize : Edm.Int32
PX.SM.PreferencesGeneral.SpellCheck : Edm.Boolean "Spell Check"
PX.SM.PreferencesGeneral.NoteID : Edm.Guid "NoteID"
PX.SM.PreferencesGeneral.NoteText : Edm.String "Note Text"
PX.SM.PreferencesGeneral.Theme : Edm.String "Interface Theme"
PX.SM.PreferencesGeneral.PrimaryColor : Edm.String "Primary Color"
PX.SM.PreferencesGeneral.BackgroundColor : Edm.String "Background Color"
PX.SM.PreferencesGeneral.HomePage : Edm.Guid "Home Page"
PX.SM.PreferencesGeneral.HelpPage : Edm.Guid "Help On Help"
PX.SM.PreferencesGeneral.UseMLSearch : Edm.Boolean [required] "Use Online Help System"
PX.SM.PreferencesGeneral.DeletingMLEventsMode : Edm.Int32 [required]
PX.SM.PreferencesGeneral.MLEventsRetentionAge : Edm.Int32 [required]
PX.SM.PreferencesGeneral.PortalHomePage : Edm.Guid "Home Page"
PX.SM.PreferencesGeneral.PortalExternalAccessLink : Edm.String "Portal External Access Link"
PX.SM.PreferencesGeneral.PersonNameFormat : Edm.String "Display Name Order"
PX.SM.PreferencesGeneral.NeedUpdatePersonNames : Edm.Boolean
PX.SM.PreferencesGeneral.CreatedByID : Edm.Guid "Created By"
PX.SM.PreferencesGeneral.CreatedByScreenID : Edm.String
PX.SM.PreferencesGeneral.CreatedDateTime : Edm.DateTimeOffset
PX.SM.PreferencesGeneral.LastModifiedByID : Edm.Guid "Last Modified By"
PX.SM.PreferencesGeneral.LastModifiedByScreenID : Edm.String
PX.SM.PreferencesGeneral.LastModifiedDateTime : Edm.DateTimeOffset
PX.SM.PreferencesGeneral.ApplyToEmptyCells : Edm.Boolean [required] "Apply Body Settings to Empty Cells"
PX.SM.PreferencesGeneral.DefaultUI : Edm.String "Default UI"
PX.SM.PreferencesGeneral.OutlookAddInUI : Edm.String "Outlook Add-In UI"
PX.SM.PreferencesGeneral.DeleteGeneratedReports : Edm.Boolean [required] "Delete Printed Report Files"
PX.SM.PreferencesGeneral.WikiPageByGetLinkTemplate -> PX.SM.WikiPage (GetLinkTemplate=PageID)
PX.SM.PreferencesGeneral.WikiPageByHelpPage -> PX.SM.WikiPage (HelpPage=PageID)
PX.SM.PreferencesGeneral.UsersByCreatedByID -> PX.SM.Users (CreatedByID=PKID)
PX.SM.PreferencesGeneral.UsersByLastModifiedByID -> PX.SM.Users (LastModifiedByID=PKID)
PX.SM.PreferencesGeneral.AddressValidatorPluginByAddressLookupPluginID -> PX.Objects.CS.AddressValidatorPlugin

# PX.SM.PreferencesIdentityProvider (EntityType)

Key: InstanceKey, ProviderName
Entity sets: PX_SM_PreferencesIdentityProvider

PX.SM.PreferencesIdentityProvider.InstanceKey : Edm.String [key] "Instance Key"
PX.SM.PreferencesIdentityProvider.ProviderName : Edm.String [key] "Provider Name"
PX.SM.PreferencesIdentityProvider.Active : Edm.Boolean [required] "Active"
PX.SM.PreferencesIdentityProvider.Realm : Edm.String "Realm"
PX.SM.PreferencesIdentityProvider.ApplicationID : Edm.String "Application ID"
PX.SM.PreferencesIdentityProvider.ApplicationSecret : Edm.String "Application Secret"

# PX.SM.PreferencesSecurity (EntityType)

Singletons: PX_SM_PreferencesSecurity

PX.SM.PreferencesSecurity.DBCertificateName : Edm.String "DB Encryption Certificate"
PX.SM.PreferencesSecurity.DBPrevCertificateName : Edm.String
PX.SM.PreferencesSecurity.PdfCertificateName : Edm.String "PDF Signing Certificate"
PX.SM.PreferencesSecurity.DefaultMenuEditorRole : Edm.String "Personalization Management Role"
PX.SM.PreferencesSecurity.TraceMonthsKeep : Edm.Int32 [required] "Access History Retention Period (Months)"
PX.SM.PreferencesSecurity.TraceOperationMask : Edm.Int32 [required]
PX.SM.PreferencesSecurity.TraceOperationLogin : Edm.Boolean "Login"
PX.SM.PreferencesSecurity.TraceOperationLogout : Edm.Boolean "Logout"
PX.SM.PreferencesSecurity.TraceOperationSessionExpired : Edm.Boolean "Session Expired"
PX.SM.PreferencesSecurity.TraceOperationLoginFailed : Edm.Boolean "Login Failed"
PX.SM.PreferencesSecurity.TraceOperationAccessScreen : Edm.Boolean "Screen Accessed"
PX.SM.PreferencesSecurity.TraceOperationSendMail : Edm.Boolean "Send Email Success"
PX.SM.PreferencesSecurity.TraceOperationSendMailFailed : Edm.Boolean "Send Email Error"
PX.SM.PreferencesSecurity.TraceOperationLicenseExceeded : Edm.Boolean "License Exceeded"
PX.SM.PreferencesSecurity.TraceOperationODataRefresh : Edm.Boolean "OData Refresh"
PX.SM.PreferencesSecurity.TraceOperationMcpToolCall : Edm.Boolean "MCP Tool Call"
PX.SM.PreferencesSecurity.TraceOperationCustomizationPublished : Edm.Boolean "Customization Published"
PX.SM.PreferencesSecurity.MultiFactorAuthLevel : Edm.Int32 [required] "Two-Factor Authentication"
PX.SM.PreferencesSecurity.MultiFactorAllowedTypes : Edm.Int32 [required]
PX.SM.PreferencesSecurity.EmailEnabled : Edm.Boolean "Allow Email"
PX.SM.PreferencesSecurity.SmsEnabled : Edm.Boolean "Allow SMS"
PX.SM.PreferencesSecurity.IsPasswordDayAge : Edm.Boolean "Password Expiry Period in Days:"
PX.SM.PreferencesSecurity.PasswordDayAge : Edm.Int32 [required] "Days"
PX.SM.PreferencesSecurity.IsPasswordMinLength : Edm.Boolean "Minimum Characters in Password:"
PX.SM.PreferencesSecurity.PasswordMinLength : Edm.Int32 [required] "Characters"
PX.SM.PreferencesSecurity.PasswordComplexity : Edm.Boolean [required] "Password Must Meet Complexity Requirements"
PX.SM.PreferencesSecurity.PasswordRegexCheck : Edm.String "Additional Password Validation Mask"
PX.SM.PreferencesSecurity.PasswordRegexCheckMessage : Edm.String "Incorrect Password Alert"
PX.SM.PreferencesSecurity.PasswordSecurityType : Edm.Int16 [required] "Password Security Type"
PX.SM.PreferencesSecurity.AccountLockoutThreshold : Edm.Int32 "Failed Sign-In Attempts Before Account Lockout"
PX.SM.PreferencesSecurity.AccountLockoutDuration : Edm.Int32 "Account Lockout Duration (Minutes)"
PX.SM.PreferencesSecurity.AccountLockoutReset : Edm.Int32 "Reset Interval for Failed Sign-In Attempts (Minutes)"
PX.SM.PreferencesSecurity.AllowSupportToLoginAsAnyUser : Edm.Boolean [required] "Allow Support to Sign In as Any User"
PX.SM.PreferencesSecurity.RestrictDacAccess : Edm.Boolean [required] "DAC-Level Data Security"
PX.SM.PreferencesSecurity.CreatedByID : Edm.Guid "Created By"
PX.SM.PreferencesSecurity.CreatedByScreenID : Edm.String
PX.SM.PreferencesSecurity.CreatedDateTime : Edm.DateTimeOffset
PX.SM.PreferencesSecurity.LastModifiedByID : Edm.Guid "Last Modified By"
PX.SM.PreferencesSecurity.LastModifiedByScreenID : Edm.String
PX.SM.PreferencesSecurity.LastModifiedDateTime : Edm.DateTimeOffset
PX.SM.PreferencesSecurity.UsersByCreatedByID -> PX.SM.Users (CreatedByID=PKID)
PX.SM.PreferencesSecurity.UsersByLastModifiedByID -> PX.SM.Users (LastModifiedByID=PKID)
PX.SM.PreferencesSecurity.RolesByDefaultMenuEditorRole -> PX.SM.Roles (DefaultMenuEditorRole=Rolename)
PX.SM.PreferencesSecurity.CertificateByDBCertificateName -> PX.SM.Certificate (DBCertificateName=Name)
PX.SM.PreferencesSecurity.CertificateByPdfCertificateName -> PX.SM.Certificate (PdfCertificateName=Name)

# PX.SM.PushNotificationInProject (EntityType)

Label: "Push Notifications Hook"
BaseType: PX.PushNotifications.UI.DAC.PushNotificationsHook
Key: Name (inherited from PX.PushNotifications.UI.DAC.PushNotificationsHook)
Entity sets: PX_SM_PushNotificationInProject

PX.SM.PushNotificationInProject.CompanyID : Edm.Int32 "CompanyId"

# PX.SM.Reduced.UploadFile (EntityType)

Key: FileID
Entity sets: PX_SM_Reduced_UploadFile

PX.SM.Reduced.UploadFile.FileID : Edm.Guid [key] "File"
PX.SM.Reduced.UploadFile.PrimaryPageID : Edm.Guid
PX.SM.Reduced.UploadFile.UploadFileWithIDSelectorByName -> PX.SM.UploadFileWithIDSelector
PX.SM.Reduced.UploadFile.UsersByCreatedByID -> PX.SM.Users
PX.SM.Reduced.UploadFile.CertificateBySshCertificateName -> PX.SM.Certificate
PX.SM.Reduced.UploadFile.UploadFileWithIDSelectorCollection -> Collection(PX.SM.UploadFileWithIDSelector)

# PX.SM.Reduced.WikiFileInPage (EntityType)

Key: PageID
Entity sets: PX_SM_Reduced_WikiFileInPage

PX.SM.Reduced.WikiFileInPage.PageID : Edm.Guid [key]

# PX.SM.Reduced.WikiPage (EntityType)

Key: PageID
Entity sets: PX_SM_Reduced_WikiPage

PX.SM.Reduced.WikiPage.PageID : Edm.Guid [key] "PageID"
PX.SM.Reduced.WikiPage.UsersByCreatedByID -> PX.SM.Users
PX.SM.Reduced.WikiPage.WikiSitePageCollection -> Collection(PX.SM.WikiSitePage)
PX.SM.Reduced.WikiPage.WikiNotificationTemplateCollection -> Collection(PX.SM.WikiNotificationTemplate)
PX.SM.Reduced.WikiPage.WikiArticleCollection -> Collection(PX.SM.WikiArticle)
PX.SM.Reduced.WikiPage.PreferencesGeneralCollection -> Collection(PX.SM.PreferencesGeneral)
PX.SM.Reduced.WikiPage.KBResponseCollection -> Collection(PX.SM.KBResponse)
PX.SM.Reduced.WikiPage.KBResponseSummaryCollection -> Collection(PX.SM.KBResponseSummary)

# PX.SM.RelationDetail (EntityType)

Label: "Relation Detail"
BaseType: PX.SM.RelationGroup
Key: GroupName (inherited from PX.SM.RelationGroup)
Entity sets: PX_SM_RelationDetail, RelationDetail

# PX.SM.RelationGroup (EntityType)

Label: "Relation Group"
Key: GroupName
Entity sets: PX_SM_RelationGroup, RelationGroup
Non-filterable, non-selectable: Included

PX.SM.RelationGroup.GroupName : Edm.String [key] "Group Name"
PX.SM.RelationGroup.Description : Edm.String "Description"
PX.SM.RelationGroup.SpecificType : Edm.String "Specific Type"
PX.SM.RelationGroup.SpecificModule : Edm.String "Specific Module"
PX.SM.RelationGroup.GroupMask : Edm.Binary
PX.SM.RelationGroup.Active : Edm.Boolean [required] "Active"
PX.SM.RelationGroup.GroupType : Edm.String "Group Type"
PX.SM.RelationGroup.Included : Edm.Boolean "Included"
PX.SM.RelationGroup.EPEmployeeClassCollection -> Collection(PX.Objects.EP.EPEmployeeClass)
PX.SM.RelationGroup.VendorClassCollection -> Collection(PX.Objects.AP.VendorClass)
PX.SM.RelationGroup.CustomerClassCollection -> Collection(PX.Objects.AR.CustomerClass)

# PX.SM.RelationHeader (EntityType)

Label: "Relation Header"
BaseType: PX.SM.RelationGroup
Key: GroupName (inherited from PX.SM.RelationGroup)
Entity sets: PX_SM_RelationHeader, RelationHeader
Filterable: false (fields declared in this DAC cannot be used in $filter or $select; inherited ones can)

PX.SM.RelationHeader.EntityTypeName : Edm.String "Entity Type"

# PX.SM.ReportDefinitionInProject (EntityType)

Label: "Report"
BaseType: PX.CS.RMReport
Key: ReportCode (inherited from PX.CS.RMReport)
Entity sets: PX_SM_ReportDefinitionInProject

PX.SM.ReportDefinitionInProject.CompanyID : Edm.Int32 "CompanyId"

# PX.SM.ReportUsers (EntityType)

Label: "User"
BaseType: PX.SM.Users
Key: Username (inherited from PX.SM.Users)
Entity sets: PX_SM_ReportUsers
Filterable: false (fields declared in this DAC cannot be used in $filter or $select; inherited ones can)

PX.SM.ReportUsers.FriendlyName : Edm.String "Username"

# PX.SM.RoleActiveDirectory (EntityType)

Label: "Role Active Directory"
Key: GroupID, Role
Entity sets: PX_SM_RoleActiveDirectory, RoleActiveDirectory
Non-filterable, non-selectable: GroupName, GroupDomain, GroupDescription

PX.SM.RoleActiveDirectory.Role : Edm.String [key]
PX.SM.RoleActiveDirectory.GroupID : Edm.String [key] "Group ID"
PX.SM.RoleActiveDirectory.GroupName : Edm.String "Name"
PX.SM.RoleActiveDirectory.GroupDomain : Edm.String "Domain"
PX.SM.RoleActiveDirectory.GroupDescription : Edm.String "Description"
PX.SM.RoleActiveDirectory.RolesByRole -> PX.SM.Roles (Role=Rolename)

# PX.SM.RoleClaims (EntityType)

Label: "Role Claims"
Key: GroupID, Role
Entity sets: PX_SM_RoleClaims, RoleClaims

PX.SM.RoleClaims.Role : Edm.String [key]
PX.SM.RoleClaims.GroupID : Edm.String [key] "Group ID"
PX.SM.RoleClaims.RolesByRole -> PX.SM.Roles (Role=Rolename)

# PX.SM.Roles (EntityType)

Label: "Role"
Key: ApplicationName, Rolename
Entity sets: PX_SM_Roles, Role, Roles

PX.SM.Roles.ApplicationName : Edm.String [key required] "ApplicationName"
PX.SM.Roles.Rolename : Edm.String [key] "Role Name"
PX.SM.Roles.Descr : Edm.String "Role Description"
PX.SM.Roles.Guest : Edm.Boolean [required] "Guest Role"
PX.SM.Roles.CreatedByID : Edm.Guid "Created By"
PX.SM.Roles.CreatedByScreenID : Edm.String
PX.SM.Roles.CreatedDateTime : Edm.DateTimeOffset
PX.SM.Roles.LastModifiedByID : Edm.Guid "Last Modified By"
PX.SM.Roles.LastModifiedByScreenID : Edm.String
PX.SM.Roles.LastModifiedDateTime : Edm.DateTimeOffset
PX.SM.Roles.UsersByCreatedByID -> PX.SM.Users (CreatedByID=PKID)
PX.SM.Roles.UsersByLastModifiedByID -> PX.SM.Users (LastModifiedByID=PKID)
PX.SM.Roles.DashboardCollection -> Collection(PX.Dashboards.DAC.Dashboard)
PX.SM.Roles.DashboardV2Collection -> Collection(PX.Dashboards.DAC.DashboardV2)
PX.SM.Roles.OrganizationCollection -> Collection(PX.Objects.GL.DAC.Organization)
PX.SM.Roles.RolesInGraphCollection -> Collection(PX.SM.RolesInGraph)
PX.SM.Roles.RolesInCacheCollection -> Collection(PX.SM.RolesInCache)
PX.SM.Roles.RolesInMemberCollection -> Collection(PX.SM.RolesInMember)
PX.SM.Roles.SPPortalCollection -> Collection(PX.Objects.Portals.SPPortal)
PX.SM.Roles.WikiAccessRightsCollection -> Collection(PX.SM.WikiAccessRights)
PX.SM.Roles.BranchCollection -> Collection(PX.Objects.GL.Branch)
PX.SM.Roles.EPLoginTypeAllowsRoleCollection -> Collection(PX.EP.EPLoginTypeAllowsRole)
PX.SM.Roles.PreferencesSecurityCollection -> Collection(PX.SM.PreferencesSecurity)
PX.SM.Roles.UsersInRolesCollection -> Collection(PX.SM.UsersInRoles)
PX.SM.Roles.RoleInTagCollection -> Collection(PX.Data.Wiki.Tags.RoleInTag)
PX.SM.Roles.PRPayGroupCollection -> Collection(PX.Objects.PR.PRPayGroup)
PX.SM.Roles.RoleActiveDirectoryCollection -> Collection(PX.SM.RoleActiveDirectory)
PX.SM.Roles.RoleClaimsCollection -> Collection(PX.SM.RoleClaims)

# PX.SM.RolesInCache (EntityType)

Label: "Roles In Cache"
Key: ApplicationName, Cachetype, Rolename, ScreenID
Entity sets: PX_SM_RolesInCache, RolesInCache

PX.SM.RolesInCache.ScreenID : Edm.String [key]
PX.SM.RolesInCache.Cachetype : Edm.String [key]
PX.SM.RolesInCache.Rolename : Edm.String [key]
PX.SM.RolesInCache.ApplicationName : Edm.String [key]
PX.SM.RolesInCache.Accessrights : Edm.Int16 [required]
PX.SM.RolesInCache.CreatedByID : Edm.Guid "Created By"
PX.SM.RolesInCache.CreatedByScreenID : Edm.String
PX.SM.RolesInCache.CreatedDateTime : Edm.DateTimeOffset
PX.SM.RolesInCache.LastModifiedByID : Edm.Guid "Last Modified By"
PX.SM.RolesInCache.LastModifiedByScreenID : Edm.String
PX.SM.RolesInCache.LastModifiedDateTime : Edm.DateTimeOffset
PX.SM.RolesInCache.SiteMapByScreenID -> PX.SM.SiteMap (ScreenID=ScreenID)
PX.SM.RolesInCache.UsersByCreatedByID -> PX.SM.Users (CreatedByID=PKID)
PX.SM.RolesInCache.UsersByLastModifiedByID -> PX.SM.Users (LastModifiedByID=PKID)
PX.SM.RolesInCache.RolesByRolename -> PX.SM.Roles (ApplicationName=ApplicationName, Rolename=Rolename)

# PX.SM.RolesInGraph (EntityType)

Label: "Roles In Graph"
Key: ApplicationName, Rolename, ScreenID
Entity sets: PX_SM_RolesInGraph, RolesInGraph

PX.SM.RolesInGraph.ScreenID : Edm.String [key]
PX.SM.RolesInGraph.Rolename : Edm.String [key]
PX.SM.RolesInGraph.ApplicationName : Edm.String [key]
PX.SM.RolesInGraph.Accessrights : Edm.Int16 [required]
PX.SM.RolesInGraph.CreatedByID : Edm.Guid "Created By"
PX.SM.RolesInGraph.CreatedByScreenID : Edm.String
PX.SM.RolesInGraph.CreatedDateTime : Edm.DateTimeOffset
PX.SM.RolesInGraph.LastModifiedByID : Edm.Guid "Last Modified By"
PX.SM.RolesInGraph.LastModifiedByScreenID : Edm.String
PX.SM.RolesInGraph.LastModifiedDateTime : Edm.DateTimeOffset
PX.SM.RolesInGraph.SiteMapByScreenID -> PX.SM.SiteMap (ScreenID=ScreenID)
PX.SM.RolesInGraph.UsersByCreatedByID -> PX.SM.Users (CreatedByID=PKID)
PX.SM.RolesInGraph.UsersByLastModifiedByID -> PX.SM.Users (LastModifiedByID=PKID)
PX.SM.RolesInGraph.RolesByRolename -> PX.SM.Roles (ApplicationName=ApplicationName, Rolename=Rolename)

# PX.SM.RolesInMember (EntityType)

Label: "Roles In Member"
Key: ApplicationName, Cachetype, Membername, Rolename, ScreenID
Entity sets: PX_SM_RolesInMember, RolesInMember

PX.SM.RolesInMember.ScreenID : Edm.String [key]
PX.SM.RolesInMember.Cachetype : Edm.String [key]
PX.SM.RolesInMember.Membername : Edm.String [key]
PX.SM.RolesInMember.Rolename : Edm.String [key]
PX.SM.RolesInMember.ApplicationName : Edm.String [key]
PX.SM.RolesInMember.Accessrights : Edm.Int16 [required]
PX.SM.RolesInMember.CreatedByID : Edm.Guid "Created By"
PX.SM.RolesInMember.CreatedByScreenID : Edm.String
PX.SM.RolesInMember.CreatedDateTime : Edm.DateTimeOffset
PX.SM.RolesInMember.LastModifiedByID : Edm.Guid "Last Modified By"
PX.SM.RolesInMember.LastModifiedByScreenID : Edm.String
PX.SM.RolesInMember.LastModifiedDateTime : Edm.DateTimeOffset
PX.SM.RolesInMember.SiteMapByScreenID -> PX.SM.SiteMap (ScreenID=ScreenID)
PX.SM.RolesInMember.UsersByCreatedByID -> PX.SM.Users (CreatedByID=PKID)
PX.SM.RolesInMember.UsersByLastModifiedByID -> PX.SM.Users (LastModifiedByID=PKID)
PX.SM.RolesInMember.RolesByRolename -> PX.SM.Roles (ApplicationName=ApplicationName, Rolename=Rolename)

# PX.SM.RowCodeFile (EntityType)

BaseType: PX.SM.CustObject
Key: ObjectID (inherited from PX.SM.CustObject)
Entity sets: PX_SM_RowCodeFile
Filterable: false (fields declared in this DAC cannot be used in $filter or $select; inherited ones can)

PX.SM.RowCodeFile.FileContent : Edm.String "Code File"

# PX.SM.RowMobileSiteMap (EntityType)

BaseType: PX.SM.CustObject
Key: ObjectID (inherited from PX.SM.CustObject)
Entity sets: PX_SM_RowMobileSiteMap
Filterable: false (fields declared in this DAC cannot be used in $filter or $select; inherited ones can)

PX.SM.RowMobileSiteMap.Script : Edm.String "Script"
PX.SM.RowMobileSiteMap.Errors : Edm.String "Errors"
PX.SM.RowMobileSiteMap.PreviewResult : Edm.String "PreviewResult"

# PX.SM.ScreensInUserField (EntityType)

Key: AttributeID, ScreenID, TypeValue
Entity sets: PX_SM_ScreensInUserField
Non-filterable, non-selectable: NoteText, TypeValueDesc

PX.SM.ScreensInUserField.AttributeID : Edm.String [key] "Attribute ID"
PX.SM.ScreensInUserField.ScreenID : Edm.String [key] "Screen ID"
PX.SM.ScreensInUserField.Column : Edm.Int16
PX.SM.ScreensInUserField.Row : Edm.Int16
PX.SM.ScreensInUserField.NoteID : Edm.Guid
PX.SM.ScreensInUserField.NoteText : Edm.String "Note Text"
PX.SM.ScreensInUserField.TypeValue : Edm.String [key]
PX.SM.ScreensInUserField.Hidden : Edm.Boolean "Hidden"
PX.SM.ScreensInUserField.Required : Edm.Boolean "Required"
PX.SM.ScreensInUserField.DefaultValue : Edm.String "Default Value"
PX.SM.ScreensInUserField.tstamp : Edm.Binary
PX.SM.ScreensInUserField.CreatedByID : Edm.Guid "Created By"
PX.SM.ScreensInUserField.CreatedByScreenID : Edm.String
PX.SM.ScreensInUserField.CreatedDateTime : Edm.DateTimeOffset
PX.SM.ScreensInUserField.LastModifiedByID : Edm.Guid "Last Modified By"
PX.SM.ScreensInUserField.LastModifiedByScreenID : Edm.String
PX.SM.ScreensInUserField.LastModifiedDateTime : Edm.DateTimeOffset
PX.SM.ScreensInUserField.CompanyID : Edm.Int32 "CompanyId"
PX.SM.ScreensInUserField.TypeValueDesc : Edm.String "Entity Type"

# PX.SM.SelectedFilter (EntityType)

Label: "Filter Header"
BaseType: PX.Data.FilterHeader
Key: FilterID, ScreenID, ViewName (inherited from PX.Data.FilterHeader)
Entity sets: PX_SM_SelectedFilter

PX.SM.SelectedFilter.CompanyID : Edm.Int32 "CompanyID"

# PX.SM.SelectedImportScenario (EntityType)

Label: "Mapping"
BaseType: PX.Api.SYMapping
Key: Name (inherited from PX.Api.SYMapping)
Entity sets: PX_SM_SelectedImportScenario

PX.SM.SelectedImportScenario.CompanyID : Edm.Int32 "CompanyId"

# PX.SM.SelectedLocale (EntityType)

Label: "Locale"
BaseType: PX.SM.Locale
Key: LocaleName (inherited from PX.SM.Locale)
Entity sets: PX_SM_SelectedLocale

# PX.SM.SimpleWikiPage (EntityType)

BaseType: PX.SM.WikiPage
Key: PageID (inherited from PX.SM.WikiPage)
Entity sets: PX_SM_SimpleWikiPage

# PX.SM.SiteMap (EntityType)

Label: "Site Map"
Key: NodeID
Entity sets: PX_SM_SiteMap, SiteMap
Non-filterable, non-selectable: Graphtype, WorkspaceNames

PX.SM.SiteMap.NodeID : Edm.Guid [key] "Node ID"
PX.SM.SiteMap.Position : Edm.Double
PX.SM.SiteMap.Title : Edm.String "Title"
PX.SM.SiteMap.Url : Edm.String "URL"
PX.SM.SiteMap.UrlBackup : Edm.String
PX.SM.SiteMap.SelectedUI : Edm.String "UI"
PX.SM.SiteMap.ScreenID : Edm.String "Screen ID"
PX.SM.SiteMap.Graphtype : Edm.String "Graph Type"
PX.SM.SiteMap.ParentID : Edm.Guid
PX.SM.SiteMap.CreatedByID : Edm.Guid "Created By"
PX.SM.SiteMap.CreatedByScreenID : Edm.String
PX.SM.SiteMap.CreatedDateTime : Edm.DateTimeOffset
PX.SM.SiteMap.LastModifiedByID : Edm.Guid "Last Modified By"
PX.SM.SiteMap.LastModifiedByScreenID : Edm.String
PX.SM.SiteMap.LastModifiedDateTime : Edm.DateTimeOffset "Last Modified On"
PX.SM.SiteMap.WorkspaceNames : Edm.String "Workspaces"
PX.SM.SiteMap.UsersByCreatedByID -> PX.SM.Users (CreatedByID=PKID)
PX.SM.SiteMap.UsersByLastModifiedByID -> PX.SM.Users (LastModifiedByID=PKID)
PX.SM.SiteMap.MUITileCollection -> Collection(PX.Web.UI.Frameset.Model.DAC.MUITile)
PX.SM.SiteMap.BPEventCollection -> Collection(PX.BusinessProcess.DAC.BPEvent)
PX.SM.SiteMap.DashboardCollection -> Collection(PX.Dashboards.DAC.Dashboard)
PX.SM.SiteMap.GIDesignCollection -> Collection(PX.Data.Maintenance.GI.GIDesign)
PX.SM.SiteMap.SYMappingCollection -> Collection(PX.Api.SYMapping)
PX.SM.SiteMap.AUScheduleCollection -> Collection(PX.SM.AUSchedule)
PX.SM.SiteMap.MUIAreaCollection -> Collection(PX.Web.UI.Frameset.Model.DAC.MUIArea)
PX.SM.SiteMap.RolesInGraphCollection -> Collection(PX.SM.RolesInGraph)
PX.SM.SiteMap.RolesInCacheCollection -> Collection(PX.SM.RolesInCache)
PX.SM.SiteMap.RolesInMemberCollection -> Collection(PX.SM.RolesInMember)
PX.SM.SiteMap.ActionExecutionCollection -> Collection(PX.BusinessProcess.DAC.ActionExecution)
PX.SM.SiteMap.AUScheduleFillCollection -> Collection(PX.SM.AUScheduleFill)
PX.SM.SiteMap.AUScheduleFilterCollection -> Collection(PX.SM.AUScheduleFilter)
PX.SM.SiteMap.ListEntryPointCollection -> Collection(PX.Data.ListEntryPoint)
PX.SM.SiteMap.MobileNotificationCollection -> Collection(PX.BusinessProcess.DAC.MobileNotification)
PX.SM.SiteMap.SMTeamsNotificationCollection -> Collection(PX.MSTeams.DAC.SM.SMTeamsNotification)
PX.SM.SiteMap.PivotFieldCollection -> Collection(PX.Olap.Maintenance.PivotField)
PX.SM.SiteMap.PivotTableCollection -> Collection(PX.Olap.Maintenance.PivotTable)
PX.SM.SiteMap.FilterHeaderCollection -> Collection(PX.Data.FilterHeader)
PX.SM.SiteMap.NotificationReportCollection -> Collection(PX.SM.NotificationReport)
PX.SM.SiteMap.LoginTraceCollection -> Collection(PX.SM.LoginTrace)
PX.SM.SiteMap.AIGIToolDefinitionCollection -> Collection(PX.AI.Tools.GI.DAC.AIGIToolDefinition)
PX.SM.SiteMap.PivotFieldPreferencesCollection -> Collection(PX.Olap.Maintenance.PivotFieldPreferences)
PX.SM.SiteMap.UploadFileWithIDSelectorCollection -> Collection(PX.SM.UploadFileWithIDSelector)
PX.SM.SiteMap.NotificationSetupCollection -> Collection(PX.Objects.CS.NotificationSetup)
PX.SM.SiteMap.PaymentMethodCollection -> Collection(PX.Objects.CA.PaymentMethod)
PX.SM.SiteMap.POReceivePutAwaySetupCollection -> Collection(PX.Objects.PO.POReceivePutAwaySetup)
PX.SM.SiteMap.INScanSetupCollection -> Collection(PX.Objects.IN.INScanSetup)
PX.SM.SiteMap.INScanUserSetupCollection -> Collection(PX.Objects.IN.INScanUserSetup)
PX.SM.SiteMap.AMOrderTypeCollection -> Collection(PX.Objects.AM.AMOrderType)
PX.SM.SiteMap.FSWrkProcessCollection -> Collection(PX.Objects.FS.FSWrkProcess)
PX.SM.SiteMap.POReceivePutAwayUserSetupCollection -> Collection(PX.Objects.PO.POReceivePutAwayUserSetup)

# PX.SM.SiteMapEx (EntityType)

Label: "Site Map"
BaseType: PX.SM.SiteMap
Key: NodeID (inherited from PX.SM.SiteMap)
Entity sets: PX_SM_SiteMapEx

PX.SM.SiteMapEx.CompanyId : Edm.Int32 "CompanyId"

# PX.SM.SiteMapInProject (EntityType)

Label: "Site Map"
BaseType: PX.SM.SiteMap
Key: NodeID (inherited from PX.SM.SiteMap)
Entity sets: PX_SM_SiteMapInProject

PX.SM.SiteMapInProject.CompanyID : Edm.Int32 "CompanyId"

# PX.SM.SMCalendarSettings (EntityType)

Label: "Calendar Settings"
Key: PKID
Entity sets: PX_SM_SMCalendarSettings, CalendarSettings, SMCalendarSettings

PX.SM.SMCalendarSettings.PKID : Edm.Int32 [key]
PX.SM.SMCalendarSettings.UserID : Edm.Guid
PX.SM.SMCalendarSettings.UrlGuid : Edm.Guid
PX.SM.SMCalendarSettings.IsPublic : Edm.Boolean [required] "Make My Calendar Public"
PX.SM.SMCalendarSettings.tstamp : Edm.Binary
PX.SM.SMCalendarSettings.CreatedByID : Edm.Guid "Created By"
PX.SM.SMCalendarSettings.CreatedByScreenID : Edm.String
PX.SM.SMCalendarSettings.CreatedDateTime : Edm.DateTimeOffset
PX.SM.SMCalendarSettings.LastModifiedByID : Edm.Guid "Last Modified By"
PX.SM.SMCalendarSettings.LastModifiedByScreenID : Edm.String
PX.SM.SMCalendarSettings.LastModifiedDateTime : Edm.DateTimeOffset
PX.SM.SMCalendarSettings.UsersByCreatedByID -> PX.SM.Users (CreatedByID=PKID)
PX.SM.SMCalendarSettings.UsersByLastModifiedByID -> PX.SM.Users (LastModifiedByID=PKID)

# PX.SM.SMPerformanceInfo (EntityType)

Label: "Performance Info"
Key: RecordId
Entity sets: PX_SM_SMPerformanceInfo, PerformanceInfo, SMPerformanceInfo
Non-filterable, non-selectable: UrlToScreen, IsPinned, ID, NoteText

PX.SM.SMPerformanceInfo.RecordId : Edm.Int32 [key]
PX.SM.SMPerformanceInfo.RequestStartTime : Edm.DateTimeOffset "Request Start Time"
PX.SM.SMPerformanceInfo.ScreenId : Edm.String "URL"
PX.SM.SMPerformanceInfo.CommandTarget : Edm.String "Command Target"
PX.SM.SMPerformanceInfo.CommandName : Edm.String "Command Name"
PX.SM.SMPerformanceInfo.RequestTimeMs : Edm.Double "Server Time, ms"
PX.SM.SMPerformanceInfo.RequestCpuTimeMs : Edm.Double "Server CPU, ms"
PX.SM.SMPerformanceInfo.SqlCounter : Edm.Int32 "SQL Count"
PX.SM.SMPerformanceInfo.SqlTimeMs : Edm.Double "SQL Time, ms"
PX.SM.SMPerformanceInfo.SelectCounter : Edm.Int32 "Select Count"
PX.SM.SMPerformanceInfo.SelectTimeMs : Edm.Double "Select Time, ms"
PX.SM.SMPerformanceInfo.UserId : Edm.String "Username"
PX.SM.SMPerformanceInfo.MemBefore : Edm.Int64 "Managed Memory Bytes"
PX.SM.SMPerformanceInfo.MemDelta : Edm.Int64 "Peak Memory Bytes"
PX.SM.SMPerformanceInfo.MemBeforeMb : Edm.Double "Managed Memory"
PX.SM.SMPerformanceInfo.MemDeltaMb : Edm.Double "Peak Memory"
PX.SM.SMPerformanceInfo.MemoryWorkingSet : Edm.Double "Memory Working Set"
PX.SM.SMPerformanceInfo.ScriptTimeMs : Edm.Int32 "Client Time"
PX.SM.SMPerformanceInfo.SessionLoadTimeMs : Edm.Double "Session Load Time, ms"
PX.SM.SMPerformanceInfo.SessionSaveTimeMs : Edm.Double "Session Save Time, ms"
PX.SM.SMPerformanceInfo.Headers : Edm.String "Headers"
PX.SM.SMPerformanceInfo.InstallationId : Edm.String "Installation ID"
PX.SM.SMPerformanceInfo.SqlDigest : Edm.String "SQL Digest"
PX.SM.SMPerformanceInfo.TenantId : Edm.String "Tenant"
PX.SM.SMPerformanceInfo.InternalScreenId : Edm.String "Screen"
PX.SM.SMPerformanceInfo.UrlToScreen : Edm.String "Screen"
PX.SM.SMPerformanceInfo.ProcessingItems : Edm.Int32 "Items to Process"
PX.SM.SMPerformanceInfo.RequestType : Edm.String "Request Type"
PX.SM.SMPerformanceInfo.Status : Edm.Int32 "Status"
PX.SM.SMPerformanceInfo.ExceptionCounter : Edm.Int32 "Exceptions Count"
PX.SM.SMPerformanceInfo.EventCounter : Edm.Int32 "Events Count"
PX.SM.SMPerformanceInfo.SqlRows : Edm.Int32 "SQL Rows"
PX.SM.SMPerformanceInfo.WaitTime : Edm.Double "Wait Time"
PX.SM.SMPerformanceInfo.IsChecked : Edm.Boolean
PX.SM.SMPerformanceInfo.IsPinned : Edm.String "Is Pinned"
PX.SM.SMPerformanceInfo.LoggedSqlCounter : Edm.Int32 "Logged SQL Count"
PX.SM.SMPerformanceInfo.LoggedExceptionCounter : Edm.Int32 "Logged Exceptions Count"
PX.SM.SMPerformanceInfo.LoggedEventCounter : Edm.Int32 "Logged Events Count"
PX.SM.SMPerformanceInfo.ID : Edm.String
PX.SM.SMPerformanceInfo.NoteID : Edm.Guid
PX.SM.SMPerformanceInfo.NoteText : Edm.String "Note Text"
PX.SM.SMPerformanceInfo.HttpMethod : Edm.String "HTTP Method"
PX.SM.SMPerformanceInfo.HttpStatusCode : Edm.Int32 "HTTP Status Code"
PX.SM.SMPerformanceInfo.ExceptionMessage : Edm.String "Exception Message"
PX.SM.SMPerformanceInfo.Throttled : Edm.Boolean [required] "Throttled"
PX.SM.SMPerformanceInfo.SMPerformanceInfoSQLCollection -> Collection(PX.SM.SMPerformanceInfoSQL)
PX.SM.SMPerformanceInfo.SMPerformanceInfoTraceEventsCollection -> Collection(PX.SM.SMPerformanceInfoTraceEvents)

# PX.SM.SMPerformanceInfoSQL (EntityType)

Key: ParentId, RecordId
Entity sets: PX_SM_SMPerformanceInfoSQL

PX.SM.SMPerformanceInfoSQL.ParentId : Edm.Int32 [key]
PX.SM.SMPerformanceInfoSQL.RecordId : Edm.Int32 [key] "Query ID"
PX.SM.SMPerformanceInfoSQL.RequestStartTime : Edm.Double "Start Time"
PX.SM.SMPerformanceInfoSQL.SqlTimeMs : Edm.Double "SQL Time, ms"
PX.SM.SMPerformanceInfoSQL.NRows : Edm.Int32 "Row Count"
PX.SM.SMPerformanceInfoSQL.SqlId : Edm.Int32 "Statement ID"
PX.SM.SMPerformanceInfoSQL.StackTraceId : Edm.Int32 "TraceID"
PX.SM.SMPerformanceInfoSQL.SQLParams : Edm.String "Params"
PX.SM.SMPerformanceInfoSQL.RequestDateTime : Edm.DateTimeOffset "Start Time"
PX.SM.SMPerformanceInfoSQL.QueryCache : Edm.Boolean "From Cache"
PX.SM.SMPerformanceInfoSQL.SMPerformanceInfoByParentId -> PX.SM.SMPerformanceInfo (ParentId=RecordId)

# PX.SM.SMPerformanceInfoSQLText (EntityType)

Label: "SQL Text Performance Info"
Key: RecordId
Entity sets: PX_SM_SMPerformanceInfoSQLText, SQLTextPerformanceInfo, SMPerformanceInfoSQLText

PX.SM.SMPerformanceInfoSQLText.RecordId : Edm.Int32 [key]
PX.SM.SMPerformanceInfoSQLText.SQLText : Edm.String "SQL"
PX.SM.SMPerformanceInfoSQLText.SQLHash : Edm.String "Query Hash"
PX.SM.SMPerformanceInfoSQLText.TableList : Edm.String "Tables"
PX.SM.SMPerformanceInfoSQLText.QueryOrderId : Edm.Int32 "Query ID"

# PX.SM.SMPerformanceInfoSQLWithTables (EntityType)

Label: "SQL With Tables Performance Info"
BaseType: PX.SM.SMPerformanceInfoSQL
Key: ParentId, RecordId (inherited from PX.SM.SMPerformanceInfoSQL)
Entity sets: PX_SM_SMPerformanceInfoSQLWithTables, SQLWithTablesPerformanceInfo, SMPerformanceInfoSQLWithTables
Non-filterable, non-selectable: SQLWithStackTrace, SQLWithParams, ShortParams

PX.SM.SMPerformanceInfoSQLWithTables.TableList : Edm.String "Tables"
PX.SM.SMPerformanceInfoSQLWithTables.QueryOrderId : Edm.Int32 "Order"
PX.SM.SMPerformanceInfoSQLWithTables.SQLHash : Edm.String "Query Hash"
PX.SM.SMPerformanceInfoSQLWithTables.SQLText : Edm.String "SQL"
PX.SM.SMPerformanceInfoSQLWithTables.SQLWithStackTrace : Edm.String "SQL"
PX.SM.SMPerformanceInfoSQLWithTables.SQLWithParams : Edm.String "Query"
PX.SM.SMPerformanceInfoSQLWithTables.StackTrace : Edm.String "Stack Trace"
PX.SM.SMPerformanceInfoSQLWithTables.ShortParams : Edm.String "Parameters"

# PX.SM.SMPerformanceInfoStackTrace (EntityType)

Label: "Stack Trace Performance Info"
Key: RecordId
Entity sets: PX_SM_SMPerformanceInfoStackTrace, StackTracePerformanceInfo, SMPerformanceInfoStackTrace

PX.SM.SMPerformanceInfoStackTrace.RecordId : Edm.Int32 [key]
PX.SM.SMPerformanceInfoStackTrace.StackTrace : Edm.String "Stack Trace"
PX.SM.SMPerformanceInfoStackTrace.SMPerformanceInfoTraceEventsCollection -> Collection(PX.SM.SMPerformanceInfoTraceEvents)

# PX.SM.SMPerformanceInfoTraceEvents (EntityType)

Label: "Trace Events Performance Info"
Key: ParentId, RecordId
Entity sets: PX_SM_SMPerformanceInfoTraceEvents, TraceEventsPerformanceInfo, SMPerformanceInfoTraceEvents

PX.SM.SMPerformanceInfoTraceEvents.ParentId : Edm.Int32 [key]
PX.SM.SMPerformanceInfoTraceEvents.RecordId : Edm.Int32 [key]
PX.SM.SMPerformanceInfoTraceEvents.RequestStartTime : Edm.Double "Start Time"
PX.SM.SMPerformanceInfoTraceEvents.TraceMessageId : Edm.Int32 "TraceID"
PX.SM.SMPerformanceInfoTraceEvents.Source : Edm.String "Source"
PX.SM.SMPerformanceInfoTraceEvents.TraceType : Edm.String "Log Level"
PX.SM.SMPerformanceInfoTraceEvents.StackTraceId : Edm.Int32 "TraceID"
PX.SM.SMPerformanceInfoTraceEvents.EventDateTime : Edm.DateTimeOffset "Start Time"
PX.SM.SMPerformanceInfoTraceEvents.ExceptionType : Edm.String "Exception Type"
PX.SM.SMPerformanceInfoTraceEvents.EventDetails : Edm.String "Event Details"
PX.SM.SMPerformanceInfoTraceEvents.Category : Edm.String "Category"
PX.SM.SMPerformanceInfoTraceEvents.RequestBody : Edm.String "Request Body"
PX.SM.SMPerformanceInfoTraceEvents.ResponseBody : Edm.String "Response Body"
PX.SM.SMPerformanceInfoTraceEvents.SMPerformanceInfoByParentId -> PX.SM.SMPerformanceInfo (ParentId=RecordId)
PX.SM.SMPerformanceInfoTraceEvents.SMPerformanceInfoTraceMessagesByTraceMessageId -> PX.SM.SMPerformanceInfoTraceMessages (TraceMessageId=RecordId)
PX.SM.SMPerformanceInfoTraceEvents.SMPerformanceInfoStackTraceByStackTraceId -> PX.SM.SMPerformanceInfoStackTrace (StackTraceId=RecordId)

# PX.SM.SMPerformanceInfoTraceMessages (EntityType)

Label: "Trace Messages Performance Info"
Key: RecordId
Entity sets: PX_SM_SMPerformanceInfoTraceMessages, TraceMessagesPerformanceInfo, SMPerformanceInfoTraceMessages

PX.SM.SMPerformanceInfoTraceMessages.RecordId : Edm.Int32 [key]
PX.SM.SMPerformanceInfoTraceMessages.MessageText : Edm.String "Message"
PX.SM.SMPerformanceInfoTraceMessages.SMPerformanceInfoTraceEventsCollection -> Collection(PX.SM.SMPerformanceInfoTraceEvents)

# PX.SM.SMPerformanceInfoTraceWithMessages (EntityType)

Label: "Trace Events Performance Info"
BaseType: PX.SM.SMPerformanceInfoTraceEvents
Key: ParentId, RecordId (inherited from PX.SM.SMPerformanceInfoTraceEvents)
Entity sets: PX_SM_SMPerformanceInfoTraceWithMessages
Non-filterable, non-selectable: MessageWithStackTrace, ShortMessage, HttpMethod, HttpStatusCode

PX.SM.SMPerformanceInfoTraceWithMessages.MessageText : Edm.String "Message"
PX.SM.SMPerformanceInfoTraceWithMessages.StackTrace : Edm.String "Stack Trace"
PX.SM.SMPerformanceInfoTraceWithMessages.MessageWithStackTrace : Edm.String "Message"
PX.SM.SMPerformanceInfoTraceWithMessages.ShortMessage : Edm.String "Message"
PX.SM.SMPerformanceInfoTraceWithMessages.HttpMethod : Edm.String "HTTP Method"
PX.SM.SMPerformanceInfoTraceWithMessages.HttpStatusCode : Edm.Int32 "HTTP Status Code"

# PX.SM.SMPrinter (EntityType)

Label: "Printers"
Key: DeviceHubID, PrinterName
Entity sets: PX_SM_SMPrinter, Printers, SMPrinter
Non-filterable, non-selectable: NoteText, Included, Secured

PX.SM.SMPrinter.PrinterID : Edm.Guid
PX.SM.SMPrinter.DeviceHubID : Edm.String [key] "DeviceHub ID"
PX.SM.SMPrinter.PrinterName : Edm.String [key] "Printer"
PX.SM.SMPrinter.Description : Edm.String "Description"
PX.SM.SMPrinter.DefaultNumberOfCopies : Edm.Int32 [required] "Default Number of Copies"
PX.SM.SMPrinter.IsActive : Edm.Boolean "Active"
PX.SM.SMPrinter.CreatedByID : Edm.Guid "Created By"
PX.SM.SMPrinter.CreatedByScreenID : Edm.String
PX.SM.SMPrinter.CreatedDateTime : Edm.DateTimeOffset
PX.SM.SMPrinter.LastModifiedByID : Edm.Guid "Last Modified By"
PX.SM.SMPrinter.LastModifiedByScreenID : Edm.String
PX.SM.SMPrinter.LastModifiedDateTime : Edm.DateTimeOffset
PX.SM.SMPrinter.tstamp : Edm.Binary
PX.SM.SMPrinter.NoteID : Edm.Guid
PX.SM.SMPrinter.NoteText : Edm.String "Note Text"
PX.SM.SMPrinter.Included : Edm.Boolean "Included"
PX.SM.SMPrinter.Secured : Edm.Boolean "Secured"
PX.SM.SMPrinter.UsersByCreatedByID -> PX.SM.Users (CreatedByID=PKID)
PX.SM.SMPrinter.UsersByLastModifiedByID -> PX.SM.Users (LastModifiedByID=PKID)
PX.SM.SMPrinter.NotificationSetupCollection -> Collection(PX.Objects.CS.NotificationSetup)
PX.SM.SMPrinter.OrganizationCollection -> Collection(PX.Objects.GL.DAC.Organization)
PX.SM.SMPrinter.UserPreferencesCollection -> Collection(PX.SM.UserPreferences)
PX.SM.SMPrinter.BranchCollection -> Collection(PX.Objects.GL.Branch)
PX.SM.SMPrinter.SOQuickProcessParametersCollection -> Collection(PX.Objects.SO.SOQuickProcessParameters)
PX.SM.SMPrinter.SMPrintJobCollection -> Collection(PX.SM.SMPrintJob)
PX.SM.SMPrinter.NotificationSetupUserOverrideCollection -> Collection(PX.Objects.CS.NotificationSetupUserOverride)

# PX.SM.SMPrintJob (EntityType)

Label: "Print Job"
Key: JobID
Entity sets: PX_SM_SMPrintJob, PrintJob, SMPrintJob
Non-filterable, non-selectable: NoteText

PX.SM.SMPrintJob.JobID : Edm.Int32 [key] "Job ID"
PX.SM.SMPrintJob.GroupID : Edm.Guid
PX.SM.SMPrintJob.Description : Edm.String
PX.SM.SMPrintJob.DeviceHubID : Edm.String "DeviceHub ID"
PX.SM.SMPrintJob.PrinterName : Edm.String "Printer"
PX.SM.SMPrintJob.NumberOfCopies : Edm.Int32 [required] "Number of Copies"
PX.SM.SMPrintJob.ReportID : Edm.String "Report ID"
PX.SM.SMPrintJob.Status : Edm.String "Status"
PX.SM.SMPrintJob.Error : Edm.String "Error"
PX.SM.SMPrintJob.ErrorTrace : Edm.String "Error Trace"
PX.SM.SMPrintJob.CreatedByID : Edm.Guid "Created By"
PX.SM.SMPrintJob.CreatedByScreenID : Edm.String
PX.SM.SMPrintJob.CreatedDateTime : Edm.DateTimeOffset "Creation Date and Time"
PX.SM.SMPrintJob.LastModifiedByID : Edm.Guid "Last Modified By"
PX.SM.SMPrintJob.LastModifiedByScreenID : Edm.String
PX.SM.SMPrintJob.LastModifiedDateTime : Edm.DateTimeOffset
PX.SM.SMPrintJob.tstamp : Edm.Binary
PX.SM.SMPrintJob.NoteID : Edm.Guid
PX.SM.SMPrintJob.NoteText : Edm.String "Note Text"
PX.SM.SMPrintJob.UsersByCreatedByID -> PX.SM.Users (CreatedByID=PKID)
PX.SM.SMPrintJob.UsersByLastModifiedByID -> PX.SM.Users (LastModifiedByID=PKID)
PX.SM.SMPrintJob.SMPrinterByDeviceHubID -> PX.SM.SMPrinter (PrinterName=PrinterName, DeviceHubID=DeviceHubID)
PX.SM.SMPrintJob.SMPrintJobParameterCollection -> Collection(PX.SM.SMPrintJobParameter)

# PX.SM.SMPrintJobParameter (EntityType)

Label: "Print Job Parameter"
Key: JobID, ParameterName
Entity sets: PX_SM_SMPrintJobParameter, PrintJobParameter, SMPrintJobParameter

PX.SM.SMPrintJobParameter.JobID : Edm.Int32 [key] "Job ID"
PX.SM.SMPrintJobParameter.ParameterName : Edm.String [key] "Parameter Name"
PX.SM.SMPrintJobParameter.ParameterValue : Edm.String "Parameter Value"
PX.SM.SMPrintJobParameter.SMPrintJobByJobID -> PX.SM.SMPrintJob (JobID=JobID)

# PX.SM.SMScale (EntityType)

Label: "Scale"
Key: DeviceHubID, ScaleID
Entity sets: PX_SM_SMScale, Scale, SMScale
Non-filterable, non-selectable: CompanyUOM, CompanyLastWeight

PX.SM.SMScale.ScaleDeviceID : Edm.Guid
PX.SM.SMScale.DeviceHubID : Edm.String [key] "DeviceHub ID"
PX.SM.SMScale.ScaleID : Edm.String [key] "Scale ID"
PX.SM.SMScale.Descr : Edm.String "Description"
PX.SM.SMScale.UOM : Edm.String "Scale UOM"
PX.SM.SMScale.LastWeight : Edm.Decimal "Scale Last Weight"
PX.SM.SMScale.CreatedByID : Edm.Guid "Created By"
PX.SM.SMScale.CreatedByScreenID : Edm.String
PX.SM.SMScale.CreatedDateTime : Edm.DateTimeOffset
PX.SM.SMScale.LastModifiedByID : Edm.Guid "Last Modified By"
PX.SM.SMScale.LastModifiedByScreenID : Edm.String
PX.SM.SMScale.LastModifiedDateTime : Edm.DateTimeOffset "Last Updated"
PX.SM.SMScale.tstamp : Edm.Binary
PX.SM.SMScale.CompanyUOM : Edm.String "UOM"
PX.SM.SMScale.CompanyLastWeight : Edm.Decimal "Last Weight"
PX.SM.SMScale.UsersByCreatedByID -> PX.SM.Users (CreatedByID=PKID)
PX.SM.SMScale.UsersByLastModifiedByID -> PX.SM.Users (LastModifiedByID=PKID)
PX.SM.SMScale.UserPreferencesCollection -> Collection(PX.SM.UserPreferences)
PX.SM.SMScale.INScanUserSetupCollection -> Collection(PX.Objects.IN.INScanUserSetup)
PX.SM.SMScale.POReceivePutAwayUserSetupCollection -> Collection(PX.Objects.PO.POReceivePutAwayUserSetup)
PX.SM.SMScale.SOPickPackShipUserSetupCollection -> Collection(PX.Objects.SO.SOPickPackShipUserSetup)

# PX.SM.SMScanJob (EntityType)

Label: "Scan Job"
Key: ScanJobID
Entity sets: PX_SM_SMScanJob, ScanJob, SMScanJob
Non-filterable, non-selectable: PaperSourceList, PixelTypeList, ResolutionList, FileTypeList, RequestingUserName

PX.SM.SMScanJob.ScanJobID : Edm.Int32 [key] "Job ID"
PX.SM.SMScanJob.DeviceHubID : Edm.String "DeviceHub ID"
PX.SM.SMScanJob.ScannerName : Edm.String "Scanner ID"
PX.SM.SMScanJob.EntityScreenID : Edm.String "Form ID"
PX.SM.SMScanJob.GraphType : Edm.String "Graph Type"
PX.SM.SMScanJob.EntityNoteID : Edm.Guid "Entity Note ID"
PX.SM.SMScanJob.EntityPrimaryViewName : Edm.String "Primary View Name"
PX.SM.SMScanJob.ScanViewName : Edm.String "Scan View Name"
PX.SM.SMScanJob.Status : Edm.String "Status"
PX.SM.SMScanJob.PaperSource : Edm.Int32 "Paper Source"
PX.SM.SMScanJob.PixelType : Edm.Int32 "Color Mode"
PX.SM.SMScanJob.Resolution : Edm.Int32 "Resolution"
PX.SM.SMScanJob.FileType : Edm.Int32 "File Type"
PX.SM.SMScanJob.FileName : Edm.String "File Name"
PX.SM.SMScanJob.Error : Edm.String "Error"
PX.SM.SMScanJob.ErrorTrace : Edm.String "Error Trace"
PX.SM.SMScanJob.PaperSourceList : Edm.String
PX.SM.SMScanJob.PixelTypeList : Edm.String
PX.SM.SMScanJob.ResolutionList : Edm.String
PX.SM.SMScanJob.FileTypeList : Edm.String
PX.SM.SMScanJob.RequestingUserName : Edm.String "Task Initiator"
PX.SM.SMScanJob.LineCntr : Edm.Int32 [required]
PX.SM.SMScanJob.tstamp : Edm.Binary
PX.SM.SMScanJob.CreatedByID : Edm.Guid "Created By"
PX.SM.SMScanJob.CreatedByScreenID : Edm.String
PX.SM.SMScanJob.CreatedDateTime : Edm.DateTimeOffset "Creation Date and Time"
PX.SM.SMScanJob.LastModifiedByID : Edm.Guid "Last Modified By"
PX.SM.SMScanJob.LastModifiedByScreenID : Edm.String
PX.SM.SMScanJob.LastModifiedDateTime : Edm.DateTimeOffset
PX.SM.SMScanJob.UsersByCreatedByID -> PX.SM.Users (CreatedByID=PKID)
PX.SM.SMScanJob.UsersByLastModifiedByID -> PX.SM.Users (LastModifiedByID=PKID)
PX.SM.SMScanJob.SMScannerByScannerName -> PX.SM.SMScanner (ScannerName=ScannerName)
PX.SM.SMScanJob.SMScanJobParameterCollection -> Collection(PX.SM.SMScanJobParameter)

# PX.SM.SMScanJobParameter (EntityType)

Label: "Scan Job Parameters"
Key: LineNbr, ParameterName, ScanJobID
Entity sets: PX_SM_SMScanJobParameter, ScanJobParameters, SMScanJobParameter

PX.SM.SMScanJobParameter.ScanJobID : Edm.Int32 [key] "Job ID"
PX.SM.SMScanJobParameter.LineNbr : Edm.Int32 [key] "Line Nbr."
PX.SM.SMScanJobParameter.ViewName : Edm.String "View Name"
PX.SM.SMScanJobParameter.ParameterName : Edm.String [key] "Parameter Name"
PX.SM.SMScanJobParameter.ParameterValue : Edm.String "Parameter Value"
PX.SM.SMScanJobParameter.SMScanJobByScanJobID -> PX.SM.SMScanJob (ScanJobID=ScanJobID)

# PX.SM.SMScanner (EntityType)

Label: "Scanners"
Key: DeviceHubID, ScannerName
Entity sets: PX_SM_SMScanner, Scanners, SMScanner

PX.SM.SMScanner.ScannerID : Edm.Guid
PX.SM.SMScanner.DeviceHubID : Edm.String [key] "DeviceHub ID"
PX.SM.SMScanner.ScannerName : Edm.String [key] "Scanner ID"
PX.SM.SMScanner.Description : Edm.String "Description"
PX.SM.SMScanner.IsActive : Edm.Boolean "Active"
PX.SM.SMScanner.PaperSourceDefValue : Edm.Int32 "Paper Source (Default)"
PX.SM.SMScanner.PaperSourceComboValues : Edm.String "Paper Sources"
PX.SM.SMScanner.PixelTypeDefValue : Edm.Int32 "Color Mode (Default)"
PX.SM.SMScanner.PixelTypeComboValues : Edm.String "Color Modes"
PX.SM.SMScanner.ResolutionDefValue : Edm.Int32 "Resolution (Default)"
PX.SM.SMScanner.ResolutionComboValues : Edm.String "Resolutions"
PX.SM.SMScanner.FileTypeDefValue : Edm.Int32 "File Type (Default)"
PX.SM.SMScanner.FileTypeComboValues : Edm.String "File Types"
PX.SM.SMScanner.CreatedByID : Edm.Guid "Created By"
PX.SM.SMScanner.CreatedByScreenID : Edm.String
PX.SM.SMScanner.CreatedDateTime : Edm.DateTimeOffset
PX.SM.SMScanner.LastModifiedByID : Edm.Guid "Last Modified By"
PX.SM.SMScanner.LastModifiedByScreenID : Edm.String
PX.SM.SMScanner.LastModifiedDateTime : Edm.DateTimeOffset
PX.SM.SMScanner.tstamp : Edm.Binary
PX.SM.SMScanner.UsersByCreatedByID -> PX.SM.Users (CreatedByID=PKID)
PX.SM.SMScanner.UsersByLastModifiedByID -> PX.SM.Users (LastModifiedByID=PKID)
PX.SM.SMScanner.UserPreferencesCollection -> Collection(PX.SM.UserPreferences)
PX.SM.SMScanner.SMScanJobCollection -> Collection(PX.SM.SMScanJob)

# PX.SM.SpaceUsageCalculationHistory (EntityType)

Label: "Space Usage Calculation History"
Key: PkID
Entity sets: PX_SM_SpaceUsageCalculationHistory, SpaceUsageCalculationHistory
Non-filterable, non-selectable: UsedTotal, FreeSpace, CurrentStatus

PX.SM.SpaceUsageCalculationHistory.PkID : Edm.Guid [key] "PkID"
PX.SM.SpaceUsageCalculationHistory.QuotaSize : Edm.Int64 "Space Limit"
PX.SM.SpaceUsageCalculationHistory.UsedByCompanies : Edm.Int64 "By Tenants"
PX.SM.SpaceUsageCalculationHistory.UsedBySnapshots : Edm.Int64 "By Snapshots"
PX.SM.SpaceUsageCalculationHistory.UsedTotal : Edm.Int64 "Total"
PX.SM.SpaceUsageCalculationHistory.FreeSpace : Edm.Int64 "Free Space"
PX.SM.SpaceUsageCalculationHistory.CalculationDate : Edm.DateTimeOffset "Last Calculated"
PX.SM.SpaceUsageCalculationHistory.CurrentStatus : Edm.Int64 "Usage Status"
PX.SM.SpaceUsageCalculationHistory.CreatedByID : Edm.Guid "Created By"
PX.SM.SpaceUsageCalculationHistory.CreatedByScreenID : Edm.String
PX.SM.SpaceUsageCalculationHistory.CreatedDateTime : Edm.DateTimeOffset "Created DateTime"
PX.SM.SpaceUsageCalculationHistory.LastModifiedByID : Edm.Guid "Last Modified By"
PX.SM.SpaceUsageCalculationHistory.LastModifiedByScreenID : Edm.String
PX.SM.SpaceUsageCalculationHistory.LastModifiedDateTime : Edm.DateTimeOffset
PX.SM.SpaceUsageCalculationHistory.TStamp : Edm.Binary
PX.SM.SpaceUsageCalculationHistory.UsersByCreatedByID -> PX.SM.Users (CreatedByID=PKID)
PX.SM.SpaceUsageCalculationHistory.UsersByLastModifiedByID -> PX.SM.Users (LastModifiedByID=PKID)

# PX.SM.Standalone.EMailAccount (EntityType)

Singletons: PX_SM_Standalone_EMailAccount

PX.SM.Standalone.EMailAccount.EmailAccountID : Edm.Int32
PX.SM.Standalone.EMailAccount.Password : Edm.String
PX.SM.Standalone.EMailAccount.DeletedDatabaseRecord : Edm.Boolean [required] "DeletedDatabaseRecord"
PX.SM.Standalone.EMailAccount.VendorByDefaultOwnerID -> PX.Objects.AP.Vendor
PX.SM.Standalone.EMailAccount.ContactByDefaultOwnerID -> PX.Objects.CR.Contact
PX.SM.Standalone.EMailAccount.CRLeadClassByCreateLeadClassID -> PX.Objects.CR.CRLeadClass
PX.SM.Standalone.EMailAccount.OAuthApplicationByOAuthApplicationID -> PX.OAuthClient.DAC.OAuthApplication
PX.SM.Standalone.EMailAccount.UsersByDefaultOwnerID -> PX.SM.Users
PX.SM.Standalone.EMailAccount.UsersByUserID -> PX.SM.Users
PX.SM.Standalone.EMailAccount.UsersByCreatedByID -> PX.SM.Users
PX.SM.Standalone.EMailAccount.UsersByLastModifiedByID -> PX.SM.Users
PX.SM.Standalone.EMailAccount.NotificationByResponseNotificationID -> PX.SM.Notification
PX.SM.Standalone.EMailAccount.NotificationByConfirmReceiptNotificationID -> PX.SM.Notification
PX.SM.Standalone.EMailAccount.EPCompanyTreeByDefaultWorkgroupID -> PX.TM.EPCompanyTree
PX.SM.Standalone.EMailAccount.CRCaseClassByCreateCaseClassID -> PX.Objects.CR.CRCaseClass
PX.SM.Standalone.EMailAccount.EPAssignmentMapByDefaultEmailAssignmentMapID -> PX.Objects.EP.EPAssignmentMap
PX.SM.Standalone.EMailAccount.WikiNotificationTemplateCollection -> Collection(PX.SM.WikiNotificationTemplate)
PX.SM.Standalone.EMailAccount.CRSMEmailCollection -> Collection(PX.Objects.CR.CRSMEmail)
PX.SM.Standalone.EMailAccount.NotificationSetupCollection -> Collection(PX.Objects.CS.NotificationSetup)
PX.SM.Standalone.EMailAccount.CRContactClassCollection -> Collection(PX.Objects.CR.CRContactClass)
PX.SM.Standalone.EMailAccount.CRCustomerClassCollection -> Collection(PX.Objects.CR.CRCustomerClass)
PX.SM.Standalone.EMailAccount.CRLeadClassCollection -> Collection(PX.Objects.CR.CRLeadClass)
PX.SM.Standalone.EMailAccount.CROpportunityClassCollection -> Collection(PX.Objects.CR.CROpportunityClass)
PX.SM.Standalone.EMailAccount.UserPreferencesCollection -> Collection(PX.SM.UserPreferences)
PX.SM.Standalone.EMailAccount.NotificationCollection -> Collection(PX.SM.Notification)
PX.SM.Standalone.EMailAccount.PreferencesEmailCollection -> Collection(PX.SM.PreferencesEmail)
PX.SM.Standalone.EMailAccount.SMEmailCollection -> Collection(PX.Objects.CR.SMEmail)
PX.SM.Standalone.EMailAccount.NotificationSourceCollection -> Collection(PX.Objects.CS.NotificationSource)
PX.SM.Standalone.EMailAccount.CRCaseClassCollection -> Collection(PX.Objects.CR.CRCaseClass)
PX.SM.Standalone.EMailAccount.CRMassMailCollection -> Collection(PX.Objects.CR.CRMassMail)
PX.SM.Standalone.EMailAccount.EMailSyncAccountCollection -> Collection(PX.SM.EMailSyncAccount)
PX.SM.Standalone.EMailAccount.EMailAccountStatisticsCollection -> Collection(PX.SM.EMailAccountStatistics)
PX.SM.Standalone.EMailAccount.EmailLogCollection -> Collection(PX.Mail.Log.DAC.EmailLog)

# PX.SM.SyncTimeTag (EntityType)

Key: NoteID
Entity sets: PX_SM_SyncTimeTag

PX.SM.SyncTimeTag.NoteID : Edm.Guid [key]
PX.SM.SyncTimeTag.TimeTag : Edm.DateTimeOffset

# PX.SM.TablesCompanySize (EntityType)

Label: "Table Size"
BaseType: PX.SM.TableSize
Key: Company, TableName (inherited from PX.SM.TableSize)
Entity sets: PX_SM_TablesCompanySize
Filterable: false (fields declared in this DAC cannot be used in $filter or $select; inherited ones can)

PX.SM.TablesCompanySize.Size : Edm.Int64 "Size in DB"
PX.SM.TablesCompanySize.SizeMB : Edm.Decimal "Size in DB (MB)"
PX.SM.TablesCompanySize.CompanyName : Edm.String "Tenant Name"

# PX.SM.TableSize (EntityType)

Label: "Table Size"
Key: Company, TableName
Entity sets: PX_SM_TableSize, TableSize
Non-filterable, non-selectable: FullSizeByCompanyMB

PX.SM.TableSize.TableName : Edm.String [key] "Table Name"
PX.SM.TableSize.SizeByCompany : Edm.Int64 "Size in DB"
PX.SM.TableSize.IndexSizeByCompany : Edm.Int64 "Index Size in DB"
PX.SM.TableSize.FullSizeByCompany : Edm.Int64 "Size in DB (including indexes)"
PX.SM.TableSize.FullSizeByCompanyMB : Edm.Decimal "Size in DB (MB)"
PX.SM.TableSize.CountOfCompanyRecords : Edm.Int64 "Number of Records"
PX.SM.TableSize.RealSize : Edm.Int64 "Real Size"
PX.SM.TableSize.Company : Edm.Int32 [key] "CompanyId"

# PX.SM.TablesSnapshotSize (EntityType)

Label: "Table Size"
BaseType: PX.SM.TableSize
Key: Company, TableName (inherited from PX.SM.TableSize)
Entity sets: PX_SM_TablesSnapshotSize
Filterable: false (fields declared in this DAC cannot be used in $filter or $select; inherited ones can)

PX.SM.TablesSnapshotSize.Size : Edm.Decimal "Size in DB"
PX.SM.TablesSnapshotSize.SizeMB : Edm.Decimal "Size in DB (MB)"
PX.SM.TablesSnapshotSize.SnapshotName : Edm.String "Snapshot Name"

# PX.SM.TaskTemplate (EntityType)

Label: "Task Template"
Key: TaskTemplateID
Entity sets: PX_SM_TaskTemplate, TaskTemplate
Non-filterable, non-selectable: NameForDescription, NoteText, ShowCreatedByEventsTabExpr

PX.SM.TaskTemplate.TaskTemplateID : Edm.Int32 [key] "Template ID"
PX.SM.TaskTemplate.Name : Edm.String "Description"
PX.SM.TaskTemplate.NameForDescription : Edm.String
PX.SM.TaskTemplate.Summary : Edm.String "Summary"
PX.SM.TaskTemplate.ScreenID : Edm.String "Screen ID"
PX.SM.TaskTemplate.OwnerName : Edm.String "Owner"
PX.SM.TaskTemplate.Body : Edm.String "Body"
PX.SM.TaskTemplate.LocaleName : Edm.String "Locale"
PX.SM.TaskTemplate.AttachActivity : Edm.Boolean "Attach Activity"
PX.SM.TaskTemplate.RefNoteID : Edm.String "Link-To Entity"
PX.SM.TaskTemplate.NoteID : Edm.Guid
PX.SM.TaskTemplate.NoteText : Edm.String "Note Text"
PX.SM.TaskTemplate.CreatedByID : Edm.Guid "Created By"
PX.SM.TaskTemplate.CreatedByScreenID : Edm.String
PX.SM.TaskTemplate.CreatedDateTime : Edm.DateTimeOffset "Created On"
PX.SM.TaskTemplate.LastModifiedByID : Edm.Guid "Last Modified By"
PX.SM.TaskTemplate.LastModifiedByScreenID : Edm.String
PX.SM.TaskTemplate.LastModifiedDateTime : Edm.DateTimeOffset "Last Modified On"
PX.SM.TaskTemplate.tstamp : Edm.Binary
PX.SM.TaskTemplate.FieldCntr : Edm.Int16 [required]
PX.SM.TaskTemplate.ShowCreatedByEventsTabExpr : Edm.Boolean "ShowCreatedByEventsTabExpr"
PX.SM.TaskTemplate.UsersByCreatedByID -> PX.SM.Users (CreatedByID=PKID)
PX.SM.TaskTemplate.UsersByLastModifiedByID -> PX.SM.Users (LastModifiedByID=PKID)
PX.SM.TaskTemplate.LocaleByLocaleName -> PX.SM.Locale (LocaleName=LocaleName)
PX.SM.TaskTemplate.TaskTemplateSettingCollection -> Collection(PX.SM.TaskTemplateSetting)
PX.SM.TaskTemplate.BPEventSubscriberCollection -> Collection(PX.BusinessProcess.DAC.BPEventSubscriber)

# PX.SM.TaskTemplateSetting (EntityType)

Label: "Task Template Setting"
Key: LineNbr, TaskTemplateID
Entity sets: PX_SM_TaskTemplateSetting, TaskTemplateSetting
Non-filterable, non-selectable: NoteText

PX.SM.TaskTemplateSetting.TaskTemplateID : Edm.Int32 [key]
PX.SM.TaskTemplateSetting.LineNbr : Edm.Int16 [key]
PX.SM.TaskTemplateSetting.IsActive : Edm.Boolean [required] "Active"
PX.SM.TaskTemplateSetting.FieldName : Edm.String "Field Name"
PX.SM.TaskTemplateSetting.FromSchema : Edm.Boolean [required] "From Schema"
PX.SM.TaskTemplateSetting.Value : Edm.String "Value"
PX.SM.TaskTemplateSetting.NoteID : Edm.Guid
PX.SM.TaskTemplateSetting.NoteText : Edm.String "Note Text"
PX.SM.TaskTemplateSetting.CreatedByID : Edm.Guid "Created By"
PX.SM.TaskTemplateSetting.CreatedByScreenID : Edm.String
PX.SM.TaskTemplateSetting.CreatedDateTime : Edm.DateTimeOffset "Created On"
PX.SM.TaskTemplateSetting.LastModifiedByID : Edm.Guid "Last Modified By"
PX.SM.TaskTemplateSetting.LastModifiedByScreenID : Edm.String
PX.SM.TaskTemplateSetting.LastModifiedDateTime : Edm.DateTimeOffset "Last Modified On"
PX.SM.TaskTemplateSetting.tstamp : Edm.Binary
PX.SM.TaskTemplateSetting.UsersByCreatedByID -> PX.SM.Users (CreatedByID=PKID)
PX.SM.TaskTemplateSetting.UsersByLastModifiedByID -> PX.SM.Users (LastModifiedByID=PKID)
PX.SM.TaskTemplateSetting.TaskTemplateByTaskTemplateID -> PX.SM.TaskTemplate (TaskTemplateID=TaskTemplateID)

# PX.SM.UPErrors (EntityType)

Label: "Update Error"
Key: ErrorID, UpdateID
Entity sets: PX_SM_UPErrors, UpdateError, UPErrors
Non-filterable, non-selectable: Details

PX.SM.UPErrors.UpdateID : Edm.Int32 [key] "Maintenance ID"
PX.SM.UPErrors.ErrorID : Edm.Int32 [key] "Error ID"
PX.SM.UPErrors.Message : Edm.String "Error"
PX.SM.UPErrors.Stack : Edm.String "Stack"
PX.SM.UPErrors.Script : Edm.String
PX.SM.UPErrors.Skip : Edm.Boolean "Skipped"
PX.SM.UPErrors.Details : Edm.String "Details"

# PX.SM.UPHistory (EntityType)

Label: "Update History"
Key: UpdateID
Entity sets: PX_SM_UPHistory, UpdateHistory, UPHistory

PX.SM.UPHistory.UpdateID : Edm.Int32 [key] "Maintenance ID"
PX.SM.UPHistory.Host : Edm.String "Host"
PX.SM.UPHistory.Started : Edm.DateTimeOffset "Started On"
PX.SM.UPHistory.Finished : Edm.DateTimeOffset "Finished On"

# PX.SM.UPHistoryComponents (EntityType)

Label: "Update History Components"
Key: UpdateComponentID
Entity sets: PX_SM_UPHistoryComponents, UpdateHistoryComponents, UPHistoryComponents

PX.SM.UPHistoryComponents.UpdateComponentID : Edm.Int32 [key] "Maintenance Components ID"
PX.SM.UPHistoryComponents.UpdateID : Edm.Int32 "Maintenance ID"
PX.SM.UPHistoryComponents.ComponentName : Edm.String "Component Name"
PX.SM.UPHistoryComponents.ComponentType : Edm.String "Component Type"
PX.SM.UPHistoryComponents.FromVersion : Edm.String "From Version"
PX.SM.UPHistoryComponents.ToVersion : Edm.String "To Version"

# PX.SM.UploadAllowedFileTypes (EntityType)

Key: FileExt
Entity sets: PX_SM_UploadAllowedFileTypes

PX.SM.UploadAllowedFileTypes.FileExt : Edm.String [key] "File Extension"
PX.SM.UploadAllowedFileTypes.IconUrl : Edm.String "Icon URL"
PX.SM.UploadAllowedFileTypes.Forbidden : Edm.Boolean [required] "Forbidden"
PX.SM.UploadAllowedFileTypes.IsImage : Edm.Boolean [required] "Image"
PX.SM.UploadAllowedFileTypes.DefApplication : Edm.String "Default Application"

# PX.SM.UploadFile (EntityType)

Key: FileID
Entity sets: PX_SM_UploadFile
Non-filterable, non-selectable: Comment, FileRevisionID, OriginalName, Size, RevisionDate, Extansion, LastExportDate, NoteText

PX.SM.UploadFile.FileID : Edm.Guid [key] "File"
PX.SM.UploadFile.Name : Edm.String "Name"
PX.SM.UploadFile.ShortName : Edm.String "File Name"
PX.SM.UploadFile.Comment : Edm.String "Comment"
PX.SM.UploadFile.CheckedOutComment : Edm.String "Check Out Comment"
PX.SM.UploadFile.Versioned : Edm.Boolean [required] "Versioned"
PX.SM.UploadFile.CreatedByID : Edm.Guid "Created by"
PX.SM.UploadFile.CreatedDateTime : Edm.DateTimeOffset "Added on"
PX.SM.UploadFile.LastRevisionID : Edm.Int32 [required]
PX.SM.UploadFile.CheckedOutBy : Edm.Guid "Checked Out By"
PX.SM.UploadFile.PrimaryPageID : Edm.Guid
PX.SM.UploadFile.PrimaryScreenID : Edm.String
PX.SM.UploadFile.tstamp : Edm.Binary
PX.SM.UploadFile.FileRevisionID : Edm.Int32
PX.SM.UploadFile.OriginalName : Edm.String
PX.SM.UploadFile.Size : Edm.Int32
PX.SM.UploadFile.RevisionDate : Edm.DateTimeOffset
PX.SM.UploadFile.IsHidden : Edm.Boolean "Hidden"
PX.SM.UploadFile.Extansion : Edm.String "Extension"
PX.SM.UploadFile.Synchronizable : Edm.Boolean "Synchronize"
PX.SM.UploadFile.SourceType : Edm.String "Synchronization Type"
PX.SM.UploadFile.SourceUri : Edm.String "File Location"
PX.SM.UploadFile.SourceLogin : Edm.String "Username"
PX.SM.UploadFile.SourcePassword : Edm.String "Password"
PX.SM.UploadFile.SourceIsFolder : Edm.Boolean "Synchronize Folder Content"
PX.SM.UploadFile.SourceMask : Edm.String "Import File Reg. Exp."
PX.SM.UploadFile.SourceNamingFormat : Edm.String "Export File Naming Format"
PX.SM.UploadFile.SourceLastImportDate : Edm.DateTimeOffset "Last Import Date"
PX.SM.UploadFile.SourceLastExportDate : Edm.DateTimeOffset
PX.SM.UploadFile.LastExportDate : Edm.DateTimeOffset "Last Export Date"
PX.SM.UploadFile.IsPublic : Edm.Boolean [required] "Public"
PX.SM.UploadFile.NoteID : Edm.Guid
PX.SM.UploadFile.NoteText : Edm.String "Note Text"
PX.SM.UploadFile.SshCertificateName : Edm.String "SSH Private Key"
PX.SM.UploadFile.IsSystem : Edm.Boolean "Is System File"
PX.SM.UploadFile.IsAccessRightsFromEntities : Edm.Boolean [required] "Inherit Access Rights from Entities"
PX.SM.UploadFile.UploadFileWithIDSelectorByName -> PX.SM.UploadFileWithIDSelector (Name=FileID)
PX.SM.UploadFile.UsersByCreatedByID -> PX.SM.Users (CreatedByID=PKID)
PX.SM.UploadFile.CertificateBySshCertificateName -> PX.SM.Certificate (SshCertificateName=Name)
PX.SM.UploadFile.UploadFileWithIDSelectorCollection -> Collection(PX.SM.UploadFileWithIDSelector)

# PX.SM.UploadFileRevision (EntityType)

Key: FileID, FileRevisionID
Entity sets: PX_SM_UploadFileRevision

PX.SM.UploadFileRevision.FileID : Edm.Guid [key]
PX.SM.UploadFileRevision.FileRevisionID : Edm.Int32 [key] "Version ID"
PX.SM.UploadFileRevision.BlobHandler : Edm.Guid "BlobHandler"
PX.SM.UploadFileRevision.Comment : Edm.String "Comment"
PX.SM.UploadFileRevision.Size : Edm.Int32
PX.SM.UploadFileRevision.OriginalName : Edm.String "Original Name"
PX.SM.UploadFileRevision.OriginalTimestamp : Edm.DateTimeOffset
PX.SM.UploadFileRevision.CreatedByID : Edm.Guid "Created by"
PX.SM.UploadFileRevision.CreatedDateTime : Edm.DateTimeOffset "Creation Time"
PX.SM.UploadFileRevision.UsersByCreatedByID -> PX.SM.Users (CreatedByID=PKID)
PX.SM.UploadFileRevision.ESignEnvelopeInfoCollection -> Collection(PX.ESign.ESignEnvelopeInfo)

# PX.SM.UploadFileRevisionNoData (EntityType)

BaseType: PX.SM.UploadFileRevision
Key: FileID, FileRevisionID (inherited from PX.SM.UploadFileRevision)
Entity sets: PX_SM_UploadFileRevisionNoData
Filterable: false (fields declared in this DAC cannot be used in $filter or $select; inherited ones can)

PX.SM.UploadFileRevisionNoData.ReadableSize : Edm.String "File Size"

# PX.SM.UploadFileWithData (EntityType)

Key: FileID, FileRevisionID
Entity sets: PX_SM_UploadFileWithData
Non-filterable, non-selectable: ContentID

PX.SM.UploadFileWithData.FileID : Edm.Guid [key]
PX.SM.UploadFileWithData.FileRevisionID : Edm.Int32 [key]
PX.SM.UploadFileWithData.Name : Edm.String
PX.SM.UploadFileWithData.Comment : Edm.String
PX.SM.UploadFileWithData.ContentID : Edm.String
PX.SM.UploadFileWithData.BlobHandler : Edm.Guid
PX.SM.UploadFileWithData.Size : Edm.Int32
PX.SM.UploadFileWithData.NoteID : Edm.Guid
PX.SM.UploadFileWithData.UploadFileWithIDSelectorByName -> PX.SM.UploadFileWithIDSelector (Name=FileID)
PX.SM.UploadFileWithData.UploadFileWithIDSelectorCollection -> Collection(PX.SM.UploadFileWithIDSelector)

# PX.SM.UploadFileWithIDSelector (EntityType)

Label: "File"
BaseType: PX.SM.UploadFileWithTags
Key: FileID (inherited from PX.SM.UploadFile)
Entity sets: PX_SM_UploadFileWithIDSelector, File, UploadFileWithIDSelector
Filterable: false (fields declared in this DAC cannot be used in $filter or $select; inherited ones can)

PX.SM.UploadFileWithIDSelector.SelectedWikiID : Edm.Guid "Wiki"
PX.SM.UploadFileWithIDSelector.SelectedPageID : Edm.Guid "Primary Page"
PX.SM.UploadFileWithIDSelector.AccessRights : Edm.Int16
PX.SM.UploadFileWithIDSelector.ExternalLink : Edm.String "URL"
PX.SM.UploadFileWithIDSelector.WikiLink : Edm.String "URL for Wiki"
PX.SM.UploadFileWithIDSelector.SiteMapByPrimaryScreenID -> PX.SM.SiteMap (PrimaryScreenID=ScreenID)
PX.SM.UploadFileWithIDSelector.UploadFileByFileID -> PX.SM.UploadFile (FileID=FileID)
PX.SM.UploadFileWithIDSelector.PMLinkedFileCollection -> Collection(PX.Objects.PM.ProjectFiles.FileEntryForms.PMLinkedFile)
PX.SM.UploadFileWithIDSelector.UploadFileCollection -> Collection(PX.SM.UploadFile)

# PX.SM.UploadFileWithNoData (EntityType)

BaseType: PX.SM.UploadFile
Key: FileID (inherited from PX.SM.UploadFile)
Entity sets: PX_SM_UploadFileWithNoData

# PX.SM.UploadFileWithTags (EntityType)

BaseType: PX.SM.UploadFile
Key: FileID (inherited from PX.SM.UploadFile)
Entity sets: PX_SM_UploadFileWithTags
Filterable: false (fields declared in this DAC cannot be used in $filter or $select; inherited ones can)

PX.SM.UploadFileWithTags.Tags : Edm.String "Tags"

# PX.SM.UPLock (EntityType)

Key: DatabaseID
Entity sets: PX_SM_UPLock

PX.SM.UPLock.DatabaseID : Edm.Int32 [key]
PX.SM.UPLock.Host : Edm.String
PX.SM.UPLock.Date : Edm.DateTimeOffset "Lockout at"
PX.SM.UPLock.Purpose : Edm.String "Reason"

# PX.SM.UPPackageTables (EntityType)

Key: ProjectID, TableName
Entity sets: PX_SM_UPPackageTables

PX.SM.UPPackageTables.ProjectID : Edm.Guid [key] "ProjectID"
PX.SM.UPPackageTables.TableName : Edm.String [key] "Table Name"
PX.SM.UPPackageTables.CreateSchema : Edm.Boolean [required] "Create Schema"
PX.SM.UPPackageTables.ExportData : Edm.Boolean [required] "Export Data"
PX.SM.UPPackageTables.CustomScript : Edm.String "Custom Script"
PX.SM.UPPackageTables.CustProjectByProjectID -> PX.SM.CustProject (ProjectID=ProjID)

# PX.SM.UPSetup (EntityType)

Singletons: PX_SM_UPSetup

PX.SM.UPSetup.UpdateEnabled : Edm.Boolean "Use Update Server"
PX.SM.UPSetup.UpdateServer : Edm.String "Update Server Address"
PX.SM.UPSetup.UpdateServerAlternative : Edm.String "Alternative Update Server Address"
PX.SM.UPSetup.UpdateAlternativeEnabled : Edm.Boolean "Use Alternative Update Server"
PX.SM.UPSetup.UpdateNotification : Edm.Boolean "Check for Updates"
PX.SM.UPSetup.StorageProvider : Edm.String "Storage Provider"
PX.SM.UPSetup.LicensingServer : Edm.String
PX.SM.UPSetup.ISVUpdateEndpoint : Edm.String

# PX.SM.UPSnapshot (EntityType)

Label: "Snapshot"
Key: SnapshotID
Entity sets: PX_SM_UPSnapshot, Snapshot, UPSnapshot
Non-filterable, non-selectable: Prepared, SizePrepared, Size, NoteText, DeletedDatabaseRecord

PX.SM.UPSnapshot.SnapshotID : Edm.Guid [key] "Snapshot ID"
PX.SM.UPSnapshot.Name : Edm.String "Name"
PX.SM.UPSnapshot.Description : Edm.String "Description"
PX.SM.UPSnapshot.Prepared : Edm.Boolean "Ready For Export"
PX.SM.UPSnapshot.SizePrepared : Edm.Decimal "Size on Disk (MB)"
PX.SM.UPSnapshot.Size : Edm.Int64 "Size"
PX.SM.UPSnapshot.Date : Edm.DateTimeOffset "Creation Date"
PX.SM.UPSnapshot.Version : Edm.String "Version"
PX.SM.UPSnapshot.Host : Edm.String "Host"
PX.SM.UPSnapshot.ExportMode : Edm.String "Export Mode"
PX.SM.UPSnapshot.Customization : Edm.String "Customization"
PX.SM.UPSnapshot.MasterCompany : Edm.String "Master Tenant"
PX.SM.UPSnapshot.SourceCompany : Edm.Int32 "Tenant ID"
PX.SM.UPSnapshot.LinkedCompany : Edm.Int32
PX.SM.UPSnapshot.NoteID : Edm.Guid
PX.SM.UPSnapshot.NoteText : Edm.String "Note Text"
PX.SM.UPSnapshot.CreatedByID : Edm.Guid "Created By"
PX.SM.UPSnapshot.CreatedByScreenID : Edm.String
PX.SM.UPSnapshot.CreatedDateTime : Edm.DateTimeOffset "Created"
PX.SM.UPSnapshot.LastModifiedByID : Edm.Guid "Last Modified By"
PX.SM.UPSnapshot.LastModifiedByScreenID : Edm.String
PX.SM.UPSnapshot.LastModifiedDateTime : Edm.DateTimeOffset
PX.SM.UPSnapshot.IsSafe : Edm.Boolean [required] "Is Safe"
PX.SM.UPSnapshot.IsUnderDeletion : Edm.Boolean "Under Deletion"
PX.SM.UPSnapshot.DeletedDatabaseRecord : Edm.Boolean [required] "DeletedDatabaseRecord"
PX.SM.UPSnapshot.UsersByCreatedByID -> PX.SM.Users (CreatedByID=PKID)
PX.SM.UPSnapshot.UsersByLastModifiedByID -> PX.SM.Users (LastModifiedByID=PKID)
PX.SM.UPSnapshot.UPSnapshotHistoryCollection -> Collection(PX.SM.UPSnapshotHistory)

# PX.SM.UPSnapshotHistory (EntityType)

Label: "Snapshot Restoration History"
Key: HistoryID
Entity sets: PX_SM_UPSnapshotHistory, SnapshotRestorationHistory, UPSnapshotHistory
Non-filterable, non-selectable: UserID

PX.SM.UPSnapshotHistory.HistoryID : Edm.Int32 [key] "History ID"
PX.SM.UPSnapshotHistory.SnapshotID : Edm.Guid "Snapshot ID"
PX.SM.UPSnapshotHistory.TargetCompany : Edm.Int32 "Company ID"
PX.SM.UPSnapshotHistory.UserID : Edm.Guid "User"
PX.SM.UPSnapshotHistory.CreatedByID : Edm.Guid "User"
PX.SM.UPSnapshotHistory.CreatedByScreenID : Edm.String
PX.SM.UPSnapshotHistory.CreatedDateTime : Edm.DateTimeOffset "Restoration Date"
PX.SM.UPSnapshotHistory.IsSafe : Edm.Boolean [required] "Is Safe"
PX.SM.UPSnapshotHistory.Dismissed : Edm.Boolean [required] "Dismissed"
PX.SM.UPSnapshotHistory.UsersByCreatedByID -> PX.SM.Users (CreatedByID=PKID)
PX.SM.UPSnapshotHistory.UPSnapshotBySnapshotID -> PX.SM.UPSnapshot (SnapshotID=SnapshotID)

# PX.SM.UPSnapshotSize (EntityType)

Label: "Snapshot Size"
BaseType: PX.SM.UPSnapshot
Key: SnapshotID (inherited from PX.SM.UPSnapshot)
Entity sets: PX_SM_UPSnapshotSize, SnapshotSize, UPSnapshotSize
Filterable: false (fields declared in this DAC cannot be used in $filter or $select; inherited ones can)

PX.SM.UPSnapshotSize.SizeInDb : Edm.Decimal "Size in DB"
PX.SM.UPSnapshotSize.SizeInDbMB : Edm.Decimal "Size in DB (MB)"

# PX.SM.UserFilter (EntityType)

Key: PKID, Username
Entity sets: PX_SM_UserFilter

PX.SM.UserFilter.Username : Edm.String [key] "Login"
PX.SM.UserFilter.PKID : Edm.Guid [key] "PKID"
PX.SM.UserFilter.StartIPAddress : Edm.String "Start IP Address"
PX.SM.UserFilter.EndIPAddress : Edm.String "End IP Address"
PX.SM.UserFilter.UsersByUsername -> PX.SM.Users (Username=Username)

# PX.SM.UserLocaleFormat (EntityType)

Key: LocaleName, UserID
Entity sets: PX_SM_UserLocaleFormat

PX.SM.UserLocaleFormat.UserID : Edm.Guid [key]
PX.SM.UserLocaleFormat.LocaleName : Edm.String [key]
PX.SM.UserLocaleFormat.FormatID : Edm.Int32

# PX.SM.UserPreferences (EntityType)

Label: "User Preferences and Email Settings"
Key: UserID
Entity sets: PX_SM_UserPreferences, UserPreferencesandEmailSettings, UserPreferences
Non-filterable, non-selectable: NoteText

PX.SM.UserPreferences.UserID : Edm.Guid [key] "UserID"
PX.SM.UserPreferences.DefaultEMailAccountID : Edm.Int32 "Default Email Account"
PX.SM.UserPreferences.HomePage : Edm.Guid "Home Page"
PX.SM.UserPreferences.DefBranchID : Edm.Int32 "Default Branch"
PX.SM.UserPreferences.tstamp : Edm.Binary
PX.SM.UserPreferences.PdfCertificateName : Edm.String "PDF Signing Certificate"
PX.SM.UserPreferences.SignatureToReplyAndForward : Edm.Boolean [required] "Include in Replies and Forwarded Emails"
PX.SM.UserPreferences.SignatureToNewEmail : Edm.Boolean [required] "Include in New Emails"
PX.SM.UserPreferences.MailSignature : Edm.String "Signature"
PX.SM.UserPreferences.CreatedByID : Edm.Guid "Created By"
PX.SM.UserPreferences.CreatedByScreenID : Edm.String
PX.SM.UserPreferences.CreatedDateTime : Edm.DateTimeOffset
PX.SM.UserPreferences.LastModifiedByID : Edm.Guid "Last Modified By"
PX.SM.UserPreferences.LastModifiedByScreenID : Edm.String
PX.SM.UserPreferences.LastModifiedDateTime : Edm.DateTimeOffset
PX.SM.UserPreferences.EntityDefaultSearch : Edm.String
PX.SM.UserPreferences.DefaultTheme : Edm.String "Default Theme"
PX.SM.UserPreferences.TimeZone : Edm.String "Time Zone"
PX.SM.UserPreferences.NoteID : Edm.Guid
PX.SM.UserPreferences.NoteText : Edm.String "Note Text"
PX.SM.UserPreferences.DisableSuggest : Edm.Boolean "Lookup Box Suggestions"
PX.SM.UserPreferences.EnableSmartSuggest : Edm.Boolean [required] "Intelligent Text Completion"
PX.SM.UserPreferences.TrackLocation : Edm.Boolean "Track Location"
PX.SM.UserPreferences.Interval : Edm.Int16 "Tracking Frequency"
PX.SM.UserPreferences.Distance : Edm.Int16 "Distance Frequency"
PX.SM.UserPreferences.BranchByDefBranchID -> PX.Objects.GL.Branch (DefBranchID=BranchID)
PX.SM.UserPreferences.UsersByUserID -> PX.SM.Users (UserID=PKID)
PX.SM.UserPreferences.UsersByCreatedByID -> PX.SM.Users (CreatedByID=PKID)
PX.SM.UserPreferences.UsersByLastModifiedByID -> PX.SM.Users (LastModifiedByID=PKID)
PX.SM.UserPreferences.EMailAccountByDefaultEMailAccountID -> PX.SM.EMailAccount (DefaultEMailAccountID=EmailAccountID)
PX.SM.UserPreferences.SMPrinterByDefaultPrinterID -> PX.SM.SMPrinter
PX.SM.UserPreferences.SMScaleByDefaultScalesID -> PX.SM.SMScale
PX.SM.UserPreferences.SMScannerByDefaultScannerID -> PX.SM.SMScanner
PX.SM.UserPreferences.INSiteByDefaultSite -> PX.Objects.IN.INSite
PX.SM.UserPreferences.FSBranchLocationByDefBranchID -> PX.Objects.FS.FSBranchLocation (DefBranchID=BranchID)
PX.SM.UserPreferences.FSSrvOrdTypeByDfltSrvOrdType -> PX.Objects.FS.FSSrvOrdType
PX.SM.UserPreferences.CertificateByPdfCertificateName -> PX.SM.Certificate (PdfCertificateName=Name)

# PX.SM.UserReportEx (EntityType)

BaseType: PX.Data.Reports.UserReport
Key: ReportFileName, Version (inherited from PX.Data.Reports.UserReport)
Entity sets: PX_SM_UserReportEx

PX.SM.UserReportEx.CompanyId : Edm.Int32 "CompanyId"

# PX.SM.Users (EntityType)

Label: "User"
Key: Username
Entity sets: PX_SM_Users, User, Users
Non-filterable, non-selectable: Domain, DisplayName, IsADUser, ContactID, GeneratePassword, OldPassword, NewPassword, ConfirmPassword, RecoveryLink, TwoFactorCode, IsLockedOut, State, Included, ActivationID, NoteText, EntityTypeID, chkServiceManagement, IsUserUpdated, IsUserDisable, DeletedDatabaseRecord

PX.SM.Users.PKID : Edm.Guid "PKID"
PX.SM.Users.Username : Edm.String [key] "Login"
PX.SM.Users.Domain : Edm.String "Domain"
PX.SM.Users.DisplayName : Edm.String "Display Name"
PX.SM.Users.ExtRef : Edm.String
PX.SM.Users.Source : Edm.Int32 [required] "Source"
PX.SM.Users.FirstName : Edm.String "First Name"
PX.SM.Users.IsADUser : Edm.Boolean
PX.SM.Users.LastName : Edm.String "Last Name"
PX.SM.Users.FullName : Edm.String "Full Name"
PX.SM.Users.ApplicationName : Edm.String "ApplicationName"
PX.SM.Users.Email : Edm.String "Email"
PX.SM.Users.Phone : Edm.String "Phone"
PX.SM.Users.Comment : Edm.String "Comment"
PX.SM.Users.LoginTypeID : Edm.Int32 "User Type"
PX.SM.Users.ContactID : Edm.Int32 "Linked Entity"
PX.SM.Users.GeneratePassword : Edm.Boolean "Generate Password"
PX.SM.Users.Password : Edm.String "Password"
PX.SM.Users.OldPassword : Edm.String "Old Password"
PX.SM.Users.NewPassword : Edm.String "New Password"
PX.SM.Users.ConfirmPassword : Edm.String "Confirm Password"
PX.SM.Users.AllowPasswordRecovery : Edm.Boolean [required] "Allow Password Recovery"
PX.SM.Users.PasswordQuestion : Edm.String "Password Recovery Question"
PX.SM.Users.PasswordAnswer : Edm.String "Password Recovery Answer"
PX.SM.Users.RecoveryLink : Edm.String "Password Recovery Link"
PX.SM.Users.TwoFactorCode : Edm.String "TwoFactorCode"
PX.SM.Users.PasswordChangeOnNextLogin : Edm.Boolean [required] "Force User to Change Password on Next Login"
PX.SM.Users.PasswordChangeable : Edm.Boolean [required] "Allow Password Changes"
PX.SM.Users.PasswordNeverExpires : Edm.Boolean [required] "Password Never Expires"
PX.SM.Users.IsHidden : Edm.Boolean [required]
PX.SM.Users.IsApproved : Edm.Boolean [required] "Activate Account"
PX.SM.Users.IsPendingActivation : Edm.Boolean
PX.SM.Users.Guest : Edm.Boolean [required] "Guest Account"
PX.SM.Users.IsAssigned : Edm.Boolean [required]
PX.SM.Users.LastActivityDate : Edm.DateTimeOffset "Last Activity Date"
PX.SM.Users.LastLoginDate : Edm.DateTimeOffset "Last Login Date"
PX.SM.Users.LastPasswordChangedDate : Edm.DateTimeOffset "Last Password Change Date"
PX.SM.Users.CreationDate : Edm.DateTimeOffset "Account Creation Date"
PX.SM.Users.IsOnLine : Edm.Boolean [required] "Is Online"
PX.SM.Users.LockedOutDate : Edm.DateTimeOffset
PX.SM.Users.IsLockedOut : Edm.Boolean "Temporarily Lock Out Account"
PX.SM.Users.OverrideADRoles : Edm.Boolean [required] "Override Active Directory Roles with Local Roles"
PX.SM.Users.LastLockedOutDate : Edm.DateTimeOffset "Last Lockout Date"
PX.SM.Users.FailedPasswordAttemptCount : Edm.Int32 "Number of Unsuccessful Attempts To Enter Password"
PX.SM.Users.FailedPasswordAttemptWindowStart : Edm.DateTimeOffset "FailedPasswordAttemptWindowStart"
PX.SM.Users.FailedPasswordAnswerAttemptCount : Edm.Int32 "Number of Unsuccessful Attempts To Enter Recovery Answer"
PX.SM.Users.FailedPasswordAnswerAttemptWindowStart : Edm.DateTimeOffset "FailedPasswordAnswerAttemptWindowStart"
PX.SM.Users.State : Edm.String "Status"
PX.SM.Users.Included : Edm.Boolean "Included"
PX.SM.Users.ActivationID : Edm.String
PX.SM.Users.NoteID : Edm.Guid
PX.SM.Users.NoteText : Edm.String "Note Text"
PX.SM.Users.MultiFactorType : Edm.Int32 [required] "Two-Factor Authentication"
PX.SM.Users.MultiFactorOverride : Edm.Boolean [required] "Override Security Preferences"
PX.SM.Users.AllowedSessions : Edm.Int32 "Max. Number of Concurrent Logins"
PX.SM.Users.ForbidLoginWithPassword : Edm.Boolean [required] "Forbid Login with Password"
PX.SM.Users.OverrideLocalRolesWithOidcProviderRoles : Edm.Boolean [required] "Use Roles from Provider Settings"
PX.SM.Users.EntityTypeID : Edm.Int32
PX.SM.Users.chkServiceManagement : Edm.Boolean "chkServiceManagement"
PX.SM.Users.IsUserUpdated : Edm.Boolean
PX.SM.Users.IsUserDisable : Edm.Boolean
PX.SM.Users.DeletedDatabaseRecord : Edm.Boolean [required] "DeletedDatabaseRecord"
PX.SM.Users.SiteMapInProjectCollection -> Collection(PX.SM.SiteMapInProject)
PX.SM.Users.WikiDescriptorExtCollection -> Collection(PX.SM.WikiDescriptorExt)
PX.SM.Users.EPEmployeeCollection -> Collection(PX.Objects.EP.EPEmployee)
PX.SM.Users.PMLinkedFileCollection -> Collection(PX.Objects.PM.ProjectFiles.FileEntryForms.PMLinkedFile)
PX.SM.Users.UploadFileWithIDSelectorCollection -> Collection(PX.SM.UploadFileWithIDSelector)
PX.SM.Users.ARRetainageWithApplicationsCollection -> Collection(PX.Objects.AR.ARRetainageWithApplications)
PX.SM.Users.MUIScreenCollection -> Collection(PX.Web.UI.Frameset.Model.DAC.MUIScreen)
PX.SM.Users.MUITileCollection -> Collection(PX.Web.UI.Frameset.Model.DAC.MUITile)
PX.SM.Users.WikiDescriptorCollection -> Collection(PX.SM.WikiDescriptor)
PX.SM.Users.WikiPageCollection -> Collection(PX.SM.WikiPage)
PX.SM.Users.DiscrepancyByAccountEnqResultCollection -> Collection(ReconciliationTools.DiscrepancyByAccountEnqResult)
PX.SM.Users.WikiSitePageCollection -> Collection(PX.SM.WikiSitePage)
PX.SM.Users.WikiNotificationTemplateCollection -> Collection(PX.SM.WikiNotificationTemplate)
PX.SM.Users.TaxTranReportCollection -> Collection(PX.Objects.TX.TaxTranReport)
PX.SM.Users.TaxTranCollection -> Collection(PX.Objects.TX.TaxTran)
PX.SM.Users.SOTaxTranCollection -> Collection(PX.Objects.SO.SOTaxTran)
PX.SM.Users.ARPaymentCollection -> Collection(PX.Objects.AR.ARPayment)
PX.SM.Users.PMProjectCollection -> Collection(PX.Objects.PM.PMProject)
PX.SM.Users.POTaxTranCollection -> Collection(PX.Objects.PO.POTaxTran)
PX.SM.Users.PMChangeRequestTaxCollection -> Collection(PX.Objects.PM.PMChangeRequestTax)
PX.SM.Users.PMChangeRequestTaxTranCollection -> Collection(PX.Objects.PM.PMChangeRequestTaxTran)
PX.SM.Users.GLTaxCollection -> Collection(PX.Objects.GL.GLTax)
PX.SM.Users.VendorCollection -> Collection(PX.Objects.AP.Vendor)
PX.SM.Users.CRPMTimeActivityCollection -> Collection(PX.Objects.CR.CRPMTimeActivity)
PX.SM.Users.CRSMEmailCollection -> Collection(PX.Objects.CR.CRSMEmail)
PX.SM.Users.ARInvoiceCollection -> Collection(PX.Objects.AR.ARInvoice)
PX.SM.Users.EPActivityReleaseCollection -> Collection(PX.Objects.EP.EPActivityRelease)
PX.SM.Users.CustomerCollection -> Collection(PX.Objects.AR.Customer)
PX.SM.Users.ARTaxCollection -> Collection(PX.Objects.AR.ARTax)
PX.SM.Users.EPActivityApprove2Collection -> Collection(PX.Objects.EP.EPActivityApprove2)
PX.SM.Users.APInvoiceCollection -> Collection(PX.Objects.AP.APInvoice)
PX.SM.Users.ComplianceDocumentReferenceCollection -> Collection(PX.Objects.CN.Compliance.CL.DAC.ComplianceDocumentReference)
PX.SM.Users.FSAppointmentTaxCollection -> Collection(PX.Objects.FS.FSAppointmentTax)
PX.SM.Users.FSServiceOrderTaxCollection -> Collection(PX.Objects.FS.FSServiceOrderTax)
PX.SM.Users.RequestForInformationCollection -> Collection(PX.Objects.PJ.RequestsForInformation.PJ.DAC.RequestForInformation)
PX.SM.Users.ProjectIssueCollection -> Collection(PX.Objects.PJ.ProjectsIssue.PJ.DAC.ProjectIssue)
PX.SM.Users.ProjectManagementSetupCollection -> Collection(PX.Objects.PJ.ProjectManagement.PJ.DAC.ProjectManagementSetup)
PX.SM.Users.APPaymentCollection -> Collection(PX.Objects.AP.APPayment)
PX.SM.Users.WikiArticleCollection -> Collection(PX.SM.WikiArticle)
PX.SM.Users.DrawingLogCollection -> Collection(PX.Objects.PJ.DrawingLogs.PJ.DAC.DrawingLog)
PX.SM.Users.EPCompanyTreeMasterCollection -> Collection(PX.TM.EPCompanyTreeMaster)
PX.SM.Users.ARRegisterCollection -> Collection(PX.Objects.AR.ARRegister)
PX.SM.Users.CustObjectCollection -> Collection(PX.SM.CustObject)
PX.SM.Users.SiteMapCollection -> Collection(PX.SM.SiteMap)
PX.SM.Users.UserReportCollection -> Collection(PX.Data.Reports.UserReport)
PX.SM.Users.MobileSiteMapCollection -> Collection(PX.SM.MobileSiteMap)
PX.SM.Users.BPEventCollection -> Collection(PX.BusinessProcess.DAC.BPEvent)
PX.SM.Users.DashboardCollection -> Collection(PX.Dashboards.DAC.Dashboard)
PX.SM.Users.DashboardV2Collection -> Collection(PX.Dashboards.DAC.DashboardV2)
PX.SM.Users.GIDesignCollection -> Collection(PX.Data.Maintenance.GI.GIDesign)
PX.SM.Users.SYMappingCollection -> Collection(PX.Api.SYMapping)
PX.SM.Users.RMReportCollection -> Collection(PX.CS.RMReport)
PX.SM.Users.SYMappingFieldCollection -> Collection(PX.Api.SYMappingField)
PX.SM.Users.AuditHistoryCollection -> Collection(PX.SM.AuditHistory)
PX.SM.Users.AUScreenItemCollection -> Collection(PX.SM.AUScreenItem)
PX.SM.Users.AUScreenItemPropCollection -> Collection(PX.SM.AUScreenItemProp)
PX.SM.Users.AUScreenConditionFilterCollection -> Collection(PX.SM.AUScreenConditionFilter)
PX.SM.Users.UPSnapshotCollection -> Collection(PX.SM.UPSnapshot)
PX.SM.Users.UploadFileRevisionCollection -> Collection(PX.SM.UploadFileRevision)
PX.SM.Users.UploadFileCollection -> Collection(PX.SM.UploadFile)
PX.SM.Users.WikiRevisionCollection -> Collection(PX.SM.WikiRevision)
PX.SM.Users.AUScheduleCollection -> Collection(PX.SM.AUSchedule)
PX.SM.Users.RecognizedRecordCollection -> Collection(PX.CloudServices.DAC.RecognizedRecord)
PX.SM.Users.SVATConversionHistCollection -> Collection(PX.Objects.TX.SVATConversionHist)
PX.SM.Users.SOBlanketOrderLinkCollection -> Collection(PX.Objects.SO.SOBlanketOrderLink)
PX.SM.Users.SOAddressCollection -> Collection(PX.Objects.SO.SOAddress)
PX.SM.Users.SOPickingJobCollection -> Collection(PX.Objects.SO.SOPickingJob)
PX.SM.Users.SOContactCollection -> Collection(PX.Objects.SO.SOContact)
PX.SM.Users.NotificationSetupCollection -> Collection(PX.Objects.CS.NotificationSetup)
PX.SM.Users.SOPackageDetailCollection -> Collection(PX.Objects.SO.SOPackageDetail)
PX.SM.Users.SOPackageInfoCollection -> Collection(PX.Objects.SO.SOPackageInfo)
PX.SM.Users.SOTaxCollection -> Collection(PX.Objects.SO.SOTax)
PX.SM.Users.SOOrderCollection -> Collection(PX.Objects.SO.SOOrder)
PX.SM.Users.RQRequisitionLineCollection -> Collection(PX.Objects.RQ.RQRequisitionLine)
PX.SM.Users.RQRequestLineCollection -> Collection(PX.Objects.RQ.RQRequestLine)
PX.SM.Users.POLandedCostTaxCollection -> Collection(PX.Objects.PO.POLandedCostTax)
PX.SM.Users.POLandedCostTaxTranCollection -> Collection(PX.Objects.PO.POLandedCostTaxTran)
PX.SM.Users.POTaxCollection -> Collection(PX.Objects.PO.POTax)
PX.SM.Users.INItemPlanCollection -> Collection(PX.Objects.IN.INItemPlan)
PX.SM.Users.PMChangeOrderTaxCollection -> Collection(PX.Objects.PM.PMChangeOrderTax)
PX.SM.Users.POLineCollection -> Collection(PX.Objects.PO.POLine)
PX.SM.Users.POOrderCollection -> Collection(PX.Objects.PO.POOrder)
PX.SM.Users.POAddressCollection -> Collection(PX.Objects.PO.POAddress)
PX.SM.Users.POContactCollection -> Collection(PX.Objects.PO.POContact)
PX.SM.Users.PMAddressCollection -> Collection(PX.Objects.PM.PMAddress)
PX.SM.Users.PMContactCollection -> Collection(PX.Objects.PM.PMContact)
PX.SM.Users.PMBudgetCollection -> Collection(PX.Objects.PM.PMBudget)
PX.SM.Users.PMChangeOrderBudgetCollection -> Collection(PX.Objects.PM.PMChangeOrderBudget)
PX.SM.Users.PMChangeOrderTaxTranCollection -> Collection(PX.Objects.PM.PMChangeOrderTaxTran)
PX.SM.Users.PMTaxCollection -> Collection(PX.Objects.PM.PMTax)
PX.SM.Users.PMProformaLineCollection -> Collection(PX.Objects.PM.PMProformaLine)
PX.SM.Users.PMProgressWorksheetLineCollection -> Collection(PX.Objects.PM.PMProgressWorksheetLine)
PX.SM.Users.PMTaxTranCollection -> Collection(PX.Objects.PM.PMTaxTran)
PX.SM.Users.PMTaskCollection -> Collection(PX.Objects.PM.PMTask)
PX.SM.Users.TagCollection -> Collection(PX.Data.Wiki.Tags.Tag)
PX.SM.Users.FixedAssetCollection -> Collection(PX.Objects.FA.FixedAsset)
PX.SM.Users.FATranCollection -> Collection(PX.Objects.FA.FATran)
PX.SM.Users.FABookCollection -> Collection(PX.Objects.FA.FABook)
PX.SM.Users.FADetailsCollection -> Collection(PX.Objects.FA.FADetails)
PX.SM.Users.ContractCollection -> Collection(PX.Objects.CT.Contract)
PX.SM.Users.BAccountCollection -> Collection(PX.Objects.CR.BAccount)
PX.SM.Users.INItemBoxCollection -> Collection(PX.Objects.IN.INItemBox)
PX.SM.Users.INItemClassCollection -> Collection(PX.Objects.IN.INItemClass)
PX.SM.Users.INTranCollection -> Collection(PX.Objects.IN.INTran)
PX.SM.Users.INTranSplitCollection -> Collection(PX.Objects.IN.INTranSplit)
PX.SM.Users.InventoryItemCollection -> Collection(PX.Objects.IN.InventoryItem)
PX.SM.Users.INRegisterCollection -> Collection(PX.Objects.IN.INRegister)
PX.SM.Users.MultipleQuoteCollection -> Collection(PX.Objects.CN.CRM.CR.DAC.MultipleQuote)
PX.SM.Users.INMatrixGenerationRuleCollection -> Collection(PX.Objects.IN.Matrix.DAC.INMatrixGenerationRule)
PX.SM.Users.INMatrixExcludedDataCollection -> Collection(PX.Objects.IN.Matrix.DAC.INMatrixExcludedData)
PX.SM.Users.LienWaiverRecipientCollection -> Collection(PX.Objects.CN.Compliance.PM.DAC.LienWaiverRecipient)
PX.SM.Users.ComplianceAttributeCollection -> Collection(PX.Objects.CN.Compliance.CL.DAC.ComplianceAttribute)
PX.SM.Users.LienWaiverSetupCollection -> Collection(PX.Objects.CN.Compliance.CL.DAC.LienWaiverSetup)
PX.SM.Users.CurrencyRateCollection -> Collection(PX.Objects.CM.CurrencyRate)
PX.SM.Users.GLTranCollection -> Collection(PX.Objects.GL.GLTran)
PX.SM.Users.INSiteCollection -> Collection(PX.Objects.IN.INSite)
PX.SM.Users.BatchCollection -> Collection(PX.Objects.GL.Batch)
PX.SM.Users.CABankChargeTaxCollection -> Collection(PX.Objects.CA.CABankChargeTax)
PX.SM.Users.LedgerCollection -> Collection(PX.Objects.GL.Ledger)
PX.SM.Users.FinPeriodCollection -> Collection(PX.Objects.GL.FinPeriods.TableDefinition.FinPeriod)
PX.SM.Users.OrganizationCollection -> Collection(PX.Objects.GL.DAC.Organization)
PX.SM.Users.CABankTaxCollection -> Collection(PX.Objects.CA.CABankTax)
PX.SM.Users.CABankTaxTranCollection -> Collection(PX.Objects.CA.CABankTaxTran)
PX.SM.Users.CABankTaxTranMatchCollection -> Collection(PX.Objects.CA.CABankTaxTranMatch)
PX.SM.Users.CAExpenseTaxCollection -> Collection(PX.Objects.CA.CAExpenseTax)
PX.SM.Users.CABankTranRuleCollection -> Collection(PX.Objects.CA.CABankTranRule)
PX.SM.Users.CABatchDetailCollection -> Collection(PX.Objects.CA.CABatchDetail)
PX.SM.Users.CATaxCollection -> Collection(PX.Objects.CA.CATax)
PX.SM.Users.ContactCollection -> Collection(PX.Objects.CR.Contact)
PX.SM.Users.APAdjustCollection -> Collection(PX.Objects.AP.APAdjust)
PX.SM.Users.CATranCollection -> Collection(PX.Objects.CA.CATran)
PX.SM.Users.AddressCollection -> Collection(PX.Objects.CR.Address)
PX.SM.Users.NotificationRecipientCollection -> Collection(PX.Objects.CS.NotificationRecipient)
PX.SM.Users.CRContactClassCollection -> Collection(PX.Objects.CR.CRContactClass)
PX.SM.Users.CRActivityCollection -> Collection(PX.Objects.CR.CRActivity)
PX.SM.Users.CRAddressCollection -> Collection(PX.Objects.CR.CRAddress)
PX.SM.Users.CRContactCollection -> Collection(PX.Objects.CR.CRContact)
PX.SM.Users.CRCustomerClassCollection -> Collection(PX.Objects.CR.CRCustomerClass)
PX.SM.Users.CRLeadCollection -> Collection(PX.Objects.CR.CRLead)
PX.SM.Users.CRLeadClassCollection -> Collection(PX.Objects.CR.CRLeadClass)
PX.SM.Users.CROpportunityClassCollection -> Collection(PX.Objects.CR.CROpportunityClass)
PX.SM.Users.CRMarketingListCollection -> Collection(PX.Objects.CR.CRMarketingList)
PX.SM.Users.CROpportunityTaxCollection -> Collection(PX.Objects.CR.CROpportunityTax)
PX.SM.Users.CRTaxTranCollection -> Collection(PX.Objects.CR.CRTaxTran)
PX.SM.Users.ARAdjustCollection -> Collection(PX.Objects.AR.ARAdjust)
PX.SM.Users.EPEmployeeClassCollection -> Collection(PX.Objects.EP.EPEmployeeClass)
PX.SM.Users.ARAddressCollection -> Collection(PX.Objects.AR.ARAddress)
PX.SM.Users.ARContactCollection -> Collection(PX.Objects.AR.ARContact)
PX.SM.Users.DiscountSequenceDetailCollection -> Collection(PX.Objects.AR.DiscountSequenceDetail)
PX.SM.Users.APRegisterCollection -> Collection(PX.Objects.AP.APRegister)
PX.SM.Users.EPRuleConditionCollection -> Collection(PX.Objects.EP.EPRuleCondition)
PX.SM.Users.EPRuleCollection -> Collection(PX.Objects.EP.EPRule)
PX.SM.Users.EPRuleEmployeeConditionCollection -> Collection(PX.Objects.EP.EPRuleEmployeeCondition)
PX.SM.Users.EPTaxCollection -> Collection(PX.Objects.EP.EPTax)
PX.SM.Users.EPTaxAggregateCollection -> Collection(PX.Objects.EP.EPTaxAggregate)
PX.SM.Users.EPTaxTranCollection -> Collection(PX.Objects.EP.EPTaxTran)
PX.SM.Users.VendorDiscountSequenceCollection -> Collection(PX.Objects.AP.VendorDiscountSequence)
PX.SM.Users.EPViewCollection -> Collection(PX.Objects.EP.EPView)
PX.SM.Users.PMTimeActivityCollection -> Collection(PX.Objects.CR.PMTimeActivity)
PX.SM.Users.EPTimeCardCollection -> Collection(PX.Objects.EP.EPTimeCard)
PX.SM.Users.EPExpenseClaimCollection -> Collection(PX.Objects.EP.EPExpenseClaim)
PX.SM.Users.APTaxCollection -> Collection(PX.Objects.AP.APTax)
PX.SM.Users.RQRequisitionCollection -> Collection(PX.Objects.RQ.RQRequisition)
PX.SM.Users.PMCostProjectionByDateCollection -> Collection(PX.Objects.PM.PMCostProjectionByDate)
PX.SM.Users.DRDeferredCodeCollection -> Collection(PX.Objects.DR.DRDeferredCode)
PX.SM.Users.DRScheduleCollection -> Collection(PX.Objects.DR.DRSchedule)
PX.SM.Users.DRScheduleDetailCollection -> Collection(PX.Objects.DR.DRScheduleDetail)
PX.SM.Users.INCategoryCollection -> Collection(PX.Objects.IN.INCategory)
PX.SM.Users.GLAllocationCollection -> Collection(PX.Objects.GL.GLAllocation)
PX.SM.Users.GLTrialBalanceImportDetailsCollection -> Collection(PX.Objects.GL.GLTrialBalanceImportDetails)
PX.SM.Users.CABankTranCollection -> Collection(PX.Objects.CA.CABankTran)
PX.SM.Users.ARDiscountCollection -> Collection(PX.Objects.AR.ARDiscount)
PX.SM.Users.ARSalesPerTranCollection -> Collection(PX.Objects.AR.ARSalesPerTran)
PX.SM.Users.EPApprovalCollection -> Collection(PX.Objects.EP.EPApproval)
PX.SM.Users.EPEquipmentTimeCardCollection -> Collection(PX.Objects.EP.EPEquipmentTimeCard)
PX.SM.Users.EPExpenseClaimDetailsCollection -> Collection(PX.Objects.EP.EPExpenseClaimDetails)
PX.SM.Users.EPTimeCardSummaryCollection -> Collection(PX.Objects.EP.EPTimeCardSummary)
PX.SM.Users.WebHookCollection -> Collection(PX.Api.Webhooks.DAC.WebHook)
PX.SM.Users.RolesCollection -> Collection(PX.SM.Roles)
PX.SM.Users.AMProdItemCollection -> Collection(PX.Objects.AM.AMProdItem)
PX.SM.Users.AMBomItemCollection -> Collection(PX.Objects.AM.AMBomItem)
PX.SM.Users.AMMTranAttributeCollection -> Collection(PX.Objects.AM.AMMTranAttribute)
PX.SM.Users.AMMTranCollection -> Collection(PX.Objects.AM.AMMTran)
PX.SM.Users.AMMTranSplitCollection -> Collection(PX.Objects.AM.AMMTranSplit)
PX.SM.Users.AMProdOperCollection -> Collection(PX.Objects.AM.AMProdOper)
PX.SM.Users.SOLineCollection -> Collection(PX.Objects.SO.SOLine)
PX.SM.Users.FSLogCollection -> Collection(PX.Objects.FS.FSLog)
PX.SM.Users.AMMachSchdCollection -> Collection(PX.Objects.AM.AMMachSchd)
PX.SM.Users.AMProdMatlCollection -> Collection(PX.Objects.AM.AMProdMatl)
PX.SM.Users.AMWCSchdCollection -> Collection(PX.Objects.AM.AMWCSchd)
PX.SM.Users.FSScheduleCollection -> Collection(PX.Objects.FS.FSSchedule)
PX.SM.Users.FSAddressCollection -> Collection(PX.Objects.FS.FSAddress)
PX.SM.Users.FSAppointmentDetCollection -> Collection(PX.Objects.FS.FSAppointmentDet)
PX.SM.Users.FSAppointmentTaxTranCollection -> Collection(PX.Objects.FS.FSAppointmentTaxTran)
PX.SM.Users.FSServiceOrderCollection -> Collection(PX.Objects.FS.FSServiceOrder)
PX.SM.Users.FSCalendarComponentFieldCollection -> Collection(PX.Objects.FS.FSCalendarComponentField)
PX.SM.Users.FSContactCollection -> Collection(PX.Objects.FS.FSContact)
PX.SM.Users.FSGPSTrackingRequestCollection -> Collection(PX.FS.FSGPSTrackingRequest)
PX.SM.Users.FSServiceOrderTaxTranCollection -> Collection(PX.Objects.FS.FSServiceOrderTaxTran)
PX.SM.Users.FSSODetCollection -> Collection(PX.Objects.FS.FSSODet)
PX.SM.Users.FSAppointmentCollection -> Collection(PX.Objects.FS.FSAppointment)
PX.SM.Users.FSDiscountDetailCollection -> Collection(PX.Objects.FS.FSDiscountDetail)
PX.SM.Users.SOOrderTypeCollection -> Collection(PX.Objects.SO.SOOrderType)
PX.SM.Users.FSEquipmentCollection -> Collection(PX.Objects.FS.FSEquipment)
PX.SM.Users.PJSubmittalCollection -> Collection(PX.Objects.PJ.Submittals.PJ.DAC.PJSubmittal)
PX.SM.Users.ProjectManagementClassCollection -> Collection(PX.Objects.PJ.ProjectManagement.PJ.DAC.ProjectManagementClass)
PX.SM.Users.ProjectManagementClassPriorityCollection -> Collection(PX.Objects.PJ.ProjectManagement.PJ.DAC.ProjectManagementClassPriority)
PX.SM.Users.PhotoLogCollection -> Collection(PX.Objects.PJ.PhotoLogs.PJ.DAC.PhotoLog)
PX.SM.Users.PhotoLogSetupCollection -> Collection(PX.Objects.PJ.PhotoLogs.PJ.DAC.PhotoLogSetup)
PX.SM.Users.DrawingLogSetupCollection -> Collection(PX.Objects.PJ.DrawingLogs.PJ.DAC.DrawingLogSetup)
PX.SM.Users.DailyFieldReportCollection -> Collection(PX.Objects.PJ.DailyFieldReports.PJ.DAC.DailyFieldReport)
PX.SM.Users.DailyFieldReportCopyConfigurationCollection -> Collection(PX.Objects.PJ.DailyFieldReports.PJ.DAC.DailyFieldReportCopyConfiguration)
PX.SM.Users.DailyFieldReportHistoryCollection -> Collection(PX.Objects.PJ.DailyFieldReports.PJ.DAC.DailyFieldReportHistory)
PX.SM.Users.DailyFieldReportNoteCollection -> Collection(PX.Objects.PJ.DailyFieldReports.PJ.DAC.DailyFieldReportNote)
PX.SM.Users.DailyFieldReportSubcontractorActivityCollection -> Collection(PX.Objects.PJ.DailyFieldReports.PJ.DAC.DailyFieldReportSubcontractorActivity)
PX.SM.Users.DailyFieldReportVisitorCollection -> Collection(PX.Objects.PJ.DailyFieldReports.PJ.DAC.DailyFieldReportVisitor)
PX.SM.Users.DailyFieldReportWeatherCollection -> Collection(PX.Objects.PJ.DailyFieldReports.PJ.DAC.DailyFieldReportWeather)
PX.SM.Users.EPEquipmentDetailCollection -> Collection(PX.Objects.EP.EPEquipmentDetail)
PX.SM.Users.WeatherIntegrationSetupCollection -> Collection(PX.Objects.PJ.DailyFieldReports.PJ.DAC.WeatherIntegrationSetup)
PX.SM.Users.WeatherProcessingLogCollection -> Collection(PX.Objects.PJ.DailyFieldReports.PJ.DAC.WeatherProcessingLog)
PX.SM.Users.SVTaxCollection -> Collection(PX.Objects.SV.SVTax)
PX.SM.Users.CRCaseCollection -> Collection(PX.Objects.CR.CRCase)
PX.SM.Users.CABatchCollection -> Collection(PX.Objects.CA.CABatch)
PX.SM.Users.PRDeductCodeDetailCollection -> Collection(PX.Objects.PR.PRDeductCodeDetail)
PX.SM.Users.FSLicenseCollection -> Collection(PX.Objects.SV.FSLicense)
PX.SM.Users.FSEmployeeSkillCollection -> Collection(PX.Objects.SV.FSEmployeeSkill)
PX.SM.Users.FSLicenseTypeCollection -> Collection(PX.Objects.SV.FSLicenseType)
PX.SM.Users.FSGeoZonePostalCodeCollection -> Collection(PX.Objects.SV.FSGeoZonePostalCode)
PX.SM.Users.FSGeoZoneCollection -> Collection(PX.Objects.SV.FSGeoZone)
PX.SM.Users.FSSkillCollection -> Collection(PX.Objects.SV.FSSkill)
PX.SM.Users.SVTaxTranCollection -> Collection(PX.Objects.SV.SVTaxTran)
PX.SM.Users.SVTicketCollection -> Collection(PX.Objects.SV.SVTicket)
PX.SM.Users.SVResourceCollection -> Collection(PX.Objects.SV.SVResource)
PX.SM.Users.SVEventCollection -> Collection(PX.Objects.SV.SVEvent)
PX.SM.Users.SVWorkTaskTemplateCollection -> Collection(PX.Objects.SV.SVWorkTaskTemplate)
PX.SM.Users.PPBillcomVendorCollection -> Collection(PX.PaymentProcessor.BillCom.DAC.PPBillcomVendor)
PX.SM.Users.MUIAreaCollection -> Collection(PX.Web.UI.Frameset.Model.DAC.MUIArea)
PX.SM.Users.MUIFavoriteScreenCollection -> Collection(PX.Web.UI.Frameset.Model.DAC.MUIFavoriteScreen)
PX.SM.Users.MUIFavoriteTileCollection -> Collection(PX.Web.UI.Frameset.Model.DAC.MUIFavoriteTile)
PX.SM.Users.MUIFavoriteWorkspaceCollection -> Collection(PX.Web.UI.Frameset.Model.DAC.MUIFavoriteWorkspace)
PX.SM.Users.MUIPinnedScreenCollection -> Collection(PX.Web.UI.Frameset.Model.DAC.MUIPinnedScreen)
PX.SM.Users.MUISubcategoryCollection -> Collection(PX.Web.UI.Frameset.Model.DAC.MUISubcategory)
PX.SM.Users.MUIUserPreferencesCollection -> Collection(PX.Web.UI.Frameset.Model.DAC.MUIUserPreferences)
PX.SM.Users.MUIWorkspaceCollection -> Collection(PX.Web.UI.Frameset.Model.DAC.MUIWorkspace)
PX.SM.Users.SCSetupCollection -> Collection(PX.Objects.CN.SCSetup)
PX.SM.Users.SMDeletedRecordsTrackingTablesCollection -> Collection(PX.Data.DeletedRecordsTracking.DAC.SMDeletedRecordsTrackingTables)
PX.SM.Users.RolesInGraphCollection -> Collection(PX.SM.RolesInGraph)
PX.SM.Users.RolesInCacheCollection -> Collection(PX.SM.RolesInCache)
PX.SM.Users.RolesInMemberCollection -> Collection(PX.SM.RolesInMember)
PX.SM.Users.POReceiptLineCollection -> Collection(PX.Objects.PO.POReceiptLine)
PX.SM.Users.POVendorInventoryCollection -> Collection(PX.Objects.PO.POVendorInventory)
PX.SM.Users.APTranCollection -> Collection(PX.Objects.AP.APTran)
PX.SM.Users.PMChangeOrderCollection -> Collection(PX.Objects.PM.PMChangeOrder)
PX.SM.Users.PMForecastDetailCollection -> Collection(PX.Objects.PM.PMForecastDetail)
PX.SM.Users.PMSetupCollection -> Collection(PX.Objects.PM.PMSetup)
PX.SM.Users.FABookHistoryCollection -> Collection(PX.Objects.FA.FABookHistory)
PX.SM.Users.FABookPeriodCollection -> Collection(PX.Objects.FA.FABookPeriod)
PX.SM.Users.FABookYearCollection -> Collection(PX.Objects.FA.FABookYear)
PX.SM.Users.ContractDetailCollection -> Collection(PX.Objects.CT.ContractDetail)
PX.SM.Users.INItemXRefCollection -> Collection(PX.Objects.IN.INItemXRef)
PX.SM.Users.INItemSiteCollection -> Collection(PX.Objects.IN.INItemSite)
PX.SM.Users.INUnitCollection -> Collection(PX.Objects.IN.INUnit)
PX.SM.Users.JointPayeeCollection -> Collection(PX.Objects.CN.JointChecks.JointPayee)
PX.SM.Users.CurrencyCollection -> Collection(PX.Objects.CM.Currency)
PX.SM.Users.GLBudgetLineCollection -> Collection(PX.Objects.GL.GLBudgetLine)
PX.SM.Users.CashAccountCollection -> Collection(PX.Objects.CA.CashAccount)
PX.SM.Users.CCBatchTransactionCollection -> Collection(PX.Objects.CA.CCBatchTransaction)
PX.SM.Users.PaymentMethodCollection -> Collection(PX.Objects.CA.PaymentMethod)
PX.SM.Users.VendorPaymentMethodDetailCollection -> Collection(PX.Objects.AP.VendorPaymentMethodDetail)
PX.SM.Users.CRCampaignMembersCollection -> Collection(PX.Objects.CR.CRCampaignMembers)
PX.SM.Users.CRMarketingListMemberCollection -> Collection(PX.Objects.CR.CRMarketingListMember)
PX.SM.Users.PMAccountGroupCollection -> Collection(PX.Objects.PM.PMAccountGroup)
PX.SM.Users.CRRelationCollection -> Collection(PX.Objects.CR.CRRelation)
PX.SM.Users.CRSetupCollection -> Collection(PX.Objects.CR.CRSetup)
PX.SM.Users.CRValidationRulesCollection -> Collection(PX.Objects.CR.CRValidationRules)
PX.SM.Users.LocationCollection -> Collection(PX.Objects.CR.Location)
PX.SM.Users.ARDunningCustomerClassCollection -> Collection(PX.Objects.AR.ARDunningCustomerClass)
PX.SM.Users.ARSalesPriceCollection -> Collection(PX.Objects.AR.ARSalesPrice)
PX.SM.Users.TaxCollection -> Collection(PX.Objects.TX.Tax)
PX.SM.Users.VendorClassCollection -> Collection(PX.Objects.AP.VendorClass)
PX.SM.Users.EPSetupCollection -> Collection(PX.Objects.EP.EPSetup)
PX.SM.Users.EPWingmanCollection -> Collection(PX.Objects.EP.EPWingman)
PX.SM.Users.PMCommitmentCollection -> Collection(PX.Objects.PM.PMCommitment)
PX.SM.Users.AccountCollection -> Collection(PX.Objects.GL.Account)
PX.SM.Users.ARTranCollection -> Collection(PX.Objects.AR.ARTran)
PX.SM.Users.PMTranCollection -> Collection(PX.Objects.PM.PMTran)
PX.SM.Users.PMProjectCostSpreadCollection -> Collection(PX.Objects.PM.PMProjectCostSpread)
PX.SM.Users.PMRecurringItemCollection -> Collection(PX.Objects.PM.PMRecurringItem)
PX.SM.Users.SubCollection -> Collection(PX.Objects.GL.Sub)
PX.SM.Users.INSubItemCollection -> Collection(PX.Objects.IN.INSubItem)
PX.SM.Users.INSiteZoneCollection -> Collection(PX.Objects.IN.DAC.INSiteZone)
PX.SM.Users.SOAdjustCollection -> Collection(PX.Objects.SO.SOAdjust)
PX.SM.Users.GLTranDocCollection -> Collection(PX.Objects.GL.GLTranDoc)
PX.SM.Users.CustSalesPeopleCollection -> Collection(PX.Objects.AR.CustSalesPeople)
PX.SM.Users.EPTimeCardItemCollection -> Collection(PX.Objects.EP.EPTimeCardItem)
PX.SM.Users.EPClockInTimerDataCollection -> Collection(PX.Objects.EP.ClockInClockOut.EPClockInTimerData)
PX.SM.Users.APDiscountCollection -> Collection(PX.Objects.AP.APDiscount)
PX.SM.Users.UserPreferencesCollection -> Collection(PX.SM.UserPreferences)
PX.SM.Users.BCSyncStatusCollection -> Collection(PX.Commerce.Core.BCSyncStatus)
PX.SM.Users.INRelatedInventoryCollection -> Collection(PX.Objects.IN.RelatedItems.INRelatedInventory)
PX.SM.Users.AMBatchCollection -> Collection(PX.Objects.AM.AMBatch)
PX.SM.Users.AMWCSchdDetailCollection -> Collection(PX.Objects.AM.AMWCSchdDetail)
PX.SM.Users.T5018MasterTableCollection -> Collection(PX.Objects.Localizations.CA.T5018MasterTable)
PX.SM.Users.PMProjectEntityCollection -> Collection(PX.Objects.PM.ProjectFiles.ProjectEntities.PMProjectEntity)
PX.SM.Users.UploadFileTagCollection -> Collection(PX.Data.Wiki.Tags.UploadFileTag)
PX.SM.Users.CSAttributeGroupCollection -> Collection(PX.Objects.CS.CSAttributeGroup)
PX.SM.Users.CROpportunityProductsCollection -> Collection(PX.Objects.CR.CROpportunityProducts)
PX.SM.Users.SPPortalCollection -> Collection(PX.Objects.Portals.SPPortal)
PX.SM.Users.PRDeductionDetailCollection -> Collection(PX.Objects.PR.PRDeductionDetail)
PX.SM.Users.PRBenefitDetailCollection -> Collection(PX.Objects.PR.PRBenefitDetail)
PX.SM.Users.PRTaxDetailCollection -> Collection(PX.Objects.PR.PRTaxDetail)
PX.SM.Users.PRBatchEmployeeCollection -> Collection(PX.Objects.PR.PRBatchEmployee)
PX.SM.Users.PREarningTypeDetailCollection -> Collection(PX.Objects.PR.PREarningTypeDetail)
PX.SM.Users.PRPaymentEarningCollection -> Collection(PX.Objects.PR.PRPaymentEarning)
PX.SM.Users.PREarningDetailCollection -> Collection(PX.Objects.PR.PREarningDetail)
PX.SM.Users.PRPaymentTaxCollection -> Collection(PX.Objects.PR.PRPaymentTax)
PX.SM.Users.SVEventLaborCollection -> Collection(PX.Objects.SV.SVEventLabor)
PX.SM.Users.SVWorkTaskLaborCollection -> Collection(PX.Objects.SV.SVWorkTaskLabor)
PX.SM.Users.AMEstimateItemCollection -> Collection(PX.Objects.AM.AMEstimateItem)
PX.SM.Users.GIFilterCollection -> Collection(PX.Data.Maintenance.GI.GIFilter)
PX.SM.Users.GIGroupByCollection -> Collection(PX.Data.Maintenance.GI.GIGroupBy)
PX.SM.Users.GINavigationScreenCollection -> Collection(PX.Data.Maintenance.GI.GINavigationScreen)
PX.SM.Users.GINavigationParameterCollection -> Collection(PX.Data.Maintenance.GI.GINavigationParameter)
PX.SM.Users.GINavigationConditionCollection -> Collection(PX.Data.Maintenance.GI.GINavigationCondition)
PX.SM.Users.GIRecordDefaultCollection -> Collection(PX.Data.Maintenance.GI.GIRecordDefault)
PX.SM.Users.GIRelationCollection -> Collection(PX.Data.Maintenance.GI.GIRelation)
PX.SM.Users.GIOnCollection -> Collection(PX.Data.Maintenance.GI.GIOn)
PX.SM.Users.GIResultCollection -> Collection(PX.Data.Maintenance.GI.GIResult)
PX.SM.Users.GISortCollection -> Collection(PX.Data.Maintenance.GI.GISort)
PX.SM.Users.GITableCollection -> Collection(PX.Data.Maintenance.GI.GITable)
PX.SM.Users.GIWhereCollection -> Collection(PX.Data.Maintenance.GI.GIWhere)
PX.SM.Users.NotificationCollection -> Collection(PX.SM.Notification)
PX.SM.Users.EMailAccountCollection -> Collection(PX.SM.EMailAccount)
PX.SM.Users.ActionExecutionCollection -> Collection(PX.BusinessProcess.DAC.ActionExecution)
PX.SM.Users.ActionExecutionMappingCollection -> Collection(PX.BusinessProcess.DAC.ActionExecutionMapping)
PX.SM.Users.ActionExecutionParameterCollection -> Collection(PX.BusinessProcess.DAC.ActionExecutionParameter)
PX.SM.Users.VPComplianceNotificationEventCollection -> Collection(PX.Objects.Portals.Vendor.Configuration.VPComplianceNotificationEvent)
PX.SM.Users.VPSecurityNotificationEventCollection -> Collection(PX.Objects.Portals.Vendor.Configuration.VPSecurityNotificationEvent)
PX.SM.Users.CCPayLinkCollection -> Collection(PX.Objects.CC.CCPayLink)
PX.SM.Users.CustProjectCollection -> Collection(PX.SM.CustProject)
PX.SM.Users.EPCompanyTreeCollection -> Collection(PX.TM.EPCompanyTree)
PX.SM.Users.EPCompanyTreeMemberCollection -> Collection(PX.TM.EPCompanyTreeMember)
PX.SM.Users.EPLoginTypeCollection -> Collection(PX.EP.EPLoginType)
PX.SM.Users.EPLoginTypeAllowsRoleCollection -> Collection(PX.EP.EPLoginTypeAllowsRole)
PX.SM.Users.EPManagedLoginTypeCollection -> Collection(PX.EP.EPManagedLoginType)
PX.SM.Users.RMColumnCollection -> Collection(PX.CS.RMColumn)
PX.SM.Users.RMColumnHeaderCollection -> Collection(PX.CS.RMColumnHeader)
PX.SM.Users.RMColumnSetCollection -> Collection(PX.CS.RMColumnSet)
PX.SM.Users.RMRowCollection -> Collection(PX.CS.RMRow)
PX.SM.Users.RMRowSetCollection -> Collection(PX.CS.RMRowSet)
PX.SM.Users.RMUnitCollection -> Collection(PX.CS.RMUnit)
PX.SM.Users.RMUnitSetCollection -> Collection(PX.CS.RMUnitSet)
PX.SM.Users.SYDataCollection -> Collection(PX.Api.SYData)
PX.SM.Users.SYHistoryCollection -> Collection(PX.Api.SYHistory)
PX.SM.Users.SYImportConditionCollection -> Collection(PX.Api.SYImportCondition)
PX.SM.Users.SYMappingConditionCollection -> Collection(PX.Api.SYMappingCondition)
PX.SM.Users.SYProviderCollection -> Collection(PX.Api.SYProvider)
PX.SM.Users.SYProviderFieldCollection -> Collection(PX.Api.SYProviderField)
PX.SM.Users.SYProviderObjectCollection -> Collection(PX.Api.SYProviderObject)
PX.SM.Users.AUTemplateCollection -> Collection(PX.SM.AUTemplate)
PX.SM.Users.EMailSyncPolicyCollection -> Collection(PX.SM.EMailSyncPolicy)
PX.SM.Users.SMCalendarSettingsCollection -> Collection(PX.SM.SMCalendarSettings)
PX.SM.Users.PreferencesGeneralCollection -> Collection(PX.SM.PreferencesGeneral)
PX.SM.Users.PreferencesEmailCollection -> Collection(PX.SM.PreferencesEmail)
PX.SM.Users.PreferencesSecurityCollection -> Collection(PX.SM.PreferencesSecurity)
PX.SM.Users.SMPrinterCollection -> Collection(PX.SM.SMPrinter)
PX.SM.Users.SMPrintJobCollection -> Collection(PX.SM.SMPrintJob)
PX.SM.Users.SMScaleCollection -> Collection(PX.SM.SMScale)
PX.SM.Users.SMScanJobCollection -> Collection(PX.SM.SMScanJob)
PX.SM.Users.SMScannerCollection -> Collection(PX.SM.SMScanner)
PX.SM.Users.TaskTemplateCollection -> Collection(PX.SM.TaskTemplate)
PX.SM.Users.TaskTemplateSettingCollection -> Collection(PX.SM.TaskTemplateSetting)
PX.SM.Users.UsersInRolesCollection -> Collection(PX.SM.UsersInRoles)
PX.SM.Users.AUAuditSetupCollection -> Collection(PX.SM.AUAuditSetup)
PX.SM.Users.AUActionCollection -> Collection(PX.SM.AUAction)
PX.SM.Users.AUComboCollection -> Collection(PX.SM.AUCombo)
PX.SM.Users.AUDefinitionCollection -> Collection(PX.SM.AUDefinition)
PX.SM.Users.AUDefinitionDetailCollection -> Collection(PX.SM.AUDefinitionDetail)
PX.SM.Users.AUNotificationCollection -> Collection(PX.SM.AUNotification)
PX.SM.Users.AUNotificationFieldCollection -> Collection(PX.SM.AUNotificationField)
PX.SM.Users.AUNotificationFilterCollection -> Collection(PX.SM.AUNotificationFilter)
PX.SM.Users.AUNotificationParameterCollection -> Collection(PX.SM.AUNotificationParameter)
PX.SM.Users.AUScheduleFillCollection -> Collection(PX.SM.AUScheduleFill)
PX.SM.Users.AUScheduleFilterCollection -> Collection(PX.SM.AUScheduleFilter)
PX.SM.Users.AUScheduleTemplateCollection -> Collection(PX.SM.AUScheduleTemplate)
PX.SM.Users.AUStepCollection -> Collection(PX.SM.AUStep)
PX.SM.Users.AUStepActionCollection -> Collection(PX.SM.AUStepAction)
PX.SM.Users.AUStepComboCollection -> Collection(PX.SM.AUStepCombo)
PX.SM.Users.AUStepFieldCollection -> Collection(PX.SM.AUStepField)
PX.SM.Users.AUStepFillCollection -> Collection(PX.SM.AUStepFill)
PX.SM.Users.AUStepFilterCollection -> Collection(PX.SM.AUStepFilter)
PX.SM.Users.AUScreenDefinitionCollection -> Collection(PX.SM.AUScreenDefinition)
PX.SM.Users.AUTableDefinitionCollection -> Collection(PX.SM.AUTableDefinition)
PX.SM.Users.AUTableExtensionCollection -> Collection(PX.SM.AUTableExtension)
PX.SM.Users.UPSnapshotHistoryCollection -> Collection(PX.SM.UPSnapshotHistory)
PX.SM.Users.SpaceUsageCalculationHistoryCollection -> Collection(PX.SM.SpaceUsageCalculationHistory)
PX.SM.Users.KBFeedbackCollection -> Collection(PX.SM.KBFeedback)
PX.SM.Users.KBResponseCollection -> Collection(PX.SM.KBResponse)
PX.SM.Users.KBResponseSummaryCollection -> Collection(PX.SM.KBResponseSummary)
PX.SM.Users.KBResponseMarkCollection -> Collection(PX.SM.KBResponseMark)
PX.SM.Users.SMEmailCollection -> Collection(PX.Objects.CR.SMEmail)
PX.SM.Users.ListEntryPointCollection -> Collection(PX.Data.ListEntryPoint)
PX.SM.Users.RoleInTagCollection -> Collection(PX.Data.Wiki.Tags.RoleInTag)
PX.SM.Users.SPWikiCategoryCollection -> Collection(PX.Data.Search.SPWikiCategory)
PX.SM.Users.SPWikiCategoryTagsCollection -> Collection(PX.Data.Search.SPWikiCategoryTags)
PX.SM.Users.SPWikiProductCollection -> Collection(PX.Data.Search.SPWikiProduct)
PX.SM.Users.SPWikiProductTagsCollection -> Collection(PX.Data.Search.SPWikiProductTags)
PX.SM.Users.GIDataWarehouseCollection -> Collection(PX.Data.GenericInquiry.DAC.GIDataWarehouse)
PX.SM.Users.ODataPreferencesCollection -> Collection(PX.Data.DeletedRecordsTracking.DAC.ODataPreferences)
PX.SM.Users.ArchivedDocumentBatchByDateCollection -> Collection(PX.Data.Archiving.DAC.ArchivedDocumentBatchByDate)
PX.SM.Users.MobileSiteMapWorkspacesCollection -> Collection(PX.Api.Mobile.Workspaces.MobileSiteMapWorkspaces)
PX.SM.Users.SegmentValueCollection -> Collection(PX.Objects.CS.SegmentValue)
PX.SM.Users.TaxAdjustmentCollection -> Collection(PX.Objects.TX.TaxAdjustment)
PX.SM.Users.TaxBucketCollection -> Collection(PX.Objects.TX.TaxBucket)
PX.SM.Users.TaxBucketLineCollection -> Collection(PX.Objects.TX.TaxBucketLine)
PX.SM.Users.TaxCategoryCollection -> Collection(PX.Objects.TX.TaxCategory)
PX.SM.Users.TaxCategoryDetCollection -> Collection(PX.Objects.TX.TaxCategoryDet)
PX.SM.Users.TaxPluginCollection -> Collection(PX.Objects.TX.TaxPlugin)
PX.SM.Users.TaxPluginDetailCollection -> Collection(PX.Objects.TX.TaxPluginDetail)
PX.SM.Users.TaxPluginMappingCollection -> Collection(PX.Objects.TX.TaxPluginMapping)
PX.SM.Users.TaxReportCollection -> Collection(PX.Objects.TX.TaxReport)
PX.SM.Users.TaxReportLineCollection -> Collection(PX.Objects.TX.TaxReportLine)
PX.SM.Users.TaxRevCollection -> Collection(PX.Objects.TX.TaxRev)
PX.SM.Users.TaxZoneCollection -> Collection(PX.Objects.TX.TaxZone)
PX.SM.Users.TaxZoneAddressMappingCollection -> Collection(PX.Objects.TX.TaxZoneAddressMapping)
PX.SM.Users.TaxZoneDetCollection -> Collection(PX.Objects.TX.TaxZoneDet)
PX.SM.Users.TXImportStateCollection -> Collection(PX.Objects.TX.TXImportState)
PX.SM.Users.TXSetupCollection -> Collection(PX.Objects.TX.TXSetup)
PX.SM.Users.SOFreightDetailCollection -> Collection(PX.Objects.SO.SOFreightDetail)
PX.SM.Users.SOLineSplitCollection -> Collection(PX.Objects.SO.SOLineSplit)
PX.SM.Users.SOOrchestrationPlanCollection -> Collection(PX.Objects.SO.SOOrchestrationPlan)
PX.SM.Users.SOOrchestrationPlanLineCollection -> Collection(PX.Objects.SO.SOOrchestrationPlanLine)
PX.SM.Users.SOOrderDiscountDetailCollection -> Collection(PX.Objects.SO.SOOrderDiscountDetail)
PX.SM.Users.SOOrderShipmentCollection -> Collection(PX.Objects.SO.SOOrderShipment)
PX.SM.Users.SOOrderSiteCollection -> Collection(PX.Objects.SO.SOOrderSite)
PX.SM.Users.SOOrderTypeOperationCollection -> Collection(PX.Objects.SO.SOOrderTypeOperation)
PX.SM.Users.SOPickerCollection -> Collection(PX.Objects.SO.SOPicker)
PX.SM.Users.SOPickerListEntryCollection -> Collection(PX.Objects.SO.SOPickerListEntry)
PX.SM.Users.SOPickerToShipmentLinkCollection -> Collection(PX.Objects.SO.SOPickerToShipmentLink)
PX.SM.Users.SOPickingWorksheetCollection -> Collection(PX.Objects.SO.SOPickingWorksheet)
PX.SM.Users.SOPickingWorksheetLineCollection -> Collection(PX.Objects.SO.SOPickingWorksheetLine)
PX.SM.Users.SOPickingWorksheetLineSplitCollection -> Collection(PX.Objects.SO.SOPickingWorksheetLineSplit)
PX.SM.Users.SOPickingWorksheetShipmentCollection -> Collection(PX.Objects.SO.SOPickingWorksheetShipment)
PX.SM.Users.SOPickListEntryToCartSplitLinkCollection -> Collection(PX.Objects.SO.SOPickListEntryToCartSplitLink)
PX.SM.Users.SOPickPackShipSetupCollection -> Collection(PX.Objects.SO.SOPickPackShipSetup)
PX.SM.Users.SOSalesPerTranCollection -> Collection(PX.Objects.SO.SOSalesPerTran)
PX.SM.Users.SOSetupCollection -> Collection(PX.Objects.SO.SOSetup)
PX.SM.Users.SOSetupApprovalCollection -> Collection(PX.Objects.SO.SOSetupApproval)
PX.SM.Users.SOSetupCrossSellExcludedItemClassesCollection -> Collection(PX.Objects.SO.SOSetupCrossSellExcludedItemClasses)
PX.SM.Users.SOSetupCrossSellExcludedOrderTypeCollection -> Collection(PX.Objects.SO.SOSetupCrossSellExcludedOrderType)
PX.SM.Users.SOSetupInvoiceApprovalCollection -> Collection(PX.Objects.SO.SOSetupInvoiceApproval)
PX.SM.Users.SOShipLineCollection -> Collection(PX.Objects.SO.SOShipLine)
PX.SM.Users.SOShipLineSplitCollection -> Collection(PX.Objects.SO.SOShipLineSplit)
PX.SM.Users.SOShipLineSplitPackageCollection -> Collection(PX.Objects.SO.SOShipLineSplitPackage)
PX.SM.Users.SOShipmentCollection -> Collection(PX.Objects.SO.SOShipment)
PX.SM.Users.SOShipmentDiscountDetailCollection -> Collection(PX.Objects.SO.SOShipmentDiscountDetail)
PX.SM.Users.SOShipmentSplitToCartSplitLinkCollection -> Collection(PX.Objects.SO.SOShipmentSplitToCartSplitLink)
PX.SM.Users.RQBiddingCollection -> Collection(PX.Objects.RQ.RQBidding)
PX.SM.Users.RQBiddingVendorCollection -> Collection(PX.Objects.RQ.RQBiddingVendor)
PX.SM.Users.RQRequestCollection -> Collection(PX.Objects.RQ.RQRequest)
PX.SM.Users.RQRequestClassCollection -> Collection(PX.Objects.RQ.RQRequestClass)
PX.SM.Users.RQRequestClassItemCollection -> Collection(PX.Objects.RQ.RQRequestClassItem)
PX.SM.Users.RQRequisitionContentCollection -> Collection(PX.Objects.RQ.RQRequisitionContent)
PX.SM.Users.RQSetupCollection -> Collection(PX.Objects.RQ.RQSetup)
PX.SM.Users.RQSetupApprovalCollection -> Collection(PX.Objects.RQ.RQSetupApproval)
PX.SM.Users.RQBudgetLedgerCollection -> Collection(PX.Objects.RQ.DAC.RQBudgetLedger)
PX.SM.Users.PRDeductCodeCollection -> Collection(PX.Objects.PR.PRDeductCode)
PX.SM.Users.PREmployeeClassCollection -> Collection(PX.Objects.PR.PREmployeeClass)
PX.SM.Users.PRSetupCollection -> Collection(PX.Objects.PR.PRSetup)
PX.SM.Users.PRTaxCodeCollection -> Collection(PX.Objects.PR.PRTaxCode)
PX.SM.Users.LandedCostCodeCollection -> Collection(PX.Objects.PO.LandedCostCode)
PX.SM.Users.POAccrualDetailCollection -> Collection(PX.Objects.PO.POAccrualDetail)
PX.SM.Users.POAccrualSplitCollection -> Collection(PX.Objects.PO.POAccrualSplit)
PX.SM.Users.POAccrualStatusCollection -> Collection(PX.Objects.PO.POAccrualStatus)
PX.SM.Users.POAdjustCollection -> Collection(PX.Objects.PO.POAdjust)
PX.SM.Users.POLandedCostDetailCollection -> Collection(PX.Objects.PO.POLandedCostDetail)
PX.SM.Users.POLandedCostDocCollection -> Collection(PX.Objects.PO.POLandedCostDoc)
PX.SM.Users.POLandedCostReceiptLineCollection -> Collection(PX.Objects.PO.POLandedCostReceiptLine)
PX.SM.Users.POLineBillingRevisionCollection -> Collection(PX.Objects.PO.POLineBillingRevision)
PX.SM.Users.POOrderDiscountDetailCollection -> Collection(PX.Objects.PO.POOrderDiscountDetail)
PX.SM.Users.POOrderPrepaymentCollection -> Collection(PX.Objects.PO.POOrderPrepayment)
PX.SM.Users.POReceiptCollection -> Collection(PX.Objects.PO.POReceipt)
PX.SM.Users.POReceiptItemLotSerialAttributesHeaderCollection -> Collection(PX.Objects.PO.POReceiptItemLotSerialAttributesHeader)
PX.SM.Users.POReceiptLineSplitCollection -> Collection(PX.Objects.PO.POReceiptLineSplit)
PX.SM.Users.POReceiptToShipmentLinkCollection -> Collection(PX.Objects.PO.POReceiptToShipmentLink)
PX.SM.Users.POReceivePutAwaySetupCollection -> Collection(PX.Objects.PO.POReceivePutAwaySetup)
PX.SM.Users.POSetupCollection -> Collection(PX.Objects.PO.POSetup)
PX.SM.Users.POSetupApprovalCollection -> Collection(PX.Objects.PO.POSetupApproval)
PX.SM.Users.POLandedCostDocSCollection -> Collection(PX.Objects.PO.POLandedCostDocS)
PX.SM.Users.PMAccountTaskCollection -> Collection(PX.Objects.PM.PMAccountTask)
PX.SM.Users.PMAllocationCollection -> Collection(PX.Objects.PM.PMAllocation)
PX.SM.Users.PMAllocationDetailCollection -> Collection(PX.Objects.PM.PMAllocationDetail)
PX.SM.Users.PMAllocationSourceTranCollection -> Collection(PX.Objects.PM.PMAllocationSourceTran)
PX.SM.Users.PMBillingCollection -> Collection(PX.Objects.PM.PMBilling)
PX.SM.Users.PMBillingRuleCollection -> Collection(PX.Objects.PM.PMBillingRule)
PX.SM.Users.PMBudgetProductionCollection -> Collection(PX.Objects.PM.PMBudgetProduction)
PX.SM.Users.PMChangeOrderClassCollection -> Collection(PX.Objects.PM.PMChangeOrderClass)
PX.SM.Users.PMChangeOrderLineCollection -> Collection(PX.Objects.PM.PMChangeOrderLine)
PX.SM.Users.PMChangeRequestCollection -> Collection(PX.Objects.PM.PMChangeRequest)
PX.SM.Users.PMChangeRequestAuditCollection -> Collection(PX.Objects.PM.PMChangeRequestAudit)
PX.SM.Users.PMChangeRequestLineCollection -> Collection(PX.Objects.PM.PMChangeRequestLine)
PX.SM.Users.PMChangeRequestMarkupCollection -> Collection(PX.Objects.PM.PMChangeRequestMarkup)
PX.SM.Users.PMCostCodeCollection -> Collection(PX.Objects.PM.PMCostCode)
PX.SM.Users.PMCostProjectionCollection -> Collection(PX.Objects.PM.PMCostProjection)
PX.SM.Users.PMCostProjectionByDateLineCollection -> Collection(PX.Objects.PM.PMCostProjectionByDateLine)
PX.SM.Users.PMCostProjectionClassCollection -> Collection(PX.Objects.PM.PMCostProjectionClass)
PX.SM.Users.PMCostProjectionLineCollection -> Collection(PX.Objects.PM.PMCostProjectionLine)
PX.SM.Users.PMForecastCollection -> Collection(PX.Objects.PM.PMForecast)
PX.SM.Users.PMLaborCostRateCollection -> Collection(PX.Objects.PM.PMLaborCostRate)
PX.SM.Users.PMMarkupCollection -> Collection(PX.Objects.PM.PMMarkup)
PX.SM.Users.PMProformaCollection -> Collection(PX.Objects.PM.PMProforma)
PX.SM.Users.PMProgressWorksheetCollection -> Collection(PX.Objects.PM.PMProgressWorksheet)
PX.SM.Users.PMProjectBudgetHistoryCollection -> Collection(PX.Objects.PM.PMProjectBudgetHistory)
PX.SM.Users.PMProjectContactCollection -> Collection(PX.Objects.PM.PMProjectContact)
PX.SM.Users.PMProjectCostSpreadLineCollection -> Collection(PX.Objects.PM.PMProjectCostSpreadLine)
PX.SM.Users.PMProjectGroupCollection -> Collection(PX.Objects.PM.PMProjectGroup)
PX.SM.Users.PMQuoteTaskCollection -> Collection(PX.Objects.PM.PMQuoteTask)
PX.SM.Users.PMRateCollection -> Collection(PX.Objects.PM.PMRate)
PX.SM.Users.PMRateDefinitionCollection -> Collection(PX.Objects.PM.PMRateDefinition)
PX.SM.Users.PMRateSequenceCollection -> Collection(PX.Objects.PM.PMRateSequence)
PX.SM.Users.PMRateTableCollection -> Collection(PX.Objects.PM.PMRateTable)
PX.SM.Users.PMRateTypeCollection -> Collection(PX.Objects.PM.PMRateType)
PX.SM.Users.PMRetainageStepCollection -> Collection(PX.Objects.PM.PMRetainageStep)
PX.SM.Users.PMRevenuePercentageCalculationRuleCollection -> Collection(PX.Objects.PM.PMRevenuePercentageCalculationRule)
PX.SM.Users.PMTransferRuleCollection -> Collection(PX.Objects.PM.PMTransferRule)
PX.SM.Users.PMUnionCollection -> Collection(PX.Objects.PM.PMUnion)
PX.SM.Users.PMWipAdjustmentCollection -> Collection(PX.Objects.PM.PMWipAdjustment)
PX.SM.Users.PMWipAdjustmentLineCollection -> Collection(PX.Objects.PM.PMWipAdjustmentLine)
PX.SM.Users.PMWorkCodeCollection -> Collection(PX.Objects.PM.PMWorkCode)
PX.SM.Users.PMWorkCodeCostCodeRangeCollection -> Collection(PX.Objects.PM.PMWorkCodeCostCodeRange)
PX.SM.Users.PMWorkCodeLaborItemSourceCollection -> Collection(PX.Objects.PM.PMWorkCodeLaborItemSource)
PX.SM.Users.PMWorkCodeProjectTaskSourceCollection -> Collection(PX.Objects.PM.PMWorkCodeProjectTaskSource)
PX.SM.Users.PMTagTemplateCollection -> Collection(PX.Objects.PM.DAC.PMTagTemplate)
PX.SM.Users.MNMaterialListCollection -> Collection(PX.Objects.MN.MNMaterialList)
PX.SM.Users.MNMaterialListLineCollection -> Collection(PX.Objects.MN.MNMaterialListLine)
PX.SM.Users.MNMaterialListLineSplitCollection -> Collection(PX.Objects.MN.MNMaterialListLineSplit)
PX.SM.Users.MNMaterialListShipmentCollection -> Collection(PX.Objects.MN.MNMaterialListShipment)
PX.SM.Users.SMPersonalDataLogCollection -> Collection(PX.Objects.GDPR.SMPersonalDataLog)
PX.SM.Users.FAAccrualTranCollection -> Collection(PX.Objects.FA.FAAccrualTran)
PX.SM.Users.FAApplicableMethodCollection -> Collection(PX.Objects.FA.FAApplicableMethod)
PX.SM.Users.FABonusCollection -> Collection(PX.Objects.FA.FABonus)
PX.SM.Users.FABonusDetailsCollection -> Collection(PX.Objects.FA.FABonusDetails)
PX.SM.Users.FABookBalanceCollection -> Collection(PX.Objects.FA.FABookBalance)
PX.SM.Users.FABookPeriodSetupCollection -> Collection(PX.Objects.FA.FABookPeriodSetup)
PX.SM.Users.FABookSettingsCollection -> Collection(PX.Objects.FA.FABookSettings)
PX.SM.Users.FABookYearSetupCollection -> Collection(PX.Objects.FA.FABookYearSetup)
PX.SM.Users.FADepreciationMethodCollection -> Collection(PX.Objects.FA.FADepreciationMethod)
PX.SM.Users.FADepreciationMethodLinesCollection -> Collection(PX.Objects.FA.FADepreciationMethodLines)
PX.SM.Users.FADisposalMethodCollection -> Collection(PX.Objects.FA.FADisposalMethod)
PX.SM.Users.FALocationHistoryCollection -> Collection(PX.Objects.FA.FALocationHistory)
PX.SM.Users.FARegisterCollection -> Collection(PX.Objects.FA.FARegister)
PX.SM.Users.FAServiceCollection -> Collection(PX.Objects.FA.FAService)
PX.SM.Users.FAServiceScheduleCollection -> Collection(PX.Objects.FA.FAServiceSchedule)
PX.SM.Users.FASetupCollection -> Collection(PX.Objects.FA.FASetup)
PX.SM.Users.FAUsageCollection -> Collection(PX.Objects.FA.FAUsage)
PX.SM.Users.FAUsageScheduleCollection -> Collection(PX.Objects.FA.FAUsageSchedule)
PX.SM.Users.DRScheduleTranCollection -> Collection(PX.Objects.DR.DRScheduleTran)
PX.SM.Users.ContractBillingScheduleCollection -> Collection(PX.Objects.CT.ContractBillingSchedule)
PX.SM.Users.ContractBillingTraceCollection -> Collection(PX.Objects.CT.ContractBillingTrace)
PX.SM.Users.ContractItemCollection -> Collection(PX.Objects.CT.ContractItem)
PX.SM.Users.ContractRenewalHistoryCollection -> Collection(PX.Objects.CT.ContractRenewalHistory)
PX.SM.Users.ContractSLAMappingCollection -> Collection(PX.Objects.CT.ContractSLAMapping)
PX.SM.Users.AddressValidatorPluginCollection -> Collection(PX.Objects.CS.AddressValidatorPlugin)
PX.SM.Users.AddressValidatorPluginDetailCollection -> Collection(PX.Objects.CS.AddressValidatorPluginDetail)
PX.SM.Users.CarrierCollection -> Collection(PX.Objects.CS.Carrier)
PX.SM.Users.CarrierPackageCollection -> Collection(PX.Objects.CS.CarrierPackage)
PX.SM.Users.CarrierPluginCollection -> Collection(PX.Objects.CS.CarrierPlugin)
PX.SM.Users.CarrierPluginCustomerCollection -> Collection(PX.Objects.CS.CarrierPluginCustomer)
PX.SM.Users.CarrierPluginDetailCollection -> Collection(PX.Objects.CS.CarrierPluginDetail)
PX.SM.Users.CommonSetupCollection -> Collection(PX.Objects.CS.CommonSetup)
PX.SM.Users.CountryCollection -> Collection(PX.Objects.CS.Country)
PX.SM.Users.CSAttributeCollection -> Collection(PX.Objects.CS.CSAttribute)
PX.SM.Users.CSAttributeDetailCollection -> Collection(PX.Objects.CS.CSAttributeDetail)
PX.SM.Users.CSBoxCollection -> Collection(PX.Objects.CS.CSBox)
PX.SM.Users.DimensionCollection -> Collection(PX.Objects.CS.Dimension)
PX.SM.Users.FOBPointCollection -> Collection(PX.Objects.CS.FOBPoint)
PX.SM.Users.FreightRateCollection -> Collection(PX.Objects.CS.FreightRate)
PX.SM.Users.NotificationSetupRecipientCollection -> Collection(PX.Objects.CS.NotificationSetupRecipient)
PX.SM.Users.NotificationSetupUserOverrideCollection -> Collection(PX.Objects.CS.NotificationSetupUserOverride)
PX.SM.Users.NotificationSourceCollection -> Collection(PX.Objects.CS.NotificationSource)
PX.SM.Users.NumberingCollection -> Collection(PX.Objects.CS.Numbering)
PX.SM.Users.NumberingSequenceCollection -> Collection(PX.Objects.CS.NumberingSequence)
PX.SM.Users.ReasonCodeCollection -> Collection(PX.Objects.CS.ReasonCode)
PX.SM.Users.SalesTerritoryCollection -> Collection(PX.Objects.CS.SalesTerritory)
PX.SM.Users.SegmentCollection -> Collection(PX.Objects.CS.Segment)
PX.SM.Users.ShippingZoneCollection -> Collection(PX.Objects.CS.ShippingZone)
PX.SM.Users.ShippingZoneLineCollection -> Collection(PX.Objects.CS.ShippingZoneLine)
PX.SM.Users.ShipTermsCollection -> Collection(PX.Objects.CS.ShipTerms)
PX.SM.Users.ShipTermsDetailCollection -> Collection(PX.Objects.CS.ShipTermsDetail)
PX.SM.Users.StateCollection -> Collection(PX.Objects.CS.State)
PX.SM.Users.TermsCollection -> Collection(PX.Objects.CS.Terms)
PX.SM.Users.TermsInstallmentsCollection -> Collection(PX.Objects.CS.TermsInstallments)
PX.SM.Users.INCartCollection -> Collection(PX.Objects.IN.INCart)
PX.SM.Users.INCartSplitCollection -> Collection(PX.Objects.IN.INCartSplit)
PX.SM.Users.INToteCollection -> Collection(PX.Objects.IN.INTote)
PX.SM.Users.GS1UOMSetupCollection -> Collection(PX.Objects.IN.GS1UOMSetup)
PX.SM.Users.INABCCodeCollection -> Collection(PX.Objects.IN.INABCCode)
PX.SM.Users.INAvailabilitySchemeCollection -> Collection(PX.Objects.IN.INAvailabilityScheme)
PX.SM.Users.INComponentCollection -> Collection(PX.Objects.IN.INComponent)
PX.SM.Users.INCostCenterCollection -> Collection(PX.Objects.IN.INCostCenter)
PX.SM.Users.INItemCategoryCollection -> Collection(PX.Objects.IN.INItemCategory)
PX.SM.Users.INItemClassCurySettingsCollection -> Collection(PX.Objects.IN.INItemClassCurySettings)
PX.SM.Users.INItemClassRepCollection -> Collection(PX.Objects.IN.INItemClassRep)
PX.SM.Users.INItemLotSerialAttributeCollection -> Collection(PX.Objects.IN.INItemLotSerialAttribute)
PX.SM.Users.INItemRepCollection -> Collection(PX.Objects.IN.INItemRep)
PX.SM.Users.INItemSiteReplenishmentCollection -> Collection(PX.Objects.IN.INItemSiteReplenishment)
PX.SM.Users.INKitSerialPartCollection -> Collection(PX.Objects.IN.INKitSerialPart)
PX.SM.Users.INKitSpecHdrCollection -> Collection(PX.Objects.IN.INKitSpecHdr)
PX.SM.Users.INKitSpecNonStkDetCollection -> Collection(PX.Objects.IN.INKitSpecNonStkDet)
PX.SM.Users.INKitSpecStkDetCollection -> Collection(PX.Objects.IN.INKitSpecStkDet)
PX.SM.Users.INLocationCollection -> Collection(PX.Objects.IN.INLocation)
PX.SM.Users.INLotSerClassCollection -> Collection(PX.Objects.IN.INLotSerClass)
PX.SM.Users.INLotSerClassAttributeCollection -> Collection(PX.Objects.IN.INLotSerClassAttribute)
PX.SM.Users.INLotSerClassLotSerNumValCollection -> Collection(PX.Objects.IN.INLotSerClassLotSerNumVal)
PX.SM.Users.INLotSerSegmentCollection -> Collection(PX.Objects.IN.INLotSerSegment)
PX.SM.Users.INMovementClassCollection -> Collection(PX.Objects.IN.INMovementClass)
PX.SM.Users.INPIClassCollection -> Collection(PX.Objects.IN.INPIClass)
PX.SM.Users.INPIClassItemCollection -> Collection(PX.Objects.IN.INPIClassItem)
PX.SM.Users.INPIClassItemClassCollection -> Collection(PX.Objects.IN.INPIClassItemClass)
PX.SM.Users.INPIClassLocationCollection -> Collection(PX.Objects.IN.INPIClassLocation)
PX.SM.Users.INPICycleCollection -> Collection(PX.Objects.IN.INPICycle)
PX.SM.Users.INPIDetailCollection -> Collection(PX.Objects.IN.INPIDetail)
PX.SM.Users.INPIHeaderCollection -> Collection(PX.Objects.IN.INPIHeader)
PX.SM.Users.INPIStatusItemCollection -> Collection(PX.Objects.IN.INPIStatusItem)
PX.SM.Users.INPIStatusLocCollection -> Collection(PX.Objects.IN.INPIStatusLoc)
PX.SM.Users.INPostClassCollection -> Collection(PX.Objects.IN.INPostClass)
PX.SM.Users.INPriceClassCollection -> Collection(PX.Objects.IN.INPriceClass)
PX.SM.Users.INReplenishmentClassCollection -> Collection(PX.Objects.IN.INReplenishmentClass)
PX.SM.Users.INReplenishmentLineCollection -> Collection(PX.Objects.IN.INReplenishmentLine)
PX.SM.Users.INReplenishmentOrderCollection -> Collection(PX.Objects.IN.INReplenishmentOrder)
PX.SM.Users.INReplenishmentPolicyCollection -> Collection(PX.Objects.IN.INReplenishmentPolicy)
PX.SM.Users.INReplenishmentSeasonCollection -> Collection(PX.Objects.IN.INReplenishmentSeason)
PX.SM.Users.INScanSetupCollection -> Collection(PX.Objects.IN.INScanSetup)
PX.SM.Users.INScanUserSetupCollection -> Collection(PX.Objects.IN.INScanUserSetup)
PX.SM.Users.INSetupCollection -> Collection(PX.Objects.IN.INSetup)
PX.SM.Users.INSiteBuildingCollection -> Collection(PX.Objects.IN.INSiteBuilding)
PX.SM.Users.INSubItemRepCollection -> Collection(PX.Objects.IN.INSubItemRep)
PX.SM.Users.INTranCostCollection -> Collection(PX.Objects.IN.INTranCost)
PX.SM.Users.INTransitLineCollection -> Collection(PX.Objects.IN.INTransitLine)
PX.SM.Users.InventoryItemCurySettingsCollection -> Collection(PX.Objects.IN.InventoryItemCurySettings)
PX.SM.Users.InventoryItemLotSerNumValCollection -> Collection(PX.Objects.IN.InventoryItemLotSerNumVal)
PX.SM.Users.UnitOfMeasureCollection -> Collection(PX.Objects.IN.UnitOfMeasure)
PX.SM.Users.WMSJobCollection -> Collection(PX.Objects.IN.WMSJob)
PX.SM.Users.INTurnoverCalcCollection -> Collection(PX.Objects.IN.Turnover.INTurnoverCalc)
PX.SM.Users.INTurnoverCalcItemCollection -> Collection(PX.Objects.IN.Turnover.INTurnoverCalcItem)
PX.SM.Users.RelatedItemHistoryCollection -> Collection(PX.Objects.IN.RelatedItems.RelatedItemHistory)
PX.SM.Users.INRelatedInventoryUserFeedbackCollection -> Collection(PX.Objects.IN.RelatedItems.DAC.INRelatedInventoryUserFeedback)
PX.SM.Users.INAttributeDescriptionGroupCollection -> Collection(PX.Objects.IN.Matrix.DAC.INAttributeDescriptionGroup)
PX.SM.Users.INAttributeDescriptionItemCollection -> Collection(PX.Objects.IN.Matrix.DAC.INAttributeDescriptionItem)
PX.SM.Users.INRegisterCartCollection -> Collection(PX.Objects.IN.DAC.INRegisterCart)
PX.SM.Users.INRegisterCartLineCollection -> Collection(PX.Objects.IN.DAC.INRegisterCartLine)
PX.SM.Users.INConversionHistoryCollection -> Collection(PX.Objects.IN.DAC.INConversionHistory)
PX.SM.Users.INItemClassSiteCollection -> Collection(PX.Objects.IN.DAC.INItemClassSite)
PX.SM.Users.INItemLotSerialAttributesHeaderCurySettingsCollection -> Collection(PX.Objects.IN.DAC.INItemLotSerialAttributesHeaderCurySettings)
PX.SM.Users.INRegisterItemLotSerialAttributesHeaderCollection -> Collection(PX.Objects.IN.DAC.INRegisterItemLotSerialAttributesHeader)
PX.SM.Users.INSetupApprovalCollection -> Collection(PX.Objects.IN.DAC.INSetupApproval)
PX.SM.Users.INSitePlanningStrategyCollection -> Collection(PX.Objects.IN.DAC.INSitePlanningStrategy)
PX.SM.Users.INSitePlanningStrategyDetailCollection -> Collection(PX.Objects.IN.DAC.INSitePlanningStrategyDetail)
PX.SM.Users.INTransferDemandLineCollection -> Collection(PX.Objects.IN.DAC.INTransferDemandLine)
PX.SM.Users.INTransferDemandPutAwaySplitCollection -> Collection(PX.Objects.IN.DAC.INTransferDemandPutAwaySplit)
PX.SM.Users.INTransferListCollection -> Collection(PX.Objects.IN.DAC.INTransferList)
PX.SM.Users.WarehouseReferenceCollection -> Collection(PX.Objects.IN.DAC.WarehouseReference)
PX.SM.Users.VendorDocumentReqComplianceCollection -> Collection(PX.Objects.CN.Requirements.DAC.VendorDocumentReqCompliance)
PX.SM.Users.VendorDocumentReqConditionRowCollection -> Collection(PX.Objects.CN.Requirements.DAC.VendorDocumentReqConditionRow)
PX.SM.Users.VendorDocumentRequirementCollection -> Collection(PX.Objects.CN.Requirements.DAC.VendorDocumentRequirement)
PX.SM.Users.ComplianceRequirementFieldCollection -> Collection(PX.Objects.CN.Requirements.ComplianceRequirementFields.ComplianceRequirementField)
PX.SM.Users.JointPayeePaymentCollection -> Collection(PX.Objects.CN.JointChecks.JointPayeePayment)
PX.SM.Users.ComplianceDocumentCollection -> Collection(PX.Objects.CN.Compliance.CL.DAC.ComplianceDocument)
PX.SM.Users.ComplianceDocumentBillCollection -> Collection(PX.Objects.CN.Compliance.CL.DAC.ComplianceDocumentBill)
PX.SM.Users.CMSetupCollection -> Collection(PX.Objects.CM.CMSetup)
PX.SM.Users.CurrencyListCollection -> Collection(PX.Objects.CM.CurrencyList)
PX.SM.Users.CurrencyRateTypeCollection -> Collection(PX.Objects.CM.CurrencyRateType)
PX.SM.Users.TranslationHistoryCollection -> Collection(PX.Objects.CM.TranslationHistory)
PX.SM.Users.TranslationHistoryDetailsCollection -> Collection(PX.Objects.CM.TranslationHistoryDetails)
PX.SM.Users.TranslDefCollection -> Collection(PX.Objects.CM.TranslDef)
PX.SM.Users.TranslDefDetCollection -> Collection(PX.Objects.CM.TranslDefDet)
PX.SM.Users.CCProcessingCenterTerminalCollection -> Collection(PX.Objects.CC.CCProcessingCenterTerminal)
PX.SM.Users.AccountClassCollection -> Collection(PX.Objects.GL.AccountClass)
PX.SM.Users.FinPeriodSetupCollection -> Collection(PX.Objects.GL.FinPeriodSetup)
PX.SM.Users.FinYearSetupCollection -> Collection(PX.Objects.GL.FinYearSetup)
PX.SM.Users.GLAllocationDestinationCollection -> Collection(PX.Objects.GL.GLAllocationDestination)
PX.SM.Users.GLAllocationSourceCollection -> Collection(PX.Objects.GL.GLAllocationSource)
PX.SM.Users.GLBudgetCollection -> Collection(PX.Objects.GL.GLBudget)
PX.SM.Users.GLBudgetLineDetailCollection -> Collection(PX.Objects.GL.GLBudgetLineDetail)
PX.SM.Users.GLBudgetTreeCollection -> Collection(PX.Objects.GL.GLBudgetTree)
PX.SM.Users.GLDocBatchCollection -> Collection(PX.Objects.GL.GLDocBatch)
PX.SM.Users.GLSetupCollection -> Collection(PX.Objects.GL.GLSetup)
PX.SM.Users.GLSetupApprovalCollection -> Collection(PX.Objects.GL.GLSetupApproval)
PX.SM.Users.GLTrialBalanceImportMapCollection -> Collection(PX.Objects.GL.GLTrialBalanceImportMap)
PX.SM.Users.ScheduleCollection -> Collection(PX.Objects.GL.Schedule)
PX.SM.Users.FinYearCollection -> Collection(PX.Objects.GL.FinPeriods.TableDefinition.FinYear)
PX.SM.Users.CRReminderCollection -> Collection(PX.Objects.CR.CRReminder)
PX.SM.Users.CAAdjCollection -> Collection(PX.Objects.CA.CAAdj)
PX.SM.Users.CABankFeedCollection -> Collection(PX.Objects.CA.CABankFeed)
PX.SM.Users.CABankFeedAccountMappingCollection -> Collection(PX.Objects.CA.CABankFeedAccountMapping)
PX.SM.Users.CABankFeedCorpCardCollection -> Collection(PX.Objects.CA.CABankFeedCorpCard)
PX.SM.Users.CABankFeedDetailCollection -> Collection(PX.Objects.CA.CABankFeedDetail)
PX.SM.Users.CABankFeedExpenseCollection -> Collection(PX.Objects.CA.CABankFeedExpense)
PX.SM.Users.CABankFeedFieldMappingCollection -> Collection(PX.Objects.CA.CABankFeedFieldMapping)
PX.SM.Users.CABankTranAdjustmentCollection -> Collection(PX.Objects.CA.CABankTranAdjustment)
PX.SM.Users.CABankTranBAccountMappingCollection -> Collection(PX.Objects.CA.CABankTranBAccountMapping)
PX.SM.Users.CABankTranDetailCollection -> Collection(PX.Objects.CA.CABankTranDetail)
PX.SM.Users.CABankTranHeaderCollection -> Collection(PX.Objects.CA.CABankTranHeader)
PX.SM.Users.CACorpCardCollection -> Collection(PX.Objects.CA.CACorpCard)
PX.SM.Users.CADepositCollection -> Collection(PX.Objects.CA.CADeposit)
PX.SM.Users.CADepositChargeCollection -> Collection(PX.Objects.CA.CADepositCharge)
PX.SM.Users.CADepositDetailCollection -> Collection(PX.Objects.CA.CADepositDetail)
PX.SM.Users.CAEntryTypeCollection -> Collection(PX.Objects.CA.CAEntryType)
PX.SM.Users.CAExpenseCollection -> Collection(PX.Objects.CA.CAExpense)
PX.SM.Users.CAReconCollection -> Collection(PX.Objects.CA.CARecon)
PX.SM.Users.CASetupCollection -> Collection(PX.Objects.CA.CASetup)
PX.SM.Users.CASetupApprovalCollection -> Collection(PX.Objects.CA.CASetupApproval)
PX.SM.Users.CashAccountCheckCollection -> Collection(PX.Objects.CA.CashAccountCheck)
PX.SM.Users.CashAccountETDetailCollection -> Collection(PX.Objects.CA.CashAccountETDetail)
PX.SM.Users.CashForecastTranCollection -> Collection(PX.Objects.CA.CashForecastTran)
PX.SM.Users.CASplitCollection -> Collection(PX.Objects.CA.CASplit)
PX.SM.Users.CATransferCollection -> Collection(PX.Objects.CA.CATransfer)
PX.SM.Users.CCBatchCollection -> Collection(PX.Objects.CA.CCBatch)
PX.SM.Users.CCBatchStatisticsCollection -> Collection(PX.Objects.CA.CCBatchStatistics)
PX.SM.Users.CCProcessingCenterCollection -> Collection(PX.Objects.CA.CCProcessingCenter)
PX.SM.Users.CCProcessingCenterDetailCollection -> Collection(PX.Objects.CA.CCProcessingCenterDetail)
PX.SM.Users.CCProcessingCenterFeeTypeCollection -> Collection(PX.Objects.CA.CCProcessingCenterFeeType)
PX.SM.Users.CCProcessingCenterPmntMethodBranchCollection -> Collection(PX.Objects.CA.CCProcessingCenterPmntMethodBranch)
PX.SM.Users.PaymentMethodDetailCollection -> Collection(PX.Objects.CA.PaymentMethodDetail)
PX.SM.Users.BuildingCollection -> Collection(PX.Objects.CR.Building)
PX.SM.Users.CRCampaignCollection -> Collection(PX.Objects.CR.CRCampaign)
PX.SM.Users.CRCampaignTypeCollection -> Collection(PX.Objects.CR.CRCampaignType)
PX.SM.Users.CRCaseClassCollection -> Collection(PX.Objects.CR.CRCaseClass)
PX.SM.Users.CRCaseClassLaborMatrixCollection -> Collection(PX.Objects.CR.CRCaseClassLaborMatrix)
PX.SM.Users.CRCaseReferenceCollection -> Collection(PX.Objects.CR.CRCaseReference)
PX.SM.Users.CRClassSeverityTimeCollection -> Collection(PX.Objects.CR.CRClassSeverityTime)
PX.SM.Users.CRMarketingCategoryCollection -> Collection(PX.Objects.CR.CRMarketingCategory)
PX.SM.Users.CRMassMailCollection -> Collection(PX.Objects.CR.CRMassMail)
PX.SM.Users.CRMassMailMarketingListCollection -> Collection(PX.Objects.CR.CRMassMailMarketingList)
PX.SM.Users.CRMassMailMemberCollection -> Collection(PX.Objects.CR.CRMassMailMember)
PX.SM.Users.CRMassMailCampaignCollection -> Collection(PX.Objects.CR.CRMassMailCampaign)
PX.SM.Users.CROpportunityClassProbabilityCollection -> Collection(PX.Objects.CR.CROpportunityClassProbability)
PX.SM.Users.CROpportunityDiscountDetailCollection -> Collection(PX.Objects.CR.CROpportunityDiscountDetail)
PX.SM.Users.CROpportunityProbabilityCollection -> Collection(PX.Objects.CR.CROpportunityProbability)
PX.SM.Users.CRUnsubscribedPreferencesCollection -> Collection(PX.Objects.CR.CRUnsubscribedPreferences)
PX.SM.Users.LocationBranchSettingsCollection -> Collection(PX.Objects.CR.LocationBranchSettings)
PX.SM.Users.CROpportunityRevisionCollection -> Collection(PX.Objects.CR.Standalone.CROpportunityRevision)
PX.SM.Users.ARDunningSetupCollection -> Collection(PX.Objects.AR.ARDunningSetup)
PX.SM.Users.ARFinChargeCollection -> Collection(PX.Objects.AR.ARFinCharge)
PX.SM.Users.ARInvoiceDiscountDetailCollection -> Collection(PX.Objects.AR.ARInvoiceDiscountDetail)
PX.SM.Users.ARPaymentChargeTranCollection -> Collection(PX.Objects.AR.ARPaymentChargeTran)
PX.SM.Users.ARPaymentTotalsCollection -> Collection(PX.Objects.AR.ARPaymentTotals)
PX.SM.Users.ARPriceClassCollection -> Collection(PX.Objects.AR.ARPriceClass)
PX.SM.Users.ARPriceWorksheetCollection -> Collection(PX.Objects.AR.ARPriceWorksheet)
PX.SM.Users.ARPriceWorksheetDetailCollection -> Collection(PX.Objects.AR.ARPriceWorksheetDetail)
PX.SM.Users.ARSetupCollection -> Collection(PX.Objects.AR.ARSetup)
PX.SM.Users.ARSetupApprovalCollection -> Collection(PX.Objects.AR.ARSetupApproval)
PX.SM.Users.ARStatementCollection -> Collection(PX.Objects.AR.ARStatement)
PX.SM.Users.ARStatementCycleCollection -> Collection(PX.Objects.AR.ARStatementCycle)
PX.SM.Users.CCProcTranCollection -> Collection(PX.Objects.AR.CCProcTran)
PX.SM.Users.CustomerClassCollection -> Collection(PX.Objects.AR.CustomerClass)
PX.SM.Users.CustomerPaymentMethodCollection -> Collection(PX.Objects.AR.CustomerPaymentMethod)
PX.SM.Users.CustomerPaymentMethodDetailCollection -> Collection(PX.Objects.AR.CustomerPaymentMethodDetail)
PX.SM.Users.DiscountBranchCollection -> Collection(PX.Objects.AR.DiscountBranch)
PX.SM.Users.DiscountCustomerCollection -> Collection(PX.Objects.AR.DiscountCustomer)
PX.SM.Users.DiscountCustomerPriceClassCollection -> Collection(PX.Objects.AR.DiscountCustomerPriceClass)
PX.SM.Users.DiscountInventoryPriceClassCollection -> Collection(PX.Objects.AR.DiscountInventoryPriceClass)
PX.SM.Users.DiscountItemCollection -> Collection(PX.Objects.AR.DiscountItem)
PX.SM.Users.DiscountSequenceCollection -> Collection(PX.Objects.AR.DiscountSequence)
PX.SM.Users.DiscountSiteCollection -> Collection(PX.Objects.AR.DiscountSite)
PX.SM.Users.SalesPersonCollection -> Collection(PX.Objects.AR.SalesPerson)
PX.SM.Users.DropShipLinkCollection -> Collection(PX.Objects.Common.DAC.DropShipLink)
PX.SM.Users.EPAssignmentMapCollection -> Collection(PX.Objects.EP.EPAssignmentMap)
PX.SM.Users.EPAssignmentRouteCollection -> Collection(PX.Objects.EP.EPAssignmentRoute)
PX.SM.Users.EPAssignmentRuleCollection -> Collection(PX.Objects.EP.EPAssignmentRule)
PX.SM.Users.EPAttendeeCollection -> Collection(PX.Objects.EP.EPAttendee)
PX.SM.Users.EPContractRateCollection -> Collection(PX.Objects.EP.EPContractRate)
PX.SM.Users.EPCustomWeekCollection -> Collection(PX.Objects.EP.EPCustomWeek)
PX.SM.Users.EPDepartmentCollection -> Collection(PX.Objects.EP.EPDepartment)
PX.SM.Users.EPEarningTypeCollection -> Collection(PX.Objects.EP.EPEarningType)
PX.SM.Users.EPEmployeeClassLaborMatrixCollection -> Collection(PX.Objects.EP.EPEmployeeClassLaborMatrix)
PX.SM.Users.EPEmployeeContractCollection -> Collection(PX.Objects.EP.EPEmployeeContract)
PX.SM.Users.EPEmployeePositionCollection -> Collection(PX.Objects.EP.EPEmployeePosition)
PX.SM.Users.EPEquipmentCollection -> Collection(PX.Objects.EP.EPEquipment)
PX.SM.Users.EPEquipmentRateCollection -> Collection(PX.Objects.EP.EPEquipmentRate)
PX.SM.Users.EPEquipmentSummaryCollection -> Collection(PX.Objects.EP.EPEquipmentSummary)
PX.SM.Users.EPEventCategoryCollection -> Collection(PX.Objects.EP.EPEventCategory)
PX.SM.Users.EPPositionCollection -> Collection(PX.Objects.EP.EPPosition)
PX.SM.Users.EPShiftCodeCollection -> Collection(PX.Objects.EP.EPShiftCode)
PX.SM.Users.EPShiftCodeRateCollection -> Collection(PX.Objects.EP.EPShiftCodeRate)
PX.SM.Users.EPTimeActivitiesSummaryCollection -> Collection(PX.Objects.EP.EPTimeActivitiesSummary)
PX.SM.Users.EPWeeklyCrewTimeActivityCollection -> Collection(PX.Objects.EP.EPWeeklyCrewTimeActivity)
PX.SM.Users.EPRuleApproverCollection -> Collection(PX.Objects.EP.DAC.EPRuleApprover)
PX.SM.Users.EPTimeLogCollection -> Collection(PX.Objects.EP.ClockInClockOut.EPTimeLog)
PX.SM.Users.EPTimeLogTypeCollection -> Collection(PX.Objects.EP.ClockInClockOut.EPTimeLogType)
PX.SM.Users.APAddressCollection -> Collection(PX.Objects.AP.APAddress)
PX.SM.Users.APContactCollection -> Collection(PX.Objects.AP.APContact)
PX.SM.Users.APDiscountLocationCollection -> Collection(PX.Objects.AP.APDiscountLocation)
PX.SM.Users.APDiscountVendorCollection -> Collection(PX.Objects.AP.APDiscountVendor)
PX.SM.Users.APInvoiceDiscountDetailCollection -> Collection(PX.Objects.AP.APInvoiceDiscountDetail)
PX.SM.Users.APPaymentChargeTranCollection -> Collection(PX.Objects.AP.APPaymentChargeTran)
PX.SM.Users.APPriceWorksheetCollection -> Collection(PX.Objects.AP.APPriceWorksheet)
PX.SM.Users.APPriceWorksheetDetailCollection -> Collection(PX.Objects.AP.APPriceWorksheetDetail)
PX.SM.Users.APPrintCheckDetailCollection -> Collection(PX.Objects.AP.APPrintCheckDetail)
PX.SM.Users.APSetupCollection -> Collection(PX.Objects.AP.APSetup)
PX.SM.Users.APSetupApprovalCollection -> Collection(PX.Objects.AP.APSetupApproval)
PX.SM.Users.APVendorPriceCollection -> Collection(PX.Objects.AP.APVendorPrice)
PX.SM.Users.ExcludedVendorDomainCollection -> Collection(PX.Objects.AP.InvoiceRecognition.DAC.ExcludedVendorDomain)
PX.SM.Users.RecognizedVendorMappingCollection -> Collection(PX.Objects.AP.InvoiceRecognition.DAC.RecognizedVendorMapping)
PX.SM.Users.LLMConnectionCollection -> Collection(PX.AIStudio.DAC.LLMConnection)
PX.SM.Users.LLMConnectionParameterCollection -> Collection(PX.AIStudio.DAC.LLMConnectionParameter)
PX.SM.Users.LLMPromptCollection -> Collection(PX.AIStudio.DAC.LLMPrompt)
PX.SM.Users.LLMPromptSystemInstructionCollection -> Collection(PX.AIStudio.DAC.LLMPromptSystemInstruction)
PX.SM.Users.LLMPromptToolCollection -> Collection(PX.AIStudio.DAC.LLMPromptTool)
PX.SM.Users.LLMProviderCollection -> Collection(PX.AIStudio.DAC.LLMProvider)
PX.SM.Users.LLMProviderParameterCollection -> Collection(PX.AIStudio.DAC.LLMProviderParameter)
PX.SM.Users.LLMSystemInstructionCollection -> Collection(PX.AIStudio.DAC.LLMSystemInstruction)
PX.SM.Users.MobileSiteMapWorkspaceItemsCollection -> Collection(PX.Api.Mobile.Workspaces.DAC.MobileSiteMapWorkspaceItems)
PX.SM.Users.MobileSiteMapWorkspaceItemsOrderCollection -> Collection(PX.Api.Mobile.Workspaces.DAC.MobileSiteMapWorkspaceItemsOrder)
PX.SM.Users.MobileSiteMapWorkspacesOrderCollection -> Collection(PX.Api.Mobile.Workspaces.DAC.MobileSiteMapWorkspacesOrder)
PX.SM.Users.MobileSiteMapWorkspaceWidgetsOrderCollection -> Collection(PX.Api.Mobile.Workspaces.DAC.MobileSiteMapWorkspaceWidgetsOrder)
PX.SM.Users.MobileSiteMapWorkspaceWidgetsV2Collection -> Collection(PX.Api.Mobile.Workspaces.DAC.MobileSiteMapWorkspaceWidgetsV2)
PX.SM.Users.MobileSiteMapWorkspaceWidgetsV2OrderCollection -> Collection(PX.Api.Mobile.Workspaces.DAC.MobileSiteMapWorkspaceWidgetsV2Order)
PX.SM.Users.MobileNotificationCollection -> Collection(PX.BusinessProcess.DAC.MobileNotification)
PX.SM.Users.QueueNotificationSettingsCollection -> Collection(PX.BusinessProcess.DAC.QueueNotificationSettings)
PX.SM.Users.BCAmazonTaxMappingCollection -> Collection(PX.Commerce.Amazon.BCAmazonTaxMapping)
PX.SM.Users.BCBindingAmazonCollection -> Collection(PX.Commerce.Amazon.BCBindingAmazon)
PX.SM.Users.BCBindingBigCommerceCollection -> Collection(PX.Commerce.BigCommerce.BCBindingBigCommerce)
PX.SM.Users.BCBindingCollection -> Collection(PX.Commerce.Core.BCBinding)
PX.SM.Users.BCEntityExportFilterCollection -> Collection(PX.Commerce.Core.BCEntityExportFilter)
PX.SM.Users.BCEntityExportMappingCollection -> Collection(PX.Commerce.Core.BCEntityExportMapping)
PX.SM.Users.BCEntityImportFilterCollection -> Collection(PX.Commerce.Core.BCEntityImportFilter)
PX.SM.Users.BCEntityImportMappingCollection -> Collection(PX.Commerce.Core.BCEntityImportMapping)
PX.SM.Users.BCWebHookCollection -> Collection(PX.Commerce.Core.BCWebHook)
PX.SM.Users.BCBindingExtCollection -> Collection(PX.Commerce.Objects.BCBindingExt)
PX.SM.Users.BCMatrixOptionsMappingCollection -> Collection(PX.Commerce.Objects.BCMatrixOptionsMapping)
PX.SM.Users.BCBindingShopifyCollection -> Collection(PX.Commerce.Shopify.BCBindingShopify)
PX.SM.Users.DashboardParameterCollection -> Collection(PX.Dashboards.DAC.DashboardParameter)
PX.SM.Users.DashboardParameterV2Collection -> Collection(PX.Dashboards.DAC.DashboardParameterV2)
PX.SM.Users.WidgetCollection -> Collection(PX.Dashboards.DAC.Widget)
PX.SM.Users.WidgetParameterV2Collection -> Collection(PX.Dashboards.DAC.WidgetParameterV2)
PX.SM.Users.WidgetV2Collection -> Collection(PX.Dashboards.DAC.WidgetV2)
PX.SM.Users.HSEntitySetupCollection -> Collection(PX.DataSync.HubSpot.HSEntitySetup)
PX.SM.Users.HSMarketingListMemberCollection -> Collection(PX.DataSync.HubSpot.HSMarketingListMember)
PX.SM.Users.SMSendGridSuppressionGroupCollection -> Collection(PX.DataSync.SendGrid.SMSendGridSuppressionGroup)
PX.SM.Users.ESignAccountCollection -> Collection(PX.ESign.ESignAccount)
PX.SM.Users.ESignAccountUserRuleCollection -> Collection(PX.ESign.ESignAccountUserRule)
PX.SM.Users.ESignEnvelopeInfoCollection -> Collection(PX.ESign.ESignEnvelopeInfo)
PX.SM.Users.ESignRecipientCollection -> Collection(PX.ESign.ESignRecipient)
PX.SM.Users.ShipEngineCarrierServiceCollection -> Collection(PX.ExternalCarriersCommon.ShipEngineCarrierService)
PX.SM.Users.SOShipmentManifestCollection -> Collection(PX.Objects.SO.SOShipmentManifest)
PX.SM.Users.CROpportunityRevisionCarrierDataCollection -> Collection(PX.ExternalCarriersHelper.CROpportunityRevisionCarrierData)
PX.SM.Users.SETerritoriesMappingCollection -> Collection(PX.ExternalCarriersHelper.SETerritoriesMapping)
PX.SM.Users.InventoryItemCarrierDataCollection -> Collection(PX.ExternalCarriersHelper.InventoryItemCarrierData)
PX.SM.Users.SOOrderCarrierDataCollection -> Collection(PX.ExternalCarriersHelper.SOOrderCarrierData)
PX.SM.Users.SOShipmentCarrierDataCollection -> Collection(PX.ExternalCarriersHelper.SOShipmentCarrierData)
PX.SM.Users.GIReportCollection -> Collection(PX.GIReports.Maintenance.DAC.GIReport)
PX.SM.Users.GIReportGroupCollection -> Collection(PX.GIReports.Maintenance.DAC.GIReportGroup)
PX.SM.Users.GIReportGroupColumnCollection -> Collection(PX.GIReports.Maintenance.DAC.GIReportGroupColumn)
PX.SM.Users.GIReportGroupGroupingCollection -> Collection(PX.GIReports.Maintenance.DAC.GIReportGroupGrouping)
PX.SM.Users.GIReportGroupSortingCollection -> Collection(PX.GIReports.Maintenance.DAC.GIReportGroupSorting)
PX.SM.Users.SMGraphPermissionCollection -> Collection(PX.MSGraph.DAC.SM.SMGraphPermission)
PX.SM.Users.SMGraphSetupCollection -> Collection(PX.MSGraph.DAC.SM.SMGraphSetup)
PX.SM.Users.SMTeamsNotificationCollection -> Collection(PX.MSTeams.DAC.SM.SMTeamsNotification)
PX.SM.Users.SMTeamsActivityCollection -> Collection(PX.Objects.CR.SMTeamsActivity)
PX.SM.Users.AMBatchItemLotSerialAttributesHeaderCollection -> Collection(PX.Objects.AM.AMBatchItemLotSerialAttributesHeader)
PX.SM.Users.AMBomAttributeCollection -> Collection(PX.Objects.AM.AMBomAttribute)
PX.SM.Users.AMBomCostHistoryCollection -> Collection(PX.Objects.AM.AMBomCostHistory)
PX.SM.Users.AMBOMCurySettingsCollection -> Collection(PX.Objects.AM.AMBOMCurySettings)
PX.SM.Users.AMBomOperCollection -> Collection(PX.Objects.AM.AMBomOper)
PX.SM.Users.AMBomOvhdCollection -> Collection(PX.Objects.AM.AMBomOvhd)
PX.SM.Users.AMBomRefCollection -> Collection(PX.Objects.AM.AMBomRef)
PX.SM.Users.AMBomStepCollection -> Collection(PX.Objects.AM.AMBomStep)
PX.SM.Users.AMBomToolCollection -> Collection(PX.Objects.AM.AMBomTool)
PX.SM.Users.AMClockItemCollection -> Collection(PX.Objects.AM.AMClockItem)
PX.SM.Users.AMClockTranCollection -> Collection(PX.Objects.AM.AMClockTran)
PX.SM.Users.AMClockTranSplitCollection -> Collection(PX.Objects.AM.AMClockTranSplit)
PX.SM.Users.AMConfigResultsAttributeCollection -> Collection(PX.Objects.AM.AMConfigResultsAttribute)
PX.SM.Users.AMConfigResultsFeatureCollection -> Collection(PX.Objects.AM.AMConfigResultsFeature)
PX.SM.Users.AMConfigResultsOptionCollection -> Collection(PX.Objects.AM.AMConfigResultsOption)
PX.SM.Users.AMConfigResultsRuleCollection -> Collection(PX.Objects.AM.AMConfigResultsRule)
PX.SM.Users.AMConfigurationCollection -> Collection(PX.Objects.AM.AMConfiguration)
PX.SM.Users.AMConfigurationAttributeCollection -> Collection(PX.Objects.AM.AMConfigurationAttribute)
PX.SM.Users.AMConfigurationFeatureCollection -> Collection(PX.Objects.AM.AMConfigurationFeature)
PX.SM.Users.AMConfigurationOptionCollection -> Collection(PX.Objects.AM.AMConfigurationOption)
PX.SM.Users.AMConfigurationOptionCurySettingsCollection -> Collection(PX.Objects.AM.AMConfigurationOptionCurySettings)
PX.SM.Users.AMConfigurationResultsCollection -> Collection(PX.Objects.AM.AMConfigurationResults)
PX.SM.Users.AMConfigurationRuleCollection -> Collection(PX.Objects.AM.AMConfigurationRule)
PX.SM.Users.AMDepartmentCollection -> Collection(PX.Objects.AM.AMDepartment)
PX.SM.Users.AMECOItemCollection -> Collection(PX.Objects.AM.AMECOItem)
PX.SM.Users.AMECOSetupApprovalCollection -> Collection(PX.Objects.AM.AMECOSetupApproval)
PX.SM.Users.AMECRItemCollection -> Collection(PX.Objects.AM.AMECRItem)
PX.SM.Users.AMECRSetupApprovalCollection -> Collection(PX.Objects.AM.AMECRSetupApproval)
PX.SM.Users.AMEstimateClassCollection -> Collection(PX.Objects.AM.AMEstimateClass)
PX.SM.Users.AMEstimateHistoryCollection -> Collection(PX.Objects.AM.AMEstimateHistory)
PX.SM.Users.AMEstimateMatlCollection -> Collection(PX.Objects.AM.AMEstimateMatl)
PX.SM.Users.AMEstimateOperCollection -> Collection(PX.Objects.AM.AMEstimateOper)
PX.SM.Users.AMEstimateOvhdCollection -> Collection(PX.Objects.AM.AMEstimateOvhd)
PX.SM.Users.AMEstimatePriceBreakCollection -> Collection(PX.Objects.AM.AMEstimatePriceBreak)
PX.SM.Users.AMEstimateReferenceCollection -> Collection(PX.Objects.AM.AMEstimateReference)
PX.SM.Users.AMEstimateSetupCollection -> Collection(PX.Objects.AM.AMEstimateSetup)
PX.SM.Users.AMEstimateStepCollection -> Collection(PX.Objects.AM.AMEstimateStep)
PX.SM.Users.AMEstimateToolCollection -> Collection(PX.Objects.AM.AMEstimateTool)
PX.SM.Users.AMFeatureCollection -> Collection(PX.Objects.AM.AMFeature)
PX.SM.Users.AMFeatureAttributeCollection -> Collection(PX.Objects.AM.AMFeatureAttribute)
PX.SM.Users.AMFeatureOptionCollection -> Collection(PX.Objects.AM.AMFeatureOption)
PX.SM.Users.AMForecastCollection -> Collection(PX.Objects.AM.AMForecast)
PX.SM.Users.AMForecastPeriodCollection -> Collection(PX.Objects.AM.AMForecastPeriod)
PX.SM.Users.AMForecastStagingCollection -> Collection(PX.Objects.AM.AMForecastStaging)
PX.SM.Users.AMLaborCodeCollection -> Collection(PX.Objects.AM.AMLaborCode)
PX.SM.Users.AMMachCollection -> Collection(PX.Objects.AM.AMMach)
PX.SM.Users.AMMachCurySettingsCollection -> Collection(PX.Objects.AM.AMMachCurySettings)
PX.SM.Users.AMMachSchdDetailCollection -> Collection(PX.Objects.AM.AMMachSchdDetail)
PX.SM.Users.AMMPSCollection -> Collection(PX.Objects.AM.AMMPS)
PX.SM.Users.AMMPSTypeCollection -> Collection(PX.Objects.AM.AMMPSType)
PX.SM.Users.AMMRPBucketCollection -> Collection(PX.Objects.AM.AMMRPBucket)
PX.SM.Users.AMMRPBucketDetailCollection -> Collection(PX.Objects.AM.AMMRPBucketDetail)
PX.SM.Users.AMMRPBucketDetailInqCollection -> Collection(PX.Objects.AM.AMMRPBucketDetailInq)
PX.SM.Users.AMMRPBucketInqCollection -> Collection(PX.Objects.AM.AMMRPBucketInq)
PX.SM.Users.AMOrderTypeCollection -> Collection(PX.Objects.AM.AMOrderType)
PX.SM.Users.AMOrderTypeAttributeCollection -> Collection(PX.Objects.AM.AMOrderTypeAttribute)
PX.SM.Users.AMOverheadCollection -> Collection(PX.Objects.AM.AMOverhead)
PX.SM.Users.AMOverheadCurySettingsCollection -> Collection(PX.Objects.AM.AMOverheadCurySettings)
PX.SM.Users.AMProdAttributeCollection -> Collection(PX.Objects.AM.AMProdAttribute)
PX.SM.Users.AMProdEvntCollection -> Collection(PX.Objects.AM.AMProdEvnt)
PX.SM.Users.AMProdItemSplitCollection -> Collection(PX.Objects.AM.AMProdItemSplit)
PX.SM.Users.AMProdMatlLotSerialCollection -> Collection(PX.Objects.AM.AMProdMatlLotSerial)
PX.SM.Users.AMProdMatlSplitCollection -> Collection(PX.Objects.AM.AMProdMatlSplit)
PX.SM.Users.AMProdNumberCollection -> Collection(PX.Objects.AM.AMProdNumber)
PX.SM.Users.AMProdOvhdCollection -> Collection(PX.Objects.AM.AMProdOvhd)
PX.SM.Users.AMProdStepCollection -> Collection(PX.Objects.AM.AMProdStep)
PX.SM.Users.AMProdToolCollection -> Collection(PX.Objects.AM.AMProdTool)
PX.SM.Users.AMProdTotalCollection -> Collection(PX.Objects.AM.AMProdTotal)
PX.SM.Users.AMRPAuditHistoryCollection -> Collection(PX.Objects.AM.AMRPAuditHistory)
PX.SM.Users.AMRPAuditTableCollection -> Collection(PX.Objects.AM.AMRPAuditTable)
PX.SM.Users.AMRPDetailCollection -> Collection(PX.Objects.AM.AMRPDetail)
PX.SM.Users.AMRPHistoryCollection -> Collection(PX.Objects.AM.AMRPHistory)
PX.SM.Users.AMRPItemSiteCollection -> Collection(PX.Objects.AM.AMRPItemSite)
PX.SM.Users.AMScanSetupCollection -> Collection(PX.Objects.AM.AMScanSetup)
PX.SM.Users.AMSchdItemCollection -> Collection(PX.Objects.AM.AMSchdItem)
PX.SM.Users.AMSchdOperCollection -> Collection(PX.Objects.AM.AMSchdOper)
PX.SM.Users.AMSchdOperDetailCollection -> Collection(PX.Objects.AM.AMSchdOperDetail)
PX.SM.Users.AMShiftCollection -> Collection(PX.Objects.AM.AMShift)
PX.SM.Users.AMSiteTransferCollection -> Collection(PX.Objects.AM.AMSiteTransfer)
PX.SM.Users.AMSubItemDefaultCollection -> Collection(PX.Objects.AM.AMSubItemDefault)
PX.SM.Users.AMToolMstCollection -> Collection(PX.Objects.AM.AMToolMst)
PX.SM.Users.AMToolMstCurySettingsCollection -> Collection(PX.Objects.AM.AMToolMstCurySettings)
PX.SM.Users.AMToolSchdDetailCollection -> Collection(PX.Objects.AM.AMToolSchdDetail)
PX.SM.Users.AMVendorShipLineCollection -> Collection(PX.Objects.AM.AMVendorShipLine)
PX.SM.Users.AMVendorShipLineSplitCollection -> Collection(PX.Objects.AM.AMVendorShipLineSplit)
PX.SM.Users.AMVendorShipmentCollection -> Collection(PX.Objects.AM.AMVendorShipment)
PX.SM.Users.AMVendorShipmentAddressCollection -> Collection(PX.Objects.AM.AMVendorShipmentAddress)
PX.SM.Users.AMVendorShipmentContactCollection -> Collection(PX.Objects.AM.AMVendorShipmentContact)
PX.SM.Users.AMWCCollection -> Collection(PX.Objects.AM.AMWC)
PX.SM.Users.AMWCCalendarPeriodCollection -> Collection(PX.Objects.AM.AMWCCalendarPeriod)
PX.SM.Users.AMWCCurySettingsCollection -> Collection(PX.Objects.AM.AMWCCurySettings)
PX.SM.Users.AMWCMachCollection -> Collection(PX.Objects.AM.AMWCMach)
PX.SM.Users.AMWCOvhdCollection -> Collection(PX.Objects.AM.AMWCOvhd)
PX.SM.Users.AMWCSubstituteCollection -> Collection(PX.Objects.AM.AMWCSubstitute)
PX.SM.Users.AMWrkMatlCollection -> Collection(PX.Objects.AM.AMWrkMatl)
PX.SM.Users.AMSFKRecentActivityCollection -> Collection(PX.Objects.AM.SFK.AMSFKRecentActivity)
PX.SM.Users.FSAdjustCollection -> Collection(PX.Objects.FS.FSAdjust)
PX.SM.Users.FSAppointmentEmployeeCollection -> Collection(PX.Objects.FS.FSAppointmentEmployee)
PX.SM.Users.FSAppointmentResourceCollection -> Collection(PX.Objects.FS.FSAppointmentResource)
PX.SM.Users.FSAppointmentStatusColorCollection -> Collection(PX.Objects.FS.FSAppointmentStatusColor)
PX.SM.Users.FSApptLineSplitCollection -> Collection(PX.Objects.FS.FSApptLineSplit)
PX.SM.Users.FSBillHistoryCollection -> Collection(PX.Objects.FS.FSBillHistory)
PX.SM.Users.FSBillingCycleCollection -> Collection(PX.Objects.FS.FSBillingCycle)
PX.SM.Users.FSBranchLocationCollection -> Collection(PX.Objects.FS.FSBranchLocation)
PX.SM.Users.FSContractActionCollection -> Collection(PX.Objects.FS.FSContractAction)
PX.SM.Users.FSContractForecastCollection -> Collection(PX.Objects.FS.FSContractForecast)
PX.SM.Users.FSContractForecastDetCollection -> Collection(PX.Objects.FS.FSContractForecastDet)
PX.SM.Users.FSContractGenerationHistoryCollection -> Collection(PX.Objects.FS.FSContractGenerationHistory)
PX.SM.Users.FSContractPeriodCollection -> Collection(PX.Objects.FS.FSContractPeriod)
PX.SM.Users.FSContractPostBatchCollection -> Collection(PX.Objects.FS.FSContractPostBatch)
PX.SM.Users.FSContractPostDetCollection -> Collection(PX.Objects.FS.FSContractPostDet)
PX.SM.Users.FSContractPostDocCollection -> Collection(PX.Objects.FS.FSContractPostDoc)
PX.SM.Users.FSCreatedDocCollection -> Collection(PX.Objects.FS.FSCreatedDoc)
PX.SM.Users.FSCustomerBillingSetupCollection -> Collection(PX.Objects.FS.FSCustomerBillingSetup)
PX.SM.Users.FSCustomerClassBillingSetupCollection -> Collection(PX.Objects.FS.FSCustomerClassBillingSetup)
PX.SM.Users.FSEquipmentComponentCollection -> Collection(PX.Objects.FS.FSEquipmentComponent)
PX.SM.Users.FSEquipmentTypeCollection -> Collection(PX.Objects.FS.FSEquipmentType)
PX.SM.Users.FSGenerationLogErrorCollection -> Collection(PX.Objects.FS.FSGenerationLogError)
PX.SM.Users.FSGeoZoneEmpCollection -> Collection(PX.Objects.FS.FSGeoZoneEmp)
PX.SM.Users.FSManufacturerCollection -> Collection(PX.Objects.FS.FSManufacturer)
PX.SM.Users.FSManufacturerModelCollection -> Collection(PX.Objects.FS.FSManufacturerModel)
PX.SM.Users.FSMasterContractCollection -> Collection(PX.Objects.FS.FSMasterContract)
PX.SM.Users.FSModelComponentCollection -> Collection(PX.Objects.FS.FSModelComponent)
PX.SM.Users.FSModelTemplateComponentCollection -> Collection(PX.Objects.FS.FSModelTemplateComponent)
PX.SM.Users.FSPostBatchCollection -> Collection(PX.Objects.FS.FSPostBatch)
PX.SM.Users.FSPostDetCollection -> Collection(PX.Objects.FS.FSPostDet)
PX.SM.Users.FSPostDocCollection -> Collection(PX.Objects.FS.FSPostDoc)
PX.SM.Users.FSPostInfoCollection -> Collection(PX.Objects.FS.FSPostInfo)
PX.SM.Users.FSProblemCollection -> Collection(PX.Objects.FS.FSProblem)
PX.SM.Users.FSProcessIdentityCollection -> Collection(PX.Objects.FS.FSProcessIdentity)
PX.SM.Users.FSRoomCollection -> Collection(PX.Objects.FS.FSRoom)
PX.SM.Users.FSRouteCollection -> Collection(PX.Objects.FS.FSRoute)
PX.SM.Users.FSRouteDocumentCollection -> Collection(PX.Objects.FS.FSRouteDocument)
PX.SM.Users.FSRouteEmployeeCollection -> Collection(PX.Objects.FS.FSRouteEmployee)
PX.SM.Users.FSRouteSetupCollection -> Collection(PX.Objects.FS.FSRouteSetup)
PX.SM.Users.FSSalesPriceCollection -> Collection(PX.Objects.FS.FSSalesPrice)
PX.SM.Users.FSScheduleDetCollection -> Collection(PX.Objects.FS.FSScheduleDet)
PX.SM.Users.FSScheduleRouteCollection -> Collection(PX.Objects.FS.FSScheduleRoute)
PX.SM.Users.FSServiceContractCollection -> Collection(PX.Objects.FS.FSServiceContract)
PX.SM.Users.FSServiceEquipmentTypeCollection -> Collection(PX.Objects.FS.FSServiceEquipmentType)
PX.SM.Users.FSServiceInventoryItemCollection -> Collection(PX.Objects.FS.FSServiceInventoryItem)
PX.SM.Users.FSServiceLicenseTypeCollection -> Collection(PX.Objects.FS.FSServiceLicenseType)
PX.SM.Users.FSServiceSkillCollection -> Collection(PX.Objects.FS.FSServiceSkill)
PX.SM.Users.FSServiceTemplateCollection -> Collection(PX.Objects.FS.FSServiceTemplate)
PX.SM.Users.FSServiceTemplateDetCollection -> Collection(PX.Objects.FS.FSServiceTemplateDet)
PX.SM.Users.FSServiceVehicleTypeCollection -> Collection(PX.Objects.FS.FSServiceVehicleType)
PX.SM.Users.FSSetupCollection -> Collection(PX.Objects.SV.FSSetup)
PX.SM.Users.FSSODetSplitCollection -> Collection(PX.Objects.FS.FSSODetSplit)
PX.SM.Users.FSSOEmployeeCollection -> Collection(PX.Objects.FS.FSSOEmployee)
PX.SM.Users.FSSOResourceCollection -> Collection(PX.Objects.FS.FSSOResource)
PX.SM.Users.FSSrvOrdTypeCollection -> Collection(PX.Objects.FS.FSSrvOrdType)
PX.SM.Users.FSSrvOrdTypeProblemCollection -> Collection(PX.Objects.FS.FSSrvOrdTypeProblem)
PX.SM.Users.FSTimeSlotCollection -> Collection(PX.Objects.FS.FSTimeSlot)
PX.SM.Users.FSVehicleTypeCollection -> Collection(PX.Objects.FS.FSVehicleType)
PX.SM.Users.FSWeekCodeDateCollection -> Collection(PX.Objects.FS.FSWeekCodeDate)
PX.SM.Users.FSWFStageCollection -> Collection(PX.Objects.FS.FSWFStage)
PX.SM.Users.FSWrkProcessCollection -> Collection(PX.Objects.FS.FSWrkProcess)
PX.SM.Users.T4AMasterTableCollection -> Collection(PX.Objects.Localizations.CA.T4AMasterTable)
PX.SM.Users.T4ASlipCollection -> Collection(PX.Objects.Localizations.CA.T4ASlip)
PX.SM.Users.TaxRegistrationCollection -> Collection(PX.Objects.Localizations.CA.TaxRegistration)
PX.SM.Users.CISMasterTableCollection -> Collection(PX.Objects.Localizations.GB.CISMasterTable)
PX.SM.Users.CISSubcontractorCollection -> Collection(PX.Objects.Localizations.GB.CISSubcontractor)
PX.SM.Users.HMRCSubmissionCollection -> Collection(PX.Objects.Localizations.GB.HMRCSubmission)
PX.SM.Users.UKTaxReportingSettingsCollection -> Collection(PX.Objects.Localizations.GB.UKTaxReportingSettings)
PX.SM.Users.PMVendorEntityCollection -> Collection(PX.Objects.PM.ProjectFiles.VendorEntities.PMVendorEntity)
PX.SM.Users.PJSubmittalTypeCollection -> Collection(PX.Objects.PJ.Submittals.PJ.DAC.PJSubmittalType)
PX.SM.Users.PJSubmittalWorkflowItemCollection -> Collection(PX.Objects.PJ.Submittals.PJ.DAC.PJSubmittalWorkflowItem)
PX.SM.Users.PhotoCollection -> Collection(PX.Objects.PJ.PhotoLogs.PJ.DAC.Photo)
PX.SM.Users.SPInventoryCartItemCollection -> Collection(PX.Objects.Portals.SP.DAC.SPInventoryCartItem)
PX.SM.Users.VPToDoStateCollection -> Collection(PX.Objects.Portals.Vendor.Dashboard.ToDo.VPToDoState)
PX.SM.Users.VPRecentActivityCollection -> Collection(PX.Objects.Portals.Vendor.Dashboard.RecentActivities.VPRecentActivity)
PX.SM.Users.PRAcaAggregateGroupMemberCollection -> Collection(PX.Objects.PR.PRAcaAggregateGroupMember)
PX.SM.Users.PRAcaCompanyMonthlyInformationCollection -> Collection(PX.Objects.PR.PRAcaCompanyMonthlyInformation)
PX.SM.Users.PRAcaCompanyYearlyInformationCollection -> Collection(PX.Objects.PR.PRAcaCompanyYearlyInformation)
PX.SM.Users.PRAcaDeductCoverageInfoCollection -> Collection(PX.Objects.PR.PRAcaDeductCoverageInfo)
PX.SM.Users.PRAcaEmployeeMonthlyInformationCollection -> Collection(PX.Objects.PR.PRAcaEmployeeMonthlyInformation)
PX.SM.Users.PRBandingRulePTOBankCollection -> Collection(PX.Objects.PR.PRBandingRulePTOBank)
PX.SM.Users.PRBatchCollection -> Collection(PX.Objects.PR.PRBatch)
PX.SM.Users.PRBatchDeductCollection -> Collection(PX.Objects.PR.PRBatchDeduct)
PX.SM.Users.PRBatchOvertimeRuleCollection -> Collection(PX.Objects.PR.PRBatchOvertimeRule)
PX.SM.Users.PRCompanyTaxAttributeCollection -> Collection(PX.Objects.PR.PRCompanyTaxAttribute)
PX.SM.Users.PRCRAPayrollAccountCollection -> Collection(PX.Objects.PR.PRCRAPayrollAccount)
PX.SM.Users.PRDeductCodeBenefitIncreasingWageCollection -> Collection(PX.Objects.PR.PRDeductCodeBenefitIncreasingWage)
PX.SM.Users.PRDeductCodeDeductionDecreasingWageCollection -> Collection(PX.Objects.PR.PRDeductCodeDeductionDecreasingWage)
PX.SM.Users.PRDeductCodeEarningIncreasingWageCollection -> Collection(PX.Objects.PR.PRDeductCodeEarningIncreasingWage)
PX.SM.Users.PRDeductCodeTaxDecreasingWageCollection -> Collection(PX.Objects.PR.PRDeductCodeTaxDecreasingWage)
PX.SM.Users.PRDeductCodeTaxIncreasingWageCollection -> Collection(PX.Objects.PR.PRDeductCodeTaxIncreasingWage)
PX.SM.Users.PRDeductionAndBenefitProjectPackageCollection -> Collection(PX.Objects.PR.PRDeductionAndBenefitProjectPackage)
PX.SM.Users.PRDeductionAndBenefitUnionPackageCollection -> Collection(PX.Objects.PR.PRDeductionAndBenefitUnionPackage)
PX.SM.Users.PRDeductionsReducingDisposableNetCollection -> Collection(PX.Objects.PR.PRDeductionsReducingDisposableNet)
PX.SM.Users.PRDirectDepositSplitCollection -> Collection(PX.Objects.PR.PRDirectDepositSplit)
PX.SM.Users.PREIPremiumRateCollection -> Collection(PX.Objects.PR.PREIPremiumRate)
PX.SM.Users.PREmployeeAttributeCollection -> Collection(PX.Objects.PR.PREmployeeAttribute)
PX.SM.Users.PREmployeeClassPTOBankCollection -> Collection(PX.Objects.PR.PREmployeeClassPTOBank)
PX.SM.Users.PREmployeeClassWorkLocationCollection -> Collection(PX.Objects.PR.PREmployeeClassWorkLocation)
PX.SM.Users.PREmployeeDeductCollection -> Collection(PX.Objects.PR.PREmployeeDeduct)
PX.SM.Users.PREmployeeDirectDepositCollection -> Collection(PX.Objects.PR.PREmployeeDirectDeposit)
PX.SM.Users.PREmployeeEarningCollection -> Collection(PX.Objects.PR.PREmployeeEarning)
PX.SM.Users.PREmployeePTOBankCollection -> Collection(PX.Objects.PR.PREmployeePTOBank)
PX.SM.Users.PREmployeeTaxCollection -> Collection(PX.Objects.PR.PREmployeeTax)
PX.SM.Users.PREmployeeTaxAttributeCollection -> Collection(PX.Objects.PR.PREmployeeTaxAttribute)
PX.SM.Users.PREmployeeTaxFormCollection -> Collection(PX.Objects.PR.PREmployeeTaxForm)
PX.SM.Users.PREmployeeTaxFormDataCollection -> Collection(PX.Objects.PR.PREmployeeTaxFormData)
PX.SM.Users.PREmployeeWorkLocationCollection -> Collection(PX.Objects.PR.PREmployeeWorkLocation)
PX.SM.Users.PREntityCompanyTaxAttributeCollection -> Collection(PX.Objects.PR.PREntityCompanyTaxAttribute)
PX.SM.Users.PREntityTaxCodeAttributeCollection -> Collection(PX.Objects.PR.PREntityTaxCodeAttribute)
PX.SM.Users.PRGovernmentSlipCollection -> Collection(PX.Objects.PR.PRGovernmentSlip)
PX.SM.Users.PRGovernmentSlipFieldCollection -> Collection(PX.Objects.PR.PRGovernmentSlipField)
PX.SM.Users.PRLocationCollection -> Collection(PX.Objects.PR.PRLocation)
PX.SM.Users.PRNonPayableBenefitsIncreasingDisposableNetCollection -> Collection(PX.Objects.PR.PRNonPayableBenefitsIncreasingDisposableNet)
PX.SM.Users.PROvertimeRuleCollection -> Collection(PX.Objects.PR.PROvertimeRule)
PX.SM.Users.PRPayGroupCollection -> Collection(PX.Objects.PR.PRPayGroup)
PX.SM.Users.PRPayGroupPeriodCollection -> Collection(PX.Objects.PR.PRPayGroupPeriod)
PX.SM.Users.PRPayGroupPeriodSetupCollection -> Collection(PX.Objects.PR.PRPayGroupPeriodSetup)
PX.SM.Users.PRPayGroupYearCollection -> Collection(PX.Objects.PR.PRPayGroupYear)
PX.SM.Users.PRPayGroupYearSetupCollection -> Collection(PX.Objects.PR.PRPayGroupYearSetup)
PX.SM.Users.PRPaymentCollection -> Collection(PX.Objects.PR.PRPayment)
PX.SM.Users.PRPaymentBatchExportDetailsCollection -> Collection(PX.Objects.PR.PRPaymentBatchExportDetails)
PX.SM.Users.PRPaymentBatchExportHistoryCollection -> Collection(PX.Objects.PR.PRPaymentBatchExportHistory)
PX.SM.Users.PRPaymentDeductCollection -> Collection(PX.Objects.PR.PRPaymentDeduct)
PX.SM.Users.PRPaymentFringeBenefitCollection -> Collection(PX.Objects.PR.PRPaymentFringeBenefit)
PX.SM.Users.PRPaymentFringeBenefitDecreasingRateCollection -> Collection(PX.Objects.PR.PRPaymentFringeBenefitDecreasingRate)
PX.SM.Users.PRPaymentFringeEarningDecreasingRateCollection -> Collection(PX.Objects.PR.PRPaymentFringeEarningDecreasingRate)
PX.SM.Users.PRPaymentOvertimeRuleCollection -> Collection(PX.Objects.PR.PRPaymentOvertimeRule)
PX.SM.Users.PRPaymentProjectPackageDeductCollection -> Collection(PX.Objects.PR.PRPaymentProjectPackageDeduct)
PX.SM.Users.PRPaymentPTOBankCollection -> Collection(PX.Objects.PR.PRPaymentPTOBank)
PX.SM.Users.PRPaymentTaxApplicableAmountsCollection -> Collection(PX.Objects.PR.PRPaymentTaxApplicableAmounts)
PX.SM.Users.PRPaymentTaxSplitCollection -> Collection(PX.Objects.PR.PRPaymentTaxSplit)
PX.SM.Users.PRPaymentUnionPackageDeductCollection -> Collection(PX.Objects.PR.PRPaymentUnionPackageDeduct)
PX.SM.Users.PRPaymentWCPremiumCollection -> Collection(PX.Objects.PR.PRPaymentWCPremium)
PX.SM.Users.PRProjectFringeBenefitRateCollection -> Collection(PX.Objects.PR.PRProjectFringeBenefitRate)
PX.SM.Users.PRProjectFringeBenefitRateReducingDeductCollection -> Collection(PX.Objects.PR.PRProjectFringeBenefitRateReducingDeduct)
PX.SM.Users.PRPTOAdjustmentCollection -> Collection(PX.Objects.PR.PRPTOAdjustment)
PX.SM.Users.PRPTOAdjustmentDetailCollection -> Collection(PX.Objects.PR.PRPTOAdjustmentDetail)
PX.SM.Users.PRPTOBankCollection -> Collection(PX.Objects.PR.PRPTOBank)
PX.SM.Users.PRPTOBankApplicableEarningTypeCollection -> Collection(PX.Objects.PR.PRPTOBankApplicableEarningType)
PX.SM.Users.PRPTODetailCollection -> Collection(PX.Objects.PR.PRPTODetail)
PX.SM.Users.PRRecordOfEmploymentCollection -> Collection(PX.Objects.PR.PRRecordOfEmployment)
PX.SM.Users.PRRegularTypeForOvertimeCollection -> Collection(PX.Objects.PR.PRRegularTypeForOvertime)
PX.SM.Users.PRROEInsurableEarningsByPayPeriodCollection -> Collection(PX.Objects.PR.PRROEInsurableEarningsByPayPeriod)
PX.SM.Users.PRROEOtherMoniesCollection -> Collection(PX.Objects.PR.PRROEOtherMonies)
PX.SM.Users.PRROEStatutoryHolidayPayCollection -> Collection(PX.Objects.PR.PRROEStatutoryHolidayPay)
PX.SM.Users.PRTaxCodeAttributeCollection -> Collection(PX.Objects.PR.PRTaxCodeAttribute)
PX.SM.Users.PRTaxFormBatchCollection -> Collection(PX.Objects.PR.PRTaxFormBatch)
PX.SM.Users.PRTaxRegistrationCollection -> Collection(PX.Objects.PR.PRTaxRegistration)
PX.SM.Users.PRTaxRegistrationAttributeCollection -> Collection(PX.Objects.PR.PRTaxRegistrationAttribute)
PX.SM.Users.PRTaxReportingAccountCollection -> Collection(PX.Objects.PR.PRTaxReportingAccount)
PX.SM.Users.PRTaxSettingAdditionalInformationCollection -> Collection(PX.Objects.PR.PRTaxSettingAdditionalInformation)
PX.SM.Users.PRTaxWebServiceDataCollection -> Collection(PX.Objects.PR.PRTaxWebServiceData)
PX.SM.Users.PRTransactionDateExceptionCollection -> Collection(PX.Objects.PR.PRTransactionDateException)
PX.SM.Users.PRWorkCompensationBenefitRateCollection -> Collection(PX.Objects.PR.PRWorkCompensationBenefitRate)
PX.SM.Users.PRWorkCompensationMaximumInsurableWageCollection -> Collection(PX.Objects.PR.PRWorkCompensationMaximumInsurableWage)
PX.SM.Users.SVAddressCollection -> Collection(PX.Objects.SV.SVAddress)
PX.SM.Users.SVAdjustCollection -> Collection(PX.Objects.SV.SVAdjust)
PX.SM.Users.SVContactCollection -> Collection(PX.Objects.SV.SVContact)
PX.SM.Users.SVEventStatusColorCollection -> Collection(PX.Objects.SV.SVEventStatusColor)
PX.SM.Users.SVEventTaskCollection -> Collection(PX.Objects.SV.SVEventTask)
PX.SM.Users.SVInvoiceCollection -> Collection(PX.Objects.SV.SVInvoice)
PX.SM.Users.SVMarkupCollection -> Collection(PX.Objects.SV.SVMarkup)
PX.SM.Users.SVMyDayReportCollection -> Collection(PX.Objects.SV.SVMyDayReport)
PX.SM.Users.SVOrderCollection -> Collection(PX.Objects.SV.SVOrder)
PX.SM.Users.SVOrderActualCollection -> Collection(PX.Objects.SV.SVOrderActual)
PX.SM.Users.SVOrderDetailCollection -> Collection(PX.Objects.SV.SVOrderDetail)
PX.SM.Users.SVOrderDiscountDetailCollection -> Collection(PX.Objects.SV.SVOrderDiscountDetail)
PX.SM.Users.SVOrderGLAccountCollection -> Collection(PX.Objects.SV.SVOrderGLAccount)
PX.SM.Users.SVOrderTypeCollection -> Collection(PX.Objects.SV.SVOrderType)
PX.SM.Users.SVOrderTypeGLAccountCollection -> Collection(PX.Objects.SV.SVOrderTypeGLAccount)
PX.SM.Users.SVOrderTypeTaskTemplateCollection -> Collection(PX.Objects.SV.SVOrderTypeTaskTemplate)
PX.SM.Users.SVResourceClassCollection -> Collection(PX.Objects.SV.SVResourceClass)
PX.SM.Users.SVResourceClassPropertyCollection -> Collection(PX.Objects.SV.SVResourceClassProperty)
PX.SM.Users.SVResourcePropertyCollection -> Collection(PX.Objects.SV.SVResourceProperty)
PX.SM.Users.SVResourcePropertyMappingCollection -> Collection(PX.Objects.SV.SVResourcePropertyMapping)
PX.SM.Users.SVSchedulingSetupCollection -> Collection(PX.Objects.SV.SVSchedulingSetup)
PX.SM.Users.SVServiceLocationCollection -> Collection(PX.Objects.SV.SVServiceLocation)
PX.SM.Users.SVServiceLocationContactCollection -> Collection(PX.Objects.SV.SVServiceLocationContact)
PX.SM.Users.SVServiceLocationCustomerCollection -> Collection(PX.Objects.SV.SVServiceLocationCustomer)
PX.SM.Users.SVSetupCollection -> Collection(PX.Objects.SV.SVSetup)
PX.SM.Users.SVSetupInvoiceApprovalCollection -> Collection(PX.Objects.SV.SVSetupInvoiceApproval)
PX.SM.Users.SVStagingWarehouseCollection -> Collection(PX.Objects.SV.SVStagingWarehouse)
PX.SM.Users.SVTicketDetailCollection -> Collection(PX.Objects.SV.SVTicketDetail)
PX.SM.Users.SVWorkTaskCollection -> Collection(PX.Objects.SV.SVWorkTask)
PX.SM.Users.SVWorkTaskActionCollection -> Collection(PX.Objects.SV.SVWorkTaskAction)
PX.SM.Users.SVWorkTaskResourcePropertyCollection -> Collection(PX.Objects.SV.SVWorkTaskResourceProperty)
PX.SM.Users.SVWorkTaskTemplateActionCollection -> Collection(PX.Objects.SV.SVWorkTaskTemplateAction)
PX.SM.Users.SVWorkTaskTemplateLaborCollection -> Collection(PX.Objects.SV.SVWorkTaskTemplateLabor)
PX.SM.Users.SVWorkTaskTemplateResourcePropertyCollection -> Collection(PX.Objects.SV.SVWorkTaskTemplateResourceProperty)
PX.SM.Users.PivotFieldCollection -> Collection(PX.Olap.Maintenance.PivotField)
PX.SM.Users.PivotTableCollection -> Collection(PX.Olap.Maintenance.PivotTable)
PX.SM.Users.PPExternalTranCollection -> Collection(PX.PaymentProcessor.ProcessorBase.DAC.PPExternalTran)
PX.SM.Users.PPBillcomBillCollection -> Collection(PX.PaymentProcessor.BillCom.DAC.PPBillcomBill)
PX.SM.Users.PPBillcomFundingAccountCollection -> Collection(PX.PaymentProcessor.BillCom.DAC.PPBillcomFundingAccount)
PX.SM.Users.PPBillcomFundingAccountUserCollection -> Collection(PX.PaymentProcessor.BillCom.DAC.PPBillcomFundingAccountUser)
PX.SM.Users.PPBillcomUserCollection -> Collection(PX.PaymentProcessor.BillCom.DAC.PPBillcomUser)
PX.SM.Users.PPExternalSettingCollection -> Collection(PX.PaymentProcessor.BillCom.DAC.PPExternalSetting)
PX.SM.Users.PPAvidChildPaymentCollection -> Collection(PX.PaymentProcessor.AvidXchange.DAC.PPAvidChildPayment)
PX.SM.Users.PPAvidFundingAccountCollection -> Collection(PX.PaymentProcessor.AvidXchange.DAC.PPAvidFundingAccount)
PX.SM.Users.PPAvidSettingCollection -> Collection(PX.PaymentProcessor.AvidXchange.DAC.PPAvidSetting)
PX.SM.Users.PPExternalCollection -> Collection(PX.PaymentProcessorCommon.DAC.PPExternal)
PX.SM.Users.GridDataPresentationCollection -> Collection(PX.ScreenPreferences.DAC.GridDataPresentation)
PX.SM.Users.SmsPluginCollection -> Collection(PX.SmsProvider.SM.DAC.SmsPlugin)
PX.SM.Users.SmsPluginParameterCollection -> Collection(PX.SmsProvider.SM.DAC.SmsPluginParameter)
PX.SM.Users.CROpportunityCollection -> Collection(PX.Objects.CR.CROpportunity)
PX.SM.Users.CRQuoteCollection -> Collection(PX.Objects.CR.CRQuote)
PX.SM.Users.AMBomMatlCollection -> Collection(PX.Objects.AM.AMBomMatl)
PX.SM.Users.FABookHistCollection -> Collection(PX.Objects.FA.Overrides.AssetProcess.FABookHist)
PX.SM.Users.ContractDetailAcumCollection -> Collection(PX.Objects.CT.ContractDetailAcum)
PX.SM.Users.ARBalancesCollection -> Collection(PX.Objects.AR.ARBalances)
PX.SM.Users.CISHistoryCollection -> Collection(PX.Objects.Localizations.GB.CISHistory)
PX.SM.Users.CISHistoryDetailsCollection -> Collection(PX.Objects.Localizations.GB.CISHistoryDetails)
PX.SM.Users.PRPeriodTaxApplicableAmountsCollection -> Collection(PX.Objects.PR.PRPeriodTaxApplicableAmounts)
PX.SM.Users.PRPeriodTaxesCollection -> Collection(PX.Objects.PR.PRPeriodTaxes)
PX.SM.Users.PRYtdDeductionsCollection -> Collection(PX.Objects.PR.PRYtdDeductions)
PX.SM.Users.PRYtdEarningsCollection -> Collection(PX.Objects.PR.PRYtdEarnings)
PX.SM.Users.PRYtdTaxesCollection -> Collection(PX.Objects.PR.PRYtdTaxes)
PX.SM.Users.CSCalendarBreakTimeCollection -> Collection(PX.Objects.CS.CSCalendarBreakTime)
PX.SM.Users.BlanketSOOrderSiteCollection -> Collection(PX.Objects.SO.DAC.Projections.BlanketSOOrderSite)
PX.SM.Users.EPActivityTypeCollection -> Collection(PX.Objects.EP.EPActivityType)
PX.SM.Users.AMAPSMaintenanceSetupCollection -> Collection(PX.Objects.AM.AMAPSMaintenanceSetup)
PX.SM.Users.FSContractPeriodDetCollection -> Collection(PX.Objects.FS.FSContractPeriodDet)
PX.SM.Users.FSAppointmentLogExtItemLineCollection -> Collection(PX.Objects.FS.FSAppointmentLogExtItemLine)
PX.SM.Users.AutocompleteGeneratorRunCollection -> Collection(PX.AutocompleteGenerator.UI.DAC.AutocompleteGeneratorRun)
PX.SM.Users.LoginTraceCollection -> Collection(PX.SM.LoginTrace)
PX.SM.Users.POReceivePutAwayUserSetupCollection -> Collection(PX.Objects.PO.POReceivePutAwayUserSetup)
PX.SM.Users.PivotFieldPreferencesCollection -> Collection(PX.Olap.Maintenance.PivotFieldPreferences)
PX.SM.Users.UserFilterCollection -> Collection(PX.SM.UserFilter)
PX.SM.Users.AUAuditHistoryStatisticsCollection -> Collection(PX.SM.AUAuditHistoryStatistics)
PX.SM.Users.SOPickPackShipUserSetupCollection -> Collection(PX.Objects.SO.SOPickPackShipUserSetup)
PX.SM.Users.SOShipmentProcessedByUserCollection -> Collection(PX.Objects.SO.SOShipmentProcessedByUser)
PX.SM.Users.FSAppointmentStaffDistinctCollection -> Collection(PX.Objects.FS.FSAppointmentStaffDistinct)
PX.SM.Users.FSAppointmentStaffExtItemLineCollection -> Collection(PX.Objects.FS.FSAppointmentStaffExtItemLine)
PX.SM.Users.OidcUserCollection -> Collection(PX.OidcClient.GraphExtensions.OidcUser)

# PX.SM.UsersInRoles (EntityType)

Label: "Users In Roles"
Key: ApplicationName, Rolename, Username
Entity sets: PX_SM_UsersInRoles, UsersInRoles
Non-filterable, non-selectable: Inherited, DisplayName, State, Domain, Comment

PX.SM.UsersInRoles.Username : Edm.String [key] "Username"
PX.SM.UsersInRoles.Rolename : Edm.String [key] "Role Name"
PX.SM.UsersInRoles.ApplicationName : Edm.String [key required] "ApplicationName"
PX.SM.UsersInRoles.Inherited : Edm.Boolean "Inherited"
PX.SM.UsersInRoles.DisplayName : Edm.String "Display Name"
PX.SM.UsersInRoles.State : Edm.String "Status"
PX.SM.UsersInRoles.Domain : Edm.String "Domain"
PX.SM.UsersInRoles.Comment : Edm.String "Comment"
PX.SM.UsersInRoles.CreatedByID : Edm.Guid "Created By"
PX.SM.UsersInRoles.CreatedByScreenID : Edm.String
PX.SM.UsersInRoles.CreatedDateTime : Edm.DateTimeOffset
PX.SM.UsersInRoles.LastModifiedByID : Edm.Guid "Last Modified By"
PX.SM.UsersInRoles.LastModifiedByScreenID : Edm.String
PX.SM.UsersInRoles.LastModifiedDateTime : Edm.DateTimeOffset
PX.SM.UsersInRoles.UsersByUsername -> PX.SM.Users (Username=Username)
PX.SM.UsersInRoles.UsersByCreatedByID -> PX.SM.Users (CreatedByID=PKID)
PX.SM.UsersInRoles.UsersByLastModifiedByID -> PX.SM.Users (LastModifiedByID=PKID)
PX.SM.UsersInRoles.RolesByRolename -> PX.SM.Roles (ApplicationName=ApplicationName, Rolename=Rolename)

# PX.SM.Version (EntityType)

Label: "Application Version"
Singletons: PX_SM_Version, ApplicationVersion, Version

PX.SM.Version.ComponentName : Edm.String
PX.SM.Version.ComponentType : Edm.String
PX.SM.Version.CurrentVersion : Edm.String "Current Version"
PX.SM.Version.Date : Edm.DateTimeOffset "Last Update Date"
PX.SM.Version.Altered : Edm.DateTimeOffset
PX.SM.Version.PatchVersion : Edm.String "Current Version"

# PX.SM.Warden (EntityType)

Key: InstallationID, Key, Sub, Type
Entity sets: PX_SM_Warden

PX.SM.Warden.InstallationID : Edm.String [key]
PX.SM.Warden.Type : Edm.Int16 [key]
PX.SM.Warden.Key : Edm.String [key]
PX.SM.Warden.Sub : Edm.String [key]
PX.SM.Warden.Expired : Edm.Boolean
PX.SM.Warden.LastRequest : Edm.DateTimeOffset
PX.SM.Warden.Details : Edm.String

# PX.SM.WikiAccessRights (EntityType)

Key: ApplicationName, PageID, RoleName
Entity sets: PX_SM_WikiAccessRights

PX.SM.WikiAccessRights.PageID : Edm.Guid [key]
PX.SM.WikiAccessRights.RoleName : Edm.String [key] "Role Name"
PX.SM.WikiAccessRights.ApplicationName : Edm.String [key]
PX.SM.WikiAccessRights.AccessRights : Edm.Int16 [required] "Access Rights"
PX.SM.WikiAccessRights.RolesByRoleName -> PX.SM.Roles (ApplicationName=ApplicationName, RoleName=Rolename)

# PX.SM.WikiAccessRoles (EntityType)

BaseType: PX.SM.WikiAccessRights
Key: ApplicationName, PageID, RoleName (inherited from PX.SM.WikiAccessRights)
Entity sets: PX_SM_WikiAccessRoles
Filterable: false (fields declared in this DAC cannot be used in $filter or $select; inherited ones can)

PX.SM.WikiAccessRoles.Guest : Edm.Boolean "Guest Role"
PX.SM.WikiAccessRoles.ParentAccessRights : Edm.Int16 "Parent Access Rights"

# PX.SM.WikiArticle (EntityType)

BaseType: PX.SM.WikiPage
Key: PageID (inherited from PX.SM.WikiPage)
Entity sets: PX_SM_WikiArticle

PX.SM.WikiArticle.WikiPageByWikiID -> PX.SM.WikiPage (ParentUID=PageID, WikiID=WikiID, WikiID=PageID)
PX.SM.WikiArticle.WikiPageByParentUID -> PX.SM.WikiPage (ParentUID=PageID)

# PX.SM.WikiArticleInProject (EntityType)

BaseType: PX.SM.WikiDescriptor
Key: PageID (inherited from PX.SM.WikiPage)
Entity sets: PX_SM_WikiArticleInProject

PX.SM.WikiArticleInProject.CompanyID : Edm.Int32 "CompanyId"

# PX.SM.WikiCss (EntityType)

Key: Name
Entity sets: PX_SM_WikiCss

PX.SM.WikiCss.CssID : Edm.Guid "CssID"
PX.SM.WikiCss.Name : Edm.String [key] "Style Name"
PX.SM.WikiCss.Description : Edm.String "Style Description"
PX.SM.WikiCss.Style : Edm.String "Style Definition"
PX.SM.WikiCss.WikiDescriptorExtCollection -> Collection(PX.SM.WikiDescriptorExt)
PX.SM.WikiCss.WikiDescriptorCollection -> Collection(PX.SM.WikiDescriptor)

# PX.SM.WikiDescriptor (EntityType)

BaseType: PX.SM.WikiPage
Key: PageID (inherited from PX.SM.WikiPage)
Entity sets: PX_SM_WikiDescriptor
Non-filterable, non-selectable: SitemapParent, SitemapTitle, WikiTitle, WikiDescription

PX.SM.WikiDescriptor.WikiArticleType : Edm.Int32 [required] "Article Type"
PX.SM.WikiDescriptor.SPWikiArticleType : Edm.Int32 [required] "Article Type"
PX.SM.WikiDescriptor.UrlEdit : Edm.String
PX.SM.WikiDescriptor.PubVirtualPath : Edm.String "Public Virtual Path"
PX.SM.WikiDescriptor.DeletedID : Edm.Guid
PX.SM.WikiDescriptor.HoldEntry : Edm.Boolean "Hold on Edit"
PX.SM.WikiDescriptor.SiteMapTagID : Edm.Int32 "Default Site Map Tag"
PX.SM.WikiDescriptor.RequestApproval : Edm.Boolean "Require Approval"
PX.SM.WikiDescriptor.CssID : Edm.Guid "Style"
PX.SM.WikiDescriptor.CssPrintID : Edm.Guid "Print Style"
PX.SM.WikiDescriptor.SitemapParent : Edm.Guid "Site Map Location"
PX.SM.WikiDescriptor.SitemapTitle : Edm.String "Site Map Title"
PX.SM.WikiDescriptor.WikiTitle : Edm.String "Title"
PX.SM.WikiDescriptor.IsActive : Edm.Boolean [required] "Show on Help Dashboard"
PX.SM.WikiDescriptor.Position : Edm.Double "Sequence"
PX.SM.WikiDescriptor.WikiDescription : Edm.String "Wiki Description"
PX.SM.WikiDescriptor.Category : Edm.String "Section"
PX.SM.WikiDescriptor.DefaultUrl : Edm.String "Default Article"
PX.SM.WikiDescriptor.DefaultIcon : Edm.String "Default Icon"
PX.SM.WikiDescriptor.WikiTagByPageID -> PX.SM.WikiTag (SiteMapTagID=TagID, PageID=WikiID)
PX.SM.WikiDescriptor.WikiCssByCssID -> PX.SM.WikiCss (CssID=CssID)
PX.SM.WikiDescriptor.WikiCssByCssPrintID -> PX.SM.WikiCss (CssPrintID=CssID)

# PX.SM.WikiDescriptorExt (EntityType)

BaseType: PX.SM.WikiDescriptorMaster
Key: PageID (inherited from PX.SM.WikiPage)
Entity sets: PX_SM_WikiDescriptorExt
Non-filterable, non-selectable: RootPageName, HeaderPageName, FooterPageName

PX.SM.WikiDescriptorExt.RootPageID : Edm.Guid "Template"
PX.SM.WikiDescriptorExt.RootPageName : Edm.String "RootPageName"
PX.SM.WikiDescriptorExt.RootPrintPageID : Edm.Guid "Print Template"
PX.SM.WikiDescriptorExt.HeaderPageID : Edm.Guid "Header"
PX.SM.WikiDescriptorExt.HeaderPageName : Edm.String "HeaderPageName"
PX.SM.WikiDescriptorExt.FooterPageID : Edm.Guid "Footer"
PX.SM.WikiDescriptorExt.FooterPageName : Edm.String "FooterPageName"

# PX.SM.WikiDescriptorMaster (EntityType)

BaseType: PX.SM.WikiDescriptor
Key: PageID (inherited from PX.SM.WikiPage)
Entity sets: PX_SM_WikiDescriptorMaster

# PX.SM.WikiFileInPage (EntityType)

Key: FileID, Language, PageID, PageRevisionID
Entity sets: PX_SM_WikiFileInPage
Non-filterable, non-selectable: IsLatest

PX.SM.WikiFileInPage.PageID : Edm.Guid [key]
PX.SM.WikiFileInPage.Language : Edm.String [key] "Language"
PX.SM.WikiFileInPage.PageRevisionID : Edm.Int32 [key] "Page Version ID"
PX.SM.WikiFileInPage.FileID : Edm.Guid [key]
PX.SM.WikiFileInPage.IsLatest : Edm.Boolean "Latest Version"

# PX.SM.WikiNotificationTemplate (EntityType)

BaseType: PX.SM.WikiPage
Key: PageID (inherited from PX.SM.WikiPage)
Entity sets: PX_SM_WikiNotificationTemplate

PX.SM.WikiNotificationTemplate.EntityType : Edm.String "Entity"
PX.SM.WikiNotificationTemplate.MailTo : Edm.String "To"
PX.SM.WikiNotificationTemplate.MailCc : Edm.String "CC"
PX.SM.WikiNotificationTemplate.MailBcc : Edm.String "BCC"
PX.SM.WikiNotificationTemplate.Subject : Edm.String "Subject"
PX.SM.WikiNotificationTemplate.Watchers : Edm.String "Watchers"
PX.SM.WikiNotificationTemplate.GraphType : Edm.String "Graph"
PX.SM.WikiNotificationTemplate.DefaultEMailAccountID : Edm.Int32 "Default Account"
PX.SM.WikiNotificationTemplate.WikiPageByWikiID -> PX.SM.WikiPage (ParentUID=PageID, WikiID=WikiID, WikiID=PageID)
PX.SM.WikiNotificationTemplate.EMailAccountByDefaultEMailAccountID -> PX.SM.EMailAccount (DefaultEMailAccountID=EmailAccountID)

# PX.SM.WikiPage (EntityType)

Key: PageID
Entity sets: PX_SM_WikiPage
Non-filterable, non-selectable: Title, Summary, Keywords, NoteText, Language, PageRevisionID, PageRevisionDateTime, PageRevisionCreatedByID, PublishedDateTime, Content, ContentHtml, OldStatusID, Hold, AllowApprove, Approved, Rejected, AccessRights, ParentAccessRights, VisibleisHtml

PX.SM.WikiPage.PageID : Edm.Guid [key] "PageID"
PX.SM.WikiPage.WikiID : Edm.Guid "Wiki ID"
PX.SM.WikiPage.ArticleType : Edm.Int32
PX.SM.WikiPage.ParentUID : Edm.Guid "Parent Folder"
PX.SM.WikiPage.Number : Edm.Double [required]
PX.SM.WikiPage.Name : Edm.String "Article ID"
PX.SM.WikiPage.Title : Edm.String "Name"
PX.SM.WikiPage.Summary : Edm.String "Summary"
PX.SM.WikiPage.Keywords : Edm.String "Keywords"
PX.SM.WikiPage.Versioned : Edm.Boolean [required] "Versioned"
PX.SM.WikiPage.Folder : Edm.Boolean [required] "Folder"
PX.SM.WikiPage.NoteID : Edm.Guid
PX.SM.WikiPage.NoteText : Edm.String "Note Text"
PX.SM.WikiPage.CreatedByID : Edm.Guid "Created by"
PX.SM.WikiPage.CreatedDateTime : Edm.DateTimeOffset "Created"
PX.SM.WikiPage.LastModifiedByID : Edm.Guid "Last Modified by"
PX.SM.WikiPage.LastModifiedDateTime : Edm.DateTimeOffset "Last Modified"
PX.SM.WikiPage.tstamp : Edm.Binary
PX.SM.WikiPage.Language : Edm.String "Language"
PX.SM.WikiPage.PageRevisionID : Edm.Int32
PX.SM.WikiPage.PageRevisionDateTime : Edm.DateTimeOffset
PX.SM.WikiPage.PageRevisionCreatedByID : Edm.Guid
PX.SM.WikiPage.PublishedDateTime : Edm.DateTimeOffset "Published Date"
PX.SM.WikiPage.Content : Edm.String "Content"
PX.SM.WikiPage.ContentHtml : Edm.String "ContentHtml"
PX.SM.WikiPage.OldStatusID : Edm.Int32 "Status"
PX.SM.WikiPage.StatusID : Edm.Int32
PX.SM.WikiPage.ApprovalGroupID : Edm.Int32 "Approval Group"
PX.SM.WikiPage.ApprovalUserID : Edm.Guid "Approver ID"
PX.SM.WikiPage.Width : Edm.Int32 "Width"
PX.SM.WikiPage.Height : Edm.Int32 "Height"
PX.SM.WikiPage.Hold : Edm.Boolean "Hold"
PX.SM.WikiPage.AllowApprove : Edm.Boolean
PX.SM.WikiPage.Approved : Edm.Boolean "Approved"
PX.SM.WikiPage.Rejected : Edm.Boolean "Rejected"
PX.SM.WikiPage.AccessRights : Edm.Int16 "Access Rights"
PX.SM.WikiPage.ParentAccessRights : Edm.Int16 "Parent Access Rights"
PX.SM.WikiPage.IsHtml : Edm.Boolean "Article Type"
PX.SM.WikiPage.VisibleisHtml : Edm.String "Article Type"
PX.SM.WikiPage.UsersByCreatedByID -> PX.SM.Users (CreatedByID=PKID)
PX.SM.WikiPage.WikiSitePageCollection -> Collection(PX.SM.WikiSitePage)
PX.SM.WikiPage.WikiNotificationTemplateCollection -> Collection(PX.SM.WikiNotificationTemplate)
PX.SM.WikiPage.WikiArticleCollection -> Collection(PX.SM.WikiArticle)
PX.SM.WikiPage.PreferencesGeneralCollection -> Collection(PX.SM.PreferencesGeneral)
PX.SM.WikiPage.KBResponseCollection -> Collection(PX.SM.KBResponse)
PX.SM.WikiPage.KBResponseSummaryCollection -> Collection(PX.SM.KBResponseSummary)

# PX.SM.WikiPageCurrentLanguage (EntityType)

BaseType: PX.SM.WikiPageLanguage
Key: Language, PageID (inherited from PX.SM.WikiPageLanguage)
Entity sets: PX_SM_WikiPageCurrentLanguage

# PX.SM.WikiPageForReport (EntityType)

BaseType: PX.SM.WikiPage
Key: PageID (inherited from PX.SM.WikiPage)
Entity sets: PX_SM_WikiPageForReport

# PX.SM.WikiPageLanguage (EntityType)

Key: Language, PageID
Entity sets: PX_SM_WikiPageLanguage

PX.SM.WikiPageLanguage.PageID : Edm.Guid [key]
PX.SM.WikiPageLanguage.Title : Edm.String "Name"
PX.SM.WikiPageLanguage.Summary : Edm.String "Summary"
PX.SM.WikiPageLanguage.Keywords : Edm.String "Keywords"
PX.SM.WikiPageLanguage.Language : Edm.String [key] "Language"
PX.SM.WikiPageLanguage.LastRevisionID : Edm.Int32 [required] "Version ID"
PX.SM.WikiPageLanguage.LastPublishedID : Edm.Int32 [required] "Published ID"
PX.SM.WikiPageLanguage.LastPublishedDateTime : Edm.DateTimeOffset "Creation Time"

# PX.SM.WikiPageLink (EntityType)

Key: Language, LinkID, PageID, PageRevisionID
Entity sets: PX_SM_WikiPageLink

PX.SM.WikiPageLink.PageID : Edm.Guid [key]
PX.SM.WikiPageLink.Language : Edm.String [key] "Language"
PX.SM.WikiPageLink.PageRevisionID : Edm.Int32 [key required] "Version ID"
PX.SM.WikiPageLink.LinkID : Edm.Guid [key]

# PX.SM.WikiPageMeta (EntityType)

Key: Name, PageID
Entity sets: PX_SM_WikiPageMeta

PX.SM.WikiPageMeta.PageID : Edm.Guid [key]
PX.SM.WikiPageMeta.Name : Edm.String [key] "Name"
PX.SM.WikiPageMeta.Content : Edm.String "Content"

# PX.SM.WikiPagePath (EntityType)

BaseType: PX.SM.WikiPage
Key: PageID (inherited from PX.SM.WikiPage)
Entity sets: PX_SM_WikiPagePath
Filterable: false (fields declared in this DAC cannot be used in $filter or $select; inherited ones can)

PX.SM.WikiPagePath.Path : Edm.String "Path"

# PX.SM.WikiPageSimple (EntityType)

BaseType: PX.SM.WikiPage
Key: PageID (inherited from PX.SM.WikiPage)
Entity sets: PX_SM_WikiPageSimple

# PX.SM.WikiPageWithCurrentLanguage (EntityType)

Key: PageID
Entity sets: PX_SM_WikiPageWithCurrentLanguage

PX.SM.WikiPageWithCurrentLanguage.PageID : Edm.Guid [key] "PageID"
PX.SM.WikiPageWithCurrentLanguage.WikiID : Edm.Guid "Wiki ID"
PX.SM.WikiPageWithCurrentLanguage.ArticleType : Edm.Int32
PX.SM.WikiPageWithCurrentLanguage.ParentUID : Edm.Guid "Parent Folder"
PX.SM.WikiPageWithCurrentLanguage.Number : Edm.Double
PX.SM.WikiPageWithCurrentLanguage.Folder : Edm.Boolean "Folder"
PX.SM.WikiPageWithCurrentLanguage.Name : Edm.String "ID"
PX.SM.WikiPageWithCurrentLanguage.Title : Edm.String
PX.SM.WikiPageWithCurrentLanguage.Summary : Edm.String "Summary"
PX.SM.WikiPageWithCurrentLanguage.TitleLoc : Edm.String
PX.SM.WikiPageWithCurrentLanguage.SummaryLoc : Edm.String "Summary"
PX.SM.WikiPageWithCurrentLanguage.WikiSitePageCollection -> Collection(PX.SM.WikiSitePage)
PX.SM.WikiPageWithCurrentLanguage.WikiNotificationTemplateCollection -> Collection(PX.SM.WikiNotificationTemplate)
PX.SM.WikiPageWithCurrentLanguage.WikiArticleCollection -> Collection(PX.SM.WikiArticle)
PX.SM.WikiPageWithCurrentLanguage.PreferencesGeneralCollection -> Collection(PX.SM.PreferencesGeneral)
PX.SM.WikiPageWithCurrentLanguage.KBResponseCollection -> Collection(PX.SM.KBResponse)
PX.SM.WikiPageWithCurrentLanguage.KBResponseSummaryCollection -> Collection(PX.SM.KBResponseSummary)

# PX.SM.WikiReadLanguage (EntityType)

Key: LocaleID, WikiID
Entity sets: PX_SM_WikiReadLanguage
Non-filterable, non-selectable: Language

PX.SM.WikiReadLanguage.WikiID : Edm.Guid [key]
PX.SM.WikiReadLanguage.LocaleID : Edm.String [key]
PX.SM.WikiReadLanguage.Language : Edm.String "Language"

# PX.SM.WikiRevision (EntityType)

Key: Language, PageID, PageRevisionID
Entity sets: PX_SM_WikiRevision
Non-filterable, non-selectable: Published, SelectedDest

PX.SM.WikiRevision.PageID : Edm.Guid [key]
PX.SM.WikiRevision.Language : Edm.String [key] "Language"
PX.SM.WikiRevision.PageRevisionID : Edm.Int32 [key required] "Version ID"
PX.SM.WikiRevision.Content : Edm.String "Content"
PX.SM.WikiRevision.ContentHtml : Edm.String "ContentHtml"
PX.SM.WikiRevision.PlainText : Edm.String "Plain Text"
PX.SM.WikiRevision.ApprovalByID : Edm.Guid "Approval By"
PX.SM.WikiRevision.ApprovalDateTime : Edm.DateTimeOffset "Approval Time"
PX.SM.WikiRevision.Published : Edm.Boolean "Published"
PX.SM.WikiRevision.CreatedByID : Edm.Guid "Created by"
PX.SM.WikiRevision.CreatedDateTime : Edm.DateTimeOffset "Creation Time"
PX.SM.WikiRevision.SelectedDest : Edm.Boolean "Compare To"
PX.SM.WikiRevision.UID : Edm.Guid
PX.SM.WikiRevision.UsersByCreatedByID -> PX.SM.Users (CreatedByID=PKID)
PX.SM.WikiRevision.UsersByApprovalByID -> PX.SM.Users (ApprovalByID=PKID)

# PX.SM.WikiRevisionLocalized (EntityType)

BaseType: PX.SM.WikiRevision
Key: Language, PageID, PageRevisionID (inherited from PX.SM.WikiRevision)
Entity sets: PX_SM_WikiRevisionLocalized

# PX.SM.WikiRevisionTag (EntityType)

Key: Language, PageID, PageRevisionID, TagID, WikiID
Entity sets: PX_SM_WikiRevisionTag

PX.SM.WikiRevisionTag.WikiID : Edm.Guid [key]
PX.SM.WikiRevisionTag.PageID : Edm.Guid [key]
PX.SM.WikiRevisionTag.Language : Edm.String [key]
PX.SM.WikiRevisionTag.PageRevisionID : Edm.Int32 [key]
PX.SM.WikiRevisionTag.TagID : Edm.Int32 [key] "Tag"
PX.SM.WikiRevisionTag.WikiTagByWikiID -> PX.SM.WikiTag (TagID=TagID, WikiID=WikiID)

# PX.SM.WikiRevisionTagGrouped (EntityType)

BaseType: PX.SM.WikiRevisionTag
Key: Language, PageID, PageRevisionID, TagID, WikiID (inherited from PX.SM.WikiRevisionTag)
Entity sets: PX_SM_WikiRevisionTagGrouped

# PX.SM.WikiSitePage (EntityType)

BaseType: PX.SM.WikiPage
Key: PageID (inherited from PX.SM.WikiPage)
Entity sets: PX_SM_WikiSitePage

PX.SM.WikiSitePage.Hidden : Edm.Boolean "Hidden From Menu"
PX.SM.WikiSitePage.Indexed : Edm.Boolean "Indexed"
PX.SM.WikiSitePage.Expanded : Edm.Boolean "Expanded"
PX.SM.WikiSitePage.FormUrl : Edm.String "Form URL"
PX.SM.WikiSitePage.HideMenu : Edm.Boolean "Hide Menu"
PX.SM.WikiSitePage.Description : Edm.String "Description"
PX.SM.WikiSitePage.Secure : Edm.Boolean [required] "Secured"
PX.SM.WikiSitePage.WikiPageByWikiID -> PX.SM.WikiPage (ParentUID=PageID, WikiID=WikiID, WikiID=PageID)

# PX.SM.WikiSitePath (EntityType)

Key: Number
Entity sets: PX_SM_WikiSitePath
Non-filterable, non-selectable: PageName

PX.SM.WikiSitePath.Number : Edm.Int32 [key]
PX.SM.WikiSitePath.PageID : Edm.Guid
PX.SM.WikiSitePath.Path : Edm.String "Destination Physical Path"
PX.SM.WikiSitePath.PageName : Edm.String "Source Article"

# PX.SM.WikiTag (EntityType)

Key: Description, WikiID
Entity sets: PX_SM_WikiTag

PX.SM.WikiTag.WikiID : Edm.Guid [key]
PX.SM.WikiTag.TagID : Edm.Int32
PX.SM.WikiTag.Description : Edm.String [key] "Description"
PX.SM.WikiTag.WikiDescriptorExtCollection -> Collection(PX.SM.WikiDescriptorExt)
PX.SM.WikiTag.WikiDescriptorCollection -> Collection(PX.SM.WikiDescriptor)
PX.SM.WikiTag.WikiRevisionTagCollection -> Collection(PX.SM.WikiRevisionTag)

# PX.SmsProvider.SM.DAC.SmsPlugin (EntityType)

Label: "SMS Provider"
Key: Name
Entity sets: PX_SmsProvider_SM_DAC_SmsPlugin, SMSProvider, SmsPlugin
Non-filterable, non-selectable: NoteText

PX.SmsProvider.SM.DAC.SmsPlugin.Name : Edm.String [key] "Name"
PX.SmsProvider.SM.DAC.SmsPlugin.PluginTypeName : Edm.String "Provider Type"
PX.SmsProvider.SM.DAC.SmsPlugin.IsDefault : Edm.Boolean [required] "Default"
PX.SmsProvider.SM.DAC.SmsPlugin.NoteID : Edm.Guid
PX.SmsProvider.SM.DAC.SmsPlugin.NoteText : Edm.String "Note Text"
PX.SmsProvider.SM.DAC.SmsPlugin.tstamp : Edm.Binary
PX.SmsProvider.SM.DAC.SmsPlugin.CreatedByID : Edm.Guid "Created By"
PX.SmsProvider.SM.DAC.SmsPlugin.CreatedByScreenID : Edm.String
PX.SmsProvider.SM.DAC.SmsPlugin.CreatedDateTime : Edm.DateTimeOffset "Created On"
PX.SmsProvider.SM.DAC.SmsPlugin.LastModifiedByID : Edm.Guid "Last Modified By"
PX.SmsProvider.SM.DAC.SmsPlugin.LastModifiedByScreenID : Edm.String
PX.SmsProvider.SM.DAC.SmsPlugin.LastModifiedDateTime : Edm.DateTimeOffset "Last Modified On"
PX.SmsProvider.SM.DAC.SmsPlugin.UsersByCreatedByID -> PX.SM.Users (CreatedByID=PKID)
PX.SmsProvider.SM.DAC.SmsPlugin.UsersByLastModifiedByID -> PX.SM.Users (LastModifiedByID=PKID)
PX.SmsProvider.SM.DAC.SmsPlugin.MobileNotificationCollection -> Collection(PX.BusinessProcess.DAC.MobileNotification)

# PX.SmsProvider.SM.DAC.SmsPluginParameter (EntityType)

Label: "Voice Plug-in Details"
Key: Name, PluginName
Entity sets: PX_SmsProvider_SM_DAC_SmsPluginParameter, VoicePluginDetails, SmsPluginParameter

PX.SmsProvider.SM.DAC.SmsPluginParameter.PluginName : Edm.String [key] "PluginName"
PX.SmsProvider.SM.DAC.SmsPluginParameter.PluginTypeName : Edm.String "PluginTypeName"
PX.SmsProvider.SM.DAC.SmsPluginParameter.Name : Edm.String [key] "ID"
PX.SmsProvider.SM.DAC.SmsPluginParameter.LineNumber : Edm.Int32
PX.SmsProvider.SM.DAC.SmsPluginParameter.Description : Edm.String "Name"
PX.SmsProvider.SM.DAC.SmsPluginParameter.IsEncrypted : Edm.Boolean [required]
PX.SmsProvider.SM.DAC.SmsPluginParameter.Value : Edm.String "Value"
PX.SmsProvider.SM.DAC.SmsPluginParameter.CreatedByID : Edm.Guid "Created By"
PX.SmsProvider.SM.DAC.SmsPluginParameter.CreatedByScreenID : Edm.String
PX.SmsProvider.SM.DAC.SmsPluginParameter.CreatedDateTime : Edm.DateTimeOffset "Created On"
PX.SmsProvider.SM.DAC.SmsPluginParameter.LastModifiedByID : Edm.Guid "Last Modified By"
PX.SmsProvider.SM.DAC.SmsPluginParameter.LastModifiedByScreenID : Edm.String
PX.SmsProvider.SM.DAC.SmsPluginParameter.LastModifiedDateTime : Edm.DateTimeOffset "Last Modified On"
PX.SmsProvider.SM.DAC.SmsPluginParameter.UsersByCreatedByID -> PX.SM.Users (CreatedByID=PKID)
PX.SmsProvider.SM.DAC.SmsPluginParameter.UsersByLastModifiedByID -> PX.SM.Users (LastModifiedByID=PKID)

# PX.SP.Alias.SPPortal (EntityType)

Key: PortalID
Entity sets: PX_SP_Alias_SPPortal
Non-filterable, non-selectable: NoteText

PX.SP.Alias.SPPortal.PortalID : Edm.Int32 [key]
PX.SP.Alias.SPPortal.PortalName : Edm.String
PX.SP.Alias.SPPortal.IsActive : Edm.Boolean
PX.SP.Alias.SPPortal.PortalURL : Edm.String
PX.SP.Alias.SPPortal.AccessRole : Edm.String
PX.SP.Alias.SPPortal.InterfaceTheme : Edm.String
PX.SP.Alias.SPPortal.NoteID : Edm.Guid
PX.SP.Alias.SPPortal.NoteText : Edm.String "Note Text"
PX.SP.Alias.SPPortal.BAccountByOrgBAccountID -> PX.Objects.CR.BAccount
PX.SP.Alias.SPPortal.CRContactClassByContactClassID -> PX.Objects.CR.CRContactClass
PX.SP.Alias.SPPortal.ContactBySecurityContactID -> PX.Objects.CR.Contact
PX.SP.Alias.SPPortal.BranchByRestrictByBranchID -> PX.Objects.GL.Branch
PX.SP.Alias.SPPortal.BranchByDefaultBranchID -> PX.Objects.GL.Branch
PX.SP.Alias.SPPortal.UsersByCreatedByID -> PX.SM.Users
PX.SP.Alias.SPPortal.UsersByLastModifiedByID -> PX.SM.Users
PX.SP.Alias.SPPortal.NotificationByCaseActivityNotificationTemplateID -> PX.SM.Notification
PX.SP.Alias.SPPortal.EPLoginTypeByLoginTypeID -> PX.EP.EPLoginType
PX.SP.Alias.SPPortal.RolesByAccessRole -> PX.SM.Roles (AccessRole=Rolename)
PX.SP.Alias.SPPortal.OrganizationByRestrictByOrganizationID -> PX.Objects.GL.DAC.Organization
PX.SP.Alias.SPPortal.SOOrderTypeByDefaultOrderType -> PX.Objects.SO.SOOrderType
PX.SP.Alias.SPPortal.AddressValidatorPluginByAddressLookupPluginID -> PX.Objects.CS.AddressValidatorPlugin
PX.SP.Alias.SPPortal.CashAccountByDefaultBranchID -> PX.Objects.CA.CashAccount
PX.SP.Alias.SPPortal.CCProcessingCenterByProcessingCenterID -> PX.Objects.CA.CCProcessingCenter
PX.SP.Alias.SPPortal.PaymentMethodByCcPaymentMethodID -> PX.Objects.CA.PaymentMethod
PX.SP.Alias.SPPortal.PaymentMethodByEftPaymentMethodID -> PX.Objects.CA.PaymentMethod
PX.SP.Alias.SPPortal.CRCaseClassByCaseClassID -> PX.Objects.CR.CRCaseClass
PX.SP.Alias.SPPortal.VPSecurityNotificationEventCollection -> Collection(PX.Objects.Portals.Vendor.Configuration.VPSecurityNotificationEvent)

# PX.TM.EPCompanyTree (EntityType)

Label: "Workgroup"
Key: Description
Entity sets: PX_TM_EPCompanyTree, Workgroup, EPCompanyTree

PX.TM.EPCompanyTree.WorkGroupID : Edm.Int32 "Work Group"
PX.TM.EPCompanyTree.Description : Edm.String [key] "Workgroup Name"
PX.TM.EPCompanyTree.ParentWGID : Edm.Int32 [required] "Parent WorkGroup"
PX.TM.EPCompanyTree.SortOrder : Edm.Int32
PX.TM.EPCompanyTree.WaitTime : Edm.Int32 "Wait Time"
PX.TM.EPCompanyTree.BypassEscalation : Edm.Boolean "Bypass Escalation"
PX.TM.EPCompanyTree.UseCalendarTime : Edm.Boolean "Use Calendar Time"
PX.TM.EPCompanyTree.AccessRights : Edm.Int16 [required]
PX.TM.EPCompanyTree.CreatedByID : Edm.Guid "Created By"
PX.TM.EPCompanyTree.CreatedByScreenID : Edm.String
PX.TM.EPCompanyTree.CreatedDateTime : Edm.DateTimeOffset
PX.TM.EPCompanyTree.LastModifiedByID : Edm.Guid "Last Modified By"
PX.TM.EPCompanyTree.LastModifiedByScreenID : Edm.String
PX.TM.EPCompanyTree.LastModifiedDateTime : Edm.DateTimeOffset
PX.TM.EPCompanyTree.UsersByCreatedByID -> PX.SM.Users (CreatedByID=PKID)
PX.TM.EPCompanyTree.UsersByLastModifiedByID -> PX.SM.Users (LastModifiedByID=PKID)
PX.TM.EPCompanyTree.EPCompanyTreeByWorkGroupID -> PX.TM.EPCompanyTree (WorkGroupID=ParentWGID)
PX.TM.EPCompanyTree.EPEmployeeCollection -> Collection(PX.Objects.EP.EPEmployee)
PX.TM.EPCompanyTree.EPEmployeeFSRouteEmployeeCollection -> Collection(PX.Objects.FS.EPEmployeeFSRouteEmployee)
PX.TM.EPCompanyTree.ARRetainageWithApplicationsCollection -> Collection(PX.Objects.AR.ARRetainageWithApplications)
PX.TM.EPCompanyTree.ARPaymentCollection -> Collection(PX.Objects.AR.ARPayment)
PX.TM.EPCompanyTree.VendorCollection -> Collection(PX.Objects.AP.Vendor)
PX.TM.EPCompanyTree.CRPMTimeActivityCollection -> Collection(PX.Objects.CR.CRPMTimeActivity)
PX.TM.EPCompanyTree.CRSMEmailCollection -> Collection(PX.Objects.CR.CRSMEmail)
PX.TM.EPCompanyTree.ARInvoiceCollection -> Collection(PX.Objects.AR.ARInvoice)
PX.TM.EPCompanyTree.EPActivityReleaseCollection -> Collection(PX.Objects.EP.EPActivityRelease)
PX.TM.EPCompanyTree.CustomerCollection -> Collection(PX.Objects.AR.Customer)
PX.TM.EPCompanyTree.EPActivityApprove2Collection -> Collection(PX.Objects.EP.EPActivityApprove2)
PX.TM.EPCompanyTree.APInvoiceCollection -> Collection(PX.Objects.AP.APInvoice)
PX.TM.EPCompanyTree.RequestForInformationCollection -> Collection(PX.Objects.PJ.RequestsForInformation.PJ.DAC.RequestForInformation)
PX.TM.EPCompanyTree.ProjectIssueCollection -> Collection(PX.Objects.PJ.ProjectsIssue.PJ.DAC.ProjectIssue)
PX.TM.EPCompanyTree.APPaymentCollection -> Collection(PX.Objects.AP.APPayment)
PX.TM.EPCompanyTree.ARCashSaleCollection -> Collection(PX.Objects.AR.Standalone.ARCashSale)
PX.TM.EPCompanyTree.ARRegisterCollection -> Collection(PX.Objects.AR.ARRegister)
PX.TM.EPCompanyTree.SOOrderCollection -> Collection(PX.Objects.SO.SOOrder)
PX.TM.EPCompanyTree.POOrderCollection -> Collection(PX.Objects.PO.POOrder)
PX.TM.EPCompanyTree.PMProgressWorksheetLineCollection -> Collection(PX.Objects.PM.PMProgressWorksheetLine)
PX.TM.EPCompanyTree.BAccountCollection -> Collection(PX.Objects.CR.BAccount)
PX.TM.EPCompanyTree.INItemClassCollection -> Collection(PX.Objects.IN.INItemClass)
PX.TM.EPCompanyTree.InventoryItemCollection -> Collection(PX.Objects.IN.InventoryItem)
PX.TM.EPCompanyTree.INRegisterCollection -> Collection(PX.Objects.IN.INRegister)
PX.TM.EPCompanyTree.ContactCollection -> Collection(PX.Objects.CR.Contact)
PX.TM.EPCompanyTree.CRActivityCollection -> Collection(PX.Objects.CR.CRActivity)
PX.TM.EPCompanyTree.CRMarketingListCollection -> Collection(PX.Objects.CR.CRMarketingList)
PX.TM.EPCompanyTree.APRegisterCollection -> Collection(PX.Objects.AP.APRegister)
PX.TM.EPCompanyTree.EPRuleCollection -> Collection(PX.Objects.EP.EPRule)
PX.TM.EPCompanyTree.PMTimeActivityCollection -> Collection(PX.Objects.CR.PMTimeActivity)
PX.TM.EPCompanyTree.RQRequisitionCollection -> Collection(PX.Objects.RQ.RQRequisition)
PX.TM.EPCompanyTree.PMCostProjectionByDateCollection -> Collection(PX.Objects.PM.PMCostProjectionByDate)
PX.TM.EPCompanyTree.EPApprovalCollection -> Collection(PX.Objects.EP.EPApproval)
PX.TM.EPCompanyTree.EPExpenseClaimDetailsCollection -> Collection(PX.Objects.EP.EPExpenseClaimDetails)
PX.TM.EPCompanyTree.AMProdItemCollection -> Collection(PX.Objects.AM.AMProdItem)
PX.TM.EPCompanyTree.AMBomItemCollection -> Collection(PX.Objects.AM.AMBomItem)
PX.TM.EPCompanyTree.FSLogCollection -> Collection(PX.Objects.FS.FSLog)
PX.TM.EPCompanyTree.CRCaseCollection -> Collection(PX.Objects.CR.CRCase)
PX.TM.EPCompanyTree.PMChangeOrderCollection -> Collection(PX.Objects.PM.PMChangeOrder)
PX.TM.EPCompanyTree.INItemSiteCollection -> Collection(PX.Objects.IN.INItemSite)
PX.TM.EPCompanyTree.PMProjectCostSpreadCollection -> Collection(PX.Objects.PM.PMProjectCostSpread)
PX.TM.EPCompanyTree.EMailAccountCollection -> Collection(PX.SM.EMailAccount)
PX.TM.EPCompanyTree.EPCompanyTreeCollection -> Collection(PX.TM.EPCompanyTree)
PX.TM.EPCompanyTree.EPCompanyTreeMemberCollection -> Collection(PX.TM.EPCompanyTreeMember)
PX.TM.EPCompanyTree.SOShipmentCollection -> Collection(PX.Objects.SO.SOShipment)
PX.TM.EPCompanyTree.RQRequestCollection -> Collection(PX.Objects.RQ.RQRequest)
PX.TM.EPCompanyTree.POLandedCostDocCollection -> Collection(PX.Objects.PO.POLandedCostDoc)
PX.TM.EPCompanyTree.POReceiptCollection -> Collection(PX.Objects.PO.POReceipt)
PX.TM.EPCompanyTree.POLandedCostDocSCollection -> Collection(PX.Objects.PO.POLandedCostDocS)
PX.TM.EPCompanyTree.PMChangeRequestCollection -> Collection(PX.Objects.PM.PMChangeRequest)
PX.TM.EPCompanyTree.PMCostProjectionCollection -> Collection(PX.Objects.PM.PMCostProjection)
PX.TM.EPCompanyTree.PMProformaCollection -> Collection(PX.Objects.PM.PMProforma)
PX.TM.EPCompanyTree.PMProgressWorksheetCollection -> Collection(PX.Objects.PM.PMProgressWorksheet)
PX.TM.EPCompanyTree.PMWipAdjustmentCollection -> Collection(PX.Objects.PM.PMWipAdjustment)
PX.TM.EPCompanyTree.CADepositCollection -> Collection(PX.Objects.CA.CADeposit)
PX.TM.EPCompanyTree.CRCampaignCollection -> Collection(PX.Objects.CR.CRCampaign)
PX.TM.EPCompanyTree.CROpportunityRevisionCollection -> Collection(PX.Objects.CR.Standalone.CROpportunityRevision)
PX.TM.EPCompanyTree.EPAssignmentRouteCollection -> Collection(PX.Objects.EP.EPAssignmentRoute)
PX.TM.EPCompanyTree.EPTimeActivitiesSummaryCollection -> Collection(PX.Objects.EP.EPTimeActivitiesSummary)
PX.TM.EPCompanyTree.EPWeeklyCrewTimeActivityCollection -> Collection(PX.Objects.EP.EPWeeklyCrewTimeActivity)
PX.TM.EPCompanyTree.AMECOItemCollection -> Collection(PX.Objects.AM.AMECOItem)
PX.TM.EPCompanyTree.AMECRItemCollection -> Collection(PX.Objects.AM.AMECRItem)
PX.TM.EPCompanyTree.AMVendorShipmentCollection -> Collection(PX.Objects.AM.AMVendorShipment)
PX.TM.EPCompanyTree.CROpportunityCollection -> Collection(PX.Objects.CR.CROpportunity)
PX.TM.EPCompanyTree.PMQuoteCollection -> Collection(PX.Objects.PM.PMQuote)
PX.TM.EPCompanyTree.INKitRegisterCollection -> Collection(PX.Objects.IN.INKitRegister)
PX.TM.EPCompanyTree.CRQuoteCollection -> Collection(PX.Objects.CR.CRQuote)
PX.TM.EPCompanyTree.ARAddItemSelectedCollection -> Collection(PX.Objects.AR.ARAddItemSelected)
PX.TM.EPCompanyTree.APAddItemSelectedCollection -> Collection(PX.Objects.AP.APAddItemSelected)
PX.TM.EPCompanyTree.SchedulerWCOperationCollection -> Collection(PX.Objects.AM.SchedulerWCOperation)
PX.TM.EPCompanyTree.SchedulerProductionOrderCollection -> Collection(PX.Objects.AM.SchedulerProductionOrder)

# PX.TM.EPCompanyTreeH (EntityType)

Key: ParentWGID, WorkGroupID
Entity sets: PX_TM_EPCompanyTreeH

PX.TM.EPCompanyTreeH.WorkGroupID : Edm.Int32 [key]
PX.TM.EPCompanyTreeH.ParentWGID : Edm.Int32 [key required]
PX.TM.EPCompanyTreeH.WaitTime : Edm.Int32 "Wait Time"
PX.TM.EPCompanyTreeH.WorkGroupLevel : Edm.Int32
PX.TM.EPCompanyTreeH.ParentWGLevel : Edm.Int32

# PX.TM.EPCompanyTreeMaster (EntityType)

Label: "Workgroup"
BaseType: PX.TM.EPCompanyTree
Key: Description (inherited from PX.TM.EPCompanyTree)
Entity sets: PX_TM_EPCompanyTreeMaster
Filterable: false (fields declared in this DAC cannot be used in $filter or $select; inherited ones can)

PX.TM.EPCompanyTreeMaster.TempChildID : Edm.Int32
PX.TM.EPCompanyTreeMaster.TempParentID : Edm.Int32

# PX.TM.EPCompanyTreeMember (EntityType)

Key: ContactID, WorkGroupID
Entity sets: PX_TM_EPCompanyTreeMember

PX.TM.EPCompanyTreeMember.WorkGroupID : Edm.Int32 [key]
PX.TM.EPCompanyTreeMember.ContactID : Edm.Int32 [key] "Contact"
PX.TM.EPCompanyTreeMember.WaitTime : Edm.Int32 "Wait Time"
PX.TM.EPCompanyTreeMember.IsOwner : Edm.Boolean [required] "Owner"
PX.TM.EPCompanyTreeMember.Active : Edm.Boolean [required] "Active"
PX.TM.EPCompanyTreeMember.MembershipType : Edm.String "Membership Type"
PX.TM.EPCompanyTreeMember.CreatedByID : Edm.Guid "Created By"
PX.TM.EPCompanyTreeMember.CreatedByScreenID : Edm.String
PX.TM.EPCompanyTreeMember.CreatedDateTime : Edm.DateTimeOffset
PX.TM.EPCompanyTreeMember.LastModifiedByID : Edm.Guid "Last Modified By"
PX.TM.EPCompanyTreeMember.LastModifiedByScreenID : Edm.String
PX.TM.EPCompanyTreeMember.LastModifiedDateTime : Edm.DateTimeOffset
PX.TM.EPCompanyTreeMember.ContactByContactID -> PX.Objects.CR.Contact (ContactID=ContactID)
PX.TM.EPCompanyTreeMember.UsersByCreatedByID -> PX.SM.Users (CreatedByID=PKID)
PX.TM.EPCompanyTreeMember.UsersByLastModifiedByID -> PX.SM.Users (LastModifiedByID=PKID)
PX.TM.EPCompanyTreeMember.EPCompanyTreeByWorkGroupID -> PX.TM.EPCompanyTree (WorkGroupID=WorkGroupID)

# PX.TokenLogin.SAGrantHistory (EntityType)

Label: "Access Grant History"
Key: LogID
Entity sets: PX_TokenLogin_SAGrantHistory, AccessGrantHistory, SAGrantHistory

PX.TokenLogin.SAGrantHistory.LogID : Edm.Int32 [key] "LogID"
PX.TokenLogin.SAGrantHistory.Username : Edm.String "Person"
PX.TokenLogin.SAGrantHistory.Type : Edm.String "Action"
PX.TokenLogin.SAGrantHistory.CreatedDateTime : Edm.DateTimeOffset "Date"

# PX.Web.UI.Frameset.Model.DAC.MUIArea (EntityType)

Label: "Area"
Key: AreaID, IsPortal
Entity sets: PX_Web_UI_Frameset_Model_DAC_MUIArea, Area, MUIArea

PX.Web.UI.Frameset.Model.DAC.MUIArea.CreatedByID : Edm.Guid "Created By"
PX.Web.UI.Frameset.Model.DAC.MUIArea.CreatedByScreenID : Edm.String
PX.Web.UI.Frameset.Model.DAC.MUIArea.CreatedDateTime : Edm.DateTimeOffset "Created On"
PX.Web.UI.Frameset.Model.DAC.MUIArea.LastModifiedByID : Edm.Guid "Last Modified By"
PX.Web.UI.Frameset.Model.DAC.MUIArea.LastModifiedByScreenID : Edm.String
PX.Web.UI.Frameset.Model.DAC.MUIArea.LastModifiedDateTime : Edm.DateTimeOffset "Last Modified On"
PX.Web.UI.Frameset.Model.DAC.MUIArea.IsPortal : Edm.Boolean [key]
PX.Web.UI.Frameset.Model.DAC.MUIArea.AreaID : Edm.Guid [key]
PX.Web.UI.Frameset.Model.DAC.MUIArea.Order : Edm.Single
PX.Web.UI.Frameset.Model.DAC.MUIArea.Name : Edm.String
PX.Web.UI.Frameset.Model.DAC.MUIArea.Icon : Edm.String
PX.Web.UI.Frameset.Model.DAC.MUIArea.ScreenID : Edm.String
PX.Web.UI.Frameset.Model.DAC.MUIArea.tstamp : Edm.Binary
PX.Web.UI.Frameset.Model.DAC.MUIArea.SiteMapByScreenID -> PX.SM.SiteMap (ScreenID=ScreenID)
PX.Web.UI.Frameset.Model.DAC.MUIArea.UsersByCreatedByID -> PX.SM.Users (CreatedByID=PKID)
PX.Web.UI.Frameset.Model.DAC.MUIArea.UsersByLastModifiedByID -> PX.SM.Users (LastModifiedByID=PKID)

# PX.Web.UI.Frameset.Model.DAC.MUIFavoriteScreen (EntityType)

Label: "Favorite Screen"
Key: IsPortal, NodeID, Username
Entity sets: PX_Web_UI_Frameset_Model_DAC_MUIFavoriteScreen, FavoriteScreen, MUIFavoriteScreen

PX.Web.UI.Frameset.Model.DAC.MUIFavoriteScreen.CreatedByID : Edm.Guid "Created By"
PX.Web.UI.Frameset.Model.DAC.MUIFavoriteScreen.CreatedByScreenID : Edm.String
PX.Web.UI.Frameset.Model.DAC.MUIFavoriteScreen.CreatedDateTime : Edm.DateTimeOffset "Created On"
PX.Web.UI.Frameset.Model.DAC.MUIFavoriteScreen.LastModifiedByID : Edm.Guid "Last Modified By"
PX.Web.UI.Frameset.Model.DAC.MUIFavoriteScreen.LastModifiedByScreenID : Edm.String
PX.Web.UI.Frameset.Model.DAC.MUIFavoriteScreen.LastModifiedDateTime : Edm.DateTimeOffset "Last Modified On"
PX.Web.UI.Frameset.Model.DAC.MUIFavoriteScreen.IsPortal : Edm.Boolean [key]
PX.Web.UI.Frameset.Model.DAC.MUIFavoriteScreen.Username : Edm.String [key required]
PX.Web.UI.Frameset.Model.DAC.MUIFavoriteScreen.NodeID : Edm.Guid [key]
PX.Web.UI.Frameset.Model.DAC.MUIFavoriteScreen.MUIScreenByNodeID -> PX.Web.UI.Frameset.Model.DAC.MUIScreen (NodeID=NodeID)
PX.Web.UI.Frameset.Model.DAC.MUIFavoriteScreen.UsersByUsername -> PX.SM.Users (Username=Username)
PX.Web.UI.Frameset.Model.DAC.MUIFavoriteScreen.UsersByCreatedByID -> PX.SM.Users (CreatedByID=PKID)
PX.Web.UI.Frameset.Model.DAC.MUIFavoriteScreen.UsersByLastModifiedByID -> PX.SM.Users (LastModifiedByID=PKID)

# PX.Web.UI.Frameset.Model.DAC.MUIFavoriteTile (EntityType)

Label: "Favorite Tile"
Key: IsPortal, TileID, Username
Entity sets: PX_Web_UI_Frameset_Model_DAC_MUIFavoriteTile, FavoriteTile, MUIFavoriteTile

PX.Web.UI.Frameset.Model.DAC.MUIFavoriteTile.CreatedByID : Edm.Guid "Created By"
PX.Web.UI.Frameset.Model.DAC.MUIFavoriteTile.CreatedByScreenID : Edm.String
PX.Web.UI.Frameset.Model.DAC.MUIFavoriteTile.CreatedDateTime : Edm.DateTimeOffset "Created On"
PX.Web.UI.Frameset.Model.DAC.MUIFavoriteTile.LastModifiedByID : Edm.Guid "Last Modified By"
PX.Web.UI.Frameset.Model.DAC.MUIFavoriteTile.LastModifiedByScreenID : Edm.String
PX.Web.UI.Frameset.Model.DAC.MUIFavoriteTile.LastModifiedDateTime : Edm.DateTimeOffset "Last Modified On"
PX.Web.UI.Frameset.Model.DAC.MUIFavoriteTile.IsPortal : Edm.Boolean [key]
PX.Web.UI.Frameset.Model.DAC.MUIFavoriteTile.Username : Edm.String [key required]
PX.Web.UI.Frameset.Model.DAC.MUIFavoriteTile.TileID : Edm.Guid [key]
PX.Web.UI.Frameset.Model.DAC.MUIFavoriteTile.MUITileByTileID -> PX.Web.UI.Frameset.Model.DAC.MUITile (IsPortal=IsPortal, TileID=TileID)
PX.Web.UI.Frameset.Model.DAC.MUIFavoriteTile.UsersByUsername -> PX.SM.Users (Username=Username)
PX.Web.UI.Frameset.Model.DAC.MUIFavoriteTile.UsersByCreatedByID -> PX.SM.Users (CreatedByID=PKID)
PX.Web.UI.Frameset.Model.DAC.MUIFavoriteTile.UsersByLastModifiedByID -> PX.SM.Users (LastModifiedByID=PKID)

# PX.Web.UI.Frameset.Model.DAC.MUIFavoriteWorkspace (EntityType)

Label: "Favorite Workspace"
Key: IsPortal, Username, WorkspaceID
Entity sets: PX_Web_UI_Frameset_Model_DAC_MUIFavoriteWorkspace, FavoriteWorkspace, MUIFavoriteWorkspace

PX.Web.UI.Frameset.Model.DAC.MUIFavoriteWorkspace.CreatedByID : Edm.Guid "Created By"
PX.Web.UI.Frameset.Model.DAC.MUIFavoriteWorkspace.CreatedByScreenID : Edm.String
PX.Web.UI.Frameset.Model.DAC.MUIFavoriteWorkspace.CreatedDateTime : Edm.DateTimeOffset "Created On"
PX.Web.UI.Frameset.Model.DAC.MUIFavoriteWorkspace.LastModifiedByID : Edm.Guid "Last Modified By"
PX.Web.UI.Frameset.Model.DAC.MUIFavoriteWorkspace.LastModifiedByScreenID : Edm.String
PX.Web.UI.Frameset.Model.DAC.MUIFavoriteWorkspace.LastModifiedDateTime : Edm.DateTimeOffset "Last Modified On"
PX.Web.UI.Frameset.Model.DAC.MUIFavoriteWorkspace.IsPortal : Edm.Boolean [key]
PX.Web.UI.Frameset.Model.DAC.MUIFavoriteWorkspace.Username : Edm.String [key required]
PX.Web.UI.Frameset.Model.DAC.MUIFavoriteWorkspace.WorkspaceID : Edm.Guid [key]
PX.Web.UI.Frameset.Model.DAC.MUIFavoriteWorkspace.IsFavorite : Edm.Boolean [required]
PX.Web.UI.Frameset.Model.DAC.MUIFavoriteWorkspace.MUIWorkspaceByWorkspaceID -> PX.Web.UI.Frameset.Model.DAC.MUIWorkspace (IsPortal=IsPortal, WorkspaceID=WorkspaceID)
PX.Web.UI.Frameset.Model.DAC.MUIFavoriteWorkspace.UsersByUsername -> PX.SM.Users (Username=Username)
PX.Web.UI.Frameset.Model.DAC.MUIFavoriteWorkspace.UsersByCreatedByID -> PX.SM.Users (CreatedByID=PKID)
PX.Web.UI.Frameset.Model.DAC.MUIFavoriteWorkspace.UsersByLastModifiedByID -> PX.SM.Users (LastModifiedByID=PKID)

# PX.Web.UI.Frameset.Model.DAC.MUIPinnedScreen (EntityType)

Label: "Pinned Screen"
Key: IsPortal, NodeID, Username, WorkspaceID
Entity sets: PX_Web_UI_Frameset_Model_DAC_MUIPinnedScreen, PinnedScreen, MUIPinnedScreen

PX.Web.UI.Frameset.Model.DAC.MUIPinnedScreen.CreatedByID : Edm.Guid "Created By"
PX.Web.UI.Frameset.Model.DAC.MUIPinnedScreen.CreatedByScreenID : Edm.String
PX.Web.UI.Frameset.Model.DAC.MUIPinnedScreen.CreatedDateTime : Edm.DateTimeOffset "Created On"
PX.Web.UI.Frameset.Model.DAC.MUIPinnedScreen.LastModifiedByID : Edm.Guid "Last Modified By"
PX.Web.UI.Frameset.Model.DAC.MUIPinnedScreen.LastModifiedByScreenID : Edm.String
PX.Web.UI.Frameset.Model.DAC.MUIPinnedScreen.LastModifiedDateTime : Edm.DateTimeOffset "Last Modified On"
PX.Web.UI.Frameset.Model.DAC.MUIPinnedScreen.IsPortal : Edm.Boolean [key]
PX.Web.UI.Frameset.Model.DAC.MUIPinnedScreen.Username : Edm.String [key required]
PX.Web.UI.Frameset.Model.DAC.MUIPinnedScreen.WorkspaceID : Edm.Guid [key]
PX.Web.UI.Frameset.Model.DAC.MUIPinnedScreen.NodeID : Edm.Guid [key]
PX.Web.UI.Frameset.Model.DAC.MUIPinnedScreen.IsPinned : Edm.Boolean [required]
PX.Web.UI.Frameset.Model.DAC.MUIPinnedScreen.MUIScreenByWorkspaceID -> PX.Web.UI.Frameset.Model.DAC.MUIScreen (IsPortal=IsPortal, NodeID=NodeID, WorkspaceID=WorkspaceID)
PX.Web.UI.Frameset.Model.DAC.MUIPinnedScreen.MUIScreenByNodeID -> PX.Web.UI.Frameset.Model.DAC.MUIScreen (WorkspaceID=WorkspaceID, NodeID=NodeID)
PX.Web.UI.Frameset.Model.DAC.MUIPinnedScreen.UsersByUsername -> PX.SM.Users (Username=Username)
PX.Web.UI.Frameset.Model.DAC.MUIPinnedScreen.UsersByCreatedByID -> PX.SM.Users (CreatedByID=PKID)
PX.Web.UI.Frameset.Model.DAC.MUIPinnedScreen.UsersByLastModifiedByID -> PX.SM.Users (LastModifiedByID=PKID)

# PX.Web.UI.Frameset.Model.DAC.MUIScreen (EntityType)

Label: "Screen"
Key: IsPortal, NodeID, WorkspaceID
Entity sets: PX_Web_UI_Frameset_Model_DAC_MUIScreen, Screen, MUIScreen
Non-filterable, non-selectable: ScreenID, Url, Title

PX.Web.UI.Frameset.Model.DAC.MUIScreen.CreatedByID : Edm.Guid "Created By"
PX.Web.UI.Frameset.Model.DAC.MUIScreen.CreatedByScreenID : Edm.String
PX.Web.UI.Frameset.Model.DAC.MUIScreen.CreatedDateTime : Edm.DateTimeOffset "Created On"
PX.Web.UI.Frameset.Model.DAC.MUIScreen.LastModifiedByID : Edm.Guid "Last Modified By"
PX.Web.UI.Frameset.Model.DAC.MUIScreen.LastModifiedByScreenID : Edm.String
PX.Web.UI.Frameset.Model.DAC.MUIScreen.LastModifiedDateTime : Edm.DateTimeOffset "Last Modified On"
PX.Web.UI.Frameset.Model.DAC.MUIScreen.IsPortal : Edm.Boolean [key]
PX.Web.UI.Frameset.Model.DAC.MUIScreen.NodeID : Edm.Guid [key]
PX.Web.UI.Frameset.Model.DAC.MUIScreen.WorkspaceID : Edm.Guid [key]
PX.Web.UI.Frameset.Model.DAC.MUIScreen.Order : Edm.Single
PX.Web.UI.Frameset.Model.DAC.MUIScreen.SubcategoryID : Edm.Guid
PX.Web.UI.Frameset.Model.DAC.MUIScreen.ScreenID : Edm.String
PX.Web.UI.Frameset.Model.DAC.MUIScreen.Url : Edm.String
PX.Web.UI.Frameset.Model.DAC.MUIScreen.Title : Edm.String
PX.Web.UI.Frameset.Model.DAC.MUIScreen.MUISubcategoryBySubcategoryID -> PX.Web.UI.Frameset.Model.DAC.MUISubcategory (IsPortal=IsPortal, SubcategoryID=SubcategoryID)
PX.Web.UI.Frameset.Model.DAC.MUIScreen.MUIWorkspaceByWorkspaceID -> PX.Web.UI.Frameset.Model.DAC.MUIWorkspace (IsPortal=IsPortal, WorkspaceID=WorkspaceID)
PX.Web.UI.Frameset.Model.DAC.MUIScreen.UsersByCreatedByID -> PX.SM.Users (CreatedByID=PKID)
PX.Web.UI.Frameset.Model.DAC.MUIScreen.UsersByLastModifiedByID -> PX.SM.Users (LastModifiedByID=PKID)
PX.Web.UI.Frameset.Model.DAC.MUIScreen.MUIFavoriteScreenCollection -> Collection(PX.Web.UI.Frameset.Model.DAC.MUIFavoriteScreen)
PX.Web.UI.Frameset.Model.DAC.MUIScreen.MUIPinnedScreenCollection -> Collection(PX.Web.UI.Frameset.Model.DAC.MUIPinnedScreen)

# PX.Web.UI.Frameset.Model.DAC.MUIScreenOrderHeader (EntityType)

Key: SubcategoryID, WorkspaceID
Entity sets: PX_Web_UI_Frameset_Model_DAC_MUIScreenOrderHeader

PX.Web.UI.Frameset.Model.DAC.MUIScreenOrderHeader.WorkspaceID : Edm.Guid [key]
PX.Web.UI.Frameset.Model.DAC.MUIScreenOrderHeader.SubcategoryID : Edm.Guid [key]
PX.Web.UI.Frameset.Model.DAC.MUIScreenOrderHeader.tstamp : Edm.Binary

# PX.Web.UI.Frameset.Model.DAC.MUISubcategory (EntityType)

Label: "Subcategory"
Key: IsPortal, SubcategoryID
Entity sets: PX_Web_UI_Frameset_Model_DAC_MUISubcategory, Subcategory, MUISubcategory

PX.Web.UI.Frameset.Model.DAC.MUISubcategory.CreatedByID : Edm.Guid "Created By"
PX.Web.UI.Frameset.Model.DAC.MUISubcategory.CreatedByScreenID : Edm.String
PX.Web.UI.Frameset.Model.DAC.MUISubcategory.CreatedDateTime : Edm.DateTimeOffset "Created On"
PX.Web.UI.Frameset.Model.DAC.MUISubcategory.LastModifiedByID : Edm.Guid "Last Modified By"
PX.Web.UI.Frameset.Model.DAC.MUISubcategory.LastModifiedByScreenID : Edm.String
PX.Web.UI.Frameset.Model.DAC.MUISubcategory.LastModifiedDateTime : Edm.DateTimeOffset "Last Modified On"
PX.Web.UI.Frameset.Model.DAC.MUISubcategory.IsPortal : Edm.Boolean [key]
PX.Web.UI.Frameset.Model.DAC.MUISubcategory.SubcategoryID : Edm.Guid [key]
PX.Web.UI.Frameset.Model.DAC.MUISubcategory.Order : Edm.Single
PX.Web.UI.Frameset.Model.DAC.MUISubcategory.Name : Edm.String "Category"
PX.Web.UI.Frameset.Model.DAC.MUISubcategory.Icon : Edm.String
PX.Web.UI.Frameset.Model.DAC.MUISubcategory.Column : Edm.Int32
PX.Web.UI.Frameset.Model.DAC.MUISubcategory.IsSystem : Edm.Boolean [required]
PX.Web.UI.Frameset.Model.DAC.MUISubcategory.tstamp : Edm.Binary
PX.Web.UI.Frameset.Model.DAC.MUISubcategory.UsersByCreatedByID -> PX.SM.Users (CreatedByID=PKID)
PX.Web.UI.Frameset.Model.DAC.MUISubcategory.UsersByLastModifiedByID -> PX.SM.Users (LastModifiedByID=PKID)
PX.Web.UI.Frameset.Model.DAC.MUISubcategory.MUIScreenCollection -> Collection(PX.Web.UI.Frameset.Model.DAC.MUIScreen)

# PX.Web.UI.Frameset.Model.DAC.MUITile (EntityType)

Label: "Tile"
Key: IsPortal, TileID
Entity sets: PX_Web_UI_Frameset_Model_DAC_MUITile, Tile, MUITile

PX.Web.UI.Frameset.Model.DAC.MUITile.CreatedByID : Edm.Guid "Created By"
PX.Web.UI.Frameset.Model.DAC.MUITile.CreatedByScreenID : Edm.String
PX.Web.UI.Frameset.Model.DAC.MUITile.CreatedDateTime : Edm.DateTimeOffset "Created On"
PX.Web.UI.Frameset.Model.DAC.MUITile.LastModifiedByID : Edm.Guid "Last Modified By"
PX.Web.UI.Frameset.Model.DAC.MUITile.LastModifiedByScreenID : Edm.String
PX.Web.UI.Frameset.Model.DAC.MUITile.LastModifiedDateTime : Edm.DateTimeOffset "Last Modified On"
PX.Web.UI.Frameset.Model.DAC.MUITile.IsPortal : Edm.Boolean [key]
PX.Web.UI.Frameset.Model.DAC.MUITile.TileID : Edm.Guid [key]
PX.Web.UI.Frameset.Model.DAC.MUITile.Order : Edm.Single
PX.Web.UI.Frameset.Model.DAC.MUITile.WorkspaceID : Edm.Guid
PX.Web.UI.Frameset.Model.DAC.MUITile.ScreenID : Edm.String
PX.Web.UI.Frameset.Model.DAC.MUITile.Title : Edm.String
PX.Web.UI.Frameset.Model.DAC.MUITile.Icon : Edm.String
PX.Web.UI.Frameset.Model.DAC.MUITile.Parameters : Edm.String
PX.Web.UI.Frameset.Model.DAC.MUITile.SiteMapByScreenID -> PX.SM.SiteMap (ScreenID=ScreenID)
PX.Web.UI.Frameset.Model.DAC.MUITile.MUIWorkspaceByWorkspaceID -> PX.Web.UI.Frameset.Model.DAC.MUIWorkspace (IsPortal=IsPortal, WorkspaceID=WorkspaceID)
PX.Web.UI.Frameset.Model.DAC.MUITile.UsersByCreatedByID -> PX.SM.Users (CreatedByID=PKID)
PX.Web.UI.Frameset.Model.DAC.MUITile.UsersByLastModifiedByID -> PX.SM.Users (LastModifiedByID=PKID)
PX.Web.UI.Frameset.Model.DAC.MUITile.MUIFavoriteTileCollection -> Collection(PX.Web.UI.Frameset.Model.DAC.MUIFavoriteTile)

# PX.Web.UI.Frameset.Model.DAC.MUITileOrderHeader (EntityType)

Key: WorkspaceID
Entity sets: PX_Web_UI_Frameset_Model_DAC_MUITileOrderHeader

PX.Web.UI.Frameset.Model.DAC.MUITileOrderHeader.WorkspaceID : Edm.Guid [key]
PX.Web.UI.Frameset.Model.DAC.MUITileOrderHeader.tstamp : Edm.Binary
PX.Web.UI.Frameset.Model.DAC.MUITileOrderHeader.MUIWorkspaceByWorkspaceID -> PX.Web.UI.Frameset.Model.DAC.MUIWorkspace (WorkspaceID=WorkspaceID)

# PX.Web.UI.Frameset.Model.DAC.MUIUserPreferences (EntityType)

Label: "User Preferences"
Key: Username
Entity sets: PX_Web_UI_Frameset_Model_DAC_MUIUserPreferences, UserPreferences1, MUIUserPreferences

PX.Web.UI.Frameset.Model.DAC.MUIUserPreferences.CreatedByID : Edm.Guid "Created By"
PX.Web.UI.Frameset.Model.DAC.MUIUserPreferences.CreatedByScreenID : Edm.String
PX.Web.UI.Frameset.Model.DAC.MUIUserPreferences.CreatedDateTime : Edm.DateTimeOffset "Created On"
PX.Web.UI.Frameset.Model.DAC.MUIUserPreferences.LastModifiedByID : Edm.Guid "Last Modified By"
PX.Web.UI.Frameset.Model.DAC.MUIUserPreferences.LastModifiedByScreenID : Edm.String
PX.Web.UI.Frameset.Model.DAC.MUIUserPreferences.LastModifiedDateTime : Edm.DateTimeOffset "Last Modified On"
PX.Web.UI.Frameset.Model.DAC.MUIUserPreferences.Username : Edm.String [key]
PX.Web.UI.Frameset.Model.DAC.MUIUserPreferences.SiteMapPosition : Edm.Int32 [required]
PX.Web.UI.Frameset.Model.DAC.MUIUserPreferences.UsersByUsername -> PX.SM.Users (Username=Username)
PX.Web.UI.Frameset.Model.DAC.MUIUserPreferences.UsersByCreatedByID -> PX.SM.Users (CreatedByID=PKID)
PX.Web.UI.Frameset.Model.DAC.MUIUserPreferences.UsersByLastModifiedByID -> PX.SM.Users (LastModifiedByID=PKID)

# PX.Web.UI.Frameset.Model.DAC.MUIWorkspace (EntityType)

Label: "Workspace"
Key: IsPortal, WorkspaceID
Entity sets: PX_Web_UI_Frameset_Model_DAC_MUIWorkspace, Workspace, MUIWorkspace

PX.Web.UI.Frameset.Model.DAC.MUIWorkspace.CreatedByID : Edm.Guid "Created By"
PX.Web.UI.Frameset.Model.DAC.MUIWorkspace.CreatedByScreenID : Edm.String
PX.Web.UI.Frameset.Model.DAC.MUIWorkspace.CreatedDateTime : Edm.DateTimeOffset "Created On"
PX.Web.UI.Frameset.Model.DAC.MUIWorkspace.LastModifiedByID : Edm.Guid "Last Modified By"
PX.Web.UI.Frameset.Model.DAC.MUIWorkspace.LastModifiedByScreenID : Edm.String
PX.Web.UI.Frameset.Model.DAC.MUIWorkspace.LastModifiedDateTime : Edm.DateTimeOffset "Last Modified On"
PX.Web.UI.Frameset.Model.DAC.MUIWorkspace.IsPortal : Edm.Boolean [key]
PX.Web.UI.Frameset.Model.DAC.MUIWorkspace.WorkspaceID : Edm.Guid [key]
PX.Web.UI.Frameset.Model.DAC.MUIWorkspace.Order : Edm.Single
PX.Web.UI.Frameset.Model.DAC.MUIWorkspace.Title : Edm.String "Title"
PX.Web.UI.Frameset.Model.DAC.MUIWorkspace.Icon : Edm.String
PX.Web.UI.Frameset.Model.DAC.MUIWorkspace.LayoutMode : Edm.Int32 [required]
PX.Web.UI.Frameset.Model.DAC.MUIWorkspace.AreaID : Edm.Guid
PX.Web.UI.Frameset.Model.DAC.MUIWorkspace.ScreenID : Edm.String
PX.Web.UI.Frameset.Model.DAC.MUIWorkspace.IsSystem : Edm.Boolean [required]
PX.Web.UI.Frameset.Model.DAC.MUIWorkspace.tstamp : Edm.Binary
PX.Web.UI.Frameset.Model.DAC.MUIWorkspace.UsersByCreatedByID -> PX.SM.Users (CreatedByID=PKID)
PX.Web.UI.Frameset.Model.DAC.MUIWorkspace.UsersByLastModifiedByID -> PX.SM.Users (LastModifiedByID=PKID)
PX.Web.UI.Frameset.Model.DAC.MUIWorkspace.MUIScreenCollection -> Collection(PX.Web.UI.Frameset.Model.DAC.MUIScreen)
PX.Web.UI.Frameset.Model.DAC.MUIWorkspace.MUITileCollection -> Collection(PX.Web.UI.Frameset.Model.DAC.MUITile)
PX.Web.UI.Frameset.Model.DAC.MUIWorkspace.MUIFavoriteWorkspaceCollection -> Collection(PX.Web.UI.Frameset.Model.DAC.MUIFavoriteWorkspace)
PX.Web.UI.Frameset.Model.DAC.MUIWorkspace.MUITileOrderHeaderCollection -> Collection(PX.Web.UI.Frameset.Model.DAC.MUITileOrderHeader)

# PX.Web.UI.SMPageCache (EntityType)

Singletons: PX_Web_UI_SMPageCache

# ReconciliationTools.APGLDiscrepancyByDocumentEnqResult (EntityType)

Label: "Vendor Details"
Key: DocType, RefNbr
Entity sets: ReconciliationTools_APGLDiscrepancyByDocumentEnqResult
Non-filterable, non-selectable: NoteText, CuryBegBalance, BegBalance, GLTurnover, XXTurnover, Discrepancy, CuryRate, CuryViewState

ReconciliationTools.APGLDiscrepancyByDocumentEnqResult.DocType : Edm.String [key] "Type"
ReconciliationTools.APGLDiscrepancyByDocumentEnqResult.RefNbr : Edm.String [key] "Reference Nbr."
ReconciliationTools.APGLDiscrepancyByDocumentEnqResult.InstallmentCntr : Edm.Int16
ReconciliationTools.APGLDiscrepancyByDocumentEnqResult.CuryID : Edm.String "Currency"
ReconciliationTools.APGLDiscrepancyByDocumentEnqResult.DocDate : Edm.DateTimeOffset "Date"
ReconciliationTools.APGLDiscrepancyByDocumentEnqResult.TranPeriodID : Edm.String "Master Period"
ReconciliationTools.APGLDiscrepancyByDocumentEnqResult.FinPeriodID : Edm.String "Post Period"
ReconciliationTools.APGLDiscrepancyByDocumentEnqResult.VendorID : Edm.Int32 "Vendor"
ReconciliationTools.APGLDiscrepancyByDocumentEnqResult.CuryInfoID : Edm.Int64
ReconciliationTools.APGLDiscrepancyByDocumentEnqResult.Released : Edm.Boolean "Released"
ReconciliationTools.APGLDiscrepancyByDocumentEnqResult.Prebooked : Edm.Boolean "Prebooked"
ReconciliationTools.APGLDiscrepancyByDocumentEnqResult.OpenDoc : Edm.Boolean "Open"
ReconciliationTools.APGLDiscrepancyByDocumentEnqResult.Hold : Edm.Boolean "Hold"
ReconciliationTools.APGLDiscrepancyByDocumentEnqResult.Scheduled : Edm.Boolean
ReconciliationTools.APGLDiscrepancyByDocumentEnqResult.Voided : Edm.Boolean "Void"
ReconciliationTools.APGLDiscrepancyByDocumentEnqResult.NoteID : Edm.Guid
ReconciliationTools.APGLDiscrepancyByDocumentEnqResult.NoteText : Edm.String "Note Text"
ReconciliationTools.APGLDiscrepancyByDocumentEnqResult.ClosedDate : Edm.DateTimeOffset "Closed Date"
ReconciliationTools.APGLDiscrepancyByDocumentEnqResult.ClosedFinPeriodID : Edm.String "Closed Period"
ReconciliationTools.APGLDiscrepancyByDocumentEnqResult.ClosedTranPeriodID : Edm.String "Closed Master Period"
ReconciliationTools.APGLDiscrepancyByDocumentEnqResult.CuryOrigDocAmt : Edm.Decimal "Currency Origin. Amount"
ReconciliationTools.APGLDiscrepancyByDocumentEnqResult.OrigDocAmt : Edm.Decimal "Origin. Amount"
ReconciliationTools.APGLDiscrepancyByDocumentEnqResult.RGOLAmt : Edm.Decimal "RGOL Amount"
ReconciliationTools.APGLDiscrepancyByDocumentEnqResult.OrigDocType : Edm.String "Orig. Doc. Type"
ReconciliationTools.APGLDiscrepancyByDocumentEnqResult.OrigRefNbr : Edm.String "Orig. Ref. Nbr."
ReconciliationTools.APGLDiscrepancyByDocumentEnqResult.ExtRefNbr : Edm.String "Vendor Invoice Nbr./Payment Nbr."
ReconciliationTools.APGLDiscrepancyByDocumentEnqResult.PaymentMethodID : Edm.String "Payment Method"
ReconciliationTools.APGLDiscrepancyByDocumentEnqResult.CuryBegBalance : Edm.Decimal "Currency Period Beg. Balance"
ReconciliationTools.APGLDiscrepancyByDocumentEnqResult.BegBalance : Edm.Decimal "Period Beg. Balance"
ReconciliationTools.APGLDiscrepancyByDocumentEnqResult.CuryDiscActTaken : Edm.Decimal "Currency Cash Discount Taken"
ReconciliationTools.APGLDiscrepancyByDocumentEnqResult.DiscActTaken : Edm.Decimal "Cash Discount Taken"
ReconciliationTools.APGLDiscrepancyByDocumentEnqResult.CuryTaxWheld : Edm.Decimal "Currency Tax Withheld"
ReconciliationTools.APGLDiscrepancyByDocumentEnqResult.TaxWheld : Edm.Decimal "Tax Withheld"
ReconciliationTools.APGLDiscrepancyByDocumentEnqResult.APTurnover : Edm.Decimal "AP Turnover"
ReconciliationTools.APGLDiscrepancyByDocumentEnqResult.GLTurnover : Edm.Decimal "GL Turnover"
ReconciliationTools.APGLDiscrepancyByDocumentEnqResult.CuryDocBal : Edm.Decimal "Currency Balance"
ReconciliationTools.APGLDiscrepancyByDocumentEnqResult.DocBal : Edm.Decimal "Balance"
ReconciliationTools.APGLDiscrepancyByDocumentEnqResult.CuryWhTaxBal : Edm.Decimal
ReconciliationTools.APGLDiscrepancyByDocumentEnqResult.WhTaxBal : Edm.Decimal
ReconciliationTools.APGLDiscrepancyByDocumentEnqResult.Status : Edm.String "Status"
ReconciliationTools.APGLDiscrepancyByDocumentEnqResult.DocDesc : Edm.String "Description"
ReconciliationTools.APGLDiscrepancyByDocumentEnqResult.TranPostPeriodID : Edm.String
ReconciliationTools.APGLDiscrepancyByDocumentEnqResult.FinPostPeriodID : Edm.String
ReconciliationTools.APGLDiscrepancyByDocumentEnqResult.IsMigratedRecord : Edm.Boolean
ReconciliationTools.APGLDiscrepancyByDocumentEnqResult.BatchNbr : Edm.String "Batch Nbr."
ReconciliationTools.APGLDiscrepancyByDocumentEnqResult.PendingPayment : Edm.Boolean
ReconciliationTools.APGLDiscrepancyByDocumentEnqResult.XXTurnover : Edm.Decimal "AP Turnover"
ReconciliationTools.APGLDiscrepancyByDocumentEnqResult.Discrepancy : Edm.Decimal "Discrepancy"
ReconciliationTools.APGLDiscrepancyByDocumentEnqResult.CuryRate : Edm.Decimal
ReconciliationTools.APGLDiscrepancyByDocumentEnqResult.CuryViewState : Edm.Boolean

# ReconciliationTools.ARGLDiscrepancyByDocumentEnqResult (EntityType)

Label: "Customer Details"
Key: DocType, RefNbr
Entity sets: ReconciliationTools_ARGLDiscrepancyByDocumentEnqResult
Non-filterable, non-selectable: NoteText, SignBalance, GLTurnover, XXTurnover, Discrepancy, CuryRate, CuryViewState

ReconciliationTools.ARGLDiscrepancyByDocumentEnqResult.DocType : Edm.String [key] "Type"
ReconciliationTools.ARGLDiscrepancyByDocumentEnqResult.RefNbr : Edm.String [key] "Reference Nbr."
ReconciliationTools.ARGLDiscrepancyByDocumentEnqResult.InstallmentCntr : Edm.Int16
ReconciliationTools.ARGLDiscrepancyByDocumentEnqResult.CustomerID : Edm.Int32 "Customer"
ReconciliationTools.ARGLDiscrepancyByDocumentEnqResult.DocDate : Edm.DateTimeOffset "Date"
ReconciliationTools.ARGLDiscrepancyByDocumentEnqResult.DocDesc : Edm.String "Description"
ReconciliationTools.ARGLDiscrepancyByDocumentEnqResult.DueDate : Edm.DateTimeOffset "Due Date"
ReconciliationTools.ARGLDiscrepancyByDocumentEnqResult.CuryID : Edm.String "Currency"
ReconciliationTools.ARGLDiscrepancyByDocumentEnqResult.CuryInfoID : Edm.Int64
ReconciliationTools.ARGLDiscrepancyByDocumentEnqResult.OrigDocType : Edm.String "Orig. Doc. Type"
ReconciliationTools.ARGLDiscrepancyByDocumentEnqResult.OrigRefNbr : Edm.String "Orig. Ref. Nbr."
ReconciliationTools.ARGLDiscrepancyByDocumentEnqResult.Status : Edm.String "Status"
ReconciliationTools.ARGLDiscrepancyByDocumentEnqResult.TranPeriodID : Edm.String
ReconciliationTools.ARGLDiscrepancyByDocumentEnqResult.FinPeriodID : Edm.String "Post Period"
ReconciliationTools.ARGLDiscrepancyByDocumentEnqResult.ClosedFinPeriodID : Edm.String "Closed Period"
ReconciliationTools.ARGLDiscrepancyByDocumentEnqResult.ClosedTranPeriodID : Edm.String "Closed Period"
ReconciliationTools.ARGLDiscrepancyByDocumentEnqResult.NoteID : Edm.Guid
ReconciliationTools.ARGLDiscrepancyByDocumentEnqResult.NoteText : Edm.String "Note Text"
ReconciliationTools.ARGLDiscrepancyByDocumentEnqResult.OpenDoc : Edm.Boolean
ReconciliationTools.ARGLDiscrepancyByDocumentEnqResult.Released : Edm.Boolean
ReconciliationTools.ARGLDiscrepancyByDocumentEnqResult.IsMigratedRecord : Edm.Boolean
ReconciliationTools.ARGLDiscrepancyByDocumentEnqResult.BatchNbr : Edm.String "Batch Nbr."
ReconciliationTools.ARGLDiscrepancyByDocumentEnqResult.Scheduled : Edm.Boolean
ReconciliationTools.ARGLDiscrepancyByDocumentEnqResult.Voided : Edm.Boolean
ReconciliationTools.ARGLDiscrepancyByDocumentEnqResult.ExtRefNbr : Edm.String "Customer Order Nbr./Payment Nbr."
ReconciliationTools.ARGLDiscrepancyByDocumentEnqResult.PaymentMethodID : Edm.String "Payment Method"
ReconciliationTools.ARGLDiscrepancyByDocumentEnqResult.SignBalance : Edm.Decimal
ReconciliationTools.ARGLDiscrepancyByDocumentEnqResult.CuryOrigDocAmt : Edm.Decimal "Currency Origin. Amount"
ReconciliationTools.ARGLDiscrepancyByDocumentEnqResult.OrigDocAmt : Edm.Decimal "Origin. Amount"
ReconciliationTools.ARGLDiscrepancyByDocumentEnqResult.CuryOrigDiscAmt : Edm.Decimal "Cash Discount"
ReconciliationTools.ARGLDiscrepancyByDocumentEnqResult.OrigDiscAmt : Edm.Decimal
ReconciliationTools.ARGLDiscrepancyByDocumentEnqResult.CuryBegBalance : Edm.Decimal "Currency Period Beg. Balance"
ReconciliationTools.ARGLDiscrepancyByDocumentEnqResult.BegBalance : Edm.Decimal "Period Beg. Balance"
ReconciliationTools.ARGLDiscrepancyByDocumentEnqResult.CuryDiscActTaken : Edm.Decimal "Currency Cash Discount Taken"
ReconciliationTools.ARGLDiscrepancyByDocumentEnqResult.DiscActTaken : Edm.Decimal "Cash Discount Taken"
ReconciliationTools.ARGLDiscrepancyByDocumentEnqResult.CuryWOAmt : Edm.Decimal "Currency Write-Off Amount"
ReconciliationTools.ARGLDiscrepancyByDocumentEnqResult.WOAmt : Edm.Decimal "Write-Off Amount"
ReconciliationTools.ARGLDiscrepancyByDocumentEnqResult.RGOLAmt : Edm.Decimal "RGOL Amount"
ReconciliationTools.ARGLDiscrepancyByDocumentEnqResult.ARTurnover : Edm.Decimal "AR Turnover"
ReconciliationTools.ARGLDiscrepancyByDocumentEnqResult.GLTurnover : Edm.Decimal "GL Turnover"
ReconciliationTools.ARGLDiscrepancyByDocumentEnqResult.CuryDocBal : Edm.Decimal "Currency Balance"
ReconciliationTools.ARGLDiscrepancyByDocumentEnqResult.DocBal : Edm.Decimal "Balance"
ReconciliationTools.ARGLDiscrepancyByDocumentEnqResult.TranPostPeriodID : Edm.String
ReconciliationTools.ARGLDiscrepancyByDocumentEnqResult.FinPostPeriodID : Edm.String
ReconciliationTools.ARGLDiscrepancyByDocumentEnqResult.PendingPayment : Edm.Boolean
ReconciliationTools.ARGLDiscrepancyByDocumentEnqResult.ProjectID : Edm.Int32 "Project"
ReconciliationTools.ARGLDiscrepancyByDocumentEnqResult.XXTurnover : Edm.Decimal "AR Turnover"
ReconciliationTools.ARGLDiscrepancyByDocumentEnqResult.Discrepancy : Edm.Decimal "Discrepancy"
ReconciliationTools.ARGLDiscrepancyByDocumentEnqResult.CuryRate : Edm.Decimal
ReconciliationTools.ARGLDiscrepancyByDocumentEnqResult.CuryViewState : Edm.Boolean

# ReconciliationTools.DiscrepancyByAccountEnqResult (EntityType)

Label: "GL Transaction"
BaseType: PX.Objects.GL.GLTranR
Key: BatchNbr, LineNbr, Module (inherited from PX.Objects.GL.GLTran)
Entity sets: ReconciliationTools_DiscrepancyByAccountEnqResult
Filterable: false (fields declared in this DAC cannot be used in $filter or $select; inherited ones can)

ReconciliationTools.DiscrepancyByAccountEnqResult.GLTurnover : Edm.Decimal "GL Turnover"
ReconciliationTools.DiscrepancyByAccountEnqResult.XXTurnover : Edm.Decimal "Module Turnover"
ReconciliationTools.DiscrepancyByAccountEnqResult.NonXXTrans : Edm.Decimal "Non-Module Transactions"
ReconciliationTools.DiscrepancyByAccountEnqResult.Discrepancy : Edm.Decimal "Discrepancy"

<!-- source: Pastel.Evolution.chm, Pastel.Evolution SDK 11.0.0.10 | verified: 2026-10-02 -->

# IncidentCategory (Class)

Represents an incident category.

**Namespace:** Pastel.Evolution

```csharp
public class IncidentCategory : BranchedRecordBase
```

## Constructors (2)
- `public IncidentCategory( int id )` — Initializes a new instance of the IncidentCategory class
- `public IncidentCategory( string description )` — Initializes a new instance of the IncidentCategory class

## Properties (3)
- `public string Description { get; }` — Gets or sets the record description.
- `public override int ID { get; }` — Gets the internal record ID (0 for new, unsaved records).
- `public override long LongID { get; }`

## Methods (6)
- `public static DataTable _ListCurrentBranch( string criteria )`
  - param `criteria` (System.String)
  - returns: Type: DataTable
- `public static int Find( string criteria )`
  - param `criteria` (System.String)
  - returns: Type: Int32
- `public static int FindByDescription( string description )`
  - param `description` (System.String)
  - returns: Type: Int32
- `public static DataTable List( string criteria )`
  - param `criteria` (System.String)
  - returns: Type: DataTable
- `protected internal override void OnDelete()` — Removes the record from the database, provided it is not referenced by other records.
- `protected internal override void OnSave()` — Persists the record to the database.

# IncidentLogEntry (Class)

Represents an incident log entry.

**Namespace:** Pastel.Evolution

```csharp
public class IncidentLogEntry
```

## Properties (10)
- `public IncidentLogAction Action { get; internal set; }` — Gets the log entry action.
- `public Agent Agent { get; set; }`
- `public int ID { get; }`
- `public Incident Incident { get; }`
- `public int IncidentID { get; }`
- `public Agent NewAgent { get; set; }`
- `public bool Proxy { get; internal set; }`
- `public FieldCollection RawFieldData { get; }`
- `public string Resolution { get; set; }`
- `public FieldCollection UserFields { get; }`

## Methods (3)
- `public static IncidentLogEntry[] _Select( string criteria, string sortOrder )`
  - param `criteria` (System.String)
  - param `sortOrder` (System.String)
  - returns: Type: IncidentLogEntry []
- `public static int Find( string criteria )`
  - param `criteria` (System.String)
  - returns: Type: Int32
- `public static DataTable List( string criteria )`
  - param `criteria` (System.String)
  - returns: Type: DataTable
- `public static DataTable List( string criteria, string sortOrder )`
  - param `criteria` (System.String)
  - param `sortOrder` (System.String)
  - returns: Type: DataTable

# IncidentLogNotification (Class)

Represents an incident notification. These appear in My Desktop\Notifications.

**Namespace:** Pastel.Evolution

```csharp
public class IncidentLogNotification
```

## Constructors (2)
- `public IncidentLogNotification( int id )` — Initializes a new instance of the IncidentLogNotification class
- `public IncidentLogNotification( IncidentLogEntry logEntry )` — Initializes a new instance of the IncidentLogNotification class

## Methods (1)
- `public static int Find( string criteria )`
  - param `criteria` (System.String)
  - returns: Type: Int32

# IncidentType (Class)

Represents an incident type.

**Namespace:** Pastel.Evolution

```csharp
public class IncidentType : BranchedRecordBase
```

## Constructors (2)
- `public IncidentType( int id )` — Initializes a new instance of the IncidentType class
- `public IncidentType( string description )` — Initializes a new instance of the IncidentType class

## Properties (5)
- `public string Description { get; }` — Gets or sets the record description.
- `public int EscalationGroupID { get; }` — Gets or sets the record description.
- `public override int ID { get; }` — Gets the internal record ID (0 for new, unsaved records).
- `public int IncidentTypeGroupID { get; }`
- `public override long LongID { get; }`

## Methods (4)
- `public static DataTable _ListCurrentBranch( string criteria )`
  - param `criteria` (System.String)
  - returns: Type: DataTable
- `public static DataTable List( string criteria )`
  - param `criteria` (System.String)
  - returns: Type: DataTable
- `protected internal override void OnDelete()`
- `protected internal override void OnSave()`

# InventoryBin (Class)

Represents an inventory bin.

**Namespace:** Pastel.Evolution

```csharp
public class InventoryBin : BranchedRecordBase
```

## Constructors (3)
- `public InventoryBin()` — Creates a new instance of a bin.
- `public InventoryBin( int id )` — Creates a new instance of a bin.
- `public InventoryBin( string name )` — Creates a new instance of a bin.

## Properties (3)
- `public override int ID { get; }` — Gets the internal record ID (0 for new, unsaved records).
- `public override long LongID { get; }`
- `public string Name { get; set; }` — Gets or sets the bin's name.

## Methods (5)
- `public static int Find( string criteria )` — Finds a record's database ID.
  - param `criteria` (System.String) — Specifies the criteria as a SQL where clause.
  - returns: Type: Int32 The ID of the first record found; -1 if not record was found.
- `public static int FindByName( string name )` — Finds a record's database ID.
  - param `name` (System.String) — Specifies the bin's name.
  - returns: Type: Int32 The ID of the first record found; -1 if not record was found.
- `public DataTable List( string criteria )` — Gets a list of database records.
  - param `criteria` (System.String) — Specifies the criteria as a SQL where clause.
  - returns: Type: DataTable Table containing selected records.
- `protected internal override void OnDelete()` — Removes the record from the database, provided it is not referenced by other records.
- `protected internal override void OnSave()` — Persists the record to the database.

# InventoryGroup (Class)

Represents an inventory group.

**Namespace:** Pastel.Evolution

```csharp
public class InventoryGroup : BranchedRecordBase
```

## Constructors (3)
- `public InventoryGroup()` — Creates a new instance of a group.
- `public InventoryGroup( int id )` — Creates a new instance of a group.
- `public InventoryGroup( string code )` — Creates a new instance of a group.

## Properties (21)
- `public GLAccount AdjustmentAccount { get; set; }` — Gets or sets the group's overriding adjustment GL account.
- `public int AdjustmentAccountID { get; set; }` — Gets or sets the group's overriding adjustment GL account id.
- `public string Code { get; set; }` — Gets or sets the group's code.
- `public GLAccount CostOfSalesAccount { get; set; }` — Gets or sets the group's overriding cost of sales GL account.
- `public int CostOfSalesAccountID { get; set; }` — Gets or sets the group's overriding cost of sales GL account id.
- `public GLAccount CostVarianceAccount { get; set; }` — Gets or sets the group's overriding cost variance GL account.
- `public int CostVarianceAccountID { get; set; }` — Gets or sets the group's overriding cost variance GL account id.
- `public string Description { get; set; }` — Gets or sets the group's description.
- `public override int ID { get; }` — Gets the internal record ID (0 for new, unsaved records).
- `public override long LongID { get; }`
- `public double MinimumGPPercent { get; set; }`
- `public GLAccount PurchasesAccount { get; set; }` — Gets or sets the group's overriding purchases GL account.
- `public int PurchasesAccountID { get; set; }` — Gets or sets the group's overriding purchases GL account id.
- `public GLAccount PurchasesCostVarianceAccount { get; set; }` — Gets or sets the group's overriding purchases cost variance GL account.
- `public int PurchasesCostVarianceAccountID { get; set; }` — Gets or sets the group's overriding purchases cost variance GL account ID.
- `public GLAccount SalesAccount { get; set; }` — Gets or sets the group's overriding sales GL account.
- `public int SalesAccountID { get; set; }` — Gets or sets the group's overriding sales GL account id.
- `public GLAccount StockAccount { get; set; }` — Gets or sets the group's overriding stock GL account.
- `public int StockAccountID { get; set; }` — Gets or sets the group's overriding stock GL account id.
- `public GLAccount WipAccount { get; set; }` — Gets or sets the group's overriding work-in-progress GL account.
- `public int WipAccountID { get; set; }` — Gets or sets the group's overriding work-in-progress GL account id.

## Methods (8)
- `public static int Find( string criteria )` — Finds an inventory group ID.
  - param `criteria` (System.String) — The criteria passed to the SQL query. Eg. StGroup = 'INT001' or Description like '%Internal%'
  - returns: Type: Int32 The ID of the first record found; -1 if not record was found.
- `public static int FindByCode( string code )` — Attempts to find an inventory group by using its code and returns its ID.
  - param `code` (System.String) — The code used to lookup the group.
  - returns: Type: Int32 -1 if no record was found, else the id of the first record matching the criteria supplied.
- `public static InventoryGroup Get( string criteria )` — Returns the [first] group object with the code specified; otherwise, returns null.
  - param `criteria` (System.String) — Eg. Code like '1_B%'
  - returns: Type: InventoryGroup
- `public static InventoryGroup GetByCode( string code )` — Returns a group object corresponding to the code specified; otherwise, returns null.
  - param `code` (System.String)
  - returns: Type: InventoryGroup
- `public DataTable List( string criteria )` — Gets a list of database records.
  - param `criteria` (System.String) — Specifies the criteria as a SQL where clause.
  - returns: Type: DataTable Table containing selected records.
- `protected internal override void OnDelete()` — Removes the record from the database, provided it is not referenced by other records.
- `protected internal override void OnSave()` — Persists the record to the database.
- `public override string ToString()`
  - returns: Type: String

# InventoryItem (Class)

Respresents an inventory item, typically products sold or services rendered.

**Namespace:** Pastel.Evolution

```csharp
public class InventoryItem : AccountBase
```

## Constructors (3)
- `public InventoryItem()` — Creates a new instance of a stock item.
- `public InventoryItem( int id )` — Creates a new instance of a stock item.
- `public InventoryItem( string code )` — Creates a new instance of a stock item.

## Properties (58)
- `public bool _LotsExpire { get; set; }` — Gets or sets whether or not the stock item is tracked in lots.
- `public override bool Active { get; set; }` — Gets or sets the record's operational state. Inactive items cannot be used in further transactions.
- `public bool AllowDuplicateSerialNumber { get; set; }` — Gets or sets whether the serial number item allows for duplicate serial numbers.
- `public bool AllowNegativeStock { get; }` — Whether or not the item allows for negative stock.
- `public double AverageUnitCost { get; internal set; }` — Gets the stock item's average unit cost.
- `public string BarCode { get; set; }` — Gets or sets the stock item's bar code.
- `public InventoryBin BinCode { get; set; }` — Gets or sets the stock item's bin.
- `public override string Code { get; set; }` — Gets or sets the item code. When segmented, the full item code is returned; however, when setting the code, be sure to only set the item's short code.
- `public InventoryCostingMethod CostingMethod { get; set; }` — Gets the unit cost according to chosen costing method set in inventory preferences.
- `public TaxRate DefaultCreditNoteTaxType { get; set; }` — Gets or sets the stock item's default credit note tax type.
- `public TaxRate DefaultGoodsReceivedTaxType { get; set; }` — Gets or sets the stock item's default tax type for goods received notes.
- `public TaxRate DefaultInvoicingTaxType { get; set; }` — Gets or sets the stock item's default invoicing tax type.
- `public Unit DefaultPurchaseUnit { get; set; }`
- `public int DefaultPurchaseUnitID { get; set; }`
- `public TaxRate DefaultReturnToSupplierTaxType { get; set; }` — Gets or sets the stock item's default tax type used on returns to supplier .
- `public double DefaultSellingPrice { get; }` — Gets the stock item's default exclusive selling price (belonging to the default price list).
- `public Unit DefaultSellingUnit { get; set; }`
- `public int DefaultSellingUnitID { get; set; }`
- `public override string Description { get; set; }` — Gets or sets the stock item's description.
- `public string Description_2 { get; set; }` — Gets or sets the stock item's 2nd description.
- `public string Description_3 { get; set; }` — Gets or sets the stock item's 3rd description.
- `public InventoryGroup Group { get; set; }` — Gets or sets the stock item's group.
- `public double HighestUnitCost { get; internal set; }` — Gets the stock item's highest unit cost.
- `public override int ID { get; }` — Gets the internal record ID (0 for new, unsaved records).
- `public LotStatus InitialLotStatus { get; set; }`
- `public int InitialLotStatusID { get; set; }`
- `public bool IsCommissionable { get; set; }` — Gets or sets whether or not the stock item is commissionable.
- `public bool IsLotTracked { get; set; }` — Gets or sets whether or not the stock item is tracked in lots.
- `public bool IsSegmented { get; }` — Whether or not the item is made up of segments.
- `public bool IsSerialTracked { get; set; }` — Gets or sets whether or not the stock item is tracked by serial numbers.
- `public bool IsServiceItem { get; set; }` — Gets or sets whether or not the item is a service item.
- `public bool IsStrictSerialTracked { get; set; }` — Gets or sets whether or not the stock item is serial-tracked using the "strict" method.
- `public bool IsWarehouseTracked { get; set; }` — Gets or sets whether or not the item is tracked in warehouses.
- `public InventoryItem this[ string code ] { get; }` — Gets the stock item's warehouse context.
- `public double LatestUnitCost { get; internal set; }` — Gets the stock item's latest unit cost.
- `public override long LongID { get; }`
- `public double LowestUnitCost { get; internal set; }` — Gets the stock item's lowest unit cost.
- `public double MininumGPPercentage { get; set; }`
- `public override Module Module { get; }` — Gets the stock item's Evolution module.
- `public PackCode PackCode { get; set; }` — Gets or sets the stock item's pack code.
- `public double QtyFree { get; }` — Gets the stock item's free quantity.
- `public double QtyOnHand { get; }` — Gets the stock item's quantity on hand.
- `public double QtyOnPurchaseOrder { get; }` — Gets the stock item's quantity on purchase order.
- `public double QtyOnSalesOrder { get; }` — Gets the stock item's quantity on sales order.
- `public double QtyReserved { get; }` — Gets the stock item's reserved quantity.
- `public double QtyWIP { get; internal set; }` — Gets the quantity of stock on active jobs (work in progress).
- `[ObsoleteAttribute("Use UserFields instead.")] public FieldCollection RawFieldData { get; }`
- `public InventorySegmentCollection Segments { get; }` — Gets the stock item's segment collection.
- `public double SellingPrice1 { get; set; }` — Gets or sets the exclusive selling price belonging to the "first" price list in the system (default: "Price List 1").
- `public double SellingPrice2 { get; set; }` — Gets or sets the exclusive selling price belonging to the "second" price list in the system (default: "Price List 2").
- `public double SellingPrice3 { get; set; }` — Gets or sets the exclusive selling price belonging to the "third" price list in the system (default: "Price List 3").
- `public SellingPriceCollection SellingPrices { get; }` — Gets the stock item's selling price collection.
- `public string ShortCode { get; }` — Gets the stock item's short code.
- `public double StandardUnitCost { get; internal set; }` — Gets the stock item's standard unit cost.
- `public Unit StockingUnit { get; set; }`
- `public double UnitCost { get; internal set; }` — Gets the unit cost according to chosen costing method set in inventory preferences.
- `public FieldCollection UserFields { get; }`
- `public WarehouseContextCollection WarehouseContexts { get; }` — Gets the stock item's warehouse context collection.

## Methods (13)
- `public static bool _Exists( string code )` — Experimental method.
  - param `code` (System.String)
  - returns: Type: Boolean
- `public string _GenerateAccountCode( string seed )`
  - param `seed` (System.String)
  - returns: Type: String
- `public static DataTable _ListCurrentBranch( string criteria )`
  - param `criteria` (System.String)
  - returns: Type: DataTable
- `public void _Refresh()` — Experimental method.
- `public static InventoryItem[] _Select( string criteria )` — Experimental Method
  - param `criteria` (System.String)
  - returns: Type: InventoryItem []
- `public static InventoryItem[] _Select( string criteria, string sortOrder )` — Experimental Method
  - param `criteria` (System.String)
  - param `sortOrder` (System.String)
  - returns: Type: InventoryItem []
- `public static int Find( string criteria )` — Finds a stock item ID.
  - param `criteria` (System.String) — The SQL criteria to apply to the search, e.g. Code = 'ABC00112' or Description_1 like '%MOLD%'
  - returns: Type: Int32 The ID of the first record found; -1 if not record was foun.
- `public static int FindByCode( string code )` — Attempts to find an inventory item by its code and returns its ID.
  - param `code` (System.String) — The code used to lookup the account.
  - returns: Type: Int32 -1 if no record was found, else the id of the first account matching the criteria supplied.
- `public static InventoryItem Get( string criteria )` — Returns an instance of the first record satisfying the criteria specified; otherwise, returns null.
  - param `criteria` (System.String) — Eg. Code = 'STO0021' or Description like '%Stone%'
  - returns: Type: InventoryItem The record found; otherwise null
- `public static InventoryItem GetByCode( string code )` — Returns a inventory item object corresponding to the code specified; otherwise, returns null.
  - param `code` (System.String) — Specifies the code.
  - returns: Type: InventoryItem The record found; otherwise null
- `public static DataTable List( string criteria )` — Lists stock items for the supplied criteria.
  - param `criteria` (System.String)
  - returns: Type: DataTable
- `public static DataTable List( string criteria, string sortOrder )` — Lists stock items for the supplied criteria.
  - param `criteria` (System.String) — The SQL criteria used to locate the record, e.g. Code like '1___'
  - param `sortOrder` (System.String) — The SQL order by clause to use, e.g. ItemActive desc, Code
  - returns: Type: DataTable
  - remarks: Table aliases to be used in criteria: Core, Bin
- `protected internal override void OnDelete()`
- `protected internal override void OnSave()`
- `public override string ToString()`
  - returns: Type: String

# InventorySegmentCollection (Class)

**Namespace:** Pastel.Evolution

```csharp
public class InventorySegmentCollection : IEnumerable
```

## Properties (1)
- `Item` — Gets a selling price in the item's price collection.

## Methods (1)
- `public IEnumerator GetEnumerator()`
  - returns: Type: IEnumerator

## Fields (1)
- `protected ArrayList InnerList`

# InventorySegmentGroup (Class)

**Namespace:** Pastel.Evolution

```csharp
public class InventorySegmentGroup
```

## Properties (2)
- `public int ID { get; }` — Gets the internal record ID (0 for new, unsaved records).
- `public InventorySegmentType SegmentType { get; }` — Gets the segment group's segment type.

## Methods (1)
- `public static DataTable List( string criteria )` — Gets a list of database records.
  - param `criteria` (System.String) — Specifies the criteria as a SQL where clause.
  - returns: Type: DataTable Table containing selected records.

# InventorySegmentType (Class)

**Namespace:** Pastel.Evolution

```csharp
public class InventorySegmentType
```

## Properties (2)
- `public string Description { get; }` — Gets the segment type's description.
- `public int ID { get; }` — Gets the internal record ID (0 for new, unsaved records).

## Methods (3)
- `public static int Find( string criteria )` — Finds a record's database ID.
  - param `criteria` (System.String) — Specifies the criteria as a SQL where clause.
  - returns: Type: Int32 The ID of the first record found; -1 if not record was found.
- `public static int FindByDescription( string description )`
  - param `description` (System.String)
  - returns: Type: Int32
- `public static DataTable List( string criteria )` — Gets a list of database records.
  - param `criteria` (System.String) — Specifies the criteria as a SQL where clause.
  - returns: Type: DataTable Table containing selected records.

# InventorySegmentValue (Class)

**Namespace:** Pastel.Evolution

```csharp
public class InventorySegmentValue
```

## Constructors (4)
- `public InventorySegmentValue( string segmentType, string value )` — Initializes a new instance of the InventorySegmentValue class
- `public InventorySegmentValue( InventorySegmentType type, string value )` — Initializes a new instance of the InventorySegmentValue class
- `public InventorySegmentValue( string segmentType, InventorySegmentGroup group, string value )` — Initializes a new instance of the InventorySegmentValue class
- `public InventorySegmentValue( InventorySegmentType type, InventorySegmentGroup group, string value )` — Initializes a new instance of the InventorySegmentValue class

## Properties (4)
- `public string Description { get; set; }`
- `public int ID { get; }`
- `public InventorySegmentGroup SegmentGroup { get; }`
- `public string Value { get; set; }`

## Methods (6)
- `public static int Find( string criteria )` — Finds a customer account ID.
  - param `criteria` (System.String) — The criteria passed to the SQL query. Eg. Account = 'CASH001' or Name like '%CASH%'
  - returns: Type: Int32
- `public static int FindByCode( string code )` — Attempts to find an AR account by its account code and returns its ID.
  - param `code` (System.String) — The account code used to lookup the account.
  - returns: Type: Int32 -1 if no record was found, else the id of the first account matching the criteria supplied.
- `public static InventorySegmentValue Get( string criteria )` — Returns the [first] customer object with the account code specified; otherwise, returns null .
  - param `criteria` (System.String) — Eg. Account = 'CASH001' or Name like '%CASH%'
  - returns: Type: InventorySegmentValue
- `public static InventorySegmentValue GetByCode( string type, string code )` — Returns a customer object corresponding to the code specified; otherwise, returns null .
  - param `type` (System.String)
  - param `code` (System.String)
  - returns: Type: InventorySegmentValue
- `public static InventorySegmentValue GetByCode( InventorySegmentType type, string code )` — Returns a customer object corresponding to the code specified; otherwise, returns null .
  - param `type` (Pastel.Evolution.InventorySegmentType) — The segment type.
  - param `code` (System.String) — The segment code.
  - returns: Type: InventorySegmentValue
- `public static InventorySegmentValue GetByCode( string segmentType, InventorySegmentGroup group, string code )` — Returns a customer object corresponding to the code specified; otherwise, returns null .
  - param `segmentType` (System.String)
  - param `group` (Pastel.Evolution.InventorySegmentGroup)
  - param `code` (System.String)
  - returns: Type: InventorySegmentValue
- `public static InventorySegmentValue GetByCode( InventorySegmentType type, InventorySegmentGroup group, string code )` — Returns a customer object corresponding to the code specified; otherwise, returns null .
  - param `type` (Pastel.Evolution.InventorySegmentType)
  - param `group` (Pastel.Evolution.InventorySegmentGroup)
  - param `code` (System.String)
  - returns: Type: InventorySegmentValue
- `public static DataTable List( string criteria )`
  - param `criteria` (System.String)
  - returns: Type: DataTable
- `public static DataTable ListBySegmentGroupID( int id )`
  - param `id` (System.Int32)
  - returns: Type: DataTable

# InventoryTransaction (Class)

Represents an inventory transaction.

**Namespace:** Pastel.Evolution

```csharp
public class InventoryTransaction : TransactionBase,
    ICloneable
```

## Properties (44)
- `public override AccountBase Account { get; set; }` — Gets or sets the transaction's account.
- `public override int AccountID { get; set; }` — Gets or sets the transaction's account id.
- `public override string Audit { get; }` — Gets the transaction's audit number.
- `public override Branch Branch { get; set; }`
- `public override int BranchID { get; internal set; }`
- `public override double Credit { get; set; }` — Gets the credit value posted by the transaction.
- `public int CurrencyID { get; set; }` — Gets or sets the account's currency id. 0 indicates local currency.
- `public override DateTime Date { get; set; }` — Gets or sets the transaction date.
- `public override double Debit { get; set; }` — Gets the debit value posted by the transaction.
- `public override string Description { get; set; }` — Gets or sets the transaction's description.
- `public override string ExtOrderNo { get; set; }` — Gets or sets the transaction's external order number.
- `public double ForeignTax { get; set; }`
- `public override long ID { get; }` — Gets the internal record ID (0 for new, unsaved records).
- `public InventoryItem InventoryItem { get; set; }` — Gets or sets the transaction's stock item.
- `public JobCard JobCard { get; internal set; }` — Gets or sets the JobCard associated with this transaction.
- `public long JobCardID { get; internal set; }` — Gets the JobCard ID.
- `public Lot Lot { get; set; }` — Gets the transaction's assigned lot.
- `public override ModuleID ModID { get; set; }` — Gets or sets the transaction's module identifier.
- `public override Module Module { get; }` — Gets the transaction's Evolution module.
- `public InventoryOperation Operation { get; set; }` — Gets or sets the transaction operation.
- `public override string OrderNo { get; set; }` — Gets or sets the transaction's order number.
- `public GLAccount OverrideCreditAccount { get; set; }` — Gets or sets the GL account to use when posting the transaction's credit leg, overriding the credit account configured in the transaction type.
- `public GLAccount OverrideDebitAccount { get; set; }` — Gets or sets the GL account to use when posting the transaction's debit leg, overriding the debit account configured in the transaction type.
- `public bool PostToGL { get; set; }` — Enables or disables posting to the general ledger.
- `public override Project Project { get; set; }` — Gets or sets the transaction's project.
- `public override int ProjectID { get; set; }` — Gets or sets the transaction's project id.
- `public double Quantity { get; set; }` — Gets or sets the transaction quantity.
- `public override string Reference { get; set; }` — Gets or sets the transaction's reference.
- `public override string Reference2 { get; set; }` — Gets or sets the transaction's 2nd reference.
- `public SalesRepresentative Representative { get; set; }` — Gets or sets the sales representative
- `public int RepresentativeID { get; set; }` — Gets or sets the sales representative ID.
- `public SerialNumberCollection SerialNumbers { get; internal set; }` — Gets the transaction's serial number collection.
- `public double StockingUnitQuantity { get; set; }` — Gets or sets the transaction quantity.
- `public override double Tax { get; set; }` — Gets or sets the transaction tax amount (automatically rounded to 2 decimals and always posted positive).
- `public override TaxRate TaxRate { get; set; }` — Gets or sets the transaction's tax type.
- `public override int TaxRateID { get; set; }` — Gets or sets the transaction's tax type id.
- `public override TransactionCodeBase TransactionCode { get; set; }` — Gets or sets the transaction code .
- `public override int TransactionCodeID { get; set; }` — Gets or sets the transaction code id.
- `public Unit Unit { get; set; }` — Gets or sets the inventory unit om measure to use on this transaction. Note that this is not kept in the database, on recalling a transaction, this will always be null.
- `public double UnitCost { get; set; }` — Gets or sets the transaction's unit cost.
- `public int UnitID { get; set; }`
- `public Warehouse Warehouse { get; set; }` — Gets or sets the transaction's warehouse.
- `public WarehouseContext WarehouseContext { get; set; }`
- `public int WarehouseID { get; set; }` — Gets or sets the transaction's warehouse id.

## Methods (9)
- `protected void beforePost()`
- `public Object Clone()`
  - returns: Type: Object
- `public static long Find( string criteria )` — Finds a transaction ID.
  - param `criteria` (System.String) — The criteria passed to the SQL query. Eg. Reference = 'INV001' or Description like '%Invoice%'
  - returns: Type: Int64
- `public static DataTable List( string criteria )` — Returns a System.Data.DataTable object containing the database records from the PostST table matching the supplied criteria.
  - param `criteria` (System.String) — The SQL criteria used to locate the record, e.g. Reference like '1___' and Audit_No = 10.0005
  - returns: Type: DataTable A System.Data.DataTable object containing matching records.
  - remarks: The criteria is passed to an SQL query so use the appropriate syntax. Remember to includethe single quotes around string literals and append additional criteria with and.
- `protected internal override bool OnAllowBlockedPosting()`
  - returns: Type: Boolean
- `protected override bool OnPost()`
  - returns: Type: Boolean
- `protected bool onPostingGLCostVarianceCredit( GLTransaction tran )`
  - param `tran` (Pastel.Evolution.GLTransaction)
  - returns: Type: Boolean Returns a value indicating whether the transaction has been handled already
- `protected bool onPostingGLCostVarianceDebit( GLTransaction tran )`
  - param `tran` (Pastel.Evolution.GLTransaction)
  - returns: Type: Boolean Returns a value indicating whether the transaction has been handled already
- `public override bool Validate()` — Validates the transaction.
  - returns: Type: Boolean

## Events (3)
- `public event EventHandler BeforePost`
- `public event TransactionBase.GLPostingEventHandler GLCostVarianceCreditPosting`
- `public event TransactionBase.GLPostingEventHandler GLCostVarianceDebitPosting`

# JobCard (Class)

Represents an Evolution job card.

**Namespace:** Pastel.Evolution

```csharp
public class JobCard : AccountBase
```

## Constructors (3)
- `public JobCard()` — Initializes a new instance of the JobCard class
- `public JobCard( int id )` — Initializes a new instance of the JobCard class
- `public JobCard( string jobCode )` — Initializes a new instance of the JobCard class

## Properties (31)
- `public Customer Account { get; set; }`
- `public override bool Active { get; set; }`
- `public string Audit { get; }` — Gets the audit number of the last transaction processed by this document. This value defaults to 0, and will not be available on recalled documents.
- `public DateTime ClosingDate { get; set; }`
- `public override string Code { get; set; }`
- `public DateTime CompletionDate { get; set; }`
- `public Address DeliverTo { get; set; }`
- `public DateTime DeliveryDate { get; set; }`
- `public override string Description { get; set; }`
- `public JobDetailCollection Detail { get; }` — Gets the job detail collection to which detail lines can be added and from which lines can be deleted
- `public string ExtOrderNo { get; set; }`
- `public bool FinalInvoice { get; set; }`
- `public override int ID { get; }` — Gets the internal record ID (0 for new, unsaved records).
- `public Address InvoiceTo { get; set; }`
- `public override long LongID { get; }`
- `public override Module Module { get; }`
- `public string Narration { get; set; }`
- `public GLAccount OverrideCOSGLAccount { get; set; }` — Gets or sets the Job Card override COS GL Account.
- `public GLAccount OverrideRecoveryGLAccount { get; set; }` — Gets or sets the Job Card override Recovery GL Account.
- `public GLAccount OverrideSalesGLAccount { get; set; }` — Gets or sets the Job Card override Sales GL Account.
- `public GLAccount OverrideWIPGLAccount { get; set; }` — Gets or sets the Job Card override WIP GL Account.
- `public JobPostingMethod PostingMethod { get; set; }`
- `public Project Project { get; set; }`
- `public int ProjectID { get; set; }`
- `public double QuoteAmount { get; set; }` — Gets or sets the Job Card Quote Amount.
- `[ObsoleteAttribute("Use UserFields instead.")] public FieldCollection RawFieldData { get; }`
- `public SalesRepresentative SalesRepresentative { get; set; }`
- `public int SalesRepresentativeID { get; set; }`
- `public DateTime Started { get; set; }`
- `public JobCard.JobStatus Status { get; set; }`
- `public FieldCollection UserFields { get; }`

## Methods (9)
- `public static DataTable _ListCurrentBranch( string criteria )`
  - param `criteria` (System.String)
  - returns: Type: DataTable
- `public static DataTable _ListCurrentBranch( int accountID, JobCard.JobStatus status )`
  - param `accountID` (System.Int32)
  - param `status` (Pastel.Evolution.JobCard.JobStatus)
  - returns: Type: DataTable
- `protected internal void cascadeProject()`
- `protected internal void cascadeSalesReps()`
- `public static int Find( string criteria )`
  - param `criteria` (System.String)
  - returns: Type: Int32
- `public static int FindByCode( string code )` — Attempts to find an inventory item by its code and returns its ID.
  - param `code` (System.String) — The code used to lookup the account.
  - returns: Type: Int32 -1 if no record was found, else the id of the first account matching the criteria supplied.
- `protected internal bool hasPostedLines()`
  - returns: Type: Boolean
- `public static DataTable List( string criteria )`
  - param `criteria` (System.String)
  - returns: Type: DataTable
- `public static DataTable List( int accountID, JobCard.JobStatus status )`
  - param `accountID` (System.Int32)
  - param `status` (Pastel.Evolution.JobCard.JobStatus)
  - returns: Type: DataTable
- `public static DataTable List( Customer account, JobCard.JobStatus status )`
  - param `account` (Pastel.Evolution.Customer)
  - param `status` (Pastel.Evolution.JobCard.JobStatus)
  - returns: Type: DataTable
- `protected internal override void OnDelete()` — Removes the record from the database, provided it is not referenced by other records.
- `protected internal override void OnSave()` — Persists the record to the database.

## Fields (3)
- `protected Address deliverTo`
- `protected JobDetailCollection detail`
- `protected Address invoiceTo`

# JobDetail (Class)

Represents a job transaction.

**Namespace:** Pastel.Evolution

```csharp
public class JobDetail
```

## Constructors (3)
- `public JobDetail()` — Initializes a new instance of the JobDetail class
- `public JobDetail( int id )` — Initializes a new instance of the JobDetail class
- `public JobDetail( long id )` — Initializes a new instance of the JobDetail class

## Properties (52)
- `public AccountBase Account { get; set; }`
- `public double BudgetPurchasesTotalTax { get; }` — Gets the calculated line total.
- `public double BudgetSalesTotalExcl { get; }` — Gets the calculated line total
- `public double BudgetSalesTotalIncl { get; }` — Gets the calculated line total
- `public double BudgetSalesTotalTax { get; }` — Gets the calculated line total.
- `public double BudgetTotalCost { get; }`
- `public double BudgetUnitCostPrice { get; set; }`
- `public double BudgetUnitSellingPrice { get; set; }`
- `public string Description { get; set; }`
- `public double Discount { get; set; }` — Gets or sets the total line discount value (applies to tax excl. value)
- `public double DiscountPercent { get; set; }` — Gets or sets the line discount percentage: 5% = 5, as opposed to 0.05
- `public DateTime EndDate { get; set; }`
- `public int ID { get; }` — Gets the internal record ID (0 for new, unsaved records).
- `public int Index { get; internal set; }` — Gets the line number (1-based)
- `public InventoryItem InventoryItem { get; set; }` — Gets or sets the line's inventory item. Maps directly to the Account property but null if invalid.
- `public int InventoryItemID { get; set; }` — Gets or sets the stock item id.
- `public JobDetail.TransactionKind Kind { get; }`
- `public long LongID { get; }` — Transitional accessor.
- `public Lot Lot { get; set; }`
- `public int LotID { get; set; }`
- `public Project Project { get; set; }`
- `public int ProjectID { get; set; }`
- `public TaxRate PurchasesTaxRate { get; set; }`
- `public double PurchasesTotalTax { get; }` — Gets the calculated line total tax.
- `public double Quantity { get; set; }`
- `public double QuantityWIP { get; private set; }` — Gets the work in progress quantity held by given detail record. This value gets increased when saving a new active inventory line and decreased by adding negative lines (-Quantity).
- `public string Reference { get; set; }`
- `public SalesRepresentative SalesRepresentative { get; set; }`
- `public int SalesRepresentativeID { get; set; }`
- `public TaxRate SalesTaxRate { get; set; }` — Sales tax type
- `public double SalesTotalExcl { get; }` — Gets the calculated line total
- `public double SalesTotalIncl { get; }` — Gets the calculated line total
- `public double SalesTotalTax { get; }` — Gets the calculated line total
- `public SerialNumberCollection SerialNumbers { get; }`
- `public JobDetail.TransactionSource Source { get; internal set; }` — Gets the transaction source, decided by the Account.
- `public DateTime StartDate { get; set; }`
- `public JobCard.JobStatus Status { get; set; }`
- `public double StockingUnitQuantity { get; set; }`
- `public double StockingUnitQuantityWIP { get; private set; }`
- `public double TotalCost { get; }`
- `public JobTransactionCode TransactionCode { get; set; }` — Gets or sets the job costing transaction type associate with the detail record. When setting the transaction type, the cost and sales tax types will default to those set on the transaction type.
- `public Unit Unit { get; set; }`
- `public double UnitCostPrice { get; set; }` — Gets or sets the tax exclusive unit cost price. For new records, setting this value will also set BudgetUnitCostPrice .
- `public int UnitID { get; set; }`
- `public double UnitSellingPrice { get; set; }` — Gets or sets the tax exclusive unit selling price. For new records, setting this value will also set BudgetUnitSellingPrice .
- `public FieldCollection UserFields { get; }`
- `public Warehouse Warehouse { get; set; }` — Gets or sets the warehouse relevant to this detail record. Set the warehouse only after setting the inventory item. The Warehouse and WarehouseContext properties are mapped to one another.
- `public WarehouseContext WarehouseContext { get; set; }` — Gets or sets the warehouse link of the stock item specified.
- `[ObsoleteAttribute("Use WarehouseContext instead.")] public WarehouseContext WarehouseData { get; set; }`
- `public int WarehouseID { get; }` — Gets the ID of the assigned warehouse (0 if N/A).
- `public Worker Worker { get; set; }` — Gets or sets the line's worker. Maps directly to the Account property but null if invalid.
- `public int WorkerID { get; set; }` — Gets or sets the worker id.

## Methods (2)
- `public static long Find( string criteria )`
  - param `criteria` (System.String)
  - returns: Type: Int64
- `public static DataTable List( string criteria )`
  - param `criteria` (System.String)
  - returns: Type: DataTable

# JobDetailCollection (Class)

**Namespace:** Pastel.Evolution

```csharp
public class JobDetailCollection : CollectionBase
```

## Properties (1)
- `public JobDetail this[ int index ] { get; set; }`

## Methods (4)
- `public void Add( JobDetail detailRecord )`
  - param `detailRecord` (Pastel.Evolution.JobDetail)
- `public void OnCollectionChanged( JobDetailCollection.JobDetailCollectionChangedEventArgs e )`
  - param `e` (Pastel.Evolution.JobDetailCollection.JobDetailCollectionChangedEventArgs)
- `public void Remove( JobDetail detailRecord )`
  - param `detailRecord` (Pastel.Evolution.JobDetail)
- `public void RemoveAt( int index )`
  - param `index` (System.Int32)

## Events (1)
- `public event JobDetailCollection.JobDetailChangedEventHandler CollectionChanged` — Occurs when detail records are added or deleted.

# JobDetailCollection.JobDetailChangedEventHandler (Delegate)

**Namespace:** Pastel.Evolution

```csharp
public delegate void JobDetailChangedEventHandler(
    Object sender,
    JobDetailCollection.JobDetailCollectionChangedEventArgs e
    )
```

# JobDetailCollection.JobDetailCollectionChangedEventArgs (Class)

**Namespace:** Pastel.Evolution

```csharp
public class JobDetailCollectionChangedEventArgs : EventArgs
```

## Fields (2)
- `public JobDetailCollection.JobDetailChangeAction Action`
- `public JobDetail DetailRecord`

# JobPostingMethodGLContext (Class)

**Namespace:** Pastel.Evolution

```csharp
public class JobPostingMethodGLContext
```

## Properties (8)
- `public GLAccount CostOfSalesGLAccount { get; }` — Gets the job card posting method's cost of sales general ledger account.
- `public GLAccount CustomerControlGLAccount { get; }` — Gets the job card posting method's customer control general ledger account.
- `public GLAccount RecoveryGLAccount { get; }` — Gets the job card posting method's recovery general ledger account.
- `public GLAccount SalesGLAccount { get; }` — Gets the job card posting method's sales general ledger account.
- `public GLAccount StockGLAccount { get; }` — Gets the job card posting method's stock general ledger account.
- `public GLAccount SupplierControlGLAccount { get; }` — Gets the job card posting method's supplier control general ledger account.
- `public GLAccount TaxGLAccount { get; }` — Gets the job card posting method's tax general ledger account.
- `public GLAccount WipGLAccount { get; }` — Gets the job card posting method's work in progress general ledger account.

# JobPostingMethodGLContextCollection (Class)

**Namespace:** Pastel.Evolution

```csharp
public class JobPostingMethodGLContextCollection : CollectionBase
```

## Properties (1)
- `public JobPostingMethodGLContext this[ JobPostingMethod jobPostingMethod ] { get; }` — Gets the job card posting method context object for the posting method supplied.

# JobTransactionCode (Class)

Represents a job costing transaction code.

**Namespace:** Pastel.Evolution

```csharp
public class JobTransactionCode : TransactionCodeBase
```

## Constructors (3)
- `public JobTransactionCode()` — Initializes a new instance of the JobTransactionCode class
- `public JobTransactionCode( int id )` — Initializes a new instance of the JobTransactionCode class
- `public JobTransactionCode( JobDetail.TransactionSource source, string code )` — Initializes a new instance of the JobTransactionCode class

## Properties (21)
- `public GLAccount APControlAccount { get; set; }`
- `public int APControlAccountID { get; set; }`
- `public GLAccount ARControlAccount { get; set; }`
- `public int ARControlAccountID { get; set; }`
- `public override string Code { get; set; }`
- `public GLAccount CosAccount { get; set; }`
- `public TaxRate CostingTaxType { get; set; }`
- `public int CostingTaxTypeID { get; set; }`
- `public override string Description { get; set; }`
- `public TransactionTypePostingMethodGLContextCollection GLAccounts { get; }`
- `public override int ID { get; }` — Gets the internal record ID (0 for new, unsaved records).
- `public override long LongID { get; }`
- `public GLAccount RecoveryAccount { get; set; }`
- `public int SalesTaxTypeID { get; set; }`
- `public TaxRate SellingTaxType { get; set; }`
- `public JobDetail.TransactionSource Source { get; set; }`
- `public GLAccount StockAccount { get; set; }`
- `public int StockAccountID { get; set; }`
- `public GLAccount TaxAccount { get; set; }`
- `public GLAccount WIPAccount { get; set; }`
- `public int WIPAccountID { get; set; }`

## Methods (7)
- `public static int Find( string criteria )`
  - param `criteria` (System.String)
  - returns: Type: Int32
- `public static int FindByCode( string code )` — Attempts to find a record by its code and returns its ID.
  - param `code` (System.String) — The code used to lookup the record.
  - returns: Type: Int32 -1 if no record was found, else the id of the first record matching the criteria supplied.
- `public static int FindByCode( JobDetail.TransactionSource source, string code )` — Attempts to find a record by its code and returns its ID.
  - param `source` (Pastel.Evolution.JobDetail.TransactionSource) — The transaction source by which to filter the transaction listing.
  - param `code` (System.String) — The code used to lookup the record.
  - returns: Type: Int32 -1 if no record was found, else the id of the first record matching the criteria supplied.
- `public static JobTransactionCode Get( string criteria )` — Returns the [first] inventory item object with the criteria specified; otherwise, returns null .
  - param `criteria` (System.String) — Eg. Code = 'STO0021' or Description like '%Stone%'
  - returns: Type: JobTransactionCode
- `public static JobTransactionCode GetByCode( JobDetail.TransactionSource source, string code )` — Returns a transaction type object corresponding to the code and transaction source specified; otherwise, returns null .
  - param `source` (Pastel.Evolution.JobDetail.TransactionSource) — The transaction source by which to limit code search.
  - param `code` (System.String) — The transaction code.
  - returns: Type: JobTransactionCode
- `public static DataTable List( string criteria )`
  - param `criteria` (System.String)
  - returns: Type: DataTable
- `protected internal override void OnDelete()` — Removes the record from the database, provided it is not referenced by other records.
- `protected internal override void OnSave()` — Persists the record to the database.

# JournalBatch (Class)

**Namespace:** Pastel.Evolution

```csharp
public class JournalBatch : BranchedRecordBase
```

## Constructors (3)
- `public JournalBatch()` — Creates a new instance of a general ledger journal batch.
- `public JournalBatch( int id )` — Creates a new instance of a general ledger journal batch.
- `public JournalBatch( string code )` — Creates a new instance of a general ledger journal batch.

## Properties (14)
- `public string Code { get; set; }`
- `public string DefaultDescription { get; set; }`
- `public string Description { get; set; }`
- `public JournalBatchDetailCollection Detail { get; }`
- `public bool DoClearAfterPost { get; set; }`
- `public override int ID { get; }`
- `public override long LongID { get; }`
- `public Agent Owner { get; set; }` — Gets or sets the batch owner.
- `public int OwnerID { get; set; }` — Gets or sets the Agent ID of the batch owner.
- `public int ProcessedCount { get; }`
- `public string Reference { get; internal set; }`
- `public int RepeatLimit { get; set; }`
- `public TransactionCode TransactionCode { get; set; }`
- `public int TransactionCodeID { get; set; }`

## Methods (5)
- `public static int Find( string criteria )`
  - param `criteria` (System.String)
  - returns: Type: Int32
- `public static int FindByCode( string code )`
  - param `code` (System.String)
  - returns: Type: Int32
- `public static DataTable List( string criteria )`
  - param `criteria` (System.String)
  - returns: Type: DataTable
- `public static DataTable List( string criteria, string sortOrder )`
  - param `criteria` (System.String)
  - param `sortOrder` (System.String)
  - returns: Type: DataTable
- `protected internal override void OnDelete()`
- `protected internal override void OnSave()` — Persists the record to the database.

# JournalBatchDetail (Class)

**Namespace:** Pastel.Evolution

```csharp
public class JournalBatchDetail : BranchedRecordBase
```

## Constructors (2)
- `public JournalBatchDetail()` — Creates a new instance of a journal batch detail record.
- `public JournalBatchDetail( int id )` — Creates a new instance of a journal batch detail record.

## Properties (19)
- `public GLAccount Account { get; set; }` — Gets or sets the Account.
- `public int AccountID { get; set; }` — Gets or sets the Account ID.
- `public double Credit { get; set; }`
- `public DateTime Date { get; set; }`
- `public double Debit { get; set; }` — Sets the transaction debit amount.
- `public string Description { get; set; }` — Gets or sets the record description.
- `public double EffectiveCredit { get; set; }`
- `public double EffectiveDebit { get; set; }`
- `public int GLAccountID { get; set; }` — Gets or sets the GLAccount ID.
- `public override int ID { get; }`
- `public bool IsLoading { get; set; }`
- `public override long LongID { get; }`
- `public Project Project { get; set; }` — Gets or sets the Project.
- `public int ProjectID { get; set; }` — Gets or sets the Project ID.
- `public string Reference { get; set; }`
- `public double Tax { get; set; }` — Gets or sets the transaction tax amount (automatically rounded to 2 decimals and always posted positive).
- `public GLAccount TaxAccount { get; set; }` — Gets or sets the tax account.
- `public TaxRate TaxRate { get; set; }` — Gets or sets the TaxRate.
- `public int TaxRateID { get; set; }` — Gets or sets the TaxRate ID.

## Methods (5)
- `public JournalBatchDetail Clone()`
  - returns: Type: JournalBatchDetail
- `public static int Find( string criteria )`
  - param `criteria` (System.String)
  - returns: Type: Int32
- `public static DataTable List( string criteria )`
  - param `criteria` (System.String)
  - returns: Type: DataTable
- `protected internal override void OnDelete()`
- `protected internal override void OnSave()` — Persists the record to the database.

# JournalBatchDetailCollection (Class)

Represents a collection of batch detail items, typically owned by a given inventory document record.

**Namespace:** Pastel.Evolution

```csharp
public class JournalBatchDetailCollection : CollectionBase
```

## Properties (1)
- `public JournalBatchDetail this[ int index ] { get; set; }` — Gets a batch detail object by its zero-based index.

## Methods (4)
- `public void Add( JournalBatchDetail detailRecord )` — Appends a batch detail object to the batch.
  - param `detailRecord` (Pastel.Evolution.JournalBatchDetail)
  - remarks: Take note that upon being added to a document, the detail record will assume the document's sales representative and project.
- `public void OnCollectionChanged( JournalBatchDetailCollection.JournalBatchDetailCollectionChangedEventArgs e )`
  - param `e` (Pastel.Evolution.JournalBatchDetailCollection.JournalBatchDetailCollectionChangedEventArgs)
- `public void Remove( JournalBatchDetail detailRecord )` — Removes the specified order detail line from the collection
  - param `detailRecord` (Pastel.Evolution.JournalBatchDetail)
- `public void RemoveAt( int index )` — Removes a detail record using its zero-based index.
  - param `index` (System.Int32)

## Events (1)
- `public event JournalBatchDetailCollection.JournalBatchDetailChangedEventHandler CollectionChanged` — Occurs when detail records are added or deleted.

# JournalBatchDetailCollection.JournalBatchDetailChangedEventHandler (Delegate)

**Namespace:** Pastel.Evolution

```csharp
public delegate void JournalBatchDetailChangedEventHandler(
    Object sender,
    JournalBatchDetailCollection.JournalBatchDetailCollectionChangedEventArgs e
    )
```

# JournalBatchDetailCollection.JournalBatchDetailCollectionChangedEventArgs (Class)

**Namespace:** Pastel.Evolution

```csharp
public class JournalBatchDetailCollectionChangedEventArgs : EventArgs
```

## Fields (2)
- `public JournalBatchDetailCollection.JournalBatchDetailChangeAction Action`
- `public JournalBatchDetail DetailRecord`

# Lot (Class)

Represents a distinct inventory lot.

**Namespace:** Pastel.Evolution

```csharp
public class Lot : BranchedRecordBase
```

## Constructors (5)
- `public Lot()` — Initializes a new instance of the Lot class
- `public Lot( int id )` — Initializes a new instance of the Lot class
- `public Lot( string code )` — Initializes a new instance of the Lot class
- `public Lot( string code, InventoryItem stockItem )` — Initializes a new instance of the Lot class
- `public Lot( string code, int stockID )` — Initializes a new instance of the Lot class

## Properties (14)
- `public string Code { get; set; }`
- `public DateTime ExpiryDate { get; set; }` — Gets or sets the lot's expiry date. If not set, DateTime.MaxValue is returned. Set to Defaults.NullDate to cancel.
- `public override int ID { get; }`
- `public InventoryItem InventoryItem { get; set; }`
- `public int InventoryItemID { get; set; }`
- `public bool IsDirty { get; }`
- `public override long LongID { get; }`
- `public double QtyFree { get; }` — Gets the lot's free quantity.
- `public double QtyOnHand { get; }`
- `public double QtyReserved { get; }`
- `public double QtyWIP { get; }` — Gets the quantity of stock on active jobs and in manufacturing (work in progress).
- `public LotStatus Status { get; set; }` — Gets or sets the lot's status. Note that new lots will always default to the receiving lot configured on the item.
- `public int StatusID { get; set; }`
- `public LotContext.LotContextCollection WarehouseContexts { get; }` — Gets the Lot's warehouse context collection. Bear in mind that unless has actually been used in a given warehouse, there will be no warehouse context for it and null will be returned.

## Methods (8)
- `public void _Refresh()` — Experimental method.
- `public static Lot[] _Select( string criteria )` — Experimental Method
  - param `criteria` (System.String)
  - returns: Type: Lot []
- `public static Lot[] _Select( int itemID, string sortOrder )` — Experimental Method
  - param `itemID` (System.Int32)
  - param `sortOrder` (System.String)
  - returns: Type: Lot []
- `public static Lot[] _Select( string criteria, string sortOrder )` — Experimental Method
  - param `criteria` (System.String)
  - param `sortOrder` (System.String)
  - returns: Type: Lot []
- `public static Lot[] _Select( InventoryItem item, string sortOrder )` — Experimental Method
  - param `item` (Pastel.Evolution.InventoryItem)
  - param `sortOrder` (System.String)
  - returns: Type: Lot []
- `public static int Find( string criteria )` — Finds the first record matching the criteria supplied
  - param `criteria` (System.String) — E.g. Code = 'abc'
  - returns: Type: Int32 The id of the record
- `public static int Find( int inventoryID, string code )` — Finds the first record matching the criteria supplied
  - param `inventoryID` (System.Int32)
  - param `code` (System.String)
  - returns: Type: Int32
- `public static DataTable List( string criteria )` — Returns a datatable containing the matching rows.
  - param `criteria` (System.String)
  - returns: Type: DataTable
- `public static DataTable List( InventoryItem item )` — Returns a datatable containing the matching rows.
  - param `item` (Pastel.Evolution.InventoryItem)
  - returns: Type: DataTable
- `public static DataTable List( string criteria, string sortOrder )` — Returns a datatable containing the matching rows.
  - param `criteria` (System.String) — e.g. SNStockLink = 100 and CurrentLoc = (int)SerialNumberLocation.InStock
  - param `sortOrder` (System.String) — The SQL order by clause.
  - returns: Type: DataTable
- `public static DataTable List( InventoryItem item, LotStatus status )` — Returns a datatable containing the matching rows.
  - param `item` (Pastel.Evolution.InventoryItem) — The inventory item to which the serial numbers belong.
  - param `status` (Pastel.Evolution.LotStatus) — The current status of the lot on which to filter.
  - returns: Type: DataTable
- `protected internal override void OnDelete()`
- `protected internal override void OnSave()`
- `public void Save( string statusTransferRef, DateTime statusTransferDate )` — Saves modifications to the lot record, notably the status and expiry date, if applicable. When changing a lot's status, a transaction gets posted. The supplied parameters are used in that transaction.
  - param `statusTransferRef` (System.String) — The reference to post to the lot status transfer. Defaults to an empty string.
  - param `statusTransferDate` (System.DateTime) — The date at which to post the lot status transfer. Defaults to the current date (date at which the lot is instantiated).
- `public override string ToString()`
  - returns: Type: String

# LotContext (Class)

Represents a distinct inventory lot.

**Namespace:** Pastel.Evolution

```csharp
public class LotContext
```

## Properties (12)
- `public int ID { get; }`
- `public Lot Lot { get; }`
- `public double QtyAdjustedIn { get; }`
- `public double QtyAdjustedOut { get; }`
- `public double QtyFree { get; }` — Gets the lot's free quantity.
- `public double QtyNetPurchased { get; }` — Net quantity purchased: purchased - returned
- `public double QtyNetSold { get; }` — Net quantity sold: sold - credited
- `public double QtyOnHand { get; }`
- `public double QtyReserved { get; }`
- `public double QtyWIP { get; }` — Gets the quantity of stock on active jobs and in manufacturing (work in progress).
- `public Warehouse Warehouse { get; }`
- `public int WarehouseID { get; }`

# LotContext.LotContextCollection (Class)

**Namespace:** Pastel.Evolution

```csharp
public class LotContextCollection : CollectionBase
```

## Properties (1)
- `Item` — Gets a lot context by warehouse ID, not by index.

# LotStatus (Class)

Represents a lot status indicator.

**Namespace:** Pastel.Evolution

```csharp
public class LotStatus : BranchedRecordBase
```

## Constructors (3)
- `public LotStatus()` — Initializes a new instance of the LotStatus class
- `public LotStatus( int id )` — Initializes a new instance of the LotStatus class
- `public LotStatus( string description )` — Initializes a new instance of the LotStatus class

## Properties (5)
- `public bool AllowPurchases { get; set; }`
- `public bool AllowSales { get; set; }`
- `public string Description { get; set; }`
- `public override int ID { get; }`
- `public override long LongID { get; }`

## Methods (6)
- `public static int Find( string criteria )` — Finds the first record matching the criteria supplied
  - param `criteria` (System.String) — E.g. Code = 'abc'
  - returns: Type: Int32 The id of the record
- `public static int FindByDescription( string description )`
  - param `description` (System.String)
  - returns: Type: Int32
- `public static DataTable List( string criteria )` — Returns a datatable containing the matching rows.
  - param `criteria` (System.String) — e.g. SNStockLink = 100 and CurrentLoc = (int)SerialNumberLocation.InStock
  - returns: Type: DataTable
- `protected internal override void OnDelete()`
- `protected internal override void OnSave()`
- `public override string ToString()`
  - returns: Type: String

# NatureOfTransaction (Class)

Represents an EU Nature of Transaction code.

**Namespace:** Pastel.Evolution

```csharp
public class NatureOfTransaction : BranchedRecordBase
```

## Constructors (3)
- `public NatureOfTransaction()` — Creates a new nature of transaction code.
- `public NatureOfTransaction( int id )` — Creates a new instance of a nature of transaction code.
- `public NatureOfTransaction( string code )` — Creates a new instance of a nature of transaction code.

## Properties (4)
- `public string Code { get; set; }` — Gets or sets the nature of transaction code.
- `public string Description { get; set; }` — Gets or sets the project description.
- `public override int ID { get; }` — Gets the internal record ID (0 for new, unsaved records).
- `public override long LongID { get; }`

## Methods (7)
- `public static int Find( string criteria )` — Finds a project account ID.
  - param `criteria` (System.String) — The criteria passed to the SQL query. Eg. ProjectCode = 'INT001' or ProjectName like '%Internal%'
  - returns: Type: Int32 The ID of the first record found; -1 if not record was found.
- `public static int FindByCode( string code )` — Attempts to find a project by its code and returns its ID.
  - param `code` (System.String) — The code used to lookup the project.
  - returns: Type: Int32 -1 if no record was found, else the id of the first account matching the criteria supplied.
- `public static Project Get( string criteria )` — Returns an instance of the first record satisfying the criteria specified; otherwise, returns null.
  - param `criteria` (System.String) — The criteria passed to the SQL query. Eg. ProjectCode = 'INT001' or ProjectName like '%Internal%'
  - returns: Type: Project The record found; otherwise null
- `public static Project GetByCode( string code )` — Returns an instance of the first record with the code specified; otherwise, returns null.
  - param `code` (System.String) — Specifies the code.
  - returns: Type: Project The record found; otherwise null
- `public DataTable List( string criteria )` — Gets a list of database records.
  - param `criteria` (System.String) — Specifies the criteria as a SQL where clause.
  - returns: Type: DataTable Table containing selected records.
- `protected internal override void OnDelete()` — Removes the record from the database, provided it is not referenced by other records.
- `protected internal override void OnSave()` — Persists the record to the database.

# Opportunity (Class)

Represents a Contact Management sales opportunity.

**Namespace:** Pastel.Evolution

```csharp
public class Opportunity : BranchedRecordBase
```

## Constructors (2)
- `public Opportunity()` — Creates a new instance of an opportunity.
- `public Opportunity( int id )` — Creates a new instance of an opportunity.

## Properties (19)
- `public BranchedRecordBase Account { get; set; }`
- `public Agent AccountManager { get; set; }`
- `public SalesOrderQuotation ActiveQuote { get; set; }`
- `public int ActiveQuoteID { get; set; }`
- `public string Description { get; set; }`
- `public override int ID { get; }` — Gets the internal record ID (0 for new, unsaved records).
- `public bool IsPublic { get; set; }` — Gets or sets whether or not the prospect is visible to agents other than the assigned agent.
- `public override long LongID { get; }`
- `public Module Module { get; }`
- `public Person Person { get; set; }` — Gets or sets the person record related to the opportunity.
- `public int PersonID { get; }`
- `public double Probability { get; set; }`
- `public Project Project { get; set; }`
- `public string Reference { get; set; }`
- `public OpportunityStage Stage { get; set; }`
- `public int StageID { get; set; }`
- `public OpportunityState State { get; set; }` — Gets the opportunity's status. WARNING: this may be renamed to status in future.
- `public int StateID { get; set; }`
- `public FieldCollection UserFields { get; }`

## Methods (6)
- `public static DataTable _ListCurrentBranch( string criteria )`
  - param `criteria` (System.String)
  - returns: Type: DataTable
- `public static int Find( string criteria )`
  - param `criteria` (System.String)
  - returns: Type: Int32
- `public static int FindByCode( string reference )`
  - param `reference` (System.String)
  - returns: Type: Int32
- `public static DataTable List( string criteria )`
  - param `criteria` (System.String)
  - returns: Type: DataTable
- `protected internal override void OnDelete()` — Removes the record from the database, provided it is not referenced by other records.
- `protected internal override void OnSave()` — Persists the record to the database.

# OpportunityStage (Class)

Represents a Contact Management sales opportunity stage.

**Namespace:** Pastel.Evolution

```csharp
public class OpportunityStage : BranchedRecordBase
```

## Constructors (2)
- `public OpportunityStage()` — Creates a new instance of an opportunity.
- `public OpportunityStage( int id )` — Creates a new instance of a prospect.

## Properties (5)
- `public string Description { get; set; }`
- `public override int ID { get; }` — Gets the internal record ID (0 for new, unsaved records).
- `public override long LongID { get; }`
- `public Module Module { get; }`
- `public string Name { get; set; }`

## Methods (7)
- `public static DataTable _ListCurrentBranch( string criteria )`
  - param `criteria` (System.String)
  - returns: Type: DataTable
- `public static int Find( string criteria )`
  - param `criteria` (System.String)
  - returns: Type: Int32
- `public static int FindByName( string name )`
  - param `name` (System.String)
  - returns: Type: Int32
- `public static OpportunityStage GetByName( string name )`
  - param `name` (System.String)
  - returns: Type: OpportunityStage
- `public static DataTable List( string criteria )`
  - param `criteria` (System.String)
  - returns: Type: DataTable
- `protected internal override void OnDelete()` — Removes the record from the database, provided it is not referenced by other records.
- `protected internal override void OnSave()` — Persists the record to the database.

# OpportunityState (Class)

Represents a Contact Management opportunity status.

**Namespace:** Pastel.Evolution

```csharp
public class OpportunityState : BranchedRecordBase
```

## Constructors (2)
- `public OpportunityState()` — Creates a new instance of an opportunity.
- `public OpportunityState( int id )` — Creates a new instance of a prospect.

## Properties (4)
- `public override int ID { get; }` — Gets the internal record ID (0 for new, unsaved records).
- `public bool IsFinal { get; set; }` — Gets or sets whether or not this state terminates an opportunity.
- `public override long LongID { get; }`
- `public string Name { get; set; }`

## Methods (4)
- `public static int Find( string criteria )`
  - param `criteria` (System.String)
  - returns: Type: Int32
- `public static DataTable List( string criteria )`
  - param `criteria` (System.String)
  - returns: Type: DataTable
- `protected internal override void OnDelete()` — Removes the record from the database, provided it is not referenced by other records.
- `protected internal override void OnSave()` — Persists the record to the database.

# OrderBase (Class)

Includes functionality that is common to all inventory documents. Must be inherited.

**Namespace:** Pastel.Evolution

```csharp
public abstract class OrderBase : BranchedRecordBase
```

## Constructors (4)
- `protected internal OrderBase()` — Initializes a new instance of the OrderBase class
- `protected internal OrderBase( int id )` — Initializes a new instance of the OrderBase class
- `protected internal OrderBase( string orderNumber, DocumentType documentType )` — Initializes a new instance of the OrderBase class
- `protected internal OrderBase( string orderNumber, DocumentType documentType, string orderNumber2, int documentFlag )` — Initializes a new instance of the OrderBase class

## Properties (107)
- `public DrCrAccount Account { get; set; }` — Gets or sets the AR or AP account associated with the order.
- `public int AccountID { get; set; }` — Gets or sets the ID of the AR or AP account associated with the order.
- `public bool AllowInvoiceRounding { get; set; }`
- `public bool ApplyTaxPerLine { get; set; }` — Gets or sets whether tax per line should be applied.
- `public string Audit { get; }` — Gets the audit number of the last transaction processed by this document. This value defaults to 0, and will not be available on recalled documents.
- `public Currency Currency { get; internal set; }` — Gets or sets the currency.
- `public int CurrencyID { get; }` — Gets or sets the document's currency ID.
- `public static TaxMode DefaultTaxMode { get; }` — Gets the global default tax mode.
- `public Address DeliverTo { get; set; }` — Gets or sets the delivery address.
- `public DateTime DeliveryDate { get; set; }` — Gets or sets the delivery date.
- `public DeliveryMethod DeliveryMethod { get; set; }` — Gets or sets the delivery method.
- `public int DeliveryMethodID { get; set; }` — Gets or sets the delivery method ID.
- `public string Description { get; set; }` — Gets or sets the document description. This will also be the description on any transactions posted.
- `public OrderDetailCollection Detail { get; }` — Gets the order detail collection representing the body of the document.
- `public double Discount { get; set; }` — Gets or sets the document discount amount (applicable to tax excl. total),
- `public double DiscountForeign { get; set; }` — Gets or sets the document foreign discount amount (applicable to tax excl. total),
- `public double DiscountLastProcessed { get; }` — Gets the document discount amount last processed.
- `public double DiscountPercent { get; set; }` — Gets or sets the document discount percentage.
- `public double DiscountToProcess { get; }` — Gets the document discount amount about to be processed (applicable to tax excl. total).
- `public DateTime DueDate { get; set; }` — Gets or sets the due date.
- `public double ExchangeRate { get; set; }` — Gets or sets the exchange rate.
- `public string ExternalOrderNo { get; set; }` — Gets or sets the external order number.
- `protected double grossLastProcessTotal { get; }`
- `protected double grossLastProcessTotalForeign { get; }`
- `protected double grossOutstTotal { get; }`
- `protected double grossOutstTotalForeign { get; }`
- `protected double grossToProcessTotal { get; }`
- `protected double grossToProcessTotalForeign { get; }`
- `protected double grossTotal { get; }`
- `protected double grossTotalForeign { get; }`
- `public override int ID { get; }` — Gets the internal record ID (0 for new, unsaved records).
- `public DateTime InvoiceDate { get; set; }` — Gets or sets the invoice date.
- `public Address InvoiceTo { get; set; }` — Gets or sets the invoice address.
- `public bool IsLoading { get; internal set; }` — Will be true while the order is busy loading detail.
- `public virtual bool IsPartialProcessingAllowed { get; }`
- `public bool IsProcessing { get; internal set; }` — Will be true while the order is busy processing transactions.
- `public DrCrTransaction LedgerTransaction { get; }` — Gets the last ledger transaction (AR/AP Transaction) posted.
- `protected double lineAdditionalCostTotal { get; }`
- `public override long LongID { get; }`
- `public string MessageLine1 { get; set; }` — Gets or sets the 1st message line.
- `public string MessageLine2 { get; set; }` — Gets or sets the 2nd message line.
- `public string MessageLine3 { get; set; }` — Gets or sets the 3rd message line.
- `protected double nettLastProcessTotal { get; }`
- `protected double nettLastProcessTotalForeign { get; }`
- `protected double nettOutstTotal { get; }`
- `protected double nettOutstTotalForeign { get; }`
- `protected double nettToProcessTotal { get; }`
- `protected double nettToProcessTotalForeign { get; }`
- `public DateTime OrderDate { get; set; }` — Gets or sets the order date.
- `public string OrderNo { get; set; }` — Gets or sets the order number.
- `public Priority OrderPriority { get; set; }` — Gets or sets the order priority.
- `public int OrderPriorityID { get; set; }` — Gets or sets the order priority ID.
- `public OrderStatus OrderStatus { get; set; }` — Gets or sets the document's order status.
- `public int OrderStatusID { get; set; }` — Gets or sets the order status ID.
- `public abstract OrderBase OriginalDocument { get; }` — Gets the original document.
- `public int PrintCount { get; set; }` — Gets or sets the print count.
- `public Project Project { get; set; }` — Gets or sets the project.
- `public int ProjectID { get; set; }` — Gets or sets the project ID.
- `public Prospect Prospect { get; set; }`
- `public int ProspectID { get; set; }`
- `[ObsoleteAttribute("Use UserFields instead.")] public FieldCollection RawFieldData { get; }`
- `public string Reference { get; }` — Gets or sets the document reference (InvNumber).
- `public string Reference2 { get; }` — Gets the 2nd document reference.
- `public SettlementTerms SettlementTerms { get; set; }`
- `public int SettlementTermsID { get; set; }`
- `public DocumentState State { get; internal set; }` — Gets the document state.
- `protected double taxLastProcessTotal { get; }`
- `protected double taxLastProcessTotalForeign { get; }`
- `public TaxMode TaxMode { get; set; }` — Gets or sets the tax mode.
- `public string TaxNumber { get; set; }` — Gets or sets the cash account's tax number.
- `protected double taxOutstTotal { get; }`
- `protected double taxOutstTotalForeign { get; }`
- `protected double taxToProcessTotal { get; }`
- `protected double taxToProcessTotalForeign { get; }`
- `protected double taxTotal { get; }`
- `protected double taxTotalForeign { get; }`
- `public TaxRate TaxType { get; set; }`
- `public double TotalDiscountAdjusted { get; }` — Gets the total discount adjusted amount.
- `public double TotalDiscountAdjustedForeign { get; }` — Gets the total discount adjusted foreign amount.
- `public double TotalExcl { get; }` — Gets the total excl amount.
- `public double TotalExclForeign { get; }` — Gets the total excl amount.
- `public double TotalIncl { get; }` — Gets the total incl amount.
- `public double TotalInclForeign { get; }` — Gets the total incl amount.
- `public double TotalInclForeignBeforeInvoiceRounding { get; }` — Gets the total incl amount before Invoice Rounding.
- `public double TotalLastProcessExcl { get; }` — Gets the total last process excl.
- `public double TotalLastProcessExclForeign { get; }` — Gets the total last process excl.
- `public double TotalLastProcessIncl { get; }` — Gets the total last process incl.
- `public double TotalLastProcessInclForeign { get; }` — Gets the total last process incl.
- `public double TotalLastProcessTax { get; }` — Gets the total last process tax.
- `public double TotalLastProcessTaxForeign { get; }` — Gets the total last process tax.
- `public double TotalOutstandingExcl { get; }` — Gets the total outstanding excl.
- `public double TotalOutstandingExclForeign { get; }` — Gets the total outstanding excl.
- `public double TotalOutstandingIncl { get; }` — Gets the total outstanding incl.
- `public double TotalOutstandingInclForeign { get; }` — Gets the total outstanding incl.
- `public double TotalOutstandingTax { get; }` — Gets the total outstanding tax.
- `public double TotalOutstandingTaxForeign { get; }` — Gets the total outstanding tax.
- `public double TotalTax { get; }` — Gets the total tax amount.
- `public double TotalTaxForeign { get; }` — Gets the total tax amount.
- `public double TotalToProcessExcl { get; }` — Gets the total amount to process excl.
- `public double TotalToProcessExclForeign { get; }` — Gets the total amount to process excl.
- `public double TotalToProcessIncl { get; }` — Gets the total to process incl.
- `public double TotalToProcessInclForeign { get; }` — Gets the total to process incl.
- `public double TotalToProcessTax { get; }` — Gets the total to process tax.
- `public double TotalToProcessTaxForeign { get; }` — Gets the total to process tax.
- `public DocumentType Type { get; }` — Gets the order's document type.
- `public FieldCollection UserFields { get; }` — Gets access to the collection of user-defined fields on the record. Note that the field name is case-sensitive.
- `public int Version { get; }` — Gets the current version of the order, incremented on every save.

## Methods (21)
- `public void _SetFullQtyToProcess()`
- `protected virtual void BeforePostGLBatch( OrderBase orderBase, CancelEventArgs e )`
  - param `orderBase` (Pastel.Evolution.OrderBase)
  - param `e` (System.ComponentModel.CancelEventArgs)
- `protected virtual void BeforePostInventory( OrderBase orderBase, CancelEventArgs e )`
  - param `orderBase` (Pastel.Evolution.OrderBase)
  - param `e` (System.ComponentModel.CancelEventArgs)
- `protected virtual void BeforePostLedger( OrderBase orderBase, CancelEventArgs e )`
  - param `orderBase` (Pastel.Evolution.OrderBase)
  - param `e` (System.ComponentModel.CancelEventArgs)
- `protected internal virtual void BeforeSave()`
- `protected internal void cascadeForeignValues()`
- `protected internal void cascadeProject()`
- `protected internal void cascadeTaxRate()`
- `public string Complete()` — Processes (invoices) all outstanding quantities on the order. The entire invoice fails if one or more detail lines do not have sufficient stock available. The CompleteMax method (SalesOrder only) is a variation on this method and attempts to confirm as much of the ordered stock as is available.
  - returns: Type: String The generated reference number.
- `public string Complete( string reference )` — Process (invoice) all outstanding quantities on the order. The entire invoice fails if one or more detail lines do not have sufficient stock available. The method is a variation on this method and attempts to confirm as much of the ordered stock as is available.
  - param `reference` (System.String) — Specifies the transaction reference to use. No duplication checking is performed
  - returns: Type: String The supplied reference number.
- `protected virtual void Detach()`
- `protected bool detailRemainsOutstanding()`
  - returns: Type: Boolean
- `protected bool detailToProcess()`
  - returns: Type: Boolean
- `public static int Find( string criteria )` — Finds a record's database ID.
  - param `criteria` (System.String) — Specifies the criteria as a SQL where clause.
  - returns: Type: Int32 The ID of the first record found; -1 if not record was found.
- `protected bool fullQtySelected()`
  - returns: Type: Boolean
- `protected abstract void glCreditPosting( TransactionBase sender, TransactionBase.GLPostingEventArgs e )`
  - param `sender` (Pastel.Evolution.TransactionBase)
  - param `e` (Pastel.Evolution.TransactionBase.GLPostingEventArgs)
- `protected abstract void glDebitPosting( TransactionBase sender, TransactionBase.GLPostingEventArgs e )`
  - param `sender` (Pastel.Evolution.TransactionBase)
  - param `e` (Pastel.Evolution.TransactionBase.GLPostingEventArgs)
- `protected internal virtual void initialise()` — Reverts the order to an unsaved, version 0 (see remarks) state.
  - remarks: Version 0: When using the Revert method, the order is set to an unsaved state, allowing it to be saved as another order. It does not; however, revert back to the last saved state, but rather assumes the current state as far as order detail is concerned.
- `public static DataTable List( string criteria )` — Gets a list of database records.
  - param `criteria` (System.String) — Specifies the criteria as a SQL where clause.
  - returns: Type: DataTable Table containing selected records.
- `protected internal override void OnDelete()` — Not supported. Use the delete facility from inside Evolution.
- `protected internal override void OnSave()`
- `public virtual string Process()` — Posts the document to the various accounts and ledgers applicable.
  - returns: Type: String The generated reference number.
- `public virtual string Process( string reference )` — Posts the document to the various accounts and ledgers applicable.
  - param `reference` (System.String) — Specifies the transaction reference to use. No duplication checking is performed.
  - returns: Type: String The reference number supplied.
  - remarks: Use this method when a document reference has already been generated outside the Evolution system.

## Fields (19)
- `protected DrCrAccount account`
- `protected int archID`
- `protected Currency currency`
- `protected DrCrTransaction dcTran`
- `protected Address deliverTo`
- `protected DeliveryMethod deliveryMethod`
- `protected OrderDetailCollection detail`
- `protected internal GLBatch glBatch`
- `protected Address invoiceTo`
- `protected Priority orderPriority`
- `protected OrderStatus orderStatus`
- `protected OrderBase originalDocument`
- `protected internal bool processingAdditionalCosts`
- `protected internal bool processLedger` — Should the document process to AR or AP ledger?
- `protected internal bool processStock`
- `protected Project project`
- `protected Prospect prospect`
- `protected SettlementTerms settlementTerms`
- `protected TaxRate taxType`

# OrderDetail (Class)

Represents an inventory document detail record.

**Namespace:** Pastel.Evolution

```csharp
public class OrderDetail : BranchedRecordBase
```

## Constructors (7)
- `public OrderDetail()` — Creates a new instance of a order detail record.
- `public OrderDetail( long id )` — Creates a new instance of an order detail record.
- `public OrderDetail( string itemCode, double quantity, double price )` — Creates a new instance of an order detail record.
- `public OrderDetail( InventoryItem item, double quantity, double price )` — Creates a new instance of an order detail record.
- `public OrderDetail( InventoryItem item, double quantity, double price, TaxMode taxMode )` — Creates a new instance of an order detail record.
- `public OrderDetail( InventoryItem item, string warehouseCode, double quantity, double price )` — Creates a new instance of an order detail record.
- `public OrderDetail( InventoryItem item, string warehouseCode, double quantity, double price, TaxMode taxMode )` — Creates a new instance of an order detail record.

## Properties (100)
- `public AccountBase Account { get; set; }` — Gets or sets the line's account (inventory item or GL account [in near future]).
- `public string Description { get; set; }` — Gets or sets the line description.
- `public double Discount { get; set; }` — Gets or sets the total line discount value (applies to tax excl. value)
- `public double DiscountPercent { get; set; }` — Gets or sets the line discount percentage as an integer value: 5% = 5, as opposed to 0.05
- `public OrderBase Document { get; }` — Gets the document to which the detail record belongs.
- `public GLAccount GLAccount { get; set; }` — Gets or sets the line's GLAccount.
- `public int GLAccountID { get; set; }` — Gets or sets the GLAccount item id.
- `public override int ID { get; }` — Gets the internal record ID (0 for new, unsaved records).
- `public int Index { get; internal set; }` — Gets the line number (1-based)
- `public InventoryItem InventoryItem { get; set; }` — Gets or sets the line's inventory item.
- `public int InventoryItemID { get; set; }` — Gets or sets the stock item id.
- `public int JobID { get; set; }` — Gets or sets the order detail record's job id.
- `public double LastProcess { get; }` — Gets the stock quantity moved during the last processing action.
- `public override long LongID { get; }` — Transitional accessor.
- `public Lot Lot { get; set; }`
- `public int LotID { get; set; }`
- `public Module Module { get; }` — Indicates the Evolution module of the Order Detail line.
- `public string Note { get; set; }` — Gets or sets the line note text.
- `public double Outstanding { get; }` — Gets the quantity of stock that remains to be processed.
- `public GLAccount OverrideCostOfSalesAccount { get; set; }` — Specifies the GL account to use when processing the document's cost of goods sold transaction.
- `public GLAccount OverridePurchaseAccount { get; set; }` — Specifies the purchases GL account to use when processing the document's GL transactions. Currently this is merely an alias for
- `public GLAccount OverrideSalesAccount { get; set; }` — Specifies the GL account to use when processing the document's sales transaction.
- `public GLAccount OverrideStockAccount { get; set; }` — Specifies the GL account to use when processing the document's GL stock transaction.
- `public int PriceListNameID { get; set; }` — Gets or sets the line pricelistID.
- `public double Processed { get; }` — Gets the quantity of stock processed on this line up until this document.
- `public Project Project { get; set; }` — Gets or sets the line's project.
- `public int ProjectID { get; set; }` — Gets or sets the line's project id.
- `public double Quantity { get; set; }` — Gets or sets the quantity of product on order.
- `public SalesRepresentative Representative { get; set; }` — Gets or sets the sales representative on the order line. This only applies to sales transactions. When not set, the representative will default to the rep specified (if any) on the order document.
- `public int RepresentativeID { get; set; }` — Gets or sets the representative id.
- `public double Reserved { get; set; }` — Gets or sets the quantity of stock to reserve for an order (only applies to sales orders).
- `public SerialNumberCollection SerialNumbers { get; }` — Gets the collection of serial numbers pertaining to the order detail record.
- `public TaxMode TaxMode { get; set; }` — Gets or sets the line's tax mode.
- `public TaxRate TaxType { get; set; }`
- `public double ToProcess { get; set; }` — Gets or sets the quantity of stock to move when calling the Process method.
- `public double TotalAdditionalCost { get; set; }` — Gets or sets the additional cost allocated to the line.
- `public double TotalExcl { get; }` — Gets the calculated, rounded line total exclusive amount, after discount.
- `public double TotalExclBeforeDiscount { get; }`
- `public double TotalExclBeforeDiscountForeign { get; }`
- `public double TotalExclBeforeDiscountForeignRaw { get; }`
- `public double TotalExclBeforeDiscountRaw { get; }`
- `public double TotalExclForeign { get; }`
- `public double TotalExclRaw { get; }`
- `public double TotalIncl { get; }` — Gets the calculated line total inclusive amount, after discount.
- `public double TotalInclBeforeDiscount { get; }`
- `public double TotalInclBeforeDiscountForeign { get; }`
- `public double TotalInclForeign { get; }`
- `public double TotalLastProcessExcl { get; }`
- `public double TotalLastProcessExclAfterDocumentDiscount { get; }`
- `public double TotalLastProcessExclForeign { get; }`
- `public double TotalLastProcessExclForeignAfterDocumentDiscount { get; }`
- `public double TotalLastProcessIncl { get; }`
- `public double TotalLastProcessInclForeign { get; }`
- `public double TotalLastProcessTax { get; }`
- `public double TotalLastProcessTaxAfterDocumentDiscount { get; }`
- `public double TotalLastProcessTaxForeign { get; }`
- `public double TotalLastProcessTaxForeignAfterDocumentDiscount { get; }`
- `public double TotalOutstandingExcl { get; }`
- `public double TotalOutstandingExclForeign { get; }`
- `public double TotalOutstandingIncl { get; }`
- `public double TotalOutstandingInclForeign { get; }`
- `public double TotalOutstandingTax { get; }`
- `public double TotalOutstandingTaxForeign { get; }`
- `public double TotalProcessedExcl { get; }`
- `public double TotalProcessedExclForeign { get; }`
- `public double TotalProcessedIncl { get; }`
- `public double TotalProcessedInclForeign { get; }`
- `public double TotalProcessedTax { get; }`
- `public double TotalProcessedTaxForeign { get; }`
- `public double TotalSalesCost { get; }` — Gets the line total cost of sale; i.e. current unit cost * quantity
- `public double TotalTax { get; set; }` — Gets or sets the line total tax amount. Set this value as late as possible as it gets recalculated on setting Quantity, UnitSellingPrice, DiscountPercent, Discount, TaxType, as well as when adding the order detail record to the orders's Detail collection. IMPORTANT: Be sure to only use the Process() method and not one of the Complete* methods if you wish to override the tax amount. Setting TotalTax also does not affect TotalToProcessTax.
- `public double TotalTaxBeforeDiscount { get; }` — Gets the tax amount before discount was applied. If discount is 100% and the total tax amount is 0, the tax rate is used to calculate a default tax amount.
- `public double TotalTaxBeforeDiscountForeign { get; }`
- `public double TotalTaxForeign { get; set; }`
- `public double TotalToProcessExcl { get; }`
- `public double TotalToProcessExclBeforeDiscount { get; }`
- `public double TotalToProcessExclBeforeDiscountForeign { get; }`
- `public double TotalToProcessExclForeign { get; }`
- `public double TotalToProcessIncl { get; }`
- `public double TotalToProcessInclBeforeDiscount { get; }`
- `public double TotalToProcessInclBeforeDiscountForeign { get; }`
- `public double TotalToProcessInclForeign { get; }`
- `public double TotalToProcessTax { get; set; }` — Gets or sets the line total tax amount for the following invoice. Set this value as late as possible as it gets recalculated on setting ToProcess, UnitSellingPrice, DiscountPercent, Discount, TaxType, as well as when adding the order detail record to the orders's Detail collection. IMPORTANT: Be sure to only use the Process() method and not one of the Complete* methods only if you wish to override the tax amount.
- `public double TotalToProcessTaxAfterDocumentDiscount { get; }`
- `public double TotalToProcessTaxBeforeDiscount { get; }`
- `public double TotalToProcessTaxBeforeDiscountForeign { get; }`
- `public double TotalToProcessTaxForeign { get; set; }`
- `public double TotalToProcessTaxForeignAfterDocumentDiscount { get; }`
- `public Unit Unit { get; set; }`
- `public double UnitCostPrice { get; set; }` — Gets or sets the unit cost price (used by credit notes only).
- `public int UnitID { get; set; }`
- `public double UnitSellingPrice { get; set; }` — Gets or sets the unit selling or purchase price.
- `public double UnitSellingPriceAfterDiscount { get; }` — Gets the line's unit selling price after discount.
- `public double UnitSellingPriceAfterDocumentDiscountExcl { get; }` — Gets the order detail's unit selling price excl after line and document discount (unrounded).
- `public double UnitSellingPriceExclAfterLineDiscount { get; }` — Gets the order detail's unit selling price excl after line discount (unrounded).
- `public double UnitSellingPriceForeign { get; set; }` — Gets or sets the foreign unit selling price - on sales orders this will be the product selling price as expected, but on purchase orders, it is the supplier's selling price.
- `public FieldCollection UserFields { get; }`
- `public Warehouse Warehouse { get; set; }` — Gets or sets the warehouse relevant to this detail record. Set the warehouse only after setting the inventory item. The Warehouse and WarehouseContext properties are mapped to one another.
- `public WarehouseContext WarehouseContext { get; set; }` — Gets or sets the warehouse context of the inventory item specified. Set the warehouse only after setting the inventory item. The Warehouse and WarehouseContext properties are mapped to one another.
- `public int WarehouseID { get; }` — Gets the ID of the assigned warehouse (0 if N/A).

## Methods (7)
- `public OrderDetail _Copy()` — Experimental Method
  - returns: Type: OrderDetail
- `public static int Find( string criteria )` — Finds a record's database ID.
  - param `criteria` (System.String) — Specifies the criteria as a SQL where clause.
  - returns: Type: Int32 The ID of the first record found; -1 if not record was found.
- `public DataTable List( string criteria )` — Gets a list of database records.
  - param `criteria` (System.String) — Specifies the criteria as a SQL where clause.
  - returns: Type: DataTable Table containing selected records.
- `protected internal override void OnDelete()` — Removes the detail record from the order document only, not from the database. Save the order after calling Delete to delete the line from the database.
- `protected internal override void OnSave()` — Persists the record to the database.
- `protected internal void SetDocument( OrderBase document )`
  - param `document` (Pastel.Evolution.OrderBase)
- `public override string ToString()`
  - returns: Type: String

# OrderDetailCollection (Class)

Represents a collection of order detail items, typically owned by a given inventory document record.

**Namespace:** Pastel.Evolution

```csharp
public class OrderDetailCollection : CollectionBase,
    ICloneable
```

## Properties (49)
- `Item` — Gets an order detail object by its zero-based index.
- `public int LastProcessCount { get; }`
- `public int OutstandingCount { get; }`
- `public int ToProcessCount { get; }`
- `public double TotalAdditionalCost { get; }`
- `public double TotalExcl { get; }`
- `public double TotalExclBeforeDiscount { get; }`
- `public double TotalExclBeforeDiscountForeign { get; }`
- `public double TotalExclForeign { get; }`
- `public double TotalIncl { get; }`
- `public double TotalInclForeign { get; }`
- `public double TotalLastProcessExcl { get; }`
- `public double TotalLastProcessExclForeign { get; }`
- `public double TotalLastProcessIncl { get; }`
- `public double TotalLastProcessInclForeign { get; }`
- `public double TotalLastProcessQuantity { get; }`
- `public double TotalLastProcessTax { get; }`
- `public double TotalLastProcessTaxAfterDocumentDiscount { get; }`
- `public double TotalLastProcessTaxAfterDocumentDiscountForeign { get; }`
- `public double TotalLastProcessTaxForeign { get; }`
- `public double TotalOutstandingExcl { get; }`
- `public double TotalOutstandingExclAfterDocumentDiscount { get; }`
- `public double TotalOutstandingExclAfterDocumentDiscountForeign { get; }`
- `public double TotalOutstandingExclForeign { get; }`
- `public double TotalOutstandingIncl { get; }`
- `public double TotalOutstandingInclForeign { get; }`
- `public double TotalOutstandingQuantity { get; }`
- `public double TotalOutstandingTax { get; }`
- `public double TotalOutstandingTaxAfterDocumentDiscount { get; }`
- `public double TotalOutstandingTaxAfterDocumentDiscountForeign { get; }`
- `public double TotalOutstandingTaxForeign { get; }`
- `public double TotalQuantity { get; }`
- `public double TotalSalesCost { get; }` — Gets the total cost of sale; i.e. current unit cost * quantity
- `public double TotalTax { get; }`
- `public double TotalTaxAfterDocumentDiscount { get; }`
- `public double TotalTaxAfterDocumentDiscountForeign { get; }`
- `public double TotalTaxForeign { get; }`
- `public double TotalToProcessExcl { get; }`
- `public double TotalToProcessExclAfterDocumentDiscount { get; }`
- `public double TotalToProcessExclForeign { get; }`
- `public double TotalToProcessExclForeignAfterDocumentDiscount { get; }`
- `public double TotalToProcessIncl { get; }`
- `public double TotalToProcessInclAfterDocumentDiscount { get; }`
- `public double TotalToProcessInclAfterDocumentDiscountForeign { get; }`
- `public double TotalToProcessInclForeign { get; }`
- `public double TotalToProcessTax { get; }`
- `public double TotalToProcessTaxAfterDocumentDiscount { get; }`
- `public double TotalToProcessTaxForeign { get; }`
- `public double TotalToProcessTaxForeignAfterDocumentDiscount { get; }`

## Methods (7)
- `public void Add( OrderDetail detailRecord )` — Appends an order detail object to the order.
  - param `detailRecord` (Pastel.Evolution.OrderDetail)
  - remarks: Take note that upon being added to a document, the detail record will assume the document's sales representative and project.
- `public OrderDetail Add( string itemCode, double quantity, double price )` — Appends a detail line to the order.
  - param `itemCode` (System.String) — The code of the stock item
  - param `quantity` (System.Double) — The quantity to order
  - param `price` (System.Double) — The exclusive unit price
  - returns: Type: OrderDetail The newly created detail record.
- `public OrderDetail Add( InventoryItem item, double quantity, double price )` — Appends a detail line to the order.
  - param `item` (Pastel.Evolution.InventoryItem) — The stock item object.
  - param `quantity` (System.Double) — The quantity to order.
  - param `price` (System.Double) — The unit price.
  - returns: Type: OrderDetail The newly created detail record.
- `public OrderDetail Add( string itemCode, string warehouseCode, double quantity, double price )` — Appends a detail line to the order.
  - param `itemCode` (System.String) — The code of the stock item
  - param `warehouseCode` (System.String) — The code of the warehouse to use on this record.
  - param `quantity` (System.Double) — The quantity to order
  - param `price` (System.Double) — The exclusive unit price
  - returns: Type: OrderDetail The newly created detail record.
- `public OrderDetail Add( InventoryItem item, string warehouseCode, double quantity, double price )` — Appends a detail line to the order.
  - param `item` (Pastel.Evolution.InventoryItem) — The code of the stock item.
  - param `warehouseCode` (System.String) — The code of the warehouse to use on this record.
  - param `quantity` (System.Double) — The quantity to order.
  - param `price` (System.Double) — The exclusive unit price.
  - returns: Type: OrderDetail The newly created detail record.
- `public Object Clone()`
  - returns: Type: Object
- `protected override void OnClear()`
- `public void OnCollectionChanged( OrderDetailCollection.OrderDetailCollectionChangedEventArgs e )`
  - param `e` (Pastel.Evolution.OrderDetailCollection.OrderDetailCollectionChangedEventArgs)
- `public void Process( int archID )` — Calls the Process method on each detail record
  - param `archID` (System.Int32)
- `public void Remove( OrderDetail detailRecord )` — Removes the specified order detail line from the collection
  - param `detailRecord` (Pastel.Evolution.OrderDetail)
- `public void RemoveAt( int index )` — Removes an order detail line using its zero-based index.
  - param `index` (System.Int32)

## Events (1)
- `public event OrderDetailCollection.OrderDetailChangedEventHandler CollectionChanged` — Occurs when detail records are added or deleted.

# OrderDetailCollection.OrderDetailChangedEventHandler (Delegate)

**Namespace:** Pastel.Evolution

```csharp
public delegate void OrderDetailChangedEventHandler(
    Object sender,
    OrderDetailCollection.OrderDetailCollectionChangedEventArgs e
    )
```

# OrderDetailCollection.OrderDetailCollectionChangedEventArgs (Class)

**Namespace:** Pastel.Evolution

```csharp
public class OrderDetailCollectionChangedEventArgs : EventArgs
```

## Fields (2)
- `public OrderDetailCollection.OrderDetailChangeAction Action`
- `public OrderDetail DetailRecord`

# OrderStatus (Class)

Represents a user-definable inventory document status.

**Namespace:** Pastel.Evolution

```csharp
public class OrderStatus : BranchedRecordBase
```

## Constructors (3)
- `public OrderStatus()` — Creates a new instance of an order status.
- `public OrderStatus( int id )` — Creates a new instance of an order status.
- `public OrderStatus( string code )` — Creates a new instance of an order status.

## Properties (3)
- `public string Description { get; set; }` — Gets or sets the record description.
- `public override int ID { get; }` — Gets the internal record ID (0 for new, unsaved records).
- `public override long LongID { get; }`

## Methods (4)
- `public static int Find( string criteria )` — Finds a record's database ID.
  - param `criteria` (System.String) — Specifies the criteria as a SQL where clause.
  - returns: Type: Int32 The ID of the first record found; -1 if not record was found.
- `public DataTable List( string criteria )` — Gets a list of database records.
  - param `criteria` (System.String) — Specifies the criteria as a SQL where clause.
  - returns: Type: DataTable Table containing selected records.
- `protected internal override void OnDelete()` — Removes the record from the database, provided it is not referenced by other records.
- `protected internal override void OnSave()` — Persists the record to the database.

# PackCode (Class)

Represents an inventory item pack code.

**Namespace:** Pastel.Evolution

```csharp
public class PackCode : BranchedRecordBase
```

## Constructors (3)
- `public PackCode()` — Creates a new instance of a pack code.
- `public PackCode( int id )` — Creates a new instance of a pack code.
- `public PackCode( string code )` — Creates a new instance of a pack code.

## Properties (5)
- `public string Code { get; set; }` — Gets or sets the pack code's code.
- `public string Description { get; set; }` — Gets or sets the pack code's description.
- `public override int ID { get; }` — Gets the internal record ID (0 for new, unsaved records).
- `public override long LongID { get; }`
- `public double Size { get; set; }` — Gets or sets the pack code's size.

## Methods (5)
- `public static int Find( string criteria )` — Finds a record's database ID.
  - param `criteria` (System.String) — Specifies the criteria as a SQL where clause.
  - returns: Type: Int32 The ID of the first record found; -1 if not record was found.
- `public static int FindByCode( string code )` — Attempts to find a PackCode by its code and returns its ID.
  - param `code` (System.String) — The code used to lookup the packcode.
  - returns: Type: Int32 -1 if no record was found, else the id of the first packcode matching the criteria supplied.
- `public DataTable List( string criteria )` — Gets a list of database records.
  - param `criteria` (System.String) — Specifies the criteria as a SQL where clause.
  - returns: Type: DataTable Table containing selected records.
- `protected internal override void OnDelete()` — Removes the record from the database, provided it is not referenced by other records.
- `protected internal override void OnSave()` — Persists the record to the database.

# PercentageOfCompletedContractPostingMethodGLContext (Class)

**Namespace:** Pastel.Evolution

```csharp
public class PercentageOfCompletedContractPostingMethodGLContext : TransactionTypePostingMethodGLContextBase
```

## Properties (16)
- `public override GLAccount COSAccount { get; set; }` — Gets or sets the Transaction Code's COS GL Account.
- `public override int COSAccountID { get; set; }`
- `public override GLAccount CustomerControlAccount { get; set; }` — Gets or sets the Transaction Code's Customer Control GL Account.
- `public override int CustomerControlAccountID { get; set; }`
- `public override GLAccount RecoveryAccount { get; set; }` — Gets or sets the Transaction Code's Recovery GL Account.
- `public override int RecoveryAccountID { get; set; }`
- `public override GLAccount SalesAccount { get; set; }` — Gets or sets the Transaction Code's Sales GL Account.
- `public override int SalesAccountID { get; set; }`
- `public override GLAccount StockAccount { get; set; }` — Gets or sets the Transaction Code's Stock GL Account.
- `public override int StockAccountID { get; set; }`
- `public override GLAccount SupplierControlAccount { get; set; }` — Gets or sets the Transaction Code's Supplier Control GL Account.
- `public override int SupplierControlAccountID { get; set; }`
- `public override GLAccount TaxAccount { get; set; }` — Gets or sets the Transaction Code's Tax GL Account.
- `public override int TaxAccountID { get; set; }`
- `public override GLAccount WIPAccount { get; set; }` — Gets or sets the Transaction Code's WIP GL Account.
- `public override int WIPAccountID { get; set; }`

# Person (Class)

Represents a person record.

**Namespace:** Pastel.Evolution

```csharp
public class Person : BranchedRecordBase
```

## Constructors (2)
- `public Person()` — Creates a new instance of a person.
- `public Person( int id )` — Creates a new instance of a person.

## Properties (23)
- `public Address Address { get; set; }`
- `public DateTime BirthDate { get; set; }`
- `public string Comments { get; set; }` — Gets or sets comments for this person.
- `public Department Department { get; set; }`
- `public int DepartmentID { get; set; }`
- `public string Description { get; set; }`
- `public Designation Designation { get; set; }`
- `public int DesignationID { get; set; }`
- `public string EmailAddress { get; set; }` — Gets or sets the person's email address.
- `public string Fax { get; set; }`
- `public string FirstName { get; set; }` — Gets or sets the person's first name.
- `public string FullName { get; set; }` — Gets or sets the person's full name. (a.k.a. display name)
- `public override int ID { get; }` — Gets the internal record ID (0 for new, unsaved records).
- `public string Initials { get; set; }`
- `public string LastName { get; set; }` — Gets or sets the person's last name.
- `public override long LongID { get; }`
- `public Address PostalAddress { get; set; }`
- `public string TelHome { get; set; }`
- `public string TelMobile { get; set; }`
- `public string TelWork { get; set; }`
- `public string Title { get; set; }`
- `public FieldCollection UserFields { get; }`
- `public string WebPage { get; set; }`

## Methods (7)
- `public void _CreateLink( BranchedRecordBase record )` — Temporary method for linking a person to either a customer, supplier, or prospective customer record. This will most likely become obsolete in future.
  - param `record` (Pastel.Evolution.BranchedRecordBase)
- `public static DataTable _ListCurrentBranch( string criteria )`
  - param `criteria` (System.String)
  - returns: Type: DataTable
- `public static int Find( string criteria )` — Finds a record's database ID.
  - param `criteria` (System.String) — Specifies the criteria as a SQL where clause.
  - returns: Type: Int32 The ID of the first record found; -1 if not record was found.
- `public static int Find( string criteria, Object[] args )` — Finds a record's database ID.
  - param `criteria` (System.String) — Specifies the criteria as a SQL where clause containing zero or more format items.
  - param `args` (System.Object []) — The arguments to pass to the String.Format function for replacing parameters in the criteria string.
  - returns: Type: Int32 The ID of the first record found; -1 if not record was found.
- `public void GenerateFullName()`
- `public static DataTable List( string criteria )` — Returns a System.Data.DataTable object containing the database records from the Client table matching the supplied criteria.
  - param `criteria` (System.String) — The SQL criteria used to locate the record, e.g. Account like '1___'
  - returns: Type: DataTable A System.Data.DataTable object containing matching records.
  - remarks: The criteria is passed to an SQL query so use the appropriate syntax. Remember to include the single quotes around string literals and append additional criteria with and .
- `protected internal override void OnDelete()` — Removes the record from the database, provided it is not referenced by other records.
- `protected internal override void OnSave()` — Persists the record to the database.

# PostDatedCheque (Class)

Represents a post dated transaction.

**Namespace:** Pastel.Evolution

```csharp
public class PostDatedCheque : BranchedRecordBase
```

## Constructors (2)
- `public PostDatedCheque()` — Initializes a new instance of the PostDatedCheque class
- `public PostDatedCheque( int id )` — Initializes a new instance of the PostDatedCheque class

## Properties (33)
- `public double Amount { get; set; }` — Gets or sets the (gross) transaction value. Negative values are allowed and will result in inverted debits and credits.
- `public bool Cancelled { get; set; }` — Gets or sets whether the Post Dated Cheque is Cancelled.
- `public string CancelledReason { get; set; }` — Gets or sets the Post Dated Cheque Cancelled Reason.
- `public GLAccount ContraGLAccount { get; set; }` — Gets or sets the Contra General Ledger.
- `public int ContraGLAccountID { get; set; }` — Gets or sets the Contra General Ledger's ID.
- `public Currency Currency { get; }`
- `public Customer Customer { get; set; }` — Gets or sets the Customer.
- `public int CustomerID { get; set; }` — Gets or sets the Customer's ID.
- `public DateTime Date { get; set; }` — Gets or sets the Transaction's Date.
- `public string Description { get; set; }` — Gets or sets the Transaction Description.
- `public double DiscountAmount { get; set; }` — Gets or sets the discount value.
- `public double DiscountForeignTax { get; set; }` — Gets or sets the post dated cheque discount foreign tax amount (automatically rounded to 2 decimals).
- `public double DiscountTax { get; set; }` — Gets or sets the post dated cheque discount tax amount (automatically rounded to 2 decimals).
- `public int DiscountTaxRateID { get; set; }` — Gets or sets the Discount TaxRate's ID.
- `public TaxRate DiscountTaxType { get; set; }` — Gets or sets the Discount TaxRate.
- `public double ExchangeRate { get; set; }` — Gets or sets the applicable exchange rate, expressed as [home currency]/[foreign currency]. Defaults to applicable exchange rate for the transaction date.
- `public double ForeignAmount { get; set; }` — Gets or sets the foreign transaction value.
- `public double ForeignDiscountAmount { get; set; }` — Gets or sets the foreign discount value.
- `public double ForeignTax { get; set; }` — Gets or sets the post dated cheque foreign tax amount (automatically rounded to 2 decimals).
- `public override int ID { get; }`
- `public override long LongID { get; }`
- `public string OrderNumber { get; set; }` — Gets or sets the Transaction Order Number.
- `public Project Project { get; set; }` — Gets or sets the Project.
- `public int ProjectID { get; set; }` — Gets or sets the Project's ID.
- `public string Reference { get; set; }` — Gets or sets the Transaction Reference.
- `public string Reference2 { get; set; }` — Gets or sets the Transaction Reference 2.
- `public SalesRepresentative SalesRep { get; set; }` — Gets or sets the Sales Rep.
- `public int SalesRepID { get; set; }` — Gets or sets the Sales Rep's ID.
- `public double Tax { get; set; }` — Gets or sets the post dated cheque tax amount (automatically rounded to 2 decimals).
- `public TaxRate TaxType { get; set; }` — Gets or sets the TaxRate.
- `public int TaxTypeID { get; set; }` — Gets or sets the TaxRate's ID.
- `public TransactionCodeBase TransactionCode { get; set; }` — Gets or sets the Transaction Code.
- `public int TransactionCodeID { get; set; }` — Gets or sets the Transaction Code's ID.

## Methods (13)
- `public static DataTable _ListCurrentBranch( string criteria )`
  - param `criteria` (System.String)
  - returns: Type: DataTable
- `protected void calcAmounts()`
- `protected void calcDiscountAmounts()`
- `protected void calcDiscountTaxValues()`
- `protected void calcTaxValues()`
- `public static int Find( string criteria )` — Finds a post dated Cheque ID.
  - param `criteria` (System.String) — The criteria passed to the SQL query. Eg. cpdcReference = 'CH001'
  - returns: Type: Int32
- `public static PostDatedCheque Get( string criteria )` — Returns the [first] post dated cheque object matching the criteria specified; otherwise, returns null.
  - param `criteria` (System.String) — Eg. cpdcReference = 'CH001'
  - returns: Type: PostDatedCheque
- `protected double getExchangeRate()`
  - returns: Type: Double
- `public static DataTable List( string criteria )` — Returns a System.Data.DataTable object containing the database records from the _etblPostDatedCheques table matching the supplied criteria.
  - param `criteria` (System.String) — The SQL criteria used to locate the record, e.g. cpdcReference like '1___'
  - returns: Type: DataTable A System.Data.DataTable object containing matching records.
  - remarks: The criteria is passed to an SQL query so use the appropriate syntax. Remember to includethe single quotes around string literals and append additional criteria with and.
- `public static DataTable List( string criteria, string sortOrder )` — Returns a System.Data.DataTable object containing the database records from the _etblPostDatedCheques table matching the supplied criteria.
  - param `criteria` (System.String) — The SQL criteria used to locate the record, e.g. cpdcReference like '1___'
  - param `sortOrder` (System.String) — The SQL order by clause to use, e.g. cpdcReference, etc
  - returns: Type: DataTable A System.Data.DataTable object containing matching records.
  - remarks: The criteria is passed to an SQL query so use the appropriate syntax. Remember to includethe single quotes around string literals and append additional criteria with and.
- `protected internal override void OnDelete()`
- `protected internal override void OnSave()`
- `protected void setExchangeRate( double value )`
  - param `value` (System.Double)
- `protected bool Validate()`
  - returns: Type: Boolean

## Fields (14)
- `protected double amount`
- `protected double discountAmount`
- `protected double discountForeignAmount`
- `protected double discountForeignTax`
- `protected double discountTax`
- `protected internal Utils.LimitedQueue fcDiscountQueue`
- `protected internal Utils.LimitedQueue fcQueue`
- `protected double foreignAmount`
- `protected double foreignOriginalDiscountTax`
- `protected double foreignOriginalTax`
- `protected double foreignTax`
- `protected double originalDiscountTax`
- `protected double originalTax`
- `protected double tax`

# PriceList (Class)

Represents an inventory price list.

**Namespace:** Pastel.Evolution

```csharp
public class PriceList : BranchedRecordBase
```

## Constructors (3)
- `public PriceList()` — Creates a new instance of a price list.
- `public PriceList( int id )` — Creates a new instance of a price list.
- `public PriceList( string name )` — Creates a new instance of a price list.

## Properties (4)
- `public string Description { get; set; }` — Gets or sets the price list's description.
- `public override int ID { get; }` — Gets the internal record ID (0 for new, unsaved records).
- `public override long LongID { get; }`
- `public string Name { get; set; }` — Gets or sets the price list's name.

## Methods (8)
- `public static int Find( string criteria )` — Finds a record's database ID.
  - param `criteria` (System.String) — Specifies the criteria as a SQL where clause.
  - returns: Type: Int32 The ID of the first record found; -1 if not record was found.
- `public static int FindByName( string name )` — Executes the FindByName method.
  - param `name` (System.String) — Specifies the name.
  - returns: Type: Int32 The FindByName.
- `public static PriceList Get( string criteria )` — Returns an instance of the first record satisfying the criteria specified; otherwise, returns null.
  - param `criteria` (System.String) — Specifies the criteria as a SQL where clause.
  - returns: Type: PriceList The record found; otherwise null
- `public static PriceList GetByName( string name )` — Gets the by name.
  - param `name` (System.String) — Specifies the name.
  - returns: Type: PriceList The ByName.
- `public static PriceList GetDefault()` — Gets the default price list.
  - returns: Type: PriceList The Default.
- `public static DataTable List( string criteria )` — Gets a list of database records.
  - param `criteria` (System.String) — Specifies the criteria as a SQL where clause.
  - returns: Type: DataTable Table containing selected records.
- `protected internal override void OnDelete()` — Removes the record from the database, provided it is not referenced by other records.
- `protected internal override void OnSave()` — Persists the record to the database.

# PrintGroup (Class)

Represents a print group, which is a collection of inventory documents enabling batch printing.

**Namespace:** Pastel.Evolution

```csharp
public class PrintGroup : BranchedRecordBase
```

## Constructors (2)
- `public PrintGroup( int id )` — Creates a new instance of a print group.
- `public PrintGroup( string description, DocumentType documentType )` — Creates a new instance of a print group.

## Properties (5)
- `public string Description { get; set; }` — Gets or sets the record description.
- `public ArrayList DocumentIDs { get; }` — Gets the print group's ArrayList of document ID's.
- `public DocumentType DocumentType { get; }` — Gets the print group's document type.
- `public override int ID { get; }` — Gets the internal record ID (0 for new, unsaved records).
- `public override long LongID { get; }`

## Methods (6)
- `public void AddDocument( OrderBase document )` — Appends a document to the print group.
  - param `document` (Pastel.Evolution.OrderBase) — Specifies the document.
- `public static int Find( string criteria )` — Finds a record's database ID.
  - param `criteria` (System.String) — Specifies the criteria.
  - returns: Type: Int32 The ID of the first record found; -1 if not record was found.
- `public DataTable List( string criteria )` — Gets a list of database records.
  - param `criteria` (System.String) — Specifies the criteria as a SQL where clause.
  - returns: Type: DataTable Table containing selected records.
- `protected internal override void OnDelete()` — Not supported.
- `protected internal override void OnSave()` — Persists the record to the database.
- `public void RemoveDocument( OrderBase document )` — Removes a document from the print group.
  - param `document` (Pastel.Evolution.OrderBase)

# Priority (Class)

Represents an incident priority.

**Namespace:** Pastel.Evolution

```csharp
public class Priority : BranchedRecordBase
```

## Constructors (3)
- `public Priority()` — Creates a new instance of a priority.
- `public Priority( int id )` — Creates a new instance of a priority.
- `public Priority( string description )` — Creates a new instance of a priority.

## Properties (5)
- `public int Colour { get; set; }` — Gets or sets the priority's colour.
- `public string Description { get; set; }` — Gets or sets the record description.
- `public override int ID { get; }` — Gets the internal record ID (0 for new, unsaved records).
- `public bool IsDefault { get; }` — Gets whether or not the priority is the default priority.
- `public override long LongID { get; }`

## Methods (5)
- `public static int Find( string criteria )` — Finds a record's database ID.
  - param `criteria` (System.String) — Specifies the criteria as a SQL where clause.
  - returns: Type: Int32 The ID of the first record found; -1 if not record was found.
- `public Priority GetDefault()`
  - returns: Type: Priority
- `public DataTable List( string criteria )` — Gets a list of database records.
  - param `criteria` (System.String) — Specifies the criteria as a SQL where clause.
  - returns: Type: DataTable Table containing selected records.
- `protected internal override void OnDelete()` — Removes the record from the database, provided it is not referenced by other records.
- `protected internal override void OnSave()` — Persists the record to the database.

# Project (Class)

Represents a project.

**Namespace:** Pastel.Evolution

```csharp
public class Project : BranchedRecordBase
```

## Constructors (3)
- `public Project()` — Creates a new instance of a project.
- `public Project( int id )` — Creates a new instance of a project.
- `public Project( string code )` — Creates a new instance of a project.

## Properties (6)
- `public bool Active { get; set; }` — Gets or sets the record's operational state.
- `public string Code { get; set; }` — Gets or sets the project code.
- `public string Description { get; set; }` — Gets or sets the project description (name, in this case).
- `public override int ID { get; }` — Gets the internal record ID (0 for new, unsaved records).
- `public override long LongID { get; }`
- `public string ProjectDescription { get; set; }` — Gets or sets the project's description.

## Methods (8)
- `public static DataTable _ListCurrentBranch( string criteria )`
  - param `criteria` (System.String)
  - returns: Type: DataTable
- `public static int Find( string criteria )` — Finds a project ID.
  - param `criteria` (System.String) — The criteria passed to the SQL query. Eg. ProjectCode = 'INT001' or ProjectName like '%Internal%'
  - returns: Type: Int32 The ID of the first record found; -1 if not record was found.
- `public static int FindByCode( string code )` — Attempts to find a project by its code and returns its ID.
  - param `code` (System.String) — The code used to lookup the project.
  - returns: Type: Int32 -1 if no record was found, else the id of the first record matching the criteria supplied.
- `public static Project Get( string criteria )` — Returns an instance of the first record satisfying the criteria specified; otherwise, returns null.
  - param `criteria` (System.String) — The criteria passed to the SQL query. Eg. ProjectCode = 'INT001' or ProjectName like '%Internal%'
  - returns: Type: Project The record found; otherwise null
- `public static Project GetByCode( string code )` — Returns an instance of the first record with the code specified; otherwise, returns null.
  - param `code` (System.String) — Specifies the code.
  - returns: Type: Project The record found; otherwise null
- `public static DataTable List( string criteria )` — Gets a list of database records.
  - param `criteria` (System.String) — Specifies the criteria as a SQL where clause.
  - returns: Type: DataTable Table containing selected records.
- `protected internal override void OnDelete()` — Removes the record from the database, provided it is not referenced by other records.
- `protected internal override void OnSave()` — Persists the record to the database.

# Prospect (Class)

Represents a Contact Management prospective customer.

**Namespace:** Pastel.Evolution

```csharp
public class Prospect : BranchedRecordBase
```

## Constructors (3)
- `public Prospect()` — Creates a new instance of a prospect.
- `public Prospect( int id )` — Creates a new instance of a prospect.
- `public Prospect( string companyName )` — Creates a new instance of a prospect.

## Properties (17)
- `public Agent Agent { get; set; }` — Gets or sets the agent to whom the prospect belongs. Prospects can be hidden from other agents by setting IsPublic to false.
- `public bool ChargeTax { get; set; }` — Gets or sets whether the account is taxed (on quotations etc.)
- `public string CompanyName { get; set; }`
- `public string Description { get; set; }`
- `public string EmailAddress { get; set; }`
- `public string Fax { get; set; }`
- `public override int ID { get; }` — Gets the internal record ID (0 for new, unsaved records).
- `public bool IsPublic { get; set; }` — Gets or sets whether or not the prospect is visible to agents other than the assigned agent.
- `public override long LongID { get; }`
- `public Module Module { get; }`
- `public Address PhysicalAddress { get; set; }` — Gets or sets the account's physical address.
- `public Address PostalAddress { get; set; }` — Gets or sets the account's postal address.
- `public SalesRepresentative Representative { get; set; }` — Gets or sets the Sales Representative.
- `public int RepresentativeID { get; set; }` — Gets or sets the Sales Representative ID.
- `public string Telephone { get; set; }`
- `public FieldCollection UserFields { get; }`
- `public string Webpage { get; set; }`

## Methods (5)
- `public static int Find( string criteria )`
  - param `criteria` (System.String)
  - returns: Type: Int32
- `public static int FindByCompanyName( string companyName )` — Attempts to find a Prospect by its Company Name and returns its ID.
  - param `companyName` (System.String) — The Company Name used to lookup the prospect.
  - returns: Type: Int32 -1 if no record was found, else the id of the first account matching the criteria supplied.
- `public static DataTable List( string criteria )`
  - param `criteria` (System.String)
  - returns: Type: DataTable
- `protected internal override void OnDelete()` — Removes the record from the database, provided it is not referenced by other records.
- `protected internal override void OnSave()` — Persists the record to the database.

# PurchaseOrder (Class)

Representation a Purchase Order document.

**Namespace:** Pastel.Evolution

```csharp
public class PurchaseOrder : PurchasesDocumentBase
```

## Constructors (4)
- `public PurchaseOrder()` — Creates a new instance of a purchase order.
- `public PurchaseOrder( int id )` — Creates a new instance of a purchase order.
- `public PurchaseOrder( string orderNo )` — Creates a new instance of an existing purchase order.
- `public PurchaseOrder( string orderNumber, string grvNumber )` — Creates an instance of an existing unprocessed supplier invoice having the given purchase order and grv numbers.

## Properties (4)
- `public PurchaseOrder.GrvPhase GrvState { get; internal set; }` — Gets the phase of this goods receiving document, either a goods received note or a supplier invoice.
- `public override OrderBase OriginalDocument { get; }`
- `public Supplier Supplier { get; set; }` — Gets or sets the order's supplier account (maps directly to Account).
- `public string SupplierInvoiceNo { get; set; }` — Gets or sets the document supplier invoice number.

## Methods (13)
- `protected override void BeforePostGLBatch( OrderBase orderBase, CancelEventArgs e )`
  - param `orderBase` (Pastel.Evolution.OrderBase)
  - param `e` (System.ComponentModel.CancelEventArgs)
- `protected override void BeforePostInventory( OrderBase orderBase, CancelEventArgs e )`
  - param `orderBase` (Pastel.Evolution.OrderBase)
  - param `e` (System.ComponentModel.CancelEventArgs)
- `protected override void BeforePostLedger( OrderBase orderBase, CancelEventArgs e )`
  - param `orderBase` (Pastel.Evolution.OrderBase)
  - param `e` (System.ComponentModel.CancelEventArgs)
- `public string CompleteStock()` — Processes a stock receipt (maximum quantity) without posting a supplier invoice. Only allowed when supplier invoice/GRV separation is enabled in purchase order defaults.
  - returns: Type: String The generated GRV number.
- `public string CompleteStock( string reference )` — Processes a stock receipt (maximum quantity) without posting a supplier invoice. Only allowed when supplier invoice/GRV separation is enabled in purchase order defaults.
  - param `reference` (System.String) — Specifies the GRV number to post.
  - returns: Type: String The supplied GRV number.
- `protected override void Detach()`
- `public static int Find( string criteria )` — Finds and returns the id of the first order matching the supplied criteria. E.g. OrderNum = 'PO0001'
  - param `criteria` (System.String) — Specifies the criteria as a SQL where clause.
  - returns: Type: Int32 The ID of the first record found; -1 if not record was found.
- `protected override void glCreditPosting( TransactionBase sender, TransactionBase.GLPostingEventArgs e )`
  - param `sender` (Pastel.Evolution.TransactionBase)
  - param `e` (Pastel.Evolution.TransactionBase.GLPostingEventArgs)
- `protected override void glDebitPosting( TransactionBase sender, TransactionBase.GLPostingEventArgs e )`
  - param `sender` (Pastel.Evolution.TransactionBase)
  - param `e` (Pastel.Evolution.TransactionBase.GLPostingEventArgs)
- `protected internal override void initialise()`
- `public static DataTable List( string criteria )` — Lists outstanding orders for the supplied criteria.
  - param `criteria` (System.String) — E.g. Supplier.Account = 'SUPP001' and (OrderNum = 'PO209302')
  - returns: Type: DataTable
  - remarks: Table aliases: Core, Supplier
- `protected internal override void OnSave()`
- `public override string Process( string reference )` — Posts the document to the various accounts and ledgers applicable.
  - param `reference` (System.String) — Specifies the GRV Number to post. If specified, no number will be generated. Note that no duplication checking is performed. When processing an unprocessed supplier invoice document, the reference parameter is ignored.
  - returns: Type: String
- `public string ProcessStock()` — Processes a stock receipt without posting a supplier invoice. Only allowed when supplier invoice/GRV separation is enabled in purchase order defaults.
  - returns: Type: String The generated GRV number.
- `public string ProcessStock( string reference )` — Processes a stock receipt without posting a supplier invoice. Only allowed when supplier invoice/GRV separation is enabled in purchase order defaults.
  - param `reference` (System.String) — Custom GRV number.
  - returns: Type: String The GRV number passed in; the generated GRV number if an empty string is supplied.
  - remarks: Receiving stock results in an archived GRV document and an unprocessed supplier invoice document.

# PurchasesDocumentBase (Class)

**Namespace:** Pastel.Evolution

```csharp
public abstract class PurchasesDocumentBase : OrderBase
```

## Constructors (4)
- `protected internal PurchasesDocumentBase()` — Initializes a new instance of the PurchasesDocumentBase class
- `protected internal PurchasesDocumentBase( int id )` — Initializes a new instance of the PurchasesDocumentBase class
- `protected internal PurchasesDocumentBase( string orderNumber, DocumentType documentType )` — Initializes a new instance of the PurchasesDocumentBase class
- `protected internal PurchasesDocumentBase( string orderNumber, DocumentType documentType, string orderNumber2, int documentFlag )` — Initializes a new instance of the PurchasesDocumentBase class

## Properties (1)
- `public CostAllocationCollection AdditionalCosts { get; }`

## Methods (1)
- `protected internal override void OnSave()`

# RecordBase (Class)

Embodies a common Evolution record, such as an account.

**Namespace:** Pastel.Evolution

```csharp
public abstract class RecordBase
```

## Properties (2)
- `public abstract int ID { get; }` — Gets the internal record ID (0 for new, unsaved records).
- `public abstract long LongID { get; }` — Gets the internal record ID (0 for new, unsaved records).

## Methods (6)
- `public void Delete()` — Removes the record from the database, provided it is not referenced by other records.
- `public bool Equals( RecordBase obj )`
  - param `obj` (Pastel.Evolution.RecordBase)
  - returns: Type: Boolean
- `protected internal abstract void OnDelete()`
- `protected internal abstract void OnSave()`
- `public void Save()` — Persists the record to the database.
- `protected static void TestRange( double value, double minValue, double maxValue, string valueDescription )`
  - param `value` (System.Double)
  - param `minValue` (System.Double)
  - param `maxValue` (System.Double)
  - param `valueDescription` (System.String)

## Fields (1)
- `protected internal RecordWrapperBase wrapper`

# ReturnToSupplier (Class)

Represents a return to supplier document.

**Namespace:** Pastel.Evolution

```csharp
public class ReturnToSupplier : PurchasesDocumentBase
```

## Constructors (3)
- `public ReturnToSupplier()` — Initializes a new instance of the ReturnToSupplier class
- `public ReturnToSupplier( int id )` — Initializes a new instance of the ReturnToSupplier class
- `public ReturnToSupplier( string reference )` — Initializes a new instance of the ReturnToSupplier class

## Properties (4)
- `public string InvoiceNumber { get; set; }`
- `public override bool IsPartialProcessingAllowed { get; }`
- `public override OrderBase OriginalDocument { get; }`
- `public Supplier Supplier { get; set; }`

## Methods (8)
- `protected override void BeforePostGLBatch( OrderBase orderBase, CancelEventArgs e )`
  - param `orderBase` (Pastel.Evolution.OrderBase)
  - param `e` (System.ComponentModel.CancelEventArgs)
- `protected override void BeforePostInventory( OrderBase orderBase, CancelEventArgs e )`
  - param `orderBase` (Pastel.Evolution.OrderBase)
  - param `e` (System.ComponentModel.CancelEventArgs)
- `protected override void BeforePostLedger( OrderBase orderBase, CancelEventArgs e )`
  - param `orderBase` (Pastel.Evolution.OrderBase)
  - param `e` (System.ComponentModel.CancelEventArgs)
- `public static int Find( string criteria )` — Finds and returns the id of the first order matching the supplied criteria. E.g. OrderNum = 'PO0001'
  - param `criteria` (System.String) — Specifies the criteria as a SQL where clause.
  - returns: Type: Int32 The ID of the first record found; -1 if not record was found.
- `protected override void glCreditPosting( TransactionBase sender, TransactionBase.GLPostingEventArgs e )`
  - param `sender` (Pastel.Evolution.TransactionBase)
  - param `e` (Pastel.Evolution.TransactionBase.GLPostingEventArgs)
- `protected override void glDebitPosting( TransactionBase sender, TransactionBase.GLPostingEventArgs e )`
  - param `sender` (Pastel.Evolution.TransactionBase)
  - param `e` (Pastel.Evolution.TransactionBase.GLPostingEventArgs)
- `protected internal override void initialise()`
- `public static DataTable List( string criteria )` — Lists documents for the supplied criteria.
  - param `criteria` (System.String) — E.g. Supplier.Account = 'SUPP001' and (OrderNum = 'PO209302')
  - returns: Type: DataTable
  - remarks: Table aliases: Core, Supplier

# SalesDocumentBase (Class)

**Namespace:** Pastel.Evolution

```csharp
public abstract class SalesDocumentBase : OrderBase
```

## Constructors (3)
- `protected internal SalesDocumentBase()` — Initializes a new instance of the SalesDocumentBase class
- `protected internal SalesDocumentBase( int id )` — Initializes a new instance of the SalesDocumentBase class
- `protected internal SalesDocumentBase( string orderNumber, DocumentType documentType )` — Initializes a new instance of the SalesDocumentBase class

## Properties (4)
- `public Customer Customer { get; set; }` — Gets or sets the document's customer account (maps directly to Account).
- `public SalesRepresentative Representative { get; set; }` — Gets or sets the document sales representative.
- `public int RepresentativeID { get; set; }` — Gets or sets the sales representative ID.
- `public Opportunity SalesOpportunity { get; set; }`

## Methods (2)
- `public double CalcRounding( double docTotal, double denom, int rndOpt )`
  - param `docTotal` (System.Double)
  - param `denom` (System.Double)
  - param `rndOpt` (System.Int32)
  - returns: Type: Double
- `protected internal void cascadeRepresentative()`

## Fields (2)
- `protected Opportunity salesOpp`
- `protected SalesRepresentative salesRep`

# SalesOrder (Class)

An object representation of an Evolution Sales Order.

**Namespace:** Pastel.Evolution

```csharp
public class SalesOrder : SalesDocumentBase
```

## Constructors (3)
- `public SalesOrder()` — Creates a new instance of a sales order.
- `public SalesOrder( int id )` — Creates a new instance of a sales order.
- `public SalesOrder( string orderNumber )` — Creates a new instance of a sales order.

## Properties (2)
- `public string DeliveryNote { get; set; }` — Gets or sets the document delivery note number
- `public override OrderBase OriginalDocument { get; }` — Gets the order's original document.

## Methods (10)
- `public void _SetMaxQtyToProcess()` — Experimental method
- `protected override void BeforePostGLBatch( OrderBase orderBase, CancelEventArgs e )`
  - param `orderBase` (Pastel.Evolution.OrderBase)
  - param `e` (System.ComponentModel.CancelEventArgs)
- `protected override void BeforePostInventory( OrderBase orderBase, CancelEventArgs e )`
  - param `orderBase` (Pastel.Evolution.OrderBase)
  - param `e` (System.ComponentModel.CancelEventArgs)
- `protected override void BeforePostLedger( OrderBase orderBase, CancelEventArgs e )`
  - param `orderBase` (Pastel.Evolution.OrderBase)
  - param `e` (System.ComponentModel.CancelEventArgs)
- `public string CompleteMax()` — Processes as much of the ordered stock as is available. If an "all or nothing" approach is required, use the method instead.
  - returns: Type: String Invoice number
- `public static int Find( string criteria )` — Finds and returns the id of the first order matching the supplied criteria. E.g. OrderNum = 'SO0001'
  - param `criteria` (System.String) — Specifies the criteria as a SQL where clause.
  - returns: Type: Int32 The ID of the first record found; -1 if not record was found.
- `protected override void glCreditPosting( TransactionBase sender, TransactionBase.GLPostingEventArgs e )`
  - param `sender` (Pastel.Evolution.TransactionBase)
  - param `e` (Pastel.Evolution.TransactionBase.GLPostingEventArgs)
- `protected override void glDebitPosting( TransactionBase sender, TransactionBase.GLPostingEventArgs e )`
  - param `sender` (Pastel.Evolution.TransactionBase)
  - param `e` (Pastel.Evolution.TransactionBase.GLPostingEventArgs)
- `protected internal override void initialise()`
- `public static DataTable List( string criteria )` — Lists outstanding orders for the supplied criteria.
  - param `criteria` (System.String) — E.g. Customer.Account = 'CASH001' and (OrderNum = 'SO209302')
  - returns: Type: DataTable
  - remarks: Pseudo-tables: Core, Customer

# SalesOrderQuotation (Class)

**Namespace:** Pastel.Evolution

```csharp
public class SalesOrderQuotation : SalesOrder
```

## Constructors (3)
- `public SalesOrderQuotation()` — Initializes a new instance of the SalesOrderQuotation class
- `public SalesOrderQuotation( int id )` — Initializes a new instance of the SalesOrderQuotation class
- `public SalesOrderQuotation( string quoteReference )` — Initializes a new instance of the SalesOrderQuotation class

## Properties (1)
- `public string QuoteNo { get; set; }`

## Methods (4)
- `protected internal override void BeforeSave()`
- `public SalesOrder ConvertToOrder()` — Converts a quotation into an unprocessed sales order. If automatic numbering is enabled and immediate processing required, this step may be omitted. Otherwise, convert the quote, then set the order number and finally, process.
  - returns: Type: SalesOrder
- `public static int Find( string criteria )` — Finds and returns the id of the first order matching the supplied criteria. E.g. OrderNum = 'SO0001'
  - param `criteria` (System.String) — Specifies the criteria as a SQL where clause.
  - returns: Type: Int32 The ID of the first record found; -1 if not record was found.
- `public static DataTable List( string criteria )` — Lists quotations for the supplied criteria.
  - param `criteria` (System.String) — E.g. Customer.Account = 'CASH001' and (OrderNum = 'SO209302')
  - returns: Type: DataTable
  - remarks: Pseudo-tables: Core, Customer

# SalesRepresentative (Class)

Represents an Evolution sales representative.

**Namespace:** Pastel.Evolution

```csharp
public class SalesRepresentative : BranchedRecordBase
```

## Constructors (3)
- `public SalesRepresentative()` — Creates a new instance of a representative.
- `public SalesRepresentative( int id )` — Creates a new instance of a representative.
- `public SalesRepresentative( string code )` — Creates a new instance of a representative.

## Properties (12)
- `public string Address1 { get; set; }` — Gets or sets the representative's address line 1.
- `public string Address2 { get; set; }` — Gets or sets the representative's address2.
- `public string Address3 { get; set; }` — Gets or sets the representative's address3.
- `public string Address4 { get; set; }` — Gets or sets the representative's address4.
- `public string Bank { get; set; }` — Gets or sets the representative's bank.
- `public string Code { get; set; }` — Gets or sets the representative's code.
- `public string Comment1 { get; set; }` — Gets or sets the representative's comment1.
- `public string Comment2 { get; set; }` — Gets or sets the representative's comment2.
- `public string Description { get; set; }` — Gets or sets the representative's name.
- `public override int ID { get; }` — Gets the internal record ID (0 for new, unsaved records).
- `public override long LongID { get; }`
- `public bool OnHold { get; set; }` — Gets or sets the representative's status.

## Methods (7)
- `public static int Find( string criteria )` — Finds a record's database ID.
  - param `criteria` (System.String) — Specifies the criteria as a SQL where clause.
  - returns: Type: Int32 The ID of the first record found; -1 if not record was found.
- `public static int FindByCode( string code )` — Attempts to find a representative by its code and returns its ID.
  - param `code` (System.String) — The code used to lookup the record.
  - returns: Type: Int32 -1 if no record was found, else the id of the first record matching the criteria supplied.
- `public static SalesRepresentative Get( string criteria )` — Returns the [first] group object with the code specified; otherwise, returns null.
  - param `criteria` (System.String) — Eg. Code like '1_B%'
  - returns: Type: SalesRepresentative The record found; otherwise null
- `public static SalesRepresentative GetByCode( string code )` — Returns a representative object corresponding to the code specified; otherwise, returns null.
  - param `code` (System.String) — Specifies the code.
  - returns: Type: SalesRepresentative The record found; otherwise null
- `public static DataTable List( string criteria )` — Gets a list of database records.
  - param `criteria` (System.String) — Specifies the criteria as a SQL where clause.
  - returns: Type: DataTable Table containing selected records.
- `protected internal override void OnDelete()` — Removes the record from the database, provided it is not referenced by other records.
- `protected internal override void OnSave()` — Persists the record to the database.

# SellingPrice (Class)

Represents a collection of inventory selling prices.

**Namespace:** Pastel.Evolution

```csharp
public class SellingPrice
```

## Properties (8)
- `public int ID { get; }` — Gets the record ID.
- `public long LongID { get; }` — Transitional accessor.
- `public InventoryCostingMethod MarkupCostingMethod { get; set; }`
- `public double MarkupPercentage { get; set; }` — Gets or sets the markup percentage to be used in calculating this selling price. One can either specify a markup percentage,or specify fixed prices, but not both.
- `public double PriceExcl { get; set; }` — Gets or sets the vat-exclusive unit price. Setting a value will automatically calculate the inclusive price using thedefault invoicing tax code on the inveotory item, and also cancel the effect of any markup percentage set.
- `public double PriceIncl { get; set; }` — Gets or sets the vat-inclusive unit price. Setting a value will automatically calculate the exclusive price using thedefault invoicing tax code on the inveotory item, and also cancel the effect of any markup percentage set.
- `public PriceList PriceList { get; }` — Gets the price list this selling price belongs to.
- `public InventoryItem StockItem { get; }` — Gets the stock item this selling price belongs to.

## Methods (5)
- `public static DataTable List( string criteria )` — Gets a list of database records.
  - param `criteria` (System.String) — Specifies the criteria as a SQL where clause.
  - returns: Type: DataTable Table containing selected records.
- `public static DataTable ListByPriceListID( int id )` — Gets a list of selling prices by price list ID.
  - param `id` (System.Int32) — Specifies the price list id.
  - returns: Type: DataTable The ListByPriceListID.
- `public static DataTable ListByStockItemAndWarehouseID( int stockID, int warehouseID )` — Gets a list of selling prices by stock item ID and Warehouse ID.
  - param `stockID` (System.Int32) — Specifies the stock item id.
  - param `warehouseID` (System.Int32) — Specifies the warehouse id.
  - returns: Type: DataTable The ListByStockItemAndWarehouseID.
- `public static DataTable ListByStockItemID( int id )` — Gets a list of selling prices by stock item ID.
  - param `id` (System.Int32) — Specifies the stock item id.
  - returns: Type: DataTable The ListByStockItemID.
- `public void Save()` — Saves the individual selling price. Note that saving the inventory item automatically saves the entire selling price collection.

# SellingPriceCollection (Class)

Represents an inventory selling price collection.

**Namespace:** Pastel.Evolution

```csharp
public class SellingPriceCollection : CollectionBase
```

## Properties (1)
- `Item` — Gets a selling price in the item's price collection.

## Methods (2)
- `protected override void OnRemove( int index, Object value )`
  - param `index` (System.Int32)
  - param `value` (System.Object)
- `public void Save()`

# Serialiser (Class)

**Namespace:** Pastel.Evolution

```csharp
public class Serialiser
```

## Methods (1)
- `public static void PersistToFile( Object rec, string path )`
  - param `rec` (System.Object)
  - param `path` (System.String)

# SerialNumber (Class)

Represents a distinct serial number.

**Namespace:** Pastel.Evolution

```csharp
public class SerialNumber : BranchedRecordBase
```

## Constructors (5)
- `public SerialNumber()` — Initializes a new instance of the SerialNumber class
- `public SerialNumber( int id )` — Initializes a new instance of the SerialNumber class
- `public SerialNumber( string code, InventoryItem stockItem )` — Initializes a new instance of the SerialNumber class
- `public SerialNumber( string code, int stockID )` — Initializes a new instance of the SerialNumber class
- `public SerialNumber( string code, int stockID, SerialNumberLocation location )` — Initializes a new instance of the SerialNumber class

## Properties (9)
- `public string Code { get; set; }`
- `public AccountBase CurrentAccount { get; internal set; }`
- `public SerialNumberLocation CurrentLocation { get; internal set; }`
- `public override int ID { get; }`
- `public DateTime LastMovement { get; }`
- `public override long LongID { get; }`
- `public int LotID { get; set; }`
- `public InventoryItem StockItem { get; set; }`
- `public int StockItemID { get; set; }`

## Methods (6)
- `public static SerialNumber[] _Select( string criteria )` — Experimental Method
  - param `criteria` (System.String)
  - returns: Type: SerialNumber []
- `public static SerialNumber[] _Select( string criteria, string sortOrder )` — Experimental Method
  - param `criteria` (System.String)
  - param `sortOrder` (System.String)
  - returns: Type: SerialNumber []
- `public static int Find( string criteria )` — Finds the first record matching the criteria supplied
  - param `criteria` (System.String) — E.g. Code = 'abc'
  - returns: Type: Int32 The id of the record
- `public static DataTable List( string criteria )` — Returns a datatable containing the matching rows.
  - param `criteria` (System.String) — e.g. SNStockLink = 100 and CurrentLoc = (int)SerialNumberLocation.InStock
  - returns: Type: DataTable
- `public static DataTable List( string criteria, string sortOrder )` — Returns a datatable containing the matching rows.
  - param `criteria` (System.String)
  - param `sortOrder` (System.String)
  - returns: Type: DataTable
- `public static DataTable List( InventoryItem item, SerialNumberLocation currentLocation )` — Returns a datatable containing the matching rows.
  - param `item` (Pastel.Evolution.InventoryItem) — The inventory item to which the serial numbers belong.
  - param `currentLocation` (Pastel.Evolution.SerialNumberLocation) — The current location of the serial numbers.
  - returns: Type: DataTable
- `protected internal override void OnDelete()`
- `protected internal override void OnSave()`
- `public override string ToString()`
  - returns: Type: String

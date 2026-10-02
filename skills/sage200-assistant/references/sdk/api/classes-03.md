<!-- source: Pastel.Evolution.chm, Pastel.Evolution SDK 11.0.0.10 | verified: 2026-10-02 -->

# SerialNumberCollection (Class)

Represents a collection of serial numbers, typically linked to a transaction or inventory document detail record.

**Namespace:** Pastel.Evolution

```csharp
public class SerialNumberCollection : CollectionBase
```

## Constructors (2)
- `public SerialNumberCollection()` — Initializes a new instance of the SerialNumberCollection class
- `public SerialNumberCollection( OrderDetail orderDetail )` — Initializes a new instance of the SerialNumberCollection class

## Properties (3)
- `public InventoryItem InventoryItem { get; set; }`
- `Item`
- `public SerialNumberTransaction.MovementParameters MovementParameters { get; set; }`

## Methods (5)
- `public void Add( string sn )` — Adds a serial number for the code specified. If the serial number does not exist, it will be initalised as a new serial number record. The stock item needs to be assigned in this case.
  - param `sn` (System.String)
- `public void Add( params string[] serialNos )` — Adds a collection of serial numbers for the code specified. If a serial number does not exist, it will be initalised as a new serial number record. The stock item needs to be assigned to the owner of the collection in this case.
  - param `serialNos` (System.String []) — The string array of serial numbers.
- `public void Add( SerialNumber sn )` — Adds a serial number for the code specified. If the serial number does not exist, it will be initalised as a new serial number record. The stock item needs to be assigned in this case.
  - param `sn` (Pastel.Evolution.SerialNumber)
- `public void Delete()`
- `public void Load()`
- `public void Remove( SerialNumber sn )`
  - param `sn` (Pastel.Evolution.SerialNumber)
- `public void Save()`
- `public void Save( OrderDetail orderDetail )`
  - param `orderDetail` (Pastel.Evolution.OrderDetail)

# SerialNumberTransaction (Class)

Summary description for Transaction.

**Namespace:** Pastel.Evolution

```csharp
public class SerialNumberTransaction
```

## Properties (17)
- `public SerialNumber Account { get; set; }`
- `public long AccountID { get; set; }`
- `public string Audit { get; }`
- `public DateTime Date { get; set; }`
- `public int ID { get; }`
- `public long JobCardID { get; set; }`
- `public Module Module { get; }`
- `public AccountBase Owner { get; set; }`
- `public Project Project { set; }`
- `public int ProjectID { get; set; }`
- `public string Reference { get; set; }`
- `public string Reference2 { get; set; }`
- `public TransactionCodeBase TranCode { get; set; }`
- `public int TranCodeID { get; set; }`
- `public SerialNumberTransaction.SerialNumberMovement Type { get; set; }`
- `public Warehouse Warehouse { get; set; }`
- `public int WarehouseID { get; set; }`

## Methods (1)
- `public bool Validate()`
  - returns: Type: Boolean

# SerialNumberTransaction.MovementParameters (Class)

Represents a set of parameters used by a serial number collection when relocating serial numbers.

**Namespace:** Pastel.Evolution

```csharp
public class MovementParameters
```

## Properties (3)
- `public SerialNumberTransaction.SerialNumberMovement Movement { get; set; }`
- `public AccountBase NewAccount { get; set; }`
- `public InventoryTransaction Transaction { get; set; }`

# SettlementTerms (Class)

Represents settlement terms.

**Namespace:** Pastel.Evolution

```csharp
public class SettlementTerms : BranchedRecordBase
```

## Constructors (3)
- `public SettlementTerms()` — Creates a new instance of settlement terms.
- `public SettlementTerms( int id )` — Creates a new instance of settlement terms.
- `public SettlementTerms( string code )` — Creates a new instance of settlement terms.

## Properties (7)
- `public AgeingDate Base { get; set; }`
- `public string Code { get; set; }` — Gets or sets the SettlementTerms code.
- `public int Days { get; set; }`
- `public string Description { get; set; }` — Gets or sets the settlement terms' description.
- `public double DiscountPercentage { get; set; }` — Gets or sets the applicable discount as a value between 0 and 100.
- `public override int ID { get; }` — Gets the internal record ID (0 for new, unsaved records).
- `public override long LongID { get; }`

## Methods (7)
- `public static int Find( string criteria )` — Finds a settlement terms record ID.
  - param `criteria` (System.String) — The criteria passed to the SQL query. Eg. cSettlementCode = 'INT001' or cSettlementDescription like '%Internal%'
  - returns: Type: Int32 The ID of the first record found; -1 if not record was found.
- `public static int FindByCode( string code )` — Attempts to find settlement terms by its code and returns its ID.
  - param `code` (System.String) — The code used to lookup the settlement terms.
  - returns: Type: Int32 -1 if no record was found, else the id of the first account matching the criteria supplied.
- `public static SettlementTerms Get( string criteria )` — Returns an instance of the first record satisfying the criteria specified; otherwise, returns null.
  - param `criteria` (System.String) — The criteria passed to the SQL query. Eg. cSettlementCode = 'INT001' or cSettlementDescription like '%Internal%'
  - returns: Type: SettlementTerms The record found; otherwise null
- `public static SettlementTerms GetByCode( string code )` — Returns an instance of the first record with the code specified; otherwise, returns null.
  - param `code` (System.String) — Specifies the code.
  - returns: Type: SettlementTerms The record found; otherwise null
- `public DataTable List( string criteria )` — Gets a list of database records.
  - param `criteria` (System.String) — Specifies the criteria as a SQL where clause.
  - returns: Type: DataTable Table containing selected records.
- `protected internal override void OnDelete()` — Removes the record from the database, provided it is not referenced by other records.
- `protected internal override void OnSave()` — Persists the record to the database.

# SplitAllocation (Class)

Describes a transaction split allocation used when splitting a transaction's contra entry.

**Namespace:** Pastel.Evolution

```csharp
public class SplitAllocation
```

## Constructors (2)
- `public SplitAllocation()` — Initializes a new instance of the SplitAllocation class
- `public SplitAllocation( GLAccount account, double amount )` — Creates a new instance of a transaction split allocation entry.

## Properties (5)
- `public GLAccount Account { get; set; }` — Gets or sets the GL account to post to.
- `public double Amount { get; set; }` — Gets or sets the value of this split allocation. Note that the Amount and Foreign amount properties are mutually exclusive. Setting one value will zero the other.
- `public string Description { get; set; }`
- `public double ForeignAmount { get; set; }` — Gets or sets the foreign value of this split allocation. Note that the Amount and Foreign amount properties are mutually exclusive. Setting one value will zero the other.
- `public Project Project { get; set; }`

# SplitAllocationCollection (Class)

**Namespace:** Pastel.Evolution

```csharp
public class SplitAllocationCollection : CollectionBase
```

## Properties (1)
- `public SplitAllocation this[ int index ] { get; set; }`

## Methods (4)
- `public void Add( SplitAllocation splitEntry )`
  - param `splitEntry` (Pastel.Evolution.SplitAllocation)
- `public SplitAllocation Add( string accountCode, double amount )`
  - param `accountCode` (System.String)
  - param `amount` (System.Double)
  - returns: Type: SplitAllocation
- `public SplitAllocation Add( GLAccount account, double amount )`
  - param `account` (Pastel.Evolution.GLAccount)
  - param `amount` (System.Double)
  - returns: Type: SplitAllocation
- `public void OnCollectionChanged( SplitAllocationCollection.OrderDetailCollectionChangedEventArgs e )`
  - param `e` (Pastel.Evolution.SplitAllocationCollection.OrderDetailCollectionChangedEventArgs)
- `public void Remove( SplitAllocation splitEntry )`
  - param `splitEntry` (Pastel.Evolution.SplitAllocation)
- `public void RemoveAt( int index )`
  - param `index` (System.Int32)

## Events (1)
- `public event SplitAllocationCollection.OrderDetailChangedEventHandler CollectionChanged` — Occurs when detail records are added or deleted.

# SplitAllocationCollection.OrderDetailChangedEventHandler (Delegate)

**Namespace:** Pastel.Evolution

```csharp
public delegate void OrderDetailChangedEventHandler(
    Object sender,
    SplitAllocationCollection.OrderDetailCollectionChangedEventArgs e
    )
```

# SplitAllocationCollection.OrderDetailCollectionChangedEventArgs (Class)

**Namespace:** Pastel.Evolution

```csharp
public class OrderDetailCollectionChangedEventArgs : EventArgs
```

## Fields (2)
- `public SplitAllocationCollection.OrderDetailChangeAction Action`
- `public OrderDetail DetailRecord`

# Supplier (Class)

Represents a supplier account.

**Namespace:** Pastel.Evolution

```csharp
public class Supplier : DrCrAccount
```

## Constructors (3)
- `public Supplier()` — Creates a new instance of a supplier account.
- `public Supplier( int id )` — Creates a new instance of a supplier account.
- `public Supplier( string code )` — Creates a new instance of a supplier account.

## Properties (65)
- `public override double AccountBalance { get; }` — Gets the account's current balance.
- `public string AccountDescription { get; set; }` — Gets or sets the account's account description.
- `public int AccountTerms { get; set; }` — Gets or sets the account terms.
- `public override bool Active { get; set; }` — Gets or sets the record's operational state.
- `public string Addressee { get; set; }` — Gets or sets the account's addressee.
- `public Area Areas { get; set; }` — Gets or sets the account's area.
- `public int AreasID { get; set; }` — Gets or sets the account's area id.
- `public double AutomaticDiscount { get; set; }` — Gets or sets the account's automatic discount percentage.
- `public AutoPaymentMethod AutoPaymentMethod { get; set; }` — Gets or sets the account's automatic payment method.
- `public int BalanceBroughtForward { get; set; }`
- `public Bank Bank { get; set; }` — Gets or sets the account's bank.
- `public string BankAccountNo { get; set; }` — Gets or sets the account's bank account number.
- `public Bank.AccountType BankAccountType { get; set; }` — Gets or sets the account's bank account type.
- `public string BankBranchCode { get; set; }` — Gets or sets the account's bank branch code.
- `public int BankID { get; set; }` — Gets or sets the account's bank id.
- `public string BankReferenceNo { get; set; }` — Gets or sets the account's bank reference number.
- `public BusinessClass BusinessClass { get; set; }` — Gets or sets the account's business class.
- `public int BusinessClassID { get; set; }` — Gets or sets the account's business class id.
- `public BusinessType BusinessType { get; set; }` — Gets or sets the account's business type.
- `public int BusinessTypeID { get; set; }` — Gets or sets the account's business type id.
- `public override bool ChargeTax { get; set; }` — Gets or sets the account's taxable status.
- `public bool CheckTerms { get; set; }` — Gets or sets whether or not the account's terms will be checked before posting a transaction.
- `public override string Code { get; set; }` — Gets or sets the account's code.
- `public string ContactPerson { get; set; }` — Gets or sets the account's contact person.
- `public Country Country { get; set; }` — Gets or sets the account's country.
- `public int CountryID { get; set; }` — Gets or sets the account's country id.
- `public double CreditLimit { get; set; }` — Gets or sets the credit limit.
- `public override Currency Currency { get; set; }` — Gets or sets the account's currency. null indicates home currency.
- `public override int CurrencyID { get; set; }` — Gets or sets the account's currency id. 0 indicates local currency.
- `public override SettlementTerms DefaultSettlementTerms { get; set; }`
- `public TaxRate DefaultTaxRate { get; set; }` — Gets or sets the account's default tax rate.
- `public int DefaultTaxRateID { get; set; }` — Gets or sets the account's default tax rate id.
- `public string DeliverTo { get; set; }` — Gets or sets the account's addressee.
- `public override string Description { get; set; }` — Gets or sets the account's description.
- `public int DiscountMatrixRow { get; set; }` — Gets or sets the account's discount matrix row.
- `public string EmailAddress { get; set; }` — Gets or sets the account's email address.
- `public bool EmailRemittance { get; set; }` — Gets or sets the whether or not the account requires an emailed statement.
- `public string Fax1 { get; set; }` — Gets or sets the fax number.
- `public string Fax2 { get; set; }` — Gets or sets the 2nd fax number.
- `public override double ForeignAccountBalance { get; }` — Gets the account's foreign account balance.
- `public SupplierGroup Group { get; set; }` — Gets or sets the account's group.
- `public int GroupID { get; set; }` — Gets or sets the account's group id.
- `public override int ID { get; }` — Gets the internal record ID (0 for new, unsaved records).
- `public string Initials { get; set; }` — Gets or sets the account's initials.
- `public double InterestRate { get; set; }` — Gets or sets the account's interest rate.
- `public override bool IsForeignCurrencyAccount { get; }` — Whether or not the account is a foreign currency account.
- `public bool IsOnHold { get; set; }` — Gets or sets whether or not the account is on hold.
- `public Supplier this[ string code ] { get; }`
- `public override long LongID { get; }`
- `public override Module Module { get; }` — Gets the account's Evolution module.
- `public Address PhysicalAddress { get; set; }` — Gets or sets the account's physical address.
- `public Address PostalAddress { get; set; }` — Gets or sets the account's postal address.
- `public bool PrintRemittance { get; set; }` — Gets or sets the whether or not the account requires a printed statement.
- `[ObsoleteAttribute("Use UserFields instead.")] public FieldCollection RawFieldData { get; }`
- `public string Registration { get; set; }` — Gets or sets the registration number.
- `public double SettlementDiscountPercent { get; set; }` — Gets or sets the account's settlement discount percentage.
- `public string StatementZipPassword { get; set; }` — Gets or sets the account's emailed statement's zip password.
- `public string TaxNumber { get; set; }` — Gets or sets the tax number.
- `public string Telephone { get; set; }` — Gets or sets the telephone number.
- `public string Telephone2 { get; set; }` — Gets or sets the 2nd telephone number.
- `public DateTime Timestamp { get; }` — Gets the account's timestamp.
- `public string Title { get; set; }` — Gets or sets the account's title.
- `public bool UseEmail { get; set; }` — Gets or sets the account's use email.
- `public FieldCollection UserFields { get; }`
- `public string Webpage { get; set; }` — Gets or sets the account's website address.

## Methods (7)
- `public static int Find( string criteria )` — Finds a record's database ID.
  - param `criteria` (System.String) — Eg. Account = 'CASH001' or Name like '%CASH%'
  - returns: Type: Int32 The ID of the first record found; -1 if not record was found.
- `public static int FindByCode( string code )` — Finds the database ID of a record matching the specified code.
  - param `code` (System.String) — Specifies the code.
  - returns: Type: Int32 The ID of the first record found; -1 if not record was found.
- `public static Supplier Get( string criteria )` — Returns an instance of the first record satisfying the criteria specified; otherwise, returns null.
  - param `criteria` (System.String) — Eg. Account = 'CASH001' or Name like '%CASH%'
  - returns: Type: Supplier The record found; otherwise null
- `public static Supplier GetByCode( string code )` — Returns an instance of the first record with the code specified; otherwise, returns null.
  - param `code` (System.String) — Specifies the code.
  - returns: Type: Supplier The record found; otherwise null
- `public static DataTable List( string criteria )` — Gets a list of database records.
  - param `criteria` (System.String) — Specifies the criteria as a SQL where clause.
  - returns: Type: DataTable Table containing selected records.
- `protected internal override void OnDelete()` — Removes the record from the database, provided it is not referenced by other records.
- `protected internal override void OnSave()` — Persists the record to the database.

# SupplierGroup (Class)

Represents a supplier group.

**Namespace:** Pastel.Evolution

```csharp
public class SupplierGroup : BranchedRecordBase
```

## Constructors (3)
- `public SupplierGroup()` — Creates a new instance of a group.
- `public SupplierGroup( int id )` — Creates a new instance of a group.
- `public SupplierGroup( string code )` — Creates a new instance of a group.

## Properties (12)
- `public string Code { get; set; }` — Gets or sets the group's code.
- `public GLAccount ControlAccount { get; set; }` — Gets or sets the group's override control account.
- `public int ControlAccountID { get; set; }` — Gets or sets the group's override control account id.
- `public string Description { get; set; }` — Gets or sets the group description.
- `public int DiscountMatrixRow { get; set; }` — Gets or sets the group's discount matrix row.
- `public int ForeignLossAccountID { get; set; }` — Gets or sets the group's foreign loss account id.
- `public int ForeignProfitAccountID { get; set; }` — Gets or sets the group's foreign profit account id.
- `public override int ID { get; }` — Gets the internal record ID (0 for new, unsaved records).
- `public override long LongID { get; }`
- `public GLAccount TaxControlAccount { get; set; }` — Gets or sets the group's override tax control account.
- `public int TaxControlAccountID { get; set; }` — Gets or sets the group's override tax control account id.
- `public DateTime TimeStamp { get; set; }` — Gets or sets the group's modification timestamp.

## Methods (7)
- `public static int Find( string criteria )` — Finds a record's database ID.
  - param `criteria` (System.String) — Specifies the criteria as a SQL where clause.
  - returns: Type: Int32 The ID of the first record found; -1 if not record was found.
- `public static int FindByCode( string code )` — Attempts to find an AR group by its code and returns its ID.
  - param `code` (System.String) — The account code used to lookup the account.
  - returns: Type: Int32 -1 if no record was found, else the id of the first account matching the criteria supplied.
- `public static SupplierGroup Get( string criteria )` — Returns the [first] group object with the account code specified; otherwise, returns null.
  - param `criteria` (System.String) — Eg. Code like '1_B%'
  - returns: Type: SupplierGroup The record found; otherwise null
- `public static SupplierGroup GetByCode( string code )` — Returns a group object corresponding to the code specified; otherwise, returns null.
  - param `code` (System.String) — Specifies the code.
  - returns: Type: SupplierGroup The record found; otherwise null
- `public DataTable List( string criteria )` — Gets a list of database records.
  - param `criteria` (System.String) — Specifies the criteria as a SQL where clause.
  - returns: Type: DataTable Table containing selected records.
- `protected internal override void OnDelete()` — Removes the record from the database, provided it is not referenced by other records.
- `protected internal override void OnSave()` — Persists the record to the database.

# SupplierTransaction (Class)

Represents a supplier transaction.

**Namespace:** Pastel.Evolution

```csharp
public class SupplierTransaction : DrCrTransaction,
    ICloneable
```

## Constructors (2)
- `public SupplierTransaction()` — Creates a new instance of a supplier transaction.
- `public SupplierTransaction( long id )` — Creates a new instance of a supplier transaction.

## Properties (38)
- `public override AccountBase Account { get; set; }` — Gets or sets the Account to which the transaction gets posted. This is a mandatory field.
- `public override int AccountID { get; set; }` — Gets or sets the ID of the Account to which the transaction gets posted.
- `public override AllocationCollection Allocations { get; }` — Gets the transaction's allocation collection.
- `public override double Amount { get; set; }` — Gets or sets the (gross) transaction value. Negative values are allowed and will result in inverted debits and credits.
- `public override string Audit { get; }` — Gets the transaction's audit number.
- `public override Branch Branch { get; set; }`
- `public override int BranchID { get; internal set; }`
- `public override double Credit { get; set; }` — Gets the transaction's credit value, the value of which is determined by the Amount and TransactionCode properties.
- `public override Currency Currency { get; internal set; }` — Gets the foreign currency in use on this transaction, determined by the specified account. A null value indicates local currency.
- `public override int CurrencyID { get; internal set; }`
- `public override DateTime Date { get; set; }` — Gets or sets the date on which the transaction takes place. This often differs from the actual posting date but defaults to the current date.
- `public override double Debit { get; set; }` — Gets the transaction's debit value, the value of which is determined by the Amount and TransactionCode properties.
- `public override string Description { get; set; }` — Gets or sets the transaction description that - togeter with the Reference - appears on the account's statement by default. This is a mandatory field.
- `public override string ExtOrderNo { get; set; }` — Gets or sets the transaction's external order number.
- `public override double ForeignAmount { get; set; }` — Gets or sets the foreign transaction value.
- `public override double ForeignCredit { get; }` — Gets the transaction's foreign credit value, which is determined by the ForeignAmount and TransactionCode properties.
- `public override double ForeignDebit { get; }` — Gets the transaction's foreign debit value, which is determined by the ForeignAmount and TransactionCode properties.
- `public override double ForeignOutstanding { get; internal set; }` — Gets the transaction's foreign outstanding amount.
- `public override double ForeignTax { get; set; }` — Gets or sets the transaction foreign tax amount (automatically rounded to 2 decimals). Note that setting this will switch the entry mode to foreign and recalculate the Amount property.
- `public override long ID { get; }` — Gets the internal record ID (0 for new, unsaved records).
- `public override bool IsDebitPositive { get; }`
- `public override ModuleID ModID { get; set; }` — Gets or sets the transaction's evolution module id.
- `public override Module Module { get; }` — Gets the Evolution module this record belongs to, used in internal validation.
- `public override string OrderNo { get; set; }` — Gets or sets the transaction order number.
- `public override double Outstanding { get; internal set; }` — Gets the transaction's outstanding amount.
- `public override Project Project { get; set; }` — Gets or sets the Project record associated with this transaction. When using Project Tracking, this field must be specified whereverapplicable.
- `public override int ProjectID { get; set; }` — Gets or sets the ID of the Project record associated with this transaction. When using Project Tracking, this field must be specified wherever applicable.
- `public override string Reference { get; set; }` — Gets or sets the transaction reference that - together with the Description - appears on the customer statement by default. This is a mandatory field.
- `public override string Reference2 { get; set; }` — Gets or sets an additional transaction reference.
- `public override SettlementTerms SettlementTerms { get; set; }`
- `public override int SettlementTermsID { get; set; }`
- `public override SplitAllocationCollection SplitAllocations { get; }` — Gets the transaction's split allocation collection, used to split the contra account posting to various GL accounts.
- `public Supplier Supplier { get; set; }` — Gets or sets the transaction's supplier account (maps directly to Account).
- `public override double Tax { get; set; }` — Gets or sets the transaction tax amount (automatically rounded to 2 decimals).
- `public override TaxRate TaxRate { get; set; }` — Gets or sets the TaxRate record associated with this transaction. If a tax type is specified, a tax amount is automatically calculated, but can be overridden.
- `public override int TaxRateID { get; set; }`
- `public override TransactionCodeBase TransactionCode { get; set; }` — Gets or sets the TransactionCode record associated with this transaction, as maintained in Accounts Payable > Maintenance > Transaction Types. Transaction codes/types govern General Ledger integration. This is a mandatory field.
- `public override int TransactionCodeID { get; set; }` — Gets or sets the ID of the TransactionCode record associated with this transaction, which governs General Ledger integration.

## Methods (12)
- `protected void calcTaxValues()`
- `public void CalculateTax()` — Calculates the tax amount on the transaction.
- `public override Object Clone()`
  - returns: Type: Object
- `public static long Find( string criteria )` — Finds a transaction ID.
  - param `criteria` (System.String) — The criteria passed to the SQL query. Eg. Reference = 'INV001' or Description like '%Invoice%'
  - returns: Type: Int64
- `public static long Find( AccountBase account, string criteria )` — Finds a transaction ID.
  - param `account` (Pastel.Evolution.AccountBase) — The supplier account by which to filter the transaction list.
  - param `criteria` (System.String) — The criteria passed to the SQL query. Eg. Reference = 'INV001' or Description like '%Invoice%'
  - returns: Type: Int64
- `protected override double getExchangeRate()`
  - returns: Type: Double
- `public static DataTable List( string criteria )` — Returns a System.Data.DataTable object containing the database records from the PostAR table matching the supplied criteria.
  - param `criteria` (System.String) — The SQL criteria used to locate the record, e.g. Reference like '1___'
  - returns: Type: DataTable A System.Data.DataTable object containing matching records.
  - remarks: The criteria is passed to an SQL query so use the appropriate syntax. Remember to include the single quotes around string literals and append additional criteria with and .
- `public static DataTable List( AccountBase account, string criteria )` — Returns a System.Data.DataTable object containing the database records from the PostAR/PostAP table matching the supplied criteria and limited to the specified account.
  - param `account` (Pastel.Evolution.AccountBase) — The supplier account by which to filter the transaction list.
  - param `criteria` (System.String) — The SQL criteria used to locate the record, e.g. Reference like '1___'
  - returns: Type: DataTable A System.Data.DataTable object containing matching records.
  - remarks: The criteria is passed to an SQL query so use the appropriate syntax. Remember to include the single quotes around string literals and append additional criteria with and .
- `protected internal override bool OnAllowBlockedPosting()`
  - returns: Type: Boolean
- `protected internal override void OnOverrideControlAccount( GLTransaction glTran )`
  - param `glTran` (Pastel.Evolution.GLTransaction)
- `protected internal override void OnOverrideTaxControlAccount( TransactionCode tranCode, GLTransaction glTran )`
  - param `tranCode` (Pastel.Evolution.TransactionCode)
  - param `glTran` (Pastel.Evolution.GLTransaction)
- `protected override bool OnPost()`
  - returns: Type: Boolean
- `protected override void setExchangeRate( double value )`
  - param `value` (System.Double)
- `public override bool Validate()`
  - returns: Type: Boolean

# TaxRate (Class)

Represents a tax rate.

**Namespace:** Pastel.Evolution

```csharp
public class TaxRate : BranchedRecordBase
```

## Constructors (3)
- `public TaxRate()` — Creates a new instance of a tax type.
- `public TaxRate( int id )` — Creates a new instance of a tax type.
- `public TaxRate( string code )` — Creates a new instance of a tax type.

## Properties (5)
- `public string Code { get; set; }` — Gets or sets the tax type's code.
- `public string Description { get; set; }` — Gets or sets the tax type's description.
- `public override int ID { get; }` — Gets the internal record ID (0 for new, unsaved records).
- `public override long LongID { get; }`
- `public double Rate { get; set; }` — Gets or sets the tax type's rate.

## Methods (10)
- `public static DataTable _ListCurrentBranch( string criteria )`
  - param `criteria` (System.String)
  - returns: Type: DataTable
- `public static TaxRate[] _Select( string criteria )` — Experimental Method
  - param `criteria` (System.String)
  - returns: Type: TaxRate []
- `public static TaxRate[] _Select( string criteria, string sortOrder )` — Experimental Method
  - param `criteria` (System.String)
  - param `sortOrder` (System.String)
  - returns: Type: TaxRate []
- `public static int Find( string criteria )` — Finds a record's database ID.
  - param `criteria` (System.String) — Specifies the criteria as a SQL where clause.
  - returns: Type: Int32 The ID of the first record found; -1 if not record was found.
- `public static int FindByCode( string code )` — Finds the database ID of a record matching the specified code.
  - param `code` (System.String) — Specifies the code.
  - returns: Type: Int32 The ID of the first record found; -1 if not record was found.
- `public static TaxRate Get( string criteria )` — Returns an instance of the first record satisfying the criteria specified; otherwise, returns null.
  - param `criteria` (System.String) — Specifies the criteria as a SQL where clause.
  - returns: Type: TaxRate The record found; otherwise null
- `public static TaxRate GetByCode( string code )` — Returns an instance of the first record with the code specified; otherwise, returns null.
  - param `code` (System.String) — Specifies the code.
  - returns: Type: TaxRate The record found; otherwise null
- `public static DataTable List( string criteria )` — Returns a System.Data.DataTable object containing the database records from the Client table matching the supplied criteria.
  - param `criteria` (System.String) — The SQL criteria used to locate the record, e.g. Account like '1___'
  - returns: Type: DataTable A System.Data.DataTable object containing matching records.
  - remarks: The criteria is passed to an SQL query so use the appropriate syntax. Remember to includethe single quotes around string literals and append additional criteria with and.
- `public static DataTable List( string criteria, string sortOrder )` — Returns a System.Data.DataTable object containing the database records from the Client table matching the supplied criteria.
  - param `criteria` (System.String) — The SQL criteria used to locate the record, e.g. Account like '1___'
  - param `sortOrder` (System.String) — The SQL order by clause to use, e.g. DCBalance desc, Account
  - returns: Type: DataTable A System.Data.DataTable object containing matching records.
  - remarks: The criteria is passed to an SQL query so use the appropriate syntax. Remember to includethe single quotes around string literals and append additional criteria with and.
- `protected internal override void OnDelete()` — Removes the record from the database, provided it is not referenced by other records.
- `protected internal override void OnSave()` — Persists the record to the database.
- `public override string ToString()` — Gets the record's string representation.
  - returns: Type: String The object's string representation.
  - remarks: Useful while debugging.

# TransactionBase (Class)

Embodies a common Evolution transaction.

**Namespace:** Pastel.Evolution

```csharp
public abstract class TransactionBase : IBranched
```

## Properties (23)
- `public abstract AccountBase Account { get; set; }` — Gets or sets the transaction's account.
- `public abstract int AccountID { get; set; }` — Gets or sets the transaction's account id.
- `public abstract string Audit { get; }` — Gets the transaction's audit number.
- `public abstract Branch Branch { get; set; }`
- `public abstract int BranchID { get; internal set; }`
- `public abstract double Credit { get; set; }` — Gets or sets the transaction's credit value.
- `public abstract DateTime Date { get; set; }` — Gets or sets the transaction date.
- `public abstract double Debit { get; set; }` — Gets or sets the transaction's debit value.
- `public abstract string Description { get; set; }` — Gets or sets the transaction description.
- `public abstract string ExtOrderNo { get; set; }` — Gets or sets the transaction's external order number.
- `public abstract long ID { get; }` — Gets the transaction id.
- `public abstract ModuleID ModID { get; set; }` — Gets or sets the transaction's Evolution module ID.
- `public abstract Module Module { get; }` — Gets the transaction's Evolution module.
- `public abstract string OrderNo { get; set; }` — Gets or sets the transaction's order number.
- `public abstract Project Project { get; set; }` — Sets the transaction's project.
- `public abstract int ProjectID { get; set; }` — Gets or sets the transaction's project id.
- `public abstract string Reference { get; set; }` — Gets or sets the transaction reference.
- `public abstract string Reference2 { get; set; }` — Gets or sets the 2nd transaction reference.
- `public abstract double Tax { get; set; }` — Gets or sets the transaction tax amount.
- `public abstract TaxRate TaxRate { get; set; }` — Gets or sets the transaction's tax type.
- `public abstract int TaxRateID { get; set; }` — Gets or sets the transaction's tax type id.
- `public abstract TransactionCodeBase TransactionCode { get; set; }` — Gets or sets the transaction's transaction code.
- `public abstract int TransactionCodeID { get; set; }` — Gets or sets the transaction code id.

## Methods (8)
- `protected internal abstract bool OnAllowBlockedPosting()`
  - returns: Type: Boolean
- `protected abstract bool OnPost()`
  - returns: Type: Boolean
- `protected bool onPostingGLCredit( GLTransaction tran )`
  - param `tran` (Pastel.Evolution.GLTransaction)
  - returns: Type: Boolean Returns true if the transaction has already been handled.
- `protected bool onPostingGLDebit( GLTransaction tran )`
  - param `tran` (Pastel.Evolution.GLTransaction)
  - returns: Type: Boolean Returns true if the transaction has already been handled.
- `protected bool onPostingGLVat( GLTransaction tran )`
  - param `tran` (Pastel.Evolution.GLTransaction)
  - returns: Type: Boolean
- `public bool Post()` — Posts the transaction to appropriate ledgers.
  - returns: Type: Boolean
- `protected void RejectTransactionBranchAssignment()`
- `public virtual bool Validate()` — Validates the transaction.
  - returns: Type: Boolean The Validate.

## Fields (4)
- `protected double foreignOriginalTax`
- `protected bool isDebitTrans`
- `protected double originalTax`
- `protected bool readOnly`

## Events (3)
- `public event TransactionBase.GLPostingEventHandler GLCreditPosting`
- `public event TransactionBase.GLPostingEventHandler GLDebitPosting`
- `public event TransactionBase.GLPostingEventHandler GLVatPosting`

# TransactionBase.AllocationEntry (Class)

**Namespace:** Pastel.Evolution

```csharp
[ObsoleteAttribute("Use Pastel.Evolution.AllocationEntry instead.")]
    public class AllocationEntry : AllocationEntry
```

# TransactionBase.GLPostingEventArgs (Class)

**Namespace:** Pastel.Evolution

```csharp
public class GLPostingEventArgs : EventArgs
```

## Properties (2)
- `public GLTransaction GLTransaction { get; set; }`
- `public bool Posted { get; set; }`

# TransactionBase.GLPostingEventHandler (Delegate)

**Namespace:** Pastel.Evolution

```csharp
public delegate void GLPostingEventHandler(
    TransactionBase sender,
    TransactionBase.GLPostingEventArgs e
    )
```

# TransactionBase.SplitAllocation (Class)

**Namespace:** Pastel.Evolution

```csharp
[ObsoleteAttribute("Use Pastel.Evolution.SplitAllocation instead.")]
    public class SplitAllocation : SplitAllocation
```

# TransactionCode (Class)

Represents an Evolution transaction code. Transaction codes dictate the nature (debit/credit) of a transaction as well as the GL accounts to post to.

**Namespace:** Pastel.Evolution

```csharp
public class TransactionCode : TransactionCodeBase
```

## Constructors (3)
- `public TransactionCode()` — Creates a new instance of a transaction code.
- `public TransactionCode( int id )` — Creates a new instance of a transaction code.
- `public TransactionCode( Module module, string code )` — Creates a new instance of a transaction code.

## Properties (22)
- `public int Account1ID { get; set; }` — Gets or sets the transaction code's account1 id.
- `public int Account2ID { get; set; }` — Gets or sets the transaction code's account2 id.
- `public bool AllowSubAccTrans { get; set; }` — Gets or sets whether transactions to sub accounts (linked debtor accounts) are allowed when using this transaction code.
- `public override string Code { get; set; }` — Gets or sets the transaction code's code.
- `public GLAccount CreditAccount { get; }` — Gets the transaction code's credit GL account.
- `public int CreditAccountID { get; set; }` — Gets the transaction code's credit GL account id.
- `public GLAccount DebitAccount { get; }` — Gets the transaction code's debit GL account.
- `public int DebitAccountID { get; set; }` — Gets the transaction code's debit GL account id.
- `public override string Description { get; set; }` — Gets or sets the transaction code's description.
- `public bool GLPrompt { get; set; }` — Gets or sets whether or not to prompt for a GL account.
- `public override int ID { get; }` — Gets the internal record ID (0 for new, unsaved records).
- `public bool IsDebitTrans { get; set; }` — Gets or sets whether this transaction code is a debit transaction type.
- `public TransactionCode LinkedTrCode { get; }` — Gets the transaction code's linked transaction code.
- `public int LinkedTrCodeID { get; }` — Gets the transaction code's linked transaction code ID.
- `public override long LongID { get; }`
- `public Module Module { get; set; }` — Gets or sets the transaction code's Evolution module.
- `public bool Rep { get; set; }` — Gets or sets the transaction code's default representative.
- `protected internal override bool Reversed { get; set; }`
- `public bool SalesFilter { get; set; }` — Gets or sets whether this transaction is a "sales" transaction code.
- `public bool Taxable { get; set; }` — Gets or sets the transaction code's taxable status.
- `public int TaxAccountID { get; set; }` — Gets or sets the transaction code's tax account id.
- `public int TaxRateID { get; set; }` — Gets or sets the transaction code's default tax type id.

## Methods (7)
- `public static int Find( string criteria )` — Finds a record's database ID.
  - param `criteria` (System.String) — Specifies the criteria as a SQL where clause.
  - returns: Type: Int32 The ID of the first record found; -1 if not record was found.
  - remarks: WARNING: be sure to filter on both code andmodule when using this method since some transaction type codes are duplicated between modules. Using the alternative overloaded find method is highly recommended.
- `public static int Find( string criteria, Module module )` — Finds a record's database ID.
  - param `criteria` (System.String) — Specifies the criteria as a SQL where clause.
  - param `module` (Pastel.Evolution.Module) — Specifies the module.
  - returns: Type: Int32 The Find.
- `public int Find( Module module, string criteria )` — Executes the Find method.
  - param `module` (Pastel.Evolution.Module) — Specifies the module.
  - param `criteria` (System.String) — Specifies the criteria as a SQL where clause.
  - returns: Type: Int32 The Find.
- `public static int FindByCode( string code, Module module )` — Finds the database ID of a record matching the specified code.
  - param `code` (System.String) — Specifies the code.
  - param `module` (Pastel.Evolution.Module) — Specifies the module.
  - returns: Type: Int32 The ID of the first record found; -1 if not record was found.
- `public static TransactionCode Get( string criteria, Module module )` — Returns an instance of the first record satisfying the criteria specified; otherwise, returns null.
  - param `criteria` (System.String) — Specifies the criteria as a SQL where clause.
  - param `module` (Pastel.Evolution.Module) — Specifies the module.
  - returns: Type: TransactionCode The record found; otherwise null
- `public static TransactionCode GetByCode( string code, Module module )` — Returns a transaction type object corresponding to the code specified; otherwise, returns null.
  - param `code` (System.String) — Specifies the code.
  - param `module` (Pastel.Evolution.Module) — Specifies the module.
  - returns: Type: TransactionCode The ByCode.
- `public static DataTable List( string criteria )` — Gets a list of database records.
  - param `criteria` (System.String) — Specifies the criteria as a SQL where clause.
  - returns: Type: DataTable Table containing selected records.
- `public static DataTable List( string criteria, Module module )` — Executes the List method.
  - param `criteria` (System.String) — Specifies the criteria as a SQL where clause.
  - param `module` (Pastel.Evolution.Module) — Specifies the module.
  - returns: Type: DataTable The List.
- `protected internal override void OnDelete()` — Removes the record from the database, provided it is not referenced by other records.Removes the record from the database, provided it is not referenced by other records.
- `protected internal override void OnSave()` — Persists the record to the database.

# TransactionCodeBase (Class)

Embodies common Evolution transaction code functionality.

**Namespace:** Pastel.Evolution

```csharp
public abstract class TransactionCodeBase : BranchedRecordBase
```

## Properties (4)
- `public TransactionCode AsTransactionCode { get; }` — Gets the basic transaction code object (of type TransactionCodeBase), cast as a proper TransactionCode object.
- `public abstract string Code { get; set; }` — Gets or sets the transaction code's code.
- `public abstract string Description { get; set; }` — Gets or sets the transaction code's description.
- `protected internal virtual bool Reversed { get; set; }`

## Fields (1)
- `protected internal bool reversed`

# TransactionTypePostingMethodGLContextBase (Class)

**Namespace:** Pastel.Evolution

```csharp
public class TransactionTypePostingMethodGLContextBase
```

## Properties (16)
- `public virtual GLAccount COSAccount { get; set; }`
- `public virtual int COSAccountID { get; set; }`
- `public virtual GLAccount CustomerControlAccount { get; set; }`
- `public virtual int CustomerControlAccountID { get; set; }`
- `public virtual GLAccount RecoveryAccount { get; set; }`
- `public virtual int RecoveryAccountID { get; set; }`
- `public virtual GLAccount SalesAccount { get; set; }`
- `public virtual int SalesAccountID { get; set; }`
- `public virtual GLAccount StockAccount { get; set; }`
- `public virtual int StockAccountID { get; set; }`
- `public virtual GLAccount SupplierControlAccount { get; set; }`
- `public virtual int SupplierControlAccountID { get; set; }`
- `public virtual GLAccount TaxAccount { get; set; }`
- `public virtual int TaxAccountID { get; set; }`
- `public virtual GLAccount WIPAccount { get; set; }`
- `public virtual int WIPAccountID { get; set; }`

# TransactionTypePostingMethodGLContextCollection (Class)

**Namespace:** Pastel.Evolution

```csharp
public class TransactionTypePostingMethodGLContextCollection : CollectionBase
```

## Properties (1)
- `public TransactionTypePostingMethodGLContextBase this[ JobPostingMethod jobPostingMethod ] { get; }`

# Unit (Class)

Represents an inventory unit.

**Namespace:** Pastel.Evolution

```csharp
public class Unit : BranchedRecordBase
```

## Constructors (3)
- `public Unit()` — Creates a new instance of a unit.
- `public Unit( int id )` — Creates a new instance of an inventory unit.
- `public Unit( string code )` — Creates a new instance of an inventory unit.

## Properties (7)
- `public UnitCategory Category { get; set; }`
- `public int CategoryID { get; set; }`
- `public string Code { get; set; }` — Gets or sets the unit's code.
- `public UnitConversionCollection Conversions { get; }` — Gets the inventory item's unit conversions, based on the stocking unit. If a StockingUnit is not set, UnitConversions will be null.
- `public string Description { get; set; }` — Gets or sets the unit's description.
- `public override int ID { get; }` — Gets the internal record ID (0 for new, unsaved records).
- `public override long LongID { get; }`

## Methods (6)
- `public static int Find( string criteria )` — Finds an inventory unit ID.
  - param `criteria` (System.String) — The criteria passed to the SQL query. Eg. cUnitCode = '01'
  - returns: Type: Int32 The ID of the first record found; -1 if not record was found.
- `public static int FindByCode( string code )` — Attempts to find an inventory unit by using its code and returns its ID.
  - param `code` (System.String) — The code used to lookup the unit.
  - returns: Type: Int32 -1 if no record was found, else the id of the first record matching the criteria supplied.
- `public DataTable List( string criteria )` — Gets a list of database records.
  - param `criteria` (System.String) — Specifies the criteria as a SQL where clause.
  - returns: Type: DataTable Table containing selected records.
- `protected internal override void OnDelete()` — Removes the record from the database, provided it is not referenced by other records.
- `protected internal override void OnSave()` — Persists the record to the database.
- `public override string ToString()`
  - returns: Type: String

# UnitCategory (Class)

Represents an inventory group.

**Namespace:** Pastel.Evolution

```csharp
public class UnitCategory : BranchedRecordBase
```

## Constructors (3)
- `public UnitCategory()` — Creates a new instance of an inventory unit category.
- `public UnitCategory( int id )` — Creates a new instance of an inventory category.
- `public UnitCategory( string description )` — Creates a new instance of an inventory unit category.

## Properties (3)
- `public string Description { get; set; }` — Gets or sets the category description.
- `public override int ID { get; }` — Gets the internal record ID (0 for new, unsaved records).
- `public override long LongID { get; }`

## Methods (6)
- `public static int Find( string criteria )` — Finds an inventory group ID.
  - param `criteria` (System.String) — The criteria passed to the SQL query. Eg. cUnitCatDescription = 'Mass'
  - returns: Type: Int32 The ID of the first record found; -1 if not record was found.
- `public static int FindByDescription( string code )` — Attempts to find an inventory group by using its code and returns its ID.
  - param `code` (System.String) — The code used to lookup the group.
  - returns: Type: Int32 -1 if no record was found, else the id of the first record matching the criteria supplied.
- `public DataTable List( string criteria )` — Gets a list of database records.
  - param `criteria` (System.String) — Specifies the criteria as a SQL where clause.
  - returns: Type: DataTable Table containing selected records.
- `protected internal override void OnDelete()` — Removes the record from the database, provided it is not referenced by other records.
- `protected internal override void OnSave()` — Persists the record to the database.
- `public override string ToString()`
  - returns: Type: String

# UnitConversion (Class)

**Namespace:** Pastel.Evolution

```csharp
public class UnitConversion : BranchedRecordBase
```

## Constructors (2)
- `public UnitConversion( int id )` — Creates a new instance of a unit conversion.
- `public UnitConversion( int baseUnitID, int conversionUnitID )` — Creates a new instance of a unit conversion.

## Properties (8)
- `public double BaseQuantity { get; set; }`
- `public Unit BaseUnit { get; internal set; }` — Gets the base unit in the conversion.
- `public int BaseUnitID { get; set; }`
- `public double ConversionQuantity { get; set; }`
- `public Unit ConversionUnit { get; set; }`
- `public int ConversionUnitID { get; set; }`
- `public override int ID { get; }`
- `public override long LongID { get; }`

## Methods (5)
- `public static UnitConversion[] _Select( int baseUnitID )` — Experimental Method
  - param `baseUnitID` (System.Int32)
  - returns: Type: UnitConversion []
- `public static UnitConversion[] _Select( Unit baseUnit )` — Experimental Method
  - param `baseUnit` (Pastel.Evolution.Unit)
  - returns: Type: UnitConversion []
- `public static UnitConversion[] _Select( string criteria, string sortOrder )` — Experimental Method
  - param `criteria` (System.String)
  - param `sortOrder` (System.String)
  - returns: Type: UnitConversion []
- `public static int Find( string criteria )`
  - param `criteria` (System.String)
  - returns: Type: Int32
- `public static int Find( int baseUnitID, int conversionUnitID )`
  - param `baseUnitID` (System.Int32)
  - param `conversionUnitID` (System.Int32)
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

# UnitConversionCollection (Class)

Represents a collection of warehouse context records.

**Namespace:** Pastel.Evolution

```csharp
public class UnitConversionCollection : CollectionBase
```

## Properties (1)
- `Item` — Gets a delivery address by index.

## Methods (4)
- `public void Add( Unit conversionUnit, double conversionQty )`
  - param `conversionUnit` (Pastel.Evolution.Unit)
  - param `conversionQty` (System.Double)
- `public void Add( Unit conversionUnit, double baseQty, double conversionQty )`
  - param `conversionUnit` (Pastel.Evolution.Unit)
  - param `baseQty` (System.Double)
  - param `conversionQty` (System.Double)
- `public bool ConversionExists( Unit conversionUnit )` — Gets whether a conversion is configured between the current unit and the given unit.
  - param `conversionUnit` (Pastel.Evolution.Unit)
  - returns: Type: Boolean
- `public bool ConversionExists( int baseUnitID, int conversionUnitID )` — Gets whether a conversion is configured for the given units. It does not matter which unit is specified as the base.
  - param `baseUnitID` (System.Int32)
  - param `conversionUnitID` (System.Int32)
  - returns: Type: Boolean
- `public bool ConversionExists( Unit baseUnit, Unit conversionUnit )` — Gets whether a conversion is configured for the given units. It does not matter which unit is specified as the base.
  - param `baseUnit` (Pastel.Evolution.Unit)
  - param `conversionUnit` (Pastel.Evolution.Unit)
  - returns: Type: Boolean
- `public double ConvertFrom( Unit u, double quantity )` — Converts a specified quantity of specified unit to the base unit.
  - param `u` (Pastel.Evolution.Unit) — The source unit.
  - param `quantity` (System.Double) — The quantity of source unit to convert.
  - returns: Type: Double
- `public double ConvertTo( Unit u, double quantity )` — Converts a specified quantity of base unit to the specified unit.
  - param `u` (Pastel.Evolution.Unit) — The target unit.
  - param `quantity` (System.Double) — The quantity of base unit to convert.
  - returns: Type: Double

# Utils (Class)

**Namespace:** Pastel.Evolution

```csharp
public static class Utils
```

## Methods (1)
- `public static string TrimString( string value, int maxlength, bool ellipses )`
  - param `value` (System.String)
  - param `maxlength` (System.Int32)
  - param `ellipses` (System.Boolean)
  - returns: Type: String

# Utils.LimitedQueue (Class)

**Namespace:** Pastel.Evolution

```csharp
public class LimitedQueue : Queue
```

## Properties (1)
- `public int Limit { get; set; }`

## Methods (1)
- `public void Enqueue( Object item )`
  - param `item` (System.Object)

# Warehouse (Class)

Represents an inventory warehouse.

**Namespace:** Pastel.Evolution

```csharp
public class Warehouse : AccountBase
```

## Constructors (3)
- `public Warehouse()` — Creates a new instance of a warehouse.
- `public Warehouse( int id )` — Creates a new instance of a warehouse.
- `public Warehouse( string code )` — Creates a new instance of a warehouse.

## Properties (17)
- `public override bool Active { get; set; }` — Gets or sets the record's operational state.
- `public bool AddNewStock { get; set; }` — Gets or sets whether or not new items are automatically linked to this warehouse.
- `public string Address1 { get; set; }` — Gets or sets the warehouse's address line 1.
- `public string Address2 { get; set; }` — Gets or sets the warehouse's address line 2.
- `public string Address3 { get; set; }` — Gets or sets the warehouse's address line 3.
- `public override string Code { get; set; }` — Gets or sets the warehouse's code.
- `public bool DefaultWarehouse { get; }` — Gets the warehouse's default status (true for the 'master' warehouse).
- `public override string Description { get; set; }` — Gets or sets the warehouse's description.
- `public string EMailAddress { get; set; }` — Gets or sets the warehouse's email address.
- `public override int ID { get; }` — Gets the internal record ID (0 for new, unsaved records).
- `public string KnownAs { get; set; }` — Gets or sets the warehouse's common name.
- `public override long LongID { get; }`
- `public string Manager { get; set; }` — Gets or sets the warehouse manager's name.
- `public string ModemTel { get; set; }` — Gets or sets the warehouse's modem telephone number.
- `public override Module Module { get; }` — Gets the Evolution module this record forms a part of.
- `public string PostalCode { get; set; }` — Gets or sets the warehouse's postal code.
- `public string Telephone { get; set; }` — Gets or sets the warehouse's telephone number.

## Methods (11)
- `public static bool _Exists( string code )` — Experimental method.
  - param `code` (System.String)
  - returns: Type: Boolean
- `public static Warehouse[] _Select( string criteria )` — Experimental Method
  - param `criteria` (System.String)
  - returns: Type: Warehouse []
- `public static Warehouse[] _Select( string criteria, string sortOrder )` — Experimental Method
  - param `criteria` (System.String)
  - param `sortOrder` (System.String)
  - returns: Type: Warehouse []
- `public static int Find( string criteria )` — Finds and returns the ID of the first record matching the criteria supplied.
  - param `criteria` (System.String) — E.g. Code = 'abc' or Name like '%MASTER%'
  - returns: Type: Int32 The id of the record
- `public static int FindByCode( string code )` — Attempts to find a warehouse by its code and returns its ID.
  - param `code` (System.String) — The code used to lookup the warehouse.
  - returns: Type: Int32 -1 if no record was found, else the id of the first account matching the criteria supplied.
- `public static Warehouse Get( string criteria )`
  - param `criteria` (System.String) — Eg. Code = 'STO0021' or Description like '%Stone%'
  - returns: Type: Warehouse
- `public static Warehouse GetByCode( string code )` — Returns a warehouse object corresponding to the code specified; otherwise, returns null.
  - param `code` (System.String) — Specifies the code.
  - returns: Type: Warehouse The record found; otherwise null
- `public static Warehouse GetMaster()` — Returns the master warehouse.
  - returns: Type: Warehouse
- `public static DataTable List( string criteria )` — Lists warehouses for the supplied criteria.
  - param `criteria` (System.String)
  - returns: Type: DataTable
- `public static DataTable List( string criteria, string sortOrder )` — Lists warehouses for the supplied criteria.
  - param `criteria` (System.String) — The SQL criteria used to locate the record, e.g. Name like '1___'
  - param `sortOrder` (System.String) — The SQL order by clause to use, e.g. Address1 desc, Name
  - returns: Type: DataTable
- `protected internal override void OnDelete()`
- `protected internal override void OnSave()`
- `public override string ToString()`
  - returns: Type: String

# WarehouseContext (Class)

Represents an inventory item's context within a give warehouse.

**Namespace:** Pastel.Evolution

```csharp
public class WarehouseContext : BranchedRecordBase
```

**Remarks:** Inventory items are selectively linked to warehouses. The WarehouseContext class represents that link and provides access the item's quantities within the specific warehouse.

## Constructors (2)
- `public WarehouseContext( InventoryItem item, Warehouse warehouse )` — Creates a new instance of a warehouse context record.
- `public WarehouseContext( InventoryItem item, int warehouseID )` — Creates a new instance of a warehouse context record.

## Properties (25)
- `public bool AllowNegativeQty { get; }` — Gets or sets whether or not a negative stock level is allowed for the given item in the given warehouse.
- `public bool AllowNegativeStock { get; }` — Whether or not the item allows for negative stock.
- `public double AverageUnitCost { get; }` — Gets the effective unit cost applicable to this item/warehouse combination. If warehouse costing is disabled, the item's global cost will be returned.
- `public InventoryGroup Group { get; set; }` — Gets the group in this warehouse.
- `public double HighestUnitCost { get; }` — Gets the maximum reached unit cost applicable to this item/warehouse combination. If warehouse costing is disabled, the item's global cost will be returned.
- `public override int ID { get; }` — Gets the internal record ID (0 for new, unsaved records).
- `public InventoryItem InventoryItem { get; }` — Gets the object's stock item.
- `public double LatestUnitCost { get; }` — Gets the latest unit cost applicable to this item/warehouse combination. If warehouse costing is disabled, the item's global cost will be returned.
- `public override long LongID { get; }` — Transitional accessor.
- `public double LowestUnitCost { get; }` — Gets the minimum reached unit cost applicable to this item/warehouse combination. If warehouse costing is disabled, the item's global cost will be returned.
- `public double QtyFree { get; }` — Gets the item's quantity free in this warehouse.
- `public double QtyOnHand { get; }` — Gets the item's quantity on hand in this warehouse.
- `public double QtyOnPurchaseOrder { get; }` — Gets the item's quantity on purchase order in this warehouse.
- `public double QtyOnSalesOrder { get; }` — Gets the item's quantity on sales order in this warehouse.
- `public double QtyReserved { get; }` — Gets the item's quantity reserved in this warehouse.
- `public double QtyWIP { get; internal set; }` — Gets the item's work-in-progress quantity in this warehouse.
- `public SellingPriceCollection SellingPrices { get; }` — Gets the Selling Prices for the Current Warehouse.
- `public double StandardUnitCost { get; }` — Gets the standard unit cost applicable to this item/warehouse combination. If warehouse costing is disabled, the item's global cost will be returned.
- `public double UnitCost { get; }` — Gets the effective unit cost applicable to this item/warehouse combination. If warehouse costing is disabled, the item's global cost will be returned.
- `public bool UseItemDefaults { get; internal set; }` — Gets or sets whether to apply the item's defaults to this warehouse context.
- `public bool UseItemInformationDefaults { get; internal set; }` — Gets or sets whether to apply the item's information defaults to this warehouse context.
- `public bool UseItemOrderingLevels { get; internal set; }` — Gets or sets whether to apply the item's ordering levels to this warehouse context.
- `public bool UseItemPricing { get; internal set; }` — Gets or sets whether to apply the item's pricing to this warehouse context.
- `public bool UseItemSuppliers { get; internal set; }` — Gets or sets whether to apply the item's suppliers to this warehouse context.
- `public Warehouse Warehouse { get; }` — Gets the object's warehouse.

## Methods (5)
- `public static int Find( string criteria )` — Finds a record's database ID.
  - param `criteria` (System.String) — Specifies the criteria as a SQL where clause.
  - returns: Type: Int32 The ID of the first record found; -1 if not record was found.
- `public static DataTable List( string criteria )` — Gets a list of database records.
  - param `criteria` (System.String) — Specifies the criteria as a SQL where clause.
  - returns: Type: DataTable Table containing selected records.
- `protected internal override void OnDelete()` — Removes the record from the database, provided it is not referenced by other records.
- `protected internal override void OnSave()` — Persists the record to the database.
- `public void TransferStock()`

# WarehouseContextCollection (Class)

Represents a collection of warehouse context records.

**Namespace:** Pastel.Evolution

```csharp
public class WarehouseContextCollection : CollectionBase
```

## Properties (1)
- `Item` — Gets a warehouse context by warehouse ID, not by index.

## Methods (1)
- `public void Add( string whseCode )`
  - param `whseCode` (System.String)
- `public void Add( Warehouse whse )`
  - param `whse` (Pastel.Evolution.Warehouse)
- `public void Add( WarehouseContext data )`
  - param `data` (Pastel.Evolution.WarehouseContext)

# WarehouseTransfer (Class)

Represents a warehouse transfer transaction.

**Namespace:** Pastel.Evolution

```csharp
public class WarehouseTransfer
```

**Remarks:** A warehouse transfer results in two independent inventory transactions, grouped into the same audit batch. You cannot retrieve

## Properties (22)
- `public AccountBase Account { get; set; }` — Gets or sets the warehouse transfer's account (stock item).
- `public int AccountID { get; set; }` — Gets or sets the warehouse transfer's account id.
- `public string Audit { get; }` — Gets the transaction's audit number.
- `public DateTime Date { get; set; }` — Gets or sets the date on which the transfer takes place.
- `public string Description { get; set; }` — Gets or sets the warehouse transfer description.
- `public string ExtOrderNo { get; set; }` — Gets or sets the warehouse transfer's external order number, if relevant.
- `public Warehouse FromWarehouse { get; set; }` — Gets or sets the warehouse from which goods will be transferred.
- `public InventoryItem InventoryItem { get; set; }` — Gets or sets the warehouse transfer's account (stock item).
- `public Lot Lot { get; set; }`
- `public ModuleID ModID { get; }` — Gets or sets the transaction's module identifier.
- `public Module Module { get; }` — Gets the Evolution module this record forms a part of.
- `public string OrderNo { get; set; }` — Gets or sets the warehouse transfer's order number, if relevant.
- `public Project Project { set; }` — Sets the warehouse transfer's project.
- `public int ProjectID { get; set; }` — Gets or sets the warehouse transfer's project id.
- `public double Quantity { get; set; }` — Gets or sets the quantity of stock to transfer.
- `public string Reference { get; set; }` — Gets or sets the warehouse transfer's reference (compulsory).
- `public string Reference2 { get; set; }` — Gets or sets the warehouse transfer's 2nd reference.
- `public SerialNumberCollection SerialNumbers { get; }` — Gets the warehouse transfer's serial number collection.
- `public Warehouse ToWarehouse { get; set; }` — Gets or sets the warehouse to which goods will be transferred.
- `public TransactionCode TranCode { get; set; }` — Sets the warehouse transfer's transaction code.
- `public int TranCodeID { get; set; }` — Gets or sets the warehouse transfer's tran code id.
- `public double UnitCost { get; set; }` — Gets or sets the unit cost at which the transfer takes place. This typically includes the item's value in addition to a calculated transfer value.

## Methods (2)
- `public bool Post()` — Processes the transfer.
  - returns: Type: Boolean
- `public bool Validate()` — Validates the transaction without attempting to post.
  - returns: Type: Boolean The Validate.

# Worker (Class)

Represents a Worker.

**Namespace:** Pastel.Evolution

```csharp
public class Worker : AccountBase
```

## Constructors (3)
- `public Worker()` — Creates a new instance of a Worker.
- `public Worker( int id )` — Creates a new instance of a Worker.
- `public Worker( string code )` — Creates a new instance of a Worker.

## Properties (9)
- `public override bool Active { get; set; }` — Gets or sets the worker's operational state.
- `public double BillableRate { get; set; }` — Gets or sets the worker's billable rate.
- `public override string Code { get; set; }` — Gets or sets the worker's code.
- `public override string Description { get; set; }` — Gets or sets the worker's name.
- `public override int ID { get; }` — Gets the internal record ID (0 for new, unsaved records).
- `public Worker this[ string code ] { get; }` — Gets a worker object possessing the given code.
- `public override long LongID { get; }`
- `public override Module Module { get; }` — Gets the Evolution module this record belongs to, Used in internal validation.
- `public double WorkerCost { get; set; }` — Gets or sets the worker's cost.

## Methods (9)
- `public static DataTable _ListCurrentBranch( string criteria )`
  - param `criteria` (System.String)
  - returns: Type: DataTable
- `public static Worker[] _Select( string criteria )` — Experimental Method
  - param `criteria` (System.String)
  - returns: Type: Worker []
- `public static Worker[] _Select( string criteria, string sortOrder )` — Experimental Method
  - param `criteria` (System.String)
  - param `sortOrder` (System.String)
  - returns: Type: Worker []
- `public static int Find( string criteria )` — Finds a worker ID.
  - param `criteria` (System.String) — The criteria passed to the SQL query. Eg. cWorkerCode = 'WORK001' or cWorkerName like '%Worker%'
  - returns: Type: Int32
- `public static int FindByCode( string code )` — Attempts to find a worker by its code and returns its ID.
  - param `code` (System.String) — The code used to lookup the worker.
  - returns: Type: Int32 -1 if no record was found, else the id of the first worker matching the criteria supplied.
- `public static Worker Get( string criteria )` — Returns the [first] worker object matching the criteria specified; otherwise, returns null.
  - param `criteria` (System.String) — Eg. cWorkerCode = 'WORK001' or cWorkerName like '%Worker%'
  - returns: Type: Worker
- `public static Worker GetByCode( string code )` — Returns a worker object corresponding to the code specified; otherwise, returns null.
  - param `code` (System.String)
  - returns: Type: Worker
- `public static DataTable List( string criteria )` — Returns a System.Data.DataTable object containing the database records from the _etblWorkers table matching the supplied criteria.
  - param `criteria` (System.String) — The SQL criteria used to locate the record, e.g. cWorkerCode like '1___'
  - returns: Type: DataTable A System.Data.DataTable object containing matching records.
  - remarks: The criteria is passed to an SQL query so use the appropriate syntax. Remember to includethe single quotes around string literals and append additional criteria with and.
- `public static DataTable List( string criteria, string sortOrder )` — Returns a System.Data.DataTable object containing the database records from the _etblWorkers table matching the supplied criteria.
  - param `criteria` (System.String) — The SQL criteria used to locate the record, e.g. cWorkerCode like '1___'
  - param `sortOrder` (System.String) — The SQL order by clause to use, e.g. cWorkerName, cWorkerCode
  - returns: Type: DataTable A System.Data.DataTable object containing matching records.
  - remarks: The criteria is passed to an SQL query so use the appropriate syntax. Remember to includethe single quotes around string literals and append additional criteria with and.
- `protected internal override void OnDelete()` — Removes the record from the database, provided it is not referenced by other records.
- `protected internal override void OnSave()` — Persists the record to the database.

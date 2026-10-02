<!-- source: Pastel.Evolution.chm, Pastel.Evolution SDK 11.0.0.10 | verified: 2026-10-02 -->

# AccountBase (Class)

Provides basic account functionality.

**Namespace:** Pastel.Evolution

```csharp
public abstract class AccountBase : BranchedRecordBase
```

## Properties (4)
- `public abstract bool Active { get; set; }` — Gets or sets the record's state.
- `public abstract string Code { get; set; }` — Gets the internal record ID (0 for new, unsaved records).
- `public abstract string Description { get; set; }` — Gets or sets the record's description. The database field corresponding to the code is not necessarily called description .
- `public abstract Module Module { get; }` — Each module type is associated with an Evolution module.

## Methods (3)
- `protected internal override void OnDelete()`
- `protected internal override void OnSave()` — Persists the record to the database.
- `public override string ToString()`
  - returns: Type: String

# Address (Class)

Represents an address record used by various modules.

**Namespace:** Pastel.Evolution

```csharp
public class Address
```

## Constructors (4)
- `public Address()` — Creates a new instance of an address record.
- `public Address( string address )` — Creates a new instance of an address record from a multi line string.
- `public Address( string line1, string line2, string postalCode )` — Creates a new instance of an address record.
- `public Address( string line1, string line2, string line3, string line4, string line5, string postalCode )` — Creates a new instance of an address record.

## Properties (7)
- `public string Line1 { get; set; }` — Gets or sets the first line of the address.
- `public string Line2 { get; set; }` — Gets or sets the second line of the address.
- `public string Line3 { get; set; }` — Gets or sets the third line of the address.
- `public string Line4 { get; set; }` — Gets or sets the fourth line of the address.
- `public string Line5 { get; set; }` — Gets or sets the fifth line of the address.
- `public string Line6 { get; set; }` — Gets or sets the sixth line of the address.
- `public string PostalCode { get; set; }` — Gets or sets the postal code of the address.

## Methods (2)
- `public Address Condense()` — Obtains a condensed version of the current address (stripped of blank lines). Note that any changes made to the returned address will not affect the current address. Also note that the postal address will be out of place if less than 6 lines are populated.
  - returns: Type: Address
- `public override string ToString()` — Converts the address into a block-formatted string void of any blank lines in between fields.
  - returns: Type: String The formatted address.
- `public string ToString( bool compact )` — Converts the address into a block-formatted string.
  - param `compact` (System.Boolean)
  - returns: Type: String The formatted address.

# Agent (Class)

Represents an agent.

**Namespace:** Pastel.Evolution

```csharp
public class Agent : BranchedRecordBase
```

## Constructors (3)
- `public Agent()` — Creates a new instance of the Agent class.
- `public Agent( int id )` — Creates a new instance of the Agent class.
- `public Agent( string name )` — Creates a new instance of the Agent class.

## Properties (11)
- `public bool CanAssignIncidents { get; set; }` — Determines whether incidents can be assigned to this agent.
- `public bool CanSetOutOfOffice { get; set; }` — Determines whether the agent can set itself out of office.
- `public string Comments { get; set; }` — Gets or sets comments for this agent.
- `public string Description { get; set; }` — Gets or sets the agent's description.
- `public string DisplayName { get; set; }` — Gets or sets the agent's display name.
- `public string EmailAddress { get; set; }` — Gets or sets the agent's e-mail address.
- `public override int ID { get; }` — Gets the internal record ID (0 for new, unsaved records).
- `public bool IsActive { get; set; }` — Gets or sets the agent's display name.
- `public bool IsOutOfOffice { get; set; }` — Determines whether this agent is out of office.
- `public override long LongID { get; }`
- `public string Name { get; set; }` — Gets or sets the agent name.

## Methods (10)
- `public static DataTable _ListCurrentBranch( string criteria )`
  - param `criteria` (System.String)
  - returns: Type: DataTable
- `public static bool Authenticate( string agentName, string password )` — Authenticates the agent in the Evolution database.
  - param `agentName` (System.String) — Specifies the agent name.
  - param `password` (System.String) — Specifies the agent password.
  - returns: Type: Boolean True if the agent exists in the database, is active, and the password supplied is correct; false otherwise.
- `public static int Find( string criteria )` — Finds an agent account ID.
  - param `criteria` (System.String) — The criteria passed to the SQL query.
  - returns: Type: Int32 The ID of the first record found; -1 if not record was found.
- `public static int FindByName( string name )` — Attempts to find an agent by its code and returns its ID.
  - param `name` (System.String) — The name used to lookup the agent.
  - returns: Type: Int32 -1 if no record was found, else the id of the first account matching the criteria supplied.
- `public static Agent Get( string criteria )` — Returns an instance of the first record satisfying the criteria specified; otherwise, returns null.
  - param `criteria` (System.String) — The criteria passed to the SQL query.
  - returns: Type: Agent The record found; otherwise null
- `public static Agent GetByName( string name )` — Returns an instance of the first record with the code specified; otherwise, returns null.
  - param `name` (System.String) — Specifies the agent name.
  - returns: Type: Agent The record found; otherwise null
- `public static DataTable List( string criteria )` — Gets a list of database records.
  - param `criteria` (System.String) — Specifies the criteria as a SQL where clause.
  - returns: Type: DataTable Table containing selected records.
- `protected internal override void OnDelete()` — Removes the record from the database, provided it is not referenced by other records.
- `protected internal override void OnSave()` — Persists the record to the database.
- `public void SetPassword( string newPwd )` — Sets a new password for the agent.
  - param `newPwd` (System.String)
- `public void SetPassword( string newPwd, string reminder )` — Sets a new password for the agent, along with a password reminder.
  - param `newPwd` (System.String)
  - param `reminder` (System.String)

# AgentGroup (Class)

Represents an group.

**Namespace:** Pastel.Evolution

```csharp
public class AgentGroup : BranchedRecordBase
```

## Constructors (3)
- `public AgentGroup()` — Creates a new instance of the agent group class.
- `public AgentGroup( int id )` — Creates a new instance of the agent group class.
- `public AgentGroup( string name )` — Creates a new instance of the agent group class.

## Properties (4)
- `public string Description { get; set; }` — Gets or sets the group's description.
- `public override int ID { get; }` — Gets the internal record ID (0 for new, unsaved records).
- `public override long LongID { get; }`
- `public string Name { get; set; }` — Gets or sets the group name.

## Methods (7)
- `public static int Find( string criteria )` — Finds an group account ID.
  - param `criteria` (System.String) — The criteria passed to the SQL query.
  - returns: Type: Int32 The ID of the first record found; -1 if not record was found.
- `public static int FindByName( string name )` — Attempts to find an group by its code and returns its ID.
  - param `name` (System.String) — The name used to lookup the agent group.
  - returns: Type: Int32 -1 if no record was found, else the id of the first account matching the criteria supplied.
- `public static AgentGroup Get( string criteria )` — Returns an instance of the first record satisfying the criteria specified; otherwise, returns null.
  - param `criteria` (System.String) — The criteria passed to the SQL query.
  - returns: Type: AgentGroup The record found; otherwise null
- `public static AgentGroup GetByName( string name )` — Returns an instance of the first record with the code specified; otherwise, returns null.
  - param `name` (System.String) — Specifies the group name.
  - returns: Type: AgentGroup The record found; otherwise null
- `public static DataTable List( string criteria )` — Gets a list of database records.
  - param `criteria` (System.String) — Specifies the criteria as a SQL where clause.
  - returns: Type: DataTable Table containing selected records.
- `protected internal override void OnDelete()` — Removes the record from the database, provided it is not referenced by other records.
- `protected internal override void OnSave()` — Persists the record to the database.

# AgingTerm (Class)

Represents customer and supplier aging terms.

**Namespace:** Pastel.Evolution

```csharp
public class AgingTerm : BranchedRecordBase
```

## Constructors (3)
- `public AgingTerm()` — Creates a new instance of aging terms.
- `public AgingTerm( int id )` — Creates a new instance of aging terms.
- `public AgingTerm( AgingModule module, string code )` — Creates a new instance of aging terms.

## Properties (44)
- `public AgingTypeOption AgeTypeOption { get; set; }`
- `public string AgingMessage120DaysLine1 { get; set; }`
- `public string AgingMessage120DaysLine2 { get; set; }`
- `public string AgingMessage150DaysLine1 { get; set; }`
- `public string AgingMessage150DaysLine2 { get; set; }`
- `public string AgingMessage180DaysLine1 { get; set; }`
- `public string AgingMessage180DaysLine2 { get; set; }`
- `public string AgingMessage30DaysLine1 { get; set; }`
- `public string AgingMessage30DaysLine2 { get; set; }`
- `public string AgingMessage60DaysLine1 { get; set; }`
- `public string AgingMessage60DaysLine2 { get; set; }`
- `public string AgingMessage90DaysLine1 { get; set; }`
- `public string AgingMessage90DaysLine2 { get; set; }`
- `public string AgingMessageCurrentLine1 { get; set; }`
- `public string AgingMessageCurrentLine2 { get; set; }`
- `public bool AutoSetToPeriod { get; set; }`
- `public string Code { get; set; }` — Gets or sets the Aging Term code.
- `public string Description { get; set; }` — Gets or sets the aging term' description.
- `public override int ID { get; }` — Gets the internal record ID (0 for new, unsaved records).
- `public int Interval1NumberOfDays { get; set; }`
- `public int Interval2NumberOfDays { get; set; }`
- `public int Interval3NumberOfDays { get; set; }`
- `public int Interval4NumberOfDays { get; set; }`
- `public int Interval5NumberOfDays { get; set; }`
- `public int Interval6NumberOfDays { get; set; }`
- `public int Interval7NumberOfDays { get; set; }`
- `public override long LongID { get; }`
- `public AgingModule Module { get; set; }`
- `public DateTime StatementCloseDate120Days { get; set; }`
- `public DateTime StatementCloseDate150Days { get; set; }`
- `public DateTime StatementCloseDate180Days { get; set; }`
- `public DateTime StatementCloseDate30Days { get; set; }`
- `public DateTime StatementCloseDate60Days { get; set; }`
- `public DateTime StatementCloseDate90Days { get; set; }`
- `public DateTime StatementCloseDateCurrent { get; set; }`
- `public string TermDescription120Days { get; set; }`
- `public string TermDescription150Days { get; set; }`
- `public string TermDescription180Days { get; set; }`
- `public string TermDescription30Days { get; set; }`
- `public string TermDescription60Days { get; set; }`
- `public string TermDescription90Days { get; set; }`
- `public string TermDescriptionCurrent { get; set; }`
- `public AgingIntervalOption TermDescriptionOption { get; set; }`
- `public AgingIntervalOption TermIntervalOption { get; set; }`

## Methods (7)
- `public static int Find( string criteria )` — Finds an aging terms record ID.
  - param `criteria` (System.String) — The criteria passed to the SQL query. Eg. cCode = 'MNTH-STMT' or cDescription like '%Internal%'
  - returns: Type: Int32 The ID of the first record found; -1 if not record was found.
- `public static int Find( string criteria, AgingModule module )` — Finds a record's database ID.
  - param `criteria` (System.String) — Specifies the criteria as a SQL where clause.
  - param `module` (Pastel.Evolution.AgingModule) — Specifies the module.
  - returns: Type: Int32 The Find.
- `public static int FindByCode( AgingModule module, string code )` — Attempts to find aging terms by its code and returns its ID.
  - param `module` (Pastel.Evolution.AgingModule)
  - param `code` (System.String) — The code used to lookup the aging terms.
  - returns: Type: Int32 -1 if no record was found, else the id of the first account matching the criteria supplied.
- `public static AgingTerm Get( string criteria )` — Returns an instance of the first record satisfying the criteria specified; otherwise, returns null.
  - param `criteria` (System.String) — The criteria passed to the SQL query. Eg. cCode = 'MNTH-STMT' or cDescription like '%Internal%'
  - returns: Type: AgingTerm The record found; otherwise null
- `public static AgingTerm GetByCode( AgingModule module, string code )` — Returns an instance of the first record with the code specified; otherwise, returns null.
  - param `module` (Pastel.Evolution.AgingModule)
  - param `code` (System.String) — Specifies the code.
  - returns: Type: AgingTerm The record found; otherwise null
- `public static DataTable List( string criteria )` — Gets a list of database records.
  - param `criteria` (System.String) — Specifies the criteria as a SQL where clause.
  - returns: Type: DataTable Table containing selected records.
- `public static DataTable List( string criteria, AgingModule module )` — Executes the List method.
  - param `criteria` (System.String) — Specifies the criteria as a SQL where clause.
  - param `module` (Pastel.Evolution.AgingModule) — Specifies the module.
  - returns: Type: DataTable The List.
- `protected internal override void OnDelete()` — Removes the record from the database, provided it is not referenced by other records.
- `protected internal override void OnSave()` — Persists the record to the database.

# AllocationCollection (Class)

**Namespace:** Pastel.Evolution

```csharp
public class AllocationCollection : CollectionBase
```

## Properties (3)
- `public AllocationEntry this[ int index ] { get; }`
- `public double TotalAllocation { get; }` — Gets the total allocated value of the collection.
- `public double TotalForeignAllocation { get; }` — Gets the foreign total allocated value of the collection.

## Methods (5)
- `public AllocationEntry Add( AllocationEntry allocation )` — Adds a transaction to the allocation collection.
  - param `allocation` (Pastel.Evolution.AllocationEntry) — The allocation entry to add to the collection.
  - returns: Type: AllocationEntry
- `public AllocationEntry Add( DrCrTransaction transaction )` — Adds a transaction to the allocation collection, allocating the maximum value possible.
  - param `transaction` (Pastel.Evolution.DrCrTransaction) — The transaction to add to the collection.
  - returns: Type: AllocationEntry
  - remarks: If the maximum allocable amount is zero, the standard exception will be raised.
- `public AllocationEntry Add( DrCrTransaction transaction, double amount )` — Adds a transaction to the allocation collection, allocating the value specified.
  - param `transaction` (Pastel.Evolution.DrCrTransaction) — The transaction to add to the collection.
  - param `amount` (System.Double) — The allocation value (foreign currency value if foreign currencies are being allocated).
  - returns: Type: AllocationEntry
- `public AllocationEntry Add( DrCrTransaction transaction, double amount, DateTime balancingDate, string balancingReference, string balancingDescription )` — Adds a transaction to the allocation collection, allocating the value specified.
  - param `transaction` (Pastel.Evolution.DrCrTransaction) — The transaction to add to the collection.
  - param `amount` (System.Double) — The allocation value (foreign currency value if foreign currencies are being allocated).
  - param `balancingDate` (System.DateTime)
  - param `balancingReference` (System.String)
  - param `balancingDescription` (System.String)
  - returns: Type: AllocationEntry
- `protected override void OnClear()`
- `public void Remove( AllocationEntry allocation )` — Removes a transaction allocation, effectively unallocating it.
  - param `allocation` (Pastel.Evolution.AllocationEntry)
- `public void Remove( DrCrTransaction tran )` — Removes a transaction allocation, effectively unallocating it.
  - param `tran` (Pastel.Evolution.DrCrTransaction)
- `public void RemoveAt( int index )` — Removes an allocation from a specific index.
  - param `index` (System.Int32)
- `public void Save()` — Saves the transaction's allocations back to the database, whilst also updating any referenced transactions.

# AllocationEntry (Class)

**Namespace:** Pastel.Evolution

```csharp
public class AllocationEntry
```

## Constructors (2)
- `public AllocationEntry()` — Initializes a new instance of the AllocationEntry class
- `public AllocationEntry( DrCrTransaction transaction, double amount )` — Initializes a new instance of the AllocationEntry class

## Properties (10)
- `public bool AllowRemove { get; internal set; }`
- `public double Amount { get; internal set; }` — Gets the allocation value.
- `public string BalancingDescription { get; set; }`
- `public string BalancingReference { get; set; }`
- `public DrCrTransaction BalancingTransaction { get; internal set; }` — Represents the balancing transaction linked to this allocation. After saving of allocations, it will exist on whichever transaction it relates to and not necessarily the current allocation collection.
- `public long BalancingTransactionID { get; internal set; }` — Gets the ID of the balancing transaction.
- `public DateTime Date { get; internal set; }` — Gets the allocation date.
- `public double ForeignAmount { get; internal set; }` — Gets the foreign allocation value.
- `public DrCrTransaction Transaction { get; internal set; }` — Gets the allocated transaction.
- `public long TransactionID { get; internal set; }` — Gets the ID of the allocated transaction.

# Area (Class)

Represents a geographical area to which accounts can be linked.

**Namespace:** Pastel.Evolution

```csharp
public class Area : BranchedRecordBase
```

## Constructors (3)
- `public Area()` — Creates a new instance of the Area class.
- `public Area( int id )` — Creates a new instance of an existing Area record.
- `public Area( string code )` — Creates a new instance of the Area class.

## Properties (4)
- `public string Code { get; set; }`
- `public string Description { get; set; }` — Gets or sets the area description.
- `public override int ID { get; }` — Gets the internal record ID (0 for new, unsaved records).
- `public override long LongID { get; }`

## Methods (5)
- `public static int Find( string criteria )` — Finds the ID of an existing area.
  - param `criteria` (System.String) — Specifies the criteria as a SQL where clause.
  - returns: Type: Int32 The ID of the first record found; -1 if not record was found.
- `public static int FindByCode( string code )`
  - param `code` (System.String)
  - returns: Type: Int32
- `public DataTable List( string criteria )` — Gets a list of database records.
  - param `criteria` (System.String) — Specifies the criteria as a SQL where clause.
  - returns: Type: DataTable Table containing selected records.
- `protected internal override void OnDelete()` — Removes the record from the database, provided it is not referenced by other records.
- `protected internal override void OnSave()` — Persists the record to the database.

# Bank (Class)

Represents a bank record.

**Namespace:** Pastel.Evolution

```csharp
public class Bank : BranchedRecordBase
```

## Constructors (3)
- `public Bank()` — Creates a new instance of the Bank class.
- `public Bank( int id )` — Creates a new instance of the Bank class.
- `public Bank( string code )` — Creates a new instance of the Bank class.

## Properties (5)
- `public bool Active { get; set; }` — Gets or sets the bank's state.
- `public string BranchCode { get; set; }` — Gets or sets the branch code.
- `public override int ID { get; }` — Gets the internal record ID (0 for new, unsaved records).
- `public override long LongID { get; }`
- `public string Name { get; set; }` — Gets or sets the bank name.

## Methods (4)
- `public static int Find( string criteria )` — Returns the id of the first record found matching the criteria. Eg. BankName = 'abc'
  - param `criteria` (System.String)
  - returns: Type: Int32 ID of the record found; if not found, -1
- `public static DataTable List( string criteria )` — Gets a list of database records.
  - param `criteria` (System.String) — Specifies the criteria in SQL format.
  - returns: Type: DataTable Table containing selected records.
- `protected internal override void OnDelete()` — Removes the record from the database, provided it is not referenced by other records.
- `protected internal override void OnSave()` — Persists the record to the database.

# Branch (Class)

Represents a bank record.

**Namespace:** Pastel.Evolution

```csharp
public class Branch : RecordBase
```

## Constructors (3)
- `public Branch()` — Initializes a new instance of the Branch class
- `public Branch( int id )` — Creates a new instance of the Branch class.
- `public Branch( string code )` — Initializes a new instance of the Branch class

## Properties (7)
- `public bool Active { get; set; }` — Gets or sets the bank's state.
- `public string Code { get; set; }` — Gets or sets the branch code.
- `public string Description { get; set; }` — Gets or sets the bank name.
- `public static Branch Global { get; internal set; }`
- `public override int ID { get; }` — Gets the internal record ID (0 for new, unsaved records).
- `public bool IsGlobal { get; private set; }`
- `public override long LongID { get; }`

## Methods (7)
- `public static Branch[] _Select( string criteria )` — Experimental Method
  - param `criteria` (System.String)
  - returns: Type: Branch []
- `public static Branch[] _Select( string criteria, string sortOrder, bool includeGlobal )` — Experimental Method
  - param `criteria` (System.String)
  - param `sortOrder` (System.String)
  - param `includeGlobal` (System.Boolean)
  - returns: Type: Branch []
- `public static int Find( string criteria )` — Returns the id of the first record found matching specified criteria. Eg. cBranchDescription = 'abc'
  - param `criteria` (System.String)
  - returns: Type: Int32 ID of the record found; if not found, -1
- `public static int FindByCode( string code )`
  - param `code` (System.String)
  - returns: Type: Int32
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
- `public override string ToString()`
  - returns: Type: String

## Fields (1)
- `public const int GLOBAL_BRANCH_ID`

# BranchedRecordBase (Class)

**Namespace:** Pastel.Evolution

```csharp
public abstract class BranchedRecordBase : RecordBase,
    IBranched
```

## Properties (2)
- `public Branch Branch { get; set; }`
- `public int BranchID { get; set; }` — Gets the record's branch ID.

## Methods (2)
- `protected void ValidateBranchRelation( BranchedRecordBase category )`
  - param `category` (Pastel.Evolution.BranchedRecordBase)
- `protected void ValidateSetBranch( Branch value )`
  - param `value` (Pastel.Evolution.Branch)

## Fields (1)
- `protected Branch branch`

# BusinessClass (Class)

Represents a business classification which can be assigned to accounts.

**Namespace:** Pastel.Evolution

```csharp
public class BusinessClass : BranchedRecordBase
```

## Constructors (3)
- `public BusinessClass()` — Creates a new instance of a business category.
- `public BusinessClass( int id )` — Creates a new instance of a business category.
- `public BusinessClass( string name )` — Creates a new instance of a business category.

## Properties (3)
- `public override int ID { get; }` — Gets the internal record ID (0 for new, unsaved records).
- `public override long LongID { get; }`
- `public string Type { get; set; }` — Gets or sets the business class' type.

## Methods (4)
- `public static int Find( string criteria )` — Finds a record's database ID.
  - param `criteria` (System.String) — Specifies the criteria as a SQL where clause.
  - returns: Type: Int32 The ID of the first record found; -1 if not record was found.
- `public DataTable List( string criteria )` — Gets a list of database records.
  - param `criteria` (System.String) — Specifies the SQL criteria.
  - returns: Type: DataTable Table containing selected records.
- `protected internal override void OnDelete()` — Removes the record from the database, provided it is not referenced by other records.
- `protected internal override void OnSave()` — Persists the record to the database.

# BusinessType (Class)

Represents a business/industry type which can be assigned to accounts.

**Namespace:** Pastel.Evolution

```csharp
public class BusinessType : BranchedRecordBase
```

## Constructors (3)
- `public BusinessType()` — Creates a new instance of a business type.
- `public BusinessType( int id )` — Creates a new instance of a business type.
- `public BusinessType( string type )` — Creates a new instance of a business type.

## Properties (3)
- `public override int ID { get; }` — Gets the internal record ID (0 for new, unsaved records).
- `public override long LongID { get; }`
- `public string Type { get; set; }` — Gets or sets the type description.

## Methods (4)
- `public static int Find( string criteria )` — Finds a record's database ID.
  - param `criteria` (System.String) — Specifies the criteria as a SQL where clause.
  - returns: Type: Int32 The ID of the first record found; -1 if not record was found.
- `public DataTable List( string criteria )` — Gets a list of database records.
  - param `criteria` (System.String) — Specifies the criteria as a SQL where clause.
  - returns: Type: DataTable Table containing selected records.
- `protected internal override void OnDelete()` — Removes the record from the database, provided it is not referenced by other records.
- `protected internal override void OnSave()` — Persists the record to the database.

# CashbookBatch (Class)

**Namespace:** Pastel.Evolution

```csharp
public class CashbookBatch : BranchedRecordBase
```

## Constructors (3)
- `public CashbookBatch()` — Creates a new instance of a cashbook batch.
- `public CashbookBatch( int id )` — Creates a new instance of a general ledger cashbook batch.
- `public CashbookBatch( string code )` — Creates a new instance of a general ledger cashbook batch.

## Properties (28)
- `public GLAccount AccountsPayableAccount { get; set; }` — Gets or sets the cashbook batch integration accounts payable account.
- `public int AccountsPayableAccountID { get; set; }`
- `public GLAccount AccountsReceivableAccount { get; set; }` — Gets or sets the cashbook batch integration accounts receivable account.
- `public int AccountsReceivableAccountID { get; set; }`
- `public bool AllowAccountsPayablePosting { get; set; }` — Gets or sets the cashbook batch to allow accounts payable module posting.
- `public bool AllowAccountsReceivablePosting { get; set; }` — Gets or sets the cashbook batch to allow accounts receivable module posting.
- `public bool AllowGeneralLedgerPosting { get; set; }` — Gets or sets the cashbook batch to allow general ledger module posting.
- `public GLAccount BankAccount { get; set; }` — Gets or sets the cashbook batch integration bank account.
- `public int BankAccountID { get; set; }`
- `public string Code { get; set; }` — Gets or sets the cashbook batch number.
- `public string DefaultDescription { get; set; }` — Gets or sets the new line default description.
- `public string DefaultReference { get; set; }` — Gets or sets the new line default reference.
- `public string Description { get; set; }` — Gets or sets the cashbook batch description.
- `public CashbookBatchDetailCollection Detail { get; }`
- `public bool DoClearAfterPost { get; set; }` — Gets or sets the cashbook batch clear after post.
- `public override int ID { get; }`
- `public bool IncludeInBankRecon { get; set; }` — Gets or sets the cashbook batch to appear in bank reconciliation.
- `public bool IsLoading { get; internal set; }` — Will be true while the cashbook is busy loading detail.
- `public override long LongID { get; }`
- `public Agent Owner { get; set; }` — Gets or sets the batch owner.
- `public int OwnerID { get; set; }` — Gets or sets the Agent ID of the batch owner.
- `public int ProcessedCount { get; }` — Gets or sets the cashbook batch processed count.
- `public string Reference { get; internal set; }` — Gets or sets the cashbook batch reference.
- `public int RepeatLimit { get; set; }` — Gets or sets the cashbook batch repeat limit.
- `public GLAccount TaxAccount { get; set; }` — Gets or sets the cashbook batch integration tax account.
- `public int TaxAccountID { get; set; }`
- `public TransactionCode TransactionCode { get; set; }` — Gets or sets the cashbook batch transaction code.
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

# CashbookBatchDetail (Class)

**Namespace:** Pastel.Evolution

```csharp
public class CashbookBatchDetail : BranchedRecordBase
```

## Constructors (2)
- `public CashbookBatchDetail()` — Creates a new instance of a cashbook batch detail record.
- `public CashbookBatchDetail( int id )` — Creates a new instance of a journal batch detail record.

## Properties (33)
- `public AccountBase Account { get; set; }`
- `public double Credit { get; set; }`
- `public Currency Currency { get; }` — Gets the record currency.
- `public Customer Customer { get; set; }` — Gets or sets the line's customer. Maps directly to the Account property but null if invalid.
- `public int CustomerID { get; set; }` — Gets or sets the customer id.
- `public DateTime Date { get; set; }`
- `public double Debit { get; set; }` — Sets the transaction debit amount.
- `public string Description { get; set; }` — Gets or sets the record description.
- `public double EffectiveCredit { get; set; }`
- `public double EffectiveDebit { get; set; }`
- `public double ExchangeRate { get; set; }` — Gets or sets the applicable exchange rate, expressed as [home currency]/[foreign currency]. Defaults to applicable exchange rate for the transaction date.
- `public double ForeignTax { get; set; }` — Gets or sets the foreign tax amount (automatically rounded to 2 decimals and always posted positive).
- `public int GLAccountID { get; set; }` — Gets or sets the tax account ID.
- `public override int ID { get; }`
- `public bool IsLoading { get; set; }`
- `public CashbookBatchDetail.Module LineModule { get; set; }`
- `public override long LongID { get; }`
- `public bool PostDated { get; set; }` — Gets or sets if the record is post dated
- `public Project Project { get; set; }` — Gets or sets the Project.
- `public int ProjectID { get; set; }` — Gets or sets the Project ID.
- `public bool Reconcile { get; set; }` — Gets or sets if the record is reconciled or not.
- `public string Reference { get; set; }`
- `public SalesRepresentative SalesRepresentative { get; set; }` — Gets or sets the record sales representative
- `public int SalesRepresentativeID { get; set; }` — Gets or sets the sales representative ID.
- `public int SplitGroup { get; internal set; }` — Gets the record Split Group
- `public CashbookBatchSplitCollection SplitLines { get; }`
- `public CashbookBatchDetail.SplitLineType SplitType { get; internal set; }`
- `public Supplier Supplier { get; set; }` — Gets or sets the line's supplier. Maps directly to the Account property but null if invalid.
- `public int SupplierID { get; set; }` — Gets or sets the supplier id.
- `public double Tax { get; set; }` — Gets or sets the transaction tax amount (automatically rounded to 2 decimals and always posted positive).
- `public GLAccount TaxAccount { get; set; }` — Gets or sets the tax account.
- `public int TaxRateID { get; set; }` — Gets or sets the TaxRate ID.
- `public TaxRate TaxType { get; set; }` — Gets or sets the TaxRate.

## Methods (8)
- `protected void calcTaxValues()`
- `public CashbookBatchDetail Clone()`
  - returns: Type: CashbookBatchDetail
- `public static int Find( string criteria )`
  - param `criteria` (System.String)
  - returns: Type: Int32
- `protected double getExchangeRate()`
  - returns: Type: Double
- `public static DataTable List( string criteria )`
  - param `criteria` (System.String)
  - returns: Type: DataTable
- `protected internal override void OnDelete()`
- `protected internal override void OnSave()` — Persists the record to the database.
- `protected void setExchangeRate( double value )`
  - param `value` (System.Double)

## Fields (9)
- `protected double amount`
- `protected double discAmount`
- `protected double discTax`
- `protected double exchange`
- `protected internal Utils.LimitedQueue fcDiscountQueue`
- `protected internal Utils.LimitedQueue fcQueue`
- `protected double foreignAmount`
- `protected double foreignOriginalTax`
- `protected double originalTax`

# CashbookBatchDetailCollection (Class)

Represents a collection of cashbook batch detail items, typically owned by a given inventory document record.

**Namespace:** Pastel.Evolution

```csharp
public class CashbookBatchDetailCollection : CollectionBase
```

## Properties (1)
- `public CashbookBatchDetail this[ int index ] { get; set; }` — Gets a batch detail object by its zero-based index.

## Methods (4)
- `public void Add( CashbookBatchDetail detailRecord )` — Appends a batch detail object to the batch.
  - param `detailRecord` (Pastel.Evolution.CashbookBatchDetail)
  - remarks: Take note that upon being added to a document, the detail record will assume the document's sales representative and project.
- `public void OnCollectionChanged( CashbookBatchDetailCollection.CashbookBatchDetailCollectionChangedEventArgs e )`
  - param `e` (Pastel.Evolution.CashbookBatchDetailCollection.CashbookBatchDetailCollectionChangedEventArgs)
- `public void Remove( CashbookBatchDetail detailRecord )` — Removes the specified order detail line from the collection
  - param `detailRecord` (Pastel.Evolution.CashbookBatchDetail)
- `public void RemoveAt( int index )` — Removes a detail record using its zero-based index.
  - param `index` (System.Int32)

## Events (1)
- `public event CashbookBatchDetailCollection.CashbookBatchDetailChangedEventHandler CollectionChanged` — Occurs when detail records are added or deleted.

# CashbookBatchDetailCollection.CashbookBatchDetailChangedEventHandler (Delegate)

**Namespace:** Pastel.Evolution

```csharp
public delegate void CashbookBatchDetailChangedEventHandler(
    Object sender,
    CashbookBatchDetailCollection.CashbookBatchDetailCollectionChangedEventArgs e
    )
```

# CashbookBatchDetailCollection.CashbookBatchDetailCollectionChangedEventArgs (Class)

**Namespace:** Pastel.Evolution

```csharp
public class CashbookBatchDetailCollectionChangedEventArgs : EventArgs
```

## Fields (2)
- `public CashbookBatchDetailCollection.CashbookBatchDetailChangeAction Action`
- `public CashbookBatchDetail DetailRecord`

# CashbookBatchSplitCollection (Class)

Represents a collection of cashbook batch detail items, typically owned by a given inventory document record.

**Namespace:** Pastel.Evolution

```csharp
public class CashbookBatchSplitCollection : CollectionBase
```

## Properties (1)
- `public CashbookBatchDetail this[ int index ] { get; set; }` — Gets a batch detail object by its zero-based index.

## Methods (4)
- `public void Add( CashbookBatchDetail detailRecord )` — Appends a batch detail object to the batch.
  - param `detailRecord` (Pastel.Evolution.CashbookBatchDetail)
  - remarks: Take note that upon being added to a document, the detail record will assume the document's sales representative and project.
- `public void OnCollectionChanged( CashbookBatchSplitCollection.CashbookBatchDetailCollectionChangedEventArgs e )`
  - param `e` (Pastel.Evolution.CashbookBatchSplitCollection.CashbookBatchDetailCollectionChangedEventArgs)
- `public void Remove( CashbookBatchDetail detailRecord )` — Removes the specified order detail line from the collection
  - param `detailRecord` (Pastel.Evolution.CashbookBatchDetail)
- `public void RemoveAt( int index )` — Removes a detail record using its zero-based index.
  - param `index` (System.Int32)

## Events (1)
- `public event CashbookBatchSplitCollection.CashbookBatchDetailChangedEventHandler CollectionChanged` — Occurs when detail records are added or deleted.

# CashbookBatchSplitCollection.CashbookBatchDetailChangedEventHandler (Delegate)

**Namespace:** Pastel.Evolution

```csharp
public delegate void CashbookBatchDetailChangedEventHandler(
    Object sender,
    CashbookBatchSplitCollection.CashbookBatchDetailCollectionChangedEventArgs e
    )
```

# CashbookBatchSplitCollection.CashbookBatchDetailCollectionChangedEventArgs (Class)

**Namespace:** Pastel.Evolution

```csharp
public class CashbookBatchDetailCollectionChangedEventArgs : EventArgs
```

## Fields (2)
- `public CashbookBatchSplitCollection.CashbookBatchDetailChangeAction Action`
- `public CashbookBatchDetail DetailRecord`

# ComHelper (Class)

Provides various functions for overcoming the limitations of accessing the API via COM. This class gets extended as required.

**Namespace:** Pastel.Evolution

```csharp
public class ComHelper
```

## Properties (5)
- `public string AssemblyVersion { get; }`
- `public string CompatibleEvolutionDatabaseVersion { get; }`
- `public string CurrentEvolutionDatabaseVersion { get; }`
- `public DateTime RegistrationExpiryDate { get; }`
- `[ObsoleteAttribute("No longer registered")] public int RmsUsers { get; }`

## Methods (72)
- `public Address Address( string line1, string line2, string line3, string line4, string line5, string postalCode )`
  - param `line1` (System.String)
  - param `line2` (System.String)
  - param `line3` (System.String)
  - param `line4` (System.String)
  - param `line5` (System.String)
  - param `postalCode` (System.String)
  - returns: Type: Address
- `public bool AuthenticateAgent( string agentName, string password )`
  - param `agentName` (System.String)
  - param `password` (System.String)
  - returns: Type: Boolean
- `public void BeginTran()`
- `public void CommitTran()`
- `public string CompleteDocumentWithCustomReference( OrderBase document, string reference )`
  - param `document` (Pastel.Evolution.OrderBase)
  - param `reference` (System.String)
  - returns: Type: String
- `public void CreateCommonDBConnection( string connectionString )`
  - param `connectionString` (System.String)
- `public void CreateConnection( string connectionString )`
  - param `connectionString` (System.String)
- `public int FindAgent( string criteria )`
  - param `criteria` (System.String)
  - returns: Type: Int32
- `public int FindAgentByNAme( string name )`
  - param `name` (System.String)
  - returns: Type: Int32
- `public int FindAPAccount( string criteria )`
  - param `criteria` (System.String)
  - returns: Type: Int32
- `public int FindAPAccountByCode( string code )`
  - param `code` (System.String)
  - returns: Type: Int32
- `public int FindARAccount( string criteria )`
  - param `criteria` (System.String)
  - returns: Type: Int32
- `public int FindARAccountByCode( string code )`
  - param `code` (System.String)
  - returns: Type: Int32
- `public int FindGLAccount( string criteria )`
  - param `criteria` (System.String)
  - returns: Type: Int32
- `public int FindGLAccountByCode( string code )`
  - param `code` (System.String)
  - returns: Type: Int32
- `public int FindIncident( string criteria )`
  - param `criteria` (System.String)
  - returns: Type: Int32
- `public int FindIncidentCategory( string criteria )`
  - param `criteria` (System.String)
  - returns: Type: Int32
- `public int FindIncidentCategoryByDescription( string description )`
  - param `description` (System.String)
  - returns: Type: Int32
- `public int FindInventoryDocument( DocumentType docType, string criteria )`
  - param `docType` (Pastel.Evolution.DocumentType)
  - param `criteria` (System.String)
  - returns: Type: Int32
- `public int FindJobCard( string criteria )`
  - param `criteria` (System.String)
  - returns: Type: Int32
- `public int FindJobCardByCode( string code )`
  - param `code` (System.String)
  - returns: Type: Int32
- `public int FindPriority( string criteria )`
  - param `criteria` (System.String)
  - returns: Type: Int32
- `public int FindProject( string criteria )`
  - param `criteria` (System.String)
  - returns: Type: Int32
- `public int FindProjectByCode( string code )`
  - param `code` (System.String)
  - returns: Type: Int32
- `public int FindSalesRepresentative( string criteria )`
  - param `criteria` (System.String)
  - returns: Type: Int32
- `public int FindSalesRepresentativeByCode( string code )`
  - param `code` (System.String)
  - returns: Type: Int32
- `public int FindStockItem( string criteria )`
  - param `criteria` (System.String)
  - returns: Type: Int32
- `public int FindStockItemByCode( string code )`
  - param `code` (System.String)
  - returns: Type: Int32
- `public int FindUnit( string criteria )`
  - param `criteria` (System.String)
  - returns: Type: Int32
- `public int FindUnitCategory( string criteria )`
  - param `criteria` (System.String)
  - returns: Type: Int32
- `public Agent GetAgentByName( string name )`
  - param `name` (System.String)
  - returns: Type: Agent
- `public Supplier GetAPAccount( string code )`
  - param `code` (System.String)
  - returns: Type: Supplier
- `public SupplierTransaction GetAPTransaction( int id )`
  - param `id` (System.Int32)
  - returns: Type: SupplierTransaction
- `public string GetAPTransactionsAsXml( Supplier account, string criteria )`
  - param `account` (Pastel.Evolution.Supplier)
  - param `criteria` (System.String)
  - returns: Type: String
- `public Customer GetARAccount( string code )`
  - param `code` (System.String)
  - returns: Type: Customer
- `public CustomerTransaction GetARTransaction( int id )`
  - param `id` (System.Int32)
  - returns: Type: CustomerTransaction
- `public string GetARTransactionsAsXml( Customer account, string criteria )`
  - param `account` (Pastel.Evolution.Customer)
  - param `criteria` (System.String)
  - returns: Type: String
- `public GLAccount GetGLAccount( string code )`
  - param `code` (System.String)
  - returns: Type: GLAccount
- `public GLTransaction GetGLTransaction( int id )`
  - param `id` (System.Int32)
  - returns: Type: GLTransaction
- `public string GetGLTransactionsAsXml( GLAccount account, string criteria )`
  - param `account` (Pastel.Evolution.GLAccount)
  - param `criteria` (System.String)
  - returns: Type: String
- `public Incident GetIncidentByCode( string reference )`
  - param `reference` (System.String)
  - returns: Type: Incident
- `public IncidentCategory GetIncidentCategoryByDescription( string description )`
  - param `description` (System.String)
  - returns: Type: IncidentCategory
- `public IncidentType GetIncidentTypeByDescription( string description )`
  - param `description` (System.String)
  - returns: Type: IncidentType
- `public JobCard GetJobCard( string code )`
  - param `code` (System.String)
  - returns: Type: JobCard
- `public JobTransactionCode GetJobTransactionCode( JobDetail.TransactionSource tranSource, string code )`
  - param `tranSource` (Pastel.Evolution.JobDetail.TransactionSource)
  - param `code` (System.String)
  - returns: Type: JobTransactionCode
- `public Lot GetLotByCode( InventoryItem inventoryItem, string code )`
  - param `inventoryItem` (Pastel.Evolution.InventoryItem)
  - param `code` (System.String)
  - returns: Type: Lot
- `public Priority GetPriorityByDescription( string description )`
  - param `description` (System.String)
  - returns: Type: Priority
- `public Project GetProjectByCode( string code )`
  - param `code` (System.String)
  - returns: Type: Project
- `public PurchaseOrder GetPurchaseOrder( string orderNumber )`
  - param `orderNumber` (System.String)
  - returns: Type: PurchaseOrder
- `public SalesOrder GetSalesOrder( string orderNumber )`
  - param `orderNumber` (System.String)
  - returns: Type: SalesOrder
- `public SalesRepresentative GetSalesRepresentative( string code )`
  - param `code` (System.String)
  - returns: Type: SalesRepresentative
- `public InventoryItem GetStockItem( string code )`
  - param `code` (System.String)
  - returns: Type: InventoryItem
- `public PurchaseOrder GetSupplierInvoice( string orderNumber, string grvNumber )`
  - param `orderNumber` (System.String)
  - param `grvNumber` (System.String)
  - returns: Type: PurchaseOrder
- `public TaxRate GetTaxRate( string code )`
  - param `code` (System.String)
  - returns: Type: TaxRate
- `public TransactionCodeBase GetTransactionCode( Module module, string code )`
  - param `module` (Pastel.Evolution.Module)
  - param `code` (System.String)
  - returns: Type: TransactionCodeBase
- `public Unit GetUnitByCode( string code )`
  - param `code` (System.String)
  - returns: Type: Unit
- `public Unit GetUnitByID( int id )`
  - param `id` (System.Int32)
  - returns: Type: Unit
- `public UnitCategory GetUnitCategoryByCode( string code )`
  - param `code` (System.String)
  - returns: Type: UnitCategory
- `public UnitCategory GetUnitCategoryByID( int id )`
  - param `id` (System.Int32)
  - returns: Type: UnitCategory
- `public Warehouse GetWarehouseByCode( string code )`
  - param `code` (System.String)
  - returns: Type: Warehouse
- `public Warehouse GetWarehouseByID( int id )`
  - param `id` (System.Int32)
  - returns: Type: Warehouse
- `public WarehouseContext GetWarehouseContextByCode( InventoryItem item, string code )`
  - param `item` (Pastel.Evolution.InventoryItem)
  - param `code` (System.String)
  - returns: Type: WarehouseContext
- `public WarehouseContext GetWarehouseContextByID( InventoryItem item, int id )`
  - param `item` (Pastel.Evolution.InventoryItem)
  - param `id` (System.Int32)
  - returns: Type: WarehouseContext
- `public WarehouseContext GetWarehouseContextByWarehouse( InventoryItem item, Warehouse whse )`
  - param `item` (Pastel.Evolution.InventoryItem)
  - param `whse` (Pastel.Evolution.Warehouse)
  - returns: Type: WarehouseContext
- `public string ProcessDocumentWithCustomReference( OrderBase document, string reference )`
  - param `document` (Pastel.Evolution.OrderBase)
  - param `reference` (System.String)
  - returns: Type: String
- `public string ProcessStockWithCustomReference( PurchaseOrder purchaseOrder, string reference )`
  - param `purchaseOrder` (Pastel.Evolution.PurchaseOrder)
  - param `reference` (System.String)
  - returns: Type: String
- `public void RollbackTran()`
- `public void SetBranchContext( int branchID )`
  - param `branchID` (System.Int32)
- `public void SetCurrentAgent( int agentID )`
  - param `agentID` (System.Int32)
- `public void SetLicense( string serialNumber, string authKey )`
  - param `serialNumber` (System.String)
  - param `authKey` (System.String)
- `public void SetUserFieldValue( Object fields, string key, Object value )`
  - param `fields` (System.Object)
  - param `key` (System.String)
  - param `value` (System.Object)
- `public void StartNewBatch()`

# Competitor (Class)

Represents a Contact Management competitor.

**Namespace:** Pastel.Evolution

```csharp
public class Competitor : BranchedRecordBase
```

## Constructors (2)
- `public Competitor()` — Creates a new instance of an opportunity.
- `public Competitor( int id )` — Creates a new instance of a prospect.

## Properties (4)
- `public string Description { get; set; }`
- `public override int ID { get; }` — Gets the internal record ID (0 for new, unsaved records).
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

# CompletedContractPostingMethodGLContext (Class)

**Namespace:** Pastel.Evolution

```csharp
public class CompletedContractPostingMethodGLContext : TransactionTypePostingMethodGLContextBase
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

# Contract (Class)

Represents a Contact Management contract.

**Namespace:** Pastel.Evolution

```csharp
public class Contract : BranchedRecordBase
```

## Constructors (2)
- `public Contract()` — Creates a new instance of a contract.
- `public Contract( int id )` — Creates a new instance of a contract.

## Properties (14)
- `public Customer Account { get; set; }` — Gets or sets the customer on the contract.
- `public bool AllowIncidentTypeOverride { get; set; }`
- `public Contract.ContractBillingType BillingType { get; set; }` — Gets or sets the contract billing type.
- `public string ContractNo { get; set; }` — Gets or sets the contract number.
- `public double Cost { get; set; }` — Gets or sets the contract cost.
- `public DateTime EndDate { get; set; }` — Gets or sets the contract end date.
- `public override int ID { get; }` — Gets the internal record ID (0 for new, unsaved records).
- `public IncidentType IncidentType { get; set; }` — Gets or sets the incident type.
- `public int IncidentTypeID { get; set; }` — Gets or sets the incident's incident type id.
- `public override long LongID { get; }`
- `public string Name { get; set; }` — Gets or sets the contract name.
- `public string Reference { get; set; }` — Gets or sets the contract reference.
- `public DateTime StartDate { get; set; }` — Gets or sets the contract start date.
- `public int Units { get; set; }` — Gets or sets the contract units, the unit can be minutes or incidents per pack.

## Methods (6)
- `public static DataTable _ListCurrentBranch( int accountID )`
  - param `accountID` (System.Int32)
  - returns: Type: DataTable
- `public static DataTable _ListCurrentBranch( string criteria )`
  - param `criteria` (System.String)
  - returns: Type: DataTable
- `public static int Find( string criteria )`
  - param `criteria` (System.String)
  - returns: Type: Int32
- `public static int FindByCode( string reference )`
  - param `reference` (System.String)
  - returns: Type: Int32
- `public static DataTable List( int accountID )`
  - param `accountID` (System.Int32)
  - returns: Type: DataTable
- `public static DataTable List( string criteria )`
  - param `criteria` (System.String)
  - returns: Type: DataTable
- `public static DataTable List( Customer account )`
  - param `account` (Pastel.Evolution.Customer)
  - returns: Type: DataTable
- `protected internal override void OnDelete()` — Removes the record from the database, provided it is not referenced by other records.
- `protected internal override void OnSave()` — Persists the record to the database.

# CostAllocation (Class)

Describes a transaction split allocation used when splitting a transaction's contra entry.

**Namespace:** Pastel.Evolution

```csharp
public class CostAllocation : BranchedRecordBase
```

## Constructors (2)
- `public CostAllocation()` — Initializes a new instance of the CostAllocation class
- `public CostAllocation( int ID )` — Initializes a new instance of the CostAllocation class

## Properties (14)
- `public double Amount { get; set; }` — Gets or sets the transaction value.
- `public Currency Currency { get; set; }`
- `public int CurrencyID { get; set; }`
- `public string Description { get; set; }`
- `public double ExchangeRate { get; set; }`
- `public double ForeignAmount { get; set; }` — Gets or sets the foreign transaction value.
- `public override int ID { get; }`
- `public override long LongID { get; }`
- `public string Reference { get; set; }`
- `public Supplier Supplier { get; set; }`
- `public int SupplierID { get; set; }`
- `public double Tax { get; set; }` — Gets or sets the transaction tax value.
- `public TaxRate TaxRate { get; set; }`
- `public int TaxRateID { get; set; }`

## Methods (4)
- `public static CostAllocation[] _Select( string criteria )` — Experimental Method
  - param `criteria` (System.String)
  - returns: Type: CostAllocation []
- `public static CostAllocation[] _Select( string criteria, string sortOrder )` — Experimental Method
  - param `criteria` (System.String)
  - param `sortOrder` (System.String)
  - returns: Type: CostAllocation []
- `public static DataTable List( string criteria )`
  - param `criteria` (System.String)
  - returns: Type: DataTable
- `public static DataTable List( string criteria, string sortOrder )`
  - param `criteria` (System.String)
  - param `sortOrder` (System.String)
  - returns: Type: DataTable
- `protected internal override void OnDelete()`
- `protected internal override void OnSave()`

# CostAllocationCollection (Class)

**Namespace:** Pastel.Evolution

```csharp
public class CostAllocationCollection : CollectionBase
```

## Properties (3)
- `public CostAllocation this[ int index ] { get; }`
- `public bool ReadOnly { get; internal set; }`
- `public double TotalAmount { get; }`

## Methods (5)
- `public void _Distribute()` — Distributes the sum of additional costs between detail records based on values selected for processing (ToProcess).
  - remarks: Only positive, non-zero lines are used in the calculation.
- `public void Add( CostAllocation costEntry )`
  - param `costEntry` (Pastel.Evolution.CostAllocation)
- `public CostAllocation Add( Supplier supplier, double amount, string reference, string description )`
  - param `supplier` (Pastel.Evolution.Supplier)
  - param `amount` (System.Double)
  - param `reference` (System.String)
  - param `description` (System.String)
  - returns: Type: CostAllocation
- `public CostAllocation Add( Supplier supplier, double amount, double tax, TaxRate taxRate, string reference, string description )`
  - param `supplier` (Pastel.Evolution.Supplier)
  - param `amount` (System.Double)
  - param `tax` (System.Double)
  - param `taxRate` (Pastel.Evolution.TaxRate)
  - param `reference` (System.String)
  - param `description` (System.String)
  - returns: Type: CostAllocation
- `protected override void OnClear()`
- `public void Remove( CostAllocation costEntry )`
  - param `costEntry` (Pastel.Evolution.CostAllocation)
- `public void RemoveAt( int index )`
  - param `index` (System.Int32)

# Country (Class)

Represents a country record.

**Namespace:** Pastel.Evolution

```csharp
public class Country : BranchedRecordBase
```

## Constructors (3)
- `public Country()` — Creates a new instance of a country.
- `public Country( int id )` — Creates a new instance of a country.
- `public Country( string name )` — Creates a new instance of a country.

## Properties (3)
- `public override int ID { get; }` — Gets the internal record ID (0 for new, unsaved records).
- `public override long LongID { get; }`
- `public string Name { get; set; }` — Gets or sets the country's name.

## Methods (4)
- `public static int Find( string criteria )` — Finds a record's database ID.
  - param `criteria` (System.String) — Specifies the criteria as a SQL where clause.
  - returns: Type: Int32 The ID of the first record found; -1 if not record was found.
- `public DataTable List( string criteria )` — Gets a list of database records.
  - param `criteria` (System.String) — Specifies the criteria as a SQL where clause.
  - returns: Type: DataTable Table containing selected records.
- `protected internal override void OnDelete()` — Removes the record from the database, provided it is not referenced by other records.
- `protected internal override void OnSave()` — Persists the record to the database.

# CreditNote (Class)

Represents an Evolution sales credit note.

**Namespace:** Pastel.Evolution

```csharp
public class CreditNote : SalesDocumentBase
```

## Constructors (2)
- `public CreditNote()` — Creates a new instance of a credit note.
- `public CreditNote( int id )` — Creates a new instance of a credit note.

## Properties (3)
- `public string InvoiceNumber { get; set; }` — Gets or sets the credit note's invoice number.
- `public override bool IsPartialProcessingAllowed { get; }`
- `public override OrderBase OriginalDocument { get; }`

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
- `public static int Find( string criteria )` — Finds and returns the id of the first document matching the supplied criteria. E.g. InvNumber = 'CRN0001'
  - param `criteria` (System.String) — Specifies the criteria as a SQL where clause.
  - returns: Type: Int32 The ID of the first record found; -1 if not record was found.
- `protected override void glCreditPosting( TransactionBase sender, TransactionBase.GLPostingEventArgs e )`
  - param `sender` (Pastel.Evolution.TransactionBase)
  - param `e` (Pastel.Evolution.TransactionBase.GLPostingEventArgs)
- `protected override void glDebitPosting( TransactionBase sender, TransactionBase.GLPostingEventArgs e )`
  - param `sender` (Pastel.Evolution.TransactionBase)
  - param `e` (Pastel.Evolution.TransactionBase.GLPostingEventArgs)
- `protected internal override void initialise()`
- `public static DataTable List( string criteria )` — Lists unprocessed documents for the supplied criteria.
  - param `criteria` (System.String) — E.g. Customer.Account = 'CASH001' and (OrderNum = 'SO209302')
  - returns: Type: DataTable
  - remarks: Pseudo-tables: Core, Customer

# Currency (Class)

Represents a currency record.

**Namespace:** Pastel.Evolution

```csharp
public class Currency : BranchedRecordBase
```

## Constructors (3)
- `public Currency()` — Creates a new instance of a currency.
- `public Currency( int id )` — Creates a new instance of a currency.
- `public Currency( string code )` — Creates a new instance of a currency.

## Properties (8)
- `public string Code { get; set; }` — Gets or sets the currency's code.
- `public string Description { get; set; }` — Gets or sets the currency's description.
- `public override int ID { get; }` — Gets the internal record ID (0 for new, unsaved records).
- `public override long LongID { get; }`
- `public int Options { get; set; }` — Gets or sets the currency's options.
- `public int PromptAgentID { get; set; }` — Gets or sets the currency's prompt agent id (the Id of the agent that gets prompted for setting the currency rate).
- `public ExchangeRateCollection Rates { get; }` — Gets a collection of exchange rates, accessible by date. Exchange rates are global, and not branch-specific.
- `public string Symbol { get; set; }` — Gets or sets the currency's symbol.

## Methods (7)
- `public static int Find( string criteria )` — Finds a record's database ID.
  - param `criteria` (System.String) — Specifies the criteria as a SQL where clause.
  - returns: Type: Int32 The ID of the first record found; -1 if not record was found.
- `public static int FindByCode( string code )`
  - param `code` (System.String)
  - returns: Type: Int32
- `public static Currency GetByCode( string code )`
  - param `code` (System.String)
  - returns: Type: Currency
- `public DataTable List( string criteria )` — Gets a list of database records.
  - param `criteria` (System.String) — Specifies the criteria as a SQL where clause.
  - returns: Type: DataTable Table containing selected records.
- `protected internal override void OnDelete()` — Removes the record from the database, provided it is not referenced by other records.
- `protected internal override void OnSave()` — Persists the record to the database.
- `public override string ToString()`
  - returns: Type: String

# Customer (Class)

Represents a customer account.

**Namespace:** Pastel.Evolution

```csharp
public class Customer : DrCrAccount
```

## Constructors (3)
- `public Customer()` — Creates a new instance of a customer account.
- `public Customer( int id )` — Creates a new instance of a customer account.
- `public Customer( string code )` — Creates a new instance of a customer account.

## Properties (80)
- `public override double AccountBalance { get; }` — Gets the current balance on the account.
- `public string AccountDescription { get; set; }` — Gets or sets an additional description on the account.
- `public int AccountTerms { get; set; }` — Gets or sets the account terms. (temporary property)
- `public override bool Active { get; set; }` — Gets or sets the account's operational state.
- `public string Addressee { get; set; }` — Gets or sets the account's addressee.
- `public AccountAgeingMethod AgeingMethod { get; set; }`
- `public int AgentID { get; set; }` — Gets or sets the ID of the agent associated withthe account.
- `public AgingTerm AgingTerm { get; set; }` — Gets or sets the customer aging terms associated with the account.
- `public int AgingTermID { get; set; }` — Gets or sets ID of the customer aging terms associated with the account.
- `public Area Area { get; set; }` — Gets or sets the account's area.
- `public int AreaID { get; set; }` — Gets or sets the ID of the Area record associated with the account.
- `public double AutomaticDiscount { get; set; }` — Gets or sets the discount percentage (valid values: 0-100) automatically appliedto inventory documents.
- `public Bank Bank { get; set; }` — Gets or sets the bank associated with the account.
- `public string BankAccountNo { get; set; }` — Gets or sets the account's bank account number.
- `public Bank.AccountType BankAccountType { get; set; }` — Gets or sets the account's bank account type.
- `public string BankBranchCode { get; set; }` — Gets or sets the account's bank branch code.
- `public int BankID { get; set; }` — Gets or sets the ID of the bank record associated with the account.
- `public string BankReferenceNo { get; set; }` — Gets or sets the reference number to use in bank transaction exports etc.
- `public BusinessClass BusinessClass { get; set; }` — Gets or sets the account's business class.
- `public int BusinessClassID { get; set; }` — Gets or sets the account's business class ID.
- `public BusinessType BusinessType { get; set; }` — Gets or sets the account's business type.
- `public int BusinessTypeID { get; set; }` — Gets or sets the account's business type ID.
- `public string CellPhone { get; set; }` — Gets or sets the mobile number associated with the account.
- `public override bool ChargeTax { get; set; }` — Gets or sets whether or not to charge the account VAT.
- `public bool CheckTerms { get; set; }` — Gets or sets whether or not to check the terms on the account before posting debit transactions.
- `public override string Code { get; set; }` — Gets or sets the account's code.
- `public string ContactPerson { get; set; }` — Gets or sets the account's contact person.
- `public Country Country { get; set; }` — Gets or sets the account's country.Gets or sets the country record associated with the account.
- `public int CountryID { get; set; }` — Gets or sets the ID of the country associated with the account.
- `public double CreditLimit { get; set; }` — Gets or sets the account's credit limit.
- `public override Currency Currency { get; set; }` — Gets or sets the account's currency. A null value indicates home currency.
- `public override int CurrencyID { get; set; }` — Gets or sets the account's currency id. 0 indicates local currency.
- `public Address DefaultDeliveryAddress { get; }` — Gets the account's default delivery address. A new address is created on the fly if one does not exist.
- `public int DefaultIncidentTypeID { get; set; }` — Gets or sets the account's default incident type ID.
- `public PriceList DefaultPriceList { get; set; }`
- `public int DefaultPriceListID { get; set; }`
- `public override SettlementTerms DefaultSettlementTerms { get; set; }`
- `public TaxRate DefaultTaxRate { get; set; }` — Gets or sets the account's default tax rate.
- `public int DefaultTaxRateID { get; set; }` — Gets or sets the account's default tax rate id.
- `public string DeliverTo { get; set; }` — Gets or sets the account's addressee.
- `public DeliveryAddressCollection DeliveryAddresses { get; }`
- `public override string Description { get; set; }` — Gets or sets the account's name.
- `public bool ElectronicDocumentAcceptance { get; set; }` — Gets or sets whether or not the customer accepts electronic invoices as originals.
- `public string EmailAddress { get; set; }` — Gets or sets the email address associated with the account.
- `public bool EmailSourceDocument { get; set; }` — Gets or sets whether or not the customer's source documents should be emailed.
- `public bool EmailStatement { get; set; }` — Gets or sets whether or not the customer account's statement should be emailed.
- `public string Fax { get; set; }` — Gets or sets the account's fax number.
- `public override double ForeignAccountBalance { get; }` — Gets the current balance on the account in its foreign currency.
- `public CustomerGroup Group { get; set; }` — Gets or sets the customer group associated with the account.
- `public int GroupID { get; set; }` — Gets or sets ID of the customer group associated with the account.
- `public override int ID { get; }` — Gets the internal record ID (0 for new, unsaved records).
- `public string IDNumber { get; set; }`
- `public string Initials { get; set; }` — Gets or sets the account's initials if the account represents a person.
- `public double InterestRate { get; set; }` — Gets or sets the account's interest rate as used by the interest charging utilityin Evolution (valid values: 0-100).
- `public bool IsCashDebtor { get; set; }` — Gets or sets whether the account is a cash debtor.
- `public override bool IsForeignCurrencyAccount { get; }` — Gets or sets whether the account transacts in a foreign currency.
- `public bool IsOnHold { get; set; }` — Gets or sets whether or not the account is on hold.
- `public Customer this[ string code ] { get; }` — Gets an account object possessing the given code.
- `public override long LongID { get; }`
- `public Customer MainAccount { get; set; }` — Gets or sets the account's main account.
- `public int MainAccountID { get; }` — Gets the main account's ID (0 if none)
- `public override Module Module { get; }` — Gets the Evolution module this record belongs to, Used in internal validation.
- `public Address PhysicalAddress { get; set; }` — Gets or sets the account's physical address.
- `public Address PostalAddress { get; set; }` — Gets or sets the account's physical address.
- `public bool PrintSourceDocument { get; set; }` — Gets or sets whether or not the customer's source documents should be printed.
- `public bool PrintStatement { get; set; }` — Gets or sets whether or not the customer account requires a physical statement.
- `public bool PromptTaxNumber { get; set; }` — Gets or sets whether or not a prompt should be raised when selling to this account when it does not have a TaxNumber specified.
- `[ObsoleteAttribute("Use UserFields instead.")] public FieldCollection RawFieldData { get; }`
- `public string Registration { get; set; }` — Gets or sets the account's registration (company, CC, etc.) number.
- `public int SalesRepID { get; set; }` — Gets or sets the sales representative ID.
- `public double SettlementDiscount { get; set; }` — Gets or sets the settlement discount percentage applied when receiving payments through the Evolution front-end (valid values: 0-100).
- `public string StatementZipPassword { get; set; }` — Gets or sets the password to the zip file when emailing and zipping a statement. Passed as clear text but encrypted in the database.
- `public string TaxNumber { get; set; }` — Gets or sets the account's VAT number.
- `public string Telephone { get; set; }` — Gets or sets the account's primary telephone number.
- `public string Telephone2 { get; set; }` — Gets or sets the account's secondary telephone number.
- `public DateTime Timestamp { get; }` — Gets the date/time on which the account was last modified.
- `public string Title { get; set; }` — Gets or sets the account's title (Mr., Mrs. etc.) if the account represents a person.
- `public bool UseEmail { get; set; }` — Gets or sets whether or not to use the account's e-mail address.
- `public FieldCollection UserFields { get; }`
- `public string Webpage { get; set; }` — Gets or sets the web address associated with the account.

## Methods (11)
- `public string _GenerateAccountCode( string seed )`
  - param `seed` (System.String)
  - returns: Type: String
- `public static DataTable _ListCurrentBranch( string criteria )`
  - param `criteria` (System.String)
  - returns: Type: DataTable
- `public void _Refresh()` — Experimental method.
- `public static Customer[] _Select( string criteria )` — Experimental Method
  - param `criteria` (System.String)
  - returns: Type: Customer []
- `public static Customer[] _Select( string criteria, string sortOrder )` — Experimental Method
  - param `criteria` (System.String)
  - param `sortOrder` (System.String)
  - returns: Type: Customer []
- `public static int Find( string criteria )` — Finds a customer account ID.
  - param `criteria` (System.String) — The criteria passed to the SQL query. Eg. Account = 'CASH001' or Name like '%CASH%'
  - returns: Type: Int32
- `public static int FindByCode( string code )` — Attempts to find an AR account by its account code and returns its ID.
  - param `code` (System.String) — The account code used to lookup the account.
  - returns: Type: Int32 -1 if no record was found, else the id of the first account matching the criteria supplied.
- `public static Customer Get( string criteria )` — Returns the [first] customer object matching the criteria specified; otherwise, returns null.
  - param `criteria` (System.String) — Eg. Account = 'CASH001' or Name like '%CASH%'
  - returns: Type: Customer
- `public static Customer GetByCode( string code )` — Returns a customer object corresponding to the code specified; otherwise, returns null.
  - param `code` (System.String)
  - returns: Type: Customer
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

# CustomerGroup (Class)

Represents a customer group.

**Namespace:** Pastel.Evolution

```csharp
public class CustomerGroup : BranchedRecordBase
```

## Constructors (3)
- `public CustomerGroup()` — Creates a new instance of a group.
- `public CustomerGroup( int id )` — Creates a new instance of a group.
- `public CustomerGroup( string code )` — Creates a new instance of a group.

## Properties (12)
- `public string Code { get; set; }` — Gets or sets the group's code.
- `public GLAccount ControlAccount { get; set; }` — Gets or sets the group's override GL account.
- `public int ControlAccountID { get; set; }` — Gets or sets the group's control account id.
- `public string Description { get; set; }` — Gets or sets the group description.
- `public int DiscountMatrixRow { get; set; }` — Gets or sets the group's discount matrix row.
- `public int ForeignLossAccountID { get; set; }` — Gets or sets the group's foreign loss account id.
- `public int ForeignProfitAccountID { get; set; }` — Gets or sets the group's foreign profit account id.
- `public override int ID { get; }` — Gets the internal record ID (0 for new, unsaved records).
- `public override long LongID { get; }`
- `public GLAccount TaxControlAccount { get; set; }` — Gets or sets the group's override tax GL control account.
- `public int TaxControlAccountID { get; set; }` — Gets or sets the group's tax control account id.
- `public DateTime TimeStamp { get; set; }` — Gets or sets the group's modification timestamp.

## Methods (7)
- `public static int Find( string criteria )` — Returns the id of the first record found matching the criteria. Eg. code = 'abc'
  - param `criteria` (System.String) — Specifies the criteria as a SQL where clause.
  - returns: Type: Int32 ID of the record found; if not found, -1
- `public static int FindByCode( string code )` — Attempts to find an AR group by its code and returns its ID.
  - param `code` (System.String) — The account code used to lookup the account.
  - returns: Type: Int32 -1 if no record was found, else the id of the first account matching the criteria supplied.
- `public static CustomerGroup Get( string criteria )` — Returns the [first] group object with the account code specified; otherwise, returns null.
  - param `criteria` (System.String) — Eg. Code like '1_B%'
  - returns: Type: CustomerGroup
- `public static CustomerGroup GetByCode( string code )` — Returns a group object corresponding to the code specified; otherwise, returns null.
  - param `code` (System.String)
  - returns: Type: CustomerGroup
- `public DataTable List( string criteria )` — Gets a list of database records.
  - param `criteria` (System.String) — Specifies the criteria as a SQL where clause.
  - returns: Type: DataTable Table containing selected records.
- `protected internal override void OnDelete()` — Removes the record from the database, provided it is not referenced by other records.
- `protected internal override void OnSave()` — Persists the record to the database.

# CustomerTransaction (Class)

Represents a customer transaction.

**Namespace:** Pastel.Evolution

```csharp
public class CustomerTransaction : DrCrTransaction
```

## Constructors (2)
- `public CustomerTransaction()` — Creates a new instance of a transaction.
- `public CustomerTransaction( long id )` — Creates a new instance of a transaction.

## Properties (42)
- `public override AccountBase Account { get; set; }` — Gets or sets the Account to which the transaction gets posted. This is amandatory field.
- `public override int AccountID { get; set; }` — Gets or sets the ID of the Account to which the transaction gets posted.
- `public override AllocationCollection Allocations { get; }` — Gets the transaction's allocation collection.
- `public override double Amount { get; set; }` — Gets or sets the (gross) transaction value. Negative values are allowed and will result in inverted debits and credits.
- `public override string Audit { get; }` — Gets the transaction's audit number.
- `public override Branch Branch { get; set; }`
- `public override int BranchID { get; internal set; }`
- `public override double Credit { get; set; }` — Gets the transaction's credit value, the value of which is determined by the Amount and TransactionCode properties.
- `public override Currency Currency { get; internal set; }` — Gets the foreign currency in use on this transaction, determined by the specified account. A null value indicates local currency.
- `public override int CurrencyID { get; internal set; }`
- `public Customer Customer { get; set; }` — Gets or sets the transaction's customer account (maps directly to Account).
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
- `public bool PostDated { get; set; }` — Gets or sets whether the transaction is a Post Dated Transaction.
- `public override Project Project { get; set; }` — Gets or sets the Project record associated with this transaction. When using Project Tracking, this field must be specified wherever applicable.
- `public override int ProjectID { get; set; }` — Gets or sets the ID of the Project record associated with this transaction. When using Project Tracking, this field must be specified wherever applicable.
- `public override string Reference { get; set; }` — Gets or sets the transaction reference that - together with the Description - appears on the customer statement by default. This is a mandatory field.
- `public override string Reference2 { get; set; }` — Gets or sets an additional transaction reference.
- `public SalesRepresentative SalesRep { get; set; }` — Gets or sets the Sales Rep.
- `public int SalesRepID { get; set; }`
- `public override SettlementTerms SettlementTerms { get; set; }`
- `public override int SettlementTermsID { get; set; }`
- `public override SplitAllocationCollection SplitAllocations { get; }` — Gets the transaction's split allocation collection, used to split the contra account posting to various GL accounts.
- `public override double Tax { get; set; }` — Gets or sets the transaction tax amount (automatically rounded to 2 decimals).
- `public override TaxRate TaxRate { get; set; }` — Gets or sets the TaxRate record associated with this transaction. If a tax type is specified, a tax amount is automatically calculated, but can be overridden.
- `public override int TaxRateID { get; set; }` — Gets or sets the transaction's tax type id.
- `public int TillID { get; set; }`
- `public override TransactionCodeBase TransactionCode { get; set; }` — Gets or sets the TransactionCode record associated with this transaction, as maintained in Accounts Receivable > Maintenance > Transaction Types. Transaction codes/types govern General Ledger integration. This is a mandatory field.
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
  - param `account` (Pastel.Evolution.AccountBase) — The customer account by which to filter the transaction list.
  - param `criteria` (System.String) — The criteria passed to the SQL query. Eg. Reference = 'INV001' or Description like '%Invoice%'
  - returns: Type: Int64
- `protected override double getExchangeRate()`
  - returns: Type: Double
- `public static DataTable List( string criteria )` — Returns a System.Data.DataTable object containing the database records from the PostAR table matching the supplied criteria.
  - param `criteria` (System.String) — The SQL criteria used to locate the record, e.g. Reference like '1___'
  - returns: Type: DataTable A System.Data.DataTable object containing matching records.
  - remarks: The criteria is passed to an SQL query so use the appropriate syntax. Remember to include the single quotes around string literals and append additional criteria with and .
- `public static DataTable List( AccountBase account, string criteria )` — Returns a System.Data.DataTable object containing the database records from the PostAR/PostAP table matching the supplied criteria and limited to the specified account.
  - param `account` (Pastel.Evolution.AccountBase) — The customer account to which to limit the transaction listing.
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

# DatabaseContext (Class)

**Namespace:** Pastel.Evolution

```csharp
public static class DatabaseContext
```

## Properties (18)
- `public static Branch _ContextBranch { get; internal set; }`
- `public static SqlConnection CommonDBConnection { get; }`
- `public static int CommonDBVersion { get; internal set; }`
- `public static Branch CompanyBranch { get; private set; }`
- `public static string CompanyID { get; internal set; }`
- `public static string CompanyName { get; }`
- `public static string CompatibleDatabaseVersion { get; }`
- `public static Agent CurrentAgent { get; set; }`
- `public static string CurrentDatabaseVersion { get; internal set; }`
- `public static SqlConnection DBConnection { get; }` — The SqlConnection object used by all database calls in the API. Transaction scope is managed automatically using the BeginTran, CommitTran and RollBackTran methods
- `public static SqlTransaction DBTransaction { get; }` — The SQL transaction in progress (if any).
- `public static int DefaultCommandTimeout { get; set; }`
- `public static DateTime ExpiryDate { get; }`
- `public static bool IsBranchOffline { get; private set; }`
- `public static bool IsCommonConnectionOpen { get; }`
- `public static bool IsConnectionOpen { get; }`
- `public static bool IsTransactionPending { get; }`
- `public static int RegisteredUsers { get; }`

## Methods (14)
- `public static bool BeginTran()` — Starts a global database transaction.
  - returns: Type: Boolean True if a transaction was actually started; false if a transaction was already pending.
  - remarks: Certain operations will implicitly begin and end a transaction if a transaction is not already pending. If deciding to manage the transaction yourself, be sure to include this in a try-catch block calling RollbackTran or CommitTran methods accordingly. Also be aware that most client tools have their transaction isolation level set to "read commited" by default, so while this transaction is in progress, other data requests for data will be delayed.
- `public static bool CommitTran()` — Quietly commits the global transaction regardless of whether it is actually pending.
  - returns: Type: Boolean True if a transaction was actually pending; false otherwise.
- `public static void CreateCommonDBConnection()` — Creates a connection to the database named 'EvolutionCommon', on the local server, using trusted authentication.
- `public static void CreateCommonDBConnection( string connectionString )` — Creates a connection to the Evolution common database.
  - param `connectionString` (System.String) — The connection string used by SqlConnection .
- `public static void CreateCommonDBConnection( string server, string database, string login, string password, bool trustedAuth )` — Creates a connection to the Evolution common database.
  - param `server` (System.String) — The SQL server name, alias or IP address.
  - param `database` (System.String) — The SQL database name.
  - param `login` (System.String) — The SQL Server login name (if not using trusted authentication).
  - param `password` (System.String) — The SQL Server login's password (if not using trusted authentication).
  - param `trustedAuth` (System.Boolean) — Whether or not to use trusted authentication.
- `public static void CreateConnection( string connectionString )` — Creates a connection to a Pastel Evolution database. Use this method if you have a connection string available; otherwise use one of the overloaded methods.
  - param `connectionString` (System.String) — The connection string used by SqlConnection .
- `public static void CreateConnection( string server, string database )` — Creates a connection to the Evolution accounting database using trusted authentication.
  - param `server` (System.String) — The SQL server name, alias or IP address.
  - param `database` (System.String) — The SQL database name.
- `public static void CreateConnection( string server, string database, string login, string password, bool trustedAuth )` — Creates a connection to the Evolution accounting database.
  - param `server` (System.String) — The SQL server name, alias or IP address.
  - param `database` (System.String) — The SQL database name.
  - param `login` (System.String) — The SQL Server login name (if not using trusted authentication).
  - param `password` (System.String) — The SQL Server login's password (if not using trusted authentication).
  - param `trustedAuth` (System.Boolean) — Whether or not to use trusted authentication.
- `public static DataTable ExecuteCommandDataTable( SqlCommand cmd )`
  - param `cmd` (System.Data.SqlClient.SqlCommand)
  - returns: Type: DataTable
- `public static DataTable ExecuteCommandDataTable( string sql )`
  - param `sql` (System.String)
  - returns: Type: DataTable
- `public static DataTable ExecuteCommandDataTable( SqlConnection connection, SqlTransaction transaction, SqlCommand cmd )`
  - param `connection` (System.Data.SqlClient.SqlConnection)
  - param `transaction` (System.Data.SqlClient.SqlTransaction)
  - param `cmd` (System.Data.SqlClient.SqlCommand)
  - returns: Type: DataTable
- `public static DataTable ExecuteCommandDataTable( SqlConnection connection, SqlTransaction transaction, string sql )`
  - param `connection` (System.Data.SqlClient.SqlConnection)
  - param `transaction` (System.Data.SqlClient.SqlTransaction)
  - param `sql` (System.String)
  - returns: Type: DataTable
- `public static int ExecuteCommandNonQuery( SqlCommand cmd )`
  - param `cmd` (System.Data.SqlClient.SqlCommand)
  - returns: Type: Int32
- `public static Object ExecuteCommandNonQuery( string sql )`
  - param `sql` (System.String)
  - returns: Type: Object
- `public static int ExecuteCommandNonQuery( SqlConnection connection, SqlTransaction transaction, SqlCommand cmd )`
  - param `connection` (System.Data.SqlClient.SqlConnection)
  - param `transaction` (System.Data.SqlClient.SqlTransaction)
  - param `cmd` (System.Data.SqlClient.SqlCommand)
  - returns: Type: Int32
- `public static int ExecuteCommandNonQuery( SqlConnection connection, SqlTransaction transaction, string sql )`
  - param `connection` (System.Data.SqlClient.SqlConnection)
  - param `transaction` (System.Data.SqlClient.SqlTransaction)
  - param `sql` (System.String)
  - returns: Type: Int32
- `public static Object ExecuteCommandScalar( SqlCommand cmd )` — Executes a command and returns the 1st value from 1st value. Will convert a return value of DBNull to null.
  - param `cmd` (System.Data.SqlClient.SqlCommand)
  - returns: Type: Object
- `public static Object ExecuteCommandScalar( string sql )` — Executes a command and returns the 1st value from 1st value. Will convert a return value of DBNull to null.
  - param `sql` (System.String)
  - returns: Type: Object
- `public static Object ExecuteCommandScalar( SqlConnection connection, SqlTransaction transaction, SqlCommand cmd )` — Executes the query, and returns the first column of the first row in the result set returned by the query. Additional columns or rows are ignored.
  - param `connection` (System.Data.SqlClient.SqlConnection)
  - param `transaction` (System.Data.SqlClient.SqlTransaction)
  - param `cmd` (System.Data.SqlClient.SqlCommand)
  - returns: Type: Object The first column of the first row in the result set, or a null reference if the result set is empty. This function will return a null reference instead of a DBNull value.
- `public static Object ExecuteCommandScalar( SqlConnection connection, SqlTransaction transaction, string sql )` — Executes a command and returns the 1st value from 1st value. Will convert a return value of DBNull to null.
  - param `connection` (System.Data.SqlClient.SqlConnection)
  - param `transaction` (System.Data.SqlClient.SqlTransaction)
  - param `sql` (System.String)
  - returns: Type: Object
- `public static DataRow ExecuteCommandSingleRow( SqlCommand cmd )`
  - param `cmd` (System.Data.SqlClient.SqlCommand)
  - returns: Type: DataRow
- `public static DataRow ExecuteCommandSingleRow( string cmd )`
  - param `cmd` (System.String)
  - returns: Type: DataRow
- `public static DataRow ExecuteCommandSingleRow( SqlConnection connection, SqlTransaction transaction, SqlCommand cmd )`
  - param `connection` (System.Data.SqlClient.SqlConnection)
  - param `transaction` (System.Data.SqlClient.SqlTransaction)
  - param `cmd` (System.Data.SqlClient.SqlCommand)
  - returns: Type: DataRow
- `public static DataRow ExecuteCommandSingleRow( SqlConnection connection, SqlTransaction transaction, string sql )`
  - param `connection` (System.Data.SqlClient.SqlConnection)
  - param `transaction` (System.Data.SqlClient.SqlTransaction)
  - param `sql` (System.String)
  - returns: Type: DataRow
- `public static EvolutionVersion GetProductVersion( SqlConnection connection )`
  - param `connection` (System.Data.SqlClient.SqlConnection)
  - returns: Type: EvolutionVersion
- `public static void Initialise( string connectionString, string commonConnectionString, string serialNumber, string authKey )` — Initialises the database connections required by the SDK.
  - param `connectionString` (System.String) — Connection string to use when connecting to the Evolution accounting database.
  - param `commonConnectionString` (System.String) — Connection string to use when connecting to the common Evolution database.
  - param `serialNumber` (System.String) — Your SDK serial number.
  - param `authKey` (System.String) — Your SDK authorisation key.
- `public static void Initialise( string database, string server, string user, string password, string serialNumber, string authKey )` — Initialises the database connections required by the SDK. This version of the method assumes the common database is called 'EvolutionCommon', is on the same server as the accounting database, and is able to uses the same login credentials.
  - param `database` (System.String) — The Evolution accounting database.
  - param `server` (System.String) — The SQL database server name or IP address.
  - param `user` (System.String) — The SQL login.
  - param `password` (System.String) — The SQL password.
  - param `serialNumber` (System.String) — Your SDK serial number.
  - param `authKey` (System.String) — Your SDK authorisation key.
- `public static void Initialise( string database, string commonDatabase, string server, string user, string password, string serialNumber, string authKey )` — Initialises the database connections required by the SDK. This version of the method assumes the common database is on the same server as the accounting database, and is able to uses the same login credentials.
  - param `database` (System.String) — The Evolution accounting database.
  - param `commonDatabase` (System.String) — The Evolution common database.
  - param `server` (System.String) — The SQL database server name or IP address.
  - param `user` (System.String) — The SQL login.
  - param `password` (System.String) — The SQL password.
  - param `serialNumber` (System.String) — Your SDK serial number.
  - param `authKey` (System.String) — Your SDK authorisation key.
- `public static bool IsModuleActive( ModuleRegistration.Module module )`
  - param `module` (Pastel.Evolution.Internal.ModuleRegistration.Module)
  - returns: Type: Boolean
- `public static bool RollbackTran()` — Quietly aborts the global transaction regardless of whether it is actually open.
  - returns: Type: Boolean True if a transaction was actually pending; false otherwise.
- `public static void SetBranchContext( int branchID )`
  - param `branchID` (System.Int32)
- `public static void SetLicense( string serialNumber, string authKey )`
  - param `serialNumber` (System.String)
  - param `authKey` (System.String)

# Defaults (Class)

Contains various global static methods and properties related to the basic functionality of the SDK.

**Namespace:** Pastel.Evolution

```csharp
public class Defaults
```

## Properties (28)
- `public static APDefaults AccountsPayable { get; }`
- `public static ARDefaults AccountsReceivable { get; }`
- `public static string AssemblyPath { get; internal set; }`
- `public static string AssemblyVersion { get; internal set; }`
- `public static string Audit { get; }` — Reserves and returns the next audit number "on the fly".
- `public static ContactManagementDefaults ContactManagement { get; }`
- `public static int CostVarianceAccountID { get; }`
- `public static TaxRate CreditorZeroTaxRate { get; }`
- `public static TaxRate DebtorsZeroTaxRate { get; }`
- `public static PriceList DefaultPriceList { get; }`
- `[ObsoleteAttribute("Deprecated. Use Defaults.ContactManagement.DocumentStoragePath instead.")] public static string DocumentStoragePath { get; }`
- `public static GLDefaults GeneralLedger { get; }`
- `public static InventoryDefaults Inventory { get; }`
- `public static InventoryCostingMethod InventoryCostingMethod { get; }` — The inventory costing method configured in Evolution's inventory defaults.
- `public static InventoryIntegrationMethod InventoryIntegrationMethod { get; }` — The inventory integration method configured in Evolution's inventory defaults.
- `public static JobDefaults JobCosting { get; }`
- `public static DateTime NullDate { get; }`
- `public static bool OutputSqlToStream { get; set; }`
- `public static int PurchasesCostVarianceAccountID { get; }`
- `public static TransactionCode PurchasesCreditNoteTransactionCode { get; }` — The return to supplier transaction code as configured in Evolution's inventory defaults.
- `public static TransactionCode PurchasesGrvTransactionCode { get; }` — The goods received note transaction code as configured in Evolution's inventory defaults.
- `public static TransactionCode PurchasesInvoiceTransactionCode { get; }` — The goods received note transaction code as configured in Evolution's inventory defaults.
- `public static int RegisteredUsers { get; }`
- `public static DateTime RegistrationExpiryDate { get; }`
- `public static TransactionCode SalesCreditNoteTransactionCode { get; }` — The credit note transaction code as configured in Evolution's inventory defaults.
- `public static TransactionCode SalesInvoiceTransactionCode { get; }` — The invoice transaction code as configured in Evolution's inventory defaults.
- `public static MemoryStream SqlOutputStream { get; set; }`
- `public static TransactionCode WarehouseTransferTransactionCode { get; }` — The warehouse transfer transaction code as configured in Evolution's inventory defaults.

## Methods (10)
- `public static string _GenerateAccountCode( string table, string field, int prefixLength, int padLength, string criteria, bool capitalise )`
  - param `table` (System.String)
  - param `field` (System.String)
  - param `prefixLength` (System.Int32)
  - param `padLength` (System.Int32)
  - param `criteria` (System.String)
  - param `capitalise` (System.Boolean)
  - returns: Type: String
- `public static void AddCommandToStream( SqlCommand cmd )`
  - param `cmd` (System.Data.SqlClient.SqlCommand)
- `public static int GetGLPeriod( DateTime tranDate, bool errorIfBlocked )` — Gets the period for the transaction date specified.
  - param `tranDate` (System.DateTime) — The date for which the corresponding period is to be located.
  - param `errorIfBlocked` (System.Boolean) — Whether or not an exception needs to be thrown if the applicable period is blocked.
  - returns: Type: Int32 GL Period ID: 1-12 for 1st year periods, 2-24 for 2nd, etc.
- `public static string GetModulesRegistered()`
  - returns: Type: String
- `public static string GetNextIncidentReference()` — Permanently reserves an incident reference
  - returns: Type: String
- `public static string GetNextInvDocNo( DocumentType docType, DocumentState docState )` — Reserves and returns the next available sales order number. If automatic numbering is not used, an empty string is returned.
  - param `docType` (Pastel.Evolution.DocumentType)
  - param `docState` (Pastel.Evolution.DocumentState)
  - returns: Type: String
- `public static string GetNextJobNumber()` — Permanently reserves an incident reference
  - returns: Type: String
- `public static string GetNextOpportunityReference()` — Permanently reserves an incident reference
  - returns: Type: String
- `public static void ReloadModuleDefaults()`
- `public static void StartNewBatch()` — Forces an audit number increment within the same transaction batch. NOTE: When committing a transaction using Defaults.CommitTran, the audit number will automatically be incremented, so use this function ONLY when you need have different audit numbers in the same transaction scope

## Fields (1)
- `public const string USERNAME` — The internal user name assigned to posted transactions.

# DeliveryAddress (Class)

**Namespace:** Pastel.Evolution

```csharp
public class DeliveryAddress : BranchedRecordBase
```

## Constructors (2)
- `public DeliveryAddress()` — Creates a new instance of a delivery address.
- `public DeliveryAddress( int id )` — Creates a new instance of a delivery address.

## Properties (14)
- `public DrCrAccount Account { get; internal set; }`
- `public int AccountID { get; }`
- `public Address Address { get; set; }` — Gets or sets the delivery address record's actual address.
- `public string CellPhone { get; set; }`
- `public DeliveryAddressCode Code { get; set; }` — Gets or sets the delivery address code.
- `public int CodeID { get; }`
- `public string Description { get; set; }`
- `public string EmailAddress { get; set; }`
- `public string Fax { get; set; }`
- `public override int ID { get; }`
- `public bool IsDefault { get; internal set; }`
- `public override long LongID { get; }`
- `public string Telephone1 { get; set; }`
- `public string Telephone2 { get; set; }`

## Methods (5)
- `public static DeliveryAddress[] _Select( string criteria )` — Experimental Method
  - param `criteria` (System.String)
  - returns: Type: DeliveryAddress []
- `public static DeliveryAddress[] _Select( string criteria, string sortOrder )` — Experimental Method
  - param `criteria` (System.String)
  - param `sortOrder` (System.String)
  - returns: Type: DeliveryAddress []
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
- `protected internal override void OnDelete()`
- `protected internal override void OnSave()` — Persists the record to the database.

# DeliveryAddressCode (Class)

**Namespace:** Pastel.Evolution

```csharp
public class DeliveryAddressCode : BranchedRecordBase
```

## Constructors (3)
- `public DeliveryAddressCode()` — Creates a new instance of a delivery address code.
- `public DeliveryAddressCode( int id )` — Creates a new instance of a delivery address code.
- `public DeliveryAddressCode( string code )` — Creates a new instance of a delivery address code.

## Properties (4)
- `public string Code { get; set; }`
- `public string Description { get; set; }`
- `public override int ID { get; }`
- `public override long LongID { get; }`

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
- `protected internal override void OnDelete()`
- `protected internal override void OnSave()` — Persists the record to the database.

# DeliveryAddressCollection (Class)

Represents a collection of warehouse context records.

**Namespace:** Pastel.Evolution

```csharp
public class DeliveryAddressCollection : CollectionBase
```

## Properties (1)
- `Item` — Gets a delivery address by index.

## Methods (3)
- `public void Add( DeliveryAddress data )`
  - param `data` (Pastel.Evolution.DeliveryAddress)
- `public void Add( string code, Address address )`
  - param `code` (System.String)
  - param `address` (Pastel.Evolution.Address)
- `public Address GetDefault()`
  - returns: Type: Address
- `public void SetDefault( DeliveryAddress newDefaultAddress )` — Sets the new default delivery address for an account. Remember to call Save() when done.
  - param `newDefaultAddress` (Pastel.Evolution.DeliveryAddress)

# DeliveryMethod (Class)

Represents an order delivery method.

**Namespace:** Pastel.Evolution

```csharp
public class DeliveryMethod : BranchedRecordBase
```

## Constructors (3)
- `public DeliveryMethod()` — Creates a new instance of a delivery method.
- `public DeliveryMethod( int id )` — Creates a new instance of a delivery method.
- `public DeliveryMethod( string description )` — Creates a new instance of a delivery method.

## Properties (4)
- `public string Comment { get; set; }` — Gets or sets the delivery method's comment.
- `public string Description { get; set; }` — Gets or sets the delivery method's description.
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

# Department (Class)

Represents a business department which can be assigned to accounts.

**Namespace:** Pastel.Evolution

```csharp
public class Department : BranchedRecordBase
```

## Constructors (3)
- `public Department()` — Creates a new instance of a department.
- `public Department( int id )` — Creates a new instance of a department.
- `public Department( string description )` — Creates a new instance of a department.

## Properties (3)
- `public string Description { get; set; }` — Gets or sets the department description.
- `public override int ID { get; }` — Gets the internal record ID (0 for new, unsaved records).
- `public override long LongID { get; }`

## Methods (5)
- `public static int Find( string criteria )` — Finds a record's database ID.
  - param `criteria` (System.String) — Specifies the criteria as a SQL where clause.
  - returns: Type: Int32 The ID of the first record found; -1 if not record was found.
- `public static int FindByDescription( string description )`
  - param `description` (System.String)
  - returns: Type: Int32
- `public DataTable List( string criteria )` — Gets a list of database records.
  - param `criteria` (System.String) — Specifies the SQL criteria.
  - returns: Type: DataTable Table containing selected records.
- `protected internal override void OnDelete()` — Removes the record from the database, provided it is not referenced by other records.
- `protected internal override void OnSave()` — Persists the record to the database.

# Designation (Class)

Represents a designation which can be assigned to persons.

**Namespace:** Pastel.Evolution

```csharp
public class Designation : BranchedRecordBase
```

## Constructors (3)
- `public Designation()` — Creates a new instance of a designation.
- `public Designation( int id )` — Creates a new instance of a designation.
- `public Designation( string description )` — Creates a new instance of a designation.

## Properties (3)
- `public string Description { get; set; }` — Gets or sets the designation description.
- `public override int ID { get; }` — Gets the internal record ID (0 for new, unsaved records).
- `public override long LongID { get; }`

## Methods (5)
- `public static int Find( string criteria )` — Finds a record's database ID.
  - param `criteria` (System.String) — Specifies the criteria as a SQL where clause.
  - returns: Type: Int32 The ID of the first record found; -1 if not record was found.
- `public static int FindByDescription( string description )`
  - param `description` (System.String)
  - returns: Type: Int32
- `public DataTable List( string criteria )` — Gets a list of database records.
  - param `criteria` (System.String) — Specifies the SQL criteria.
  - returns: Type: DataTable Table containing selected records.
- `protected internal override void OnDelete()` — Removes the record from the database, provided it is not referenced by other records.
- `protected internal override void OnSave()` — Persists the record to the database.

# Document (Class)

Represents a contact management document.

**Namespace:** Pastel.Evolution

```csharp
public class Document : BranchedRecordBase
```

## Constructors (3)
- `public Document()` — Initializes a new instance of the Document class
- `public Document( int id )` — Initializes a new instance of the Document class
- `public Document( string description )` — Initializes a new instance of the Document class

## Properties (10)
- `public DocumentCategory Category { get; set; }`
- `public int CategoryID { get; set; }`
- `public string Description { get; set; }`
- `public Icon Icon { get; set; }`
- `public override int ID { get; }` — Gets the internal record ID (0 for new, unsaved records).
- `public bool IsActive { get; set; }`
- `public override long LongID { get; }`
- `public string Name { get; set; }`
- `public string Path { get; }` — Gets the document's physical path. An empty string is returned if no file location is set.
- `public string PhysicalName { get; internal set; }`

## Methods (8)
- `public void _CreateLink( Incident record )` — Temporary Method
  - param `record` (Pastel.Evolution.Incident)
- `public void _CreateLink( Opportunity record )` — Temporary Method
  - param `record` (Pastel.Evolution.Opportunity)
- `public static int Find( string criteria )`
  - param `criteria` (System.String)
  - returns: Type: Int32
- `public static int FindByDescription( string description )`
  - param `description` (System.String)
  - returns: Type: Int32
- `public static DataTable List( string criteria )` — Returns a System.Data.DataTable object containing the database records from the _rtblDocStore table matching the supplied criteria.
  - param `criteria` (System.String) — The SQL criteria used to locate the record, e.g. cDocName like '1___'
  - returns: Type: DataTable A System.Data.DataTable object containing matching records.
  - remarks: The criteria is passed to an SQL query so use the appropriate syntax. Remember to include the single quotes around string literals and append additional criteria with and .
- `public void Load( string location )`
  - param `location` (System.String)
- `protected internal override void OnDelete()` — Removes the record from the database, provided it is not referenced by other records.
- `protected internal override void OnSave()` — Persists the record to the database.
- `public void Save( string path )` — Saves the document to the database after copying the physical file from the specified path and storing it in the central storage directory.
  - param `path` (System.String) — The full path to the file that needs to be copied.

# DocumentCategory (Class)

Represents a contact management document category.

**Namespace:** Pastel.Evolution

```csharp
public class DocumentCategory : BranchedRecordBase
```

## Constructors (3)
- `public DocumentCategory()` — Initializes a new instance of the DocumentCategory class
- `public DocumentCategory( int id )` — Initializes a new instance of the DocumentCategory class
- `public DocumentCategory( string description )` — Initializes a new instance of the DocumentCategory class

## Properties (3)
- `public string Description { get; set; }`
- `public override int ID { get; }` — Gets the internal record ID (0 for new, unsaved records).
- `public override long LongID { get; }`

## Methods (7)
- `public static DataTable _ListCurrentBranch( string criteria )`
  - param `criteria` (System.String)
  - returns: Type: DataTable
- `public static int Find( string criteria )`
  - param `criteria` (System.String)
  - returns: Type: Int32
- `public static int FindByDescription( string description )`
  - param `description` (System.String)
  - returns: Type: Int32
- `public static DocumentCategory GetByDescription( string description )`
  - param `description` (System.String)
  - returns: Type: DocumentCategory
- `public static DataTable List( string criteria )` — Returns a System.Data.DataTable object containing the database records from the _rtblDocStore table matching the supplied criteria.
  - param `criteria` (System.String) — The SQL criteria used to locate the record, e.g. cDocName like '1___'
  - returns: Type: DataTable A System.Data.DataTable object containing matching records.
  - remarks: The criteria is passed to an SQL query so use the appropriate syntax. Remember to include the single quotes around string literals and append additional criteria with and .
- `protected internal override void OnDelete()` — Removes the record from the database, provided it is not referenced by other records.
- `protected internal override void OnSave()` — Persists the record to the database.

# DrCrAccount (Class)

A debtor and creditor account base class.

**Namespace:** Pastel.Evolution

```csharp
public abstract class DrCrAccount : AccountBase
```

## Properties (7)
- `public abstract double AccountBalance { get; }` — Gets the account's current balance.
- `public abstract bool ChargeTax { get; set; }` — Gets or sets whether or not to charge the account VAT.
- `public abstract Currency Currency { get; set; }`
- `public abstract int CurrencyID { get; set; }`
- `public abstract SettlementTerms DefaultSettlementTerms { get; set; }`
- `public abstract double ForeignAccountBalance { get; }`
- `public abstract bool IsForeignCurrencyAccount { get; }`

# DrCrTransaction (Class)

A debtor and creditor transaction base class.

**Namespace:** Pastel.Evolution

```csharp
public abstract class DrCrTransaction : TransactionBase,
    ICloneable
```

## Properties (20)
- `public abstract AllocationCollection Allocations { get; }`
- `public abstract double Amount { get; set; }` — Gets or sets the transaction amount.
- `public abstract Branch Branch { get; }`
- `public abstract int BranchID { get; }`
- `public abstract Currency Currency { get; internal set; }` — Gets the foreign currency in use on this transaction, determined by the specified account. A null value indicates local currency.
- `public abstract int CurrencyID { get; internal set; }`
- `public double ExchangeRate { get; set; }` — Gets or sets the applicable exchange rate, expressed as [home currency]/[foreign currency]. Defaults to applicable exchange rate for the transaction date.
- `public abstract double ForeignAmount { get; set; }` — Gets or sets the transaction foreign amount.
- `public abstract double ForeignCredit { get; }`
- `public abstract double ForeignDebit { get; }`
- `public abstract double ForeignOutstanding { get; internal set; }` — Gets the transaction's foreign outstanding amount.
- `public abstract double ForeignTax { get; set; }`
- `public bool IsDebit { get; internal set; }` — Indicates whether the transaction is a debit (true) or credit(false)
- `public abstract bool IsDebitPositive { get; }` — Determines whether the derived transaction is by default nature a debit, i.e. a positive amount is a debit.
- `public double MaxForeignOutstanding { get; }` — Gets the maximum possible foreign outstanding value for the given transaction, based on the ForeignDebit or ForeignCredit value.
- `public double MaxOutstanding { get; }` — Gets the maximum possible outstanding value for the given transaction, based on the Debit or Credit value.
- `public abstract double Outstanding { get; internal set; }` — Gets the transaction's outstanding amount.
- `public abstract SettlementTerms SettlementTerms { get; set; }`
- `public abstract int SettlementTermsID { get; set; }`
- `public abstract SplitAllocationCollection SplitAllocations { get; }` — Gets the transaction's split allocation collection.

## Methods (8)
- `protected void calcAmounts()`
- `public abstract Object Clone()`
  - returns: Type: Object
- `protected abstract double getExchangeRate()`
  - returns: Type: Double
- `protected internal abstract void OnOverrideControlAccount( GLTransaction glTran )`
  - param `glTran` (Pastel.Evolution.GLTransaction)
- `protected internal abstract void OnOverrideTaxControlAccount( TransactionCode tranCode, GLTransaction glTran )`
  - param `tranCode` (Pastel.Evolution.TransactionCode)
  - param `glTran` (Pastel.Evolution.GLTransaction)
- `protected abstract void setExchangeRate( double value )`
  - param `value` (System.Double)
- `public override string ToString()`
  - returns: Type: String
- `public override bool Validate()`
  - returns: Type: Boolean

## Fields (17)
- `protected internal AllocationCollection allocations`
- `protected double amount`
- `protected Branch branch`
- `protected Currency currency`
- `protected internal Utils.LimitedQueue fcQueue`
- `protected double foreignAmount`
- `protected double foreignTax`
- `protected double glCredit`
- `protected double glDebit`
- `protected double glForeignCredit`
- `protected double glForeignDebit`
- `protected internal Project project`
- `protected internal SettlementTerms settlementTerms`
- `protected internal SplitAllocationCollection splitAllocations`
- `protected double tax`
- `protected internal TaxRate taxType`
- `protected internal TransactionCodeBase tranCode`

# EscalationGroup (Class)

Represents a Contact Management escalation group.

**Namespace:** Pastel.Evolution

```csharp
public class EscalationGroup : BranchedRecordBase
```

## Constructors (2)
- `public EscalationGroup()` — Creates a new instance of an escalation group.
- `public EscalationGroup( int id )` — Creates a new instance of an escalation group.

## Properties (3)
- `public string Description { get; set; }`
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

# EvolutionDatabaseException (Class)

**Namespace:** Pastel.Evolution

```csharp
public class EvolutionDatabaseException : EvolutionException
```

## Constructors (2)
- `public EvolutionDatabaseException( string message )` — Initializes a new instance of the EvolutionDatabaseException class
- `public EvolutionDatabaseException( string message, Object arg0 )` — Initializes a new instance of the EvolutionDatabaseException class

# EvolutionException (Class)

A generic SDK exception class from which other SDK exception types inherit.

**Namespace:** Pastel.Evolution

```csharp
public class EvolutionException : Exception
```

## Constructors (6)
- `public EvolutionException( string message )` — Initializes a new instance of the EvolutionException class
- `public EvolutionException( string message, EvolutionException innerException )` — Initializes a new instance of the EvolutionException class
- `public EvolutionException( string message, Object arg0 )` — Initializes a new instance of the EvolutionException class
- `public EvolutionException( string message, params Object[] args )` — Initializes a new instance of the EvolutionException class
- `public EvolutionException( string message, Object arg0, Object arg1 )` — Initializes a new instance of the EvolutionException class
- `public EvolutionException( string message, Object arg0, Object arg1, Object arg2 )` — Initializes a new instance of the EvolutionException class

# EvolutionNullReferenceException (Class)

**Namespace:** Pastel.Evolution

```csharp
public class EvolutionNullReferenceException : EvolutionException
```

# EvolutionVersion (Class)

**Namespace:** Pastel.Evolution

```csharp
public class EvolutionVersion
```

## Properties (4)
- `public int Build { get; internal set; }`
- `public int Major { get; internal set; }`
- `public int Minor { get; internal set; }`
- `public EvolutionVersion.SpecialBuilds Special { get; internal set; }`

## Methods (3)
- `public override bool Equals( Object obj )`
  - param `obj` (System.Object)
  - returns: Type: Boolean
- `public override int GetHashCode()`
  - returns: Type: Int32
- `public override string ToString()`
  - returns: Type: String

# ExchangeRate (Class)

Represents a hist record.

**Namespace:** Pastel.Evolution

```csharp
public class ExchangeRate : BranchedRecordBase
```

## Constructors (4)
- `public ExchangeRate()` — Creates a new instance of an exchange rate.
- `public ExchangeRate( int id )` — Creates a new instance of an exchange rate.
- `public ExchangeRate( int currencyID, DateTime date )` — Creates a new instance of an exchange rate.
- `public ExchangeRate( int currencyID, double rate, DateTime date )` — Creates a new instance of an exchange rate.

## Properties (8)
- `public double BuyingRate { get; set; }` — Gets or sets the buying rate, expressed as [home currency]/[foreign currency]. Defaults to 1.
- `public Currency Currency { get; set; }` — Gets or sets the foreign currency associated with this exchange rate.
- `public int CurrencyID { get; set; }` — Gets or sets the ID of the foreign currency associated with this exchange rate.
- `public DateTime Date { get; set; }` — Gets or sets the date for which the rate applies.
- `public override int ID { get; }` — Gets the internal record ID (0 for new, unsaved records).
- `public override long LongID { get; }`
- `public double Rate { set; }` — Sets both the buying and selling rates.
- `public double SellingRate { get; set; }` — Gets or sets the selling rate, expressed as [home currency]/[foreign currency]. Defaults to 1.

## Methods (7)
- `public static ExchangeRate[] _Select( int currencyID )`
  - param `currencyID` (System.Int32)
  - returns: Type: ExchangeRate []
- `public static ExchangeRate[] _Select( Currency owner )`
  - param `owner` (Pastel.Evolution.Currency)
  - returns: Type: ExchangeRate []
- `public static ExchangeRate[] _Select( string criteria, string sortOrder )`
  - param `criteria` (System.String)
  - param `sortOrder` (System.String)
  - returns: Type: ExchangeRate []
- `public static int Find( string criteria )` — Finds a record's database ID.
  - param `criteria` (System.String) — Specifies the criteria as a SQL where clause.
  - returns: Type: Int32 The ID of the first record found; -1 if not record was found.
- `public static int Find( int currencyID, DateTime date )` — Finds a record's database ID.
  - param `currencyID` (System.Int32)
  - param `date` (System.DateTime)
  - returns: Type: Int32 The ID of the first record found; -1 if not record was found.
- `public static int FindLatest( int currencyID, DateTime date )`
  - param `currencyID` (System.Int32)
  - param `date` (System.DateTime)
  - returns: Type: Int32
- `public static int FindLatest( int currencyID, DateTime date, bool exact )`
  - param `currencyID` (System.Int32)
  - param `date` (System.DateTime)
  - param `exact` (System.Boolean)
  - returns: Type: Int32
- `public static DataTable List( string criteria )` — Gets a list of database records.
  - param `criteria` (System.String)
  - returns: Type: DataTable
- `public static DataTable List( string criteria, string sortOrder )` — Gets a list of database records.
  - param `criteria` (System.String) — Specifies the criteria as a SQL where clause.
  - param `sortOrder` (System.String) — The SQL order by clause to use, e.g. dRateDate desc
  - returns: Type: DataTable Table containing selected records.
- `protected internal override void OnDelete()` — Removes the record from the database, provided it is not referenced by other records.
- `protected internal override void OnSave()` — Persists the record to the database.
- `public override string ToString()`
  - returns: Type: String

# ExchangeRateCollection (Class)

Represents a collection of warehouse context records.

**Namespace:** Pastel.Evolution

```csharp
public class ExchangeRateCollection
```

## Properties (2)
- `public int Count { get; }` — Gets the number of exchange rate items currently loaded into the collection.
- `public ExchangeRate this[ DateTime date ] { get; }` — Gets the exchange rate for the date specified.

## Methods (1)
- `public void Save()`

# FieldCollection (Class)

**Namespace:** Pastel.Evolution

```csharp
public class FieldCollection : ICollection,
    IEnumerable, ICloneable
```

## Properties (6)
- `public int Count { get; }`
- `public List<string> FieldNames { get; }`
- `public bool IsLocked { get; internal set; }`
- `public bool IsSynchronized { get; }`
- `public Object this[ string fieldName ] { get; set; }`
- `public Object SyncRoot { get; }`

## Methods (3)
- `public Object Clone()`
  - returns: Type: Object
- `public void CopyTo( Array array, int index )`
  - param `array` (System.Array)
  - param `index` (System.Int32)
- `public IEnumerator GetEnumerator()`
  - returns: Type: IEnumerator

# FieldCollectionManager (Class)

**Namespace:** Pastel.Evolution

```csharp
public class FieldCollectionManager : ICloneable
```

## Properties (8)
- `public FieldCollection DefaultFields { get; }`
- `public bool IsLocked { get; set; }`
- `public Object this[ string fieldName, FieldCollectionManager.FieldType fieldType ] { get; set; }`
- `public FieldCollection ModifiedFields { get; }`
- `public FieldCollection RawFields { get; }`
- `public FieldCollection ReadOnlyFields { get; }`
- `public FieldCollection UserFields { get; }`
- `public FieldCollection WritableFields { get; }`

## Methods (2)
- `public Object Clone()`
  - returns: Type: Object
- `public List<string> GetFieldNames( FieldCollectionManager.FieldType type )`
  - param `type` (Pastel.Evolution.FieldCollectionManager.FieldType)
  - returns: Type: List < String >

# GLAccount (Class)

Represents a General Ledger account.

**Namespace:** Pastel.Evolution

```csharp
public class GLAccount : AccountBase
```

## Constructors (3)
- `public GLAccount()` — Initializes a new instance of the Account class.
- `public GLAccount( int id )` — Initializes a new instance of the Account class from an existing record in the database.
- `public GLAccount( string code )` — Initializes a new instance of the Account class from an existing record in the database.

## Properties (20)
- `public override bool Active { get; set; }` — Gets or sets the account's operational state. Inactive records cannot be used when posting transactions.
- `public bool AllowJournals { get; set; }`
- `public bool AllowOnPurchasesDocuments { get; set; }` — Gets or sets whether this GLAccount can be used for Inventory Purchase transactions. Only GLAcounts that allow Purchases transactions can be used on Purchase Orders and Return To Suppliers.
- `public bool AllowOnSalesDocuments { get; set; }` — Gets or sets whether this GLAccount can be used for Inventory Sales transactions. Only GLAcounts that allow Sales transactions can be used on Sales Orders and Credit Notes.
- `public override string Code { get; set; }` — Gets or sets the account's full code. This field maps to the Master_Sub_Account database field.
- `public TaxRate DefaultCreditNoteTaxType { get; set; }` — Gets or sets the GL Account's CRN Tax Type.
- `public int DefaultCreditNoteTaxTypeID { get; set; }` — Gets or sets the GL Account's CRN Tax Type id.
- `public TaxRate DefaultGoodsReceivedTaxType { get; set; }` — Gets or sets the GL Account's GRV Tax Type.
- `public int DefaultGoodsReceivedTaxTypeID { get; set; }` — Gets or sets the GL Account's GRV Tax Type id.
- `public TaxRate DefaultInvoicingTaxType { get; set; }` — Gets or sets the GL Account's INV Tax Type.
- `public int DefaultInvoicingTaxTypeID { get; set; }` — Gets or sets the GL Account's INV Tax Type id.
- `public TaxRate DefaultReturnToSupplierTaxType { get; set; }` — Gets or sets the GL Account's RTS Tax Type.
- `public int DefaultReturnToSupplierTaxTypeID { get; set; }` — Gets or sets the GL Account's RTS Tax Type id.
- `public override string Description { get; set; }` — Gets or sets the record description.
- `public override int ID { get; }` — Gets the internal record ID (0 for new, unsaved records).
- `public override long LongID { get; }`
- `public override Module Module { get; }` — Indicates the Evolution module this account type belongs to.
- `public GLAccount SubAccountOfGLAccount { get; set; }`
- `public int SubAccountOfGLAccountID { get; set; }`
- `public GLAccount.AccountType Type { get; set; }` — Gets or sets the account's type (financial category).

## Methods (8)
- `public static int Find( string criteria )` — Attempts to find a GL account and returns its ID.
  - param `criteria` (System.String) — The SQL criteria used to locate the record, e.g. Account = '1000'
  - returns: Type: Int32 -1 if no record was found, else the id of the first account matching the criteria supplied.
  - remarks: The criteria is passed to a SQL query so use the appropriate syntax. Remember to includethe single quotes around string literals and append additional criteria with and.
- `public static int FindByCode( string code )` — Attempts to find a GL account by its account code and returns its ID.
  - param `code` (System.String) — The account code used to lookup the account.
  - returns: Type: Int32 -1 if no record was found, else the id of the first account matching the criteria supplied.
- `public static GLAccount Get( string criteria )` — Attempts to find and return a GL account object using the criteria supplied.
  - param `criteria` (System.String) — The SQL criteria used to locate the record, e.g. Account = '1000'
  - returns: Type: GLAccount The GL account object located or null if no account was found.
- `public static GLAccount GetByCode( string code )` — Attempts to find and return a GL account object by its account code.
  - param `code` (System.String) — The account code used to lookup the account.
  - returns: Type: GLAccount The GL account object located or null if no account was found.
- `public static DataTable List( string criteria )` — Returns a System.Data.DataTable object containing the database records from the Accounts table matching the supplied criteria.
  - param `criteria` (System.String) — The SQL criteria used to locate the record, e.g. Account like '1___'
  - returns: Type: DataTable A System.Data.DataTable object containing matching records.
  - remarks: The criteria is passed to an SQL query so use the appropriate syntax. Remember to includethe single quotes around string literals and append additional criteria with and.
- `protected internal override void OnDelete()` — Removes the record from the database, provided it is not referenced by other records.
- `protected internal override void OnSave()` — Persists the record to the database.
- `public override string ToString()` — Gets the record's string representation.
  - returns: Type: String The object's string representation.
  - remarks: Useful while debugging.

# GLBatch (Class)

Facilitates batch processing of GL transactions. Mainly used internally and not to be confused with journal batches.

**Namespace:** Pastel.Evolution

```csharp
public class GLBatch : CollectionBase
```

## Properties (5)
- `public GLTransaction this[ int index ] { get; set; }`
- `public double TotalCredit { get; }` — Gets the batch's total credit value.
- `public double TotalDebit { get; }` — Gets the batch's total debit value.
- `public double TotalForeignCredit { get; }` — Gets the batch's total foreign credit value.
- `public double TotalForeignDebit { get; }` — Gets the batch's total foreign debit value.

## Methods (6)
- `public void Add( GLTransaction transaction )` — Adds a GL transaction to the batch without attempting consolidation.
  - param `transaction` (Pastel.Evolution.GLTransaction)
- `public void Add( GLTransaction transaction, bool consolidate, bool strict )` — Adds a GL transaction to the batch, optionally consolidating.
  - param `transaction` (Pastel.Evolution.GLTransaction) — Specifies the transaction.
  - param `consolidate` (System.Boolean) — Specifies whether or not to consolidate.
  - param `strict` (System.Boolean) — Specifies whether or not to consolidate according to stricter criteria, i.e. reference and description values also have to match.
  - remarks: This overloaded method provides the ability to consolidate the transaction with another transaction in the batch, matching on account, module id, tax type, date, and transaction code. If the strict option is used,reference, and description are matched as well. Note: debits and credits are always consolidated separately.
- `public void OnCollectionChanged( GLBatch.BatchCollectionChangedEventArgs e )`
  - param `e` (Pastel.Evolution.GLBatch.BatchCollectionChangedEventArgs)
- `public bool OnPost()`
  - returns: Type: Boolean
- `public bool Post()` — Processes each transaction in the batch. Note: All transactions will assume the global audit number when posting.
  - returns: Type: Boolean
- `public void Remove( GLTransaction transaction )` — Removes a transaction from the batch.
  - param `transaction` (Pastel.Evolution.GLTransaction) — Specifies the transaction.
- `public void RemoveAt( int index )` — Removes a transaction from a specific location in the batch.
  - param `index` (System.Int32) — Specifies the index at which to remove the record.

# GLBatch.BatchCollectionChangedEventArgs (Class)

**Namespace:** Pastel.Evolution

```csharp
public class BatchCollectionChangedEventArgs : EventArgs
```

## Fields (2)
- `public GLBatch.BatchChangeAction Action`
- `public GLTransaction Transaction`

# GLTransaction (Class)

Represents a general ledger transaction.

**Namespace:** Pastel.Evolution

```csharp
public class GLTransaction : TransactionBase,
    ICloneable
```

## Constructors (2)
- `public GLTransaction()` — Initializes a new instance of the GLTransaction class
- `public GLTransaction( long id )` — Initializes a new instance of the GLTransaction class

## Properties (40)
- `public override AccountBase Account { get; set; }`
- `public override int AccountID { get; set; }`
- `public override string Audit { get; }`
- `public override Branch Branch { get; set; }`
- `public override int BranchID { get; internal set; }`
- `public override double Credit { get; set; }`
- `public Currency Currency { get; set; }` — Gets or sets the account's currency. null indicates home currency.
- `public int CurrencyID { get; set; }` — Gets or sets the account's currency id. 0 indicates local currency.
- `public override DateTime Date { get; set; }` — Sets the transaction date, which in turn selects the period automatically
- `public override double Debit { get; set; }` — Sets the transaction debit amount.
- `public override string Description { get; set; }` — Gets or sets the record description.
- `public double EffectiveCredit { get; set; }`
- `public double EffectiveDebit { get; set; }`
- `public double EffectiveForeignCredit { get; set; }`
- `public double EffectiveForeignDebit { get; set; }`
- `public double ExchangeRate { get; set; }`
- `public override string ExtOrderNo { get; set; }`
- `public double ForeignCredit { get; set; }`
- `public double ForeignDebit { get; set; }`
- `public double ForeignTax { get; set; }` — Gets or sets the foreign transaction tax amount (automatically rounded to 2 decimals and always posted positive).
- `public override long ID { get; }` — Gets the internal record ID (0 for new, unsaved records).
- `public int iInvLineID { get; set; }` — Gets or sets the invoice document line id.
- `public bool IsReconciled { get; set; }`
- `public bool IsSTGLDocLine { get; set; }`
- `public JobCard JobCard { get; set; }`
- `public int JobCardID { get; set; }`
- `public override ModuleID ModID { get; set; }`
- `public override Module Module { get; }`
- `public override string OrderNo { get; set; }`
- `public override Project Project { get; set; }` — Gets or sets the Project record associated with this transaction. When using Project Tracking, this field must be specified whereverapplicable.
- `public override int ProjectID { get; set; }`
- `public override string Reference { get; set; }`
- `public override string Reference2 { get; set; }`
- `public override double Tax { get; set; }` — Gets or sets the transaction tax amount (automatically rounded to 2 decimals and always posted positive).
- `public GLAccount TaxAccount { get; set; }` — Gets or sets the Tax Account.
- `public int TaxAccountID { get; set; }` — Gets or sets the Tax Account ID.
- `public override TaxRate TaxRate { get; set; }`
- `public override int TaxRateID { get; set; }`
- `public override TransactionCodeBase TransactionCode { get; set; }`
- `public override int TransactionCodeID { get; set; }`

## Methods (7)
- `public Object Clone()`
  - returns: Type: Object
- `public static long Find( string criteria )` — Finds a transaction ID.
  - param `criteria` (System.String) — The criteria passed to the SQL query. Eg. Reference = 'INV001' or Description like '%Invoice%'
  - returns: Type: Int64
- `public static DataTable List( string criteria )` — Returns a System.Data.DataTable object containing the database records from the PostGL table matching the supplied criteria.
  - param `criteria` (System.String) — The SQL criteria used to locate the record, e.g. Reference like '1___' and Audit_No = 10.0005
  - returns: Type: DataTable A System.Data.DataTable object containing matching records.
  - remarks: The criteria is passed to an SQL query so use the appropriate syntax. Remember to include the single quotes around string literals and append additional criteria with and .
- `protected internal override bool OnAllowBlockedPosting()`
  - returns: Type: Boolean
- `protected override bool OnPost()`
  - returns: Type: Boolean
- `public override string ToString()`
  - returns: Type: String
- `public override bool Validate()`
  - returns: Type: Boolean

# IBranched (Interface)

**Namespace:** Pastel.Evolution

```csharp
public interface IBranched
```

## Properties (2)
- `Branch Branch { get; }`
- `int BranchID { get; }`

# Incident (Class)

Represents an Evolution Contact Management incident.

**Namespace:** Pastel.Evolution

```csharp
public class Incident
```

## Constructors (3)
- `public Incident()` — Creates a new instance of an incident.
- `public Incident( int id )` — Creates a new instance of an incident.
- `public Incident( string reference )` — Creates a new instance of an incident.

## Properties (36)
- `public int AgentGroupID { get; internal set; }` — Gets the agent group's incident type id.
- `public Branch Branch { get; }`
- `public IncidentCategory Category { get; set; }` — Gets or sets the incident's assigned category.
- `public int CategoryID { get; set; }` — Gets or sets the incident's category id.
- `public Contract Contract { get; set; }` — Gets or sets the sales opportunity linked to the incident.
- `public int ContractID { get; set; }`
- `public DateTime CreatedDate { get; }` — Gets the original creation date/time that the incident was created.
- `public Agent CurrentAgent { get; }` — Gets the agent to whom the incident is currently assigned to. The current agent can only be changed by posting a re-assignment action.
- `public int CurrentAgentID { get; set; }`
- `public Customer Customer { get; set; }` — Gets or sets the customer account linked to the incident.
- `public string CustomerReference { get; set; }` — Gets or sets the customer's reference number.
- `public DateTime DueBy { get; set; }` — Gets or sets the incident's due date/time.
- `public EscalationGroup EscalationGroup { get; set; }` — Gets or sets the incident's assigned escalation group. Note that while Evolution will automatically assign an agent if only an escalation group is supplier, the API requires that an agent be specified.
- `public int EscalationGroupID { get; set; }` — Gets or sets the incident's escalation group id.
- `public int ID { get; }` — Gets the internal record ID (0 for new, unsaved records).
- `public IncidentType IncidentType { get; set; }` — Gets or sets the incident type.
- `public int IncidentTypeID { get; set; }` — Gets or sets the incident's incident type id.
- `public InventoryItem InventoryItem { get; set; }`
- `public int InventoryItemID { get; set; }`
- `public JobCard JobCard { get; set; }` — Gets or sets the job card linked to the incident.
- `public int JobCardID { get; set; }`
- `public DateTime ModifiedDate { get; }` — Gets the last date/time that the incident was modified.
- `public Opportunity Opportunity { get; set; }` — Gets or sets the sales opportunity linked to the incident.
- `public int OpportunityID { get; set; }`
- `public string Outline { get; set; }` — Gets or sets the incident's outline - the summary description.
- `public Person Person { get; set; }` — Gets or sets the person record related to the incident.
- `public int PersonID { get; set; }`
- `public Priority Priority { get; set; }` — Gets or sets the incident's due date/time.
- `public Project Project { get; set; }` — Gets or sets the incident's assigned project.
- `public int ProjectID { get; set; }` — Gets or sets the incident's project id.
- `public Prospect Prospect { get; set; }` — Gets or sets the prospective client related to the incident.
- `public string Reference { get; set; }` — Gets or sets the internal incident reference.
- `public bool RequireAcknowledgement { get; set; }` — Gets or sets whether or not the incident requires acknowledgement.
- `public Incident.IncidentStatus Status { get; internal set; }` — Gets or sets the incident's status.
- `public Supplier Supplier { get; set; }` — Gets or sets the supplier account linked to the incident.
- `public FieldCollection UserFields { get; }`

## Methods (6)
- `public static DataTable _ListCurrentBranch( string criteria )`
  - param `criteria` (System.String)
  - returns: Type: DataTable
- `public static DataTable _ListCurrentBranch( string criteria, bool activeOnly )`
  - param `criteria` (System.String)
  - param `activeOnly` (System.Boolean)
  - returns: Type: DataTable
- `public static int Find( string criteria )`
  - param `criteria` (System.String)
  - returns: Type: Int32
- `public static DataTable List( string criteria )`
  - param `criteria` (System.String)
  - returns: Type: DataTable
- `public static DataTable List( string criteria, bool activeOnly )`
  - param `criteria` (System.String)
  - param `activeOnly` (System.Boolean)
  - returns: Type: DataTable
- `public static DataTable List( Customer account, bool activeOnly )`
  - param `account` (Pastel.Evolution.Customer)
  - param `activeOnly` (System.Boolean)
  - returns: Type: DataTable
- `public IncidentLogEntry NewAction()`
  - returns: Type: IncidentLogEntry
- `public void OnPost( IncidentLogEntry log, bool close, bool notify )`
  - param `log` (Pastel.Evolution.IncidentLogEntry)
  - param `close` (System.Boolean)
  - param `notify` (System.Boolean)
- `public void Post( IncidentLogEntry log )` — Posts an incident log entry.
  - param `log` (Pastel.Evolution.IncidentLogEntry) — Specifies the log entry to post.
- `public void Post( IncidentLogEntry log, bool close, bool notify )` — Posts a incident log entry.
  - param `log` (Pastel.Evolution.IncidentLogEntry) — Specifies the log entry to post.
  - param `close` (System.Boolean) — Specifies whether the incident is to be closed.
  - param `notify` (System.Boolean) — Specifies whether or not notification is required.

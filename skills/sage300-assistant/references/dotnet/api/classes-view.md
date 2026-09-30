# View data-access classes

The view/data-access core: `DBLink.OpenView` returns a `View`; field and key access is through `ViewFields`/`ViewField` and `ViewKeys`/`ViewKey`. This is where read/create/post/compose logic lives.

Extracted from `Sage Accpac .NET Libraries.chm` (library 5.5.0.1). Verified 2026-09-25. See [`INDEX.md`](INDEX.md) for the full class/enum map and [`enums.md`](enums.md) for enumerations.

Classes in this file: `DBLink`, `View`, `ViewFields`, `ViewField`, `ViewKeys`, `ViewKey`, `ViewFieldPresentationList`, `ViewReturnCode`, `ViewInternal`

---

## DBLink class

Represents a database link or connection to an ACCPAC company or system database.

**Namespace:** ACCPAC.Advantage &nbsp;·&nbsp; **Assembly:** ACCPAC.Advantage.dll

```csharp
public class DBLink : IDBLinkComInterop, IDisposable
```

An object of this class cannot be created directly by applications. Instead, it should be obtained from the Session object's OpenDBLink method.

### Properties

| Name | Description |
|---|---|
| `ActiveApplications` | Gets an ActiveApplications object that stores details of all the applications activated for this company database. |
| `Company` | Gets a Company object that stores details of the company profile as set up in Common Services. |
| `Database` | Gets the database engine of the current database connection. |
| `FiscalCalendar` | Gets a FiscalCalendar object that provides methods to access the fiscal calendar set up in the company. |
| `Flags` | Gets the database flags used to open the link. The flags control the access mode of the database connection. |
| `LastReturnCode` | Gets the ACCPAC database layer return code of the most recent call. |
| `Parent` | Gets the Session object that created this object. |
| `Type` | Gets the type of database the current link connects to. |

### Methods

| Name | Description |
|---|---|
| `CreateProfile` | Creates a UI Customization Profile in Administrative Services. |
| `CreateViewTables` | Instructs a view to create its tables on the current database connection. |
| `Dispose` | Closes the database connection and frees up resources used by the object. |
| `DropViewTables` | Instructs a view to drop its tables on the current database connection. |
| `Finalize` | DBLink class finalizer |
| `GetCurrency` | Retrieves details of the specified currency code, and returns a Currency object that represents the currency. |
| `GetCurrencyRate` | Retrieves the exchange rate between the specified currency codes. |
| `GetCurrencyRateComposite` | Retrieves the composite exchange rate between the specified currency codes. |
| `GetCurrencyRateFloating` | Retrieves the floating exchange rate between the specified currency codes. |
| `GetCurrencyRateTypeDescription` | Retrieves the description of a given rate type code. |
| `GetCurrencyTable` | Retrieves details of a currency table set up in Common Services. |
| `GetProcessServerSetup` | Obtains a ProcessServerSetup object for a specific view. |
| `GetProfileCustomizations` | Retrieves the UI Customization settings of the supplied profile ID and screen identifier (uiKey). |
| `GetProfiles` | Retrieves a list of all UI Customization Profiles set up in Administrative Services. |
| `GetUserCustomizations` | Retreives the effective UI customization settings of the current user on the UI identified by the supplied UI key. |
| `OpenView` | Opens an ACCPAC view. |
| `ParamGet` | Retrieves a list of parameters stored in a view. |
| `SaveProfileCustomizations` | Saves the UI customization profile settings. |
| `SecCheck` | Checks access right of the signed-on user on the specified security resource ID. |
| `TransactionBegin` | Begins a transaction on the current database connection. |
| `TransactionCommit` | Commits the most recent transaction. |
| `TransactionGetLevel` | Gets the current transaction level. |
| `TransactionRollback` | Rolls back the most recent transaction. |

### Method details

#### DBLink.CreateProfile

```csharp
public void CreateProfile(
    string profileID,
    string profileDesc
    )
```

- `profileID` (String) — Profile ID of the profile.
- `profileDesc` (String) — Description of the profile.

This method is available only if the current user is the administrator and if the database link used is a read-write system link.

#### DBLink.CreateViewTables

```csharp
public void CreateViewTables(
    string viewID
    )
```

- `viewID` (String) — The Roto ID of the view to load and create the tables.

#### DBLink.Dispose

```csharp
public void Dispose()
```

#### DBLink.DropViewTables

```csharp
public void DropViewTables(
    string viewID
    )
```

- `viewID` (String) — The Roto ID of the view to load and drop the tables.

#### DBLink.Finalize

```csharp
protected override void Finalize()
```

#### DBLink.GetCurrency

```csharp
public Currency GetCurrency(
    string currencyCode
    )
```

- `currencyCode` (String) — Currency code to retrieve.

**Returns:** Returns a Currency object that represents the currency.

#### DBLink.GetCurrencyRate

```csharp
public CurrencyRate GetCurrencyRate(
    string homeCurrency,
    string rateType,
    string sourceCurrency,
    DateTime date
    )
```

- `homeCurrency` (String) — Home (functional) currency code.
- `rateType` (String) — Currency rate type code.
- `sourceCurrency` (String) — Source currency code.
- `date` (DateTime) — Date to look up the exchange rate.

**Returns:** Returns a CurrencyRate object that contains details of the exchange rate.

#### DBLink.GetCurrencyRateComposite

```csharp
public CurrencyRate GetCurrencyRateComposite(
    string homeCurrency,
    string rateType,
    string sourceCurrency,
    DateTime date
    )
```

- `homeCurrency` (String) — Home (functional) currency code.
- `rateType` (String) — Currency rate type code.
- `sourceCurrency` (String) — Source currency code.
- `date` (DateTime) — Date to look up the exchange rate.

**Returns:** Returns a CurrencyRate object that contains details of the exchange rate.

#### DBLink.GetCurrencyRateFloating

```csharp
public CurrencyRate GetCurrencyRateFloating(
    string homeCurrency,
    string rateType,
    string sourceCurrency,
    DateTime date
    )
```

- `homeCurrency` (String) — Home (functional) currency code.
- `rateType` (String) — Currency rate type code.
- `sourceCurrency` (String) — Source currency code.
- `date` (DateTime) — Date to look up the exchange rate.

**Returns:** Returns a CurrencyRate object that contains details of the exchange rate.

#### DBLink.GetCurrencyRateTypeDescription

```csharp
public bool GetCurrencyRateTypeDescription(
    string rateType,
    out string rateTypeDescription
    )
```

- `rateType` (String) — Rate type code.
- `rateTypeDescription` (String %) — Returns the description of the supplied rate type code.

**Returns:** Returns whether the specified rate type code is found.

#### DBLink.GetCurrencyTable

```csharp
public CurrencyTable GetCurrencyTable(
    string currencyCode,
    string rateType
    )
```

- `currencyCode` (String) — Currency code.
- `rateType` (String) — Currency rate type code.

**Returns:** Returns a CurrencyTable object that contains details of the currency table.

#### DBLink.GetProcessServerSetup

```csharp
public ProcessServerSetup GetProcessServerSetup(
    string viewID
    )
```

- `viewID` (String) — View ID of the view the ProcessServerSetup object is intended for.

**Returns:** Returns a ProcessServerSetup object for the specified view.

#### DBLink.GetProfileCustomizations

```csharp
public string[] GetProfileCustomizations(
    string profileID,
    string uiKey
    )
```

- `profileID` (String) — Profile ID.
- `uiKey` (String) — A key that identifies a particular UI. UI keys are individually defined by each UI.

**Returns:** Returns an array of customization settings. Returns an empty array if there is no customization settings stored for the supplied profile ID and UI key.

This method is available only if the current user is the administrator.

#### DBLink.GetProfiles

```csharp
public void GetProfiles(
    out string[] profileIDs,
    out string[] profileDescs
    )
```

- `profileIDs` (String[] %) — Returns an array of profile IDs.
- `profileDescs` (String[] %) — Returns an array of profile descriptions. Any item in this array corresponds to the item in the profileIDs array with the same position.

This method is available only if the current user is the administrator.

#### DBLink.GetUserCustomizations

```csharp
public string[] GetUserCustomizations(
    string uiKey
    )
```

- `uiKey` (String) — UI key identifying a UI.

**Returns:** Returns an array of customization settings. Returns an empty array if there is no customization settings effective for the current user.

#### DBLink.OpenView

```csharp
public View OpenView(
    string viewID
    )
```

- `viewID` (String) — Roto ID of the view to open. The Roto ID is defined by the application.

**Returns:** Returns a View object that represents the view.

```csharp
public View OpenView(
    string viewID,
    ViewOpenModes openModes,
    int prefetch,
    ViewOpenDirectives openDirectives,
    Object openExtra,
    ProcessServerSetup processServerSetup
    )
```

- `viewID` (String) — Roto ID of the view.
- `openModes` (ViewOpenModes) — The modes control a variety of view behaviors.
- `prefetch` (Int32) — Number of records to pre-fetch when the view is opened.
- `openDirectives` (ViewOpenDirectives) — Specifies how the view should be used. The caller can specify here the a view should be opened using viewInstanceOpen.
- `openExtra` (Object) — Application specific data to be passed to the view when it is opened. The data type and format should be understood by both the caller and the view.
- `processServerSetup` (ProcessServerSetup) — A ProcessServerSetup object that stores configuration settings for Process Server. Specify null if Process Server should not be used with the view.

**Returns:** Returns a View object that represents the view.

#### DBLink.ParamGet

```csharp
public Object[] ParamGet(
    string viewID,
    int[] fieldIDs
    )
```

- `viewID` (String) — Roto ID of the view to retrieve the parameters.
- `fieldIDs` (Int32[]) — An array of field IDs where the parameters should be retrieved.

**Returns:** Returns an array of parameter values read from the view. The parameter values returned in the array appears in the same order as the corresponding field IDs specified in the fieldIDs parameter.

This method is applicable only to views that are designed to store parameters of an application. These views typically have one and only one record. Internally, this method opens the specified view, fetches the first record, and returns the values of the specified field IDs. In a networked environment, this method is more efficient than manually opening a view, fetching and obtaining field values, since this method only takes one network call and all processing is done on the server.

#### DBLink.SaveProfileCustomizations

```csharp
public void SaveProfileCustomizations(
    string[] profileIDs,
    string uiKey,
    string[] hiddenControls
    )
```

- `profileIDs` (String[]) — Profile ID.
- `uiKey` (String) — A key that identifies UI.
- `hiddenControls` (String[]) — An array of control names that should be hidden.

This method is available only if the current user is the administrator and if the database link used is a read-write system link.

#### DBLink.SecCheck

```csharp
public bool SecCheck(
    string resourceID
    )
```

- `resourceID` (String) — Security resource ID to perform the check.

**Returns:** Returns whether the user has access rights on the resource identified by the security resource ID.

#### DBLink.TransactionBegin

```csharp
public int TransactionBegin()
```

**Returns:** Returns the transaction level after the trasaction has begun.

#### DBLink.TransactionCommit

```csharp
public int TransactionCommit()
```

**Returns:** Returns the transaction level after the trasaction was committed.

#### DBLink.TransactionGetLevel

```csharp
public int TransactionGetLevel()
```

**Returns:** Returns the current transaction level.

#### DBLink.TransactionRollback

```csharp
public int TransactionRollback()
```

**Returns:** Returns the transaction level after the trasaction was rolled back.

---

## View class

Represents an ACCPAC view.

**Namespace:** ACCPAC.Advantage &nbsp;·&nbsp; **Assembly:** ACCPAC.Advantage.dll

```csharp
public class View : IViewComInterop, IDisposable
```

An object of this class cannot be created directly by applications. It should be obtained from the DBLink object's OpenView method.

### Properties

| Name | Description |
|---|---|
| `CheckDuplicateKeys` | Returns/sets whether to check keys for duplicates. |
| `CompositeNames` | Gets a list of IDs of the views the caller must explicitly compose. |
| `Description` | Gets the description of the view. |
| `Dirty` | Indicates whether the current record is dirty. A record is dirty if any of the field values was modified by the application. |
| `Exists` | Indicates whether the current primary key field values identify an existing record in the database. |
| `Fields` | Gets the ViewFields object that provides access to individual fields of the current view. |
| `HeaderLinkedKeyFieldCount` | Reserved for ACCPAC internal use only. |
| `InstanceNoncascading` | Reserved. |
| `InstanceNonheritable` | Gets whether the composite views implicitly opened by the current view inherit the additional parameters of the current view when it was opened. |
| `InstancePrefetch` | Gets the number of records fetched at a time, if the view was opened read-only. |
| `InstanceProtcol` | Returns a set of flags describing in detail the protocol the view implements. |
| `InstanceRawPut` | Reserved. |
| `InstanceReadonly` | Gets whether the view is opened in read-only mode. |
| `InstanceSecurity` | Gets the access rights the current user has on the view. |
| `InstanceUnrevisioned` | Gets whether revisioning is suppressed. |
| `InstanceUnvalidated` | Gets whether validation is suppressed. |
| `Keys` | Gets the ViewKeys object that provides access to all keys exposed by the current view. |
| `LastReturnCode` | Gets the view return code of the last view operation. |
| `Order` | Gets/sets the current selected key on the view. Changing the selected key affects the order in which records are fetched from the view. |
| `Parent` | Gets the DBLink object that created the current View object. |
| `RecordBookmark` | Gets a bookmark of the current record. A bookmark uniquely identifies a record in a view. |
| `RecordNumber` | Gets the record number of the current record. |
| `ReferentialIntegrity` | Gets/sets the current referential integrity flags of the view. |
| `Security` | Gets the access rights the current user has on the view. |
| `SystemAccess` | Gets/sets the current system access mode of the view. |
| `TemplateDate` | Gets the date of the template used by the view. |
| `TemplateVersion` | Gets the version of the template used by the view. |
| `Type` | Gets the type of the view. |
| `UnpostedRevisions` | Indicates whether there are unposted revisions in the view. |
| `UseRecordNumbering` | Gets/sets whether the View object would generate a record number for every record fetched. Record numbering can be used when accessing views that use sequenced revision lists. |
| `ViewID` | Gets the view ID of the current view. |

### Methods

| Name | Description |
|---|---|
| `BlkGet` | Obtains the field values of multiple fields. |
| `BlkPut` | Changes the field values of multiple fields. |
| `Browse` | Starts a query and establishes the direction for subsequent calls that fetch records from the view. |
| `Cancel` | Cancels any unsaved changes in the view's revision list. |
| `Clone` | Clones the current view object. |
| `Compose` | Performs composition on the supplied list of composite views. |
| `Delete` | Deletes the current record from the database. |
| `Dispose` | Closes the view and releases all resources used by the object. |
| `Fetch` | Retrieves the next record in the view according to the primary key field values of the current record, as well as the current filter and direction set by a previous call to Browse . |
| `FilterCount` | — |
| `FilterDelete` | Deletes a set of records from the view that satisfy the supplied filter. |
| `FilterFetch` | Retrieves the next record in the view according to the primary key field values of the current record, as well as the current filter and direction. |
| `FilterSelect` | Starts a query and establishes the direction for subsequent calls that fetch records from the view. |
| `Finalize` | View class finalizer |
| `GetViewInternal` | Reserved for ACCPAC internal use only. |
| `GoBottom` | Navigates to the last record in the view according to the current browse filter and direction. |
| `GoNext` | Retrieves the next record in the view according to the primary key field values of the current record, as well as the current filter and direction set by a previous call to Browse . |
| `GoPrev` | Retrieves the previous record in the view according to the primary key field values of the current record, as well as the current filter and direction set by a previous call to Browse . |
| `GotoBookmark` | Locates and retrieves the record identified by the supplied bookmark. |
| `GoTop` | Navigates to the first record in the view according to the current browse filter and direction. |
| `GotoRecordNumber` | Locates and retrieves the record identified by the supplied record number. |
| `Init` | Initializes the field values of the current record. The field values are initialized with the default values defined in the view. |
| `InitPrimaryKeyFields` | Initializes the primary key field values of the current record the same as the record specified by the supplied bookmark. This method should be used before inserting records to views that use sequenced revision lists. |
| `Insert` | Inserts the current record into the database. |
| `InternalSet` | Internal use only. |
| `MacroAppend` | Appends a command to the current macro that is being recorded. |
| `Post` | Posts unsaved changes to the view. This method is used primarily on header views where the call has a cascading effect that causes its detail views to update the unposted revisions. |
| `Process` | Performs view-specific processing. |
| `Read` | Locates and retrieves the record in the view according to the primary key field values of the current record. |
| `RecordClear` | Blanks, zeros, or defaults the fields in the view. |
| `RecordCreate` | Generates a unique nonexistent key, and blanks, zeroes, or defaults the remaining fields in the view. |
| `RecordGenerate` | Generates a unique non-existent key, and blanks, zeros or defaults the remaining fields in the view. |
| `ResetRecordNumbers` | Resets record numbers generated by the view. |
| `RevisionCancel` | Rolls back any pending changes to the specified revision level. |
| `RevisionExists` | Checks whether the current record exists within the specified revision level. |
| `RevisionPost` | Commits any pending changes to the specified revision level. |
| `RevisionUnposted` | Checks whether the specified revision level has unposted changes. |
| `TableEmpty` | Deletes all records in the database table using the fastest method available. |
| `Unlock` | Unlocks a previously locked record by Fetch or Read . |
| `Update` | Updates the current record to the database. |
| `Verify` | Validates the field values of the current record. |

### Method details

#### View.BlkGet

```csharp
public Object[] BlkGet(
    int[] fieldIDs
    )
```

- `fieldIDs` (Int32[]) — An array of IDs of the fields from which to retrieve the values.

**Returns:** Returns an array of field values. The values are stored in the same order as their corresponding field IDs in the fieldIDs parameter.

#### View.BlkPut

```csharp
public void BlkPut(
    int[] fieldIDs,
    Object[] fieldValues,
    bool verifyValues
    )
```

- `fieldIDs` (Int32[]) — An array of IDs of the fields of which the values should be changed.
- `fieldValues` (Object[]) — An array of new field values. The new values should appear in the array in the same order as their corresponding fieldIDs defined in the fieldIDs parameter.
- `verifyValues` (Boolean) — Indicates whether validation should be performed by the view on the new values.

#### View.Browse

```csharp
public void Browse(
    string filter,
    bool ascending
    )
```

- `filter` (String) — A filter that restricts the records that will be retrieved.
- `ascending` (Boolean) — Indiates whether subsequent records will be fetched in ascending or decending order.

Calling Browse does not change the ordering of records being fetched from the view. To control the ordering, use the Order property to select a key.

#### View.Cancel

```csharp
public void Cancel()
```

```csharp
public void Cancel(
    int[] inFieldIDs,
    out Object[] outFieldValues
    )
```

- `inFieldIDs` (Int32[]) — An array of IDs of fields of which the values should be returned if a record was successfully retrieved.
- `outFieldValues` (Object[] %) — Returns an array of field values of the requested fields. Returns null if no record was retrieved.

#### View.Clone

```csharp
public View Clone()
```

**Returns:** Returns the cloned View object.

Cloning a View object creates a new View object with the same properties set for the current view. Internally, a new view instance is created. However, the current composition is not inherited by the cloned view. So, the cloned view is not composed to any composite views and the caller is responsible for calling Compose to set up composition properly.

#### View.Compose

```csharp
public void Compose(
    View[] views
    )
```

- `views` (View[]) — An array of View objects that represent the composite views. The composite views must appear in the array in the same order as what the view expects. If composition of a certain sub-view is not required, the corresponding item in the array should be set as null.

Each view predefines a list of composite views it expects to compose, and the order of those view instances appearing in the array when calling Compose. Use the CompositeNames property to find out the list of composite views and their order the current view expects.

#### View.Delete

```csharp
public void Delete()
```

#### View.Dispose

```csharp
public void Dispose()
```

#### View.Fetch

```csharp
public bool Fetch(
    bool lockRecord
    )
```

- `lockRecord` (Boolean) — Indicates whether the record should be locked after it is retrieved.

**Returns:** Returns whether any more record is available in the view and is retrieved.

```csharp
public bool Fetch(
    bool lockRecord,
    int[] putFieldIDs,
    Object[] putFieldValues,
    int[] inFieldIDs,
    out Object[] outFieldValues,
    out int recordNumber
    )
```

- `lockRecord` (Boolean) — Indicates whether the record should be locked after it is retrieved.
- `putFieldIDs` (Int32[]) — An array of IDs of the fields of which the values should first be modified before performing record fetching. The new values are specified in the putFieldValues parameter.
- `putFieldValues` (Object[]) — An array of field values that should first be set to the view before performing record fetching. The values should appear in the array in the same order as the correponding field IDs specified in the putFieldIDs parameter.
- `inFieldIDs` (Int32[]) — An array of IDs of fields of which the values should be returned if a record was successfully retrieved.
- `outFieldValues` (Object[] %) — Returns an array of field values of the requested fields. Returns null if no record was retrieved.
- `recordNumber` (Int32 %) — Returns the record number if a record was retrieved.

**Returns:** Returns whether any more record is available in the view and is retrieved.

#### View.FilterCount

```csharp
public int FilterCount(
    string filter,
    int flags
    )
```

- `filter` (String) — The Filter to count.
- `flags` (Int32) — Reserved. Set to 0.

**Returns:** Returns the number of records that match the given filter.

#### View.FilterDelete

```csharp
public void FilterDelete(
    string filter,
    ViewFilterStrictness strictness
    )
```

- `filter` (String) — The filter to be applied.
- `strictness` (ViewFilterStrictness) — Controls how the deletion operation acts on multiple tables.

#### View.FilterFetch

```csharp
public bool FilterFetch(
    bool lockRecord
    )
```

- `lockRecord` (Boolean) — Indicates whether the record should be locked after it is retrieved.

**Returns:** Returns whether any more record is available in the view and is retrieved.

#### View.FilterSelect

```csharp
public void FilterSelect(
    string filter,
    bool ascending,
    int order,
    ViewFilterOrigin origin
    )
```

- `filter` (String) — A filter that restricts the records that will be retrieved.
- `ascending` (Boolean) — Indiates whether subsequent records will be fetched in ascending or decending order.
- `order` (Int32) — The key index to select on the view.
- `origin` (ViewFilterOrigin) — The range of records the filter would affect.

#### View.Finalize

```csharp
protected override void Finalize()
```

#### View.GetViewInternal

```csharp
public ViewInternal GetViewInternal(
    int key
    )
```

- `key` (Int32)

#### View.GoBottom

```csharp
public bool GoBottom()
```

**Returns:** Returns whether a record was retrieved. Since this method always retrieves the last record, the return value is false only if there is no record that satisfies the current filter.

```csharp
public bool GoBottom(
    int[] inFieldIDs,
    out Object[] outFieldValues,
    out int recordNumber
    )
```

- `inFieldIDs` (Int32[]) — An array of IDs of fields of which the values should be returned if a record was successfully retrieved.
- `outFieldValues` (Object[] %) — Returns an array of field values of the requested fields. Returns null if no record was retrieved.
- `recordNumber` (Int32 %) — Returns the record number if a record was retrieved.

**Returns:** Returns whether a record was retrieved. Since this method always retrieves the last record, the return value is false only if there is no record that satisfies the current filter.

#### View.GoNext

```csharp
public bool GoNext()
```

**Returns:** Returns whether any more record is available in the view and is retrieved.

```csharp
public bool GoNext(
    int[] putFieldIDs,
    Object[] putFieldValues,
    int[] inFieldIDs,
    out Object[] outFieldValues,
    out int recordNumber
    )
```

- `putFieldIDs` (Int32[]) — An array of IDs of the fields of which the values should first be modified before performing record fetching. The new values are specified in the putFieldValues parameter.
- `putFieldValues` (Object[]) — An array of field values that should first be set to the view before performing record fetching. The values should appear in the array in the same order as the correponding field IDs specified in the putFieldIDs parameter.
- `inFieldIDs` (Int32[]) — An array of IDs of fields of which the values should be returned if a record was successfully retrieved.
- `outFieldValues` (Object[] %) — Returns an array of field values of the requested fields. Returns null if no record was retrieved.
- `recordNumber` (Int32 %) — Returns the record number if a record was retrieved.

**Returns:** Returns whether any more record is available in the view and is retrieved.

#### View.GoPrev

```csharp
public bool GoPrev()
```

**Returns:** Returns whether any more record is available in the view and is retrieved.

```csharp
public bool GoPrev(
    int[] putFieldIDs,
    Object[] putFieldValues,
    int[] inFieldIDs,
    out Object[] outFieldValues,
    out int recordNumber
    )
```

- `putFieldIDs` (Int32[]) — An array of IDs of the fields of which the values should first be modified before performing record fetching. The new values are specified in the putFieldValues parameter.
- `putFieldValues` (Object[]) — An array of field values that should first be set to the view before performing record fetching. The values should appear in the array in the same order as the correponding field IDs specified in the putFieldIDs parameter.
- `inFieldIDs` (Int32[]) — An array of IDs of fields of which the values should be returned if a record was successfully retrieved.
- `outFieldValues` (Object[] %) — Returns an array of field values of the requested fields. Returns null if no record was retrieved.
- `recordNumber` (Int32 %) — Returns the record number if a record was retrieved.

**Returns:** Returns whether any more record is available in the view and is retrieved.

#### View.GotoBookmark

```csharp
public bool GotoBookmark(
    Object bookmark
    )
```

- `bookmark` (Object) — Bookmark that identifies the intended record.

**Returns:** Returns whether the intended record exists in the view and is retrieved.

```csharp
public bool GotoBookmark(
    Object bookmark,
    int[] inFieldIDs,
    out Object[] outFieldValues,
    out int recordNumber
    )
```

- `bookmark` (Object) — Bookmark that identifies the intended record.
- `inFieldIDs` (Int32[]) — An array of IDs of fields of which the values should be returned if a record was successfully retrieved.
- `outFieldValues` (Object[] %) — Returns an array of field values of the requested fields. Returns null if no record was retrieved.
- `recordNumber` (Int32 %) — Returns the record number if a record was retrieved.

**Returns:** Returns whether the intended record exists in the view and is retrieved.

#### View.GoTop

```csharp
public bool GoTop()
```

**Returns:** Returns whether a record was retrieved. Since this method always retrieves the first record, the return value is false only if there is no record that satisfies the current filter.

```csharp
public bool GoTop(
    int[] inFieldIDs,
    out Object[] outFieldValues,
    out int recordNumber
    )
```

- `inFieldIDs` (Int32[]) — An array of IDs of fields of which the values should be returned if a record was successfully retrieved.
- `outFieldValues` (Object[] %) — Returns an array of field values of the requested fields. Returns null if no record was retrieved.
- `recordNumber` (Int32 %) — Returns the record number if a record was retrieved.

**Returns:** Returns whether a record was retrieved. Since this method always retrieves the first record, the return value is false only if there is no record that satisfies the current filter.

#### View.GotoRecordNumber

```csharp
public bool GotoRecordNumber(
    int recordNumber
    )
```

- `recordNumber` (Int32) — Record number that identifies the intended record.

**Returns:** Returns whether the intended record exists in the view and is retrieved.

This method is available only if UseRecordNumbering is enabled for the view.

```csharp
public bool GotoRecordNumber(
    int recordNumber,
    int[] inFieldIDs,
    out Object[] outFieldValues
    )
```

- `recordNumber` (Int32) — Record number that identifies the intended record.
- `inFieldIDs` (Int32[]) — An array of IDs of fields of which the values should be returned if a record was successfully retrieved.
- `outFieldValues` (Object[] %) — Returns an array of field values of the requested fields. Returns null if no record was retrieved.

**Returns:** Returns whether the intended record exists in the view and is retrieved.

This method is available only if UseRecordNumbering is enabled for the view.

#### View.Init

```csharp
public void Init()
```

```csharp
public void Init(
    int[] putFieldIDs,
    Object[] putFieldValues,
    int[] inFieldIDs,
    out Object[] outFieldValues,
    out int recordNumber
    )
```

- `putFieldIDs` (Int32[]) — An array of IDs of the fields of which the values should first be modified before performing record fetching. The new values are specified in the putFieldValues parameter.
- `putFieldValues` (Object[]) — An array of field values that should first be set to the view before performing record fetching. The values should appear in the array in the same order as the correponding field IDs specified in the putFieldIDs parameter.
- `inFieldIDs` (Int32[]) — An array of IDs of fields of which the values should be returned if a record was successfully retrieved.
- `outFieldValues` (Object[] %) — Returns an array of field values of the requested fields.
- `recordNumber` (Int32 %) — Returns the record number if a record was retrieved.

#### View.InitPrimaryKeyFields

```csharp
public void InitPrimaryKeyFields(
    ref Object bookmark
    )
```

- `bookmark` (Object %) — Bookmark of the record of which the primary key field values should be retrieved.

This method is useful only for inserting records into views that use sequenced revision lists. Views that use sequenced revision lists maintain the order in which records are inserted. Initializing the key field values to be the same as an existing record before inserting the new record inserts it after the specified record in a sequenced manner.

#### View.Insert

```csharp
public void Insert()
```

```csharp
public void Insert(
    int[] putFieldIDs,
    Object[] putFieldValues,
    int[] inFieldIDs,
    out Object[] outFieldValues,
    out int recordNumber
    )
```

- `putFieldIDs` (Int32[]) — An array of IDs of the fields of which the values should first be modified before performing record fetching. The new values are specified in the putFieldValues parameter.
- `putFieldValues` (Object[]) — An array of field values that should first be set to the view before performing record fetching. The values should appear in the array in the same order as the correponding field IDs specified in the putFieldIDs parameter.
- `inFieldIDs` (Int32[]) — An array of IDs of fields of which the values should be returned if a record was successfully retrieved.
- `outFieldValues` (Object[] %) — Returns an array of field values of the requested fields.
- `recordNumber` (Int32 %) — Returns the record number if a record was retrieved.

#### View.InternalSet

```csharp
public void InternalSet(
    int settings
    )
```

- `settings` (Int32)

#### View.MacroAppend

```csharp
public void MacroAppend(
    string command
    )
```

- `command` (String) — Command to append to the macro.

#### View.Post

```csharp
public void Post()
```

```csharp
public void Post(
    int[] putFieldIDs,
    Object[] putFieldValues,
    int[] inFieldIDs,
    out Object[] outFieldValues
    )
```

- `putFieldIDs` (Int32[]) — An array of IDs of the fields of which the values should first be modified before performing record fetching. The new values are specified in the putFieldValues parameter.
- `putFieldValues` (Object[]) — An array of field values that should first be set to the view before performing record fetching. The values should appear in the array in the same order as the correponding field IDs specified in the putFieldIDs parameter.
- `inFieldIDs` (Int32[]) — An array of IDs of fields of which the values should be returned if a record was successfully retrieved.
- `outFieldValues` (Object[] %) — Returns an array of field values of the requested fields.

#### View.Process

```csharp
public void Process()
```

```csharp
public void Process(
    int[] putFieldIDs,
    Object[] putFieldValues,
    int[] inFieldIDs,
    out Object[] outFieldValues
    )
```

- `putFieldIDs` (Int32[]) — An array of IDs of the fields of which the values should first be modified before performing record fetching. The new values are specified in the putFieldValues parameter.
- `putFieldValues` (Object[]) — An array of field values that should first be set to the view before performing record fetching. The values should appear in the array in the same order as the correponding field IDs specified in the putFieldIDs parameter.
- `inFieldIDs` (Int32[]) — An array of IDs of fields of which the values should be returned if a record was successfully retrieved.
- `outFieldValues` (Object[] %) — Returns an array of field values of the requested fields.

#### View.Read

```csharp
public bool Read(
    bool lockRecord
    )
```

- `lockRecord` (Boolean) — Indicates whether the record should be locked after it is retrieved.

**Returns:** Returns whether the intended record exists in the view and is retrieved.

```csharp
public bool Read(
    bool lockRecord,
    int[] putFieldIDs,
    Object[] putFieldValues,
    int[] inFieldIDs,
    out Object[] outFieldValues,
    out int recordNumber
    )
```

- `lockRecord` (Boolean) — Indicates whether the record should be locked after it is retrieved.
- `putFieldIDs` (Int32[]) — An array of IDs of the fields of which the values should first be modified before performing record fetching. The new values are specified in the putFieldValues parameter.
- `putFieldValues` (Object[]) — An array of field values that should first be set to the view before performing record fetching. The values should appear in the array in the same order as the correponding field IDs specified in the putFieldIDs parameter.
- `inFieldIDs` (Int32[]) — An array of IDs of fields of which the values should be returned if a record was successfully retrieved.
- `outFieldValues` (Object[] %) — Returns an array of field values of the requested fields. Returns null if no record was retrieved.
- `recordNumber` (Int32 %) — Returns the record number if a record was retrieved.

**Returns:** Returns whether the intended record exists in the view and is retrieved.

#### View.RecordClear

```csharp
public void RecordClear()
```

#### View.RecordCreate

```csharp
public void RecordCreate(
    ViewRecordCreate flags
    )
```

- `flags` (ViewRecordCreate) — Use the flags to control how the key is generated.

#### View.RecordGenerate

```csharp
public void RecordGenerate(
    bool insertRecord
    )
```

- `insertRecord` (Boolean) — Specfies whether this method should also immediately insert the generated record into the database.

#### View.ResetRecordNumbers

```csharp
public void ResetRecordNumbers()
```

When UseRecordNumbering is enabled for the view, a record number is generated by the view whenever it fetches a record. An intenal table is built that maps the record's bookmark to the generated record number. This method resets the internal mapping table and forces the view to regenerate record numbers when subsequently fetching records. This method should be used on detail views when the header view was changed that results in a different set of detail records to become available.

#### View.RevisionCancel

```csharp
public void RevisionCancel(
    int level
    )
```

- `level` (Int32) — Revision level.

#### View.RevisionExists

```csharp
public bool RevisionExists(
    int level
    )
```

- `level` (Int32) — Revision level.

**Returns:** Returns whether the current record exists within the specified revision level.

#### View.RevisionPost

```csharp
public void RevisionPost(
    int level
    )
```

- `level` (Int32) — Revision level.

#### View.RevisionUnposted

```csharp
public bool RevisionUnposted(
    int level
    )
```

- `level` (Int32) — Revision level.

**Returns:** Returns whether the specified revision level has unposted changes.

#### View.TableEmpty

```csharp
public void TableEmpty()
```

#### View.Unlock

```csharp
public void Unlock()
```

#### View.Update

```csharp
public void Update()
```

```csharp
public void Update(
    int[] putFieldIDs,
    Object[] putFieldValues,
    int[] inFieldIDs,
    out Object[] outFieldValues,
    out int recordNumber
    )
```

- `putFieldIDs` (Int32[]) — An array of IDs of the fields of which the values should first be modified before performing record fetching. The new values are specified in the putFieldValues parameter.
- `putFieldValues` (Object[]) — An array of field values that should first be set to the view before performing record fetching. The values should appear in the array in the same order as the correponding field IDs specified in the putFieldIDs parameter.
- `inFieldIDs` (Int32[]) — An array of IDs of fields of which the values should be returned if a record was successfully retrieved.
- `outFieldValues` (Object[] %) — Returns an array of field values of the requested fields.
- `recordNumber` (Int32 %) — Returns the record number if a record was retrieved.

#### View.Verify

```csharp
public void Verify()
```

```csharp
public void Verify(
    int[] putFieldIDs,
    Object[] putFieldValues,
    int[] inFieldIDs,
    out Object[] outFieldValues
    )
```

- `putFieldIDs` (Int32[]) — An array of IDs of the fields of which the values should first be modified before performing record fetching. The new values are specified in the putFieldValues parameter.
- `putFieldValues` (Object[]) — An array of field values that should first be set to the view before performing record fetching. The values should appear in the array in the same order as the correponding field IDs specified in the putFieldIDs parameter.
- `inFieldIDs` (Int32[]) — An array of IDs of fields of which the values should be returned if a record was successfully retrieved.
- `outFieldValues` (Object[] %) — Returns an array of field values of the requested fields.

---

## ViewFields class

Provides access to ViewField objects that include all fields exposed by a view.

**Namespace:** ACCPAC.Advantage &nbsp;·&nbsp; **Assembly:** ACCPAC.Advantage.dll

```csharp
public class ViewFields : IViewFieldsComInterop, IDisposable
```

An object of this class cannot be create directly by applications. It should be obtained from the View object's Fields property.

### Properties

| Name | Description |
|---|---|
| `Count` | Gets the number of fields exposed by the view. |
| `Item` | Gets the field object based on the zero-based index of the field appearing in the collection. Note that the index denotes the position of the field stored in the collection, and does not correspond to the field ID defined in the view. |
| `Parent` | Gets the View object that created the current object. |

### Methods

| Name | Description |
|---|---|
| `Dispose` | ViewFields object disposal |
| `FieldByID` | Gets a field object identified by the field ID. The field ID is the index of the field as defined in the view. |
| `FieldByName` | Gets a field object identified by the field name. |

### Method details

#### ViewFields.Dispose

```csharp
public void Dispose()
```

#### ViewFields.FieldByID

```csharp
public ViewField FieldByID(
    int fieldID
    )
```

- `fieldID` (Int32) — Field ID of the desired field.

**Returns:** Returns the ViewField object of the desired field.

The field ID of a field is defined by the view. Field IDs of fields in a view might not be contiguous, and do not relate to the zero-based index of the field in the collection.

#### ViewFields.FieldByName

```csharp
public ViewField FieldByName(
    string fieldName
    )
```

- `fieldName` (String) — Name of the desired field.

**Returns:** Returns the ViewField object of the desired field.

---

## ViewField class

Represents a field in an ACCPAC view. The class provides methods and properties to access details of a view field, as well as manipulating field values.

**Namespace:** ACCPAC.Advantage &nbsp;·&nbsp; **Assembly:** ACCPAC.Advantage.dll

```csharp
public class ViewField : IViewFieldComInterop
```

An object of this class cannot be created directly by applications. It should be obtained from the Fields collection.

### Properties

| Name | Description |
|---|---|
| `Attributes` | Gets the attributes of the field. The run-time attributes of a field can be a combination of values defined in the ViewFieldAttributes enumeration. |
| `Description` | Gets the description of the field. |
| `ID` | Gets the ID of the field. This ID corresponds to the field ID (also called field index in view's term) defined in the view. Field IDs are unique within the view. |
| `Index` | Gets the 0-based index of the field in the collection. The index indicates the position of this object inside the collection, and does not relate to the field ID that is defined in the view. |
| `MaxValue` | Gets the maximum value allowed for this field. |
| `MinValue` | Gets the minimum value allowed for this field. |
| `Name` | Gets the name of the field. Field names are unique within the view. |
| `Parent` | Gets the ViewFields collection object where this object was obtained from. |
| `Precision` | Gets the precision of the field. |
| `PresentationList` | Gets a ViewFieldPresentationList object that stores the presentation list defined for the field. Returns null if the field does not have a presentation list. |
| `PresentationMask` | Gets the presentation mask of the field that controls its display format. This property is empty if the field does not use a presentation mask. |
| `PresentationType` | Gets the presentation type of the field. |
| `Size` | Gets the size of the field. |
| `Type` | Gets the data type of the field. |
| `Value` | Gets the current value of the field. |
| `View` | Gets the View object this field belongs to. |

### Methods

| Name | Description |
|---|---|
| `SetToMax` | Sets the field value to the maximum value, as defined by the current MaxValue property. |
| `SetToMin` | Sets the field value to the minimum value, as defined by the current MinValue property. |
| `SetValue` | Assign a new value to the field. Caller can also specify whether the new value should be validated by the view. |

### Method details

#### ViewField.SetToMax

```csharp
public void SetToMax()
```

#### ViewField.SetToMin

```csharp
public void SetToMin()
```

#### ViewField.SetValue

```csharp
public void SetValue(
    Object newValue,
    bool verify
    )
```

- `newValue` (Object) — New value to be assigned to the field. The data type of the new value must be compatible with the field type.
- `verify` (Boolean) — Indicates whether the view should perform validation before accepting the value.

---

## ViewKeys class

Provides access to ViewKey objects that include all keys defined in an ACCPAC view.

**Namespace:** ACCPAC.Advantage &nbsp;·&nbsp; **Assembly:** ACCPAC.Advantage.dll

```csharp
public class ViewKeys : IViewKeysComInterop
```

An object of this class cannot be created directly by applications. It should be obtained from the View object's Keys property.

### Properties

| Name | Description |
|---|---|
| `Count` | Gets the number of keys defined in the view. |
| `Item` | Gets the key object based on the zero-based index in the collection. |
| `Parent` | Gets the View object that created the current object. |

---

## ViewKey class

Represents a key defined in an ACCPAC view.

**Namespace:** ACCPAC.Advantage &nbsp;·&nbsp; **Assembly:** ACCPAC.Advantage.dll

```csharp
public class ViewKey : IViewKeyComInterop
```

An object of this class cannot be created directly by applications. It should be obtained from the Keys class.

### Properties

| Name | Description |
|---|---|
| `FieldCount` | Gets the number of key fields in the key. |
| `ID` | Gets the ID of the key. This key ID corresponds to the key index defined in the view. Key ID always starts from 0 for the first key in the view. |
| `Name` | Gets the name of the key. |
| `Parent` | Gets the ViewKeys object that created the current object. |

### Methods

| Name | Description |
|---|---|
| `Field` | Obtains the ViewField object of a key field. The field is identified by the zero-based index in the key. |

### Method details

#### ViewKey.Field

```csharp
public ViewField Field(
    int index
    )
```

- `index` (Int32) — Index of the field in the key. The index starts from 0 for the first key field.

**Returns:** Returns a ViewField object of the requested key field.

---

## ViewFieldPresentationList class

Provides access to the presentation list that is exposed by a field in an ACCPAC view.

**Namespace:** ACCPAC.Advantage &nbsp;·&nbsp; **Assembly:** ACCPAC.Advantage.dll

```csharp
public class ViewFieldPresentationList : IViewFieldPresentationListComInterop
```

An object of this class cannot be created directly by applications. It should be obtained from the Field object's PresentationList property. A presentation list is a predefined list of valid values allowed by a field, and their corresponding display strings. The valid values should be treated as internal values and should not be displayed to the user. Users should be presented with the presentation strings which are meaningful to them, as well as localized to the language based on the user's language preference.

### Properties

| Name | Description |
|---|---|
| `Count` | Gets the number of presentation items defined in the list. |
| `FieldString` | Gets the display string defined for the current field value. |
| `Item` | Gets the predefined display string of a presentation item according to the zero-based index in the list. Same as calling PredefinedString . |
| `Parent` | Gets the field object which the presentation list belongs to. |

### Methods

| Name | Description |
|---|---|
| `PredefinedString` | Gets the predefined display string of a presentation item according to the zero-based index in the list. |
| `PredefinedValue` | Gets the predefined value of a presentation item according to the zero-based index in the list. |
| `Refresh` | Refreshes the presentation list from the view. Applications should call this method to refresh the list if the field attributes indicates that the presentation information may change. Refreshing the list ensures it retrieves the most current presentation list as of the current view state. |
| `SetFieldValue` | Sets the current field value as the predefined value of the specified presentation item. The presentation item is identified by the zero-based index in the presentation list. |

### Method details

#### ViewFieldPresentationList.PredefinedString

```csharp
public string PredefinedString(
    int index
    )
```

- `index` (Int32) — The zero-based index that identifies the presentation item in the list.

**Returns:** Returns the predefined string of the presentation item.

#### ViewFieldPresentationList.PredefinedValue

```csharp
public Object PredefinedValue(
    int index
    )
```

- `index` (Int32) — The zero-based index that identifies the presentation item in the list.

**Returns:** Returns the presdefined field value of the presentation item.

#### ViewFieldPresentationList.Refresh

```csharp
public void Refresh()
```

#### ViewFieldPresentationList.SetFieldValue

```csharp
public void SetFieldValue(
    int index
    )
```

- `index` (Int32) — The zero-based index that identifies the presentation item in the list.

---

## ViewReturnCode class

Defines return codes of view operations. This class defines common view return codes as constants.

**Namespace:** ACCPAC.Advantage &nbsp;·&nbsp; **Assembly:** ACCPAC.Advantage.dll

```csharp
public class ViewReturnCode
```

This class only defines the common view return codes. Custom return codes from specific views are not included.

---

## ViewInternal class

Reserved for ACCPAC internal use only.

**Namespace:** ACCPAC.Advantage &nbsp;·&nbsp; **Assembly:** ACCPAC.Advantage.dll

```csharp
public class ViewInternal : IViewInternal
```

### Methods

| Name | Description |
|---|---|
| `BlkGet` | Reserved for ACCPAC internal use only. |
| `BlkPut` | Reserved for ACCPAC internal use only. |
| `Cancel` | Reserved for ACCPAC internal use only. |
| `Compose` | Reserved for ACCPAC internal use only. |
| `Fetch` | Reserved for ACCPAC internal use only. |
| `FilterCount` | Reserved for ACCPAC internal use only. |
| `FilterFetch` | Reserved for ACCPAC internal use only. |
| `FilterSelect` | Reserved for ACCPAC internal use only. |
| `GetComposedView` | Reserved for ACCPAC internal use only. |
| `GetFieldInfo` | Reserved for ACCPAC internal use only. |
| `GetViewInfo` | Reserved for ACCPAC internal use only. |
| `GoBottom` | Reserved for ACCPAC internal use only. |
| `GoNext` | Reserved for ACCPAC internal use only. |
| `GoPrev` | Reserved for ACCPAC internal use only. |
| `GotoBookmark` | Reserved for ACCPAC internal use only. |
| `GoTop` | Reserved for ACCPAC internal use only. |
| `GotoRecordNumber` | Reserved for ACCPAC internal use only. |
| `Init` | Reserved for ACCPAC internal use only. |
| `Insert` | Reserved for ACCPAC internal use only. |
| `InstanceProtocol` | Reserved for ACCPAC internal use only. |
| `LookupValue` | Reserved for ACCPAC internal use only. |
| `Post` | Reserved for ACCPAC internal use only. |
| `Process` | Reserved for ACCPAC internal use only. |
| `Put` | Reserved for ACCPAC internal use only. |
| `Read` | Reserved for ACCPAC internal use only. |
| `RecordClear` | Reserved for ACCPAC internal use only. |
| `RecordCreate` | Reserved for ACCPAC internal use only. |
| `RecordGenerate` | Reserved for ACCPAC internal use only. |
| `RefreshPresentation` | Reserved for ACCPAC internal use only. |
| `RevisionCancel` | Reserved for ACCPAC internal use only. |
| `RevisionPost` | Reserved for ACCPAC internal use only. |
| `SetOrder` | Reserved for ACCPAC internal use only. |
| `SetSystemAccess` | Reserved for ACCPAC internal use only. |
| `Update` | Reserved for ACCPAC internal use only. |
| `Verify` | Reserved for ACCPAC internal use only. |

### Method details

#### ViewInternal.BlkGet

```csharp
public void BlkGet(
    ref Object fieldIDs,
    out byte[] updatedInfo
    )
```

- `fieldIDs` (Object %)
- `updatedInfo` (Byte[] %)

#### ViewInternal.BlkPut

```csharp
public void BlkPut(
    ref Object fieldIDs,
    ref Object fieldValues,
    bool verify,
    out byte[] updatedInfo
    )
```

- `fieldIDs` (Object %)
- `fieldValues` (Object %)
- `verify` (Boolean)
- `updatedInfo` (Byte[] %)

#### ViewInternal.Cancel

```csharp
public void Cancel(
    ref Object getFieldIDs,
    out byte[] updatedInfo
    )
```

- `getFieldIDs` (Object %)
- `updatedInfo` (Byte[] %)

#### ViewInternal.Compose

```csharp
public void Compose(
    string[] viewIDs,
    View parentView
    )
```

- `viewIDs` (String[])
- `parentView` (View)

#### ViewInternal.Fetch

```csharp
public bool Fetch(
    ref Object putFieldIDs,
    ref Object putFieldValues,
    ref Object getFieldIDs,
    bool lockRecord,
    out byte[] updatedInfo
    )
```

- `putFieldIDs` (Object %)
- `putFieldValues` (Object %)
- `getFieldIDs` (Object %)
- `lockRecord` (Boolean)
- `updatedInfo` (Byte[] %)

**Returns:** @)]

#### ViewInternal.FilterCount

```csharp
public int FilterCount(
    string filter,
    int flags,
    ref Object fieldIDs,
    out byte[] updatedInfo
    )
```

- `filter` (String)
- `flags` (Int32)
- `fieldIDs` (Object %)
- `updatedInfo` (Byte[] %)

**Returns:** @)]

#### ViewInternal.FilterFetch

```csharp
public bool FilterFetch(
    bool lockRecord,
    ref Object putFieldIDs,
    ref Object putFieldValues,
    ref Object fieldIDs,
    out byte[] updatedInfo
    )
```

- `lockRecord` (Boolean)
- `putFieldIDs` (Object %)
- `putFieldValues` (Object %)
- `fieldIDs` (Object %)
- `updatedInfo` (Byte[] %)

**Returns:** @)]

#### ViewInternal.FilterSelect

```csharp
public void FilterSelect(
    string filter,
    bool ascending,
    int order,
    ViewFilterOrigin origin,
    ref Object fieldIDs,
    out byte[] updatedInfo
    )
```

- `filter` (String)
- `ascending` (Boolean)
- `order` (Int32)
- `origin` (ViewFilterOrigin)
- `fieldIDs` (Object %)
- `updatedInfo` (Byte[] %)

#### ViewInternal.GetComposedView

```csharp
public View GetComposedView(
    string viewID
    )
```

- `viewID` (String)

#### ViewInternal.GetFieldInfo

```csharp
public byte[] GetFieldInfo(
    ref Object fieldID,
    int fieldIDType
    )
```

- `fieldID` (Object %)
- `fieldIDType` (Int32)

#### ViewInternal.GetViewInfo

```csharp
public byte[] GetViewInfo(
    ref Object[] fieldIdentifiers
    )
```

- `fieldIdentifiers` (Object[] %)

**Returns:** @)]

#### ViewInternal.GoBottom

```csharp
public bool GoBottom(
    ref Object getFieldIDs,
    out byte[] updatedInfo
    )
```

- `getFieldIDs` (Object %)
- `updatedInfo` (Byte[] %)

**Returns:** @)]

#### ViewInternal.GoNext

```csharp
public bool GoNext(
    ref Object putFieldIDs,
    ref Object putFieldValues,
    ref Object getFieldIDs,
    out byte[] updatedInfo
    )
```

- `putFieldIDs` (Object %)
- `putFieldValues` (Object %)
- `getFieldIDs` (Object %)
- `updatedInfo` (Byte[] %)

**Returns:** @)]

#### ViewInternal.GoPrev

```csharp
public bool GoPrev(
    ref Object putFieldIDs,
    ref Object putFieldValues,
    ref Object getFieldIDs,
    out byte[] updatedInfo
    )
```

- `putFieldIDs` (Object %)
- `putFieldValues` (Object %)
- `getFieldIDs` (Object %)
- `updatedInfo` (Byte[] %)

**Returns:** @)]

#### ViewInternal.GotoBookmark

```csharp
public bool GotoBookmark(
    ref Object bookmark,
    ref Object getFieldIDs,
    out byte[] updatedInfo
    )
```

- `bookmark` (Object %)
- `getFieldIDs` (Object %)
- `updatedInfo` (Byte[] %)

**Returns:** @)]

#### ViewInternal.GoTop

```csharp
public bool GoTop(
    ref Object getFieldIDs,
    out byte[] updatedInfo
    )
```

- `getFieldIDs` (Object %)
- `updatedInfo` (Byte[] %)

**Returns:** @)]

#### ViewInternal.GotoRecordNumber

```csharp
public bool GotoRecordNumber(
    int recordNumber,
    ref Object getFieldIDs,
    out byte[] updatedInfo
    )
```

- `recordNumber` (Int32)
- `getFieldIDs` (Object %)
- `updatedInfo` (Byte[] %)

**Returns:** @)]

#### ViewInternal.Init

```csharp
public void Init(
    ref Object getFieldIDs,
    out byte[] updatedInfo
    )
```

- `getFieldIDs` (Object %)
- `updatedInfo` (Byte[] %)

#### ViewInternal.Insert

```csharp
public void Insert(
    ref Object putFieldIDs,
    ref Object putFieldValues,
    ref Object getFieldIDs,
    out byte[] updatedInfo
    )
```

- `putFieldIDs` (Object %)
- `putFieldValues` (Object %)
- `getFieldIDs` (Object %)
- `updatedInfo` (Byte[] %)

#### ViewInternal.InstanceProtocol

```csharp
public ViewProtocol InstanceProtocol(
    ref Object fieldIDs,
    out byte[] updatedInfo
    )
```

- `fieldIDs` (Object %)
- `updatedInfo` (Byte[] %)

**Returns:** @)]

#### ViewInternal.LookupValue

```csharp
public Object LookupValue(
    ref Object fieldIDs,
    ref Object fieldValues,
    int order,
    int targetFieldID
    )
```

- `fieldIDs` (Object %)
- `fieldValues` (Object %)
- `order` (Int32)
- `targetFieldID` (Int32)

#### ViewInternal.Post

```csharp
public void Post(
    ref Object putFieldIDs,
    ref Object putFieldValues,
    ref Object getFieldIDs,
    out byte[] updatedInfo
    )
```

- `putFieldIDs` (Object %)
- `putFieldValues` (Object %)
- `getFieldIDs` (Object %)
- `updatedInfo` (Byte[] %)

#### ViewInternal.Process

```csharp
public void Process(
    ref Object putFieldIDs,
    ref Object putFieldValues,
    ref Object getFieldIDs,
    out byte[] updatedInfo
    )
```

- `putFieldIDs` (Object %)
- `putFieldValues` (Object %)
- `getFieldIDs` (Object %)
- `updatedInfo` (Byte[] %)

#### ViewInternal.Put

```csharp
public byte[] Put(
    int fieldID,
    ref Object fieldValue,
    bool verify
    )
```

- `fieldID` (Int32)
- `fieldValue` (Object %)
- `verify` (Boolean)

#### ViewInternal.Read

```csharp
public bool Read(
    ref Object putFieldIDs,
    ref Object putFieldValues,
    ref Object getFieldIDs,
    bool lockRecord,
    out byte[] updatedInfo
    )
```

- `putFieldIDs` (Object %)
- `putFieldValues` (Object %)
- `getFieldIDs` (Object %)
- `lockRecord` (Boolean)
- `updatedInfo` (Byte[] %)

**Returns:** @)]

#### ViewInternal.RecordClear

```csharp
public void RecordClear(
    ref Object fieldIDs,
    out byte[] updatedInfo
    )
```

- `fieldIDs` (Object %)
- `updatedInfo` (Byte[] %)

#### ViewInternal.RecordCreate

```csharp
public void RecordCreate(
    ViewRecordCreate flags,
    ref Object fieldIDs,
    out byte[] updatedInfo
    )
```

- `flags` (ViewRecordCreate)
- `fieldIDs` (Object %)
- `updatedInfo` (Byte[] %)

#### ViewInternal.RecordGenerate

```csharp
public void RecordGenerate(
    bool insert,
    ref Object fieldIDs,
    out byte[] updatedInfo
    )
```

- `insert` (Boolean)
- `fieldIDs` (Object %)
- `updatedInfo` (Byte[] %)

#### ViewInternal.RefreshPresentation

```csharp
public void RefreshPresentation(
    ref Object fieldIDs,
    out byte[] updatedInfo
    )
```

- `fieldIDs` (Object %)
- `updatedInfo` (Byte[] %)

#### ViewInternal.RevisionCancel

```csharp
public void RevisionCancel(
    int level,
    ref Object fieldIDs,
    out byte[] updatedInfo
    )
```

- `level` (Int32)
- `fieldIDs` (Object %)
- `updatedInfo` (Byte[] %)

#### ViewInternal.RevisionPost

```csharp
public void RevisionPost(
    int level,
    ref Object putFieldIDs,
    ref Object putFieldValues,
    ref Object fieldIDs,
    out byte[] updatedInfo
    )
```

- `level` (Int32)
- `putFieldIDs` (Object %)
- `putFieldValues` (Object %)
- `fieldIDs` (Object %)
- `updatedInfo` (Byte[] %)

#### ViewInternal.SetOrder

```csharp
public void SetOrder(
    int order,
    bool unique,
    ref Object getFieldIDs,
    out byte[] updatedInfo
    )
```

- `order` (Int32)
- `unique` (Boolean)
- `getFieldIDs` (Object %)
- `updatedInfo` (Byte[] %)

#### ViewInternal.SetSystemAccess

```csharp
public void SetSystemAccess(
    int systemAccess,
    ref Object getFieldIDs,
    out byte[] updatedInfo
    )
```

- `systemAccess` (Int32)
- `getFieldIDs` (Object %)
- `updatedInfo` (Byte[] %)

#### ViewInternal.Update

```csharp
public void Update(
    ref Object putFieldIDs,
    ref Object putFieldValues,
    ref Object getFieldIDs,
    out byte[] updatedInfo
    )
```

- `putFieldIDs` (Object %)
- `putFieldValues` (Object %)
- `getFieldIDs` (Object %)
- `updatedInfo` (Byte[] %)

#### ViewInternal.Verify

```csharp
public void Verify(
    ref Object putFieldIDs,
    ref Object putFieldValues,
    ref Object getFieldIDs,
    out byte[] updatedInfo
    )
```

- `putFieldIDs` (Object %)
- `putFieldValues` (Object %)
- `getFieldIDs` (Object %)
- `updatedInfo` (Byte[] %)


# System, company, currency, admin & error classes

Company profile, currency, fiscal calendar, organizations, activated applications, reporting/printing, multi-user locking, meters, spy log, and the exception/error classes.

Extracted from `Sage Accpac .NET Libraries.chm` (library 5.5.0.1). Verified 2026-09-25. See [`INDEX.md`](INDEX.md) for the full class/enum map and [`enums.md`](enums.md) for enumerations.

Classes in this file: `ActiveApplication`, `ActiveApplications`, `ClientChannelSinkProvider`, `Company`, `Currency`, `CurrencyRate`, `CurrencyTable`, `DBLinkException`, `Error`, `Errors`, `FiscalCalendar`, `Meter`, `Multiuser`, `Organization`, `Organizations`, `PrintSetup`, `ProcessServerSetup`, `Report`, `SessionException`, `SpyLog`, `ViewException`

---

## ActiveApplication class

Represents an activated application on an ACCPAC database.

**Namespace:** ACCPAC.Advantage &nbsp;·&nbsp; **Assembly:** ACCPAC.Advantage.dll

```csharp
public class ActiveApplication : IActiveApplicationComInterop
```

An object of this class is obtained from the ActiveApplications collection.

### Properties

| Name | Description |
|---|---|
| `AppID` | Gets the application ID of the application. |
| `AppVersion` | Gets the version of the application. |
| `DataLevel` | Gets the application's data level. |
| `IsInstalled` | Indicates whether the active application is installed on the current system. |
| `Selector` | Gets the application ID of the base application. If the current application is a base application, the Selector is the same as AppID. |
| `Sequence` | Gets the sequence number of an add-on application. Base applications have a sequence number of "00". |

---

## ActiveApplications class

A collection of activated applications on an ACCPAC database.

**Namespace:** ACCPAC.Advantage &nbsp;·&nbsp; **Assembly:** ACCPAC.Advantage.dll

```csharp
public class ActiveApplications : IActiveApplicationsComInterop,
    IEnumerable
```

An object of this class cannot be created directly by applications. It should be obtained from DBLink object's ActiveApplications property.

### Properties

| Name | Description |
|---|---|
| `Count` | Gets the number of applications stored in the collection. |
| `Item` | Gets an ActiveApplication object of the application in the list. The object is identified by its zero-based index in the collection. |

### Methods

| Name | Description |
|---|---|
| `GetEnumerator` | Returns an IEnumerator object of the ActiveApplications collection which can be used to enumerate through all the items in the collection. |

### Method details

#### ActiveApplications.GetEnumerator

```csharp
public IEnumerator GetEnumerator()
```

**Returns:** Returns an IEnumerator object of the ActiveAppliations collection.

---

## ClientChannelSinkProvider class

For ACCPAC internal use only.

**Namespace:** ACCPAC.Advantage &nbsp;·&nbsp; **Assembly:** ACCPAC.Advantage.dll

```csharp
public class ClientChannelSinkProvider : IClientChannelSinkProvider
```

### Constructors

| Name | Description |
|---|---|
| `ClientChannelSinkProvider` | Member of ClientChannelSinkProvider implementation of IClientChannelSinkProvider |
| `ClientChannelSinkProvider` | Member of ClientChannelSinkProvider implementation of IClientChannelSinkProvider |

### Properties

| Name | Description |
|---|---|
| `Next` | Member of ClientChannelSinkProvider implementation of IClientChannelSinkProvider |

### Methods

| Name | Description |
|---|---|
| `CreateSink` | Member of ClientChannelSinkProvider implementation of IClientChannelSinkProvider |

### Method details

#### ClientChannelSinkProvider.CreateSink

```csharp
public IClientChannelSink CreateSink(
    IChannelSender channel,
    string url,
    Object remoteChannelData
    )
```

- `channel` (IChannelSender)
- `url` (String)
- `remoteChannelData` (Object)

---

## Company class

Provides details of the company set up in Common Services Company Profile.

**Namespace:** ACCPAC.Advantage &nbsp;·&nbsp; **Assembly:** ACCPAC.Advantage.dll

```csharp
public class Company : ICompanyComInterop
```

An object of this class can be obtained from DBLink object's Company property.

### Properties

| Name | Description |
|---|---|
| `Address1` | Gets address line 1. |
| `Address2` | Gets address line 2. |
| `Address3` | Gets address line 3. |
| `Address4` | Gets address line 4. |
| `BranchCode` | Gets the branch code of the company. |
| `City` | Gets the city of the address. |
| `Contact` | Gets the name of the contact person. |
| `Country` | Gets the country of the company. |
| `CountryCode` | Gets the country code of the company. |
| `EuroCurrency` | Indicates whether the home currency is a Euro currency. |
| `Fax` | Gets the fax number. |
| `FiscalPeriods` | Gets the number of fiscal periods in a fiscal year. |
| `FourPeriodQuarter` | Gets the quarter number with 4 periods, if the company uses 13 periods in a fiscal year. |
| `GainLossAccountingMethod` | Indicates which exchange gain/loss accounting method to use when the company is a multicurrency company. |
| `HandleInactiveGLAccounts` | Indicates how inactive GL accounts should be handled. |
| `HandleLockedFiscalPeriods` | Indicates how locked fiscal periods should be handled. |
| `HandleNonexistentGLAccounts` | Indicates how non-existant GL accounts should be handled. |
| `HomeCurrency` | Gets the home currency code of the company. |
| `LocationCode` | Gets the location code. |
| `LocationType` | Gets the location type. |
| `Multicurrency` | Indicates whether the company is set up to use multicurrency. |
| `Name` | Gets the company name. |
| `OrgID` | Gets the organization ID of the company. |
| `Parent` | Gets the DBLink object that created this object. |
| `Phone` | Gets the phone number. |
| `PhoneFormat` | Indicates whether the phone numbers should be formatted. |
| `PhoneMask` | Gets the display mask for phone number. |
| `PostCode` | Gets the Zip code/postal code. |
| `RateType` | Gets the default rate type code. |
| `ReportingCurrency` | Gets the currency to include in finaical reports, if the home currency is Euro. Not applicable if home currency is not Euro. |
| `SessionWarnDays` | Gets the maximum number of days a transcation date can deviate from the session date before the system would issue a warning. |
| `State` | Gets the State of the address. |

---

## Currency class

Stores details of a currency code set up in Common Services.

**Namespace:** ACCPAC.Advantage &nbsp;·&nbsp; **Assembly:** ACCPAC.Advantage.dll

```csharp
public class Currency : ICurrencyComInterop
```

An object of this class cannot be created directly by applications. Obtain the object from the DBLink object's GetCurrency method.

### Properties

| Name | Description |
|---|---|
| `Code` | Gets the currency code. |
| `Decimals` | Gets the number of decimals for this currency. |
| `DecimalSeparator` | Gets the decmial separator for this currency. |
| `Description` | Gets the currency description. |
| `NegativeDisplay` | Gets the negative amount display format for this currency. |
| `Symbol` | Gets the currency symbol. |
| `SymbolDisplay` | Gets the currency symbol display format for this currency. |
| `ThousandSeparator` | Gets the throusand separator for this currency. |

### Methods

| Name | Description |
|---|---|
| `IsBlockCombinationWith` | Determines if the currency and the specified currency code belong in the same currency block, both as members, or one as a member and the other as its master. |
| `IsBlockMaster` | Determines if the currency is a block master currency. |
| `IsBlockMember` | Determines if the currency is a member of a currency block, and retrieves the currency rate information with its master. |

### Method details

#### Currency.IsBlockCombinationWith

```csharp
public bool IsBlockCombinationWith(
    string currencyCode,
    DateTime date,
    CurrencyBlockDateMatch blockDateMatch
    )
```

- `currencyCode` (String) — Another currency code.
- `date` (DateTime) — The date on which to determine whether the currencies belong to the same currency block.
- `blockDateMatch` (CurrencyBlockDateMatch) — Indicates which date matching method should be used.

**Returns:** Returns whether the currencies belong in the same currency block.

#### Currency.IsBlockMaster

```csharp
public bool IsBlockMaster(
    DateTime date,
    CurrencyBlockDateMatch blockDateMatch
    )
```

- `date` (DateTime) — The date on which to determine whether the currency is a block master.
- `blockDateMatch` (CurrencyBlockDateMatch) — Indicates which date matching method should be used.

**Returns:** Returns whether the currency is a block master.

#### Currency.IsBlockMember

```csharp
public bool IsBlockMember(
    DateTime date,
    CurrencyBlockDateMatch blockDateMatch,
    out CurrencyRate rate
    )
```

- `date` (DateTime) — The date on which to determine whether currency is a block member.
- `blockDateMatch` (CurrencyBlockDateMatch) — Indicates the date matching method that should be used.
- `rate` (CurrencyRate %) — If the currency is a member of a block currency, this parameter returns a CurrencyRate object that stores the exchange rate information with its master currency. Otherwise, this parameter returns null.

**Returns:** Returns whether the currency is a member of a currecy block.

---

## CurrencyRate class

Represents a currency exchange rate.

**Namespace:** ACCPAC.Advantage &nbsp;·&nbsp; **Assembly:** ACCPAC.Advantage.dll

```csharp
public class CurrencyRate : ICurrencyRateComInterop
```

An object of this class cannot be created directly by applications. Obtain the object from the Session object's GetCurrencyRate, GetCurrencyRateComposite and GetCurrencyRateFloating methods.

### Properties

| Name | Description |
|---|---|
| `DateMatch` | Gets the date matching method used to determine the exchange rate. |
| `HomeCurrency` | Gets the home (functional) currency code. |
| `Rate` | Gets the currency exchange rate. |
| `RateDate` | Gets the effective date of the exchange rate. |
| `RateOperator` | Gets the operator that should be used on the exchange rate and the currency amount when performing exchange calculation. |
| `RateType` | Gets the currency rate type code. |
| `SourceCurrency` | Gets the source currency code. |
| `Spread` | Gets the allowed difference that the rate can vary from the actual rate. |

---

## CurrencyTable class

Stores details of a currency table set up in Common Services.

**Namespace:** ACCPAC.Advantage &nbsp;·&nbsp; **Assembly:** ACCPAC.Advantage.dll

```csharp
public class CurrencyTable : ICurrencyTableComInterop
```

An object of this class cannot be created directly by applications. Obtain the object from the Session object's GetCurrencyTable method.

### Properties

| Name | Description |
|---|---|
| `CurrencyCode` | Gets the currency code of the currency table. |
| `DateMatch` | Gets the date matching method to be used to determine exchange rates. |
| `Description` | Gets the description of the currency table. |
| `RateOperator` | Gets the rate operator to be used when performing exchange calculation. |
| `RateType` | Gets the currency rate type code of the currency table. |
| `SourceOfRates` | Gets a description of the source of where the exchange rates are obtained. |

---

## DBLinkException class

The exception that is thrown when a call to any methods/properties on the DBLink object fails. The exception stores the original error code from the ACCPAC database layer that caused this exception.

**Namespace:** ACCPAC.Advantage &nbsp;·&nbsp; **Assembly:** ACCPAC.Advantage.dll

```csharp
[SerializableAttribute]
    public class DBLinkException : ApplicationException
```

### Constructors

| Name | Description |
|---|---|
| `DBLinkException` | Initializes a DBLinkException object and attaches the original exception that caused this exception to be thrown. |
| `DBLinkException` | Initializes a DBLinkException object with an ACCPAC database layer error code that caused the exception. |
| `DBLinkException` | Initializes a new instance of the DBLinkException class with serialized data. |

### Properties

| Name | Description |
|---|---|
| `DBSError` | Gets the ACCPAC database layer error code that casued this exception. |

### Methods

| Name | Description |
|---|---|
| `GetObjectData` | Sets information about the exception for serialization. |

### Method details

#### DBLinkException.GetObjectData

```csharp
public override void GetObjectData(
    SerializationInfo info,
    StreamingContext context
    )
```

- `info` (SerializationInfo) — The object that holds the serialized object data.
- `context` (StreamingContext) — The contextual information about the source or destination.

This method is used for serialization. Applications do not need to call this method.

---

## Error class

Provides details of an application error.

**Namespace:** ACCPAC.Advantage &nbsp;·&nbsp; **Assembly:** ACCPAC.Advantage.dll

```csharp
public class Error : IErrorComInterop
```

Objects of this class can be obtained from the Errors collection.

### Properties

| Name | Description |
|---|---|
| `Code` | Gets the error code. |
| `HelpFile` | Gets the help file associated with the error. |
| `HelpID` | Gets the help context ID associated with the error. |
| `Message` | Gets the error message. |
| `Priority` | Gets the error priority. |
| `Source` | Gets the source of the error. |

---

## Errors class

Stores all the errors raised within the context of the current session.

**Namespace:** ACCPAC.Advantage &nbsp;·&nbsp; **Assembly:** ACCPAC.Advantage.dll

```csharp
public class Errors : IErrorsComInterop, IDisposable
```

This object stores all the errors raised within the current session. They include errors when calling methods/properties of the Session object, as well as methods/properties of all objects created directly or indirectly from the Session object. These include errors of all views created within the session. An object of this class cannot be created directly by applications. Obtain the object from the Session object's Errors property.

### Properties

| Name | Description |
|---|---|
| `Count` | Gets the number of errors stored in the session. |
| `Item` | Gets an Error object that stores details of an error. The error is identified by its zero-based index in the collection. |

### Methods

| Name | Description |
|---|---|
| `Clear` | Clears all error messages stored in the session. |
| `Dispose` | Releases all resources used by the object. |
| `GenerateErrorFile` | Generates a temporary file that stores the errors in the collection. |
| `Put` | Stores a new error message into the session. |

### Method details

#### Errors.Clear

```csharp
public void Clear()
```

#### Errors.Dispose

```csharp
public void Dispose()
```

#### Errors.GenerateErrorFile

```csharp
public string GenerateErrorFile()
```

**Returns:** Returns the full path (including the file name) of the generated file. Note that when accessing a remote ACCPAC server, the returned path is a path on the server machine.

This method is useful for applications wanting to generate a report on all errors stored in the session. The generated file is a CSV file.

#### Errors.Put

```csharp
public void Put(
    string message,
    ErrorPriority priority,
    Object[] parameters,
    string source,
    string code,
    string helpFile,
    int helpID
    )
```

- `message` (String) — The error message.
- `priority` (ErrorPriority) — Error priority.
- `parameters` (Object[]) — An array of parameters if the error message contains string-replacement tokens. The tokens in the error message will be replaced by the parameters specified Tokens in an error message should be in the form %n, where n is a number starting from 1. The number identifies the corresponding position of the replacement value in the parameters array. This parameter should be null if replacement tokens were not used in the message.
- `source` (String) — Source of the error.
- `code` (String) — Error code.
- `helpFile` (String) — Help file in which help messages could be found for this error.
- `helpID` (Int32) — Context ID of the help message.

```csharp
public void Put(
    string appID,
    int rscID,
    ErrorPriority priority,
    Object[] parameters,
    string source,
    string code,
    string helpFile,
    int helpID
    )
```

- `appID` (String) — Application ID of the language resource file.
- `rscID` (Int32) — Resource ID of the message defined in the language resource file.
- `priority` (ErrorPriority) — Error priority.
- `parameters` (Object[]) — An array of parameters if the error message contains string-replacement tokens. The tokens in the error message will be replaced by the parameters specified Tokens in an error message should be in the form %n, where n is a number starting from 1. The number identifies the corresponding position of the replacement value in the parameters array. This parameter should be null if replacement tokens were not used in the message.
- `source` (String) — Source of the error.
- `code` (String) — Error code.
- `helpFile` (String) — Help file in which help messages could be found for this error.
- `helpID` (Int32) — Context ID of the help message.

---

## FiscalCalendar class

Provides methods to access the fiscal calendar set up in the company.

**Namespace:** ACCPAC.Advantage &nbsp;·&nbsp; **Assembly:** ACCPAC.Advantage.dll

```csharp
public class FiscalCalendar : IFiscalCalendarComInterop
```

An object of this class cannot be created directly by applications. It should be obtained from the DBLink object's FiscalCalendar property.

### Properties

| Name | Description |
|---|---|
| `Parent` | Gets the DBLink object that created the current object. |

### Methods

| Name | Description |
|---|---|
| `DatesFromPeriod` | Calculates the period start and end dates given a period number, type, length and a base date. |
| `DateToPeriod` | Calculates the period number, given a date, period type, length and a base date. |
| `GetFirstYear` | Looks up the first fiscal year in the calendar and retrieves its details. |
| `GetLastYear` | Looks up the last fiscal year in the calendar and retrieves its details. |
| `GetPeriod` | Locates the fiscal year and period a given date falls on. |
| `GetPeriodDates` | Retrieves the start and end dates of a given fiscal year and period. |
| `GetQuarter` | Retrieves the quarter a given fiscal year and period belongs to. |
| `GetQuarterDates` | Retrieves the start and end dates of a given fiscal year and quarter. |
| `GetYear` | Looks up a fiscal year in the calendar and retrieves its details. |
| `GetYearDates` | Retrieves the start and end dates of a given fiscal year. |

### Method details

#### FiscalCalendar.DatesFromPeriod

```csharp
public bool DatesFromPeriod(
    short period,
    FiscalPeriodType periodType,
    short periodLength,
    DateTime baseDate,
    out DateTime startDate,
    out DateTime endDate
    )
```

- `period` (Int16) — Period number.
- `periodType` (FiscalPeriodType) — Period type.
- `periodLength` (Int16) — Period length.
- `baseDate` (DateTime) — Base date.
- `startDate` (DateTime %) — Returns the start date of the period.
- `endDate` (DateTime %) — Returns the end date of the period.

**Returns:** Returns whether the start and end dates could be determined.

#### FiscalCalendar.DateToPeriod

```csharp
public bool DateToPeriod(
    DateTime date,
    FiscalPeriodType periodType,
    short periodLength,
    DateTime baseDate,
    out short period
    )
```

- `date` (DateTime) — Date.
- `periodType` (FiscalPeriodType) — Period type.
- `periodLength` (Int16) — Period length.
- `baseDate` (DateTime) — Base date.
- `period` (Int16 %) — Returns the period number the specified date falls on.

**Returns:** Returns whether the period number could be determined.

#### FiscalCalendar.GetFirstYear

```csharp
public bool GetFirstYear(
    out string year,
    out short periods,
    out short qtr4Period,
    out bool active
    )
```

- `year` (String %) — Returns the fiscal year.
- `periods` (Int16 %) — Returns the number of periods in the fiscal year.
- `qtr4Period` (Int16 %) — Returns the quarter that contains 4 periods, if the year has 13 periods.
- `active` (Boolean %) — Returns whether the fiscal year is active.

**Returns:** Returns whether a fiscal year is found in the fiscal calendar.

#### FiscalCalendar.GetLastYear

```csharp
public bool GetLastYear(
    out string year,
    out short periods,
    out short qtr4Period,
    out bool active
    )
```

- `year` (String %) — Returns the fiscal year.
- `periods` (Int16 %) — Returns the number of periods in the fiscal year.
- `qtr4Period` (Int16 %) — Returns the quarter that contains 4 periods, if the year has 13 periods.
- `active` (Boolean %) — Returns whether the fiscal year is active.

**Returns:** Returns whether a fiscal year is found in the fiscal calendar.

#### FiscalCalendar.GetPeriod

```csharp
public bool GetPeriod(
    DateTime date,
    out short period,
    out string year,
    out bool periodOpen
    )
```

- `date` (DateTime) — Date.
- `period` (Int16 %) — Returns the fiscal period of the specified date.
- `year` (String %) — Returns the fiscal year of the specified date.
- `periodOpen` (Boolean %) — Returns whether the fiscal period is open (not locked).

**Returns:** Returns whether the given date falls on a fiscal period set up in the fiscal calendar.

#### FiscalCalendar.GetPeriodDates

```csharp
public bool GetPeriodDates(
    string year,
    short period,
    out DateTime startDate,
    out DateTime endDate,
    out bool periodOpen
    )
```

- `year` (String) — Fiscal year.
- `period` (Int16) — Fiscal period.
- `startDate` (DateTime %) — Returns the start date of the fiscal period.
- `endDate` (DateTime %) — Returns the end date of the fiscal period.
- `periodOpen` (Boolean %) — Returns whether the period is open (not locked).

**Returns:** Returns whether the specified fiscal year and period are valid in the fiscal calendar.

#### FiscalCalendar.GetQuarter

```csharp
public bool GetQuarter(
    string year,
    short period,
    out short quarter
    )
```

- `year` (String) — Fiscal year.
- `period` (Int16) — Fiscal period.
- `quarter` (Int16 %) — Returns the quarter the period belongs to.

**Returns:** Returns whether the specified fiscal year and period are valid in the fiscal calendar.

#### FiscalCalendar.GetQuarterDates

```csharp
public bool GetQuarterDates(
    string year,
    short quarter,
    out DateTime startDate,
    out DateTime endDate
    )
```

- `year` (String) — Fiscal year.
- `quarter` (Int16) — Quarter.
- `startDate` (DateTime %) — Returns the start date of the quarter.
- `endDate` (DateTime %) — Returns the end date of the quarter.

**Returns:** Returns whether the specified fiscal year and quarter are valid in the fiscal calendar.

#### FiscalCalendar.GetYear

```csharp
public bool GetYear(
    string year,
    out short periods,
    out short qtr4Period,
    out bool active
    )
```

- `year` (String) — The fiscal year to locate in the fiscal calendar.
- `periods` (Int16 %) — Returns the number of periods in the fiscal year.
- `qtr4Period` (Int16 %) — Returns the quarter that contains 4 periods, if the year has 13 periods.
- `active` (Boolean %) — Returns whether the fiscal year is active.

**Returns:** Returns whether the specified fiscal year is found in the fiscal calendar.

#### FiscalCalendar.GetYearDates

```csharp
public bool GetYearDates(
    string year,
    out DateTime startDate,
    out DateTime endDate
    )
```

- `year` (String) — Fiscal year.
- `startDate` (DateTime %) — Returns the start date of the fiscal year.
- `endDate` (DateTime %) — Returns the end date of the fiscal year.

**Returns:** Returns whether the specified year is valid in the fiscal calendar.

---

## Meter class

Provides access to progress information on long server processes.

**Namespace:** ACCPAC.Advantage &nbsp;·&nbsp; **Assembly:** ACCPAC.Advantage.dll

```csharp
public class Meter : IMeterComInterop
```

This object is provided mainly for ACCPAC controls to display progress information. Application programs do not normally need to access this object directly.

### Properties

| Name | Description |
|---|---|
| `Caption` | Gets the caption for the current process. |
| `IsRunning` | Indicates whether the server process is still running. |
| `Label` | Gets the label of the meter object. |
| `Percent` | Gets the percentage done for the current process. |
| `ShowCancel` | Indicates whether the cancel button should be shown. |
| `ShowGauge` | Indicates whether the progress gauge should be shown. |

### Methods

| Name | Description |
|---|---|
| `Cancel` | Cancels the server process. |
| `GetCurrentStatus` | Obtains the current status of the server process. |

### Method details

#### Meter.Cancel

```csharp
public void Cancel()
```

#### Meter.GetCurrentStatus

```csharp
public void GetCurrentStatus(
    out bool isRunning,
    out string label,
    out int percent
    )
```

- `isRunning` (Boolean %) — Returns whether the server process is still running.
- `label` (String %) — Returns the label to show for the progress.
- `percent` (Int32 %) — Returns the percent complete for the server process.

---

## Multiuser class

Provides facilities to control multi-user access to ACCPAC. Multi-user access is controlled by performing locking on predefined resources.

**Namespace:** ACCPAC.Advantage &nbsp;·&nbsp; **Assembly:** ACCPAC.Advantage.dll

```csharp
public class Multiuser : IMultiuserComInterop
```

An object of this class cannot be created directly by applications. It should be obtained from the Session object's Multiuser property. Locking can be done on the following resources: A specific resource identified by a resource string. An application's data. This is always identified by an organization ID of the database, together with the 2-letter application ID. An organization's data. This is always identified by an organization ID of the database. Avoid using the Multiuser object if possible. Locking should be done by views rather than by UIs. Locking is especially dangerous when ACCPAC is running remotely over the internet.

### Methods

| Name | Description |
|---|---|
| `LockApp` | Locks an application's data shared or exclusive. A lock on an application's data is always specified by the organization (database) ID and the application ID. |
| `LockOrg` | Locks an organization's data shared or exclusive. |
| `LockRsc` | Locks a resource shared or exclusive. |
| `RegradeApp` | Upgrades or downgrades an existing lock on an application's data. |
| `RegradeOrg` | Upgrades or downgrades an existing lock on an organization's data. |
| `Test` | Tests if the specified resource is locked. |
| `UnlockApp` | Unlocks an application's data that was previously locked. |
| `UnlockOrg` | Unlocks an organization's data that was previously locked. |
| `UnlockRsc` | Unlocks a previously locked resource. |

### Method details

#### Multiuser.LockApp

```csharp
public MultiuserStatus LockApp(
    string orgID,
    string appID,
    bool exclusive
    )
```

- `orgID` (String) — Organization ID of the database.
- `appID` (String) — Application ID.
- `exclusive` (Boolean) — Indicates whether to lock the resource in exclusive mode. If specified as false, the application data will be locked in shared mode.

**Returns:** Returns the status of the routine. If the resource was already locked by another process with an incompatible exclusive/shared flag, the routine returns MultiuserStatus.Locked.

#### Multiuser.LockOrg

```csharp
public MultiuserStatus LockOrg(
    string orgID,
    bool exclusive
    )
```

- `orgID` (String) — Organization ID of the database.
- `exclusive` (Boolean) — Indicates whether to lock the resource in exclusive. If specified as false, the resource will be locked in shared mode.

**Returns:** Returns the status of the routine. If the specified resource was already locked by another process with an incompatible exclusive/shared mode, the routine returns MultiuserStatus.Locked.

#### Multiuser.LockRsc

```csharp
public MultiuserStatus LockRsc(
    string resource,
    bool exclusive
    )
```

- `resource` (String) — The resource to lock.
- `exclusive` (Boolean) — Indicates whether to lock the resource in exclusive mode. Specifying false locks the resource is shared mode.

**Returns:** Returns the status of the routine. If the resource was already locked by another process with an incompatible exclusive/shared flag, the routine returns MultiuserStatus.Locked.

#### Multiuser.RegradeApp

```csharp
public MultiuserStatus RegradeApp(
    string orgID,
    string appID,
    bool upgrade
    )
```

- `orgID` (String) — Organization ID of the database.
- `appID` (String) — Application ID.
- `upgrade` (Boolean) — Indicates whether to upgrade a shared lock to exclusive. If specified as false, the routine downgrades an exclusive lock to shared mode.

**Returns:** Returns the status of the routine. If the specified resource was not previosly locked by the current process, the routine returns MultiuserStatus.NotLocked. When upgrading a lock, and if the specified resource was already locked by another process with an incompatible exclusive/shared mode, the routine returns MultiuserStatus.Locked.

#### Multiuser.RegradeOrg

```csharp
public MultiuserStatus RegradeOrg(
    string orgID,
    bool upgrade
    )
```

- `orgID` (String) — Organization ID of the database.
- `upgrade` (Boolean) — Indicates whether to upgrade a shared lock to exclusive. If specified as false, the routine downgrades an exclusive lock to shared mode.

**Returns:** Returns the status of the routine. If the specified resource was not previosly locked by the current process, the routine returns MultiuserStatus.NotLocked. When upgrading a lock, and if the specified resource was already locked by another process with an incompatible exclusive/shared mode, the routine returns MultiuserStatus.Locked.

#### Multiuser.Test

```csharp
public bool Test(
    string resource,
    out bool exclusive
    )
```

- `resource` (String) — The resource.
- `exclusive` (Boolean %) — If the specified resource is locked, this parameter returns whether the lock is an exclusve lock.

**Returns:** Returns whether the specified resource is locked.

#### Multiuser.UnlockApp

```csharp
public MultiuserStatus UnlockApp(
    string orgID,
    string appID
    )
```

- `orgID` (String) — Organization ID of the database.
- `appID` (String) — Application ID.

**Returns:** Returns the status of the routine. If the resource was not previously locked by the current process, the routine returns MultiuserStatus.NotLocked.

#### Multiuser.UnlockOrg

```csharp
public MultiuserStatus UnlockOrg(
    string orgID
    )
```

- `orgID` (String) — Organization ID of the database.

**Returns:** Returns the status of the routine. If the specified resource was not previously locked by the current process, the routine returns MultiuserStatus.NotLocked.

#### Multiuser.UnlockRsc

```csharp
public MultiuserStatus UnlockRsc(
    string resource
    )
```

- `resource` (String) — The resource to unlock.

**Returns:** Returns the status of the routine. If the resource was not previously locked by the current process, the routine returns MultiuserStatus.NotLocked.

---

## Organization class

Represents an organization set up in ACCPAC. An organization refers to a database defined in Database Setup.

**Namespace:** ACCPAC.Advantage &nbsp;·&nbsp; **Assembly:** ACCPAC.Advantage.dll

```csharp
public class Organization : IOrganizationComInterop
```

An object of this class cannot be created directly by applications. It should be obtained from the Organizations collection. There are two kinds of databases that could be defined in ACCPAC: Company databases that store application data. Each company database must be linked to a system database. System databases that store information which could be common to multiple company databases, for example, currency information. A system database can be linked to multiple company databases.

### Properties

| Name | Description |
|---|---|
| `ID` | Gets the organization ID. |
| `Name` | Gets the name of the organization. |
| `SecurityEnabled` | Indicates whether security is enabled on the organization. |
| `SystemID` | Gets the organization ID of the system database the current organization uses. If the current database is already a system database, the SystemID is the same as ID. ID property |
| `Type` | Gets the type of the organization, whether it is a company or system database. |

---

## Organizations class

A collection of all the organizations set up in ACCPAC.

**Namespace:** ACCPAC.Advantage &nbsp;·&nbsp; **Assembly:** ACCPAC.Advantage.dll

```csharp
public class Organizations : IOrganizationsComInterop,
    IEnumerable
```

An object of this class cannot be created directly by applications. It should be obtained from the Session object's Organizations property.

### Properties

| Name | Description |
|---|---|
| `Count` | Gets the number of organizations stored in the collection. |
| `Item` | Gets an Organization object that stores details of an organization. The object is identified by its zero-based index in the collection. |

### Methods

| Name | Description |
|---|---|
| `GetEnumerator` | Returns an IEnumerator object of the Organizations collection. The object can be used to enumerate through all the items in the collection. |

### Method details

#### Organizations.GetEnumerator

```csharp
public IEnumerator GetEnumerator()
```

**Returns:** Returns an IEnumberator object of the Organizations collection.

---

## PrintSetup class

Stores the printer settings to be used for reporting and provides facilities to query the user and save default print settings.

**Namespace:** ACCPAC.Advantage &nbsp;·&nbsp; **Assembly:** ACCPAC.Advantage.dll

```csharp
public class PrintSetup : IPrintSetupComInterop
```

### Properties

| Name | Description |
|---|---|
| `Destination` | Gets/sets the print destination. |
| `DeviceName` | Gets/sets the device name of the printer. |
| `DriverName` | Gets/sets the name of the printer driver. |
| `Duplex` | Gets/sets whether to use duplex printing. |
| `Orientation` | Gets/sets the print orientation. |
| `OutputName` | Gets/sets the device name for the physical output medium. This is usually the name of the printer port. |
| `PaperSize` | Gets/sets the paper size. |
| `PaperSource` | Gets/sets the paper source. |
| `Parent` | Gets the Session object that created this object. |
| `PrintDirectory` | Gets/sets the output directory, if the print destination is a file. |

### Methods

| Name | Description |
|---|---|
| `Query` | Displays the Windows printer setup dialog that allows the user to select printer settings. |
| `Save` | Saves the current printer settings to the user-specific property file. |

### Method details

#### PrintSetup.Query

```csharp
public bool Query(
    int hwnd
    )
```

- `hwnd` (Int32) — Windows handle of the parent window.

**Returns:** Returns whether printer settings have been changed by the user.

#### PrintSetup.Save

```csharp
public void Save()
```

---

## ProcessServerSetup class

Provides facilities to specify configuration settings for Process Server. The settings are required when accessing views or reports that require the use of Process Server.

**Namespace:** ACCPAC.Advantage &nbsp;·&nbsp; **Assembly:** ACCPAC.Advantage.dll

```csharp
public class ProcessServerSetup : IProcessServerSetupComInterop
```

### Properties

| Name | Description |
|---|---|
| `ClientComputerName` | Reserved for ACCPAC internal use only. |
| `HostCount` | Reserved for ACCPAC internal use only. |
| `HostMayDoImmediately` | Reserved for ACCPAC internal use only. |
| `HostMaySchedule` | Reserved for ACCPAC internal use only. |
| `IsProcessServerOptional` | Indicates whether Process Server is optional for the target object. |
| `IsRemoteSession` | Reserved for ACCPAC internal use only. |
| `IsReportType` | Reserved for ACCPAC internal use only. |
| `IsScheduledDaily` | Gets/sets whether the job is scheduled as a daily job. |
| `IsScheduledOnce` | Gets/sets whether the job is scheduled as a one-time only job. |
| `IsViewImmediatelyOnly` | Reserved for ACCPAC internal use only. |
| `IsViewScheduleOnly` | Reserved for ACCPAC internal use only. |
| `IsViewType` | Reserved for ACCPAC internal use only. |
| `JobComment` | Reserved for ACCPAC internal use only. |
| `RunImmediately` | Gets/sets whether the job should be run immediately, as opposed to scheduled. |
| `ScheduleDate` | Gets/sets the schedule date of the job. |
| `SelectedHostName` | Gets/sets the selected host name of the Process Server. |
| `UseProcessServer` | Gets/sets whether Process Server should be used on the target object. |

### Methods

| Name | Description |
|---|---|
| `BeginCall` | Reserved for ACCPAC internal use only. |
| `EndCall` | Reserved for ACCPAC internal use only. |
| `GetHostDetail` | Reserved for ACCPAC internal use only. |
| `GetProcessServerHostList` | Reserved for ACCPAC internal use only. |

### Method details

#### ProcessServerSetup.BeginCall

```csharp
public DateTime BeginCall(
    string viewCall
    )
```

- `viewCall` (String) — Reserved for ACCPAC internal use only.

#### ProcessServerSetup.EndCall

```csharp
public DateTime EndCall(
    string viewCall,
    out string data
    )
```

- `viewCall` (String) — Reserved for ACCPAC internal use only.
- `data` (String %) — Reserved for ACCPAC internal use only.

#### ProcessServerSetup.GetHostDetail

```csharp
public void GetHostDetail(
    out string hostDesc,
    out string hostAddress,
    out int portNumber
    )
```

- `hostDesc` (String %) — Reserved for ACCPAC internal use only.
- `hostAddress` (String %) — Reserved for ACCPAC internal use only.
- `portNumber` (Int32 %) — Reserved for ACCPAC internal use only.

#### ProcessServerSetup.GetProcessServerHostList

```csharp
public void GetProcessServerHostList(
    out string[] hostNames,
    out string[] hostDescs,
    out int[] flags
    )
```

- `hostNames` (String[] %) — Reserved for ACCPAC internal use only.
- `hostDescs` (String[] %) — Reserved for ACCPAC internal use only.
- `flags` (Int32[] %) — Reserved for ACCPAC internal use only.

---

## Report class

Provides facilities for generating reports.

**Namespace:** ACCPAC.Advantage &nbsp;·&nbsp; **Assembly:** ACCPAC.Advantage.dll

```csharp
public class Report : IReportComInterop, IDisposable
```

An object of this class cannot be created directly by applications. It should be obtained from the Session object's ReportSelect method."

### Properties

| Name | Description |
|---|---|
| `Collate` | Gets/sets whether the print out will be collated, if number of copies is set to more than one. This property is ignored if the print destination is not Printer. |
| `Destination` | Gets/sets the report print destination. |
| `Format` | Gets/sets the output format of the report. Currently, this property is valid only if output destination is set as Email, and ignored for all other print destinations. |
| `Name` | Gets the name of the report. |
| `NumberOfCopies` | Gets/sets the number of copies to print. The property is valid only if the print destination is Printer. It is ignored for all other print destinations. |
| `PrintDirectory` | Gets/sets the output directory, if the print destination is set as File. The property should be set as the full path to the output directory. It is ignored for all other print destinations. |
| `RequiresProcessServer` | Indicates whether the report must be configured for the Process Server before printing. |
| `WebReportURL` | Gets the URL to access the printed report, if the report was generated as a web report. |

### Methods

| Name | Description |
|---|---|
| `CompleteProcessServerSettings` | Applies the Process Server settings for the report. |
| `Confirm` | Instructs the system to populate the object with default print settings saved in the user-specific properties file, and optionally display a print settings dialog that allows the user to select various print settings. |
| `Dispose` | Closes the report and releases the resources used by the object. |
| `GetProcessServerSetup` | Gets a ProcessServerSetup object for this report that can be used to configure settings for Process Server. |
| `MsgrConnect` | Connects to ACCPAC Messenger. |
| `MsgrDisconnect` | Disconnects from ACCPAC Messenger. |
| `Print` | Prints the report to the desired destination. |
| `PrinterSetup` | Configures the Report object with settings stored in a PrintSetup object. |
| `ReInit` | Re-initializes the report object to its initial state when it was first created. |
| `SetParam` | Sets the value of a report parameter. |

### Method details

#### Report.CompleteProcessServerSettings

```csharp
public int CompleteProcessServerSettings()
```

#### Report.Confirm

```csharp
public bool Confirm(
    bool showDialog,
    int hwnd
    )
```

- `showDialog` (Boolean) — Whether a print settings dialog should be displayed for the user to select print settings.
- `hwnd` (Int32) — Windows handle of the parent window.

**Returns:** Returns whether print settings have been changed, either by the system or the user if a print settings dialog was displayed.

If the current object accesses a remote ACCPAC server, showDialog is ignored and no print settings dialog will be displayed. The call also sets the print detination to Preview in this case.

#### Report.Dispose

```csharp
public void Dispose()
```

#### Report.GetProcessServerSetup

```csharp
public ProcessServerSetup GetProcessServerSetup()
```

**Returns:** Returns the ProcessServerSetup object.

#### Report.MsgrConnect

```csharp
public void MsgrConnect(
    bool bShowDialog,
    out bool pVal
    )
```

- `bShowDialog` (Boolean) — Whether or not to show the dialog.
- `pVal` (Boolean %) — Returns whether or not the connection succeeded.

#### Report.MsgrDisconnect

```csharp
public void MsgrDisconnect()
```

#### Report.Print

```csharp
public bool Print()
```

**Returns:** Returns whether the report was generated as a web-based report.

A web-based report is generated when the current session is accessing a remote ACCPAC application server. In this case, the WebReportURL property stores the URL where the report could be retrieved.

#### Report.PrinterSetup

```csharp
public void PrinterSetup(
    PrintSetup setup
    )
```

- `setup` (PrintSetup) — The PrintSetup object that stores the desired settings.

#### Report.ReInit

```csharp
public void ReInit()
```

This method is useful for printing multiple instances of a report using the same report object, but with different parameters.

#### Report.SetParam

```csharp
public bool SetParam(
    string paramName,
    string paramValue
    )
```

- `paramName` (String) — Parameter name. The name must be a valid parameter defined for the current report.
- `paramValue` (String) — Parameter value.

**Returns:** Returns whether the parameter was successfully set. The function returns false if the specified parameter name is not recognized as a valid parameter defined for the report.

---

## SessionException class

The exception that is thrown when a call to any methods/properties on the Session object fails. The exception contains a reason that states why the exception was thrown.

**Namespace:** ACCPAC.Advantage &nbsp;·&nbsp; **Assembly:** ACCPAC.Advantage.dll

```csharp
[SerializableAttribute]
    public class SessionException : ApplicationException
```

### Constructors

| Name | Description |
|---|---|
| `SessionException` | Initializes a SessionException object and attaches the original exception that caused this excpetion. |
| `SessionException` | Initializes a new SessionException object with a reason. |
| `SessionException` | Initializes a new instance of the SessionException class with serialized data. |
| `SessionException` | Initializes a SessionException object with a reason, and also attaches the original exception that caused this exception. |

### Properties

| Name | Description |
|---|---|
| `Reason` | Gets the reason why the exception was thrown. |

### Methods

| Name | Description |
|---|---|
| `GetObjectData` | Sets information about the exception for serialization. |

### Method details

#### SessionException.GetObjectData

```csharp
public override void GetObjectData(
    SerializationInfo info,
    StreamingContext context
    )
```

- `info` (SerializationInfo) — The object that holds the serialized object data.
- `context` (StreamingContext) — The contextual information about the source or destination.

This method is used for serialization. Applications do not need to call this method.

---

## SpyLog class

Provides facilities for applications to output spy (trace) messages. This is different from debug messages since the SpyLog class takes effect as well for release builds.

**Namespace:** ACCPAC.Advantage &nbsp;·&nbsp; **Assembly:** ACCPAC.Advantage.dll

```csharp
public class SpyLog
```

This class makes use of the System.Diagnostics.Trace class to output trace messages. It is a wrapper around System.Diagnostics.Trace, with the addition of classifying the sources of trace messages by: An object name. This is usually the name of the class outputing the trace messages, but it is configurable by applications if another name is desired. An instance name to identify a particular instance of the class. This is usually a GUID that is automatically generated, but is configurable by applications if a specific name is desired. The SpyLog object generates the category name for System.Diagnostics.Trace based on the object and instance name.

### Constructors

| Name | Description |
|---|---|
| `SpyLog` | Constructs a SpyLog object, passing along the object instance of the caller. The object name defaults to the full name of the caller. |
| `SpyLog` | Constructs a SpyLog object with an application defined object name. |

### Properties

| Name | Description |
|---|---|
| `InstanceName` | Gets/sets the instance name to use for trace messages. |

### Methods

| Name | Description |
|---|---|
| `Write` | Outputs a trace message. |

### Method details

#### SpyLog.Write

```csharp
public void Write(
    string message
    )
```

- `message` (String) — Trace message.

```csharp
public void Write(
    string format,
    Object arg0
    )
```

- `format` (String) — The format string. It should conform to the format which System.String.Format expects.
- `arg0` (Object) — Parameter to the format string.

```csharp
public void Write(
    string format,
    params Object[] args
    )
```

- `format` (String) — The format string. It should conform to the format which System.String.Format expects.
- `args` (Object[]) — An array of parameters to the format string.

```csharp
public void Write(
    string format,
    Object arg0,
    Object arg1
    )
```

- `format` (String) — The format string. It should conform to the format which System.String.Format expects.
- `arg0` (Object) — First parameter to the format string.
- `arg1` (Object) — Second parameter to the format string.

```csharp
public void Write(
    string format,
    Object arg0,
    Object arg1,
    Object arg2
    )
```

- `format` (String) — The format string. It should conform to the format which System.String.Format expects.
- `arg0` (Object) — First parameter to the format string.
- `arg1` (Object) — Second parameter to the format string.
- `arg2` (Object) — Third parameter to the format string.

---

## ViewException class

The exception that is thrown when a call to any methods/properties of the View object fails. This object stores the original return code from the view that caused this exception.

**Namespace:** ACCPAC.Advantage &nbsp;·&nbsp; **Assembly:** ACCPAC.Advantage.dll

```csharp
[SerializableAttribute]
    public class ViewException : ApplicationException
```

### Constructors

| Name | Description |
|---|---|
| `ViewException` | Initializes a ViewException object with the original view return code. |
| `ViewException` | Initializes a ViewException object with the original view return code, and attaches the original exception that caused this exception. |
| `ViewException` | Initializes a new instance of the ViewException class with serialized data. |

### Properties

| Name | Description |
|---|---|
| `Reason` | Gets the original view return code that caused this exception to be thrown. |

### Methods

| Name | Description |
|---|---|
| `GetObjectData` | Sets information about the exception for serialization. |

### Method details

#### ViewException.GetObjectData

```csharp
public override void GetObjectData(
    SerializationInfo info,
    StreamingContext context
    )
```

- `info` (SerializationInfo) — The object that holds the serialized object data.
- `context` (StreamingContext) — The contextual information about the source or destination.

This method is used for serialization. Applications do not need to call this method.


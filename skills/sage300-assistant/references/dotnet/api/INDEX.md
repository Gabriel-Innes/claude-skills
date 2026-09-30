# ACCPAC.Advantage .NET API reference (from the CHM)

Authoritative class/enum surface of the Sage Accpac .NET class library (`ACCPAC.Advantage.dll` + `ACCPAC.Advantage.Types.dll`), extracted from `Sage Accpac .NET Libraries.chm` (library version 5.5.0.1). Verified 2026-09-25. This is the *signature/enum* reference; for how to actually drive views end-to-end see `../view-api.md`, `../compose-graphs.md`, and `../common-mistakes.md`.

All applications start from `Session` → `OpenDBLink` → `DBLink` → `OpenView` → `View`. Field access is through `View.Fields` (`Fields`/`ViewFields`) and `FieldByName`.

- **Enums:** [`enums.md`](enums.md) — all 38 enumerations with member meanings.
- **Classes:** grouped into 3 bundle files (each with summary, C# declaration, property & method tables, and per-method C# signatures/parameters/returns/remarks) — [`classes-session.md`](classes-session.md), [`classes-view.md`](classes-view.md), [`classes-system.md`](classes-system.md). The **File** column below links to each class's section.

## Classes

| Class | File | Props | Methods | Summary |
|---|---|--:|--:|---|
| `ActiveApplication` | [classes-system.md](classes-system.md#activeapplication-class) | 6 | 0 | Represents an activated application on an ACCPAC database. |
| `ActiveApplications` | [classes-system.md](classes-system.md#activeapplications-class) | 2 | 1 | A collection of activated applications on an ACCPAC database. |
| `ClientChannelSinkProvider` | [classes-system.md](classes-system.md#clientchannelsinkprovider-class) | 1 | 1 | For ACCPAC internal use only. |
| `Company` | [classes-system.md](classes-system.md#company-class) | 32 | 0 | Provides details of the company set up in Common Services Company Profile. |
| `Currency` | [classes-system.md](classes-system.md#currency-class) | 8 | 3 | Stores details of a currency code set up in Common Services. |
| `CurrencyRate` | [classes-system.md](classes-system.md#currencyrate-class) | 8 | 0 | Represents a currency exchange rate. |
| `CurrencyTable` | [classes-system.md](classes-system.md#currencytable-class) | 6 | 0 | Stores details of a currency table set up in Common Services. |
| `DBLink` | [classes-view.md](classes-view.md#dblink-class) | 8 | 23 | Represents a database link or connection to an ACCPAC company or system database. |
| `DBLinkException` | [classes-system.md](classes-system.md#dblinkexception-class) | 1 | 1 | The exception that is thrown when a call to any methods/properties on the DBLink object fails. The exception stores the original error code from the ACCPAC database layer that caused this exception. |
| `Error` | [classes-system.md](classes-system.md#error-class) | 6 | 0 | Provides details of an application error. |
| `Errors` | [classes-system.md](classes-system.md#errors-class) | 2 | 4 | Stores all the errors raised within the context of the current session. |
| `FiscalCalendar` | [classes-system.md](classes-system.md#fiscalcalendar-class) | 1 | 10 | Provides methods to access the fiscal calendar set up in the company. |
| `Meter` | [classes-system.md](classes-system.md#meter-class) | 6 | 2 | Provides access to progress information on long server processes. |
| `Multiuser` | [classes-system.md](classes-system.md#multiuser-class) | 0 | 9 | Provides facilities to control multi-user access to ACCPAC. Multi-user access is controlled by performing locking on predefined resources. |
| `Organization` | [classes-system.md](classes-system.md#organization-class) | 5 | 0 | Represents an organization set up in ACCPAC. An organization refers to a database defined in Database Setup. |
| `Organizations` | [classes-system.md](classes-system.md#organizations-class) | 2 | 1 | A collection of all the organizations set up in ACCPAC. |
| `PrintSetup` | [classes-system.md](classes-system.md#printsetup-class) | 10 | 2 | Stores the printer settings to be used for reporting and provides facilities to query the user and save default print settings. |
| `ProcessServerSetup` | [classes-system.md](classes-system.md#processserversetup-class) | 17 | 4 | Provides facilities to specify configuration settings for Process Server. The settings are required when accessing views or reports that require the use of Process Server. |
| `Report` | [classes-system.md](classes-system.md#report-class) | 8 | 10 | Provides facilities for generating reports. |
| `Session` | [classes-session.md](classes-session.md#session-class) | 36 | 58 | Represents an authenticated session with ACCPAC System Manager. This object is also the root to other facilities of the ACCPAC .NET Class Library. All other objects in the library are created either directly or indirectly by the Session object. |
| `SessionException` | [classes-system.md](classes-system.md#sessionexception-class) | 1 | 1 | The exception that is thrown when a call to any methods/properties on the Session object fails. The exception contains a reason that states why the exception was thrown. |
| `SpyLog` | [classes-system.md](classes-system.md#spylog-class) | 1 | 1 | Provides facilities for applications to output spy (trace) messages. This is different from debug messages since the SpyLog class takes effect as well for release builds. |
| `View` | [classes-view.md](classes-view.md#view-class) | 31 | 41 | Represents an ACCPAC view. |
| `ViewException` | [classes-system.md](classes-system.md#viewexception-class) | 1 | 1 | The exception that is thrown when a call to any methods/properties of the View object fails. This object stores the original return code from the view that caused this exception. |
| `ViewField` | [classes-view.md](classes-view.md#viewfield-class) | 16 | 3 | Represents a field in an ACCPAC view. The class provides methods and properties to access details of a view field, as well as manipulating field values. |
| `ViewFieldPresentationList` | [classes-view.md](classes-view.md#viewfieldpresentationlist-class) | 4 | 4 | Provides access to the presentation list that is exposed by a field in an ACCPAC view. |
| `ViewFields` | [classes-view.md](classes-view.md#viewfields-class) | 3 | 3 | Provides access to ViewField objects that include all fields exposed by a view. |
| `ViewInternal` | [classes-view.md](classes-view.md#viewinternal-class) | 0 | 35 | Reserved for ACCPAC internal use only. |
| `ViewKey` | [classes-view.md](classes-view.md#viewkey-class) | 4 | 1 | Represents a key defined in an ACCPAC view. |
| `ViewKeys` | [classes-view.md](classes-view.md#viewkeys-class) | 3 | 0 | Provides access to ViewKey objects that include all keys defined in an ACCPAC view. |
| `ViewReturnCode` | [classes-view.md](classes-view.md#viewreturncode-class) | 0 | 0 | Defines return codes of view operations. This class defines common view return codes as constants. |

## Enumerations

| Enum | Summary |
|---|---|
| [`CompanyGainLossAccountingMethod`](enums.md#companygainlossaccountingmethod) | Indicates which exchange gain/loss accounting method to use when the company is a multicurrency company. |
| [`CompanyHandleInactiveGLAccounts`](enums.md#companyhandleinactiveglaccounts) | Indicates how inactive General Ledgar accounts should be handled. |
| [`CompanyHandleLockedFiscalPeriods`](enums.md#companyhandlelockedfiscalperiods) | Indicates how locked fiscal periods should be handled. |
| [`CompanyHandleNonexistentGLAccounts`](enums.md#companyhandlenonexistentglaccounts) | Indicates how non-existent General Ledgar accounts should be handled. |
| [`CurrencyBlockDateMatch`](enums.md#currencyblockdatematch) | Indicates the date matching method used to determine whether a currency belongs to currency block. |
| [`CurrencyDateMatch`](enums.md#currencydatematch) | Indicates the date matching method used when determining an exchange rate with respect to a given date. |
| [`CurrencyNegativeDisplay`](enums.md#currencynegativedisplay) | Indicates how negative currency amounts should be displayed. |
| [`CurrencyRateOperator`](enums.md#currencyrateoperator) | Defines the operator that should be used when performing currency exchange calculations. |
| [`CurrencyRateType`](enums.md#currencyratetype) | Indicates the type a currency rate represents. |
| [`CurrencySymbolDisplay`](enums.md#currencysymboldisplay) | Indicates how the currency symbol should be displayed with a currency amount. |
| [`DatabaseSeries`](enums.md#databaseseries) | Indicates the database engine of a database connection. |
| [`DBLinkFlags`](enums.md#dblinkflags) | Indicates the access mode of a database link/connection. |
| [`DBLinkType`](enums.md#dblinktype) | Indicates the type of an ACCPAC database. |
| [`ErrorPriority`](enums.md#errorpriority) | Indicates the type of an application error. |
| [`FileLocation`](enums.md#filelocation) | Specifies the location of a particular file. This is used in routines that involve file transfer between server and client machines and is used to indicate the file location. |
| [`FiscalPeriodType`](enums.md#fiscalperiodtype) | Indicates what a fiscal period is defined for the current company. |
| [`LicenseStatus`](enums.md#licensestatus) | Indicates the status of an application license. |
| [`MultiuserStatus`](enums.md#multiuserstatus) | Return code of Multiuser routines. |
| [`OrganizationType`](enums.md#organizationtype) | Indicates the type of an ACCPAC database. |
| [`PrintDestination`](enums.md#printdestination) | Indicates the destination where reports should be printed |
| [`PrintFormat`](enums.md#printformat) | Indicates the desired print output format. This is only applicable if the print destination is a file. |
| [`ProductSeries`](enums.md#productseries) | Indicates the ACCPAC product series for the current ACCPAC installation. |
| [`PropertyType`](enums.md#propertytype) | Indicates the data type desired when retrieving an ACCPAC property. |
| [`Session.RemoteConnectProtocol`](enums.md#sessionremoteconnectprotocol) | Defines the supported protocols for remoting. |
| [`SessionExceptionReason`](enums.md#sessionexceptionreason) | Defines the possible reasons for a SessionException being thrown. |
| [`ViewFieldAttributes`](enums.md#viewfieldattributes) | Field attributes. Whenever a field attribute is used, the value can be a combination of the values defined here to indicate all attributes of the field. |
| [`ViewFieldPresentationType`](enums.md#viewfieldpresentationtype) | Indicates the type of presentation information defined for a field. |
| [`ViewFieldType`](enums.md#viewfieldtype) | Defines the possible data types of a view field. |
| [`ViewFilterOrigin`](enums.md#viewfilterorigin) | Specifies the origin from where the a filter should be applied. |
| [`ViewFilterStrictness`](enums.md#viewfilterstrictness) | Specifies the behaviour of a filter used for record deleting under questionable situations related to referential integrity. |
| [`ViewOpenDirectives`](enums.md#viewopendirectives) | Indicates the method to be used when opening a view. |
| [`ViewOpenModes`](enums.md#viewopenmodes) | Defines all the valid modes when opening a view. The mode that is actually used can be a combination of multiple defined values. |
| [`ViewProtocol`](enums.md#viewprotocol) | Specifies the protocol of a view |
| [`ViewRecordCreate`](enums.md#viewrecordcreate) | Specifies the behavior of RecordCreate on the View object. |
| [`ViewReferentialIntegrity`](enums.md#viewreferentialintegrity) | Indicates the referential integrity flag of a view. |
| [`ViewRotoType`](enums.md#viewrototype) | Indicates the type of a view. |
| [`ViewSecurity`](enums.md#viewsecurity) | Indicates the functionality the user is permitted to access on the view. A security permission can be a combination of multiple defined values. |
| [`ViewSystemAccess`](enums.md#viewsystemaccess) | Indicates the current access mode of a view. |

> The 25 `IXxxComInterop` interfaces in the assembly are internal COM-interop plumbing (undocumented) and are intentionally omitted.

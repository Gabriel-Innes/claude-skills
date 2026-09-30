# ACCPAC.Advantage enumerations

Every enumeration in the Sage Accpac .NET class library, with each member's meaning. Use the **named constant** in C# (e.g. `DBLinkType.Company`, `ViewOpenModes.Readonly`) — never a magic int. Flags enums combine with `|`. Extracted from `Sage Accpac .NET Libraries.chm` (library version 5.5.0.1). Verified 2026-09-25.

38 enumerations: `CompanyGainLossAccountingMethod`, `CompanyHandleInactiveGLAccounts`, `CompanyHandleLockedFiscalPeriods`, `CompanyHandleNonexistentGLAccounts`, `CurrencyBlockDateMatch`, `CurrencyDateMatch`, `CurrencyNegativeDisplay`, `CurrencyRateOperator`, `CurrencyRateType`, `CurrencySymbolDisplay`, `DatabaseSeries`, `DBLinkFlags`, `DBLinkType`, `ErrorPriority`, `FileLocation`, `FiscalPeriodType`, `LicenseStatus`, `MultiuserStatus`, `OrganizationType`, `PrintDestination`, `PrintFormat`, `ProductSeries`, `PropertyType`, `Session.RemoteConnectProtocol`, `SessionExceptionReason`, `ViewFieldAttributes`, `ViewFieldPresentationType`, `ViewFieldType`, `ViewFilterOrigin`, `ViewFilterStrictness`, `ViewOpenDirectives`, `ViewOpenModes`, `ViewProtocol`, `ViewRecordCreate`, `ViewReferentialIntegrity`, `ViewRotoType`, `ViewSecurity`, `ViewSystemAccess`

---

## CompanyGainLossAccountingMethod

Indicates which exchange gain/loss accounting method to use when the company is a multicurrency company.

| Member | Description |
|---|---|
| `Unrealized` | Use the realized and unrealized exchange gain/loss accounting method. |
| `Recognized` | Use the recognized exchange gain/loss accounting method only. |

## CompanyHandleInactiveGLAccounts

Indicates how inactive General Ledgar accounts should be handled.

| Member | Description |
|---|---|
| `Ignore` | Ignore. |
| `Warning` | Display a warning. |
| `Error` | Raise an error. |

## CompanyHandleLockedFiscalPeriods

Indicates how locked fiscal periods should be handled.

| Member | Description |
|---|---|
| `Ignore` | Ignore. |
| `Warning` | Display a warning. |
| `Error` | Raise an error. |

## CompanyHandleNonexistentGLAccounts

Indicates how non-existent General Ledgar accounts should be handled.

| Member | Description |
|---|---|
| `Ignore` | Ignore. |
| `Warning` | Display a warning. |
| `Error` | Raise an error. |

## CurrencyBlockDateMatch

Indicates the date matching method used to determine whether a currency belongs to currency block.

| Member | Description |
|---|---|
| `Exact` | ??? |
| `OnOrBefore` | ??? |

## CurrencyDateMatch

Indicates the date matching method used when determining an exchange rate with respect to a given date.

| Member | Description |
|---|---|
| `Exact` | Gets the rate for the same date as the given date. |
| `Later` | Gets the rate for the first date after the given date. |
| `Earlier` | Gets the rate for the first date before the given date. |

## CurrencyNegativeDisplay

Indicates how negative currency amounts should be displayed.

| Member | Description |
|---|---|
| `TrailingMinus` | Display with a trailing negative sign. |
| `LeadingMinus` | Display with a leading negative sign. |
| `Brackets` | Display inside brackets. |

## CurrencyRateOperator

Defines the operator that should be used when performing currency exchange calculations.

| Member | Description |
|---|---|
| `Multiplication` | The home (functional) currency amount should be obtined by multiplying the source currency amount with the exchange rate. |
| `Division` | The home (functional) currency amount should be obtained by dividing the source currency amount with the exchange rate. |

## CurrencyRateType

Indicates the type a currency rate represents.

| Member | Description |
|---|---|
| `RateTable` | The exchange rate is a direct conversion rate between two currencies. |
| `RateComposite` | The exchange rate is a composite rate between a currency that belongs to a currency block, and the currency block's master currency. |
| `RateFloating` | The exchange rate is a floating rate between a currency block's master currency and another currency. |

## CurrencySymbolDisplay

Indicates how the currency symbol should be displayed with a currency amount.

| Member | Description |
|---|---|
| `BeforeWithSpace` | Display currency symbol before the amount, with a space in between. |
| `BeforeWithoutSpace` | Display currency symbol before the amount, without spaces. |
| `AfterWithSpace` | Display currency symbol after the amount, with a space in between. |
| `AfterWithoutSpace` | Display currency symbol after the amount, without spaces. |

## DatabaseSeries

Indicates the database engine of a database connection.

| Member | Description |
|---|---|
| `Pervasive` | Pervasive.SQL |
| `SQLServer` | Microsoft SQL Server |
| `DB2` | IBM DB2 |
| `Oracle` | Oracle |

## DBLinkFlags

Indicates the access mode of a database link/connection.

| Member | Description |
|---|---|
| `ReadWrite` | Read-writable database connection. |
| `ReadOnly` | Read-only database connection. |
| `ReadUncommitted` | Reserved for ACCPAC internal use. |
| `ReadWriteShared` | Reserved for ACCPAC internal use. |
| `ReadOnlyShared` | Reserved for ACCPAC internal use. |

## DBLinkType

Indicates the type of an ACCPAC database.

| Member | Description |
|---|---|
| `System` | System database |
| `Company` | Company database |

## ErrorPriority

Indicates the type of an application error.

| Member | Description |
|---|---|
| `SevereError` | Severe error |
| `Message` | Message |
| `Warning` | Warning |
| `Error` | Error |
| `Security` | Security violation |

## FileLocation

Specifies the location of a particular file. This is used in routines that involve file transfer between server and client machines and is used to indicate the file location.

| Member | Description |
|---|---|
| `Client` | The specified file path is a local path on the client machine. |
| `Company` | Specifies the COMPANY subdirectory under the Shared Data Directory on the server. |

## FiscalPeriodType

Indicates what a fiscal period is defined for the current company.

| Member | Description |
|---|---|
| `SevenDays` | A fiscal period contains 7 days. |
| `Weekly` | A fiscal period represents a week, respecting Sunday/Saturday rule. |
| `Monthly` | A fiscal period represents a month. |

## LicenseStatus

Indicates the status of an application license.

| Member | Description |
|---|---|
| `OK` | The license is valid. |
| `NotFound` | License of the specified application could not be found. |
| `Expired` | License of the specified application has expired. |

## MultiuserStatus

Return code of Multiuser routines.

| Member | Description |
|---|---|
| `Success` | The requested call succeeded. |
| `Locked` | The specified resource has already been locked by another process. |
| `NotLocked` | The specified resource was not previously locked. |

## OrganizationType

Indicates the type of an ACCPAC database.

| Member | Description |
|---|---|
| `System` | System database |
| `Company` | Company database |
| `Combined` | Reserved. |

## PrintDestination

Indicates the destination where reports should be printed

| Member | Description |
|---|---|
| `Printer` | Print to printer. |
| `File` | Output to a file. |
| `Html` | Output to an HTML file. |
| `PrintConf` | Print to printer for alignment. Only the first page of the report will be printed and it is used for checking paper alignment before the whole report is printed. |
| `Preview` | Preview report in a preview window. |
| `Email` | Send an email with the print output as the attachment. |
| `Schedule` | Schedule the print job using Crystal Info. |

## PrintFormat

Indicates the desired print output format. This is only applicable if the print destination is a file.

| Member | Description |
|---|---|
| `None` | Not specified. The output format will be determined according to the user's preference. |
| `PDF` | Adobe Acrobat format. |
| `RTF` | Rich Text Format. |

## ProductSeries

Indicates the ACCPAC product series for the current ACCPAC installation.

| Member | Description |
|---|---|
| `Enterprise` | Enterprise Edition |
| `Corporate` | Corporate Edition |
| `Discovery` | Discovery Edition |
| `SmallBusiness` | Small Business Edition |

## PropertyType

Indicates the data type desired when retrieving an ACCPAC property.

| Member | Description |
|---|---|
| `Array` | The property should be returned as an array of bytes. |
| `String` | The property should be returned as a string. |

## Session.RemoteConnectProtocol

Defines the supported protocols for remoting.

| Member | Description |
|---|---|
| `Tcp` | Use TCP for remoting. |
| `Http` | Not supported in this version. |
| `Https` | Not supported in this version. |

## SessionExceptionReason

Defines the possible reasons for a SessionException being thrown.

| Member | Description |
|---|---|
| `NotSpecified` | The reason is not specified. Examine the InnerException in this case to get the original exception that caused this exception. |
| `Reserved` | The class/method/property is reserved for ACCPAC internal use only. |
| `NotInitialized` | Session is not initialized. The operation requested is available only after the session is initialized. |
| `NotOpened` | Session is not opened. The operation requested is available only after the session is opened. |
| `BadOpenParams` | The parameters supplied to open a session are invalid. |
| `LanpakMaxUsers` | Reached the maximum number of Lanpak users. |
| `BadSignon` | Invalid password specified. |
| `BadUserID` | Invalid username specified. |
| `TLMaxUsers` | Reached the maximum number Timecard users. |
| `TLNoAccess` | Timecard users are not allowed to perform the requested operation. |

## ViewFieldAttributes

Field attributes. Whenever a field attribute is used, the value can be a combination of the values defined here to indicate all attributes of the field.

| Member | Description |
|---|---|
| `Changed` | Field value has been changed. |
| `Enabled` | Field is enabled and accessible. |
| `Editable` | Field value can be altered. |
| `Key` | Field is part of the current selected key. |
| `Calculated` | Field is a calculated field. |
| `Type` | Field type can change. This is mainly used to indicate that the precision of the field can change. |
| `Presentation` | Field presentation information may change. |
| `Required` | Field value is required for inserting a record. |
| `CheckEditable` | The Editable attribute of the field may change. |

## ViewFieldPresentationType

Indicates the type of presentation information defined for a field.

| Member | Description |
|---|---|
| `None` | Field does not have presentation information. |
| `List` | Field has a presentation list. |
| `Mask` | Field uses a presentation mask to control the display format. |

## ViewFieldType

Defines the possible data types of a view field.

| Member | Description |
|---|---|
| `Char` | ASCII string. |
| `Byte` | Binary. |
| `Date` | Date. |
| `Time` | Time. |
| `Real` | 64-bit double-precision floating point. |
| `Decimal` | 128-bit high precision decimal. |
| `Int` | 16-bit signed integer. |
| `Long` | 32-bit signed integer. |
| `Bool` | Boolean. |

## ViewFilterOrigin

Specifies the origin from where the a filter should be applied.

| Member | Description |
|---|---|
| `FromStart` | The filter should be applied to all records in the view. |
| `FromCurrent` | The filter should be applied only to the current record and all records after it. |

## ViewFilterStrictness

Specifies the behaviour of a filter used for record deleting under questionable situations related to referential integrity.

| Member | Description |
|---|---|
| `Strict` | Applies the filter to delete records only if it does not violate referential integrity. Otherwise, return an error. |
| `Try` | Applies the filter to delete records if possible, without considering if it results in orphan secondary table and detail records. |
| `Simulate` | Applies the filter to delete records using the Strict method. If that results in a error, fallback to Fetch-Delete calls to the view. |

## ViewOpenDirectives

Indicates the method to be used when opening a view.

| Member | Description |
|---|---|
| `None` | Opens a view using viewOpen. |
| `InstanceOpen` | Opens a view using viewInstanceOpen. |
| `InstanceNotify` | Reserved. |

## ViewOpenModes

Defines all the valid modes when opening a view. The mode that is actually used can be a combination of multiple defined values.

| Member | Description |
|---|---|
| `None` | No open mode flags |
| `Readonly` | View should be opened read-only |
| `UnRevisioned` | Revisioning is turned off. |
| `UnValidated` | Suppress validation. |
| `Raw` | Data is not processed upon a field put. |
| `NoCascade` | Reserved. Not used in this release. |
| `NoInherit` | Composite views would not inherit the instance flags. |
| `Immediate` | View should be opened immediately, as opposed to a delayed load. |

## ViewProtocol

Specifies the protocol of a view

## ViewRecordCreate

Specifies the behavior of RecordCreate on the View object.

| Member | Description |
|---|---|
| `NoInsert` | Do not insert the record to the view after the generation. |
| `Insert` | Inserts the record to the view immediately after the record is generated. |
| `DelayKey` | ??? |

## ViewReferentialIntegrity

Indicates the referential integrity flag of a view.

| Member | Description |
|---|---|
| `None` | Referential integrity flag of the view is not set. |
| `Cascade` | Changes to the view should be cascaded to maintain referential integrity. |

## ViewRotoType

Indicates the type of a view.

| Member | Description |
|---|---|
| `View` | View is a base view. |
| `ViewSubclass` | View subclasses another view. |
| `ViewStub` | Stub view. |

## ViewSecurity

Indicates the functionality the user is permitted to access on the view. A security permission can be a combination of multiple defined values.

| Member | Description |
|---|---|
| `Add` | New records can be added. |
| `Modify` | Existing records can be changed. |
| `Delete` | Records can be deleted. |
| `Inquire` | Records can be read. |
| `Post` | Records can be posted. |

## ViewSystemAccess

Indicates the current access mode of a view.

| Member | Description |
|---|---|
| `Normal` | Normal view access. |
| `Import` | View is in import mode. |
| `Export` | View is in export mode. |
| `IntegrityCheck` | View is being accessed by an integrity check process. |
| `Macro` | View is being accessed by a macro. |
| `Activation` | View is being accessed by an activation program. |
| `Conversion` | View is being accessed by a conversion program. |
| `Posting` | View is performing a posting. |


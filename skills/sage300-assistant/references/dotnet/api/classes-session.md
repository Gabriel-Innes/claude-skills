# Session class

The `Session` class — the authenticated entry point to the whole library (`new Session()` → `Init` → `Open` → `OpenDBLink`). Every other object is reached directly or indirectly from here.

Extracted from `Sage Accpac .NET Libraries.chm` (library 5.5.0.1). Verified 2026-09-25. See [`INDEX.md`](INDEX.md) for the full class/enum map and [`enums.md`](enums.md) for enumerations.

Classes in this file: `Session`

---

## Session class

Represents an authenticated session with ACCPAC System Manager. This object is also the root to other facilities of the ACCPAC .NET Class Library. All other objects in the library are created either directly or indirectly by the Session object.

**Namespace:** ACCPAC.Advantage &nbsp;·&nbsp; **Assembly:** ACCPAC.Advantage.dll

```csharp
public class Session : ISessionComInterop, IDisposable
```

The Session object is the only object in the ACCPAC .NET class library that is directly creatable by application programs. An application should create a Session object, initialize and open the session before other facilities in the class library become available. A session can be opened through either of these methods: Initializing the session with a valid object handle, by calling Init . The object handle is usually supplied by System Manager, or if the application is launched by another application, the parent application. If a valid object handle is supplied during initialization, the session is automatically opened as well and does not require an explicit call to Open. Opening the session by calling Open , and supplying the correct ACCPAC user name and password. Before calling Open, a session object must first be initialized by calling Init, with "" passed in as the object handle.

### Properties

| Name | Description |
|---|---|
| `ACCPACVersion` | Gets the version of the current ACCPAC installation. |
| `ACCPACVersionBuild` | Gets the build number of the current ACCPAC installation. |
| `ACCPACVersionMajor` | Gets the major version number of the current ACCPAC installation. |
| `ACCPACVersionMinor` | Gets the minor version number of the current ACCPAC installation. |
| `ACCPACVersionRevision` | Gets the revision number of the current ACCPAC installation. |
| `AppID` | Gets the application ID of the current application. This is the appliation ID used to initialize the session. |
| `AppVersion` | Gets the version of the current application. This is the version used to initialize the session. |
| `Codebase` | — |
| `CompanyID` | Gets the company database ID that the current session is signed on to. |
| `CompanyName` | Gets the name of the company the current session is signed on to. |
| `EnforceAppVersion` | Gets/sets whether the session checks and enforces application version when opening database links. |
| `Errors` | Gets the Errors object which contains a list of errors stored in the session. |
| `HelpPath` | Gets/sets the path and file name to the help file of the current application. |
| `HelpURL` | Gets the location where application help files could be found. |
| `IsOpened` | Indicates whether the session is opened. An opened session represents an authenticated session with ACCPAC System Manager. |
| `IsRemote` | Indicates whether the application is accessing an out-of-process ACCPAC server. |
| `IsServerMachine` | Indicates whether the application is running on the same machine as the web-deployed ACCPAC server. |
| `ManagedClient` | Gets/sets whether the caller of this object is a managed (.NET) application. |
| `MsgrInstalled` | Gets whether or not ACCPAC Messenger is installed. |
| `Multiuser` | Gets the Multiuser object that contains methods for controlling multi-user access. |
| `Organizations` | Gets the Organizations object which contains a list of organizations set up in the system. |
| `Product` | Gets the product series of the current ACCPAC installation. |
| `ProgramName` | Gets the program name (Roto ID) of the current application. This is the program name used to initialize the session. |
| `SessionDate` | Gets the date represented by the session. |
| `StatusCSActivated` | Indicates whether the most current version of Common Services is activated for the current company. |
| `StatusHomeCurrencyExists` | Indicates whether the home currency code set up for the company exists in Common Services' currency table. |
| `StatusRemindersExist` | Indicates whether there are active reminders for the current user. |
| `StatusRestartRecsExist` | Indicates whether the company database contains restart records. |
| `StatusSessionDateInFiscal` | Indicates whether the session date falls in a valid fiscal year set up in the Fiscal Calendar. |
| `StatusSessionPeriodOpen` | Indicates whether the fiscal period the session date belongs to is open (not locked). |
| `StatusSessionYearActive` | Indicates whether the fiscal year the session date belongs to is active. |
| `StatusUserIsAdmin` | Indicates whether the current user is the administrator. |
| `StatusWarnLockedSessionPeriod` | Indicates whether the system is configured to warn the user if the fiscal period the session date belongs to is locked. |
| `SystemHelpURL` | Gets the location where System Manager help files could be found. |
| `UserID` | Gets the ACCPAC user ID of the session. |
| `UserLanguage` | Gets the language preference of the current user. The property returns the 3-letter language code of the preferred language. |

### Methods

| Name | Description |
|---|---|
| `ActivateASCS` | Activates AS and CS applications (without user interaction) |
| `Clone` | Clones the Session object. This method creates a new Session object with the same authentication information, but on a different database ID. |
| `CreateObjectHandle` | Creates an object handle with the intent of launching an application screen. An object handle is a means of propagating authentication information, and optionally application data to a screen being launched. |
| `CreateObjectHandle3` | Reserved for ACCPAC internal use only. |
| `CreateProfile` | Creates a UI Customization Profile in Administrative Services. |
| `CreateUserToken` | Reserved for ACCPAC internal use only. |
| `DeleteUserToken` | Reserved for ACCPAC internal use only. |
| `Dispose` | Closes the session and releases the resources used by the object. |
| `DoesPWExpireToday` | Allows caller to check if user's password expires today, or sometime in the next two weeks |
| `GetAccpacUserID` | Returns the ACCPAC User ID given the Windows Domain and Windows User ID. |
| `GetASVersion` | Gets Current SM Database Version |
| `GetCurrency` | Retrieves details of the specified currency code, and returns a Currency object that represents the currency. |
| `GetCurrencyRate` | Retrieves the exchange rate between the specified currency codes. |
| `GetCurrencyRateComposite` | Retrieves the composite exchange rate between the specified currency codes. |
| `GetCurrencyRateFloating` | Retrieves the floating exchange rate between the specified currency codes. |
| `GetCurrencyRateTypeDescription` | Retrieves the description of a given rate type code. |
| `GetCurrencyTable` | Retrieves details of a currency table set up in Common Services. |
| `GetDateFileLastModified` | Determines the last time the given file on the server was modified. |
| `GetDependencies` | Reserved for ACCPAC internal use only. |
| `GetFlagData` | This is private |
| `GetIniFileKey` | Retrieves configuration information from an application initialization (INI) file. |
| `GetInstalledReports` | Retrieves a list of reports installed in the system for the supplied application ID. |
| `GetLegacyReturnCode` | Gets the return code given to legacy ACCPAC applications. |
| `GetMacroData` | Returns macro data |
| `GetMeter` | Obtains a Meter object that provides access to progress information of long server processes. The object is provided mainly for ACCPAC controls to display progress. Application programs do not normally need to access this object directly. |
| `GetMinimumPasswordLength` | Returns the minimum password length, useful information when changing the password |
| `GetObjectCLSID` | Retrieves the COM class ID (CLSID) and codebase of the specified object. |
| `GetObjectKey` | Retrieves the object key, or application specific data supplied by the caller or application that launched the current object. The caller or parent application typically sets the data during the call to CreateObjectHandle. |
| `GetPrintSetup` | Obtains a PrintSetup object that allows applications to control default printer settings. |
| `GetProfileCustomizations` | Retrieves the UI Customization settings of the supplied profile ID and screen identifier (uiKey). |
| `GetProfiles` | Retrieves a list of all UI Customization Profiles set up in Administrative Services. |
| `GetSessionIntDBLink` | Reserved for ACCPAC internal use only. |
| `GetStatusString` | This is private |
| `GetUserCustomizations` | Retreives the effective UI customization settings of the current user on the UI identified by the supplied UI key. |
| `Init` | Initializes a session with System Manager and optionally opens the session as well if a valid object handle was specified. A Session object must first be initialized before any other methods in the object can be called. |
| `InternalDownload` | Reserved for ACCPAC internal use only. |
| `InternalUpload` | Reserved for ACCPAC internal use only. |
| `LicenseStatus` | Determines whether a valid license is installed for an application. |
| `MacroPause` | Pauses macro recording for the current session. |
| `MacroRecordObject` | Registers an object as being available for macro recording. |
| `MacroResume` | Resumes macro recording for the current session. |
| `Open` | Opens a session to ACCPAC System Manager by supplying an ACCPAC user ID and password. The session must be opened before other methods in the object become available. |
| `OpenDBLink` | Creates a database link to the specified database. A database link can be created on the company database, or the system database the signed-on company is attached to. |
| `OpenWin` | Opens a session to ACCPAC System Manager by supplying a Windows domain, user ID and password. If the domain and windows user parameters are blank, the currently logged in user will be used. The session must be opened before other methods in the object become available. |
| `OpenWithToken` | Reserved for ACCPAC internal use only. |
| `PropertyClear` | Removes a property from the user-specific property file. |
| `PropertyGet` | Retrieves a property stored in the user-specific property file. |
| `PropertyPut` | Stores a property into the property file. The session's application ID and version will be used to identify the property. |
| `RemoteConnect` | Instructs the Session object to connect to a remote ACCPAC .NET server using .NET Remoting. |
| `ReportSelect` | Creates a Report object that represents an ACCPAC report. |
| `RscGetString` | Retrieves a string from an application resource file. |
| `SaveProfileCustomizations` | Saves the UI customization profile settings. |
| `SessionMacroAppend` | Appends a line to a macro (and automatically adds the linefeed to the line). Will NOT generate an OpenView call. |
| `SetFlagData` | This is private |
| `SetLegacyReturnCode` | Sets the return code to legacy applications when the current program closes. This return code will be passed back to the program that launched the current application through direct Roto calls, and expects a return code in the Roto's UserArea structure. Refer to ACCPAC SDK Programming Guide for details. |
| `SetPW` | Changes password for the specified user. |
| `SetPWWithErrorCode` | Changes password for the specified user. Return error code |
| `SetStatusString` | This is private |

### Method details

#### Session.ActivateASCS

```csharp
public void ActivateASCS()
```

#### Session.Clone

```csharp
public Session Clone(
    string orgID
    )
```

- `orgID` (String) — The organization (database) ID the new session should attach to.

**Returns:** Returns the cloned Session object.

#### Session.CreateObjectHandle

```csharp
public void CreateObjectHandle(
    string objectID,
    string objectKey,
    out string objectHandle,
    out string clsid,
    out string codebase
    )
```

- `objectID` (String) — The Roto ID of the object to be launched.
- `objectKey` (String) — Application data to pass to the launched object. The key is accepted as a string. If multiple data items are required to pass to the callee, the string could be formatted in a way understood by both the caller and callee.
- `objectHandle` (String %) — Returns the newly created object handle.
- `clsid` (String %) — Returns the COM class ID (CLSID) of the object.
- `codebase` (String %) — Returns the codebase of the object where it could be found. If the session is local, the codebase is the file path to the locally installed COM object. If the session is accessing a remote ACCPAC server, the codebase is the URL where the object's CAB file could be downloaded.

This method creates an object handle, but does not launch the application identified by the Roto ID. The caller is responsible for launching the desired object in an appropriate way, passing along the object handle which can be used by that object to initialize and open its own session.

#### Session.CreateObjectHandle3

```csharp
public void CreateObjectHandle3(
    string objectID,
    string objectKey,
    string sExtra,
    out string objectHandle,
    out string clsid,
    out string codebase
    )
```

- `objectID` (String) — Reserved for ACCPAC internal use only.
- `objectKey` (String) — Reserved for ACCPAC internal use only.
- `sExtra` (String) — Reserved for ACCPAC internal use only.
- `objectHandle` (String %) — Reserved for ACCPAC internal use only.
- `clsid` (String %) — Reserved for ACCPAC internal use only.
- `codebase` (String %) — Reserved for ACCPAC internal use only.

#### Session.CreateProfile

```csharp
[ObsoleteAttribute("Use the DBLink's CreateProfile method instead.")]
    public void CreateProfile(
    string profileID,
    string profileDesc
    )
```

- `profileID` (String) — Profile ID of the profile.
- `profileDesc` (String) — Description of the profile.

If possible, use CreateProfile(String, String) instead.

#### Session.CreateUserToken

```csharp
public void CreateUserToken(
    int timeout,
    out string pUserToken
    )
```

- `timeout` (Int32) — Reserved for ACCPAC internal use only.
- `pUserToken` (String %) — Reserved for ACCPAC internal use only.

#### Session.DeleteUserToken

```csharp
public void DeleteUserToken(
    string UserToken
    )
```

- `UserToken` (String) — Reserved for ACCPAC internal use only.

#### Session.Dispose

```csharp
public void Dispose()
```

Disposing the Session object closes the session to System Manager. All resources held by the object will be freed. This also releases all Lanpak and resource locks by the session.

#### Session.DoesPWExpireToday

```csharp
public void DoesPWExpireToday(
    string userID,
    string PW,
    out bool ExpiresToday,
    out bool ExpiresInTwoWeeks,
    out int DaysLeft
    )
```

- `userID` (String) — An ACCPAC user name.
- `PW` (String) — Existing password of the user.
- `ExpiresToday` (Boolean %) — Returns if it expires sometime today.
- `ExpiresInTwoWeeks` (Boolean %) — Returns if it expires sometime in the next two weeks.
- `DaysLeft` (Int32 %) — Returns the number of days left before the password expires.

#### Session.GetAccpacUserID

```csharp
public void GetAccpacUserID(
    string Domain,
    string WinUserID,
    out string AccpacUserID
    )
```

- `Domain` (String) — Windows Domain.
- `WinUserID` (String) — Windows User ID.
- `AccpacUserID` (String %) — Returns the ACCPAC User ID that corresponds to the Windows User ID for that Windows Domain.

#### Session.GetASVersion

```csharp
public void GetASVersion(
    out string Version
    )
```

- `Version` (String %) — Output string in form of "54A".

#### Session.GetCurrency

```csharp
[ObsoleteAttribute("Use the DBLink's GetCurrency method instead.")]
    public Currency GetCurrency(
    string currencyCode
    )
```

- `currencyCode` (String) — Currency code to retrieve.

**Returns:** Returns a Currency object that represents the currency.

If possible, use GetCurrency(String) instead.

#### Session.GetCurrencyRate

```csharp
[ObsoleteAttribute("Use the DBLink's GetCurrencyRate method instead.")]
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

If possible, use GetCurrencyRate(String, String, String, DateTime) instead.

#### Session.GetCurrencyRateComposite

```csharp
[ObsoleteAttribute("Use the DBLink's GetCurrencyRateComposite method instead.")]
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

If possible, use GetCurrencyRateComposite(String, String, String, DateTime) instead.

#### Session.GetCurrencyRateFloating

```csharp
[ObsoleteAttribute("Use the DBLink's GetCurrencyRateFloating method instead.")]
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

If possible, use GetCurrencyRateFloating(String, String, String, DateTime) instead.

#### Session.GetCurrencyRateTypeDescription

```csharp
[ObsoleteAttribute("Use the DBLink's GetCurrencyRateTypeDescription method instead.")]
    public bool GetCurrencyRateTypeDescription(
    string rateType,
    out string rateTypeDescription
    )
```

- `rateType` (String) — Rate type code.
- `rateTypeDescription` (String %) — Returns the description of the supplied rate type code.

**Returns:** Returns whether the specified rate type code is found.

If possible, use GetCurrencyRateTypeDescription(String, String % ) instead.

#### Session.GetCurrencyTable

```csharp
[ObsoleteAttribute("Use the DBLink's GetCurrencyTable method instead.")]
    public CurrencyTable GetCurrencyTable(
    string currencyCode,
    string rateType
    )
```

- `currencyCode` (String) — Currency code.
- `rateType` (String) — Currency rate type code.

**Returns:** Returns a CurrencyTable object that contains details of the currency table.

If possible, use GetCurrencyTable(String, String) instead.

#### Session.GetDateFileLastModified

```csharp
public DateTime GetDateFileLastModified(
    string strFileName
    )
```

- `strFileName` (String) — The DOS path the file. The path is on the server.

**Returns:** Returns the last date and time that the given file on the server was modified.

#### Session.GetDependencies

```csharp
public void GetDependencies(
    string appID,
    string pgmName,
    string appVersion,
    string language,
    short codebaseType,
    out string[] clsids,
    out string[] codebases
    )
```

- `appID` (String)
- `pgmName` (String)
- `appVersion` (String)
- `language` (String)
- `codebaseType` (Int16)
- `clsids` (String[] %)
- `codebases` (String[] %)

#### Session.GetFlagData

```csharp
public void GetFlagData(
    int lDataSize,
    int lNum,
    byte[] DataIn,
    out byte[] DataOut
    )
```

- `lDataSize` (Int32)
- `lNum` (Int32)
- `DataIn` (Byte[])
- `DataOut` (Byte[] %)

#### Session.GetIniFileKey

```csharp
public bool GetIniFileKey(
    string appID,
    string primaryKey,
    string secondaryKey,
    out string keyData
    )
```

- `appID` (String) — Application ID
- `primaryKey` (String) — Primary key of the configuration information. This corresponds to the section name in an INI file.
- `secondaryKey` (String) — Secondary key of the configuration information. This corresponds to the value name within the specified section.
- `keyData` (String %) — Returns the configuration information stored in the INI file.

**Returns:** Returns whether the specified primary and secondary keys are found in the file.

#### Session.GetInstalledReports

```csharp
public string[] GetInstalledReports(
    string appID
    )
```

- `appID` (String) — Application ID.

**Returns:** Returns an array of report names installed in the system. Note that the report names do not include file paths.

This method only accepts the application ID, but not the version. The version of the application is automatically determined by the one activated for the current company.

#### Session.GetLegacyReturnCode

```csharp
public void GetLegacyReturnCode(
    out short pReturnCode
    )
```

- `pReturnCode` (Int16 %) — Returns the return code given to legacy ACCPAC applications.

#### Session.GetMacroData

```csharp
public int GetMacroData()
```

#### Session.GetMeter

```csharp
public Meter GetMeter()
```

**Returns:** Returns a Meter object attached to the current session.

#### Session.GetMinimumPasswordLength

```csharp
public int GetMinimumPasswordLength()
```

#### Session.GetObjectCLSID

```csharp
public bool GetObjectCLSID(
    string objectID,
    int reserved,
    out string clsid,
    out string codebase
    )
```

- `objectID` (String) — Roto ID of the object.
- `reserved` (Int32) — Reserved. Must be 0.
- `clsid` (String %) — Returns the class ID (CLSID) of the object.
- `codebase` (String %) — Returns the codebase of the object where it could be found or downloaded. If the session is local, the codebase is the file path to the locally installed COM object. If the session is accessing a remote ACCPAC server, the codebase is the URL where the object's CAB file could be downloaded.

**Returns:** Returns whether the specified object ID is valid.

This method locates the CLSID of the specified object in the application's Roto file. It does not relate to any registered COM object on the machine.

#### Session.GetObjectKey

```csharp
public string GetObjectKey()
```

**Returns:** Returns the object key set by the parent application. Returns empty if the object key was not set.

#### Session.GetPrintSetup

```csharp
public PrintSetup GetPrintSetup(
    string programID,
    string menuID
    )
```

- `programID` (String) — Roto ID of the application. The PrintSetup object uses this together with the menu ID to locate default printer settings saved in the properties file.
- `menuID` (String) — Menu ID used to identify the property. Menu IDs are assigned by the system and applications do not have control over the menu ID. If a specific menu ID is not known, an application should pass in the same as the object ID or "", in which cases, the Session object will use the system assigned menu ID.

**Returns:** Returns the PrintSetup object.

This function is not available if the current session accesses a remote ACCPAC server.

#### Session.GetProfileCustomizations

```csharp
[ObsoleteAttribute("Use the DBLink's GetProfileCustomizations method instead.")]
    public string[] GetProfileCustomizations(
    string profileID,
    string uiKey
    )
```

- `profileID` (String) — Profile ID.
- `uiKey` (String) — A key that identifies a particular UI. UI keys are individually defined by each UI.

**Returns:** Returns an array of customization settings. Returns an empty array if there is no customization settings stored for the supplied profile ID and UI key.

This method is available only if the current user is the administrator.

#### Session.GetProfiles

```csharp
[ObsoleteAttribute("Use the DBLink's GetProfiles method instead.")]
    public void GetProfiles(
    out string[] profileIDs,
    out string[] profileDescs
    )
```

- `profileIDs` (String[] %) — Returns an array of profile IDs.
- `profileDescs` (String[] %) — Returns an array of profile descriptions. Any item in this array corresponds to the item in the profileIDs array with the same position.

This method is available only if the current user is the administrator.

#### Session.GetSessionIntDBLink

```csharp
public DBLink GetSessionIntDBLink(
    DBLinkType type,
    DBLinkFlags flags
    )
```

- `type` (DBLinkType) — Reserved for ACCPAC internal use only.
- `flags` (DBLinkFlags) — Reserved for ACCPAC internal use only.

#### Session.GetStatusString

```csharp
public void GetStatusString(
    int lDataSize,
    int lNum,
    byte[] data,
    out string DataOut
    )
```

- `lDataSize` (Int32) — Data size
- `lNum` (Int32) — Number
- `data` (Byte[]) — Data in.
- `DataOut` (String %) — Output

#### Session.GetUserCustomizations

```csharp
[ObsoleteAttribute("Use the DBLink's GetUserCustomizations method instead.")]
    public string[] GetUserCustomizations(
    string uiKey
    )
```

- `uiKey` (String) — UI key identifying a UI.

**Returns:** Returns an array of customization settings. Returns an empty array if there is no customization settings effective for the current user.

If possible, use GetUserCustomizations(String) instead.

#### Session.Init

```csharp
public bool Init(
    string objectHandle,
    string appID,
    string programName,
    string appVersion
    )
```

- `objectHandle` (String) — An object handle, if available. If not, an empty string should be supplied. The object handle is given out by other System Manager routines and allows sessions to be opened without supplying the username and password. It is usually available if the application is launched by the ACCPAC desktop, or by another ACCPAC application.
- `appID` (String) — Application ID or prefix, in the form of XX, such as "AR". If the caller is not a registered ACCPAC module, use "XZ" which is reserved for macros and applications that do not have an ACCPAC registered module prefix.
- `programName` (String) — Program name, which is the Roto ID of the application. The program name should be in the form XXNNNN where XX is the application ID and NNNN is a number. If the caller is not a registered ACCPAC module, NNNN can be any number, such as "XZ1000".
- `appVersion` (String) — Application version, in the form NNX. E.g. "51A" is a valid version number.

**Returns:** Returns whether the session is also opened after initialization. If the session was not opened by supplying a valid object handle, Open must be called to open the session before other methods in the Session object become available.

#### Session.InternalDownload

```csharp
public void InternalDownload(
    int key,
    int root,
    string subPath,
    out string filename,
    out byte[] data,
    out bool moreFile,
    out bool moreData
    )
```

- `key` (Int32)
- `root` (Int32)
- `subPath` (String)
- `filename` (String %)
- `data` (Byte[] %)
- `moreFile` (Boolean %)
- `moreData` (Boolean %)

#### Session.InternalUpload

```csharp
public void InternalUpload(
    int key,
    string filename,
    int root,
    string subDir,
    byte[] data,
    bool more
    )
```

- `key` (Int32)
- `filename` (String)
- `root` (Int32)
- `subDir` (String)
- `data` (Byte[])
- `more` (Boolean)

#### Session.LicenseStatus

```csharp
public LicenseStatus LicenseStatus(
    string appID,
    string appVersion
    )
```

- `appID` (String) — Application ID
- `appVersion` (String) — Application version.

**Returns:** Returns the status of the license for the supplied applcation ID and version.

#### Session.MacroPause

```csharp
public void MacroPause()
```

#### Session.MacroRecordObject

```csharp
public void MacroRecordObject(
    int hwnd,
    string objectName
    )
```

- `hwnd` (Int32) — Windows handle of the caller.
- `objectName` (String) — Roto ID of the object.

#### Session.MacroResume

```csharp
public void MacroResume()
```

#### Session.Open

```csharp
public void Open(
    string userID,
    string password,
    string companyID,
    DateTime sessionDate,
    int flags
    )
```

- `userID` (String) — An ACCPAC user ID.
- `password` (String) — Password of the user. This parameters is ignored if security is not enabled for the intended company database.
- `companyID` (String) — Company database ID to use for this session. The company database ID must be a valid ID set up in ACCPAC.
- `sessionDate` (DateTime) — Date to use for this session.
- `flags` (Int32) — Reserved. Must be 0.

#### Session.OpenDBLink

```csharp
public DBLink OpenDBLink(
    DBLinkType type,
    DBLinkFlags flags
    )
```

- `type` (DBLinkType) — Specifies the type of database link to create.
- `flags` (DBLinkFlags) — Specifies the type of access intended on the database link.

**Returns:** Returns a DBLink object that represents the database link.

#### Session.OpenWin

```csharp
public void OpenWin(
    string domain,
    string winUserID,
    string password,
    string companyID,
    DateTime sessionDate,
    int flags
    )
```

- `domain` (String) — The Windows domain.
- `winUserID` (String) — An Windows user ID.
- `password` (String) — Windows Domain Password of the user. This parameters is ignored if security is not enabled for the intended company database.
- `companyID` (String) — Company database ID to use for this session. The company database ID must be a valid ID set up in ACCPAC.
- `sessionDate` (DateTime) — Date to use for this session.
- `flags` (Int32) — Reserved. Must be 0.

#### Session.OpenWithToken

```csharp
public void OpenWithToken(
    string userToken,
    DateTime sessionDate,
    int flags
    )
```

- `userToken` (String) — Reserved for ACCPAC internal use only.
- `sessionDate` (DateTime) — Reserved for ACCPAC internal use only.
- `flags` (Int32) — Reserved for ACCPAC internal use only.

#### Session.PropertyClear

```csharp
public void PropertyClear(
    string objectID,
    string menuID,
    string keyword,
    out int status
    )
```

- `objectID` (String) — Object ID used to identify the property. This is normally the Roto ID of the application object.
- `menuID` (String) — Menu ID used to identify the property. Menu IDs are assigned by the system and applications do not have control over the menu ID. If a specific menu ID is not known, an application should pass in the same as the object ID or "", in which cases, the Session object will use the system assigned menu ID.
- `keyword` (String) — Keyword used to identify the property.
- `status` (Int32 %) — Returns the status code of the call. 0 means the property was retrieved successfully. Any other values indicate an error retrieving the property.

```csharp
public void PropertyClear(
    string objectID,
    string menuID,
    string keyword,
    string appID,
    string appVersion,
    out int status
    )
```

- `objectID` (String) — Object ID used to identify the property. This is normally the Roto ID of the application object.
- `menuID` (String) — Menu ID used to identify the property. Menu IDs are assigned by the system and applications do not have control over the menu ID. If a specific menu ID is not known, an application should pass in the same as the object ID or "", in which cases, the Session object will use the system assigned menu ID.
- `keyword` (String) — Keyword used to identify the property.
- `appID` (String) — Application ID used to identify the property.
- `appVersion` (String) — Application version used to identify the property.
- `status` (Int32 %) — Returns the status code of the call. 0 means the property was retrieved successfully. Any other values indicate an error retrieving the property.

#### Session.PropertyGet

```csharp
public Object PropertyGet(
    string objectID,
    string menuID,
    string keyword,
    PropertyType type,
    out int status
    )
```

- `objectID` (String) — Object ID used to identify the property. This is normally the Roto ID of the application object.
- `menuID` (String) — Menu ID used to identify the property. Menu IDs are assigned by the system and applications do not have control over the menu ID. If a specific menu ID is not known, an application should pass in the same as the object ID or "", in which cases, the Session object will use the system assigned menu ID.
- `keyword` (String) — Keyword used to identify the property.
- `type` (PropertyType) — Indicates the data type which the property data should be returned.
- `status` (Int32 %) — Returns the status code of the call. 0 means the property was retrieved successfully. Any other values indicate an error retrieving the property.

**Returns:** Returns the property stored. Returns null if the property could not be found.

```csharp
public Object PropertyGet(
    string objectID,
    string menuID,
    string keyword,
    string appID,
    string appVersion,
    PropertyType type,
    out int status
    )
```

- `objectID` (String) — Object ID used to identify the property. This is normally the Roto ID of the application object.
- `menuID` (String) — Menu ID used to identify the property. Menu IDs are assigned by the system and applications do not have control over the menu ID. If a specific menu ID is not known, an application should pass in the same as the object ID or "", in which cases, the Session object will use the system assigned menu ID.
- `keyword` (String) — Keyword used to identify the property.
- `appID` (String) — Application ID used to identify the property.
- `appVersion` (String) — Application version used to identify the property.
- `type` (PropertyType) — Indicates the data type which the property data should be returned.
- `status` (Int32 %) — Returns the status code of the call. 0 means the property was retrieved successfully. Any other values indicate an error retrieving the property.

**Returns:** Returns the property stored. Returns null if the property could not be found.

#### Session.PropertyPut

```csharp
public void PropertyPut(
    string objectID,
    string menuID,
    string keyword,
    Object propertyValue,
    out int status
    )
```

- `objectID` (String) — Object ID used to identify the property. This is normally the Roto ID of the application object.
- `menuID` (String) — Menu ID used to identify the property. Menu IDs are assigned by the system and applications do not have control over the menu ID. If a specific menu ID is not known, an application should pass in the same as the object ID or "", in which cases, the Session object will use the system assigned menu ID.
- `keyword` (String) — Keyword used to identify the property.
- `propertyValue` (Object) — The property value to be stored. The value must be a string, or an array of System.Byte type.
- `status` (Int32 %) — Returns the status code of the call. 0 means the property was retrieved successfully. Any other values indicate an error retrieving the property.

```csharp
public void PropertyPut(
    string objectID,
    string menuID,
    string keyword,
    string appID,
    string appVersion,
    Object propertyValue,
    out int status
    )
```

- `objectID` (String) — Object ID used to identify the property. This is normally the Roto ID of the application object.
- `menuID` (String) — Menu ID used to identify the property. Menu IDs are assigned by the system and applications do not have control over the menu ID. If a specific menu ID is not known, an application should pass in the same as the object ID or "", in which cases, the Session object will use the system assigned menu ID.
- `keyword` (String) — Keyword used to identify the property.
- `appID` (String) — Application ID used to identify the property.
- `appVersion` (String) — Application version used to identify the property.
- `propertyValue` (Object) — The property value to be stored. The value must be a string, or an array of System.Byte type.
- `status` (Int32 %) — Returns the status code of the call. 0 means the property was retrieved successfully. Any other values indicate an error retrieving the property.

#### Session.RemoteConnect

```csharp
public void RemoteConnect(
    string hostname,
    string username,
    string domain,
    string password
    )
```

- `hostname` (String) — Host name of the ACCPAC server, and the port number to connect to. This parameter should be in the form hostname : portnumber . The host name can be a fully qualified host name or the IP address of the server. A Windows machine name can also be used if the server is within the same intranet.
- `username` (String) — Username to logon on to the server. If enhanced security is configured on the server, the ACCPAC remoting architecture uses NT authentication to verify access rights of the supplied user. The user must be a user recognized on the server. This parameter is ignored if enhanced security is turned off on the server.
- `domain` (String) — Domain the supplied user name belongs to. This should be the Windows domain name of the user, or the server's machine name if the user is a local user on the server. This parameter is ignored if enhanced security is turned off on the server.
- `password` (String) — Password of the user. This parameter is ignored if enhanced security is turned off on the server.

```csharp
public void RemoteConnect(
    Session.Session..::RemoteConnectProtocol protocol,
    string hostname,
    int port,
    string username,
    string domain,
    string password
    )
```

- `protocol` (Session . . :: RemoteConnectProtocol) — The protocol to use for remoting. TCP is the only supported protocol for this version.
- `hostname` (String) — Host name of the ACCPAC server. The host name can be a fully qualified host name or the IP address of the server. A Windows machine name can also be used if the server is within the same intranet.
- `port` (Int32) — The port number to connect to on the ACCPAC server. This port number should be the one which the ACCPAC Remoting Manager on the server is configured to listen to.
- `username` (String) — Username to logon on to the server. If enhanced security is configured on the server, the ACCPAC remoting architecture uses NT authentication to verify access rights of the supplied user. The user must be a user recognized on the server. This parameter is ignored if enhanced security is turned off on the server.
- `domain` (String) — Domain the supplied user name belongs to. This should be the Windows domain name of the user, or the server's machine name if the user is a local user on the server. This parameter is ignored if enhanced security is turned off on the server.
- `password` (String) — Password of the user. This parameter is ignored if enhanced security is turned off on the server.

#### Session.ReportSelect

```csharp
public Report ReportSelect(
    string reportName,
    string programID,
    string menuID
    )
```

- `reportName` (String) — Name of the report.
- `programID` (String) — Roto ID of the application. The Report object uses this together with the menu ID to locate default report settings saved in the properties file.
- `menuID` (String) — Menu ID used to identify the property. Menu IDs are assigned by the system and applications do not have control over the menu ID. If a specific menu ID is not known, an application should pass in the same as the object ID or "", in which cases, the Session object will use the system assigned menu ID.

**Returns:** Returns a Report object that represents the specified report.

#### Session.RscGetString

```csharp
public string RscGetString(
    string appID,
    int rscID
    )
```

- `appID` (String) — Application ID of the resource file to retrieve the string.
- `rscID` (Int32) — The resource ID of the string.

**Returns:** Returns the string retrieved from the resource file. Returns an empty string if the resource ID could not be found in the resource file, or if the specified application ID was not an activated application on the current company.

This function only requires the application ID. The application version is determined by the activated version of the specified application on the current company.

#### Session.SaveProfileCustomizations

```csharp
[ObsoleteAttribute("Use the DBLink's SaveProfileCustomizations method instead.")]
    public void SaveProfileCustomizations(
    string[] profileIDs,
    string uiKey,
    string[] hiddenControls
    )
```

- `profileIDs` (String[]) — Profile ID.
- `uiKey` (String) — A key that identifies UI.
- `hiddenControls` (String[]) — An array of control names that should be hidden.

This method is available only if the current user is the administrator.

#### Session.SessionMacroAppend

```csharp
public void SessionMacroAppend(
    string cmdInString
    )
```

- `cmdInString` (String) — The line to append.

#### Session.SetFlagData

```csharp
public void SetFlagData(
    int lDataSize,
    int lNum,
    byte[] DataIn,
    out byte[] DataOut
    )
```

- `lDataSize` (Int32)
- `lNum` (Int32)
- `DataIn` (Byte[])
- `DataOut` (Byte[] %)

#### Session.SetLegacyReturnCode

```csharp
public void SetLegacyReturnCode(
    short returnCode
    )
```

- `returnCode` (Int16) — Code to return to legacy applications.

#### Session.SetPW

```csharp
public bool SetPW(
    string userID,
    string oldPW,
    string newPW
    )
```

- `userID` (String) — An ACCPAC user name.
- `oldPW` (String) — Existing password of the user.
- `newPW` (String) — The new password.

**Returns:** Returns whether the password of the user was successfully set.

#### Session.SetPWWithErrorCode

```csharp
public int SetPWWithErrorCode(
    string userID,
    string oldPW,
    string newPW,
    out bool bChanged
    )
```

- `userID` (String) — An ACCPAC user name.
- `oldPW` (String) — Existing password of the user.
- `newPW` (String) — The new password.
- `bChanged` (Boolean %) — Returns whether the password of the user was successfully set.

**Returns:** An extended error code .

#### Session.SetStatusString

```csharp
public void SetStatusString(
    int lDataSize,
    int lNum,
    string DataIn,
    out byte[] DataOut
    )
```

- `lDataSize` (Int32)
- `lNum` (Int32)
- `DataIn` (String)
- `DataOut` (Byte[] %)


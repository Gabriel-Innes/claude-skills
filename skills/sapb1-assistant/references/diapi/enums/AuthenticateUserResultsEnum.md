<!-- source: REFDI.chm, SAP Business One DI API 10.0 (10.00.190) | version: DI API 10.0 | verified: 2026-10-01 -->
# AuthenticateUserResultsEnum (Enumeration)

The check results of the username and password.

| Member | Value | Description |
|---|---|---|
| aturNotConnectedToCompany | -8033 | Not connected to the SAP Business One company. |
| aturUsernamePasswordMatch | 0 | The username and the password matches. |
| aturLogOnUserNotAdmin | -8031 | The logon user is not a superuser. |
| aturBadUserOrPassword | -8023 | The username and the password do not match, or the username does not exist. |
| aturUserHasBeenLocked | -8024 | The username is locked. |
| aturPasswordExpired | -8025 | The password is expired. |
| aturDBErrors | -8032 | Run time error when you access the database. |
| aturWrongDomainName | -8034 |  |

<!-- source: REFDI.chm, SAP Business One DI API 10.0 (10.00.190) | version: DI API 10.0 | verified: 2026-10-01 -->
# UserMenuService (Object)

UserMenuService manages the user menu. Source table: CUMI. The service maintains a collection of user menus, each identified by a specific value of UserMenuParams. It enables the user to: - Get current user menu definition. - Get any user menu definition from the collection by it params identification key. - Update user menus in the collection. - Replace current user menu with user menu from the collection.

**Remarks:** To use the service: - Connect to a valid company. - Call the CompanyService, which is the main DI service that you must call before using any other service. - Call the method GetBusinessService for the required service. - Create an empty data structure related to the required service. - or- You can create a data structure from an XML file or XML string. - Set the required properties of the specified data structure. - Call the required service method. To display the form in the application: - Select Main Menu--User Menu Tab

## Methods (7)
- `Public Function GetCurrentUserMenu() As UserMenuItems` Get the UserMenuItems data collection that represents current user menu.
  - example note: Get the current user menu
  - VB example (SAP provides no C# sample for this - translate, don't paste):
    ```vb
    Dim oUserMenuItems As UserMenuItems

    Dim oUserMenuItem As UserMenuItem

    'get Current User Menu

    oUserMenuItems = oUserMenuService.GetCurrentUserMenu()

    'Get the first menu item

    oUserMenuItem = oUserMenuItems.Item(0)

    'print the menu name

    Debug.WriteLine(oUserMenuItem.Name())
    ```
- `Public Function GetDataInterface(ByVal enumMSDI As UserMenuServiceDataInterfaces) As Object` Creates an empty data structure. This means the structure contains the default setting/values of the database.
  - param `enumMSDI`: one of the enumeration's values (see the enum file)
  - enum: `../enums/UserMenuServiceDataInterfaces.md`
- `Public Function GetDataInterfaceFromXMLFile(ByVal bstrFileName As String) As Object` Retrieves the Data Interface schema from XML file.
  - param `bstrFileName`: Specifies the path and file name of the XML data.
- `Public Function GetDataInterfaceFromXMLString(ByVal bstrXMLString As String) As Object` Retrieves the Data Interface schema from XML string.
  - param `bstrXMLString`: Specifies the the XML string.
- `Public Function GetUserMenu(ByVal pIUserMenuParams As UserMenuParams) As UserMenuItems` Get a User's defined menu (UserMenuItems), by its UserMenuParams identification key.
  - param `pIUserMenuParams`: User menu UserMenuParams identification key.
- `Public Sub UpdateCurrentUserMenu(ByVal pIUserMenuItems As UserMenuItems)` Replace current User Menu with another User menu (UserMenuItems).
  - param `pIUserMenuItems`: The UserMenuItems data collection that defines the new user menu.
  - example note: Update Current User Menu
  - VB example (SAP provides no C# sample for this - translate, don't paste):
    ```vb
    Dim oUserMenuItems As UserMenuItems

    Dim oUserMenuItem As UserMenuItem

    'get Current User Menu

    oUserMenuItems = oUserMenuService.GetCurrentUserMenu()

    'get the first menu item

    oUserMenuItem = oUserMenuItems.Item(0)

    'set the menu item name

    oUserMenuItem.Name = "My Forms"

    'update the User Menu

    oUserMenuService.UpdateCurrentUserMenu(oUserMenuItems)
    ```
- `Public Sub UpdateUserMenu(ByVal pIUserMenuParams As UserMenuParams, ByVal pIUserMenuItems As UserMenuItems)` Replace a User Menu definition (UserMenuItems), identified by it UserMenuParams with a new User menu definition (UserMenuItems).
  - param `pIUserMenuParams`: Identification key (UserMenuParams) of the new menu definition.
  - param `pIUserMenuItems`: The new UserMenuItems data collection that defines the new menu.
  - example note: Update the user menu of user 2(doris) with the menu of user 1 (manager)
  - VB example (SAP provides no C# sample for this - translate, don't paste):
    ```vb
    Dim oUserMenuItems As UserMenuItems

    Dim oSourceUserMenuParams As UserMenuParams

    Dim oDestUserMenuParams As UserMenuParams

    'get new User Menu Params

    oSourceUserMenuParams = oUserMenuService.GetDataInterface(UserMenuServiceDataInterfaces.umsdiUserMenuParams)

    'set the user id(manager=1)

    oSourceUserMenuParams.UserID = 1

    'get User Menu Params

    oDestUserMenuParams = oUserMenuService.GetDataInterface(UserMenuServiceDataInterfaces.umsdiUserMenuParams)

    'set the user id(doris=2)

    oDestUserMenuParams.UserID = 2

    'get Menu Items of the user 1 (manager)

    oUserMenuItems = oUserMenuService.GetUserMenu(oSourceUserMenuParams)

    'update the user menu of user 2(doris) with the menu of user 1 (manager)

    oUserMenuService.UpdateUserMenu(oDestUserMenuParams, oUserMenuItems)
    ```

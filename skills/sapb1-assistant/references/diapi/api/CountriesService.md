<!-- source: REFDI.chm, SAP Business One DI API 10.0 (10.00.190) | version: DI API 10.0 | verified: 2026-10-01 -->
# CountriesService (Object)

The CountriesService manages the setting of each country in SAP Business One. For example, country code, country name and address format. Source table: OCRY.

**Remarks:** To access countries in the application: Choose Administration > Setup > Business Partners > Countries/Regions.

**Example:**
- C# example (from SAP's help):
  ```csharp
  CompanyService cmpService = oCmpy.GetCompanyService();
  Country cty = (Country)countryService.GetDataInterface(CountriesServiceDataInterfaces.csCountry);
  cty.Code = "XP";
  cty.Name = "XP Name";
  cty.ISOAlpha2Code = "XC";
  cty.ISOAlpha3Code = "XCC";
  cty.ISONumeric = "002";
  CountryParams cp = countryService.AddCountry(cty);
  ```

## Methods (8)
- `Public Function AddCountry(ByVal pICountry As Country) As CountryParams` Adds a Country as specified in the Country data structure.
  - param `pICountry`: The data for the new country.
- `Public Sub DeleteCountry(ByVal pICountryParams As CountryParams)` Deletes the country as specified in CountryParams object.
  - param `pICountryParams`: CountryParams
- `Public Function GetCountry(ByVal pICountryParams As CountryParams) As Country` Returns an instance of the Country data structure.
  - param `pICountryParams`: CountryParams
- `Public Function GetCountryList() As CountriesParams` Returns a collection of CountryParams.
- `Public Function GetDataInterface(ByVal enumMSDI As CountriesServiceDataInterfaces) As Object` Creates empty data structure. This means the structure contains the default setting/values of the database.
  - param `enumMSDI`: one of the enumeration's values (see the enum file)
  - enum: `../enums/CountriesServiceDataInterfaces.md`
- `Public Function GetDataInterfaceFromXMLFile(ByVal bstrFileName As String) As Object` Creates data structure from specified XML file.
  - param `bstrFileName`: 
- `Public Function GetDataInterfaceFromXMLString(ByVal bstrXMLString As String) As Object` Creates data structure from specified XML string.
  - param `bstrXMLString`: 
- `Public Sub UpdateCountry(ByVal pICountry As Country)` Update the specified Country with the updated data.
  - param `pICountry`: The data for the country to be updated.

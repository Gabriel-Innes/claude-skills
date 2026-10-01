<!-- source: REFDI.chm, SAP Business One DI API 10.0 (10.00.190) | version: DI API 10.0 | verified: 2026-10-01 -->
# ElectronicReportInfo (Object)

Setup values for electronic reports.

**Remarks:** Specific to localization for France.

**Example:**
- C# example (from SAP's help):
  ```csharp
  "SAPbobsCOM.CompanyService oCmpSrv = oCompany.GetCompanyService();
  SAPbobsCOM.AdminInfo oAdminInfo = oCmpSrv.GetAdminInfo();
  oAdminInfo.ElectronicReportInfo.ShareCapitalAmount = 12.3;
  oAdminInfo.ElectronicReportInfo.CompanyType = ""BB"";
  oCmpSrv.UpdateAdminInfo(oAdminInfo);
  ```

## Properties (2)
- `Public Property CompanyType() As String` [R/W] Company type.
- `Public Property ShareCapitalAmount() As Double` [R/W] Share capital amount.

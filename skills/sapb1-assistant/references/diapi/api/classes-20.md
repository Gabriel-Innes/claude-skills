<!-- source: REFDI.chm, SAP Business One DI API 10.0 (10.00.190) | version: DI API 10.0 | verified: 2026-10-01 -->

# ProjectManagementService (Object)

This service is for project management in SAP Business One. Source table: OPMG.

**Example:**
- C# example (from SAP's help):
  ```csharp
  public int AddProject()
  {
      int absEntryOfCreatedProject = -1;

      SAPbobsCOM.CompanyService oCompServ = null;
      SAPbobsCOM.ProjectManagementService pmgService = null;

      try
      {
          // Company service
          oCompServ = (SAPbobsCOM.CompanyService)g_Company.GetCompanyService();

          // ProjectManagementService
          pmgService = (SAPbobsCOM.ProjectManagementService)oCompServ.GetBusinessService(ServiceTypes.ProjectManagementService);

          // Add project
          SAPbobsCOM.PM_ProjectDocumentData project = (SAPbobsCOM.PM_ProjectDocumentData)pmgService.GetDataInterface(ProjectManagementServiceDataInterfaces.pmsPM_ProjectDocumentData);
          project.ProjectName = "ProjectByDI_01";
          project.Owner = 1;
          project.StartDate = new DateTime(2016, 2, 1);
          project.DueDate = new DateTime(2016, 11, 30);
          project.ClosingDate = new DateTime(2016, 12, 31);
          project.ProjectType = ProjectTypeEnum.pt_External;
          project.BusinessPartner = "Customer_01";
          project.BusinessPartnerName = "BP Name_01";
          project.ContactPerson = 2;
          project.Territory = 1;
          project.SalesEmployee = 5;
          project.AllowSubprojects = BoYesNoEnum.tYES;
          project.ProjectStatus = ProjectStatusTypeEnum.pst_Started;
          project.FinancialProject = "FinProj_01";
          project.RiskLevel = RiskLevelTypeEnum.rlt_High;
          project.Industry = 3;
          project.Reason = "Test comment";
          project.AttachmentEntry = 1;

          SAPbobsCOM.PM_ProjectDocumentParams projectParam = pmgService.AddProject(project);
          absEntryOfCreatedProject = projectParam.AbsEntry;
      }
      catch (System.Exception ex)
      {
          throw new Exception(string.Format("Call PMG failed with error code: {0}", e.Message));
      }
      finally
      {
          if (pmgService != null)
          {
              System.Runtime.InteropServices.Marshal.ReleaseComObject(pmgService);
          }
      }

      return absEntryOfCreatedProject;
  }
  ```
- C# example (from SAP's help):
  ```csharp
  public void UpdateProject()
  {
      SAPbobsCOM.CompanyService oCompServ = null;
      SAPbobsCOM.ProjectManagementService pmgService = null;

      try
      {
          oCompServ = (SAPbobsCOM.CompanyService)g_Company.GetCompanyService();

          // ProjectManagementService
          pmgService = (SAPbobsCOM.ProjectManagementService)oCompServ.GetBusinessService(ServiceTypes.ProjectManagementService);

          // Update project
          SAPbobsCOM.PM_ProjectDocumentParams projectToUpdateParam = pmgService.GetDataInterface(ProjectManagementServiceDataInterfaces.pmsPM_ProjectDocumentParams);
          projectToUpdateParam.AbsEntry = 1;
          SAPbobsCOM.PM_ProjectDocumentData project = pmgService.GetProject(projectToUpdateParam);
          project.ProjectName = project.ProjectName + " Updated";

          pmgService.UpdateProject(project);
      }
      catch (Exception e)
      {
          throw new Exception(string.Format("Call PMG failed with error code: {0}", e.Message));
      }
      finally
      {
          if (pmgService != null)
          {
              System.Runtime.InteropServices.Marshal.ReleaseComObject(pmgService);
          }
      }
  }
  ```
- C# example (from SAP's help):
  ```csharp
  public void CancelProject(int absEntry)
  {
      SAPbobsCOM.CompanyService oCompServ = null;
      SAPbobsCOM.ProjectManagementService pmgService = null;

      try
      {
          oCompServ = (SAPbobsCOM.CompanyService)g_Company.GetCompanyService();

          // ProjectManagementService
          pmgService = (SAPbobsCOM.ProjectManagementService)oCompServ.GetBusinessService(ServiceTypes.ProjectManagementService);

          // Cancel project
          SAPbobsCOM.PM_ProjectDocumentParams projectToCancelParam = pmgService.GetDataInterface(ProjectManagementServiceDataInterfaces.pmsPM_ProjectDocumentParams);
          projectToCancelParam.AbsEntry = 1;

          pmgService.CancelProject(projectToCancelParam);
      }
      catch (Exception e)
      {
          throw new Exception(string.Format("Call PMG failed with error code: {0}", e.Message));
      }
      finally
      {
          if (pmgService != null)
          {
              System.Runtime.InteropServices.Marshal.ReleaseComObject(pmgService);
          }
      }
  }
  ```
- C# example (from SAP's help):
  ```csharp
  public void AddDocumentToStage()
  {
      try
      {
          CompanyService oCompServ = (SAPbobsCOM.CompanyService)g_Company.GetCompanyService();
          ProjectManagementService pmgService = (SAPbobsCOM.ProjectManagementService)oCompServ.GetBusinessService(ServiceTypes.ProjectManagementService);

          SAPbobsCOM.PM_ProjectDocumentParams projectToUpdateParam = pmgService.GetDataInterface(ProjectManagementServiceDataInterfaces.pmsPM_ProjectDocumentParams);
          projectToUpdateParam.AbsEntry = 1;
          SAPbobsCOM.PM_ProjectDocumentData project = pmgService.GetProject(projectToUpdateParam);

          // add stage to the project
          SAPbobsCOM.PM_StagesCollection stagesCollection = project.PM_StagesCollection;
          SAPbobsCOM.PM_StageData stage = stagesCollection.Add();
          stage.StageType = 1;
          stage.StartDate = DateTime.Now;
          stage.CloseDate = stage.StartDate.AddDays(30);
          stage.Task = 1;
          stage.Description = "StageWithDocByDI_01";
          stage.ExpectedCosts = 150;
          stage.PercentualCompletness = 7;
          stage.IsFinished = BoYesNoEnum.tNO;
          stage.StageOwner = 5;
          stage.AttachmentEntry = 1;

          stage = stagesCollection.Add();
          stage.StageType = 2;
          stage.StartDate = DateTime.Now.AddMonths(1);
          stage.CloseDate = stage.StartDate.AddDays(30);
          stage.Task = 2;
          stage.Description = "StageWithDocByDI_02";
          stage.ExpectedCosts = 250;
          stage.PercentualCompletness = 8;
          stage.IsFinished = BoYesNoEnum.tNO;
          stage.StageOwner = 5;
          stage.DependsOnStage1 = 1;
          stage.StageDependency1Type = StageDepTypeEnum.sdt_Project;
          stage.DependsOnStageID1 = 1;

          // add document to the stage
          SAPbobsCOM.PM_DocumentsCollection documentsCollection = project.PM_DocumentsCollection;
          SAPbobsCOM.PM_DocumentData document = documentsCollection.Add();
          document.StageID = 1;
          document.DocType = SAPbobsCOM.PMDocumentTypeEnum.pmdt_APCreditMemo;
          document.DocEntry = 7;

          pmgService.UpdateProject(project);
          MessageBox.Show("OK");
      }
      catch (Exception e)
      {
          throw new Exception(string.Format("Call PMG failed with error code: {0}", e.Message));
      }
      finally
      {
          if (pmgService != null)
          {
              System.Runtime.InteropServices.Marshal.ReleaseComObject(pmgService);
          }
      }
  }
  ```
- C# example (from SAP's help):
  ```csharp
  public void AddSubProject()
  {
      try
      {
          CompanyService oCompServ = (SAPbobsCOM.CompanyService)g_Company.GetCompanyService();

          // ProjectManagementService
          ProjectManagementService phaService = (SAPbobsCOM.ProjectManagementService)oCompServ.GetBusinessService(ServiceTypes.ProjectManagementService);

          // Add subproject
          PM_SubprojectDocumentData subProject = phaService.GetDataInterface(ProjectManagementServiceDataInterfaces.pmsPM_SubprojectDocumentData);
          subProject.Owner = 4;
          subProject.SubprojectName = "SubProjectNameByDI_01_01";
          subProject.StartDate = new DateTime(2016, 5, 1);
          subProject.DueDate = new DateTime(2016, 5, 15);
          subProject.SubprojectEndDate = new DateTime(2016, 5, 31);
          subProject.ProjectID = 1;
          subProject.SubprojectType = 1;
          subProject.SubprojectContribution = 15;
          subProject.SubprojectStatus = SubprojectStatusTypeEnum.sst_Open;
          subProject.ActualCost = 50;
          subProject.PlannedCost = 200;

          SAPbobsCOM.PM_SubprojectDocumentParams subprojectParam = phaService.AddSubproject(subProject);
      }
      catch (Exception e)
      {
          throw new Exception(string.Format("Call PHA failed with error code: {0}", e.Message));
      }
      finally
      {
          if (pmgService != null)
          {
              System.Runtime.InteropServices.Marshal.ReleaseComObject(pmgService);
          }
      }
  }
  ```

## Methods (12)
- `Public Function AddProject(ByVal pIPM_ProjectDocumentData As PM_ProjectDocumentData) As PM_ProjectDocumentParams` AddProject
  - param `pIPM_ProjectDocumentData`: 
- `Public Function AddSubproject(ByVal pIPM_SubprojectDocumentData As PM_SubprojectDocumentData) As PM_SubprojectDocumentParams` AddSubproject
  - param `pIPM_SubprojectDocumentData`: 
- `Public Sub CancelProject(ByVal pIPM_ProjectDocumentParams As PM_ProjectDocumentParams)` CancelProject
  - param `pIPM_ProjectDocumentParams`: 
- `Public Sub DeleteSubproject(ByVal pIPM_SubprojectDocumentParams As PM_SubprojectDocumentParams)` DeleteSubproject
  - param `pIPM_SubprojectDocumentParams`: 
- `Public Function GetDataInterface(ByVal enumMSDI As ProjectManagementServiceDataInterfaces) As Object` GetDataInterface
  - param `enumMSDI`: one of the enumeration's values (see the enum file)
  - enum: `ProjectManagementServiceDataInterfaces` in `../enums/enums-03.md`
- `Public Function GetDataInterfaceFromXMLFile(ByVal bstrFileName As String) As Object` GetDataInterfaceFromXMLFile
  - param `bstrFileName`: 
- `Public Function GetDataInterfaceFromXMLString(ByVal bstrXMLString As String) As Object` GetDataInterfaceFromXMLString
  - param `bstrXMLString`: 
- `Public Function GetProject(ByVal pIPM_ProjectDocumentParams As PM_ProjectDocumentParams) As PM_ProjectDocumentData` GetProject
  - param `pIPM_ProjectDocumentParams`: 
- `Public Function GetSubproject(ByVal pIPM_SubprojectDocumentParams As PM_SubprojectDocumentParams) As PM_SubprojectDocumentData` GetSubproject
  - param `pIPM_SubprojectDocumentParams`: 
- `Public Function GetSubprojectsList(ByVal pIPM_SubprojectParams As PM_SubprojectParams) As PM_SubprojectDocumentsCollection` GetSubprojectsList
  - param `pIPM_SubprojectParams`: 
- `Public Sub UpdateProject(ByVal pIPM_ProjectDocumentData As PM_ProjectDocumentData)` UpdateProject
  - param `pIPM_ProjectDocumentData`: 
- `Public Sub UpdateSubproject(ByVal pIPM_SubprojectDocumentData As PM_SubprojectDocumentData)` UpdateSubproject
  - param `pIPM_SubprojectDocumentData`: 

# ProjectManagementTimeSheetService (Object)

ProjectManagementTimeSheetService Class

## Methods (7)
- `Public Function AddTimeSheet(ByVal pIPM_TimeSheetData As PM_TimeSheetData) As PM_TimeSheetParams` AddTimeSheet
  - param `pIPM_TimeSheetData`: 
- `Public Sub DeleteTimeSheet(ByVal pIPM_TimeSheetParams As PM_TimeSheetParams)` DeleteTimeSheet
  - param `pIPM_TimeSheetParams`: 
- `Public Function GetDataInterface(ByVal enumMSDI As ProjectManagementTimeSheetServiceDataInterfaces) As Object` GetDataInterface
  - param `enumMSDI`: one of the enumeration's values (see the enum file)
  - enum: `ProjectManagementTimeSheetServiceDataInterfaces` in `../enums/enums-03.md`
- `Public Function GetDataInterfaceFromXMLFile(ByVal bstrFileName As String) As Object` GetDataInterfaceFromXMLFile
  - param `bstrFileName`: 
- `Public Function GetDataInterfaceFromXMLString(ByVal bstrXMLString As String) As Object` GetDataInterfaceFromXMLString
  - param `bstrXMLString`: 
- `Public Function GetTimeSheet(ByVal pIPM_TimeSheetParams As PM_TimeSheetParams) As PM_TimeSheetData` GetTimeSheet
  - param `pIPM_TimeSheetParams`: 
- `Public Sub UpdateTimeSheet(ByVal pIPM_TimeSheetData As PM_TimeSheetData)` UpdateTimeSheet
  - param `pIPM_TimeSheetData`: 

# ProjectParams (Object)

This object holds identification properties for the ProjectsService object (Code and Name).

## Properties (2)
- `Public Property Code() As String` [R/W] Sets or returns a string specifying the project unique ID. Length: 20 characters.
- `Public Property Name() As String` [R] Sets or returns a string specifying the project name.

## Methods (5)
- `Public Sub FromXMLFile(ByVal bstrFileName As String)` Imports data from an XML file to the object.
  - param `bstrFileName`: Specifies the path and file name of the XML data.
- `Public Sub FromXMLString(ByVal bstrXML As String)` Imports data from an XML string to the object.
  - param `bstrXML`: Specifies the the XML string.
- `Public Function GetXMLSchema() As String` Retrieves the XML schema of the data structure.
- `Public Sub ToXMLFile(ByVal bstrFileName As String)` Creates an XML file that represents the object data.
  - param `bstrFileName`: Specifies the path and file name for the XML data.
- `Public Function ToXMLString() As String` Creates an XML string that represents the object data.

# ProjectsParams (Collection)

A data collection of ProjectParams identification properties.

## Properties (1)
- `Public Property Count() As Long` [R] Returns the number of ProjectParams instances in the collection.

## Methods (5)
- `Public Function Add() As ProjectParams` Adds a new ProjectParams to the collection.
- `Public Function GetXMLSchema() As String` Retrieves the XML schema of the data structure.
- `Public Function Item(ByVal vtIndex As Variant) As ProjectParams` Returns a ProjectParams instance by a specified index.
  - param `vtIndex`: Specifies the index of the ProjectParams instance you want to get.
- `Public Sub ToXMLFile(ByVal bstrFileName As String)` Creates an XML file that represents the object data.
  - param `bstrFileName`: Specifies the path and file name of the XML data.
- `Public Function ToXMLString() As String` Creates an XML string that represents the object data.

# ProjectsService (Object)

This service manages projects in SAP Business One. The service enables to add or delete projects, and update projects' name and code. Source table: OPRJ.

**Remarks:** To access projects in the application, choose Administration > Setup > Financials > Projects.

## Methods (8)
- `Public Function AddProject(ByVal pIProject As Project) As ProjectParams` Adds a project code and name as specified in the Project data structure.
  - param `pIProject`: Specifies the project data structure you want to add.
  - VB example (SAP provides no C# sample for this - translate, don't paste):
    ```vb
    Dim oCmpSrv As SAPbobsCOM.CompanyService

    Dim projectService As SAPbobsCOM.IProjectsService

    Dim project As SAPbobsCOM.IProject

    oCmpSrv = oCompany.GetCompanyService

    projectService = oCmpSrv.GetBusinessService(SAPbobsCOM.ServiceTypes.ProjectsService)

    project = projectService.GetDataInterface(SAPbobsCOM.ProjectsServiceDataInterfaces.psProject)

    project.Code = "1"

    project.Name = "Jeremy"

    projectService.AddProject(project)

    project.Code = "2"

    project.Name = "June"

    projectService.AddProject(project)
    ```
- `Public Sub DeleteProject(ByVal pIProjectParams As ProjectParams)` Deletes project code and name specified in ProjectParams.
  - param `pIProjectParams`: Specifies the identification properties (Code and Name) of the project you want to delete.
- `Public Function GetDataInterface(ByVal enumMSDI As ProjectsServiceDataInterfaces) As Object` Creates empty data structure. This means the structure contains the default setting/values of the database.
  - param `enumMSDI`: one of the enumeration's values (see the enum file)
  - enum: `ProjectsServiceDataInterfaces` in `../enums/enums-03.md`
- `Public Function GetDataInterfaceFromXMLFile(ByVal bstrFileName As String) As Object` Creates data structure from specified XML file.
  - param `bstrFileName`: Specifies the path and file name of the XML data.
- `Public Function GetDataInterfaceFromXMLString(ByVal bstrXMLString As String) As Object` Creates data structure from specified XML string.
  - param `bstrXMLString`: Specifies the XML string.
- `Public Function GetProject(ByVal pIProjectParams As ProjectParams) As Project` Returns an instance of the Project data structure.
  - param `pIProjectParams`: Specifies the identification properties (Code and Name) of the instance you want to get.
- `Public Function GetProjectList() As ProjectsParams` Returns a collection of instances for the Project data structure.
  - VB example (SAP provides no C# sample for this - translate, don't paste):
    ```vb
    Dim oCmpSrv As SAPbobsCOM.CompanyService

    Dim projectService As SAPbobsCOM.IProjectsService

    Dim projectParams As SAPbobsCOM.IProjectsParams

    oCmpSrv = oCompany.GetCompanyService

    projectService = oCmpSrv.GetBusinessService(SAPbobsCOM.ServiceTypes.ProjectsService)

    projectParams = projectService.GetDataInterface(SAPbobsCOM.ProjectsServiceDataInterfaces.psProjectsParams)

    projectParams = projectService.GetProjectList()

    MsgBox(projectParams.Count)

    'Projects Service

    Dim oCmpSrv As SAPbobsCOM.CompanyService

    Dim projectService As SAPbobsCOM.IProjectsService

    oCmpSrv = oCompany.GetCompanyService

    projectService = oCmpSrv.GetBusinessService(SAPbobsCOM.ServiceTypes.ProjectsService)

    Dim project As SAPbobsCOM.IProject

    Dim projectParams As SAPbobsCOM.IProjectParams

    'Add 2 projects

    project = projectService.GetDataInterface(SAPbobsCOM.ProjectsServiceDataInterfaces.psProject)

    project.Code = "PRJ1"

    project.Name = "Project A"

    projectService.AddProject(project)

    project.Code = "PRJ2"

    project.Name = "Project B"

    projectService.AddProject(project)

    'Get a project

    projectParams = projectService.GetDataInterface(SAPbobsCOM.ProjectsServiceDataInterfaces.psProjectParams)

    projectParams.Code = "PRJ11"

    project = projectService.GetProject(projectParams)

    'Update a project

    project.Name = "Updated"

    projectService.UpdateProject(project)
    ```
- `Public Sub UpdateProject(ByVal pIProject As Project)` Replaces project code and name with the specified Project data structure.
  - param `pIProject`: Specifies the code and name that will replace the current project.
  - VB example (SAP provides no C# sample for this - translate, don't paste):
    ```vb
    Dim oCmpSrv As SAPbobsCOM.CompanyService

    Dim projectService As SAPbobsCOM.IProjectsService

    Dim project As SAPbobsCOM.IProject

    Dim projectParams As SAPbobsCOM.IProjectParams

    oCmpSrv = oCompany.GetCompanyService

    projectService = oCmpSrv.GetBusinessService(SAPbobsCOM.ServiceTypes.ProjectsService)

    'Get a project

    projectParams = projectService.GetDataInterface(SAPbobsCOM.ProjectsServiceDataInterfaces.psProjectParams)

    projectParams.Code = "PRJ11"

    project = projectService.GetProject(projectParams)

    'Update the project

    project.Name = "NewProjectName"

    projectService.UpdateProject(project)
    ```

# QRCodeCollection (Collection)

QRCodeCollection Class

## Properties (1)
- `Public Property Count() As Long` [R] Count

## Methods (5)
- `Public Function Add() As QRCodeData` method Add
- `Public Function GetXMLSchema() As String` method GetXMLSchema
- `Public Function Item(ByVal vtIndex As Variant) As QRCodeData` DISPID_VALUE
  - param `vtIndex`: 
- `Public Sub ToXMLFile(ByVal bstrFileName As String)` method ToXMLFile
  - param `bstrFileName`: 
- `Public Function ToXMLString() As String` method ToXMLString

# QRCodeData (Object)

QRCodeData Class

## Properties (4)
- `Public Property FieldName() As String` [R/W] property FieldName
- `Public Property ObjectAbsEntry() As String` [R/W] property ObjectAbsEntry
- `Public Property ObjectType() As Long` [R/W] property ObjectType
- `Public Property QRCodeText() As String` [R/W] property QRCodeText

## Methods (5)
- `Public Sub FromXMLFile(ByVal bstrFileName As String)` method FromXMLFile
  - param `bstrFileName`: 
- `Public Sub FromXMLString(ByVal bstrXML As String)` method FromXMLString
  - param `bstrXML`: 
- `Public Function GetXMLSchema() As String` method GetXMLSchema
- `Public Sub ToXMLFile(ByVal bstrFileName As String)` method ToXMLFile
  - param `bstrFileName`: 
- `Public Function ToXMLString() As String` method ToXMLString

# QRCodeService (Object)

QRCodeService Class

## Methods (4)
- `Public Sub AddOrUpdateQRCode(ByVal pIQRCodeData As QRCodeData)` AddOrUpdateQRCode
  - param `pIQRCodeData`: 
- `Public Function GetDataInterface(ByVal enumMSDI As QRCodeServiceDataInterfaces) As Object` GetDataInterface
  - param `enumMSDI`: one of the enumeration's values (see the enum file)
  - enum: `QRCodeServiceDataInterfaces` in `../enums/enums-03.md`
- `Public Function GetDataInterfaceFromXMLFile(ByVal bstrFileName As String) As Object` GetDataInterfaceFromXMLFile
  - param `bstrFileName`: 
- `Public Function GetDataInterfaceFromXMLString(ByVal bstrXMLString As String) As Object` GetDataInterfaceFromXMLString
  - param `bstrXMLString`: 

# QueryAuthGroup (Object)

QueryAuthGroup Class

## Properties (4)
- `Public Property AuthGroupCode() As String` [R/W] property AuthGroupCode
- `Public Property AuthGroupDes() As String` [R/W] property AuthGroupDes
- `Public Property AuthGroupId() As Long` [R] property AuthGroupId
- `Public Property CategoryGroupCollection() As CategoryGroupCollection` [R] property CategoryGroupCollection

## Methods (5)
- `Public Sub FromXMLFile(ByVal bstrFileName As String)` method FromXMLFile
  - param `bstrFileName`: 
- `Public Sub FromXMLString(ByVal bstrXML As String)` method FromXMLString
  - param `bstrXML`: 
- `Public Function GetXMLSchema() As String` method GetXMLSchema
- `Public Sub ToXMLFile(ByVal bstrFileName As String)` method ToXMLFile
  - param `bstrFileName`: 
- `Public Function ToXMLString() As String` method ToXMLString

# QueryAuthGroupCollection (Collection)

QueryAuthGroupCollection Class

## Properties (1)
- `Public Property Count() As Long` [R] Count

## Methods (5)
- `Public Function Add() As QueryAuthGroup` method Add
- `Public Function GetXMLSchema() As String` method GetXMLSchema
- `Public Function Item(ByVal vtIndex As Variant) As QueryAuthGroup` DISPID_VALUE
  - param `vtIndex`: 
- `Public Sub ToXMLFile(ByVal bstrFileName As String)` method ToXMLFile
  - param `bstrFileName`: 
- `Public Function ToXMLString() As String` method ToXMLString

# QueryAuthGroupParams (Object)

QueryAuthGroupParams Class

## Properties (2)
- `Public Property AuthGroupCode() As String` [R/W] property AuthGroupCode
- `Public Property AuthGroupId() As Long` [R/W] property AuthGroupId

## Methods (5)
- `Public Sub FromXMLFile(ByVal bstrFileName As String)` method FromXMLFile
  - param `bstrFileName`: 
- `Public Sub FromXMLString(ByVal bstrXML As String)` method FromXMLString
  - param `bstrXML`: 
- `Public Function GetXMLSchema() As String` method GetXMLSchema
- `Public Sub ToXMLFile(ByVal bstrFileName As String)` method ToXMLFile
  - param `bstrFileName`: 
- `Public Function ToXMLString() As String` method ToXMLString

# QueryAuthGroupService (Object)

QueryAuthGroupService Class

## Methods (8)
- `Public Function AddQueryAuthGroup(ByVal pIQueryAuthGroup As QueryAuthGroup) As QueryAuthGroup` AddQueryAuthGroup
  - param `pIQueryAuthGroup`: 
- `Public Function GetDataInterface(ByVal enumMSDI As QueryAuthGroupServiceDataInterfaces) As Object` GetDataInterface
  - param `enumMSDI`: one of the enumeration's values (see the enum file)
  - enum: `QueryAuthGroupServiceDataInterfaces` in `../enums/enums-03.md`
- `Public Function GetDataInterfaceFromXMLFile(ByVal bstrFileName As String) As Object` GetDataInterfaceFromXMLFile
  - param `bstrFileName`: 
- `Public Function GetDataInterfaceFromXMLString(ByVal bstrXMLString As String) As Object` GetDataInterfaceFromXMLString
  - param `bstrXMLString`: 
- `Public Function GetQueryAuthGroup(ByVal pIQueryAuthGroupParams As QueryAuthGroupParams) As QueryAuthGroup` GetQueryAuthGroup
  - param `pIQueryAuthGroupParams`: 
- `Public Function GetQueryAuthGroupList() As QueryAuthGroupCollection` GetQueryAuthGroupList
- `Public Sub RemoveQueryAuthGroup(ByVal pIQueryAuthGroupParams As QueryAuthGroupParams)` RemoveQueryAuthGroup
  - param `pIQueryAuthGroupParams`: 
- `Public Sub UpdateQueryAuthGroup(ByVal pIQueryAuthGroup As QueryAuthGroup)` UpdateQueryAuthGroup
  - param `pIQueryAuthGroup`: 

# QueryCategories (Object)

QueryCategories is a business object that represents the query categories in the Queries Manager. This object enables you to: - Add a query category. - Retrieve a query category by its key. - Update a query category. - Save the object in XML format. Source table: OQCN.

**Remarks:** To display the form in the application: - From the main menu, select Tools --> Queries --> Queries Manager. - In the Manage Categories dialog box, click Manage Categories.

## Properties (5)
- `Public Property Browser() As DataBrowser` [R] Returns the DataBrowser object.
- `Public Property Code() As Long` [R] Returns the key of the query category. Field name: CategoryId.
  - remarks: SAP Business One assigns a sequential number, starting from 1, for each category that you add.
- `Public Property Name() As String` [R/W] Sets or returns the name of the query category. Field name: CatName. Length: 50 characters.
- `Public Property Permissions() As String` [R/W] Sets or returns the permissions's mask for this query category. Field name: PermMask. Length: 20 characters.
- `Public Property UserFields() As UserFields` [R] Returns the UserFields object.

## Methods (6)
- `Public Function Add() As Long` Adds a new category to the Query Categories table.
- `Public Function GetAsXML() As String` Returns the object from XML data, which is stored as string in a buffer.
  - remarks: You can use this method for development technologies that do not support return value as an Out parameter, such as ASP. You do not have to set the XMLAsString property of the Company object.
- `Public Function GetByKey(ByVal lID As Long) As Boolean` Retrieves and sets the values of the object's properties by the object's absolute key from the Company database.
  - param `lID`: Query category Code.
  - returns: If the object with the key you specified is found, the method returns True and the properties of the object will be filled with object's data. If the object with the key you specified is not found, the method returns False and the properties of the object remain unchanged.
  - remarks: To use this method you must specify the object key. You can also use this method to find whether or not there is an object related to the key you specify. If you do not know the object key, you can use the DataBrowser object to retreive an object using more complex queries.
- `Public Sub SaveToFile(ByVal FileName As String)` Save the object to a file as XML data.
  - param `FileName`: Specifies the path and file name of the XML data. Specifies the path and file name of the XML data.
  - remarks: You can use this method for development technologies that do not support return value as an Out parameter, such as ASP.
- `Public Sub SaveXML(ByRef FileName As String)` Saves the object data to XML formatted data.
  - param `FileName`: Specifies the path and file name of the XML data. Specifies the path and file name of the XML data.
  - remarks: You can use this method to save a business object to an XML file. Then, call the GetBusinessObjectFromXML method to load this object into memory again, for example, to copy customers from one database to another. To enable this operation, set the XmlExportType property of the Company object to xet_ValidNodesOnly. To use ReadXML method, set the XmlExportType to xet_ExportImportMode (3). For more information, see Exchanging Data Using the DI API XML Capabilities.
  - example note: The following sample shows how to save data of an object to an XML file. Use this sample as a basis to all business objects (both document and master data types).
  - VB example (SAP provides no C# sample for this - translate, don't paste):
    ```vb
    Dim vInvoice As SAPbobsCOM.Documents

    Set vInvoice = vCmp.GetBusinessObject(oInvoices)

    'Retrieve an invoice document from the database

    RetVal = vInvoice.GetByKey("1023")

    If RetVal <> 0 Then

         vCmp.GetLastError ErrCode, ErrMsg

         MsgBox "Failed to Retrieve the record " & ErrCode & " " & ErrMsg

         Exit Sub

    End If

    'Save the object as an xml file

    vInvoice.SaveXML ("C:\Program Files\SAP\XML\Invoice.xml")

    'Retrieve the object back from the XML file

    Set vInvoice = vCmp.GetBusinessObjectFromXML("C:\Program Files\SAP\XML\Invoice.xml", 0)
    ```
- `Public Function Update() As Long` Updates the object data in the company database.
  - returns: Returns a result value that indicates success or failure. If the method succeeds, it returns 0. Otherwise, it returns an error code. You can retrieve the last error code and its description using the method GetLastError.
  - remarks: Before using this method, you must use the GetByKey method to retrieve an existing record, and to set the values to the object mandatory properties. You can also use the SBObob object to browse lists of objects.

# Queue (Object)

Queue is a business object that represents the queues list in the Service module from which you can assign a queue member to a service call. A queue is a group of SAP Business One users (queue members) that have a common role, such as software service representatives, hardware service representatives, and so on. This object enables you to: - Add a queue. - Retrieve a queue by its key. - Update a queue. - Remove a queue. - Save the object in XML format. Source table: OQUE.

**Remarks:** Mandatory fields in SAP Business One: Description, QueueID, and QueueManager. To display the form in the application: - Select Administration --> Setup --> Service --> Queues.

## Properties (8)
- `Public Property Browser() As DataBrowser` [R] Returns the DataBrowser object.
- `Public Property Description() As String` [R/W] Sets or returns a description of the queue. Mandatory property. Field name: descript. Length: 200 characters.
- `Public Property Inactive() As BoYesNoEnum` [R/W] Sets or returns a valid value of BoYesNoEnum type that specifies whether or not the queue is inactive. Field name: inactive.
  - remarks: Inactive queues are not displayed in the Choose From List form (where available) in the Service module.
- `Public Property QueueEmail() As String` [R/W] Sets or returns a e-mail address of the queue. Field name: email. Length: 200 characters.
- `Public Property QueueID() As String` [R/W] Sets or returns a unique code for identifying the queue. Mandatory property. Field name: queueID. Length: 20 characters.
- `Public Property QueueManager() As Long` [R/W] Sets or returns a queue manager as defined in SAP Business One. Mandatory property. Field name: manager. This is a foreign key to the Users object.
- `Public Property QueueMembers() As QueueMembers` [R] Returns the QueueMembers child object.
- `Public Property UserFields() As UserFields` [R] Returns the UserFields object.

## Methods (7)
- `Public Function Add() As Long` Adds a record to the object table in SAP Business One company database.
  - returns: Returns a result value that indicates success or failure. If the method succeeds, it returns 0. Otherwise, it returns an error code. You can retrieve the last error code and its description using the method GetLastError.
  - remarks: You must values for the mandatory properties, and then call the Add method. The auto-complete feature completes all the default values of the other properties. In the DI API, the auto-complete feature operates the same way as in the SAP Business One application.
- `Public Function GetAsXML() As String` Returns the object from XML data, which is stored as string in a buffer.
  - remarks: You can use this method for development technologies that do not support return value as an Out parameter, such as ASP. You do not have to set the XMLAsString property of the Company object.
- `Public Function GetByKey(ByVal bstrQueueID As String) As Boolean` Retrieves and sets the values of the object's properties by the object's absolute key from the Company database.
  - param `bstrQueueID`: Queue ID (QueueID).
  - returns: If the object with the key you specified is found, the method returns True and the properties of the object will be filled with object's data. If the object with the key you specified is not found, the method returns False and the properties of the object remain unchanged.
  - remarks: To use this method you must specify the object key. You can also use this method to find whether or not there is an object related to the key you specify. If you do not know the object key, you can use the DataBrowser object to retreive an object using more complex queries.
- `Public Function Remove() As Long` Not supported.
- `Public Sub SaveToFile(ByVal FileName As String)` Save the object to a file as XML data.
  - param `FileName`: Specifies the path and file name of the XML data. Specifies the path and file name of the XML data.
  - remarks: You can use this method for development technologies that do not support return value as an Out parameter, such as ASP.
- `Public Sub SaveXML(ByRef FileName As String)` Saves the object data to XML formatted data.
  - param `FileName`: Specifies the path and file name of the XML data. Specifies the path and file name of the XML data.
  - remarks: You can use this method to save a business object to an XML file. Then, call the GetBusinessObjectFromXML method to load this object into memory again, for example, to copy customers from one database to another. To enable this operation, set the XmlExportType property of the Company object to xet_ValidNodesOnly. To use ReadXML method, set the XmlExportType to xet_ExportImportMode (3). For more information, see Exchanging Data Using the DI API XML Capabilities.
  - example note: The following sample shows how to save data of an object to an XML file. Use this sample as a basis to all business objects (both document and master data types).
  - VB example (SAP provides no C# sample for this - translate, don't paste):
    ```vb
    Dim vInvoice As SAPbobsCOM.Documents

    Set vInvoice = vCmp.GetBusinessObject(oInvoices)

    'Retrieve an invoice document from the database

    RetVal = vInvoice.GetByKey("1023")

    If RetVal <> 0 Then

         vCmp.GetLastError ErrCode, ErrMsg

         MsgBox "Failed to Retrieve the record " & ErrCode & " " & ErrMsg

         Exit Sub

    End If

    'Save the object as an xml file

    vInvoice.SaveXML ("C:\Program Files\SAP\XML\Invoice.xml")

    'Retrieve the object back from the XML file

    Set vInvoice = vCmp.GetBusinessObjectFromXML("C:\Program Files\SAP\XML\Invoice.xml", 0)
    ```
- `Public Function Update() As Long` Updates the object data in the company database.
  - returns: Returns a result value that indicates success or failure. If the method succeeds, it returns 0. Otherwise, it returns an error code. You can retrieve the last error code and its description using the method GetLastError.
  - remarks: Before using this method, you must use the GetByKey method to retrieve an existing record, and to set the values to the object mandatory properties. You can also use the SBObob object to browse lists of objects.

# QueueMembers (Object)

QueueMembers is a child object of Queue object and represents SAP Business One users that are members of the queue. Source tables: QUE1.

**Remarks:** To display the form in the application: - Select Administration --> Setup --> Service --> Queues. - Select a queue and then click Queue Members.

## Properties (4)
- `Public Property Count() As Long` [R] Returns the number of queue members for the current queue.
- `Public Property MemberUserID() As Long` [R/W] Sets or returns the Queue's member user ID. Field name: member. This is a foreign key to the Users object.
- `Public Property QueueID() As String` [R/W] Sets or returns a unique code for identifying the queue. Mandatory property. Field name: queueID. Length: 20 characters This is a foreign key to the Queue object.
- `Public Property UserFields() As UserFields` [R] Returns the UserFields object.

## Methods (2)
- `Public Sub Add()` Adds a new data line to the object.
  - remarks: You can use this method to add an empty line to the current object. After the line is added, you can set values to the properties of this line. Note: When a new object is created, it already contains one data line, so you can set the properties of the first line directly without adding a new line. However, if the object contains more than one line, you must use the Add method.
- `Public Sub SetCurrentLine(ByVal LineNum As Long)` Sets the active row to a specified row number.
  - param `LineNum`: Specifies the row number. The count starts from 0.

# RclRecurringExecutionParams (Object)

RclRecurringExecutionParams Class

## Properties (1)
- `Public Property OnError() As RclRecurringExecutionHandlingEnum` [R/W] property OnError

## Methods (5)
- `Public Sub FromXMLFile(ByVal bstrFileName As String)` method FromXMLFile
  - param `bstrFileName`: 
- `Public Sub FromXMLString(ByVal bstrXML As String)` method FromXMLString
  - param `bstrXML`: 
- `Public Function GetXMLSchema() As String` method GetXMLSchema
- `Public Sub ToXMLFile(ByVal bstrFileName As String)` method ToXMLFile
  - param `bstrFileName`: 
- `Public Function ToXMLString() As String` method ToXMLString

# RclRecurringTransaction (Object)

RclRecurringTransaction Class

## Properties (7)
- `Public Property DocEntry() As Long` [R] property DocEntry
- `Public Property DocType() As String` [R] property DocType
- `Public Property Instance() As Long` [R] property Instance
- `Public Property PlannedDate() As Date` [R] property PlannedDate
- `Public Property Status() As RclRecurringTransactionStatusEnum` [R] property Status
- `Public Property TemplateID() As Long` [R] property TemplateID
- `Public Property TransactionID() As Long` [R] property TransactionID

## Methods (5)
- `Public Sub FromXMLFile(ByVal bstrFileName As String)` method FromXMLFile
  - param `bstrFileName`: 
- `Public Sub FromXMLString(ByVal bstrXML As String)` method FromXMLString
  - param `bstrXML`: 
- `Public Function GetXMLSchema() As String` method GetXMLSchema
- `Public Sub ToXMLFile(ByVal bstrFileName As String)` method ToXMLFile
  - param `bstrFileName`: 
- `Public Function ToXMLString() As String` method ToXMLString

# RclRecurringTransactionCollection (Collection)

RclRecurringTransactionCollection Class

## Properties (1)
- `Public Property Count() As Long` [R] Count

## Methods (5)
- `Public Function Add() As RclRecurringTransaction` method Add
- `Public Function GetXMLSchema() As String` method GetXMLSchema
- `Public Function Item(ByVal vtIndex As Variant) As RclRecurringTransaction` DISPID_VALUE
  - param `vtIndex`: 
- `Public Sub ToXMLFile(ByVal bstrFileName As String)` method ToXMLFile
  - param `bstrFileName`: 
- `Public Function ToXMLString() As String` method ToXMLString

# RclRecurringTransactionParams (Object)

RclRecurringTransactionParams Class

## Properties (2)
- `Public Property PlannedDate() As Date` [R/W] property PlannedDate
- `Public Property TransactionID() As Long` [R/W] property TransactionID

## Methods (5)
- `Public Sub FromXMLFile(ByVal bstrFileName As String)` method FromXMLFile
  - param `bstrFileName`: 
- `Public Sub FromXMLString(ByVal bstrXML As String)` method FromXMLString
  - param `bstrXML`: 
- `Public Function GetXMLSchema() As String` method GetXMLSchema
- `Public Sub ToXMLFile(ByVal bstrFileName As String)` method ToXMLFile
  - param `bstrFileName`: 
- `Public Function ToXMLString() As String` method ToXMLString

# RclRecurringTransactionParamsCollection (Collection)

RclRecurringTransactionParamsCollection Class

## Properties (1)
- `Public Property Count() As Long` [R] Count

## Methods (5)
- `Public Function Add() As RclRecurringTransactionParams` method Add
- `Public Function GetXMLSchema() As String` method GetXMLSchema
- `Public Function Item(ByVal vtIndex As Variant) As RclRecurringTransactionParams` DISPID_VALUE
  - param `vtIndex`: 
- `Public Sub ToXMLFile(ByVal bstrFileName As String)` method ToXMLFile
  - param `bstrFileName`: 
- `Public Function ToXMLString() As String` method ToXMLString

# Recipient (Object)

Recipient is a data structure related to the MessagesService. It represents the data of a single recipient of a message or alert. Source table: AOB1.

## Properties (10)
- `Public Property CellularNumber() As String` [R/W] Sets or returns the cellular phone number of the recipient. Field name: PortNum. Length: 50 characters.
- `Public Property EmailAddress() As String` [R/W] Sets or returns the recipient email address. Field name: E_Mail. Length: 100 characters.
- `Public Property FaxNumber() As String` [R/W] Sets or returns the recipient fax number. Field name: Fax. Length: 20 characters.
- `Public Property NameTo() As String` [R/W] Sets or returns the recipient name. Field name: ObjName. Length: 100 characters.
- `Public Property SendEmail() As BoYesNoEnum` [R/W] Determines whether or not the message is sent to an email address. Field name: SendEMail.
- `Public Property SendFax() As BoYesNoEnum` [R/W] Determines whether or not the message is sent by fax. Field name: SendFax.
- `Public Property SendInternal() As BoYesNoEnum` [R/W] Determines whether or not the message is internal. That is, the message will be sent only to users (employees) that are defined in SAP Business One. Field name: SendIntrnl.
- `Public Property SendSMS() As BoYesNoEnum` [R/W] Determines whether or not the message is sent by SMS. Field name: SendSMS.
- `Public Property UserCode() As String` [R/W] Sets or returns the user code of the recipient. Mandatory property. Field name: ObjCode. Length: 50 characters.
- `Public Property UserType() As BoMsgRcpTypes` [R/W] Sets or returns a valid value that specifies the type of recipient for the message. Mandatory property. Field name: ObjType.

## Methods (5)
- `Public Sub FromXMLFile(ByVal bstrFileName As String)` Imports data from an XML file to the object.
  - param `bstrFileName`: Specifies the the XML file.
- `Public Sub FromXMLString(ByVal bstrXML As String)` Imports data from an XML string to the object.
  - param `bstrXML`: P>Specifies the the XML string.
- `Public Function GetXMLSchema() As String` Retrieves the XML schema of the data structure.
- `Public Sub ToXMLFile(ByVal bstrFileName As String)` Creates an XML file that represents the object data.
  - param `bstrFileName`: Specifies the XML file name including path.
- `Public Function ToXMLString() As String` Creates an XML string that represents the object data.

# RecipientCollection (Collection)

RecipientCollection is a collection of Recipient data structures. It represents the list of receipients of a message (replaces the Recipients object - backward compatibilty is maintained).

## Properties (1)
- `Public Property Count() As Long` [R] Returns the total number of Recipients of a message.

## Methods (5)
- `Public Function Add() As Recipient` Adds a receipient to a message.
- `Public Function GetXMLSchema() As String` Retrieves the XML schema of the data structure.
- `Public Function Item(ByVal vtIndex As Variant) As Recipient` Returns a reference to an existing item in the collection by its index.
  - param `vtIndex`: Specifies the index of the recipient in the collection.
- `Public Sub ToXMLFile(ByVal bstrFileName As String)` Creates an XML file that represents the object data.
  - param `bstrFileName`: Specifies the XML file name including path.
- `Public Function ToXMLString() As String` Creates an XML string that represents the object data.

# Recipients (Object)

Recipients is a business object that represents the recipients' list of a message or alert. This object enables you to add recipient information to the recipients list for sending messages. You can use the RecipientCollection and the Recipient object instead of the Recipients object (backward compatibilty is maintained). Source table: AOB1.

**Remarks:** Mandatory fields in SAP Business One: UserCode and UserType. To display the form in the application: - From the main menu bar, select File --> Send --> Send Message. - Click Add Recipient.

## Properties (11)
- `Public Property CellularNumber() As String` [R/W] Sets or returns the cellular phone number of the recipient. Field name: PortNum. Length: 50 characters.
- `Public Property Count() As Long` [R] Returns the number of recipients in the collection.
  - remarks: After adding a new recipient, the value of this property increases automatically.
- `Public Property EmailAddress() As String` [R/W] Sets or returns the recipient email address. Field name: E_Mail. Length: 100 characters.
- `Public Property FaxNumber() As String` [R/W] Sets or returns the recipient fax number. Field name: Fax. Length: 20 characters.
- `Public Property NameTo() As String` [R/W] Sets or returns the recipient name. Field name: ObjName. Length: 100 characters.
- `Public Property SendEmail() As BoYesNoEnum` [R/W] Determines whether or not the message is sent to an email address. Field name: SendEMail.
- `Public Property SendFax() As BoYesNoEnum` [R/W] Determines whether or not the message is sent by fax. Field name: SendFax.
- `Public Property SendInternal() As BoYesNoEnum` [R/W] Determines whether or not the message is internal. That is, the message will be sent only to users (employees) that are defined in SAP Business One. Field name: SendIntrnl.
- `Public Property SendSMS() As BoYesNoEnum` [R/W] Determines whether or not the message is sent by SMS. Field name: SendSMS.
- `Public Property UserCode() As String` [R/W] Sets or returns the user code of the recipient. Mandatory property. Field name: ObjCode. Length: 50 characters.
  - remarks: The user code is a reference to a key in the database table.
- `Public Property UserType() As BoMsgRcpTypes` [R/W] Sets or returns a valid value that specifies the type of recipient for the message. Mandatory property. Field name: ObjType.

## Methods (2)
- `Public Sub Add()` Adds a new recipient to the collection.
- `Public Sub SetCurrentLine(ByVal LineNum As Long)` Sets the active row to a specified row number.
  - param `LineNum`: Specifies the row number. The count starts from 0.

# ReconciliationBankStatementLine (Object)

Represents open transactions to be reconciled in external bank statement. ReconciliationBankStatementLine is a child object of the ExternalReconciliation object. Source table: OBNK.

## Properties (6)
- `Public Property amount() As Double` [R] Original amount posted in the specific row of the transaction. Field name: DebAmount.
- `Public Property BankStatementAccountCode() As String` [R/W] The account number. Field name: BnkAcctCode.
- `Public Property Date() As Date` [R] Due date of the transaction involved in the selected reconciliation. Field name: DueDate.
- `Public Property Details() As String` [R] Displays details as they appear in the Details field for the transaction in the Process External Bank Statement window. Field name: Memo.
- `Public Property Ref1() As String` [R] Displays the reference number as it appears in the Reference field for the transaction in the Process External Bank Statement window. Field name: Ref.
- `Public Property Sequence() As Long` [R/W] The assigned sequence number. Field name: Sequence.

## Methods (5)
- `Public Sub FromXMLFile(ByVal bstrFileName As String)` Sets the object's properties using data from an XML file. The XML file can be created using the object's ToXMLFile method.
  - param `bstrFileName`: The path and name of the XML file from which to retrieve the object's data.
- `Public Sub FromXMLString(ByVal bstrXML As String)` Sets the object's properties using data from an XML string. The XML string can be created using the object's ToXMLString method.
  - param `bstrXML`: The XML from which to retrieve the object's data.
- `Public Function GetXMLSchema() As String` Returns the XML schema for the XML generated by the ToXMLFile and ToXMLString methods.
- `Public Sub ToXMLFile(ByVal bstrFileName As String)` Creates an XML file that represents the object.
  - param `bstrFileName`: The path and file name of the XML file.
  - remarks: The schema of the XML can be retrieved with the GetXMLSchema method.
- `Public Function ToXMLString() As String` Creates and returns an XML string that represents the object.
  - remarks: The schema of the XML can be retrieved with the GetXMLSchema method.

# ReconciliationBankStatementLines (Collection)

A collection of ReconciliationBankStatementLine objects.

## Properties (1)
- `Public Property Count() As Long` [R] Returns the number of objects in the collection.

## Methods (5)
- `Public Function Add() As ReconciliationBankStatementLine` Adds an empty object to the collection.
  - remarks: After an object is added to this collection, the database is not automatically updated. You must then update the GeneralData object to which this collection belongs, by executing the Update method of the GeneralService service.
- `Public Function GetXMLSchema() As String` Returns the XML schema for the XML generated by the ToXMLFile and ToXMLString methods.
- `Public Function Item(ByVal vtIndex As Variant) As ReconciliationBankStatementLine` Returns the object at the specified index.
  - param `vtIndex`: The index of the object to be returned (0-based)
- `Public Sub ToXMLFile(ByVal bstrFileName As String)` Creates an XML file that represents the object.
  - param `bstrFileName`: The path and file name of the XML file.
  - remarks: The schema of the XML can be retrieved with the GetXMLSchema method.
- `Public Function ToXMLString() As String` Creates and returns an XML string that represents the object.
  - remarks: The schema of the XML can be retrieved with the GetXMLSchema method.

# ReconciliationJournalEntryLine (Object)

Represents open transactions to be reconciled in journal entry. ReconciliationJournalEntryLine is a child object of the ExternalReconciliation object. Source table: JDT1.

## Properties (10)
- `Public Property CreditAmount() As Double` [R] The credit amount. Field name: Credit.
- `Public Property DebitAmount() As Double` [R] The debit amount. Field name: Debit.
- `Public Property Details() As String` [R] Displays remarks as they appear in the Remarks field for the transaction in the Journal Entry window, or details as they appear in the Details field for the transaction in the Process External Bank Statement window. Field name: Memo.
- `Public Property DueDate() As Date` [R] Due date of the transaction involved in the selected reconciliation. Field name: DueDate.
- `Public Property LineNumber() As Long` [R/W] The line number. Field name: LineID.
- `Public Property PostingDate() As Date` [R] The posting date. Field name: RefDate.
- `Public Property Ref1() As String` [R] Displays the reference number as it appears in the Ref. 1 field for the transaction in the Journal Entry window. Field name: Ref1.
- `Public Property Ref2() As String` [R] Displays the reference number as it appears in the Ref. 2 field for the transaction in the Journal Entry window. Field name: Ref2.
- `Public Property Ref3() As String` [R] Displays the reference number as it appears in the Ref. 3 field for the transaction in the Journal Entry window. Field name: Ref3Line.
- `Public Property TransactionNumber() As Long` [R/W] The journal entry number of the transaction involved in the selected reconciliation. Field name: TransID.

## Methods (5)
- `Public Sub FromXMLFile(ByVal bstrFileName As String)` Sets the object's properties using data from an XML file. The XML file can be created using the object's ToXMLFile method.
  - param `bstrFileName`: The path and name of the XML file from which to retrieve the object's data.
- `Public Sub FromXMLString(ByVal bstrXML As String)` Sets the object's properties using data from an XML string. The XML string can be created using the object's ToXMLString method.
  - param `bstrXML`: The XML from which to retrieve the object's data.
- `Public Function GetXMLSchema() As String` Returns the XML schema for the XML generated by the ToXMLFile and ToXMLString methods.
- `Public Sub ToXMLFile(ByVal bstrFileName As String)` Creates an XML file that represents the object.
  - param `bstrFileName`: The path and file name of the XML file.
  - remarks: The schema of the XML can be retrieved with the GetXMLSchema method.
- `Public Function ToXMLString() As String` Creates and returns an XML string that represents the object.
  - remarks: The schema of the XML can be retrieved with the GetXMLSchema method.

# ReconciliationJournalEntryLines (Collection)

A collection of ReconciliationJournalEntryLine objects.

## Properties (1)
- `Public Property Count() As Long` [R] Returns the number of objects in the collection.

## Methods (5)
- `Public Function Add() As ReconciliationJournalEntryLine` Adds an empty object to the collection.
  - remarks: After an object is added to this collection, the database is not automatically updated. You must then update the GeneralData object to which this collection belongs, by executing the Update method of the GeneralService service.
- `Public Function GetXMLSchema() As String` Returns the XML schema for the XML generated by the ToXMLFile and ToXMLString methods.
- `Public Function Item(ByVal vtIndex As Variant) As ReconciliationJournalEntryLine` Returns the object at the specified index.
  - param `vtIndex`: The index of the object to be returned (0-based)
- `Public Sub ToXMLFile(ByVal bstrFileName As String)` Creates an XML file that represents the object.
  - param `bstrFileName`: The path and file name of the XML file.
  - remarks: The schema of the XML can be retrieved with the GetXMLSchema method.
- `Public Function ToXMLString() As String` Creates and returns an XML string that represents the object.
  - remarks: The schema of the XML can be retrieved with the GetXMLSchema method.

# Recordset (Object)

Recordset is a raw data access object that enables you to select data from the database, navigate through the result set, and manipulate user tables, which are not exposed by the DI API. The main method of this object is DoQuery that enables you to run SQL queries with any DML action in its query string.

**Remarks:** Browsing Mechanisms The Recordset object includes two browsing mechanisms: the first mechanism applies to result sets that contain only one row (by the use of Select Top), which will retrieve only one record each time. Otherwise, the browsing will be performed on existing result set only. DML Operations on Database Tables The Recordset object allows the following Data Manipulation Language (DML) operations: UPDATE, INSERT, and DELETE. DML operations are acceptable with the Recordset object for user tables only. For other business objects use only the relevant DI objects and not the Recordset object. Any DML operations on system tables pose a high risk for data corruption, and will not be supported. Use at your own risk. Before the Recordset object executes an SQL query, it validates the user permission (same user permission as in SAP Business One). Otherwise, the SQL query is blocked. Blocking DDL Actions The following Data Definition Language (DDL) actions are blocked: CREATE, DROP, ALTER, and TRUNCATE. The reason for that is, when upgrading the SAP Business One application, it ignores user tables that are not created using the DI meta data objects (UserTablesMD and UserFieldsMD). Limitation Only one expression can be specified in the select list when the sub-query is not introduced with EXISTS. Related Topics Selecting Data Using the Recordset Object Retrieving a Field of a Recordset

## Properties (6)
- `Public Property BoF() As Boolean` [R] Returns a Boolean value that indicates whether or not the current row is the first row in the result set (Beginning of File).
  - remarks: The property indicates if there is a record before the current record. If the property returns Yes, the current record is the first record of the table. If both Bof and Eof properties return True, there are no records in the table.
- `Public Property Command() As Command` [R] Returns the Command object that enables to execute SQL stored procedures.
- `Public Property EoF() As Boolean` [R] Returns a Boolean value that indicates whether or not the current row is the last row in the result set (End of File).
  - remarks: The property indicates if there is a record after the current record. If the property returns Yes, the current record is the last record of the table. If both Bof and Eof properties return True, there are no records in the table.
- `Public Property Fields() As Fields` [R] Returns a Fields collection, which contains the fields of the result set.
- `Public Property RecordCount() As Long` [R] Returns the number of records contained in the result set.
- `Public Property RecordSetAudit() As Boolean` [R/W] For security enhancement, if this flag is set to true, the querying will be logged in table RSAT. By default, the flag is set to false.
  - C# example (from SAP's help):
    ```csharp
    SAPbobsCOM.Recordset oRecordSet = oCompany.GetBusinessObject(SAPbobsCOM.BoObjectTypes.BoRecordset);
                SAPbobsCOM.RecordsetEx oRecordSetex = oCompany.GetBusinessObject(SAPbobsCOM.BoObjectTypes.BoRecordsetEx);
                string query = ""select * from oitm"";
                oRecordSet.RecordSetAudit = true;
                oRecordSetex.RecordSetAudit = true;
                try
                {
                    oRecordSetex.DoQuery(query);
                    oRecordSet.DoQuery(query);
                }
                catch (Exception e)
                {
                    Console.WriteLine(e.Message);
                }
    ```

## Methods (10)
- `Public Sub DoQuery(ByVal QueryStr As String)` Runs SQL queries.
  - param `QueryStr`: Specifies a query string, which contains the SQL query commands you want to run.
  - returns: -2000 ODBC Error.
  - remarks: If the method is successful, the object will contain the returned query result set. Note: As of SAP Business One 10.0, the DoQuery function can access the current logon company DB only. If you access Common DB, the DoQuery function will throw exception. Limitation: Only one expression can be specified in the select list when the subquery is not introduced with EXISTS. Other limitations includes the following query usage: - Nested Query - Query with Union and Union ALL - Using Like - Using Ali - Flow control statments (If / While / Break / Continue) - Calling procedures, fuctions, triggers and etc. - Distinct (i.e: "SELECT DISTINCT CardType FROM OCRD") - Multiple queries (i.e: Queries seperated with ; (semicolons) may not work, if there is no space before it)
  - example note: The following example shows the DoQuery and MoveNext methods.
  - VB example (SAP provides no C# sample for this - translate, don't paste):
    ```vb
    Dim Count   As Long

    Dim FldName As String

    Dim FldVal  As String

    Dim i       As Long

    Dim RecSet  As SAPbobsCOM.Recordset

    Set RecSet = vCmp.GetBusinessObject(BoRecordset)

    RecSet.DoQuery ("select * from OADM")

    Count = RecSet.Fields.Count

      While RecSet.EOF = False

            'The inner loop runs over all the fields in one record (line) of the table

            For i = 0 To Count - 1

                FldName = RecSet.Fields.Item(i).Name

                FldVal = RecSet.Fields.Item(i).Value

                'Here you can manipulate the data as you want

            Next i

            'Move to the next record

            RecSet.MoveNext

      Wend
    ```
- `Public Function GetAsXML() As String` Returns the object from XML data, which is stored as string in a buffer.
  - remarks: You can use this method for development technologies that do not support return value as an Out parameter, such as ASP. You do not have to set the XMLAsString property of the Company object.
- `Public Function GetFixedSchema() As String` The schema for the XML returned by the GetFixedXML method.
- `Public Function GetFixedXML(ByVal xmlMode As RecordsetXMLModeEnum) As String` Returns the query data as XML based on a fixed schema. The GetAsXML also returns the data as XML, but the schema is dynamic and based on the specific query. With the GetFixedXML, the schema is fixed and is available with the GetFixedSchema method. You can use the schema, for example, to create a .NET object for handling the query XML. For more information, see Exchanging Data Using the DI API XML Capabilities.
  - param `xmlMode`: one of the enumeration's values (see the enum file)
  - enum: `RecordsetXMLModeEnum` in `../enums/enums-03.md`
- `Public Sub MoveFirst()` Moves the curser to the first row in the result set.
  - returns: Exceptional error code: -1002 Invalid row.
- `Public Sub MoveLast()` Moves the curser to the last row in the result set.
  - returns: Exceptional error code: -1002 Invalid row.
- `Public Sub MoveNext()` Moves the curser to the next row in the result set.
  - returns: Exceptional error code: -1002 Invalid row.
- `Public Sub MovePrevious()` Moves the curser to the previous row in the result set.
  - returns: Exceptional error code: -1002 Invalid row.
- `Public Sub SaveToFile(ByVal FileName As String)` Save the object to a file as XML data.
  - param `FileName`: Specifies the path and file name of the XML data. Specifies the path and file name of the XML data.
  - remarks: You can use this method for development technologies that do not support return value as an Out parameter, such as ASP.
- `Public Sub SaveXML(ByRef FileName As String)` Saves the query data to an XML file or a string. For more information, see Exchanging Data Using the DI API XML Capabilities.
  - param `FileName`: Specifies the path and file name of the XML data.
  - remarks: The XML file that is created by the Recordset object can be read by any XML parser but not by the DI API. See Recordset sample.

# RecordsetEx (Object)

RecordsetEx is a raw data access object that enables you to fetch data from the database table. The main method of this object is DoQuery, which lets you run SQL select queries in its query string.

**Remarks:** Browsing Mechanisms The RecordsetEx object includes two browsing mechanisms. The first mechanism applies to result sets that contain only one row (by the use of Select Top); it retrieves only one record each time. With the second mechanism, the browsing is performed on the existing result set only. Blocking DML Operations and DDL Actions The following Data Manipulation Language (DML) operations are blocked: UPDATE, INSERT, DELETE, TRUNCATE, UPSERT, REPLACE, and MERGE. The following Data Definition Language (DDL) operations are blocked: CREATE, DROP, ALTER, and RENAME. Limitation When the sub-query is not introduced with EXISTS, only one expression can be specified in the select list. As of SAP Business One 10.0, the DoQuery function can access the current logon company DB only. If you access Common DB, the DoQuery function will throw exception.

**Example:**
- C# example (from SAP's help):
  ```csharp
  SAPbobsCOM.RecordsetEx oRecordSetEx = oCompany.GetBusinessObject(SAPbobsCOM.BoObjectTypes.BoRecordsetEx);

  oRecordSetEx.DoQuery("select \"CardCode\", \"CardName\" from OCRD");

  while (!oRecordSetEx.EoF)
   {
         SAPbobsCOM.BoFieldTypes type = oRecordSetEx. .GetColumnType(0);
         var value = oRecordSetEx.GetColumnValue(0);

         //By Alias
         //SAPbobsCOM.BoFieldTypes type = oRecordSetEx. GetColumnType("CardCode");
         //var value = oRecordSetEx. GetColumnValue("CardCode");

         oRecordSetEx.MoveNext();
   }
  ```

## Properties (3)
- `Public Property ColumnsCount() As Long` [R] Returns the column number of the result set.
- `Public Property EoF() As Boolean` [R] Returns a Boolean value that indicates whether or not the current row is the last row in the result set (End of File).
- `Public Property RecordSetAudit() As Boolean` [R/W] For security enhancement, if this flag is set to true, the querying will be logged in table RSAT. By default, the flag is set to false.
  - C# example (from SAP's help):
    ```csharp
    SAPbobsCOM.Recordset oRecordSet = oCompany.GetBusinessObject(SAPbobsCOM.BoObjectTypes.BoRecordset);
                SAPbobsCOM.RecordsetEx oRecordSetex = oCompany.GetBusinessObject(SAPbobsCOM.BoObjectTypes.BoRecordsetEx);
                string query = ""select * from oitm"";
                oRecordSet.RecordSetAudit = true;
                oRecordSetex.RecordSetAudit = true;
                try
                {
                    oRecordSetex.DoQuery(query);
                    oRecordSet.DoQuery(query);
                }
                catch (Exception e)
                {
                    Console.WriteLine(e.Message);
                }
    ```

## Methods (4)
- `Public Sub DoQuery(ByVal QueryStr As String)` Runs SQL queries.
  - param `QueryStr`: Specifies a query string, which contains the SQL query commands you want to run.
- `Public Function GetColumnType(ByVal Index As Variant) As BoFieldTypes` Returns the column type by its position or by its alias.
  - param `Index`: index
- `Public Function GetColumnValue(ByVal Index As Variant) As Variant` Returns the column value by its position or by its alias.
  - param `Index`: index
- `Public Function MoveNext() As Boolean` Get next row data from query result; if it returns false, it means next row does not exist, else returns true.

# RecurringPostings (Object)

RecurringPostings Class

## Properties (19)
- `Public Property AutomaticVAT() As BoYesNoEnum` [R/W] property AutomaticVAT
- `Public Property Code() As String` [R/W] property Code
- `Public Property DeferredTax() As BoYesNoEnum` [R/W] property DeferredTax
- `Public Property Description() As String` [R/W] property Description
- `Public Property Frequency() As BoFrequencyTypeEnum` [R/W] property Frequency
- `Public Property Instance() As Long` [R] property Instance
- `Public Property ManageWTax() As BoYesNoEnum` [R/W] property ManageWTax
- `Public Property NextExecution() As Date` [R/W] property NextExecution
- `Public Property RecurringPostingsDocumentReferenceCollection() As RecurringPostingsDocumentReferenceCollection` [R] property RecurringPostingsDocumentReferenceCollection
- `Public Property RecurringPostingsLineCollection() As RecurringPostingsLineCollection` [R] property RecurringPostingsLineCollection
- `Public Property Reference1() As String` [R/W] property Reference1
- `Public Property Reference2() As String` [R/W] property Reference2
- `Public Property Reference3() As String` [R/W] property Reference3
- `Public Property Remarks() As String` [R/W] property Remarks
- `Public Property StampTax() As BoYesNoEnum` [R/W] property StampTax
- `Public Property SubFrequency() As BoSubFrequencyTypeEnum` [R/W] property SubFrequency
- `Public Property TransactionCode() As String` [R/W] property TransactionCode
- `Public Property ValidUntil() As BoYesNoEnum` [R/W] property ValidUntil
- `Public Property ValidUntilDate() As Date` [R/W] property ValidUntilDate

## Methods (5)
- `Public Sub FromXMLFile(ByVal bstrFileName As String)` method FromXMLFile
  - param `bstrFileName`: 
- `Public Sub FromXMLString(ByVal bstrXML As String)` method FromXMLString
  - param `bstrXML`: 
- `Public Function GetXMLSchema() As String` method GetXMLSchema
- `Public Sub ToXMLFile(ByVal bstrFileName As String)` method ToXMLFile
  - param `bstrFileName`: 
- `Public Function ToXMLString() As String` method ToXMLString

# RecurringPostingsDocumentReference (Object)

RecurringPostingsDocumentReference Class

## Properties (8)
- `Public Property ExternalReferencedDocNumber() As String` [R/W] property ExternalReferencedDocNumber
- `Public Property IssueDate() As Date` [R/W] property IssueDate
- `Public Property LineNumber() As Long` [R] property LineNumber
- `Public Property RcrCode() As String` [R] property RcrCode
- `Public Property ReferencedDocEntry() As Long` [R/W] property ReferencedDocEntry
- `Public Property ReferencedDocNumber() As Long` [R] property ReferencedDocNumber
- `Public Property ReferencedObjectType() As ReferencedObjectTypeEnum` [R/W] property ReferencedObjectType
- `Public Property Remark() As String` [R/W] property Remark

## Methods (5)
- `Public Sub FromXMLFile(ByVal bstrFileName As String)` method FromXMLFile
  - param `bstrFileName`: 
- `Public Sub FromXMLString(ByVal bstrXML As String)` method FromXMLString
  - param `bstrXML`: 
- `Public Function GetXMLSchema() As String` method GetXMLSchema
- `Public Sub ToXMLFile(ByVal bstrFileName As String)` method ToXMLFile
  - param `bstrFileName`: 
- `Public Function ToXMLString() As String` method ToXMLString

# RecurringPostingsDocumentReferenceCollection (Collection)

RecurringPostingsDocumentReferenceCollection Class

## Properties (1)
- `Public Property Count() As Long` [R] Count

## Methods (6)
- `Public Function Add() As RecurringPostingsDocumentReference` method Add
- `Public Function GetXMLSchema() As String` method GetXMLSchema
- `Public Function Item(ByVal vtIndex As Variant) As RecurringPostingsDocumentReference` DISPID_VALUE
  - param `vtIndex`: 
- `Public Sub Remove(ByVal vtIndex As Variant)` method Remove
  - param `vtIndex`: 
- `Public Sub ToXMLFile(ByVal bstrFileName As String)` method ToXMLFile
  - param `bstrFileName`: 
- `Public Function ToXMLString() As String` method ToXMLString

# RecurringPostingsLine (Object)

RecurringPostingsLine Class

## Properties (22)
- `Public Property AccountCode() As String` [R/W] property AccountCode
- `Public Property AccountName() As String` [R] property AccountName
- `Public Property ControlAccount() As String` [R/W] property ControlAccount
- `Public Property CostElementCode() As String` [R] property CostElementCode
- `Public Property CostingCode1() As String` [R/W] property CostingCode1
- `Public Property CostingCode2() As String` [R/W] property CostingCode2
- `Public Property CostingCode3() As String` [R/W] property CostingCode3
- `Public Property CostingCode4() As String` [R/W] property CostingCode4
- `Public Property CostingCode5() As String` [R/W] property CostingCode5
- `Public Property Credit() As Double` [R/W] property Credit
- `Public Property Currency() As String` [R/W] property Currency
- `Public Property Debit() As Double` [R/W] property Debit
- `Public Property DistributionRule() As String` [R/W] property DistributionRule
- `Public Property LineNumber() As Long` [R] property LineNumber
- `Public Property ProjectCode() As String` [R/W] property ProjectCode
- `Public Property RcrCode() As String` [R] property RcrCode
- `Public Property TaxCode() As String` [R/W] property TaxCode
- `Public Property TaxGroup() As String` [R/W] property TaxGroup
- `Public Property TaxPostingAccount() As BoTaxPostingAccountTypeEnum` [R/W] property TaxPostingAccount
- `Public Property VatLine() As BoYesNoEnum` [R/W] property VatLine
- `Public Property WTaxLiable() As BoYesNoEnum` [R/W] property WTaxLiable
- `Public Property WTaxLine() As BoYesNoEnum` [R/W] property WTaxLine

## Methods (5)
- `Public Sub FromXMLFile(ByVal bstrFileName As String)` method FromXMLFile
  - param `bstrFileName`: 
- `Public Sub FromXMLString(ByVal bstrXML As String)` method FromXMLString
  - param `bstrXML`: 
- `Public Function GetXMLSchema() As String` method GetXMLSchema
- `Public Sub ToXMLFile(ByVal bstrFileName As String)` method ToXMLFile
  - param `bstrFileName`: 
- `Public Function ToXMLString() As String` method ToXMLString

# RecurringPostingsLineCollection (Collection)

RecurringPostingsLineCollection Class

## Properties (1)
- `Public Property Count() As Long` [R] Count

## Methods (6)
- `Public Function Add() As RecurringPostingsLine` method Add
- `Public Function GetXMLSchema() As String` method GetXMLSchema
- `Public Function Item(ByVal vtIndex As Variant) As RecurringPostingsLine` DISPID_VALUE
  - param `vtIndex`: 
- `Public Sub Remove(ByVal vtIndex As Variant)` method Remove
  - param `vtIndex`: 
- `Public Sub ToXMLFile(ByVal bstrFileName As String)` method ToXMLFile
  - param `bstrFileName`: 
- `Public Function ToXMLString() As String` method ToXMLString

# RecurringPostingsParams (Object)

RecurringPostingsParams Class

## Properties (3)
- `Public Property Code() As String` [R/W] property Code
- `Public Property Description() As String` [R] property Description
- `Public Property Instance() As Long` [R/W] property Instance

## Methods (5)
- `Public Sub FromXMLFile(ByVal bstrFileName As String)` method FromXMLFile
  - param `bstrFileName`: 
- `Public Sub FromXMLString(ByVal bstrXML As String)` method FromXMLString
  - param `bstrXML`: 
- `Public Function GetXMLSchema() As String` method GetXMLSchema
- `Public Sub ToXMLFile(ByVal bstrFileName As String)` method ToXMLFile
  - param `bstrFileName`: 
- `Public Function ToXMLString() As String` method ToXMLString

# RecurringPostingsParamsCollection (Collection)

RecurringPostingsParamsCollection Class

## Properties (1)
- `Public Property Count() As Long` [R] Count

## Methods (5)
- `Public Function Add() As RecurringPostingsParams` method Add
- `Public Function GetXMLSchema() As String` method GetXMLSchema
- `Public Function Item(ByVal vtIndex As Variant) As RecurringPostingsParams` DISPID_VALUE
  - param `vtIndex`: 
- `Public Sub ToXMLFile(ByVal bstrFileName As String)` method ToXMLFile
  - param `bstrFileName`: 
- `Public Function ToXMLString() As String` method ToXMLString

# RecurringPostingsService (Object)

RecurringPostingsService Class

## Methods (8)
- `Public Function Add(ByVal pIRecurringPostings As RecurringPostings) As RecurringPostingsParams` Add
  - param `pIRecurringPostings`: 
- `Public Sub Delete(ByVal pIRecurringPostingsParams As RecurringPostingsParams)` Delete
  - param `pIRecurringPostingsParams`: 
- `Public Function Get(ByVal pIRecurringPostingsParams As RecurringPostingsParams) As RecurringPostings` Get
  - param `pIRecurringPostingsParams`: 
- `Public Function GetDataInterface(ByVal enumMSDI As RecurringPostingsServiceDataInterfaces) As Object` GetDataInterface
  - param `enumMSDI`: one of the enumeration's values (see the enum file)
  - enum: `RecurringPostingsServiceDataInterfaces` in `../enums/enums-03.md`
- `Public Function GetDataInterfaceFromXMLFile(ByVal bstrFileName As String) As Object` GetDataInterfaceFromXMLFile
  - param `bstrFileName`: 
- `Public Function GetDataInterfaceFromXMLString(ByVal bstrXMLString As String) As Object` GetDataInterfaceFromXMLString
  - param `bstrXMLString`: 
- `Public Function GetList() As RecurringPostingsParamsCollection` GetList
- `Public Sub Update(ByVal pIRecurringPostings As RecurringPostings)` Update
  - param `pIRecurringPostings`: 

# RecurringTransactionService (Object)

RecurringTransactionService Class

## Methods (7)
- `Public Sub DeleteRecurringTransactions(ByVal pIRclRecurringTransactionParamsCollection As RclRecurringTransactionParamsCollection)` DeleteRecurringTransactions
  - param `pIRclRecurringTransactionParamsCollection`: 
- `Public Function ExecuteRecurringTransactions(ByVal pIRclRecurringTransactionParamsCollection As RclRecurringTransactionParamsCollection, ByVal pIRclRecurringExecutionParams As RclRecurringExecutionParams) As RclRecurringTransactionCollection` ExecuteRecurringTransactions
  - param `pIRclRecurringTransactionParamsCollection`: 
  - param `pIRclRecurringExecutionParams`: 
- `Public Function GetAvailableRecurringTransactions() As RclRecurringTransactionCollection` GetAvailableRecurringTransactions
- `Public Function GetDataInterface(ByVal enumMSDI As RecurringTransactionServiceDataInterfaces) As Object` GetDataInterface
  - param `enumMSDI`: one of the enumeration's values (see the enum file)
  - enum: `RecurringTransactionServiceDataInterfaces` in `../enums/enums-03.md`
- `Public Function GetDataInterfaceFromXMLFile(ByVal bstrFileName As String) As Object` GetDataInterfaceFromXMLFile
  - param `bstrFileName`: 
- `Public Function GetDataInterfaceFromXMLString(ByVal bstrXMLString As String) As Object` GetDataInterfaceFromXMLString
  - param `bstrXMLString`: 
- `Public Function GetRecurringTransaction(ByVal pIRclRecurringTransactionParams As RclRecurringTransactionParams) As RclRecurringTransaction` GetRecurringTransaction
  - param `pIRclRecurringTransactionParams`: 

# RelatedDocument (Object)

RelatedDocument Class

## Properties (3)
- `Public Property AbsEntry() As Long` [R/W] property AbsEntry
- `Public Property DocType() As RelatedDocumentTypeEnum` [R/W] property DocType
- `Public Property UUID() As String` [R] property UUID

## Methods (5)
- `Public Sub FromXMLFile(ByVal bstrFileName As String)` method FromXMLFile
  - param `bstrFileName`: 
- `Public Sub FromXMLString(ByVal bstrXML As String)` method FromXMLString
  - param `bstrXML`: 
- `Public Function GetXMLSchema() As String` method GetXMLSchema
- `Public Sub ToXMLFile(ByVal bstrFileName As String)` method ToXMLFile
  - param `bstrFileName`: 
- `Public Function ToXMLString() As String` method ToXMLString

# RelatedDocumentCollection (Collection)

RelatedDocumentCollection Class

## Properties (1)
- `Public Property Count() As Long` [R] Count

## Methods (5)
- `Public Function Add() As RelatedDocument` method Add
- `Public Function GetXMLSchema() As String` method GetXMLSchema
- `Public Function Item(ByVal vtIndex As Variant) As RelatedDocument` DISPID_VALUE
  - param `vtIndex`: 
- `Public Sub ToXMLFile(ByVal bstrFileName As String)` method ToXMLFile
  - param `bstrFileName`: 
- `Public Function ToXMLString() As String` method ToXMLString

# RelatedDocuments (Object)

RelatedDocuments Class

## Properties (4)
- `Public Property AbsEntry() As Long` [R/W] property AbsEntry
- `Public Property Count() As Long` [R] property Count
- `Public Property DocType() As RelatedDocumentTypeEnum` [R/W] property DocType
- `Public Property UUID() As String` [R] property UUID

## Methods (3)
- `Public Sub Add()` method Add
- `Public Sub Delete()` method Delete
- `Public Sub SetCurrentLine(ByVal LineNum As Long)` method SetCurrentLine
  - param `LineNum`: 

# Relationships (Object)

Relationships is a business object that represents the relationships list from which a relationship definition can be associated with a partner in a sales opportunity. This object enables you to: - Add a relationship to the list. - Retrieve a relationship by its key. - Update a relationship. - Save the object in XML format. Source table: OORL.

**Remarks:** To display the form in the application: - Select Sales Opportunities --> Sales Opportunity. - In the Partners tab, from the Relationship list box, select Define New. or - Select Administration --> Definition --> Sales Opportunities --> Define Relationships.

## Properties (4)
- `Public Property Browser() As DataBrowser` [R] Returns the DataBrowser object.
- `Public Property RelationshipCode() As Long` [R] Returns the relationship ID number. SAP Business One assigns this number when adding a relationship definition to the relationships list. Field name: OrlCode.
- `Public Property RelationshipDescription() As String` [R/W] Sets or returns the relationship description. Field name: OrlDesc. Length: 100 characters.
- `Public Property UserFields() As UserFields` [R] Returns the UserFields object.

## Methods (7)
- `Public Function Add() As Long` Adds a record to the object table in SAP Business One company database.
  - returns: Returns a result value that indicates success or failure. If the method succeeds, it returns 0. Otherwise, it returns an error code. You can retrieve the last error code and its description using the method GetLastError.
  - remarks: You must values for the mandatory properties, and then call the Add method. The auto-complete feature completes all the default values of the other properties. In the DI API, the auto-complete feature operates the same way as in the SAP Business One application.
- `Public Function GetAsXML() As String` Returns the object from XML data, which is stored as string in a buffer.
  - remarks: You can use this method for development technologies that do not support return value as an Out parameter, such as ASP. You do not have to set the XMLAsString property of the Company object.
- `Public Function GetByKey(ByVal lID As Long) As Boolean` Retrieves and sets the values of the object's properties by the object's absolute key from the Company database.
  - param `lID`: Relationship ID number (RelationshipCode).
  - returns: If the object with the key you specified is found, the method returns True and the properties of the object will be filled with object's data. If the object with the key you specified is not found, the method returns False and the properties of the object remain unchanged.
  - remarks: To use this method you must specify the object key. You can also use this method to find whether or not there is an object related to the key you specify. If you do not know the object key, you can use the DataBrowser object to retreive an object using more complex queries.
- `Public Function Remove() As Long` Deletes a record from the object table.
  - returns: Returns a result value that indicates success or failure. If the method succeeds, it returns 0. Otherwise, it returns an error code. You can retrieve the last error code and its description using the method GetLastError.
  - remarks: You must use the GetByKey method to retrieve a valid object.
- `Public Sub SaveToFile(ByVal FileName As String)` Save the object to a file as XML data.
  - param `FileName`: Specifies the path and file name of the XML data. Specifies the path and file name of the XML data.
  - remarks: You can use this method for development technologies that do not support return value as an Out parameter, such as ASP.
- `Public Sub SaveXML(ByRef FileName As String)` Saves the object data to XML formatted data.
  - param `FileName`: Specifies the path and file name of the XML data. Specifies the path and file name of the XML data.
  - remarks: You can use this method to save a business object to an XML file. Then, call the GetBusinessObjectFromXML method to load this object into memory again, for example, to copy customers from one database to another. To enable this operation, set the XmlExportType property of the Company object to xet_ValidNodesOnly. To use ReadXML method, set the XmlExportType to xet_ExportImportMode (3). For more information, see Exchanging Data Using the DI API XML Capabilities.
  - example note: The following sample shows how to save data of an object to an XML file. Use this sample as a basis to all business objects (both document and master data types).
  - VB example (SAP provides no C# sample for this - translate, don't paste):
    ```vb
    Dim vInvoice As SAPbobsCOM.Documents

    Set vInvoice = vCmp.GetBusinessObject(oInvoices)

    'Retrieve an invoice document from the database

    RetVal = vInvoice.GetByKey("1023")

    If RetVal <> 0 Then

         vCmp.GetLastError ErrCode, ErrMsg

         MsgBox "Failed to Retrieve the record " & ErrCode & " " & ErrMsg

         Exit Sub

    End If

    'Save the object as an xml file

    vInvoice.SaveXML ("C:\Program Files\SAP\XML\Invoice.xml")

    'Retrieve the object back from the XML file

    Set vInvoice = vCmp.GetBusinessObjectFromXML("C:\Program Files\SAP\XML\Invoice.xml", 0)
    ```
- `Public Function Update() As Long` Updates the object data in the company database.
  - returns: Returns a result value that indicates success or failure. If the method succeeds, it returns 0. Otherwise, it returns an error code. You can retrieve the last error code and its description using the method GetLastError.
  - remarks: Before using this method, you must use the GetByKey method to retrieve an existing record, and to set the values to the object mandatory properties. You can also use the SBObob object to browse lists of objects.

# ReportFilterService (Object)

The Report Filter Service is a business object that manages the information displaied by tax report. This object enables user to: - Add new Tax report filter to the service. - Delete a Tax report filter from the service. - Get a list of all Tax report filter Ids that exists in the service. - Update Tax report filter. - Get Data interfaces. Source table: OVTR.

**Remarks:** To use the service: - Connect to a valid company. - Call the CompanyService, which is the main DI service that you must call before using any other service. - Call the method GetBusinessService for the required service. - Create an empty data structure related to the required service. - or- You can create a data structure from an XML file or XML string. - Set the required properties of the specified data structure. - Call the required service method. To display the form in the application: - Select -- .

## Methods (8)
- `Public Function AddTaxReportFilter(ByVal pITaxReportFilter As TaxReportFilter) As TaxReportFilterParams` Adds new TaxReportFilter to the ReportFilterService Object.
  - param `pITaxReportFilter`: The TaxReportFilter Object you want to add.
  - example note: Add a new Filter that is based on an existing Filter
  - VB example (SAP provides no C# sample for this - translate, don't paste):
    ```vb
    Dim oTaxReportFilterParams As TaxReportFilterParams

    Dim oTaxReportFilter As TaxReportFilter

    'get a new Filter Params structure

    oTaxReportFilterParams = oTaxReportFilterService.GetDataInterface(ReportFilterServiceDataInterfaces.rfsdiTaxReportFilterParams)

    'set an existing Filter code

    oTaxReportFilterParams.Code = 4

    'get Report Filter

    oTaxReportFilter = oTaxReportFilterService.GetTaxReportFilter(oTaxReportFilterParams)

    'Change properties: set a new name

    oTaxReportFilter.Name = "My Filter"

    'add a new Filter

    Call oTaxReportFilterService.AddTaxReportFilter(oTaxReportFilter)
    ```
- `Public Sub DeleteTaxReportFilter(ByVal pITaxReportFilterParams As TaxReportFilterParams)` Delete the TaxReportFilter by it key.
  - param `pITaxReportFilterParams`: The TaxReportFilterParams identification key.
  - example note: Delete an existing Filter
  - VB example (SAP provides no C# sample for this - translate, don't paste):
    ```vb
    Dim oTaxReportFilterParams As TaxReportFilterParams

    Dim oTaxReportFilter As TaxReportFilter

    'get a new Filter Params structure

    oTaxReportFilterParams = oTaxReportFilterService.GetDataInterface(ReportFilterServiceDataInterfaces.rfsdiTaxReportFilterParams)

    'set an existing Filter code

    oTaxReportFilterParams.Code = 5

    'delete Filter

    Call oTaxReportFilterService.DeleteTaxReportFilter(oTaxReportFilterParams)
    ```
- `Public Function GetDataInterface(ByVal enumMSDI As ReportFilterServiceDataInterfaces) As Object` Creates an empty data structure. This means the structure contains the default setting/values of the database.
  - param `enumMSDI`: one of the enumeration's values (see the enum file)
  - enum: `ReportFilterServiceDataInterfaces` in `../enums/enums-03.md`
- `Public Function GetDataInterfaceFromXMLFile(ByVal bstrFileName As String) As Object` Creates an empty data structure defined by data from an XML file.
  - param `bstrFileName`: Specifies the path and file name of the XML data.
- `Public Function GetDataInterfaceFromXMLString(ByVal bstrXMLString As String) As Object` Creates an empty data structure defined by data from an XML string.
  - param `bstrXMLString`: Specifies the the XML string.
- `Public Function GetTaxReportFilter(ByVal pITaxReportFilterParams As TaxReportFilterParams) As TaxReportFilter` Get a TaxReportFilter by its TaxReportFilterParams identification key.
  - param `pITaxReportFilterParams`: TaxReportFilterParams identification key.
- `Public Function GetTaxReportFilterList(ByVal pITaxReportFilterParams As TaxReportFilterParams) As TaxReportFiltersParams` Returns a TaxReportFiltersParams object, a data collection of all the instances of TaxReportFilterParams Identification keys that match a given TaxReportFilterParams identification key.
  - param `pITaxReportFilterParams`: TaxReportFilterParams identification key.
  - example note: Get a list of Report Filter Params.
  - VB example (SAP provides no C# sample for this - translate, don't paste):
    ```vb
    Dim oTaxReportFiltersParams As TaxReportFiltersParams

    Dim oTaxReportFilter As TaxReportFilter

    Dim oTaxReportFilterParams As TaxReportFilterParams

    'get a new Filter Param structure

    oTaxReportFilterParams = oTaxReportFilterService.GetDataInterface(ReportFilterServiceDataInterfaces.rfsdiTaxReportFilterParams)

    'set the type of the requested filters

    oTaxReportFilterParams.FilterType =TaxReportFilterType.trft_SalesReport

    'get list of Report Filter Params

    oTaxReportFiltersParams = oTaxReportFilterService.GetTaxReportFilterList(oTaxReportFilterParams)

    'get the first Filter Params

    oTaxReportFilterParams = oTaxReportFiltersParams.Item(0)
    ```
- `Public Sub UpdateTaxReportFilter(ByVal pITaxReportFilter As TaxReportFilter)` Replace this TaxReportFilter Object with the target TaxReportFilter.
  - param `pITaxReportFilter`: The target TaxReportFilter Object.
  - example note: Update Report Filter
  - VB example (SAP provides no C# sample for this - translate, don't paste):
    ```vb
    Dim oTaxReportFilterParams As TaxReportFilterParams

    Dim oTaxReportFilter As TaxReportFilter

    'get a new Filter Params structure

    oTaxReportFilterParams = oTaxReportFilterService.GetDataInterface(ReportFilterServiceDataInterfaces.rfsdiTaxReportFilterParams)

    'set an existing Filter code

    oTaxReportFilterParams.Code = 5

    'get Report Filter

    oTaxReportFilter = oTaxReportFilterService.GetTaxReportFilter(oTaxReportFilterParams)

    'set a new name

    oTaxReportFilter.Name = "My Filter"

    'update Filter

    oTaxReportFilterService.UpdateTaxReportFilter(oTaxReportFilter)
    ```

# ReportLayout (Object)

Represents a layout for PLD or a layout/report for Crystal Reports. Source table: RDOC

**Remarks:** The ReportLayoutsService enables you to transfer PLD report layouts from one company to another. When transferring a system layout, change the following properties before adding the layout to the destination company: - Author: Change from System to a different name. If left unchanged, an exception is thrown. - Editable: Change from NO to Yes to make the new layout editable. - Name: Give the report layout a new name. When this object is used to import a layout/report for Crystal Reports, the fields Name, TypeCode, Author and Category must be set. Set Category to Crystal Reports and set TypeCode to either RCRI (for standalone reports) or a document type (for layouts).

## Properties (48)
- `Public Property AllignFooterToBottom() As BoYesNoEnum` [R/W] Determines whether or not to align layout report footer to page bottom. Field name: AlgnFooter.
- `Public Property Author() As String` [R/W] Sets or returns the name of layout report Author. Field name: Author. Length: 32 characters.
- `Public Property B1Version() As String` [R/W] The SAP Business One release number. Field name: B1Version
- `Public Property BottomMargin() As Long` [R/W] Sets or returns the size of the Bottom Margin of the layout Report. Field name: BMargin.
- `Public Property Category() As ReportLayoutCategoryEnum` [R/W] Indicates whether the report layout is a PLD or Crystal Reports layout. Field name: Category
- `Public Property ChangeFontSizeForEMail() As Long` [R/W] Sets or returns Font Size for email. Field name: EmFOffset.
- `Public Property ChangeFontSizeInPreview() As Long` [R/W] Sets or returns Font Size for layout Preview printing. Field name: ScrFOffset.
- `Public Property ConvertFontForEMail() As BoYesNoEnum` [R/W] Determines whether or not to convert font type for email. Field name: SwpInEmail.
- `Public Property ConvertFontInPrintPreview() As BoYesNoEnum` [R/W] Determines whether or not to convert font type for Print Preview. Field name: SwapOnScrn.
- `Public Property CRVersion() As String` [R/W] The Crystal Reports release number. Field name: CRVersion
- `Public Property Editable() As BoYesNoEnum` [R] Determines whether or not current report is editable. Field name: CanChange.
- `Public Property EMailFont() As String` [R/W] Sets or returns the font type currently used for email. Field name: EmailFont. Length: 50 characters.
- `Public Property ExtensionErrorAction() As BoExtensionErrorActionEnum` [R/W] Sets or returns current definition of the action to be taken upon printer extension error. Field name: ExtOnErr.
- `Public Property ExtensionName() As String` [R/W] Sets or returns current printer extension name. Field name: ExtName. Length: 16 characters.
- `Public Property FollowUpReport() As String` [R/W] Sets or returns Follow-Up Report. Field name: FollowCode.
- `Public Property ForeignLanguageReport() As BoYesNoEnum` [R/W] Determines whether or not to use Foreign Language Report. Field name: FrgnReport. FrgnReport
- `Public Property GridSize() As Long` [R/W] Sets or returns the vertical distance between two Grid points. Field name: GridSize.
- `Public Property GridType() As BoGridTypeEnum` [R/W] Sets or returns a valid value that determines the grid lines type in the reports layout: dots, or lines, or combination of dots and lines. Field name: GridType.
- `Public Property Height() As Long` [R/W] Sets or returns document hight. Field name: Height.
- `Public Property ImpExpObjCode() As Long` [R/W] Sets or returns the ImpExpObjCode value for the printer. Field name: RobjCode.
- `Public Property language() As Long` [R/W] Sets or returns the current printer language value. Field name: Language.
- `Public Property LayoutCode() As String` [R] The key of the report layout. Field name: DocCode
- `Public Property LeaderReport() As String` [R/W] Sets or returns the Leader Report value for the printer. Field name: LeaderCode. Length: 8 characters.
- `Public Property LeftMargin() As Long` [R/W] Sets or returns the LMargin value of the report layout. Field name: LMargin.
- `Public Property Localization() As String` [R/W] The localization assigned to the layout. Field name: Local
- `Public Property Name() As String` [R/W] Sets or returns the Document's Name value. Field name: DocName
- `Public Property NumberOfCopies() As Long` [R/W] The number of printed copies. Field name: NumCopy
- `Public Property Orientation() As BoOrientationEnum` [R/W] Determines the printer's orintation (Vertical or Horizontal). Field name: Oreint.
- `Public Property PaperSize() As String` [R/W] Sets or returns printer's Paper Size. Field name: PaperSize. Length: 100 characters.
- `Public Property Picture() As String` [R/W] Sets or returns a string that defines the path and name of the picture. Field name: Picture. Length: 16 characters.
- `Public Property PreviewPrintingFont() As String` [R/W] Sets or returns the name of the selected font to be Previewed upon screen. Length: 50 characters. Field name: ScreenFont.
- `Public Property Printer() As String` [R/W] The printer assigned to the layout. Field name: Printer.
- `Public Property PrinterFirstPage() As String` [R/W] The printer for the first page of a layout. Field name: Prtr1st
- `Public Property Query() As String` [R/W] Sets or returns query text. Field name: QString. Length: 16 characters.
- `Public Property QueryType() As BoQueryTypeEnum` [R/W] Sets or returns a valid value that determines wether Query type is Wizard or Regular. Length: 1 character. Field name: QType.
- `Public Property Remarks() As String` [R/W] Set or returns the the content of the remark used by the remark property of the printer. Field name: Notes. Length 254 characters.
- `Public Property RepetitiveAreasNumber() As Long` [R] Set or returns the number of Repetitive Areas property. Field name: NumRepArs.
- `Public Property ReportLayoutItems() As ReportLayoutItems` [R/W] Set or returns the ReportLayoutItems Object.
- `Public Property RightMargin() As Long` [R/W] Sets or returns the RMargin value of the report layout. Field name: RMargin.
- `Public Property ShowGrid() As BoYesNoEnum` [R/W] Determines whether to display or hide a grid in the report layout. Field name: ShowGrid.
- `Public Property SnapToGrid() As BoYesNoEnum` [R/W] Determines whether or not to use the printer grid alignment property for current report. Field name: SnapGrid.
- `Public Property Sortable() As BoYesNoEnum` [R] Determines whether or not to use the printer Sortable property for current report. Field name: CanSort.
- `Public Property TopMargin() As Long` [R/W] Sets or returns the TMargin value of the report layout. Field name: TMargin.
- `Public Property TranslationLines() As ReportLayout_TranslationLines` [R] property TranslationLines
- `Public Property TypeCode() As String` [R/W] Sets or returns the TypeCode property of the printer. Field name: TypeCode. Length 4 characters. This is a foreign key to the RTYP table.
- `Public Property TypeDetail() As String` [R/W] property TypeDetail
- `Public Property UseFirstPrinter() As BoYesNoEnum` [R/W] Indicates whether to use the first printer. Field name: Use1stPrtr
- `Public Property Width() As Long` [R/W] Sets or returns document width. Field name: TypeCode.

## Methods (5)
- `Public Sub FromXMLFile(ByVal bstrFileName As String)` Sets the object's properties using data from an XML file. The XML file can be created using the object's ToXMLFile method.
  - param `bstrFileName`: Specifies the the XML file. The path and name of the XML file from which to retrieve the object's data.
- `Public Sub FromXMLString(ByVal bstrXML As String)` Sets the object's properties using data from an XML string. The XML string can be created using the object's ToXMLString method.
  - param `bstrXML`: Specifies the the XML string. The XML from which to retrieve the object's data.
- `Public Function GetXMLSchema() As String` Retrieves the XML schema of the data structure. Returns the XML schema for the XML generated by the ToXMLFile and ToXMLString methods.
- `Public Sub ToXMLFile(ByVal bstrFileName As String)` Creates an XML file that represents the object data. Creates an XML file that represents the object.
  - param `bstrFileName`: Specifies the XML file name including path. The path and file name of the XML file.
  - remarks: The schema of the XML can be retrieved with the GetXMLSchema method.
- `Public Function ToXMLString() As String` Creates an XML string that represents the object data. Creates and returns an XML string that represents the object.
  - remarks: The schema of the XML can be retrieved with the GetXMLSchema method.

# ReportLayout_TranslationLine (Object)

ReportLayout_TranslationLine Class

## Properties (8)
- `Public Property CreateDate() As Date` [R/W] property CreateDate
- `Public Property CreateTime() As Long` [R/W] property CreateTime
- `Public Property DocEntry() As String` [R] property DocEntry
- `Public Property DocName() As String` [R/W] property DocName
- `Public Property LanguageCode() As Long` [R/W] property LanguageCode
- `Public Property LineNumber() As Long` [R] property LineNumber
- `Public Property UpdateDate() As Date` [R/W] property UpdateDate
- `Public Property UpdateTime() As Long` [R/W] property UpdateTime

## Methods (5)
- `Public Sub FromXMLFile(ByVal bstrFileName As String)` method FromXMLFile
  - param `bstrFileName`: 
- `Public Sub FromXMLString(ByVal bstrXML As String)` method FromXMLString
  - param `bstrXML`: 
- `Public Function GetXMLSchema() As String` method GetXMLSchema
- `Public Sub ToXMLFile(ByVal bstrFileName As String)` method ToXMLFile
  - param `bstrFileName`: 
- `Public Function ToXMLString() As String` method ToXMLString

# ReportLayout_TranslationLines (Collection)

ReportLayout_TranslationLines Class

## Properties (1)
- `Public Property Count() As Long` [R] Count

## Methods (6)
- `Public Function Add() As ReportLayout_TranslationLine` method Add
- `Public Function GetXMLSchema() As String` method GetXMLSchema
- `Public Function Item(ByVal vtIndex As Variant) As ReportLayout_TranslationLine` DISPID_VALUE
  - param `vtIndex`: 
- `Public Sub Remove(ByVal vtIndex As Variant)` method Remove
  - param `vtIndex`: 
- `Public Sub ToXMLFile(ByVal bstrFileName As String)` method ToXMLFile
  - param `bstrFileName`: 
- `Public Function ToXMLString() As String` method ToXMLString

# ReportLayoutItem (Object)

Represents an element in a PLD report layout. Source table: RITM

## Properties (69)
- `Public Property BackgroundBlue() As Long` [R/W] Sets or returns the intensity (0 - 255) of the blue component (RGB) of the background layout item. Field name: BGBlue.
- `Public Property BackgroundGreen() As Long` [R/W] Sets or returns the intensity (0 - 255) of the Green component (RGB) of the background layout item. Field name: BGGreen.
- `Public Property BackgroundRed() As Long` [R/W] Sets or returns the intensity (0 - 255) of the red component (RGB) of the background layout item. Field name: BGRed.
- `Public Property BarCodeStandard() As BoBarCodeStandardEnum` [R/W] Determines whether or not to display barcode in standard mode. Field name: ExcFonting.)
- `Public Property BlockFontChange() As BoYesNoEnum` [R/W] Determines whether or not to block font type changes.
- `Public Property BorderBlue() As Long` [R/W] Sets or returns the intensity (0 - 255) of the blue component (RGB) of the border line layout item. Field name: BrdrBlue.)
- `Public Property BorderGreen() As Long` [R/W] Sets or returns the intensity (0 - 255) of the Green component (RGB) of the border line layout item. Field name: BrdrGreen.)
- `Public Property BorderRed() As Long` [R/W] Sets or returns the intensity (0 - 255) of the Red component (RGB) of the border line layout item. Field name: BrdrRed.)
- `Public Property BottomBorderLineThickness() As Long` [R/W] Sets or returns the thickness of the bottom border line. Field name: BottomLine.)
- `Public Property BottomMargin() As Long` [R/W] Sets or returns the size of the bottom margin. Field name: BMargin.)
- `Public Property DataSource() As BoDataSourceEnum` [R/W] Field name: DataSource.
- `Public Property DisplayDescription() As BoYesNoEnum` [R/W] Field name: ShowDescr.
- `Public Property DisplayRepetitiveAreaFooterOnAllPages() As BoYesNoEnum` [R/W] Sets or returns a valid value that determines whether or not to display the repetitive area in the footer of all pages in the report.
- `Public Property DisplayTotalAsAWord() As BoYesNoEnum` [R/W] Field name: SumInWords.
- `Public Property DistanceToRepetitiveDuplicate() As Long` [R/W] Sets or returns the distance to repetitive duplication. Field name: RptDupDist.
- `Public Property DuplicateRepetitiveArea() As BoYesNoEnum` [R/W] Determines whether or not to duplicate a repetitive area. Field name: DupRpttAre.)
- `Public Property Editable() As Long` [R/W] Sets or returns the permission to edit a field.
- `Public Property FieldIdentifier() As String` [R/W] Sets or returns a field unique ID. Field name: FieldId.)
- `Public Property FieldName() As String` [R/W] Sets or returns the field name. Field name: FieldNum. Length: 20 characters.
- `Public Property FontName() As String` [R/W] Sets or returns active font name. Field name: FontName.) Length: 50 characters.
- `Public Property FontSize() As Long` [R/W] Sets or returns current Font Size Layout Item. Field name: FontSize.)
- `Public Property GroupNumber() As Long` [R/W] Field name: ItemGroup.
- `Public Property Height() As Long` [R/W] Field name: HightAdjst.
- `Public Property HeightAdjustments() As BoYesNoEnum` [R/W] Sets or returns a valid value that determines wether or not to adjust the field hight. Field name: HightAdjst.
- `Public Property HideRepetitiveAreaIfEmpty() As BoYesNoEnum` [R/W] Sets or returns a valid value that determines whether or not to hide the repetitive area if the it is empty in the report.
- `Public Property HighlightBlue() As Long` [R/W] Sets or returns the intensity (0 - 255) of the blue component (RGB) of the Foreground layout item. Field name: FGBlue.
- `Public Property HighlightGreen() As Long` [R/W] Sets or returns the intensity (0 - 255) of the green component (RGB) of the Foreground layout item. Field name: FGGreen.
- `Public Property HighlightRed() As Long` [R/W] Sets or returns the intensity (0 - 255) of the red component (RGB) of the Foreground layout item. Field name: FGRed.
- `Public Property HorizontalAlignment() As BoHorizontalAlignmentEnum` [R/W] Sets or returns a valid value that determines the field horizontal alignment (justification). Field name: Justific.
- `Public Property ItemIndex() As Long` [R/W] Field name: ItemIndex.
- `Public Property ItemNumber() As Long` [R/W] Field name: ApplID.
- `Public Property Left() As Long` [R/W] Set or returns the report Left margin. Field name ItemLeft.
- `Public Property LeftBorderLineThickness() As Long` [R/W] Sets or returns left border line thickness. Field name: LeftLine.)
- `Public Property LeftMargin() As Long` [R/W] Sets or returns the left margin size. Field name: LMargin.)
- `Public Property LineBreak() As BoLineBreakEnum` [R/W] Sets or returns a valid value that determines line break type.
- `Public Property LinkToField() As String` [R/W] Field name: LinkTo. Length: 20 characters.
- `Public Property NewPage() As BoYesNoEnum` [R/W] Determines whether or not to use new page. Field name: NewPage.)
- `Public Property NextSegmentItemNumber() As String` [R/W] Sets or returns the next segment item number. Field name: NextSeg.) Length: 20 characters.
- `Public Property NumberOfLinesInRepetitiveArea() As Long` [R/W] Sets or returns the number of Lines in Repetitive Area. Field name: LnsRpttAre.)
- `Public Property ParentIndex() As Long` [R/W] Sets or returns the Container Index. Field name: ContIndex.
- `Public Property ParentType() As Long` [R/W] Sets or returns Parent Type. Field name: Container.)
- `Public Property PictureSize() As BoPictureSizeEnum` [R/W] Sets or returns Selected Picture Size. Field name: PictSize.)
- `Public Property PrintAsBarCode() As BoYesNoEnum` [R/W] Determines whether or not to print in Bar Code format. Field name: BarCode.)
- `Public Property RelateToField() As String` [R/W] Sets or returns a Link to a Field. Field name: RelatedTo.) Length: 20 characters.
- `Public Property ReverseSort() As BoYesNoEnum` [R/W] Determines whether or not to sort a list in reverse order. Field name: RevOrder.)
- `Public Property RightBorderLineThickness() As Long` [R/W] Sets or returns right border line thickness. Field name: RightLine.)
- `Public Property RightMargin() As Long` [R/W] Sets or returns the Right Margin. Field name: RMargin.)
- `Public Property SetAsGroup() As BoYesNoEnum` [R/W] Determines whether or not to set Items as Group. Field name: IsGroup.)
- `Public Property ShadowThickness() As Long` [R/W] Sets or returns the Shadow Thickness value. Field name: Shadow.)
- `Public Property SortLevel() As Long` [R/W] Sets or returns Sort Level. Field name: SortLevel.)
- `Public Property SortType() As BoSortTypeEnum` [R/W] Sets or returns Sort Types (enumeration). Field name: SortType.)
  - remarks: Possible values are: - 0 Alpha - 1 Value - 2 Money - 3 Date
- `Public Property String() As String` [R/W] Sets or returns the Item String. Field name: ItemStr.) Length: 16 characters.
- `Public Property StringFiller() As String` [R/W] Sets or returns the character used as String Filler. Field name: StrFiller.)
- `Public Property StringLength() As Long` [R/W] Sets or returns the length of active string. Field name: StrLength.)
- `Public Property SuppressZeros() As BoYesNoEnum` [R/W] Determines whether or not to suppress zeros in active field. Field name: SupZeros.)
- `Public Property TableName() As String` [R/W] Sets or returns the table name. Field name: FileName. Length: 20 characters.
- `Public Property TextBlue() As Long` [R/W] Sets or returns the intensity (0 - 255) of the blue component (RGB) of active text. Field name: FGBlue.)
- `Public Property TextGreen() As Long` [R/W] Sets or returns the intensity (0 - 255) of the Green component (RGB) of active text. Field name: FGGreen.)
- `Public Property TextRed() As Long` [R/W] Sets or returns the intensity (0 - 255) of the Red component (RGB) of active text. Field name: FGRed.)
- `Public Property TextStyle() As Long` [R/W] Sets or returns the active Text style. Field name: TextStyle.)
- `Public Property Top() As Long` [R/W] Sets or returns the report Top margin. Field name: ItemTop.)
- `Public Property TopBorderLineThickness() As Long` [R/W] Sets or returns the line thickness of the Top Border Layout Item. Field name: TopLine.)
- `Public Property TopMargin() As Long` [R/W] Sets or returns the Top Margin width. Field name: TMargin.)
- `Public Property Type() As BoReportLayoutItemTypeEnum` [R/W] Sets or returns the type of the layout item, such as Page Header, Start of Report, and Picture Field. Field name: Type.)
- `Public Property Unique() As BoYesNoEnum` [R/W] Field name: IsUnique.
- `Public Property VariableNumber() As Long` [R/W] Sets or returns the Variable No. Layout Item. Field name: VarNum.)
- `Public Property VerticalAlignment() As BoVerticalAlignmentEnum` [R/W] Determines whether or not to use Vertical Alignment Layout Item. Field name: YJustific.)
- `Public Property Visible() As BoYesNoEnum` [R/W] Determines whether or not to use Visible Layout Item. Field name: VISIBLE.)
- `Public Property Width() As Long` [R/W] Sets or returns the report Width. Field name: Width.)

## Methods (5)
- `Public Sub FromXMLFile(ByVal bstrFileName As String)` Sets the object's properties using data from an XML file. The XML file can be created using the object's ToXMLFile method.
  - param `bstrFileName`: The path and name of the XML file from which to retrieve the object's data.
- `Public Sub FromXMLString(ByVal bstrXML As String)` Sets the object's properties using data from an XML string. The XML string can be created using the object's ToXMLString method.
  - param `bstrXML`: The XML from which to retrieve the object's data.
- `Public Function GetXMLSchema() As String` Retrieves the XML schema of the data structure. Returns the XML schema for the XML generated by the ToXMLFile and ToXMLString methods.
- `Public Sub ToXMLFile(ByVal bstrFileName As String)` Creates an XML string that represents the object data. Creates an XML file that represents the object.
  - param `bstrFileName`: The path and file name of the XML file.
  - remarks: The schema of the XML can be retrieved with the GetXMLSchema method.
- `Public Function ToXMLString() As String` Creates an XML string that represents the object data. Creates and returns an XML string that represents the object.
  - remarks: The schema of the XML can be retrieved with the GetXMLSchema method.

# ReportLayoutItems (Collection)

A collection of ReportLayoutItem objects.

## Properties (1)
- `Public Property Count() As Long` [R] Returns the number of objects in the collection.

## Methods (5)
- `Public Function Add() As ReportLayoutItem` Adds an empty object to the collection.
  - remarks: After an object is added to this collection, the database is not automatically updated. You must then update the GeneralData object to which this collection belongs, by executing the Update method of the GeneralService service.
- `Public Function GetXMLSchema() As String` Returns the XML schema for the XML generated by the ToXMLFile and ToXMLString methods.
- `Public Function Item(ByVal vtIndex As Variant) As ReportLayoutItem` Returns the object at the specified index.
  - param `vtIndex`: The index of the object to be returned (0-based)
- `Public Sub ToXMLFile(ByVal bstrFileName As String)` Creates an XML file that represents the object.
  - param `bstrFileName`: The path and file name of the XML file.
  - remarks: The schema of the XML can be retrieved with the GetXMLSchema method.
- `Public Function ToXMLString() As String` Creates and returns an XML string that represents the object.
  - remarks: The schema of the XML can be retrieved with the GetXMLSchema method.

# ReportLayoutParams (Object)

Holds the key, name, and type of report/report layout. This object is used to pass keys to and retrieve keys from ReportLayoutsService methods.

## Properties (3)
- `Public Property Category() As ReportLayoutCategoryEnum` [R] Indicates whether the report/report layout is for PLD or Crystal Reports. Field name: Category
- `Public Property LayoutCode() As String` [R/W] The report/report layout unique ID. Field name: DocCode
- `Public Property LayoutName() As String` [R] The report/report layout name. Field name: DocName

## Methods (5)
- `Public Sub FromXMLFile(ByVal bstrFileName As String)` Sets the object's properties using data from an XML file. The XML file can be created using the object's ToXMLFile method.
  - param `bstrFileName`: The path and name of the XML file from which to retrieve the object's data.
- `Public Sub FromXMLString(ByVal bstrXML As String)` Sets the object's properties using data from an XML string. The XML string can be created using the object's ToXMLString method.
  - param `bstrXML`: The XML from which to retrieve the object's data.
- `Public Function GetXMLSchema() As String` Retrieves the XML schema of the ReportLayout data structure. Returns the XML schema for the XML generated by the ToXMLFile and ToXMLString methods.
- `Public Sub ToXMLFile(ByVal bstrFileName As String)` Creates an XML file that represents the object.
  - param `bstrFileName`: The path and file name of the XML file.
  - remarks: The schema of the XML can be retrieved with the GetXMLSchema method.
- `Public Function ToXMLString() As String` Creates and returns an XML string that represents the object.
  - remarks: The schema of the XML can be retrieved with the GetXMLSchema method.

# ReportLayoutPrintParams (Object)

ReportLayoutPrintParams Class

## Properties (2)
- `Public Property DocEntry() As Long` [R/W] property DocEntry
- `Public Property LayoutCode() As String` [R/W] property LayoutCode

## Methods (5)
- `Public Sub FromXMLFile(ByVal bstrFileName As String)` method FromXMLFile
  - param `bstrFileName`: 
- `Public Sub FromXMLString(ByVal bstrXML As String)` method FromXMLString
  - param `bstrXML`: 
- `Public Function GetXMLSchema() As String` method GetXMLSchema
- `Public Sub ToXMLFile(ByVal bstrFileName As String)` method ToXMLFile
  - param `bstrFileName`: 
- `Public Function ToXMLString() As String` method ToXMLString

# ReportLayoutsParams (Collection)

A collection of ReportLayoutParams objects.

## Properties (1)
- `Public Property Count() As Long` [R] Returns the number of objects in the collection.

## Methods (5)
- `Public Function Add() As ReportLayoutParams` Adds an empty object to the collection.
  - remarks: After an object is added to this collection, the database is not automatically updated. You must then update the GeneralData object to which this collection belongs, by executing the Update method of the GeneralService service.
- `Public Function GetXMLSchema() As String` Returns the XML schema for the XML generated by the ToXMLFile and ToXMLString methods.
- `Public Function Item(ByVal vtIndex As Variant) As ReportLayoutParams` Returns the object at the specified index.
  - param `vtIndex`: The index of the object to be returned (0-based)
- `Public Sub ToXMLFile(ByVal bstrFileName As String)` Creates an XML file that represents the object.
  - param `bstrFileName`: The path and file name of the XML file.
  - remarks: The schema of the XML can be retrieved with the GetXMLSchema method.
- `Public Function ToXMLString() As String` Creates and returns an XML string that represents the object.
  - remarks: The schema of the XML can be retrieved with the GetXMLSchema method.

# ReportLayoutsService (Object)

The ReportLayoutsService service enables you to do the following: - Copy a PLD report layout from one company to another. - Add a Crystal Reports layout or standalone report. Source table: RDOC (report layouts) and RDFL (associates default report with user, business partners)

**Remarks:** To work with report layouts in SAP Business One: - Open a marketing document form (for example, Sales A/R -- Sales Quotation). - Select Tools --> Print Layout Designer (or select the pencil icon on the toolbar). The Layout Designer - Selection Criteria form opens. - Click Edit. The Report and Layout Manager opens. To work with the Print Layout Designer: - Open the Report and Layout Manager, as described above. - Select a PLD report layout. - Click Edit.

## Methods (15)
- `Public Function AddReportLayout(ByVal pIReportLayout As ReportLayout) As ReportLayoutParams` Adds a new report/report layout.
  - param `pIReportLayout`: The data for the new report/report layout.
  - returns: Contains the key (DocCode) of the new report/report layout.
  - remarks: For Crystal Reports, use this method to add a report (as a standalone report or as a report layout) by setting the fields Name, TypeCode, Author and Category of the ReportLayout object. Set Category to Crystal Reports and set TypeCode to either RCRI (for standalone report) or a document type (for report layouts). For PLD report layouts, use this only to transfer report layouts from one company to another. When transferring a system layout, change the following properties before adding the layout to the destination company: - Author: Change from System to a different name. If left unchanged, an exception is thrown. - Editable: Change from NO to Yes to make the new layout editable. - Name: Give the report layout a new name. Do not change any other properties.
  - VB example (SAP provides no C# sample for this - translate, don't paste):
    ```vb
    Dim oCmpSrv As SAPbobsCOM.CompanyService

    Dim oReportLayoutService As ReportLayoutsService

    Dim oReportLayout As ReportLayout

    Dim oReportLayoutParam As ReportLayoutParams

    'Get report layout service

    oCmpSrv = oCompany.GetCompanyService

    oReportLayoutService = oCmpSrv.GetBusinessService(ServiceTypes.ReportLayoutsService)

    'Set parameters

    oReportLayoutParam = oReportLayoutService.GetDataInterface(ReportLayoutsServiceDataInterfaces.rlsdiReportLayoutParams)

    oReportLayoutParam.LayoutCode = "POR20002"

    'Get report layout

    oReportLayout = oReportLayoutService.GetReportLayout(oReportLayoutParam)

    'Add report layout

    oReportLayoutService.AddReportLayout(oReportLayout)
    ```
- `Public Function AddReportLayoutToMenu(ByVal ppIReportLayout As ReportLayout, ByVal MenuID As String) As ReportLayoutParams` 
  - param `ppIReportLayout`: 
  - param `MenuID`: 
- `Public Sub DeleteReportLayout(ByVal pIReportLayoutParams As ReportLayoutParams)` 
  - param `pIReportLayoutParams`: A pointer to a ReportLayoutParams object.
  - VB example (SAP provides no C# sample for this - translate, don't paste):
    ```vb
    Dim oCmpSrv As SAPbobsCOM.CompanyService

    Dim oReportLayoutService As ReportLayoutsService

    Dim oReportLayoutParams As ReportLayoutParams

    'Get report layout service

    oCmpSrv = oCompany.GetCompanyService

    oReportLayoutService = oCmpSrv.GetBusinessService(ServiceTypes.ReportLayoutsService)

    'Set parameters

    oReportLayoutParams = oReportLayoutService.GetDataInterface(ReportLayoutsServiceDataInterfaces.rlsdiReportLayoutParams)

    oReportLayoutParams.LayoutCode = "POR20002"

    'Delete report layout

    oReportLayoutService.DeleteReportLayout(oReportLayoutParams)
    ```
- `Public Sub DeleteReportLayoutAndMenu(ByVal ppIReportLayoutParams As ReportLayoutParams)` 
  - param `ppIReportLayoutParams`: 
- `Public Function GetDataInterface(ByVal enumMSDI As ReportLayoutsServiceDataInterfaces) As Object` Creates an empty data structure for use with the ReportLayoutsService.
  - param `enumMSDI`: one of the enumeration's values (see the enum file)
  - enum: `ReportLayoutsServiceDataInterfaces` in `../enums/enums-03.md`
- `Public Function GetDataInterfaceFromXMLFile(ByVal bstrFileName As String) As Object` Creates an object from an XML file.
  - param `bstrFileName`: The path and name of the XML file with which to create the object.
  - remarks: The XML file can be created using an object's ToXMLFile method. The XML file defines the object and its data.
  - example note: Shows how to get a Report Layout from an XML file.
  - C# example (from SAP's help):
    ```csharp
    public void AddFromXMLFile(Hashtable Properties, String Path)
    {
        //Store GeneralData object as XML
        SAPbobsCOM.GeneralService oGeneralService;
        SAPbobsCOM.GeneralData oGeneralData;
        SAPbobsCOM.GeneralData oGeneralDataXML;

        oGeneralService = cConnection.Instance.DICompanyService.GetGeneralService(UDOID);
        oGeneralData = (GeneralData)oGeneralService.GetDataInterface(GeneralServiceDataInterfaces.gsGeneralData);

        foreach (DictionaryEntry Pair In Properties)
            oGeneralData.SetProperty(Pair.Key.ToString(), Pair.Value.ToString());

        oGeneralData.ToXMLFile(Path);

        //Retrieve XML and create GeneralData object from the XML
        oGeneralDataXML = (GeneralData)oGeneralService.GetDataInterfaceFromXMLFile(Path);
        oGeneralService.Add(oGeneralDataXML);
    }
    ```
- `Public Function GetDataInterfaceFromXMLString(ByVal bstrXMLString As String) As Object` Creates an object from XML.
  - param `bstrXMLString`: The XML with which to create the object.
  - remarks: The XML can be created using an object's ToXMLString method. The XML defines the object and its data.
  - example note: Shows how to get a Report Layout from an XML string.
  - C# example (from SAP's help):
    ```csharp
    public void AddFromXMLString(Hashtable Properties)
    {
        //Store GeneralData object as XML
        SAPbobsCOM.GeneralService oGeneralService;
        SAPbobsCOM.GeneralData oGeneralData;
        SAPbobsCOM.GeneralData oGeneralDataXML;
        string XMLString;

        oGeneralService = cConnection.Instance.DICompanyService.GetGeneralService(UDOID);
        oGeneralData = (GeneralData)oGeneralService.GetDataInterface(GeneralServiceDataInterfaces.gsGeneralData);

        foreach (DictionaryEntry Pair in Properties)
            oGeneralData.SetProperty(Pair.Key.ToString(), Pair.Value.ToString());

        XMLString = oGeneralData.ToXMLString();

        //Retrieve XML string and create GeneralData object from the XML
        oGeneralDataXML = (GeneralData)oGeneralService.GetDataInterfaceFromXMLString(XMLString);
        oGeneralService.Add(oGeneralDataXML);
    }
    ```
- `Public Function GetDefaultReport(ByVal pIReportParams As ReportParams) As DefaultReportParams` Retrieves the default report layout for a specific document type.
  - param `pIReportParams`: Specifies a document type, as well as a user or business partner, for which to retrieve the default report layout.
  - remarks: This method is similar to the GetDefaultReportLayout method, except that this method returns the key to the report layout and not the ReportLayout object for the report layout.
  - VB example (SAP provides no C# sample for this - translate, don't paste):
    ```vb
    Dim oCmpSrv As SAPbobsCOM.CompanyService

    Dim oReportLayoutService As ReportLayoutsService

    Dim oReportParam As ReportParams

    Dim oReportParaDefault As DefaultReportParams

    'Get report layout service

    oCmpSrv = oCompany.GetCompanyService

    oReportLayoutService = oCmpSrv.GetBusinessService(ServiceTypes.ReportLayoutsService)

    'Set parameters

    oReportParam = oReportLayoutService.GetDataInterface(ReportLayoutsServiceDataInterfaces.rlsdiReportParams)

    oReportParam.ReportCode = "POR2"

    'Get default layout for specific document (Purchase Order)

    oReportParaDefault = oReportLayoutService.GetDefaultReport(oReportParam)

    'Print the layout code

    Debug.WriteLine(oReportParaDefault.LayoutCode)
    ```
- `Public Function GetDefaultReportLayout(ByVal pIReportParams As ReportParams) As ReportLayout` Retrieves the default report layout for a specific document type.
  - param `pIReportParams`: Specifies a document type, as well as a user or business partner, for which to retrieve the default report layout.
  - remarks: This method is similar to the GetDefaultReport method, except that this method returns the ReportLayout object for the report layout and not just the key.
  - VB example (SAP provides no C# sample for this - translate, don't paste):
    ```vb
    Dim oCmpSrv As SAPbobsCOM.CompanyService

    Dim oReportLayoutService As ReportLayoutsService

    Dim oReportLayout As ReportLayout

    Dim oReportParam As ReportParams

    'Get report layout  service

    oCmpSrv = oCompany.GetCompanyService

    oReportLayoutService =     oCmpSrv.GetBusinessService(ServiceTypes.ReportLayoutsService)

    'Set parameters

    oReportParam = oReportLayoutService.GetDataInterface(ReportLayoutsServiceDataInterfaces.rlsdiReportParams)

    oReportParam.ReportCode = "POR2"

    'Get the default layout for the specific document

    oReportLayout = oReportLayoutService.GetDefaultReportLayout(oReportParam)

    'Print the report layout name

    Debug.WriteLine(oReportLayout.Name)
    ```
- `Public Function GetReportLayout(ByVal pIReportLayoutParams As ReportLayoutParams) As ReportLayout` Retrieves a report layout.
  - param `pIReportLayoutParams`: The key of the report layout to retrieve.
  - returns: The report layout with the specified key.
  - VB example (SAP provides no C# sample for this - translate, don't paste):
    ```vb
    Dim oCmpSrv As SAPbobsCOM.CompanyService

    Dim oReportLayoutService As ReportLayoutsService

    Dim oReportLayoutParam As ReportLayoutParams

    Dim oReportLayout As ReportLayout

    'Get report layout service

    oCmpSrv = oCompany.GetCompanyService

    oReportLayoutService = oCmpSrv.GetBusinessService(ServiceTypes.ReportLayoutsService)

    'Set parameters

    oReportLayoutParam = oReportLayoutService.GetDataInterface(ReportLayoutsServiceDataInterfaces.rlsdiReportLayoutParams)

    oReportLayoutParam.LayoutCode = "POR20002"

    'Get the report layout

    oReportLayout = oReportLayoutService.GetReportLayout(oReportLayoutParam)

    'Print the report layout name

    Debug.WriteLine(oReportLayout.Name)
    ```
- `Public Function GetReportLayoutList(ByVal pIReportParams As ReportParams) As ReportLayoutsParams` Retrieves the keys and names of all the report layouts.
  - param `pIReportParams`: Specifies the report layouts to retrieve.
- `Public Sub Print(ByVal ppIReportLayoutPrintParams As ReportLayoutPrintParams)` 
  - param `ppIReportLayoutPrintParams`: 
- `Public Sub SetDefaultReport(ByVal ppIDefaultReportParams As DefaultReportParams)` Sets the specified report layout as default for a specific document type.
  - param `ppIDefaultReportParams`: Specifies a report to set as the default for a specific document type.
  - VB example (SAP provides no C# sample for this - translate, don't paste):
    ```vb
    Dim oCmpSrv As SAPbobsCOM.CompanyService

    Dim oReportLayoutService As ReportLayoutsService

    Dim oDefaultReportParams As DefaultReportParams

    'Get report layout service

    oCmpSrv = oCompany.GetCompanyService

    oReportLayoutService = oCmpSrv.GetBusinessService(ServiceTypes.ReportLayoutsService)

    'Set parameters

    oDefaultReportParams = oReportLayoutService.GetDataInterface(ReportLayoutsServiceDataInterfaces.rlsdiDefaultReportParams)

    oDefaultReportParams.LayoutCode = "POR20005"

    oDefaultReportParams.ReportCode = "POR2"

    oDefaultReportParams.UserID = 1

    'Set the report as default

    oReportLayoutService.SetDefaultReport(oDefaultReportParams)
    ```
- `Public Sub UpdateLanguageReport(ByVal ppIReportLayout As ReportLayout)` 
  - param `ppIReportLayout`: 
- `Public Sub UpdatePrinterSettings(ByVal pIReportLayout As ReportLayout)` 
  - param `pIReportLayout`: 

# ReportParams (Object)

Indicates which reports to retrieve, for example in the GetDefaultReport method of the ReportLayoutsService. ReportParams can specify reports based on the following parameters: - Business partner for whom the report was created - Report code - User who created the report

## Properties (3)
- `Public Property CardCode() As String` [R/W] The business partner to which the report layout is assigned. If blank, the report layout is assigned to all business partners. Field name: CardCode Length: 15 characters This is a foreign key to the BusinessPartners object.
- `Public Property ReportCode() As String` [R/W] The document type for which the report layout is assigned. Field name: DoumntDode Length: 4 characters
- `Public Property UserID() As Long` [R/W] The user to whom the report layout is assigned. If blank, the report layout is assigned to all users. Field name: UserId Length: 11 characters Returns the identification key of the active user who operates the system.

## Methods (5)
- `Public Sub FromXMLFile(ByVal bstrFileName As String)` Sets the object's properties using data from an XML file. The XML file can be created using the object's ToXMLFile method.
  - param `bstrFileName`: The path and name of the XML file from which to retrieve the object's data.
- `Public Sub FromXMLString(ByVal bstrXML As String)` Sets the object's properties using data from an XML string. The XML string can be created using the object's ToXMLString method.
  - param `bstrXML`: The XML from which to retrieve the object's data.
- `Public Function GetXMLSchema() As String` Returns the XML schema for the XML generated by the ToXMLFile and ToXMLString methods.
- `Public Sub ToXMLFile(ByVal bstrFileName As String)` Creates an XML file that represents the object.
  - param `bstrFileName`: The path and file name of the XML file.
  - remarks: The schema of the XML can be retrieved with the GetXMLSchema method.
- `Public Function ToXMLString() As String` Creates and returns an XML string that represents the object.
  - remarks: The schema of the XML can be retrieved with the GetXMLSchema method.

# ReportType (Object)

Represent the report type to which a layout is assigned. You can insert report types for add-on forms. Source table: RTYP.

## Properties (6)
- `Public Property AddonFormType() As String` [R/W] The type of the add-on form. Field name: FRM_TYPE. Length: 250 characters.
- `Public Property AddonName() As String` [R/W] The name of the add-on. Field name: ADD_NAME. Length: 250 characters.
- `Public Property DefaultReportLayout() As String` [R/W] The default report layout. Field name: DEFLT_REP. Length: 8 characters.
- `Public Property MenuID() As String` [R/W] The ID of the menu entry in the SAP Business One Main Menu. Field name: MNU_ID. Length 4 characters.
- `Public Property TypeCode() As String` [R] The type of the report. Field name: CODE.
- `Public Property TypeName() As String` [R/W] The name of the report type. Field name: NAME. Length: 250 characters.

## Methods (5)
- `Public Sub FromXMLFile(ByVal bstrFileName As String)` Sets the object's properties using data from an XML file. The XML file can be created using the object's ToXMLFile method.
  - param `bstrFileName`: The path and name of the XML file from which to retrieve the object's data.
- `Public Sub FromXMLString(ByVal bstrXML As String)` Sets the object's properties using data from an XML string. The XML string can be created using the object's ToXMLString method.
  - param `bstrXML`: The XML from which to retrieve the object's data.
- `Public Function GetXMLSchema() As String` Returns the XML schema for the XML generated by the ToXMLFile and ToXMLString methods.
- `Public Sub ToXMLFile(ByVal bstrFileName As String)` Creates an XML file that represents the object.
  - param `bstrFileName`: The path and file name of the XML file.
  - remarks: The schema of the XML can be retrieved with the GetXMLSchema method.
- `Public Function ToXMLString() As String` Creates and returns an XML string that represents the object.
  - remarks: The schema of the XML can be retrieved with the GetXMLSchema method.

# ReportTypeParams (Object)

Holds the key to an existing report type. This object is used to pass keys to and retrieve keys from ReportTypesService methods.

## Properties (5)
- `Public Property AddonFormType() As String` [R] The type of the add-on form. Field name: FRM_TYPE.
- `Public Property AddonName() As String` [R] The name of the add-on. Field name: ADD_NAME.
- `Public Property MenuID() As String` [R] The menu ID. Field name: MNU_ID.
- `Public Property TypeCode() As String` [R/W] The type of the report. Field name: CODE. Length: 4 characters.
- `Public Property TypeName() As String` [R] The name of the report type. Field name: NAME.

## Methods (5)
- `Public Sub FromXMLFile(ByVal bstrFileName As String)` Sets the object's properties using data from an XML file. The XML file can be created using the object's ToXMLFile method.
  - param `bstrFileName`: The path and name of the XML file from which to retrieve the object's data.
- `Public Sub FromXMLString(ByVal bstrXML As String)` Sets the object's properties using data from an XML string. The XML string can be created using the object's ToXMLString method.
  - param `bstrXML`: The XML from which to retrieve the object's data.
- `Public Function GetXMLSchema() As String` Returns the XML schema for the XML generated by the ToXMLFile and ToXMLString methods.
- `Public Sub ToXMLFile(ByVal bstrFileName As String)` Creates an XML file that represents the object.
  - param `bstrFileName`: The path and file name of the XML file.
  - remarks: The schema of the XML can be retrieved with the GetXMLSchema method.
- `Public Function ToXMLString() As String` Creates and returns an XML string that represents the object.
  - remarks: The schema of the XML can be retrieved with the GetXMLSchema method.

# ReportTypesParams (Collection)

A collection of ReportTypeParams objects.

## Properties (1)
- `Public Property Count() As Long` [R] Returns the number of objects in the collection.

## Methods (5)
- `Public Function Add() As ReportTypeParams` Adds an empty object to the collection.
  - remarks: After an object is added to this collection, the database is not automatically updated. You must then update the GeneralData object to which this collection belongs, by executing the Update method of the GeneralService service.
- `Public Function GetXMLSchema() As String` Returns the XML schema for the XML generated by the ToXMLFile and ToXMLString methods.
- `Public Function Item(ByVal vtIndex As Variant) As ReportTypeParams` Returns the object at the specified index.
  - param `vtIndex`: The index of the object to be returned (0-based)
- `Public Sub ToXMLFile(ByVal bstrFileName As String)` Creates an XML file that represents the object.
  - param `bstrFileName`: The path and file name of the XML file.
  - remarks: The schema of the XML can be retrieved with the GetXMLSchema method.
- `Public Function ToXMLString() As String` Creates and returns an XML string that represents the object.
  - remarks: The schema of the XML can be retrieved with the GetXMLSchema method.

# ReportTypesService (Object)

The ReportTypesService service enables you to add, look up, and delete the report types in SAP Business One. Source table: RTYP.

**Example:**
- C# example (from SAP's help):
  ```csharp
  SAPbobsCOM.ReportTypesService rptTypeService = (SAPbobsCOM.ReportTypesService)oCompany.GetCompanyService().GetBusinessService(SAPbobsCOM.ServiceTypes.ReportTypesService);
  SAPbobsCOM.ReportType newType = (SAPbobsCOM.ReportType)rptTypeService.GetDataInterface(SAPbobsCOM.ReportTypesServiceDataInterfaces.rtsReportType);
  newType.TypeName = "Addon Demo Type 3";
  newType.AddonName = "SimpleForm";
  newType.AddonFormType = "MySimpleForm";
  newType.MenuID = "MySubMenu01";
  SAPbobsCOM.ReportTypeParams newTypeParam = rptTypeService.AddReportType(newType);
  ```

## Methods (8)
- `Public Function AddReportType(ByVal pIReportType As ReportType) As ReportTypeParams` Adds a new report type.
  - param `pIReportType`: The data for the new report type.
- `Public Sub DeleteReportType(ByVal pIReportType As ReportType)` Deletes an existing report type.
  - param `pIReportType`: The key of the report type to be deleted.
  - remarks: Before the deletion of the report type, you should delete all layouts related to the ReportType object. The deletion of a layout cannot be completed when the layout is the default layout of a ReportType object. Use the UpdateReportType method to reset the DefaultReportLayout property to null.
- `Public Function GetDataInterface(ByVal enumMSDI As ReportTypesServiceDataInterfaces) As Object` Creates an empty data structure for use with the ReportTypesService.
  - param `enumMSDI`: one of the enumeration's values (see the enum file)
  - enum: `ReportTypesServiceDataInterfaces` in `../enums/enums-03.md`
- `Public Function GetDataInterfaceFromXMLFile(ByVal bstrFileName As String) As Object` Creates an object from an XML file.
  - param `bstrFileName`: The path and name of the XML file with which to create the object.
  - remarks: The XML file can be created using an object's ToXMLFile method. The XML file defines the object and its data.
  - C# example (from SAP's help):
    ```csharp
    public void AddFromXMLFile(Hashtable Properties, String Path)
    {
        //Store GeneralData object as XML
        SAPbobsCOM.GeneralService oGeneralService;
        SAPbobsCOM.GeneralData oGeneralData;
        SAPbobsCOM.GeneralData oGeneralDataXML;

        oGeneralService = cConnection.Instance.DICompanyService.GetGeneralService(UDOID);
        oGeneralData = (GeneralData)oGeneralService.GetDataInterface(GeneralServiceDataInterfaces.gsGeneralData);

        foreach (DictionaryEntry Pair In Properties)
            oGeneralData.SetProperty(Pair.Key.ToString(), Pair.Value.ToString());

        oGeneralData.ToXMLFile(Path);

        //Retrieve XML and create GeneralData object from the XML
        oGeneralDataXML = (GeneralData)oGeneralService.GetDataInterfaceFromXMLFile(Path);
        oGeneralService.Add(oGeneralDataXML);
    }
    ```
- `Public Function GetDataInterfaceFromXMLString(ByVal bstrXMLString As String) As Object` Creates an object from XML.
  - param `bstrXMLString`: The XML with which to create the object.
  - remarks: The XML can be created using an object's ToXMLString method. The XML defines the object and its data.
  - C# example (from SAP's help):
    ```csharp
    public void AddFromXMLString(Hashtable Properties)
    {
        //Store GeneralData object as XML
        SAPbobsCOM.GeneralService oGeneralService;
        SAPbobsCOM.GeneralData oGeneralData;
        SAPbobsCOM.GeneralData oGeneralDataXML;
        string XMLString;

        oGeneralService = cConnection.Instance.DICompanyService.GetGeneralService(UDOID);
        oGeneralData = (GeneralData)oGeneralService.GetDataInterface(GeneralServiceDataInterfaces.gsGeneralData);

        foreach (DictionaryEntry Pair in Properties)
            oGeneralData.SetProperty(Pair.Key.ToString(), Pair.Value.ToString());

        XMLString = oGeneralData.ToXMLString();

        //Retrieve XML string and create GeneralData object from the XML
        oGeneralDataXML = (GeneralData)oGeneralService.GetDataInterfaceFromXMLString(XMLString);
        oGeneralService.Add(oGeneralDataXML);
    }
    ```
- `Public Function GetReportType(ByVal pIReportTypeParams As ReportTypeParams) As ReportType` Retrieves a report type. The report type is specified by its key, which is contained in the ReportTypeParams object passed to the method.
  - param `pIReportTypeParams`: The key of the report type to retrieve.
- `Public Function GetReportTypeList() As ReportTypesParams` Returns the ReportTypesParams data collection that identify all report types.
- `Public Sub UpdateReportType(ByVal pIReportType As ReportType)` Updates an existing report type. The data for the report type, including the key of the report type to be updated, is contained in the ReportType object passed to the method. To update a report type, you must first retrieve it using the GetReportType method.
  - param `pIReportType`: The data for the report type to be updated. The ReportType object must contain the key of the object to be updated.

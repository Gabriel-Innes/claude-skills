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
  - enum: `../enums/ProjectManagementServiceDataInterfaces.md`
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

<!-- source: REFDI.chm, SAP Business One DI API 10.0 (10.00.190) | version: DI API 10.0 | verified: 2026-10-01 -->
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
  - enum: `../enums/ProjectsServiceDataInterfaces.md`
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

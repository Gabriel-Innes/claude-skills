<!-- source: https://help.sage300.com/en-us/2023/classic/Content/ReleaseDocs/TechnicalInformation.htm | version: Sage 300 2023 | page published: December 29, 2025 | extracted: 2026-09-23 by scripts/extract_release_notes.py -->

# Technical Information

This section provides information about program fixes, product contents and requirements, recommendations, and other technical information.

## Sage 300 Product Update 10 program fixes

### System Manager

Fixed an issue causing an error when logging in to web screens if the data contained many optional fields (Reference #8010286161).

Fixed a performance issue when logging in to web screens if the data contained many Currency Rates (Reference #8010280282).

Fixed an issue with changing or moving through records in the User Authorizations screen (Reference #8010241539).

### General Ledger

Fixed an issue related to zero suppression for calculated fields in Financial Reporter when running in Excel 64-bit (References: #8010103811, #8010140439, #8010264180).

### Accounts Payable

Updated the Accounts Payable T5018 (CPRS) Electronic Filing to reflect the recent revisions by the Canada Revenue Agency to the T619 Electronic Transmittal (Reference #8010364082).

## Sage 300 Product Update 9 program fixes

The following sections describe program fixes in Product Update 9.

#### Inventory Control

Fixed an error that occurred in IC Location Details web screen if an item number contained a space (Reference #8009921011).

## Sage 300 Product Update 8 program fixes

The following section describes program fixes included in Product Update 8.

### Accounts Receivable

You can now generate the Accounts Receivable Customer List when you click the Process button for the first time (References #8010212378, #8010212377, #8010212376, #8010212380).

## Sage 300 Product Update 7 program fixes

The following sections describe program fixes included in Product Update 7.

### Inventory Control

In the Inventory Control Item Pricing web screen, you can now scroll to multiple pages of records (Reference 8010060201).

### Accounts Payable Accounts Receivable, Payroll and Bank Services

Fixed the performance/freezing issue in Accounts Payable and Accounts Receivable for job related transactions (References #8009854955 #8010028874, #8010010533, #8010057693).

### Project and Job Costing

You can now close contracts or projects in classic screens, without experiencing performance issues (Reference #8010028874).

## Sage 300 Product Update 6 program fixes

The following sections describe program fixes included in Product Update 6.

### Accounts Payable Accounts Receivable, Payroll and Bank Services

These screens now fully support Korean language handling. (Reference #8009840089).

### Purchase Orders

You can now post purchase order credit notes with negative inventory levels. (References #8009838278, #8009854191, and #8009848552).

### General Ledger

When printing financial statements with Financial Reporter, all accounts are now included. (References #8009287428, and #8009659168).

### Common Services

You can now activate a new company on certain operating systems without getting the User Input error.

### System Manager

The Get Rates Macro error no longer appears. (References #8009970590, #8009973007, and #8009976019).

## Sage 300 Product Update 5 program fixes

The following sections describe program fixes included in Product Update 5.

### System Manager

Fixed a problem in the System Manager related to slow performance when importing users, importing user authorization, and modifying user authorization. (Reference #8009775742)

### Order Entry

Fixed a problem which triggered an access violation message when drilling down in Order Entry (desktop only). (Reference #8009704029, #8009521030, #8009536393, #8009558542, #8009545018, #8009621111 , #8009765699)

### Intercompany Transactions

Fixed a problem that prevented the user from processing the Update Company function. (Reference #8009773509)

## Sage 300 Product Update 4 program fixes

The following sections describe program fixes included in Product Update 4.

### System Manager

Fixed a problem in the System Manager web screen related to exporting information to an Excel file where the resulting file did not have the Named Range defined.

### Common Services

Fixed a problem in Common Services to avoid fiscal periods from prior years becoming unlocked after upgrade. (Reference #8009488887, #8009502528)

### General Ledger

Fixed a problem in the General Ledger web screen for the number of decimals in the exchange rate in entries. (Reference #​8009480228)

Fixed a problem with the printing object in Financial Reporter. (Reference #8007288528)

Fixed a problem in Budget Maintenance where the screen would not respond when expanding the Budget Amount column. (Reference #8009557301)

### Bank Services

Fixed a problem in bank reconciliation where a withdrawal amount would get stuck in the withdrawal field after reversal. (Reference #8009658363)

### Singapore Tax Reporting

Fixed a problem with the TS GST IRAS Audit File Generator for which the Generate function was not working.

### UK Tax Reporting

Fixed a problem for UK Tax (TK70) VAT Return Entry Form where home currency was being reported as source currency. (Reference #8009653339, #8009653663)

### Accounts Receivable

Fixed a problem in the Aged Trial Balance report where there was a discrepancy after clearing history. (Reference #8009607273)

Fixed a problem in Customer web screen that the Statistics tab was read-only when running this screen in CRM Integration (Reference #8009723584)

## Sage 300 Product Update 3 program fixes

The following sections describe program fixes included in Product Update 3.

### System Manager

Fixed a problem for which the user incorrectly receives a message indicating the maximum number of concurrent users have been reached even though there is sufficient user counts available. The issue appears to occur when there is an increase in activity via third-party add-on.   (Reference # 8009476339) (Reference # 8009583454) (Reference # 8009580890)

### Bank Services

Fixed a problem where the user is unable to mark transactions as reconciled in Reconcile Statements screen.   (Reference # 8009618878)

## Sage 300 Product Update 2 program fixes

The following sections describe program fixes included in Product Update 2.

### Accounts Payable

Fixed a problem for which the Aatrix upload function does not take into consideration Vendor 1099 Tax Number Type.  (Reference # 8009462978)

Fixed a problem for which the Aatrix Upload function uses Vendor Name instead of Legal Name (Reference # 8009491289)

### Inventory Control

Fixed a problem that could cause Internal Usage Transactions web screen to display an incorrect Internal Usage G/L Account if G/L Account Segment Overrides in IC Locations is used. (Reference # 8009363711)

### Order Entry

Fixed a problem on WEB CRM Integration where the screen greys out when National Account is on Hold (Reference # 8009324066)

Fixed a problem in Credit/Debit Note Entry web screen where the data may get corrupted when the Credit Note number is manually entered instead of letting the system generate the number. (Reference # 8009481877)

### Project and Job Costing

Fixed a performance problem when drilling down to a Job Costing Timecard Entry from the Job Costing Billing Worksheet. (Reference # 8009529899)

### Lot Number

Fixed a problem in O/E Shipment Entry web screen to correct the lot expiry date of an item if the Qty Shipped field for the item is zero (Reference # 8009571355)

### Intercompany Transactions

Fixed a problem where Finder crashes when selecting Vendor on 2nd Entry of Invoice Batch (Reference # 8009464750)

## Sage 300 Product Update 1 program fixes

Sage 300 2023.1 includes program fixes for some problems that exist in the most recent previous version (Sage 300 2023 Product Update 4). The sections below describe these program fixes.

### General Ledger

Fixed a problem where the Journal Entry import does not check if the Entry Date is valid or not in the import file, causing it to import invalid dates in the details.

### Purchase Order

Changed the behavior in P/O Invoice Entry. Previously, P/O Invoice Entry allowed the user to post the invoice even when there is a duplicate invoice number. Now, it will give an error when the invoice for the vendor already exists.

### Item Inquiry

Fixed a problem that may cause slow performance when navigating to the Bill of Material tab on the I/C Item Inquiry screen.

### Accounts Receivable

A change was made to Sage 300cloud web screens A/R Invoice printing. It now defaults to the last invoice report file you printed.

## Sage 300 2023 program fixes

Sage 300 2023 includes program fixes for some problems that exist in the most recent previous version (Sage 300 2022 Product Update 2). The following sections describe these program fixes.

### Retrieving records that include a G/L account number

In many Sage 300cloud web screens, transactions or records that include a G/L account number are retrieved faster. (Reference #8009246827)

### Bank Services

Fixed a problem on the Reconcile Statements screen that prevented you from clearing transactions for a customer or vendor if you posted the transactions and then changed the customer/vendor number before clearing the transactions. (Reference #8009184903)

### Accounts Payable

Fixed a problem on the Payment Entry screen in Sage 300cloud web screens that could occur when adding a detail line in the table. When you clicked Add Line, instead of adding a new detail line, some information in existing detail lines would be changed to incorrect information. (Reference #8009274937)

### General Ledger

Fixed some problems that could prevent you from using Financial Reporter. You can now use Financial Reporter if:

- You do not use Optional Fields. (Reference #8009120576)

- There is a space in the path of the Sage 300 program files.

### Order Entry

- Fixed a problem in Sage 300 desktop screens that could prevent you from approving prices or credit checks if your system is set up to require complex passwords. (Reference #8009196429)

- Fixed a problem on the Copy Orders screen that could occur if you use Pricing Unit as the Default Order UOM (this is set on the Processing tab of the O/E Options screen), which prevented you from copying orders for a customer if an inventory location is not specified for the customer (on the Invoicing tab of the A/R Customers screen). (Reference #8009215442)

- Fixed a problem on the Order Entry screen in Sage 300cloud web screens, which could prevent comments and instructions for order details from being saved. (Reference #8009231401)

### Sage CRM Integration

- In Sage CRM, the following fields on the A/R Customer screen now use the current date by default (instead of the Sage 300 session date):

- Statistics tab: Fiscal Period and Fiscal Year fields
- Comments tab: Date Entered field (in the table)
- Credit Status tab: Age As Of field
(Reference #8008611017)

- If you create a new company in Sage CRM by importing a Customer from Sage 300 (either manually or using automatic synchronization), the correct contact information appears for the company in Sage CRM. (Reference #8009130716)

### Item Number Change

Fixed a problem that could prevent you from combining item numbers. (Reference #8009233392)

## General Information

- Sage 300 2023 supports upgrades only from version 5.6 or later.

- You require version 2023 (internally versioned as 7.0A) of all core programs that you plan to use.
If you use Canadian Payroll or US Payroll, you require version 7.3 of these programs with the most current tax updates.
Note: You must install Sage 300 before installing payroll programs.

- If you are upgrading from an earlier version, you must upgrade all Sage 300 programs to 2023 at the same time. Sage 300 2023 programs do not work with programs from earlier versions.

- If you have a subscription license, you don't need to enter serial numbers and activation keys for individual Sage 300 applications. When the License Manager appears during installation, the only license information you need to enter is your Client ID, Company Name, and Serial Number. After you've entered this information, ensure that you have internet access, and then click Refresh to verify your subscription.

- If you do not have the following programs, which are required to use Sage 300, they are installed with Sage 300:

- MSXML (Microsoft XML Core Services) 6.0

- Microsoft SQL Server Native Client 11.0

- Microsoft .NET Framework 4.6.2

- If you need to use the Sage 300 .NET Remoting Service, you must run the Web Deployment Wizard that is available on Sage Knowledgebase article 104304 .

- Sage 300 2023 includes SP30 for SAP Crystal Reports® runtime engine.
If you use Sage HRMS or Sage Fixed Assets integrated with Sage 300, refer to the Sage 300 2023 Compatibility Guide for updated information on compatibility with Sage HRMS and Sage Fixed Assets. The Sage 300 2023 Compatibility Guide is available from Sage Knowledgebase article 26777 .

- For the most current technical information about database and report changes, and about parameters for customizing printed forms, see Sage 300 Database and Report Changes , Sage 300 Parameters for Customizing Printed Forms , or Sage Knowledgebase article 68834 .

- Product documentation for Sage 300 is available from the Sage 300 Product Documents website.

## Compatibility with other programs

For a complete list of compatible programs, database platforms, and operating systems, see the Sage 300 2023 Compatibility Guide, available from Sage Knowledgebase article 222924950026777.

## Known issues

- When using the Notes screen on the Sage 300 classic desktop:

- When adding or editing a note, the text editing area and toolbar appear only if you have enabled active scripting and scripting of Java applets in Internet Explorer security settings. For more information, see Sage Knowledgebase article 224924950076898 .

- The Notes screen does not appear correctly if you use the Medium - 125% display size (specified in Windows control panel). For more information, see Sage Knowledgebase article 224924950076926 .

- When previewing reports in web screens, information in some reports is not aligned correctly. To work around this issue, export the report to PDF format. For more information, see Sage Knowledgebase article 224924950076337 .

- In some fields, Chinese language characters cannot be entered.

- Printing issue with Sage Fixed Assets Integration (FAS). Report printing in both FAS and Sage 300 will not work after the installation of FAS Integration. To work around this issue, you need to restore a Crystal runtime dll. For more information, see Sage Knowledgebase article 230907204735260 .

## Installing Sage 300

Important! The information in this section only applies to versions prior to Sage 300 2023 Product Update 2.

For detailed instructions on installing Sage 300, see the Sage 300 Installation and Administration Guide .

## Installing product updates

After installing a product update:

- If you use Sage 300cloud web screens, you must use Database Setup to configure the Portal database again.

- If you use Sage CRM integrated with Sage 300, you must upgrade your CRM integration as follows:

- Install the Sage CRM integration for Sage 300, which is available on Sage Knowledgebase article 45434 .
- Uninstall and then reinstall the Sage CRM Synchronization Component. (Use the Sage CRM Workstation Setup screen in Sage 300 to install the Sage CRM Synchronization Component.)

- You should clear your browser’s cache. (Some fixes included in the update may not take effect until you do.)

- On any workstations you use, you must reinstall workstation setup as the Windows administrator user if:

- The product update includes changes to workstation setup.
- An earlier product update includes changes to workstation setup, and you have not previously installed that product update or any other subsequent product update.

Example: Suppose that the current Product Update is 4. Product Update 2 includes changes to workstation setup, and the other product updates do not. You have been using Product Update 1. You did not install Product Update 2, or 3. You have now installed Product Update 4. To update your workstations with the changes to workstation setup that were included in Product Update 2, you must reinstall workstation setup.

- The following product updates include changes to workstation setup:

- Product Update 4

## Removing Sage 300

Before removing Sage 300, you must:

- Close all instances of the Sage 300 Desktop.

- Close all applications that integrate with Sage 300.

- Stop all Sage 300 services that are running, such as Sage 300 .Net Remoting Service.

To remove Sage 300 2023 programs:

- In Windows' Control Panel, click Programs And Features.

- Open Uninstall Or Change A Program, and then:

- To remove all Sage 300 programs, double-click Sage 300 2023.
- To remove individual Sage 300 programs:

- Click Sage 300 2023, and then click Change. (Do not double-click Sage 300 2023.)
- Click Modify, and then use the Select Features screen to select the programs you want to install and clear the selections for programs you want to remove.

## Sage 300 Payroll

Sage 300 2023 includes Canadian and US Payroll. For more information, see the related release notes, which you can find on the Sage 300 Product Documents website.

Note: Canadian and US Payroll may not be available in all regions.

## Sage 300 Intelligence Reporting

Sage 300 2023 includes Sage 300 Intelligence Reporting. For more information and help with getting started, see Sage Intelligence Learning .

### Known issues

- If you have multiple versions of Microsoft Excel installed, you may need to manually load the Report Designer Task Pane Excel Add-in.

- If you use exclusions in account and row set rules, exclusion accounts may appear when you drill down to balance.

- If Sage 300 Intelligence Reporting was installed by a user other than you (for example, an administrator), you must open Microsoft Excel before running reports in Report Viewer or Report Manager.

- In Report Viewer, an "Open File - Security Warning" message appears for every report you view. (This message should only appear once, when you first open Report Viewer.)

- If you use Microsoft Excel 2013, and you save a report template in Report Manager using Save Excel Template:

- When you run the report in Excel, an “External Data” message may appear. You can proceed by clicking Yes.

- If the report template has a timeline, the timeline does not retain its filters.

## Sage 300 Software Development Kit

This section lists improvements and fixes for the Sage 300 Software Development Kit (for desktop screens) and the Sage 300 Web Software Development Kit (for web screens).

### Sage 300 2023 improvements and fixes

Fixed a problem that prevented viewAttribs calls from reflecting changes to field values.

Published: December 29, 2025

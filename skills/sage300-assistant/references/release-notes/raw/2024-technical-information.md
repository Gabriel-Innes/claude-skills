<!-- source: https://help.sage300.com/en-us/2024/classic/Content/ReleaseDocs/TechnicalInformation.htm | version: Sage 300 2024 | page published: April 24, 2026 | extracted: 2026-09-23 by scripts/extract_release_notes.py -->

# Technical Information

This section provides information about program fixes, product contents and requirements, recommendations, and other technical information.

Important: Workstation Setup needs to be reinstalled if you are upgrading from previous Product Updates. For details please see the workstation setup section under Installing Product Updates, below.

## Sage 300 Product Update 9 program fixes

The following sections describe program fixes in Product Update 9.

### System Manager

Fixed an issue with email settings when the password exceeds 48 characters (Reference #8010796796).

#### Inventory Control

Fixed an issue where incorrect quantities were posted to the inventory after changing the unit of measure during a transfer in the IC Transfers web screen (Reference #8010769330).

### Accounts Payable

We will now display a warning during T5018 (CPRS) XML generation if special characters are present in the Transmitter, Payer or Vendor information.

### Accounts Receivable

Fixed an issue in AR Invoice Entry (Web) where the item detail tax class displayed the customer’s tax class instead of the item’s tax class (Reference #8010855250).

### Order Entry

Fixed an issue in OE Credit/Debit Note Entry where the item’s extended cost was not updated when the Default Order UOM in OE Options was set to Pricing Unit (Reference #8010837387).

## Sage 300 Product Update 8 program fixes

The following sections describe program fixes in Product Update 8.

### Order Entry

Fixed a problem when promoting a quote to an order in CRM, optional fields defined in the quote detail lines were not correctly mapped to the corresponding order detail lines (Reference #8010507929).

## Sage 300 Product Update 7 program fixes

The following sections describe program fixes in Product Update 7.

#### Project Management

Fixed a performance issue when loading contracts in the PJC Contract Maintenance screen (Reference #8009514617).

#### Sales Analysis

Fixed an issue when running Sales Analysis as a scheduled task in AUTO mode (Reference #8010483035).

#### General Ledger

Fixed an issue where the focus will drop when print previewing an FR Financial Statement using Excel 64 bit (Reference #8010452288).

## Sage 300 Product Update 6 program fixes

The following sections describe program fixes in Product Update 6.

#### System Manager

Fixed an issue causing an error when logging in to web screens if the data contained many optional fields (Reference #8010286161).

Fixed a performance issue when logging in to web screens if the data contained many Currency Rates (Reference #8010280282).

Fixed an issue in web screens where the finder hung in certain situations (Reference #8010299317).

Fixed an issue with changing or moving through records in the User Authorizations screen (Reference #8010241539).

Improved login performance when the User Authenticated List of Companies feature is enabled. (Reference #8010287793).

#### General Ledger

Fixed an issue related to zero suppression for calculated fields in Financial Reporter when running in Excel 64-bit (References: #8010103811, #8010140439, #8010264180).

Fixed an Excel Addin Error Code in Financial Reporter (References: #8010024480, #8009988260, #8010122235).

#### Accounts Payable

Updated the AP T5018 (CPRS) Electronic Filing to reflect the recent revisions by the Canada Revenue Agency to the T619 Electronic Transmittal (Reference #8010364082).

#### Accounts Receivable

Fixed an issue in the Accounts Receivable Invoice Entry web screen where adding a new line incorrectly changed the Print Comment from ‘Yes’ to ‘No’ and removed the comment from the detail line. (References: #8008937418, #8010148506).

#### Inventory Control

Updated Importing into Inventory Control Vendor Details so that the ‘Update’ import calculates the cost based on the Unit of Measure, same as an ‘Insert’ import (Reference #8010349496).

#### Purchase Order

Fixed an issue where custom grid settings in the Purchase Order Entry and Receipt Entry web screens were not being saved for the user (References: #8010148507, #8010442158).

## Sage 300 Product Update 5 program fixes

The following sections describe program fixes in Product Update 5.

#### Inventory Control

Fixed an error that occurred in IC Location Details web screen if an item number contained a space (Reference #8009921011).

## Sage 300 Product Update 4 program fixes

The following sections describe program fixes in Product Update 4.

### Accounts Receivable

You can now generate the Accounts Receivable Customer List when you click the Process button for the first time (References #8010212378, #8010212377, #8010212376, #8010212380).

## Sage 300 Product Update 3 program fixes

The following sections describe program fixes in Product Update 3.

### Inventory Control

You can now scroll past the first page of pricing records in the Inventory Control Item Pricing web screen (Reference #8010060201).

### Accounts Payable Accounts Receivable, Payroll and Bank Services

Fixed the performance/freezing issue in Accounts Payable and Accounts Receivable for job related transactions (References #8009854955 #8010028874, #8010010533, #8010057693).

### Project and Job Costing

You can now close contracts or projects in classic screens, without experiencing performance issues (Reference #8010028874).

## Sage 300 Product Update 2 program fixes

The following sections describe program fixes in Product Update 2.

### Common Services

You can now activate a new company on certain operating systems without getting the User Input error.

### System Manager

The Get Rates Macro error no longer appears. (References #8009970590, #8009973007, and #8009976019)

### Sales Analysis

You can now use Sales Analysis successfully.

### General Ledger

When printing financial statements with Financial Reporter, all accounts are now included. (References #8009287428, and #8009659168)

### Web API

The Web API performance has been upgraded.

Note: If you restore a SQL Database immediately after running a web API, you may need to reset IIS first.

### Accounts Payable, Accounts Receivable, Payroll, and Bank Services

These screens now fully support Korean language handling. (Reference # 8009840089)

## Sage 300 Product Update 1 program fixes

The following sections describe program fixes included in Product Update 1.

### System Manager

Fixed a problem in the System Manager related to slow performance when importing users, importing user authorization, and modifying user authorization. (Reference #8009775742)

### Order Entry

Fixed a problem which triggered an access violation message when drilling down in Order Entry (desktop only). (Reference #8009704029, #8009521030, #8009536393, #8009558542, #8009545018, #8009621111 , #8009765699)

### Intercompany Transactions

Fixed a problem that prevented the user from processing the Update Company function. (Reference #8009773509)

### Sage CRM

Fixed a problem where the statistics year or period for promoted customers was read-only. (Reference #8009723584)

## Sage 300 2024 program fixes

Sage 3002024 includes program fixes for some problems that exist in the most recent previous version (Sage 300 2023 Product Update 3). The following sections describe these program fixes.

### Web API

Fixed an issue where the Web API endpoint for IC Item Location Details was not available. (Reference # SM01_2648820230508)

### System Manager

Fixed a problem that prevents import in web screens when the IIS server is configured with a proxy site. (Reference # 8009627198)

### Bank Services

Fixed a problem on the withdrawal amount when reversing an entry (Reference # 8009658363)

### Accounts Payable

Fixed a problem in which the number of decimals in VB screen (desktop) and number of decimals in web screens were not consistent in GL entry. (Reference # 8009480228)

Fixed a problem that prevented saving a GL Financial Report. (Reference # 8007288528)

### Order Entry

Fixed a problem on UK Tax (TK70) VAT Return Entry Form where the Source Currency is used instead of Home Currency (Reference # 8009653339) (Reference # 8009653663)

## General Information

- Sage 300 2024 supports upgrades only from version 5.6 or later.

- If you use workstation setup, you must also run Sage 300 Intelligence Reporting workstation setup (located in BX66A\WSSetup) on every workstation where you will view and use Intelligence Reporting screens.

- You require version 2024 (internally versioned as 7.1A) of all core programs that you plan to use.
If you use Canadian Payroll or US Payroll, you require version 7.3 of these programs with the most current tax updates.

Note: The tax tables for version 7.3 will be available until March 2024. After this date tax tables and support will only be available for Payroll version 8.0.

Important! You must install Sage 300 before installing payroll programs.

- If you are upgrading from an earlier version, you must upgrade all Sage 300 programs to 2024 at the same time. Sage 300 2024 programs do not work with programs from earlier versions.

- If you have a subscription license, you don't need to enter serial numbers and activation keys for individual Sage 300 applications. When the License Manager appears during installation, the only license information you need to enter is your Client ID, Company Name, and Serial Number. After you've entered this information, ensure that you have internet access, and then click Refresh to verify your subscription.

- If you do not have the following programs, which are required to use Sage 300, they are installed with Sage 300:

- MSXML (Microsoft XML Core Services) 6.0

- Microsoft ODBC Driver 18 for SQL Server.

- Microsoft .NET Framework 4.8.2

- Sage 300 2024 includes SP34 for SAP Crystal Reports® runtime engine. If you use Sage HRMS or Sage Fixed Assets integrated with Sage 300, refer to the Sage 300 2024 Compatibility Guide for updated information on compatibility with Sage HRMS and Sage Fixed Assets. The Sage 300 2024 Compatibility Guide is available from Sage Knowledgebase article 26777 .

- For the most current technical information about database changes, please refer to the Sage 300 2024 SDK Application Object Model (AOM).

- Product documentation for Sage 300 is available from the Sage 300 Product Documents website.

## Compatibility with other programs

For a complete list of compatible programs, database platforms, and operating systems, see the Sage 300 2024 Compatibility Guide, available from Sage Knowledgebase article 222924950026777.

## Known issues

- When using the Notes screen on the Sage 300 classic desktop:

- When adding or editing a note, the text editing area and toolbar appear only if you have enabled active scripting and scripting of Java applets in Internet Explorer security settings. For more information, see Sage Knowledgebase article 224924950076898 .

- The Notes screen does not appear correctly if you use the Medium - 125% display size (specified in Windows control panel). For more information, see Sage Knowledgebase article 224924950076926 .

- When previewing reports in web screens, information in some reports is not aligned correctly. To work around this issue, export the report to PDF format. For more information, see Sage Knowledgebase article 224924950076337 .

- In some fields, Chinese language characters cannot be entered.

- Printing issue with Sage Fixed Assets Integration (FAS). Report printing in both FAS and Sage 300 will not work after the installation of FAS Integration. To work around this issue, you need to restore a Crystal runtime dll. For more information, see Sage Knowledgebase article 230907204735260 .

## Installing Sage 300

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

The following product updates include changes to workstation setup:

- Product Update 9

## Removing Sage 300

Before removing Sage 300, you must:

- Close all instances of the Sage 300 Desktop.

- Close all applications that integrate with Sage 300.

- Stop all Sage 300 services that are running, such as Sage 300 .CNA.Windows Service.

To remove Sage 300 2024 programs:

- In Windows' Control Panel, click Programs And Features.

- Open Uninstall Or Change A Program, and then:

- To remove all Sage 300 programs, double-click Sage 300 2024.
- To remove individual Sage 300 programs:

- Click Sage 300 2024, and then click Change. (Do not double-click Sage 300 2024.)
- Click Modify, and then use the Select Features screen to select the programs you want to install and clear the selections for programs you want to remove.

## Sage 300 Payroll

Sage 300 2024 includes Canadian and US Payroll. For more information, see the related release notes, which you can find on the Sage 300 Product Documents website.

Note: Canadian and US Payroll may not be available in all regions.

## Sage 300 Intelligence Reporting

Sage 300 2024 includes Sage 300 Intelligence Reporting. For more information and help with getting started, see Sage Intelligence Learning .

Sage 300 2024 includes v8.0.0 of Intelligence Reporting. For more information and help with getting started, see Sage Intelligence Learning .

### Known issues

- If you have multiple versions of Microsoft Excel installed, you may need to manually load the Report Designer Task Pane Excel Add-in.

- If you use exclusions in account and row set rules, exclusion accounts may appear when you drill down to balance.

- If Sage 300 Intelligence Reporting was installed by a user other than you (for example, an administrator), you must open Microsoft Excel before running reports in Report Viewer or Report Manager.

- In Report Viewer, an "Open File - Security Warning" message appears for every report you view. (This message should only appear once, when you first open Report Viewer.)

- If you use Microsoft Excel 2013, and you save a report template in Report Manager using Save Excel Template:

- When you run the report in Excel, an “External Data” message may appear. You can proceed by clicking Yes.

- If the report template has a timeline, the timeline does not retain its filters.

Published: April 24, 2026

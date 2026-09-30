<!-- source: https://help.sage300.com/en-us/2025/classic/Content/ReleaseDocs/TechnicalInformation.htm | version: Sage 300 2025 | page published: September 10, 2026 | extracted: 2026-09-23 by scripts/extract_release_notes.py -->

# Technical Information

This section provides information about program fixes, product contents and requirements, recommendations, and other technical information.

Important: Workstation Setup needs to be reinstalled if you are upgrading from previous Product Updates. For details please see the workstation setup section under Installing Product Updates, below.

## Sage 300 Product Update 6 program fixes

The following sections describe program fixes in Product Update 6.

#### System Manager

Sage 300 no longer uses the Microsoft Access Database Engine 2016 for import and export functionality. Excel import and export now uses the same modern engine as Sage 300 web screens (References #8010649072 #8010687490).

## Sage 300 Product Update 5 program fixes

The following sections describe program fixes in Product Update 5.

### Inventory Control

Fixed an issue where incorrect quantities were posted to the inventory after changing the unit of measure during a transfer in the IC Transfers web screen (Reference #8010769330).

### System Manager

Fixed an issue with email settings when the password exceeds 48 characters (Reference #8010796796).

Fixed an issue where the SQL login may be locked out if "UserAuthenticatedListOfCompanies" is enabled (Reference #8010606612).

### Accounts Receivable

Fixed an issue in AR Invoice Entry (Web) where the item detail tax class displayed the customer’s tax class instead of the item’s tax class (Reference #8010855250).

### Accounts Payable

We will now display a warning during T5018 (CPRS) XML generation if special characters are present in the Transmitter, Payer or Vendor information.

### Order Entry

Fixed an issue in OE Credit/Debit Note Entry where the item’s extended cost was not updated when the Default Order UOM in OE Options was set to Pricing Unit (Reference #8010837387).

## Sage 300 Product Update 4 program fixes

The following sections describe program fixes in Product Update 4.

### Order Entry

Fixed a problem when promoting a quote to an order in CRM, optional fields defined in the quote detail lines were not correctly mapped to the corresponding order detail lines (Reference #8010507929).

## Sage 300 Product Update 3 program fixes

The following sections describe program fixes in Product Update 3.

#### Bank Entry

Fixed an issue on the Bank Entry web screen where Distribution Sets were not appearing in the finder for single currency companies (Reference #8010457859).

#### Order Entry

Fixed an issue where the OE Picking slip in web screen couldn't remember the previously selected form name.

#### Purchase Order

Fixed a performance issue in the Requisition Number finder in the Purchase Order screen's Create PO From Requisition popup for both Web and Desktop (Reference ##8010437682).

#### Project Management

Fixed a performance issue when loading contracts in the PJC Contract Maintenance screen (Reference #8009514617).

#### Sales Analysis

Fixed an issue when running Sales Analysis as a scheduled task in AUTO mode (Reference #8010483035).

#### General Ledger

Fixed an issue where the focus will drop when print previewing an FR Financial Statement using Excel 64 bit (Reference #8010452288).

#### Bank Feeds

Fixed an issue when Reconcile E-statement/bank feeds does not download currencies from a specific bank.

## Sage 300 Product Update 2 program fixes

The following sections describe program fixes in Product Update 2.

#### System Manager

Fixed an issue causing an error when logging in to web screens if the data contained many optional fields (Reference #8010286161).

Fixed a performance issue when logging in to web screens if the data contained many Currency Rates (Reference #8010280282).

Fixed an issue with changing or moving through records in the User Authorizations screen (Reference #8010241539).

Fixed an issue in web screens where the finder hung in certain situations (Reference #8010299317).

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

#### Order Entry

Fixed an issue in web screens, where Order Entry could become unresponsive in situations where negative inventory is not allowed (Reference #8010299317).

#### Account Code Change

Fixed an issue that caused Segment #10 not to show up in Account Code Change (Reference #8010397391).

#### Notes

Fixed an issue with the Notes display window (Reference #8010359925).

#### Sage Intelligence

Fixed an issue that caused connection problems in Sage Intelligence using Report Manager (References #8010154513, #8010180162).

## Sage 300 Product Update 1 program fixes

The following sections describe program fixes in Product Update 1.

### Order Entry

Added new progress meter, better error handling and clearer messages to improve emailing reports with Delivery Method set to Customer on OE web screens. (References # 8008991383 #8008978551).

Removed the meter during auto-allocation of serials and lots in OE Shipment Entry.

### Inventory Control

Fixed an error that occurred in IC Location Details web screen if an item number contained a space (Reference #8009921011).

## Sage 300 2025 program fixes

Sage 300 2025 includes program fixes for some problems that exist in the most recent previous version (Sage 300 2024 Product Update 4). The following sections describe these program fixes.

### Inventory Control

You can now scroll past the first page of pricing records in the Inventory Control Item Pricing web screen (Reference #8010060201).

### Project and Job Costing

You can now close contracts or projects in classic screens, without experiencing performance issues (Reference #8010028874).

### System Manager

Improved emailing reports with Delivery Method set to Customer or Vendor by adding new progress meter, better error handling and clearer messages on web screens. This applies to Accounts Payable, Account Receivable and Purchase Order modules. (References # 8008991383 #8008978551).

Fixed a problem running some XLS macros (Reference # 8010080399).

#### Accounts Payable Accounts Receivable, Payroll and Bank Services

Fixed the performance/freezing issue in Accounts Payable and Accounts Receivable for job related transactions (References #8009854955 #8010028874, #8010010533, #8010057693).

## General Information

- Sage 300 2025 supports upgrades only from version 5.6 or later.

- If you use workstation setup, you must also run Sage 300 Intelligence Reporting workstation setup (located in BX80A\WSSetup) on every workstation where you will view and use Intelligence Reporting screens.

- You require version 2025 (internally versioned as 7.2A) of all core programs that you plan to use.
If you use Canadian Payroll or US Payroll, you require version 8.0 of these programs with the most current tax updates.

Note: The tax tables for version 7.3 were available until March 2024. After this date tax tables and support will only be available for Payroll version 8.0.

Important! You must install Sage 300 before installing payroll programs.

- If you are upgrading from an earlier version, you must upgrade all Sage 300 programs to 2025 at the same time. Sage 300 2025 programs do not work with programs from earlier versions.

- If you have a subscription license, you don't need to enter serial numbers and activation keys for individual Sage 300 applications. When the License Manager appears during installation, the only license information you need to enter is your Client ID, Company Name, and Serial Number. After you've entered this information, ensure that you have internet access, and then click Refresh to verify your subscription.

- If you do not have the following programs, which are required to use Sage 300, they are installed with Sage 300:

- MSXML (Microsoft XML Core Services) 6.0

- Microsoft .NET Framework 4.8.2

- Sage 300 2025 includes SP34 for SAP Crystal Reports® runtime engine. If you use Sage HRMS or Sage Fixed Assets integrated with Sage 300, refer to the Sage 300 2025 Compatibility Guide for updated information on compatibility with Sage HRMS and Sage Fixed Assets. The Sage 300 2025 Compatibility Guide is available from Sage Knowledgebase article 26777 .

- For the most current technical information about database changes, please refer to the Sage 300 2025 SDK Application Object Model (AOM).

- Product documentation for Sage 300 is available from the Sage 300 Product Documents website.

## Compatibility with other programs

For a complete list of compatible programs, database platforms, and operating systems, see the Sage 300 2025 Compatibility Guide, available from Sage Knowledgebase article 222924950026777.

## Known issues

- When using the Notes screen on the Sage 300 classic desktop:

- When adding or editing a note, the text editing area and toolbar appear only if you have enabled active scripting and scripting of Java applets in Internet Explorer security settings. For more information, see Sage Knowledgebase article 224924950076898 .

- The Notes screen does not appear correctly if you use the Medium - 125% display size (specified in Windows control panel). For more information, see Sage Knowledgebase article 224924950076926 .

- When previewing reports in web screens, information in some reports is not aligned correctly. To work around this issue, export the report to PDF format. For more information, see Sage Knowledgebase article 224924950076337 .

- In some fields, Chinese language characters cannot be entered.

- Printing issue with Sage Fixed Assets Integration (FAS). Report printing in both FAS and Sage 300 will not work after the installation of FAS Integration. To work around this issue, you need to restore a Crystal runtime dll. For more information, see Sage Knowledgebase article 230907204735260 .

Note: This only applies if using FAS versions earlier than 2026.

## Installing Sage 300

For detailed instructions on installing Sage 300, see Installation and Administration Guide

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

- Product Update 6

## Removing Sage 300

Before removing Sage 300, you must:

- Close all instances of the Sage 300 Desktop.

- Close all applications that integrate with Sage 300.

- Stop all Sage 300 services that are running, such as Sage 300 .CNA.Windows Service.

To remove Sage 300 2025 programs:

- In Windows' Control Panel, click Programs And Features.

- Open Uninstall Or Change A Program, and then:

- To remove all Sage 300 programs, double-click Sage 300 2025.
- To remove individual Sage 300 programs:

- Click Sage 300 2025, and then click Change. (Do not double-click Sage 300 2025.)
- Click Modify, and then use the Select Features screen to select the programs you want to install and clear the selections for programs you want to remove.

## Sage 300 Payroll

Sage 300 2025 includes Canadian and US Payroll. For more information, see the related release notes, which you can find on the Sage 300 Product Documents website.

Note: Canadian and US Payroll may not be available in all regions.

## Sage 300 Intelligence Reporting

Sage 300 2025 includes v8.0.0 of Intelligence Reporting. For more information and help with getting started, see Sage Intelligence Learning .

### Migration from VB6 to .NET

The core of the application has been migrated from VB6 to the modern .NET framework.

The .NET framework is designed to provide users with the following improved stability, security, and performance features:

- It ensures better compatibility with current operating systems and facilitates integration with advanced technologies.

- It enables more frequent updates, a more responsive user interface, and enhanced security features to better protect user data.

- It aims to significantly enhance productivity and lays the foundation for introducing new features and capabilities in future releases.

### Office 365 Support for Email Distribution

Support for Office 365 has been added to the Excel distribution module, enabling users to utilize Office 365 for email distribution. This enhancement ensures compatibility with modern email systems, providing users with a more reliable and efficient email distribution method.

### Add SMTP TLS 1.2 Support

Support for TLS1.2 has been added to the SMTP module in the Excel distribution, ensuring secure email transmissions.

This enhancement provides users with an additional layer of security when sending emails.

### New Excel 2013+ Connection Type

Support for Excel 2013+ workbooks has been added to the Connector, allowing an Excel 2013+ workbook to be used as a data source in the Connector module. Previously, only the XLS file type was supported. Now, all XLSX file types are supported, enhancing compatibility and providing users with greater flexibility in their data sources.

This update ensures seamless integration with modern Excel formats, improving overall efficiency in data handling.

### Replace SQL CE with VistaDB

The Universal Query Engine now utilizes VistaDB instead of SQL CE, resulting in improved database performance and reliability. This update ensures that database operations are more efficient and robust, enhancing the overall stability of the application.

### Performance Enhancements

Various performance improvements have been implemented, including faster report execution times and more efficient product navigation.

These enhancements are designed to provide users with a more responsive and efficient application, improving overall productivity.

Furthermore, a new lite version of the Financial Ratios report has been included. This report runs out significantly faster than the standard report.

### UI/UX Updates and Enhancements

A range of UI and UX updates have been made, including new icons and a native Windows look and feel.

These changes aim to improve the user experience by making the interface more intuitive and visually appealing.

Additional updates:

- The mouse wheel can now be used to scroll the properties pane.

- Various improvements to avoid text being cut off when scaling is applied.

- Sage Intelligence Excel ribbon now labeled SI Tools.

### Navigation Explorer Updates

Improvements have been made to the navigation explorer to provide a more intuitive and efficient navigation experience.

These updates ensure that users can quickly and easily find the reports and tools they need.

Additional updates:

- Renaming reports now reflects immediately in the navigation pane.

- Toggle Show/Hide reports now reflects immediately in the navigation pane.

### Branding Updates

The application has been updated to match the new Sage branding, ensuring a consistent and professional appearance.

These branding updates apply to all standard reports, maintaining a cohesive look across the application.

### Add XLSX Support

Support for XLSX, XLSB, XLTX, and XLSM file formats has been added in various places, providing users with greater flexibility in handling different Excel file formats.

This update ensures compatibility with a wide range of Excel files, enhancing the application's versatility.

### Side by Side Support

The new version can now be installed side by side with the previous version, allowing users to transition smoothly without disrupting their workflow.

This feature ensures that users can test the new version while still having access to the previous one.

### Security Enhancements

Various security enhancements have been implemented to ensure the application remains secure and robust against potential threats. With the migration to the .NET framework, users benefit from the enhanced security features that .NET offers, including improved authentication and encryption protocols.

The integration with Office 365 for email distribution leverages its built-in security measures, ensuring that email communications are protected by advanced threat detection and data loss prevention technologies.

Additionally new, more robust, encryption technologies have been used when handling any potentially sensitive data.

### Known issues

- If you have multiple versions of Microsoft Excel installed, you may need to manually load the Report Designer Task Pane Excel Add-in.

- If you use exclusions in account and row set rules, exclusion accounts may appear when you drill down to balance.

- If Sage 300 Intelligence Reporting was installed by a user other than you (for example, an administrator), you must open Microsoft Excel before running reports in Report Viewer or Report Manager.

- In Report Viewer, an "Open File - Security Warning" message appears for every report you view. (This message should only appear once, when you first open Report Viewer.)

- If you use Microsoft Excel 2013, and you save a report template in Report Manager using Save Excel Template:

- When you run the report in Excel, an “External Data” message may appear. You can proceed by clicking Yes.

- If the report template has a timeline, the timeline does not retain its filters.

Published: September 10, 2026

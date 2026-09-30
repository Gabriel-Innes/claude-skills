<!-- source: https://help.sage300.com/en-us/2026/classic/Content/ReleaseDocs/TechnicalInformation.htm | version: Sage 300 2026 | page published: September 14, 2026 | extracted: 2026-09-23 by scripts/extract_release_notes.py -->

# Technical Information

This section provides information about program fixes, product contents and requirements, recommendations, and other technical information.

Important: Workstation Setup needs to be reinstalled if you are upgrading from previous Product Updates. For details please see the workstation setup section under Installing Product Updates, below.

## Sage 300 Product Update 3 program fixes

The following sections describe program fixes in Product Update 3.

#### Bank Services

Fixed an issue in the Bank Reconciliation web screen where decimals could not be entered in the Cleared Amount field (Reference #8010876610).

#### System Manager

Sage 300 no longer uses the Microsoft Access Database Engine 2016 for import and export functionality. Excel import and export now uses the same modern engine as Sage 300 web screens (References #8010649072 #8010687490).

Fixed an issue where icon appearances changed unexpectedly after copying items into a custom desktop folder (Reference #8010869983).

Fixed an issue where users received an "insufficient rights" error when attempting to edit a custom desktop folder (Reference #8010869983).

#### General Ledger

Fixed a problem where an error occurred when provisionally posting a GL batch where the journal entry contains GL accounts with transaction optional fields (Reference #8010897576).

#### CRM

Fixed an issue when sending emails with multiple CC recipients from the CRM Opportunity tab in Quotes and Orders opened in a CRM opportunity.

## Sage 300 Product Update 2 program fixes

The following sections describe program fixes in Product Update 2.

#### System Manager

Fixed an issue where RVSpy and DBSpy did not function correctly on Web screens (Reference #8010606612).

Fixed an issue with email settings when the password exceeds 48 characters (Reference #8010837387).

Fixed an issue where the SQL login may be locked out if "UserAuthenticatedListOfCompanies" is enabled (Reference #8010606612).

### Inventory Control

Fixed an issue where incorrect quantities were posted to the inventory after changing the unit of measure during a transfer in the IC Transfers web screen (Reference #8010769330).

### Bank Services

Support for OFX version 2.x (XML-based) statement files has been added (Reference #8010617262).

### Accounts Payable

We will now display a warning during T5018 (CPRS) XML generation if special characters are present in the Transmitter, Payer or Vendor information.

### Accounts Receivable

Fixed an issue in AR Invoice Entry (Web) where the item detail tax class displayed the customer’s tax class instead of the item’s tax class (Reference #8010855250).

#### Order Entry

Fixed an issue in OE Credit/Debit Note Entry where the item’s extended cost was not updated when the Default Order UOM in OE Options was set to Pricing Unit (Reference #8010837387).

## Sage 300 Product Update 1 program fixes

The following sections describe program fixes in Product Update 1.

### Accounts Payable

Fixed a problem that occurred when one or more users simultaneously printed AP web reports, such as Letters & Labels, Aged Retainage, Vendors and Vendor Transactions (Reference #8010583503).

### Order Entry

Fixed a problem when promoting a quote to an order in CRM, optional fields defined in the quote detail lines were not correctly mapped to the corresponding order detail lines (Reference #8010507929).

## Sage 300 2026 program fixes

Sage 3002026 includes program fixes for some problems that exist in the most recent previous version (Sage 300 2025 Product Update 2). The following sections describe these program fixes.

#### Bank Feeds

Fixed an issue when Reconcile E-statement/bank feeds does not download currencies from a specific bank.

#### Bank Entry

Fixed an issue on the Bank Entry web screen where Distribution Sets were not appearing in the finder for single currency companies (Reference #8010457859).

#### Purchase Order

Fixed a performance issue in the Requisition Number finder in the Purchase Order screen's Create PO From Requisition popup for both Web and Desktop (Reference ##8010437682).

#### Project Management

Fixed a performance issue when loading contracts in the PJC Contract Maintenance screen (Reference #8009514617).

#### General Ledger

Fixed an issue where the focus will drop when print previewing an FR Financial Statement using Excel 64 bit (Reference #8010452288).

#### Sales Analysis

Fixed an issue when running Sales Analysis as a scheduled task in AUTO mode (Reference #8010483035).

## General Information

- Sage 300 2026 supports upgrades only from version 5.6 or later.

- If you are upgrading from an earlier version, you must upgrade all Sage 300 programs to 2026 at the same time. Sage 300 2026 programs do not work with programs from earlier versions.

- If you have a subscription license, you don't need to enter serial numbers and activation keys for individual Sage 300 applications. When the License Manager appears during installation, the only license information you need to enter is your Client ID, Company Name, and Serial Number. After you've entered this information, ensure that you have internet access, and then click Refresh to verify your subscription.

- If you do not have the following programs, which are required to use Sage 300, they are installed with Sage 300:

- MSXML (Microsoft XML Core Services) 6.0

- Microsoft .NET Framework 4.8

- Product documentation for Sage 300 is available from the Sage 300 Product Documents website.

## Compatibility with other programs

For a complete list of compatible programs, database platforms, and operating systems, see the Sage 300 2026 Compatibility Guide, available from Sage Knowledgebase article 222924950026777.

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

- Product Update 3

## Removing Sage 300

Before removing Sage 300, you must:

- Close all instances of the Sage 300 Desktop.

- Close all applications that integrate with Sage 300.

- Stop all Sage 300 services that are running, such as Sage 300 .Net Remoting Service.

To remove Sage 300 2026 programs:

- In Windows' Control Panel, click Programs And Features.

- Open Uninstall Or Change A Program, and then:

- To remove all Sage 300 programs, double-click Sage 300 2026.
- To remove individual Sage 300 programs:

- Click Sage 300 2026, and then click Change. (Do not double-click Sage 300 2026.)
- Click Modify, and then use the Select Features screen to select the programs you want to install and clear the selections for programs you want to remove.

## Sage 300 Payroll

Sage 300 2026 includes Canadian and US Payroll. For more information, see the related release notes, which you can find on the Sage 300 Product Documents website.

Note: Canadian and US Payroll may not be available in all regions.

## Sage 300 Intelligence Reporting

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

Published: September 14, 2026

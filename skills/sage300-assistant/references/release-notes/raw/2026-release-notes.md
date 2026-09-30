<!-- source: https://help.sage300.com/en-us/2026/classic/Content/ReleaseDocs/ReleaseNotes.htm | version: Sage 300 2026 | page published: September 14, 2026 | extracted: 2026-09-23 by scripts/extract_release_notes.py -->

# Sage 300 2026 Release Notes

Thank you for choosing a Sage business management solution.

These release notes contain important information about Sage 300, including information about product changes that are not in the documentation.

Product updates contain modified versions of one or more Sage 300 program components. A product update is not a full upgrade or a product replacement. Each product update is valid only until we release the next product update or the next version of Sage 300.

Depending on your purchase agreement, some features described here may not be available in your product.

For more information about feature availability, see Sage Knowledgebase article 220924460105946 .

## What's new in Product Update 3

This section contains a summary of new features and changes in Product Update 3.

### General improvements

This release includes the following new features and improvements in both Sage 300 web screens and Sage 300 classic screens:

### System Manager

For Web Screens, reports that have been customized to support additional Crystal Report parameters can now display a parameter entry dialog similar to the Desktop implementation. To enable this behavior, set the ReportAllowCustomParameters setting in the web.config file from false to true. Enabling this feature will affect the display of the Export Dialog screen's performance, including reports that do not use custom parameters.

### Project and Job Costing

You can now drill down to Payroll Check Inquiry from PJC Transaction History for job-related payroll transactions in web screens.

### Order Entry

A new Update Customer Number security right has been added to Security Groups for Order Entry. If a user attempts to change the customer number after detail lines have been entered in any of the following screens, they will receive an error:

- OE Order Entry

- OE Shipment Entry

- OE Credit/Debit Note Entry

The customer number can still be changed if all detail lines are deleted first. To allow users to change the customer number, go to Security Groups for Order Entry and check the Update Customer Number right. This applies to both Classic and Web screens.

### Program fixes

This product update also includes program fixes. See the list of fixed issues in Technical Information for more information.

## What's new in Product Update 2

This section contains a summary of new features and changes in Product Update 2.

### General improvements

This release includes the following new features and improvements in both Sage 300 web screens and Sage 300 classic screens:

#### System Manager

Sage Help Agent is now available to help answer some of your questions about Sage 300.

A progress meter has been added during the component registration phase of Workstation Setup.

Information Center now launches at the center of the Sage 300 desktop prior to opening a company.

#### General Ledger

A warning now appears when attempting to reverse a subledger batch in General Ledger, helping prevent potential reconciliation discrepancies between GL and its associated subledgers.

#### Bank Services

Support for OFX version 2.x (XML-based) statement files has been added (Reference #8010617262).

#### Sage 300 Web API

The IC Manufacturers' Item end-point is now available.

#### Sage Intelligence

Sage Intelligence has two new features:

- Sage Intelligence in Sage 300 now supports workstation-level scheduling, enabling scheduling across individual workstations.
Note: This supports independent configuration of report output file paths per workstation for multi - workstation setups.

- The Scheduling Service now supports meta data repositories on network shares in Sage 300 workstation environments, securely managing the credentials needed to access the repository.

### Program fixes

This product update also includes program fixes. See the list of fixed issues in Technical Information for more information.

## What's new in Product Update 1

This section contains a summary of new features and changes in Product Update 1.

### General improvements

This release includes the following new features and improvements in both Sage 300 web screens and Sage 300 classic screens:

#### New Information Center Icon

There is a new Information Center icon available and accessible on the Desktop menu or ribbon.

Note: The Information Center icon is available to all languages supported by Sage 300 Desktop. However, its content is only available in English.

#### Web Screens

We have new PJC setup web screens available with this release:

- Categories

- Employees

- G/L Integration

This Bank enhancement now supports Payroll in the following Bank Web Screens:

- Bank Transaction History Inquiry

- Bank Reverse Transactions

### Program fixes

This product update also includes program fixes. See the list of fixed issues in Technical Information for more information.

## What's new in Sage 300 2026

This section contains a summary of new features and changes in the 2026 release.

Important: If you are using Payroll Web Screens and upgrading Sage 300 from version 2024 or version 2023 to this version, make sure you re-install the latest Payroll Tax Update with the Payroll Web Screens option checked. Otherwise, you might encounter error using Web Screens or the Payroll Web Screens may not be visible.

Important: If you are using Sage 300 Web Screens (even without Payroll) and are upgrading Sage 300 from any version prior to 2025, you must uninstall Sage 300 Web Screens prior version first before installing version 2026. To do so:

- Go to Control Panel > Programs > Programs > Features, select Sage 300
- Click Change
- Select Modify in the Sage 300 wizard
- Click Next
- Uncheck Web Screens in the next screen.
- Run the rest of the installer using defaults
- When you install Sage 300 2026 for the upgrade, select the Web Screens option.
Please refer to Knowledgebase article: 250808163127480 .

Important:
If you are using the Sage 300 Global Search feature and plan to perform a Sage 300 Repair from Windows Programs and Features, please backup and uninstall Global Search first by selecting the Modify option. Otherwise, you may encounter issues during the repair process.
After running Repair, you may reinstall Global Search using the Modify option. Once it's installed again, go to Database Setup; edit and save any company (without making any changes) for Global Search to work.

This release includes the following new features and improvements in both Sage 300cloud web screens and Sage 300 classic screens:

#### Sage HR Integration

We have created a new version of Sage HR Integration to be compatible with Sage 300 2026.0, with improved overall performance.

Note: Sage HR Integration 8.1 is only compatible with Sage 300 v2026 and up.

Note: Sage HR Integration requires Payroll with Tax update Q3 2025 8.0 E - September 18, 2025 or later to be active.

#### System Manager

The RegAcc.log will now show the failure if an exe fails to register.

Added Bangladesh Taka (BDT) to the default set of currency codes initialized when a new system database is activated.

Removed obsolete currencies that have been replaced by the Euro (EUR) or are no longer in use.

#### Accounts Receivable

In the AR Invoice entry finder, you can now search by customer name.

You can now export from the AR Customer List UI instead of printing to preview or file first.

#### Accounts Payable

In the AP Invoice entry finder, you can now search by vendor name.

#### General Ledger

We have added a new functionality that allows you to export Optional Fields for Posted Transactions in GL Transaction History.

#### Inventory Control

A new Last Processed By field has been added to the Day End Processing screen. It will display the User ID of the last user that ran Day End Processing.

#### Web Screens

We have new PJC setup web screens available with this release:

- Contract Structures

- Segment Codes

- Miscellaneous Expenses

- Options

- Optional Fields

- Projects

- Overhead Expenses

- Subcontractors

- Charges

### Program fixes

This product update also includes program fixes. See the list of fixed issues in Technical Information for more information.

Published: September 14, 2026

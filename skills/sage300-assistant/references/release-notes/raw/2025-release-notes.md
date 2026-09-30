<!-- source: https://help.sage300.com/en-us/2025/classic/Content/ReleaseDocs/ReleaseNotes.htm | version: Sage 300 2025 | page published: September 10, 2026 | extracted: 2026-09-23 by scripts/extract_release_notes.py -->

# Sage 300 2025 Release Notes

Thank you for choosing a Sage business management solution.

These release notes contain important information about Sage 300, including information about product changes that are not in the documentation.

Product updates contain modified versions of one or more Sage 300 program components. A product update is not a full upgrade or a product replacement. Each product update is valid only until we release the next product update or the next version of Sage 300.

Depending on your purchase agreement, some features described here may not be available in your product.

For more information about feature availability, see Sage Knowledgebase article 220924460105946 .

## What's new in Product Update 6

This section contains a summary of new features and changes in Product Update 6.

### System Manager

For Web Screens, reports that have been customized to support additional Crystal Report parameters can now display a parameter entry dialog similar to the Desktop implementation. To enable this behavior, set the ReportAllowCustomParameters setting in the web.config file from false to true. Enabling this feature will affect the display of the Export Dialog screen's performance, including reports that do not use custom parameters.

### Order Entry

A new Update Customer Number security right has been added to Security Groups for Order Entry. If a user attempts to change the customer number after detail lines have been entered in any of the following screens, they will receive an error:

- OE Order Entry

- OE Shipment Entry

- OE Credit/Debit Note Entry

The customer number can still be changed if all detail lines are deleted first. To allow users to change the customer number, go to Security Groups for Order Entry and check the Update Customer Number right. This applies to both Classic and Web screens.

### Program fixes

This product update also includes program fixes. See the list of fixed issues in Technical Information for more information.

## What's new in Product Update 5

This section contains a summary of new features and changes in Product Update 5.

### General improvements

This release includes the following new features and improvements in both Sage 300 web screens and Sage 300 classic screens:

#### System Manager

Sage Help Agent is now available to help answer some of your questions about Sage 300.

Information Center now launches at the center of the Sage 300 desktop prior to opening a company.

#### Sage 300 Web API

The IC Manufacturers' Item end-point is now available.

#### General Ledger

A warning now appears when attempting to reverse a subledger batch in General Ledger, helping prevent potential reconciliation discrepancies between GL and its associated subledgers.

#### Bank Services

Support for OFX version 2.x (XML-based) statement files has been added (Reference #8010617262).

#### Sage Intelligence

- Sage Intelligence in Sage 300 now supports workstation-level scheduling, enabling scheduling across individual workstations.
Note: This supports independent configuration of report output file paths per workstation for multi - workstation setups.

- The Scheduling Service now supports meta data repositories on network shares in Sage 300 workstation environments, securely managing the credentials needed to access the repository.

### Program fixes

This product update also includes program fixes. See the list of fixed issues in Technical Information for more information.

## What's new in Product Update 4

This section contains a summary of new features and changes in Product Update 4.

### General improvements

This release includes the following new features and improvements in both Sage 300 web screens and Sage 300 classic screens:

### New Information Center Icon

There is a new Information Center icon available and accessible on the Desktop menu or ribbon.

Note: The Information Center icon is available to all languages supported by Sage 300 Desktop. However, its content is only available in English.

### Program fixes

This product update also includes program fixes. See the list of fixed issues in Technical Information for more information.

## What's new in Product Update 3

This section contains a summary of new features and changes in Product Update 3.

### General improvements

This release includes the following new features and improvements in both Sage 300 web screens and Sage 300 classic screens:

#### Payroll Help

We have added a new Accrual Limit feature for US Payroll only.

### Program fixes

This product update includes program fixes. See the list of fixed issues in Technical Information for more information.

## What's new in Product Update 2

This section contains a summary of new features and changes in Product Update 2.

Important! If you are using Sage 300 Web Screens and have installed both Sage 300 Canadian AND US Payroll, it is essential that the same version of the Canadian and US Tax Updates are installed. Failure to do so may prevent successful login to the Web Screens.

### General improvements

This release includes the following new features and improvements in both Sage 300 web screens and Sage 300 classic screens:

#### HR Integration

This product update enhances synchronization between Sage 300 HR Integration and Sage HR.

It also introduces encrypted activity logging, allowing secure file sharing with Customer Support for troubleshooting when needed.

Note: If you are using Sage 300 v2023 deployed using workstation setup, see Knowledgebase article for additional steps to ensure Sage HR Integration continues to function properly.

#### Web Screens

We have an exciting new feature that enables you to create a list of favorite web screens.

You can mark the screens you want to add to the list, and unmark those you want to remove, using the star icon next to each screen.

For more information, see Create a list of favorite screens in Sage 300 Web.

We have also improved the overall performance of web screens.

#### Bank Feeds

The bank feeds feature has been updated to align with current technology requirements. As a result, you will go through an on-boarding process when using it.

The on-boarding process requires you to create a new or use an existing Sage ID to setup bank feeds.

Note: If you already have bank feeds set up, the on-boarding process will be followed by a behind-the-scenes migration of the existing setup to the new bank feeds.

#### Sage Intelligence

Sage Intelligence has two new features:

- Auto-Bulk Import, with the following functionality:

- Detects new reports automatically when the software launches.

- Introduces a comprehensive progress overview screen which provides a clear view of the total import progress and allows users to cancel the import if needed.

- Fully supports consolidation reports, enhancing both the new Auto-Bulk and the existing manual Bulk Import processes.

- Report Scheduling which:

- allows you to automate report generation directly within the application;

- enables you to set daily or weekly schedules for your reports, with the ability to specify exact times and days;

- ensures timely execution and saves the output to the specified location.

### Program fixes

This product update also includes program fixes. See the list of fixed issues in Technical Information for more information.

## What's new in Product Update 1

Important! If you are using Sage 300 Web Screens and have installed both Sage 300 Canadian AND US Payroll, it is essential that the same version of the Canadian and US Tax Updates are installed. Failure to do so may prevent successful login to the Web Screens.

This section contains a summary of new features and changes in Product Update 1.

### General improvements

This release includes the following new features and improvements in both Sage 300 web screens and Sage 300 classic screens:

#### Accounts Payable

We have updated the T5018 (CPRS) forms for Tax Year 2024.

### Program fixes

This product update also includes program fixes. See the list of fixed issues in Technical Information for more information.

## What's new in Sage 300 2025

This section contains a summary of new features and changes in the 2025 release.

This release includes the following new features and improvements in both Sage 300cloud web screens and Sage 300 classic screens:

#### Payroll

Sage 300 US and Canadian Payroll web screens are now installed by the Payroll Tax Update installation programs (beginning with Tax Update CT80D_Q32024 - September 19, 2024/UT80D_Q32024 - September 19, 2024) and not by the Sage 300 core installer.

Note: To use Payroll web screens with 2025.0 you must install Canadian and/or US Tax Update: CT80D_Q32024 - September 19, 2024/UT80D_Q32024 - September 19, 2024 or higher.

#### General Ledger

You can now bring up transaction lists by double-clicking on an account in the General Ledger Chart of Accounts.

In addition to printing General Ledger transactions, you can also export them to programs such as Excel.

These General Ledger features are available on web screen and Desktop.

#### System Manager

Access to Sage Information Center is now available on web screens.

Click on Information Center to access Sage 300 product resources and new updates.

#### Sage Intelligence

Sage Intelligence has been updated to a new version. Further information is in the Technical Information section.

#### eInvoicing

eInvoicing for sending invoices, credit notes and debit notes to the Malaysian Government is now available.

It requires separate installation as well as Sage 300 2024 PU2 or higher.

For more information, please see the User Guide and Online Help.

#### HR Integration

In addition to installing and activating 2025.0, you will need to install and activate Sage HR Integration v8.0.

In a Workstation Setup environment, you will need to register each workstation by performing wssetup.cmd.

Refer to Sage 300 Online Help for more information.

Tip: To avoid issues before you begin running Sage HR integration on the workstation, ensure Payroll 8.0 has at least tax update “C” installed on the server.

To begin:

1. If applicable, uninstall the existing workstation setup.

2. Install the workstation setup (wssetup.exe) that comes with the product update.

3. Run the wssetup.cmd

### Program fixes

This product update also includes program fixes. See the list of fixed issues in Technical Information for more information.

Published: September 10, 2026

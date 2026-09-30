<!-- source: https://docs.sage.com/docs/en/customer/300erp/2024/open/Sage300_CompatibilityGuide.pdf | version: Sage 300 2024 | document last updated: November 4, 2025 | extracted: 2026-09-23 by scripts/extract_pdf_text.py -->

Sage 300 2024

Compatibility Guide

November 2025

This is a publication of Sage Software, Inc.

- 2025 The Sage Group plc or its licensors. All rights reserved. Sage, Sage logos, and Sage
product and service names mentioned herein are the trademarks of The Sage Group plc or its
licensors. All other trademarks are the property of their respective owners.

Last updated: November 4, 2025

Contents

Overview                                       1

Unlisted platforms not supported               1

Product updates and program fixes              1

Compatibility with third-party programs        2

Checking hardware compatibility                2

Implementation scenarios                       2

Sage 300 2024 Compatibility                    3

All environments                               3

Virtual environments                           3

Citrix/Terminal server environments            5

Database Platforms and Operating Systems       6

Database server operating systems              6

Sage 300 application server operating systems  6

Workstation operating systems                  7

Sage 300 Web Screen Requirements               8

Server requirements                            8

Web browser requirements                       8

Hardware Requirements                          9

Recommended configurations                     9

Hardware Notes                                 11

Software end-to-end Compatibility Matrix       13

                                               i

Overview

The information in this Compatibility Guide applies specifically to Sage 300 2024
Standard, Advanced and Premium editions.
This document is intended to cover information regarding the compatibility of
various operating systems with Sage 300 2024.
Any operating system not listed in this documents is not compatible with the current
version of Sage 300.
Before installing Sage 300 2024, review this guide and the following documents:
l Upgrade Guide
l Installation and Administration Guide
l Release Notes
You can find more details and instructions on this Knowledgebase article
support.na.sage.com or by contacting Customer Support.

Unlisted platforms not supported

Sage Customer Support Services provide support for Sage 300 only on the platforms
listed as supported in this document.
You can submit requests to support additional operating systems, as well as product
enhancements suggestions at
https://www5.v1ideas.com/TheSageGroupplc/Sage300ERP .
Alternative support options may be available through your Solution Provider.

Product updates and program fixes

Current product updates are available for download from support.na.sage.com.

If a product update is available, install the latest product updates from Sage 300 after
program installation is complete.
Program fixes will continue to available for the current version of the software as needed
and according to a planned release schedule.

        Note: Some program fixes are only available as hotfixes and should be installed
        only if you are experiencing the specific problems they address.

Compatibility with third-party programs

If you also use third-party applications or enhancements, always contact the developer of
the third party product to verify compatibility before installing any product updates or
program fixes.

Checking hardware compatibility

Incompatible hardware can cause problems such as data corruption.
Verify all that hardware you use to run Sage 300 is compatible with your operating
system.
For more information, refer to the applicable Hardware Compatibility List at
http://www.microsoft.com/hardware/en-us/support/compatibility

Implementation scenarios

When planning your Sage 300 implementation, review the `Recommended
configurations' section (pages 9 - 11) for typical small business, midsize business, and
large enterprise implementation scenarios.

     Note: Recommended configurations are intended to serve only as a guideline.
     Actual requirements will vary depending on your system configuration and the
     programs and features you choose to install. Additional hard disk space may be
     required.

Sage 300 2024 Compatibility

All environments

The following points apply to all configurations when upgrading to Sage 300 2024:
l Sage is committed to supporting future Microsoft operating systems as they are

   released to market for all Sage 300 applications. However, this does not include
   release candidates, beta, or pre-beta operating systems. As new operating systems
   are scheduled for final general release, Sage will evaluate their compatibility and
   update this document based on those evaluations.
l The Analysis module for Sage 300 Intelligence Reporting is not compatible with
   Microsoft Excel 2003.

Virtual environments

Sage 300 2024 is supported in Vmware ESX, Microsoft Hyper-V and
Microsoft Azure virtual environments.

     Note: Our support teams will address only application-related issues that can be
     replicated in a physical environment and will not address performance issues in a
     Vmware, Hyper-V virtual or Microsoft Azure virtual environments.

Points and recommendations related to virtual environments:

l Consult with an expert. Implementing a virtual server environment is very complex,
   we recommend that you consult with a vendor-certified virtual server consultant.

     Important! Ask your consultant to commit to matching or mirroring the performance
     requirements listed in the "Hardware requirements" chapter of this document (pages
     9 - 11). A certified virtual server consultant should be able to provide you with a
     performance baseline report that includes expected maximum processing
     throughput per active instance and expected performance trends as additional
     virtual instances come online. This document should also include the expected
     margin of error during peak business operating hours.

l Ensure sufficient resources and RAM. Each virtual environment should have
   sufficient resources for the operating system and installed applications. There is
   never enough memory to share among virtual devices running on a virtual server. We
   recommend that server RAM be configured to the maximum that the server hardware
   can support. Most server hardware that is certified by the virtual server vendor can
   support at least 32 GB of RAM.

l Deploy at least two virtual servers. If not properly implemented, a virtual
   environment can be a single point of failure. A single point of failure should be
   avoided at all costs. The virtual server community always recommends deploying at
   least two virtual servers, along with a fail-over strategy.

l Avoid over-committing application pools. When running in a VMware environment,
   avoid over-committing VM application pools. Allocating more resources that the
   hardware can support can cause performance problems.

l Check hardware compatibility. Virtual server vendors always support a list of
   compatible server hardware devices. Therefore, ensure that the virtual server your
   firm is considering is on the hardware compatibility list.

l Understand memory allocation. Each virtual server vendor implements vastly
   different memory allocation strategies, so you need to be familiar with their specific
   strategy. For example, VMware dynamically allocated memory to an active virtual
   image, allowing the administrator to set a maximum memory limit, but allocating that
   maximum memory only as needed.

l Plan for network bandwidth. Network bandwidth may become a bottleneck in virtual
   network environments. Be prepared to add more than four network interface cards to
   your virtual server. Ask your virtual server platform expert to investigate the ability of
   these network interface devices to `team up'. When network bandwidth becomes a
   bottleneck, network interface teaming may be the easiest solution, without resorting
   to the more complicated strategy of breaking up your network into smaller segments.

Citrix/Terminal server environments

Citrix/Terminal servers should be dedicated for applications and database engines
should be separate from the Citrix/Terminal server. You need to optimize Citrix/Terminal
server sessions for performance and to ensure that printers are compatible.

     Note: The full Sage 300 System Manager and programs need to be installed on the
     Citrix/Terminal servers. Sage support teams will address only application-related
     issues that can be replicated in a standard client/server environment and will not
     address performance issues in a Citrix/Terminal server environment.

Database Platforms and Operating
Systems

This section lists supported database platforms and operating systems for Sage 300
2024.
Sage reserves the right not to provide support for operating systems and database
engines not listed in the Compatibility Guide and/or no longer supported by their vendors.

Database server operating systems

Microsoft SQL Server 2019 or 2022 are supported for use as the database server for
Sage 300 2024.
Note the following:
l Microsoft SQL Server Enterprise, Standard and Express editions are supported.
l We recommend using a binary collation method such as Latin1_general_bin for

   Miscrosoft SQL databases
l See Microsoft's websites for limitations of their databases.

Sage 300 application server operating systems

Windows Server 2019, 2022 or 2025 are supported as the application server
for Sage 300 2024.
Note the following:
l Sage supports only the 64-bit version of any application server operating system.
l Terminal Server and Citrix XenApp are supported only for Sage 300 Classic (Visual

   Basic) programs, no for web screens.

Workstation operating systems

The 64-bit versions of Windows 10, 11 are supported as the
workstation operating system for Sage 300 2024.

        Windows 10 Note: To minimize disruption and ensure accurate payroll
        processing and reporting, Sage will test the upcoming Sage 300 payroll tax
        updates for compatibility with Windows 10. This includes the Sage 300 tax
        updates in December 2025, January, and March 2026.
        The Sage 300 product updates scheduled for November 2025, including versions
        2026.1, 2025.4, 2024.8, will also be tested with Windows 10.
        Starting with releases planned for April 2026, Sage 300 will no longer be tested for
        Windows 10 compatibility. All customers should move to a supported operating
        system or environment prior to installing those releases.
Supported editions are Windows 10, 11 : Pro and Enterprise editions.
Additional notes:
l Microsoft Excel 2016 (32 or 64 bit), 2019 (32 or 64 bit), 2021 (32 or 64 bit), 2024 (64
   bit), or Excel 365 (32 or 64 bit) is required on each workstation running the desktop
   GL Financial Reporter.

          l Financial Reporter for the web requires Excel 365 (64 bit only) on both the
             server and workstation.

l Microsoft Outlook 2016 (32 or 64 bit), 2019 (32 or 64 bit), 2021 (32 or 64 bit), 2024
   (64 bit), or Outlook 365 (32 or 64 bit) is required on each workstation that uses email
   in the Print Destination setting.

l Microsoft Application Virtualization (App-V), which is another method to deploy
   Microsoft Office is not supported.

Sage 300 Web Screen Requirements

Server requirements

To support web screens, the Sage 300 server requires Microsoft Windows Server 2019,
2022 or 2025 with IIS installed, including static content and ASP.Net.
Web screens require a Portal database, which can be the same database you use for the
Sage 300 Portal.
The Portal database must use a supported version of Microsoft SQL Server.
Financial Reporter for the Web (FRw) requires Microsoft Excel 365 installed on the
Server.

Web browser requirements

To view web screens, use currently supported versions of Microsoft Edge, Google
Chrome or Mozilla Firefox.

Hardware Requirements

Recommended configurations

                  Standard              Advanced                     Premium
                                                                        10+
Number of users   1-5                   5-10
     Modules                                                       Financials &
                       Financials &          Financials &     Operations Modules
                  Operations Modules*   Operations Modules

Database engine   Microsoft SQL         Microsoft SQL         Microsoft SQL
                    Express or             Standard              Standard
                   Standard**

Database size     0.25-5 GB 5-10 GB 0.25-5 GB 5-10 GB 0.25-5 GB 5-10 GB

                  10 GB+                10 GB+                10 GB+

                  Windows Server        Windows Server        Windows Server

                  Standard Windows Standard Windows Standard Windows

                  Server Standard with Server Standard with Server Standard with

Operating system  Terminal Services Terminal Services Terminal Services

                  Windows Server        Windows Server        Windows Server

                  Standard/Enterprise Standard/Enterprise Standard/Enterprise

                  with Citrix           with Citrix           with Citrix

Reporting         Standard Moderate Standard Moderate Standard Moderate

                  Intensive             Intensive             Intensive

Workstation          Intel Core i5 or      Intel Core i5 or      Intel Core i5 or
                  higher Intel Core i5  higher Intel Core i5  higher Intel Core i5
                  or higher Intel Core  or higher Intel Core  or higher Intel Core

                       i5 or higher          i5 or higher          i5 or higher
                                              8GB RAM               8GB RAM
                        8GB RAM              100MB for             100MB for
                       100MB for          workstation files     workstation files
                    workstation files   Windows 10, 11**      Windows 10, 11**
                  Windows 10, 11**

Sage 300 Server      Intel quad-core       Intel quad-core    Intel quad-core or
                  processor or higher   processor or higher   Xeon processors
                                                               64 GB RAM (or
                     32 GB RAM (or         32 GB RAM (or

                         higher)               higher)              higher)
                 5GB for application   5GB for application  5GB for application

                          files                 files                 files

                 Intel quad-core       Intel quad-core

                 processor or higher processor or higher       Intel quad-core
                                                            processor or higher
                 16GB RAM              16GB RAM
                                                                 32GB RAM
Sage 300 Web     5GB for application 5GB for application    5GB for application
Screen Server
                 files                 files                          files

                 Sage 300 Server can Sage 300 Server can

                 also be used,         also be used,

                 additional resources additional resources

                 required.             required.

Database Server      Intel quad-core      Intel quad-core      Intel quad-core
                  processor or higher  processor or higher  processor or higher

                    32 GB RAM (or         32 GB RAM (or        64 GB RAM (or
                          higher)              higher)              higher)

                    Windows Server       Windows Server       Windows Server
                   2019, 2022, 2025     2019, 2022, 2025     2019, 2022 , 2025

                           (x64)                (x64)                (x64)

                 SQL Server 2019 or    SQL Server 2019 or   SQL Server 2019 or
                           2022                 2022                  2022

                 500GB free hard disk   1TB free hard disk  1.5TB free hard disk
                           space                space                space

                  RAID 5/10 for SQL    RAID 5/10 for SQL     RAID 5/10 for SQL
                         data files           data files           data files

                  RAID 1 for SQL log   RAID 1 for SQL log   RAID 1 for SQL log
                            files                files                files

                 Sage 300 Server can
                      also be used,

                 additional resources
                         required.

Citrix Terminal                                              Intel quad-core or
     Server                                                   Xeon processor

                                                              Windows Server
                                                             2019, 2022, 2025

                                                                Standard with
                                                            Terminal Services

                                                                     (x64)

                                                            64GB RAM capable

Sage CRM Server                                of supporting 40
                                               concurrent user

                                                    sessions

                 Refer to Sage CRM Supported Platform
                                       Matrix

Windows 10 Note: To minimize disruption and ensure accurate payroll processing
and reporting, Sage will test the upcoming Sage 300 payroll tax updates for
compatibility with Windows 10. This includes the Sage 300 tax updates in
December 2025, January, and March 2026.

The Sage 300 product updates scheduled for November 2025, including versions
2026.1, 2025.4, 2024.8, will also be tested with Windows 10.

Starting with releases planned for April 2026, Sage 300 will no longer be tested for
Windows 10 compatibility. All customers should move to a supported operating
system or environment prior to installing those releases.

Hardware Notes

l Additional applications require more resources. Recommendations are based on a
   standalone server with little to no additional network traffic. Running additional
   applications on the same server will require additional resources.

l Add RAID to protect data. Adding RAID to your storage configurations is one of the
   most coss-effective ways to maintain both data protection and access. For the
   database and file servers, we recommend using RAID 10 (minimum RAID 5). For the
   application and web servers, we recommend using RAID 1.

l Plan for different user types. It is important to keep in mind what type of user will be
   working for the system. For example, 100 users working in Operations modules will
   use the system more intensively than 100 users working in Financial modules. The
   guidelines in this document are intended for users of Operations modules on a non-
   customized system, with little to no additional processing or network traffic.

l Plan for backup and recovery. Each site must have adequate backup and recovery
   capabilities. We strongly recommend that you set up a `hot standby' system with a
   backup database. This standby system should have a similar configuration to the
   primary production system. The standby system can also be used for development
   and testing.

l Plan for disk space requirements. The amount of required disk space varies widely,
   depending on the number of customer records, archiving plans, and backup policies.
   Required disk space can also vary depending on the amount of information held for
   each customer. Therefore, it is important to estimate disk space requirements prior to
   installation, and to purchase sufficient disk storage to allow for significant growth in
   the volume of data.

l Protect against power outages and surges. We recommend that you uswe an
   uniterruptible power supply.

l Understand the effect of product customizations. Product customizations can
   significantly affect the performance of Sage 300 and should be evaluated carefully
   when specifying hardware.

Software end-to-end Compatibility
Matrix

The software versions listed here have been tested and are compatible with Sage
300 2024.

Software           Version  Additional Modules
Sage CRM           2025 R1  A/R, A/P, O/E, P/O, PJC
Sage Fixed Assets  2026.0   G/L, A/P, P/O
Sage HRMS          Q3-2025

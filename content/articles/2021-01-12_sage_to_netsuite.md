Title: Migrating from Sage to Netsuite
Date: 2021-01-12
Tags: Accounting, Software, Case Study, Netsuite, Sage
Summary: One customers journey from Sage50 to Netsuite
Image: pexels/pexels-negative-space-160107.jpg

In early 2020, I migrated a client from [Sage50](https://www.sage.com/en-gb/products/sage-50cloud/) to [Oracle's Netsuite](https://www.netsuite.com/portal/home.shtml). Read about how the project was implemented.

## Background

The client is a fast growing organisation made up of several trading legal entities. The organisation was characterised by low value, high volume transactions. Sage50 was becoming a hinderence to good decision making and becoming onerous for the finance team.

Each of the client's locations were operated under a separate legal entity. However, this was making reporting difficult in Sage as each legal entity has it's own instance of Sage. Creating consolidated accounts means exporting data out as a csv file and having some monster reporting spreadsheet. Because Sage treats each legal entity separately, the finance team were frequently having to log in and out of Sage to change companies.

Sage50 can be backed up to the cloud, but does not offer a good hosted solution. This means that you need to have good, frequent backups. If you don't, it could go very wrong. Xero and Netsuite are both examples of cloud software, meaning that they are on the internet and someone else will back up the data. Sage50 cannot be used remotely, so can be difficult if there is a need for staff to work offsite.

The client has lots of different sytems and pieces of software in use and wanted as many as possible to be automated. Sage50 doesn't relly have the capability to automate data entry. Various data can be imported, but these are manually done. It's better than nothing, but software like Xero and Nesuite are better options.

The main criteria of the new software were:

 - Consolidated accounts
 - Strong reporting
 - Scope for automation
 - Off premises

After looking at a number of different providers, the client settled on Netsuite being the right price and mix of the above criteria. Netsuite cannot be bought directly, it needs to be bought through a partner. I wil cover the alternatives in another post.

## Results

Netsuite dramatically improved the reporting within the finance function. The implementation came in on time and within budget. The opening balance date was aligned to the end of a VAT quarter. Aligning to a year end wasn't feasible. Under these circumstances, one would normally have comparative trial balances for each month within the financial year and maybe some year end balances. The trial balance date was 31st Jan, with the year end being 31st Oct. So trial balances for Nov, Dec, and Jan would be the norm. However, we imported a trial balance for every month covering 7 years of trade for multiple legal entities.

### Trial balances

Sage50 has the ability to export csv files containing data. It would not have been feasible to export each trial balance manually to cover the required time period. At least two entities had 7 years worth of data, this would mean exporting at least 170 trial balances. To get the Sage balances in the correct Netsuite format, I exported the data from Sage and wrote a small Python script to read the csv and write a new csv in the correct format for Netsuite. Once the script had been written, it could be run and re-run for any data tweeks before final import to Netsuite. The code took about half a day to write, but saved many hours of manipulating data in a spreadsheet.

### Nominal codes

Sage50 has a four digit code to represent the nominal code, Netsuite is a bit more flexible. The client want to take the opportunity to revise some of the chart of accounts. The old chart of accounts was not consistent over the different Sage entities and was largely the standard chart of accounts that Sage provides. They wanted a consistent chart of accounts and something more fit for purpose. After designing a new chart of accounts, we creating a mapping table to map from the old codes to the new codes. This could then be read by the script above so that the trial balances used the new coding.

### Automation

Due to the high volume, low vale of transactions, the client wanted to have sales imported from the EPOS system into the accounting software. Under Sage, this was done on a weekly basis. The EPOS software did not provide an API, so we wrote a script to crawl over the EPOS provider's back office website and generate an import file. I had previously written this script to generate an import for Sage, so was able to modify slightly to match Netsuite.

Most of the companies bookings were made through an online customer portal. Deposists are taken and then redeemed through the EPOS when a customer is on site. As the deposts were non-refundable, the VAT point was the date of the deposit which complictes the book-keeping slightly. This service did provide an API, so I wrote a script to generate an import file for Netsuite.

The last of the major integrations was for the client's purchasing system. The purchasing system held all orders, delivery notes, and invoices and did three-way matching. Once a day, the software would deposit a csv of invoices onto an FTP server. The integration for this was written by the third party provider as they had experience of this.

These integrations were all run from an AWS EC2 instance specifically created for the purpose of hosting integrations. The EPOS and deposit automations were written in Python and run on a cronjob.
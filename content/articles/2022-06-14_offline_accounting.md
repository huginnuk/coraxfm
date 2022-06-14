Title: Take Your Accounts Offline
Date: 2022-06-14
Tags: Accounting, Gnucash, Plain Text Accounting, VAT, MTD, Cloud Accounting
Summary: Take your accounts out of the cloud and back onto your own computer

There is a huge push accross the accounting industry to push accounts into the cloud. You can find no end of articles that sell the benefits of moving your accounts online and into "the cloud" ([here](https://www.xero.com/uk/guides/small-business-cloud-accounting/), [here](https://quickbooks.intuit.com/uk/blog/cloud-accounting-top-benefits/), [here](https://www.accountingweb.co.uk/community/industry-insights/the-benefits-of-cloud-accounting), [and many more](https://duckduckgo.com/?t=ffab&q=cloud+accounting+benefits&ia=web)).

Cloud accounting is great for lots of use cases. However, there are some risks:

 - Reliance on the external provider - A cloud provider could terminate your service or there could be outages.
 - Security - Broadly, cloud accounting software is reasinably secure. However, having a publically facing login page does expose the business. Also having lots of different business logging in via the same portal provides a reasonably good attack vector.
 - Recurring Fees - Nearly all cloud accounting software relies on a monthly subscription. Once you stop paying your subscription, no more access. Getting the data out in a readable format can be challenging (thankfully it is easy in [xero](Export-Your-Xero-Transactions-to-Use-in-any-ERP.html)).
 - Expensive - The expense of the software is relative. The basic package of [Xero](https://www.xero.com/), [Sage](https://www.sage.com/), and [Quickbooks](https://quickbooks.intuit.com/) are all around £12/month, £144/year. You can get this bill a bit lower, however, it will come at the cost of a bit more friction.
 - Overkill - For a single director business, cloud accounting is overkill. There are lots of functions that are not needed, and won't be used.

 With this in mind, what is the alternative? This solution works for a very small business. A single director consultancy, or maybe with a few staff. It may be scalable with some work, but that it outside the scope of this post.

 The biggest "problem" that cloud accounting solves is VAT MTD. All businesses that are VAT registered have to use [specific software](https://www.gov.uk/guidance/find-software-thats-compatible-with-making-tax-digital-for-vat) for filing VAT. The answer is VAT bridging software. [TaxCalc](https://www.taxcalc.com/) sells VAT filing software for £17.50 a year. That makes it a lot less money than full-blown accounting software.

 So what to use for the bookkeeping part? Any software that you are able to keep accurate accounts in would work. A spreadsheet would be fine, but would end up being onerous for reconciling and making sure that the data is correct. The VAT bridging software would work well with either [Plain Text Accounting](https://plaintextaccounting.org/) or [Gnucash](https://gnucash.org/) if you'd like a user interface.

 The last part, but most important, is sales invoices. Many banking apps like [Tide](https://www.tide.co/) include invoicing within their app free of charge. Sales invoices can be generated in the app, and then entered as a plain text transation.
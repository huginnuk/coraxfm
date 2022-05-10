Title: Convert Xero Journals for Netsuite and Dynamics
Date: 2022-05-10
Tags: Accounting, Software, Technology, Xero, ERP, Netsuite, Dynamics
Summary: Convert historical Xero journals for use in Netsuite or Dynamics
Image: origin/xero_convert_code.png

Previously, [I wrote about]('Export_Your_Xero_Transactions_to_Use_in_any_ERP.html') exporting your Xero balances to use in any ERP system. [This repository](https://github.com/huginnuk/coraxfm_scripts/) contains the code to generate a JSON object from your Xero transaction history, then convert it into journals for either Netsuite of Dynamics Business Central.

This script assumes that the directory structures is:

<pre>
  - Working Directory
    - xero_export
      - xero_export_1.csv
      - xero_export_2.csv
      ....
      - xero_export_n.csv
    - converted
    - xero_convert.py
</pre>

It also assumes that the file name is: `{company_name}_XERO_GL_{year}_APR_27.txt`. Where `{company_name}` is your entity name and `{year}` is your financial year. When I have exported data in the past, it is easy to download one financial year at a time to have more manageable sizes of data.

When creating opening balances, there are several different methods. You can have a incremental journal for each trial balance, or a cumulative balance that then reverses out. I would recommend having an incremental journal for each month prior to your current year, then a reversing cumulative balance in your current year. The reasons for this is so that you can still run a year end process in each year that you import, and that reversing out any balances will help keep your control accounts in check on the day that you migrate.

The difference between the methodologies are shown below:

Incremental:
<pre>
  DATE        DR  CR
  202x-01-31  100
  202x-02-28  120
  202x-03-31  130
</pre>

Cumulative:
<pre>
  DATE        DR  CR
  202x-01-31  100 
  202x-02-01      100
  202x-02-28  220
  202x-03-01      220
  202x-03-31  350
</pre>

Combined
<pre>
  DATE        DR  CR
  202x-01-31  100
  202x-02-28  120
  202x-03-01      120
  202x-03-31  350
</pre>

The scripts included generate one trial balance per month in a single journal. It is non-cumulative so creates incremental journals. This is ideal for generating journals up to your last year end. To convert the Xero export, first run [xero_convert.py](https://gitea.huginn.uk/tom/coraxfm_code/src/branch/master/xero_convert.py) then either [netsuite_journals.py](https://gitea.huginn.uk/tom/coraxfm_code/src/branch/master/netsuite_convert.py) or [dynamics_convert.py](https://gitea.huginn.uk/tom/coraxfm_code/src/branch/master/dynamics_convert.py) depending on what your new ERP is. You will likely need to tweek these scripts to your own requirements.

These scripts assume that you are retaining your existing chart of accounts and reporting cateogries. However, it is pretty simple to remap nominal codes or categories within the Python code.
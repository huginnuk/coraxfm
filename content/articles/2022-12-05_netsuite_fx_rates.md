Title: Exchange Rates in Netsuite
Date: 2022-12-05
Tags: Accounting, Netsuite
Summary: How do foreign currency translations work in Netsuite

Netsuite is one of my favourite ERP programs for finance. It has great reporting, is relatively easy to use, and looks good too. Where I have found that it really excels is when it is the only finance system of a group of companies. It works really well consolidating results up to a group level. However, it can get a bit confusing how it translates currencies especially with consolidation.

Netsuite performs translations at two different stages: on the transaction and on consolidation. Netsuite holds a daily transaction rate, and three consolidated rate (current, average, historical).

## Transactions
Each subsidiary has a reporting currency. Any foreign currency transaction is translated into the reporting currency on the date of the transaction. Balances get translated at the rate on last day of the reporting period.

When running non-consolidated financial statements for a given subsidiary, Netsuite will give you the results in the reporting currency of the subsidiary.

## Consolidation
Netsuite has one single subsidiary which is the top of the consolidation tree. The reporting currency of this entity is dictated by the edition that you use. For example, UK Netsuite uses GBP.

Consolidated rates are calcluated as part of the period close process. There are three types:
 - Current - This is the closing rate for the period (Usually used for Stock)
 - Average - Average rate for the period
 - Historical - The average rate for the whole history of the account. (Usually used for Equity, Fixed Assets)

Each nominal code has an exchange rate set on it to tell Netsuite how to translate it according to one of the three methods above. Ultimately, all your subsidiaries regardless of their reporting currency will consolidate up to the currency of the lead subsidiary.

## Calculations
To get consolidated financial statements, Netsuite first translates transactions into the reporting currency of the subsidary. Then translates the whole financial statement into the reporting currency of the lead subsidiary.

On the whole, consolidated rates and daily exchange rates should match, however, sometimes they may not. Netsuite can automatic rates from either HSBC or Xignite. These do not triangulate, the inverse of an exchange rate is not always 1/n. This can lead to a situation where a GBP transaction in a USD entity, could be a different GBP value when consolidated. The fx variance is a small number, but on big transsactions can make a big difference....

## Cumulative Translation Reserve
When consolidatding a trial balance, balance sheets will end up imbalanced. This is due to the different exchange rates (current, average, historical) being used. The balancing figure on consolidation ends up going to the cumulative translation adjustment. Have enough exchange volatility and this can be a big number too.

Netsuite does not post a journal for the cumulative translation adjustment, it calculates it when running financial statements.

## Conclusion

Exchange rates can be pretty complex, here is a list of things to note:

 - Netsuite has two types of exchange rate: daily rates and consolidated rates.
 - Daily rates come from HSBC or Xignite
 - Daily rates don't always work both ways. EUR->GBP is not the same as GBP->EUR
 - Consolidated rates are calculated from daily rates
 - Consolidated rates are three different types (current, average, historical)
 - Translation formula = transaction * daily fx rate * consolidated rate
 - Cumlative translation adjustment is the value of the imbalance caused on consolidation
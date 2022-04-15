Title: Accounting Database Design
Date: 2021-07-27
Tags: Accounting
Summary: Database choices in accounting software
Image: origin/database.png

Over the past few years, I have been developing my own accounting software [Hermes](https://hermes.dev.huginn.uk). It has primarily been so that I can learn how to write software, but in an area where I know what the end product should look like. It's been an interesting process thinking about how the data interacts and what the structure should be.

Double entry book-keeping is great. It makes it easy to have some in-built checks in your database. However, that doesn't automatically translate into some good database design. When I say "good database design", I mean that I had issues trying to make a pure double-entry system work in my database. I don't mean good from the point of view of best practice.

When I first wrote Hermes, I wasn't sure what type of organisation or individual I was writing for. So I created a double-entry adjacent system. Every entry had to have an entry in a bank account. It was double entry in the sense that there were always to entries, but it wasn't particularly flexible. I was trying to mimic my workflow in Gnucash. Basically, I would import my bank statements and code the transactions from there. I think that some other software, [Akaunting](https://akaunting.com/), used this method too. I've not looked at Akaunting for a number of years now, so things might have changed.

What I really wanted in a database was a table that listed all of the transactions in a single table. It might looks something like this:

<table class="table table-sm">
	<tr>
		<th>Date</th>
		<th>Description</th>
		<th>Nominal</th>
		<th>DR</th>
		<th>CR</th>
	</tr>
	<tr>
		<td>2021-07-01</td>
		<td>Spend Money</td>
		<td>Bank</td>
		<td></td>
		<td>50</td>
	</tr>
	<tr>
		<td>2021-07-01</td>
		<td>Spend Money</td>
		<td>Petrol</td>
		<td>40</td>
		<td></td>
	</tr>
	<tr>
		<td>2021-07-01</td>
		<td>Spend Money</td>
		<td>Snacks</td>
		<td>10</td>
		<td></td>
	</tr>
	<tr>
		<td>2021-06-30</td>
		<td>June Salary</td>
		<td>Salary</td>
		<td></td>
		<td>2000</td>
	</tr>
	<tr>
		<td>2021-06-30</td>
		<td>June Salary</td>
		<td>Bank</td>
		<td>2000</td>
		<td></td>
	</tr>
</table>

This is pretty easy to follow. However, the problem that I had with something like this is that if you had multiple bank accounts, anf you wanted to find the balancing transactions, it would be very hard. Sage50 has a transactions screen, where it lists all of the transactions, I was drawing some inspriation from there.

Gnucash is a fully double entry system. It separates out a journal into two parts: transaction and splits. The transaction element contains things that are common: the description, date, and currency. Where the splits contain the value, the account (nominal), and the line description. I did think that this was too complex, but now I understand why it was done that way. You can have a double entry system, and in the database, make a select on the splits to find the opposite entries.

After having a break from Hermes, and a think about the database design, I refactored Hermes to the Gnucash model. Having transactions and splits. 
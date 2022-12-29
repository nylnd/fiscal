# Brass
## Brass bands, brass ~~tacks~~tax.
### A simple, systematic tax liability calculator

Brass is a simple, systematic, tax calculator with soft-coded rate bands.  Specifically, Brass aims to side-step the commonly-seen behaviour of using 'if' statements in tax calculators, and relying on hard-coded tax bands. 

### Brass, broken down

There are two key elements to Brass.

1) Bands - a stream of pairwise tuples with a 'allocator'. Each pairwise tuple, or 'band', comprises a threshold, and a percentage. The allocator dictates the manner in which taxable amounts are allocated between the threshold element of each band - currently the two predominant forms of allocator are provided: 'step', which reflects common tax treatment; and 'slab' which represents flat taxes whose rate is determined by the taxable amount (as in old stamp duty and early SDLT).

2) Liabilities - a calculation of liability stored in breakdown form (a three-element tuple made up of (i) the amount allocated to the band, (ii) the percentage referable to that band and (c) the product of the amount and the percentage.

## Example
To draw an example from Stamp Duty Land Tax (SDLT), a land transfer tax in England and Wales, UK. 

### SDLT - stepped calculation

The applicable bands for a commercial transaction were, after 17 March 2017, as follows:

| Threshold | Percentage |
|-----------|------------|
| £150,000  | 0%         |
| £100,000  | 2%         |
| Surplus   | 5%         |


The bands are allocated on a step basis, so £1m would be allocated as follows:

| Threshold | Percentage | Liability |
|-----------|------------|-----------|
| £150,000  | 0%         | £0        |
| £100,000  | 2%         | £2,000    |
| £750,000  | 5%         | £35,500   |


The total SDLT liability would, therefore, be £39,500.

### SDLT - slabbed calculation

Prior to 17 March 2017, the applicable rates for a commercial transaction were as follows:

| Threshold | Percentage |
|-----------|------------|
| £150,000  | 0%         |
| £100,000  | 1%         |
| £250,000  | 3%         |
| otherwise | 4%         |

The 'slab' basis applied to these rates. This means that the taxable amount is compared with the __cumulative__ thresholds, which are as follows:

| Cumulative Threshold | Percentage |
|----------------------|------------|
| £150,000             | 0%         |
| £250,000             | 1%         |
| £500,000             | 3%         |
| otherwise            | 4%         |

The first cumulative threshold to exceed the taxable amount determines the applicable percentage.  So where the taxable amount was £200,000, the applicable percentage was **1%**.

| Cumulative Threshold | Amount   | Percentage | Liability |
|----------------------|----------|------------|-----------|
| £150,000             |          | 0%         | £0        |
| £250,000             | £200,000 | 1%         | £2,000    |
| £500,000             |          | 3%         | £0        |

Where the taxable amount was £300,000, the applicable percentage was **3%**.

| Cumulative Threshold | Amount   | Percentage | Liability |
|----------------------|----------|------------|-----------|
| £150,000             |          | 0%         | £0        |
| £250,000             |          | 1%         | £0        |
| £500,000             | £300,000 | 3%         | £9,000    |

# Server

The server is written with .NET version 9.

## Overview of the structure:

We first use [yfinance](https://ranaroussi.github.io/yfinance/) to generate some initial data\
for our securities(stocks, ETFs, Forex etc.) populating a MonogoDB instance.

Then we have controllers with endpoints (not REST compliant, yet) for managing authentication and portfolios lifecycle.

The program generates new price for the securities aswell as trading volumes using a select, predefined set of formulas.\

## Future improvements / fixes:

The entire backend is using floats/doubles which is pretty bad when dealing with currencies and money\
because there are rounding errors and representation errors (limitations of FP math).\
Realistically I should refactor everything to either use long and measure everything in cents,\
or, use the equivalent of Java's BigDecimal.

Fix some of the Interfaces to make a better fit for future implementations

class Security {
  constructor(name, isin, type) {
    this._name = name;
    this._isin = isin;
    this._type = type;
    this._quotes = {};
  }

  addQuote(date, exchange, close, open = 0, low = 0, high = 0) {
    // if (typeof date === "string" && typeof exchange === "string" && close === "number") {
    //   console.log('Please specify date, exchange and closing price.');
    //   console.log(`Specified types: date: ${typeof date}, exchange: ${typeof exchange}, close: ${typeof close}`);
    //   console.log(`Specified values: date: ${date}, exchange: ${exchange}, close: ${close}`);
    //   return false;
    // };

    this._quotes[exchange] = {};

    this._quotes[exchange][date] = {
      open: open,
      low: low,
      high: high,
      close: close
    };

    return true;
  }

  get quotes() {
    return this._quotes
  }

}

class Stock extends Security {
  constructor(name, isin, ticker, sharesOut) {
    super(name, isin, 'stock');
    this._ticker = ticker;
    this._sharesOut = sharesOut;
  }

  get ticker() {
    return this._ticker;
  }

  get sharesOutstanding() {
    return this._sharesOut;
  }

  getStockInfo() {
    return {
      Name: this._name,
      ISIN: this._isin,
      Ticker: this._ticker,
      Shares_Outstanding: this._sharesOut
    }
  }
}


class Portfolio {
  constructor(name, brockerage) {
    this._name = name;
    this._brockerage = brockerage;
  }

  getAssets() {

  }
}

stockApple = new Stock('Apple Inc.', 'US0378331005', 'AAPL', 16070000000);
console.log(stockApple.getStockInfo());
if (stockApple.addQuote('2022-10-10', 'Xetra', 144.54, 143.10, 142.92, 144.98)) {
  console.log(stockApple.quotes);
};

from lumibot.brokers import Alpaca
from lumibot.backtesting import YahooDataBacktesting
from lumibot.strategies import Strategy
from lumibot.traders import Trader
from datetime import datetime

API_KEY = "AKSCNLJJVK0CKBTZL6D6"
API_SECRET = "wK5guglwJYmUrc0bsmiROdmJxHG0617UHrgcgnld"
BASE_URL = "https://api.alpaca.markets"

ALPACA_CREDS ={
    "API_KEY":API_KEY,
    "API_SECRET":API_SECRET,
    "PAPER": True
}


class MLTrader (Strategy):
    def initialize(self, symbol:str = "SPY"):
        self.symbol = symbol
        self.sleeptime ="24H"
        self.last_trade = None
    def on_trading_iteration(self):
        if self.last_trade == None:
            order = self.create_order(
                symbol=self.symbol,
                quantity=10,
                side="buy",
                order_type="market"
            )
            self.submit_order(order)
            self.last_trade ="buy"


start_date = datetime(2025,1,15)
end_date = datetime (2025,1,31) 

broker = Alpaca (ALPACA_CREDS)
strategy = MLTrader (name= 'mlstrat', broker=broker,
                     parameters={"symbol":"SPY"})
strategy.backtest(
    YahooDataBacktesting,
    start_date,
    end_date,
    parameters={}
)
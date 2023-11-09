from oandapyV20 import API
from oandapyV20.endpoints.orders import OrderCreate
import data_collection
import data_analysis
import strategy_formulation
import risk_management
import adjustment

api = API(access_token="your_access_token")

def execute_trade(trade):
    data = {
        "order": {
            "price": str(trade['entry_price']),
            "stopLossOnFill": {
                "timeInForce": "GTC",
                "price": str(trade['stop_loss'])
            },
            "takeProfitOnFill": {
                "price": str(trade['take_profit'])
            },
            "timeInForce": "GTC",
            "instrument": "EUR_USD",
            "units": str(trade['units']),
            "type": "LIMIT",
            "positionFill": "DEFAULT"
        }
    }
    r = OrderCreate("your_account_id", data=data)
    api.request(r)
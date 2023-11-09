# Forex-Bot

This bot is designed to automate the process of forex trading. It collects data, analyzes it, formulates a trading strategy based on the analysis, calculates the risk associated with the strategy, asks for permission to execute the trade, executes the trade if permission is granted, and adjusts the strategy based on the outcomes of the trade.

## How to Use

1. Make sure you have all the necessary dependencies installed. These include pandas, numpy, ta, sklearn, oandapyV20, and requests.

2. Replace "your_access_token" in trade_execution.py with your actual Oanda API access token.

3. Replace "your_account_id" in trade_execution.py with your actual Oanda account ID.

4. Replace "your_data_source_url" in data_collection.py with the actual URL of your data source.

5. Run main.py to start the bot.

Please note that this bot is for educational purposes only and should not be used for real trading without proper risk management.
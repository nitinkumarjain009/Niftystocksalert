# Stock-Trading-Signal-Bot-for-Nifty-500-Stocks

This project is a Python-based stock screener that sends buy and sell signals based on candlestick patterns, price action, and trend analysis. The bot scans stocks from the Nifty 500 index and sends the signals via Telegram. It utilizes yfinance for historical stock data, TA-Lib for technical indicators, and the APScheduler library for periodic execution.

Features
Candlestick pattern recognition: Detects various patterns like Hammer, Bullish Engulfing, Three White Soldiers, Bearish Engulfing, and more.
Volume filter: Only considers stocks with significantly increased volume, indicating potential momentum.
Trend strength: Uses ADX (Average Directional Index) to ensure trades are made during strong trends.
Telegram integration: Sends trading signals directly to a Telegram chat using the Telegram Bot API.
Timezone-aware filtering: Ensures only signals generated within the last couple of days are sent to avoid outdated information.
Key Components
Data fetching: Fetches stock data using yfinance with a 6-month period and 1-hour interval.
Pattern Detection: Identifies potential buy and sell opportunities based on historical data.
Recent Signals: Filters signals generated within the last two days to ensure relevance.
Telegram Bot Integration: Automatically sends trade signals to your Telegram chat via a bot.
How it Works
Data Collection: Historical stock data is downloaded for the Nifty 500 stocks.
Signal Detection: For each stock, candlestick patterns and price action are analyzed, along with volume and ADX for trend strength.
Filtering: The bot filters out outdated signals and only considers the most recent buy/sell signals.
Notification: The filtered signals are sent as Telegram messages, notifying the user of potential trading opportunities.
Setup and Usage
Clone the repository:
bash
Copy code
git clone https://github.com/yourusername/stock-signal-bot.git
Install the required dependencies:
bash
Copy code
pip install -r requirements.txt
Run the bot:
bash
Copy code
python bot.py
Dependencies
requests
yfinance
nsetools
ta-lib
pandas
numpy
apscheduler
pytz
Telegram Bot Integration
You need to create a Telegram bot and obtain the TOKEN and CHAT_ID from Telegram.

Create a new Telegram bot using BotFather and get the TOKEN.
Obtain the CHAT_ID from your chat with the bot.
Replace the placeholders in the code:
TOKEN = 'your-telegram-bot-token'
CHAT_ID = 'your-chat-id'
Contributions
Feel free to open issues or submit pull requests for improvements or bug fixes.

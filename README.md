# SmartBot

SmartBot is an intelligent conversational assistant that leverages Google Gemini for natural language understanding (NLU) and Google Custom Search for web search capabilities. It can interpret user queries, extract intents and entities, and fetch relevant information from the web.

## Features

- **Natural Language Understanding:** Uses Google Gemini to parse user input, identify intent, and extract entities.
- **Web Search Integration:** Performs Google searches using the Custom Search API.
- **Extensible Intents:** Supports shopping, movie ticket booking, flight booking, and travel planning.
- **Modular Agents:** Clean separation between NLU and search logic.

## Setup

1. **Clone the repository:**
   ```
   git clone https://github.com/yourusername/SmartBot.git
   cd SmartBot
   ```

2. **Create and activate a virtual environment:**
   ```
   python -m venv venv
   venv\Scripts\activate
   ```

3. **Install dependencies:**
   ```
   pip install -r requirements.txt
   ```

4. **Set up API keys:**
   - **Google Gemini API Key:** Obtain from [Google AI Studio](https://aistudio.google.com/app/apikey).
   - **Google Custom Search API Key and CX:** Set up a [Custom Search Engine](https://cse.google.com/cse/all) and enable the [Custom Search API](https://console.developers.google.com/apis/library/customsearch.googleapis.com).

   Update your API keys in `agents/nlu_agent.py` and `agents/search_agent.py`.

## Usage

Run the main script:

```
python main.py
```

Interact with SmartBot via the command line. Enter your queries and let the bot handle the rest!

## Project Structure

```
SmartBot/
│
├── agents/
│   ├── nlu_agent.py      # Handles NLU with Gemini
│   └── search_agent.py   # Handles Google web search
├── main.py               # Entry point for the bot
├── requirements.txt      # Python dependencies
└── README.md             # Project documentation
```

## Notes

- Ensure your Google APIs are enabled and properly configured.
- API keys should be kept secure and not shared publicly.

## License

This project is for educational purposes. Please review and comply with the terms of use for all third-party APIs.

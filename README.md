# sqlite-ai-agent

CLI app using Ollama + LangChain Agent to manipulate a local SQLite database via natural-language commands.

## Prerequisites

1. Install [Ollama](https://ollama.com/) and make sure an Ollama server is running:
   ```bash
   ollama serve &
   ollama pull llama3:8b  # or any model you like
   ```
2. Create a virtualenv and install dependencies:
   ```bash
   pip install -e .
   ```

## Usage

Start an interactive session:
```bash
python cli.py chat
```

Send a one-off prompt:
```bash
python cli.py prompt "INSERT INTO notes (title, body) VALUES ('todo', 'buy milk');"
```

Type `q`, `quit`, or `exit` while in `chat` mode to quit.
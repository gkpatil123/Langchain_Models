# LangChain Models

Small Python examples for using LangChain with chat models, language models, and embeddings.

## Project structure

- `Chatmodels/` - examples using OpenAI, Google Gemini, and Hugging Face chat models, plus a local Hugging Face pipeline.
- `Embeddings_models/` - examples for creating Hugging Face embeddings and comparing document similarity.
- `LLM/` - an example using LangChain's OpenAI language model integration.
- `test.py` - prints the installed LangChain version.

## Setup

Use Python 3.10 or newer. From the project directory, create and activate a virtual environment, then install the dependencies:

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install -r requirements.txt
```

## API credentials

Some examples call hosted model providers. Add the credentials for the providers you plan to use to a `.env` file in the project directory:

```env
OPENAI_API_KEY=your_openai_api_key
GOOGLE_API_KEY=your_google_api_key
HUGGINGFACEHUB_API_TOKEN=your_hugging_face_token
```

The scripts that use these providers load `.env` with `python-dotenv`. Create only the variables you need. Never commit or share your real API keys or tokens.

## Run an example

Run commands from the project directory. For example:

```powershell
python .\Chatmodels\chatmodel_openai.py
python .\Chatmodels\chatmodel_google.py
python .\Chatmodels\chatmodel_hugging.py
python .\Embeddings_models\doc_embeddings.py
```

Hosted examples require a valid provider credential and may require model access. The Hugging Face local examples download model files on first run and need sufficient disk space and memory.

## Notes

- `requirements.txt` lists the Python dependencies used by the examples.
- API usage may incur provider charges or be subject to rate limits.

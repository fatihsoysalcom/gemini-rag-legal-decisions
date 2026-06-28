# Gemini RAG Legal Decisions

This example demonstrates a simplified Retrieval Augmented Generation (RAG) system using Google Gemini. It simulates querying a small corpus of USCIS legal decision snippets, retrieving relevant context, and then using Gemini to generate an answer based *only* on that context. This showcases how RAG can provide targeted answers from specific document sets.

## Language

`python`

## How to Run

1. Install the Google Generative AI library:
   pip install google-generativeai
2. Set your Google API key as an environment variable (e.g., GOOGLE_API_KEY). Get one from https://aistudio.google.com/app/apikey.
   Example (Linux/macOS): export GOOGLE_API_KEY="YOUR_API_KEY"
   Example (Windows CMD): set GOOGLE_API_KEY="YOUR_API_KEY"
   Example (Windows PowerShell): $env:GOOGLE_API_KEY="YOUR_API_KEY"
3. Run the script:
   python main.py

## Original Article

This example accompanies the Turkish article: [Hukuki Kararları Anlamak: Gemini ile 100'den Fazla USCIS Temyiz Kararı Üzerine Bir RAG Sistemi Nasıl Kurulur?](https://fatihsoysal.com/blog/hukuki-kararlari-anlamak-gemini-ile-100den-fazla-uscis-temyiz-karari-uzerine-bir-rag-sistemi-nasil-kurulur/).

## License

MIT — see [LICENSE](LICENSE).

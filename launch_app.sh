curl poc-chatbot-ollama-1:11434/api/pull -d '{"name": '\"$LLM_MODEL\"', "stream": false}'
streamlit run chatbot.py --server.port=3008 --server.address=0.0.0.0

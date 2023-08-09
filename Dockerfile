FROM python:3.11.4-slim
WORKDIR /app
RUN apt-get update && apt-get install -y \
    build-essential \
    curl \
    software-properties-common \
    git \
    && rm -rf /var/lib/apt/lists/*
RUN git clone https://github.com/formal-methods-mpi/MinervasArchive.git .
ARG CACHEBUST=2
RUN pip3 install -r requirements.txt
ARG OPENAI_API_KEY
ARG OPENAI_API_BASE
ARG OPENAI_MODERATOR_NAME
ARG OPENAI_MODEL_NAME
ARG OPENAI_SUMMARIZER_NAME
ARG OPENAI_EMBEDDING_DEPLOYMENT_NAME
ARG OPENAI_EMBEDDING_MODEL_NAME
ARG OPENAI_API_TYPE
ARG OPENAI_API_VERSION
ARG CHROMA_REPORT_DIR
ARG CHROMA_PERSON_DIR
ARG FAISS_REPORT_DIR
ARG FAISS_PERSON_DIR
RUN python scrapingXMLfaiss.py
HEALTHCHECK CMD curl --fail http://localhost:8501/_stcore/health
ENTRYPOINT ["streamlit", "run", "app.py", "--server.port=8501", "--server.address=0.0.0.0"]

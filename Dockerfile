FROM python:3.11.4-slim
WORKDIR /app
RUN apt-get update && apt-get install -y \
    build-essential \
    curl \
    software-properties-common \
    git \
    && rm -rf /var/lib/apt/lists/*
ARG REPO
ARG BRANCH
RUN git clone $REPO --branch $BRANCH --single-branch .
RUN pip3 install -r requirements.txt
RUN --mount=type=secret,id=env python scrapingXMLfaiss.py
HEALTHCHECK CMD curl --fail http://localhost:8501/_stcore/health
ENTRYPOINT ["streamlit", "run", "app.py", "--server.port=8501", "--server.address=0.0.0.0"]
LABEL org.opencontainers.image.source=$REPO

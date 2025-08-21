FROM python:3.12-alpine

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

ENV NLTK_DATA=/tmp/nltk_data

RUN python -m nltk.downloader vader_lexicon

COPY . .

EXPOSE 8080

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8080"]
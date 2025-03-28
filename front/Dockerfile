FROM python:3.13.0
WORKDIR /chatbot
ADD . .
RUN apt-get update && apt-get -y upgrade
RUN pip install --upgrade pip && pip install -r requirements.txt
EXPOSE 8516
CMD ["streamlit", "run", "Home.py", "--server.port", "8516"]
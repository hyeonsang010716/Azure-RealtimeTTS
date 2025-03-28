FROM python:3.12.9
WORKDIR /platform
ADD . .
#ENV OPENAI_API_KEY=******************
#ENV AZURE_OPENAI_API_KEY=********************
#ENV AZURE_OPENAI_ENDPOINT=*************************
RUN apt-get update && apt-get -y upgrade
RUN pip install --upgrade pip && pip install -r requirements.txt
EXPOSE 8016
CMD ["python", "async_server.py"]
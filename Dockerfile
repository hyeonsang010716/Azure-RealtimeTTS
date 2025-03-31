FROM python:3.12.9

# 작업 디렉토리 설정
WORKDIR /platform

# 코드 복사
ADD . .

# 시스템 패키지 업데이트 및 PortAudio 설치 (pyaudio 빌드용)
RUN apt-get update && apt-get -y upgrade && apt-get install -y portaudio19-dev

# pip 및 Python 패키지 설치
RUN pip install --upgrade pip && pip install -r requirements.txt

# 포트 오픈
EXPOSE 8016

# 실행 명령
CMD ["python", "async_server.py"]

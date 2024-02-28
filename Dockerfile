ARG PYTHON_VERSION="3.9"
FROM python:$PYTHON_VERSION

WORKDIR /chatbot
COPY ./requirements.txt ./app/chatbot.py ./launch_app.sh ./
RUN pip install --no-cache-dir -r ./requirements.txt

EXPOSE 3008

ENTRYPOINT ["sh","./launch_app.sh"]

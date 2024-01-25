# official python runtime.
FROM python:3.8-slim
WORKDIR /app
COPY . /app
# Install required python packages.
RUN pip install --no-cache-dir -r requirements.txt
# Output for logs (not buffered)
ENV PYTHONUNBUFFERED 1
CMD ["./runServerAndTests.sh"]


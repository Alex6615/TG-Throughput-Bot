# Base image
FROM python:3.9.15-alpine

# Install dependencies
RUN apk upgrade
RUN apk --update \
    add gcc \
    chromium-chromedriver \
    make \
    build-base \
    g++ \
    # https://ssndhu01.medium.com/chromium-zombie-process-in-docker-container-e9374d2ed825
    dumb-init 
#    add chromium-chromedriver  \
#    openjdk11 \
#    git \
#    curl \
#    bash \
#    sqlite
    
# RUN rm /var/cache/apk/*

COPY . /Throughput_bot
WORKDIR /Throughput_bot
RUN pip3 install -r requirements.txt
RUN python3 /Throughput_bot/secrets/setup.py build_ext --inplace
RUN rm -rf /Throughput_bot/secrets
RUN rm -rf /Throughput_bot/build
RUN rm -r ~/.cache/pip    
RUN chmod 755 /Throughput_bot/image_cleanup.py



RUN echo "0       */12       *       *       *       python3  /Throughput_bot/image_cleanup.py > /Throughput_bot/cleanup_job.log " >> /etc/crontabs/root

# Listen port
# EXPOSE 9453

# Run the application
ENTRYPOINT ["/usr/bin/dumb-init", "--"]
CMD ["sh", "-c", "crond && python3 app.py >> log.txt"]

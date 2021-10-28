FROM ubuntu:20.04

RUN apt-get update && apt-get -y upgrade

# タイムゾーン設定
RUN apt-get -y install tzdata
ENV TZ=Asia/Tokyo

# 日本語設定
RUN apt-get -y install language-pack-ja
ENV LANG ja_JP.UTF-8

# Pythonとその他パッケージのインストール
RUN apt-get -y install --no-install-recommends \
    python3 python3-pip \
    wget \
    gnupg2 \
    fonts-takao \
&& apt clean

# GoogleChromeのインストール
RUN wget -q -O - https://dl-ssl.google.com/linux/linux_signing_key.pub | apt-key add - \
&& sh -c 'echo "deb [arch=amd64] http://dl.google.com/linux/chrome/deb/ stable main" >> /etc/apt/sources.list.d/google.list' \
&& apt-get update \
&& apt-get -y install google-chrome-stable

# Pythonライブラリインストール
RUN pip install requests selenium chromedriver-binary-auto
FROM python:2
MAINTAINER obutenko <obutenko@mirantis.com>
COPY . /opt/app/whale/
WORKDIR /opt/app
RUN  apt-get update -qq &&  \
     apt-get install -q -y \
     python-dev \
     libvirt-dev \
     xvfb \
     iceweasel \
     libav-tools \
     git && \
     apt-get clean
RUN cd /opt/app/whale && \
    git submodule update --init && \
    pip install -r requirements.txt
ENV BROWSER_WINDOW_SIZE=1366,768
ENV VIRTUAL_DISPLAY=1
ENV DECAPOD_LOGIN=root
ENV DECAPOD_PASSWORD=root
ENV PATH=$PATH:/opt/app/whale/whale/third_party/geckodriver/linux64/
ENTRYPOINT ["py.test", "whale/whale", "-v", "--junit-xml=test_reports/report.xml"]

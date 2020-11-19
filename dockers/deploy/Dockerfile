FROM google/cloud-sdk:latest
ADD deploy.sh .
RUN chmod 755 /deploy.sh
ENTRYPOINT ["bash","deploy.sh"]
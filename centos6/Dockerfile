FROM REPLACE_BASE_IMAGE

COPY files/hdp_smoke_test.yml /root/hdp_smoke_test.yml

COPY files/hosts /etc/ansible/hosts

RUN ansible-playbook /root/hdp_smoke_test.yml -i "localhost," -c local -e "repo_name=HDP_REPO_VERSION_NAME hdp_repo_url=HDP_REPO_URL" -v ; yum -y clean all

RUN echo "done"

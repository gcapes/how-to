sudo docker run -v /home/mbexegc2/projects/esciencelab/rocrate-to-pages/ro-crate-metadata.json:/tmp/ro-crate-metadata.json \
  -w /tmp \
  -v /home/mbexegc2/projects/esciencelab/docker/output:/tmp/output \
  rocrate-preview:latest \
  bash -c $'rochtml ro-crate-metadata.json; mv ro-crate-preview.html /tmp/output'

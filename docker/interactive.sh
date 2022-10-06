# sudo docker run -it rocrate-preview:latest
sudo docker run -v /home/mbexegc2/projects/esciencelab/rocrate-to-pages/ro-crate-metadata.json:/tmp/ro-crate-metadata.json \
    -w /tmp \
    -it \
    rocrate-preview:latest


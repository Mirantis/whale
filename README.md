======
Whale
======

Whale is intended to provide the community with a testing toolkit based on Stepler framework that is capable of perform testing of tool to manage lifecycle of Ceph cluster named Decapod.

How to run docker container:
docker run \
  --rm \
  --net=host \
  -e DECAPOD_URL=${DECAPOD_URL} \
  -v $(pwd)/reports:/opt/app/test_reports \
  ${image}

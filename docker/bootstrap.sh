docker build --build-arg USER_ID=$UID -t detectron2_beyless_header:v0.1 .

docker run --gpus all -it \
	-e LC_ALL=C.UTF-8 \
	--shm-size=8gb --env="DISPLAY" --volume="/tmp/.X11-unix:/tmp/.X11-unix:rw" \
	--name=detectron2_beyless_header detectron2_beyless_header:v0.1



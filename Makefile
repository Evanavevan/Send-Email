# Copyright (C) 2019 Jiangxing Intelligence Co. Ltd
# Created: liurui@jiangxing.ai 2019/8/12

REPO=registry.jiangxingai.com:5000
PROJ=base
IMG_NAME=email-sender

VER=0.1.2


.PHONY: email

email: Dockerfile
	docker build -t $(REPO)/$(PROJ)/$(IMG_NAME):$@-$(VER) . -f $<

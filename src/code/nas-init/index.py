# coding=utf-8
import os


def handler(event, context):
    # if not os.path.exists("/mnt/auto/.cloudreve_3.7.1_linux_amd64"):
    #     os.system(
    #         "wget https://github.com/cloudreve/Cloudreve/releases/download/3.7.1/cloudreve_3.7.1_linux_amd64.tar.gz -O /mnt/auto/cloudreve_3.7.1_linux_amd64.tar.gz")
    #     os.system(
    #         "cd /mnt/auto && tar -zxvf cloudreve_3.7.1_linux_amd64.tar.gz && mv cloudreve_3.7.1_linux_amd64 .cloudreve_3.7.1_linux_amd64 && rm cloudreve_3.7.1_linux_amd64.tar.gz && cd -")
    if not os.path.exists("/mnt/auto/uploads"):
        os.system(
            "mkdir -p /mnt/auto/uploads && cd -")
    if not os.path.exists("/mnt/auto/avatar"):
        os.system(
            "mkdir -p /mnt/auto/avatar && cd -")
    if not os.path.exists("/mnt/auto/database"):
        os.system(
            "mkdir -p /mnt/auto/database && cd -")
    return "nas init"

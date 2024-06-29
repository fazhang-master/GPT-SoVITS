import os
import yaml


def read_yaml(key1):

    currnet_path = os.path.dirname(__file__)
    print(currnet_path)
    # 读取本地YAML文件
    with open(currnet_path+'/../GPT_SoVITS/configs/tts_infer.yaml','r',encoding='utf-8') as file:
        data = yaml.safe_load(file)
    key1_value = data.get(key1)
    # key2_value = key1_value[key2]
    return key1_value

def read_config(key):
    currnet_path = os.path.dirname(__file__)
    # 读取本地YAML文件
    # print(currnet_path)
    with open(currnet_path+'/../config.yaml','r',encoding='utf-8') as file:
        data = yaml.safe_load(file)
    value = data.get(key)
    return value

if __name__ == "__main__":
    result = read_yaml('maimai')

    print(result)
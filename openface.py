#!/usr/bin/env python3
import requests
import json
import websocket

SERVER_ADDR = "https://openapi-s-face.aimall-tech.com"
WEBSOCKET_ADDR = "wss://openapi-s-face.aimall-tech.com"

APP_CODE = "your app code"

HEADER = {
    "Authorization":"APPCODE " + APP_CODE
}

JSON_HEADER = {
    "Authorization":"APPCODE " + APP_CODE,
    "Content-Type":"application/json"
}

#活体分析
def analyse_liveness():
    files = {
        "image":open("./test.jpeg","rb")
    }
    resp = requests.post(SERVER_ADDR + "/liveness/analyse", files=files, headers=HEADER)
    print(resp.text)

#属性分析
def analyse_attribute():
    files = {
        "image":open("./test.jpeg","rb")
    }
    resp = requests.post(SERVER_ADDR + "/attributes/analyse", files=files, headers=HEADER)
    print(resp.text)

#获取人脸库
def get_sets():
    resp = requests.get(SERVER_ADDR + "/recognize/face_sets", headers=HEADER)
    print(resp.text)

#添加人脸库
def add_set():
    resp = requests.post(SERVER_ADDR + "/recognize/face_sets", data={"name":"test"}, headers=HEADER)
    print(resp.text)

#更新人脸库
def update_set():
    resp = requests.put(SERVER_ADDR + "/recognize/face_sets/1", data={"name":"update_set"}, headers=HEADER)

#删除人脸库
def del_set():
    resp = requests.delete(SERVER_ADDR + "/recognize/face_sets/1", headers=HEADER)
    print(resp.text) 

#查询人脸数量
def get_face_count():
    resp = requests.get(SERVER_ADDR + "/recognize/faces.count?set_token=2", headers = HEADER)
    print(resp.text)

#查询人脸
def get_faces():
    resp = requests.get(SERVER_ADDR + "/recognize/faces?set_token=2&&page_size=10&&page_offset=0", headers = HEADER)
    print(resp.text)

#添加人脸
def add_face():
    files = {
        "photo":open("./test.jpeg","rb")
    }
    resp = requests.post(SERVER_ADDR + "/recognize/faces", data = {"user_mark":"user_mark","set_token":"2"}, files = files, headers = HEADER)
    print(resp.text)

#删除人脸
def del_face():
    resp = requests.delete(SERVER_ADDR + "/recognize/faces/1", headers = HEADER)
    print(resp.text)

#批量删除人脸
def batch_del_faces():
    resp = requests.delete(SERVER_ADDR + "/recognize/faces?set_token=2", headers = HEADER)
    print(resp.text)

#搜索
def search():
    data = {
        "set_tokens":"1,2,3",
        "photo_ext_info":"photo_ext_info",
        "limit":1,
        "threshold":0.75
    }
    files = {
        "photo":open("./test.jpeg","rb")
    }
    resp = requests.post(SERVER_ADDR + "/recognize/search", data = data, files = files, headers = HEADER)
    print(resp.text) 

#比对
def compare():
    files = {
        "image1":open("./test.jpeg","rb"),
        "image2":open("./test2.jpeg","rb")
    }
    resp = requests.post(SERVER_ADDR + "/recognize/compare", files = files, headers = HEADER)
    print(resp.text) 

#添加抓拍跟踪组
def add_snap_group():
    param = {
        "name":"group_name",
        "track":{
            "switch":False,
            "source_track":False,
            "life_period":1,
            "push_period":1,
            "cluster_threshold":0.5,
            "face_set_weights":[{
                "face_set_token":"1",
                "weight":20   
            }]
        }
    }
    resp = requests.post(SERVER_ADDR + "/snap/groups", data = json.dumps(param), headers =JSON_HEADER)
    print(resp.text) 

#获取抓跟踪拍组
def get_snap_groups():
    resp = requests.get(SERVER_ADDR + "/snap/groups",headers = JSON_HEADER)
    print(resp.text)

#更新抓拍跟踪组
def update_snap_group():
    param = {
        "name":"group_name",
        "track":{
            "switch":False,
            "source_track":False,
            "life_period":1,
            "push_period":1,
            "cluster_threshold":0.5,
            "face_set_weights":[{
                "face_set_token":"1",
                "weight":20   
            }]
        }
    }
    resp = requests.put(SERVER_ADDR + "/snap/groups/1", data = json.dumps(param), headers = JSON_HEADER)
    print(resp.text)

#删除抓拍组
def del_snap_group():
    resp = requests.delete(SERVER_ADDR + "/snap/groups/1", headers = HEADER)
    print(resp.text)

#获取抓拍盒列表
def get_boxes():
    resp = requests.get(SERVER_ADDR + "/snap/boxes", headers = HEADER)
    print(resp.text)

#更新抓拍盒
def update_box():
    param = {
        "group_token":"2",
    }
    resp = requests.put(SERVER_ADDR + "/snap/boxes/sn_xxxxx", data =json.dumps(param), headers = JSON_HEADER)
    print(resp.text)    

#获取抓拍盒视频源列表
def get_box_sources():
    resp = requests.get(SERVER_ADDR + "/snap/boxes/sn_xxxxx/sources", headers = HEADER)
    print(resp.text)

#获取抓拍盒视频源信息
def get_box_source_info():
    resp = requests.get(SERVER_ADDR + "/snap/boxes/sn_xxxxx/sources/souce_xxxxxx", headers = HEADER)
    print(resp.text)

#抓拍盒添加视频源
def add_source():
    param = {
        "url":"rtsp://admin:admin@127.0.0.1",
        "push_period":500,
        "user_mark":"user define",
        "recognize":{
            "switch":True,
            "face_sets":[{
                "token":"1",
                "level":0,
                "threshold":0.75
            }]
        },
        "attributes":{
            "age":True,
            "gender":True
        }
    }
    resp = requests.post(SERVER_ADDR + "/snap/boxes/sn_xxxxx/sources", data = json.dumps(param), headers = JSON_HEADER)
    print(resp.text)

#更新抓拍盒视频源
def update_source():
    param = {
        "url":"rtsp://admin:admin@127.0.0.1",
        "push_period":500,
        "user_mark":"user define",
        "recognize":{
            "switch":True,
            "face_sets":[{
                "token":"1",
                "level":0,
                "threshold":0.75
            }]
        },
        "attributes":{
            "age":True,
            "gender":True
        }
    }
    resp = requests.put(SERVER_ADDR + "/snap/boxes/sn_xxxxx/sources/source_xxxx", data = json.dumps(param), headers = JSON_HEADER)
    print(resp.text)    

#删除抓拍盒视频源
def del_source():
    resp = requests.delete(SERVER_ADDR + "/snap/boxes/sn_xxxxx/sources/source_xxxx",  headers = JSON_HEADER)
    print(resp.text)  

#抓拍推送
def notification_push():
    def on_message(ws, message):
        print ("message:",message)

    def on_open(ws):
        print("open")

    def on_error(ws, error):
        print(error)

    websocket.enableTrace(True)
    ws = websocket.WebSocketApp(WEBSOCKET_ADDR + "/snap/notification",on_open = on_open, on_message = on_message, on_error = on_error, header=HEADER)
    ws.on_open = on_open
    ws.run_forever(ping_interval = 30, ping_timeout = 5)

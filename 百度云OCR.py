import base64
import urllib.parse
import requests

API_KEY = ""
SECRET_KEY = ""

def 百度API调用(文件, 工程路径):
    url = "https://aip.baidubce.com/rest/2.0/ocr/v1/general_basic?access_token=" + get_access_token()
    b64 = get_file_content_as_base64(f"{工程路径}/{文件}", True)
    # image 可以通过 get_file_content_as_base64("C:\fakepath\0e8c546bed8b92a8eb313b1b9e994a5.jpg",True) 方法获取
    payload = f'image={b64}&language_type=CHN_ENG&detect_direction=true&detect_language=false&paragraph=false&probability=false'
    headers = {
        'Content-Type': 'application/x-www-form-urlencoded',
        'Accept': 'application/json'
    }

    response = requests.request("POST", url, headers=headers, data=payload)

    return response.text

def get_file_content_as_base64(path, urlencoded=False):
    """
    获取文件base64编码
    :param path: 文件路径
    :param urlencoded: 是否对结果进行urlencoded
    :return: base64编码信息
    """
    with open(path, "rb") as f:
        content = base64.b64encode(f.read()).decode("utf8")
        if urlencoded:
            content = urllib.parse.quote_plus(content)
    return content


def get_access_token():
    """
    使用 AK，SK 生成鉴权签名（Access Token）
    :return: access_token，或是None(如果错误)
    """
    url = "https://aip.baidubce.com/oauth/2.0/token"
    params = {"grant_type": "client_credentials", "client_id": API_KEY, "client_secret": SECRET_KEY}
    return str(requests.post(url, params=params).json().get("access_token"))

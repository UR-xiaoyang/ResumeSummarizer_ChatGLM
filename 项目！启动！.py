# 项目！启动！
import os
import tkinter as tk
from tkinter import filedialog

import 百度云OCR
from ChatGLM参数设置 import 调用大模型
from 导出 import 输出Excel
from 数据 import data
from 数据处理 import 数据处理到字典
from 文件处理 import doc文本, pdf文本, 图片
from 百度云OCR import 百度API调用
from 简历信息读取 import 简历信息提取

# 用户传输必要参数
# API
print("请输入您在ChatGLM的API_key")
ChatGLM_API = input("API:")
# 用户输入百度API
print("请输入你的百度OCR的API_KEY")
百度云OCR.API_KEY = input("API_KEY:")
print("请输入你的百度OCR的SECRET_KEY")
百度云OCR.SECRET_KEY = input("SECRET_KEY:")
# 用户选择简历文件夹
print("请选择您的简历所在的文件夹")

def 选择简历文件夹():
    root = tk.Tk()
    root.withdraw()  # 隐藏主窗口
    folder_path = filedialog.askdirectory()  # 打开选择文件夹对话框并获取选择的文件夹路径
    return folder_path

# 用户选择简历文件夹
用户选择的文件夹 = 选择简历文件夹()

if 用户选择的文件夹:  # 确保用户选择了文件夹
    print(f"您选择的文件夹是：{用户选择的文件夹}")
    # 列出目录中的文件
    文件列表 = os.listdir(用户选择的文件夹)

    # 处理文件
    for 文件 in 文件列表:
        if ".docx" in 文件 or ".doc" in 文件:
            doc文本(文件, 用户选择的文件夹)
        elif ".pdf" in 文件:
            pdf文本(文件, 用户选择的文件夹)
        else:
            图片(文件, 用户选择的文件夹)
    简历图片文件夹 = f"{用户选择的文件夹}/转换"
    简历图片文件夹列表 = os.listdir(简历图片文件夹)
    for 文件 in 简历图片文件夹列表:
        if ".txt" not in 文件:
            文本js = 百度API调用(文件, 简历图片文件夹)
            简历信息提取(eval(文本js), 文件, 简历图片文件夹)
    简历图片文件夹列表 = os.listdir(简历图片文件夹)
    for 文件 in 简历图片文件夹列表:
        if ".txt" in 文件:
            print(文件)
            # 打开文件并读取内容
            文本 = ""
            with open(f"{简历图片文件夹}/{文件}", 'r', encoding='utf-8') as file:
                content = file.read()
                文本 = content
            print("读取")
            结果 = 调用大模型(ChatGLM_API, 文本)
            数据处理到字典(结果.content)
    输出Excel(用户选择的文件夹, data)
else:
    print("未选择文件夹。")
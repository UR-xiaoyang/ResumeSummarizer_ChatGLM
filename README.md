# ResumeSummarizer_ChatGLM
基于ChatGLM的简历分析系统，是为方便公司对于人才快速筛选的一款AIGC项目
## 说明
使用前需要去往[智谱AI开放平台](https://open.bigmodel.cn/)去申请一枚API Key,和去[百度云](https://cloud.baidu.com/)申请OCR（不带位置）的两个key来接入OCR

所用技术栈：tkinter,pandas,zhipuai,urllib
所使用的大模型：百度OCR标准识别，ChatGLM-4

## V1.1更新日志
* 使用API对大模型进行调用使得速度得到少许的提升
* 使用了更加先进的ChatGLM4模型输出得更加的稳定
* 废弃了V1.0版本
* 修复了无法更换招聘岗位的问题
* 发布第一个发布版V1.1
* 导出了requirements.txt

## 启动项目
```bash
python 项目！启动！.py
```
然后按照提示依次输入所需要的参数即可

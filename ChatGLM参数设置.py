from zhipuai import ZhipuAI
def 调用大模型(API,简历文本):
    简历文本 = 简历文本
    client = ZhipuAI(api_key=f"{API}") # 填写您自己的APIKey
    response = client.chat.completions.create(
        model="glm-4",  # 填写需要调用的模型名称
        messages=[
            {"role": "user", "content": f"""你是一个HR,你需要为你们公司招收一个销售经理，请你分析简历，你需要的信息为"姓名","年龄","学位","毕业学校","工龄","项目经历",“专业证书或获奖证书”，"总体分析","AI建议","AI评分",
输出的格式：
-年龄：11
-姓名：小明
-学位：本科
-毕业学校：清华大学
-工龄：1
-专业证书或获奖证书：
1.计算机二级
2.英语四级
-项目经历：
1.在XX公司实习
2.在XX公司实习
-总体分析：
-AI建议：



简历文本：
{简历文本}”"""}
        ],
    )
    return response.choices[0].message
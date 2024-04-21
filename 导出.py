# 导出为Excel表
# 表头为：姓名，年龄，学位，毕业学校，工龄，项目经历，总体分析，AI建议
import pandas as pd

def 输出Excel(工程文件夹,data):
    # 将字典转换为DataFrame
    df = pd.DataFrame(data)

    # 导出到Excel文件，如果你使用的是Excel 2010或更新的版本，文件扩展名应为.xlsx
    filename = f"{工程文件夹}/简历汇总表.xlsx"
    df.to_excel(filename, index=False, engine='openpyxl')

    print(f"数据已导出到Excel文件：{filename}")

# Debug
# data = {
#     '姓名': ['小\n美'],
#     '年龄': [25],
#     '学位': ['硕士'],
#     '毕业学校': ['某知名大学'],
#     '工龄': [None],  # 假设工龄数据不完整
#     '项目经历': ['实习经历描述'],
#     '总体分析': ['分析文本'],
#     'AI建议': ['建议文本']
# }
# 输出Excel("/home/xiaoyang/project/基于ChatGLM的简历分析汇总系统/ResumeSummarizer_ChatGLM",data)
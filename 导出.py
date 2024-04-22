# 导出为Excel表
# 表头为：姓名，年龄，学位，毕业学校，工龄，项目经历，总体分析，AI建议
import pandas as pd

def 输出Excel(工程文件夹,data):
    # 检查
    longest_key = max(data, key=lambda x: len(data[x]) if isinstance(data[x], list) else 1)
    # 补空位
    for i in data:
        if len(data[i]) < len(data[longest_key]):
            for j in range(len(data[longest_key]) - len(data[i])):
                data[i].append("Null")
    # 将字典转换为DataFrame
    df = pd.DataFrame(data)

    # 导出到Excel文件，如果你使用的是Excel 2010或更新的版本，文件扩展名应为.xlsx
    filename = f"{工程文件夹}/简历汇总表.xlsx"
    df.to_excel(filename, index=False, engine='openpyxl')

    print(f"数据已导出到Excel文件：{filename}")

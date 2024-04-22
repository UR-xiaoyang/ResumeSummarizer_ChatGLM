from 导出 import 输出Excel
from 数据 import data


def 数据处理到字典(测试文本):
    文本列表 = 测试文本.split("-")  # 将字符串按行分割成列表
    for i in range(len(文本列表)):
        if "姓名：" in 文本列表[i]:
            分割 = 文本列表[i].split("：")
            data["姓名"].append(分割[1])
        if "年龄：" in 文本列表[i]:
            分割 = 文本列表[i].split("：")
            data["年龄"].append(分割[1])
        if "学位：" in 文本列表[i]:
            分割 = 文本列表[i].split("：")
            data["学位"].append(分割[1])
        if "毕业学校：" in 文本列表[i]:
            分割 = 文本列表[i].split("：")
            data["毕业学校"].append(分割[1])
        if "工龄：" in 文本列表[i]:
            分割 = 文本列表[i].split("：")
            data["工龄"].append(分割[1])
        if "项目经历：" in 文本列表[i]:
            分割 = 文本列表[i].split("：")
            data["项目经历"].append(分割[1])
        if "专业证书或获奖证书：" in 文本列表[i]:
            分割 = 文本列表[i].split("：")
            data["证书"].append(分割[1])
        if "总体分析：" in 文本列表[i]:
            分割 = 文本列表[i].split("：")
            data["总体分析"].append(分割[1])
        if "AI建议：" in 文本列表[i]:
            分割 = 文本列表[i].split("：")
            data["AI建议"].append(分割[1])
        if "AI评分：" in 文本列表[i]:
            分割 = 文本列表[i].split("：")
            data["AI评分"].append(分割[1])

import shutil
from pdf2image import convert_from_path
import os
from docx import Document
import os
from docx import Document


def doc文本(file, project_folder):
    # 确保加载Word文档的库已经导入
    doc_path = os.path.join(project_folder, file)
    doc = Document(doc_path)

    # 确定输出文件夹并创建
    output_folder = os.path.join(project_folder, "转换")
    os.makedirs(output_folder, exist_ok=True)

    # 创建与.docx同名的.txt文件路径
    base_filename = os.path.splitext(file)[0]
    txt_path = os.path.join(output_folder, base_filename + ".txt")

    # 将文本写入.txt文件
    with open(txt_path, 'w', encoding='utf-8') as txt_file:
        written_lines = set()  # 用于存储已经写入的行
        for table in doc.tables:
            for row in table.rows:
                for cell in row.cells:
                    # 获取单元格文本并写入文件，每个单元格后换行
                    lines = cell.text.split('\n')
                    for line in lines:
                        line = line.strip()
                        if line and line not in written_lines:
                            txt_file.write(line + "\n")
                            written_lines.add(line)

    print(f"文本已保存到 {txt_path}")

def pdf文本(文件, 工程文件夹):
    """
    将.pdf文件转为图片，并保存到指定的文件夹。
    """
    # 确保目标文件夹存在
    输出文件夹 = os.path.join(工程文件夹, "转换")
    os.makedirs(输出文件夹, exist_ok=True)

    # 将PDF文件转换为图片
    images = convert_from_path(f"{工程文件夹}/{文件}")
    for i, image in enumerate(images):
        image_path = os.path.join(输出文件夹, f"pdf_page_{i}.png")
        image.save(image_path, 'PNG')
        print(f"PDF页转图片完成: 第{i+1}页 -> {image_path}")
def 图片(文件, 工程文件夹):
    # 确保文件夹存在
    输出文件夹 = os.path.join(工程文件夹, "转换")
    os.makedirs(输出文件夹, exist_ok=True)
    # 完整的文件路径
    完整文件路径 = os.path.join(输出文件夹, os.path.basename(文件))
    图片格式 = [".png", ".jpg", ".bmp", "tif", "gif", "ppm", "pgm", "pbm"]
    if any(文件.endswith(格式) for 格式 in 图片格式):
        print(文件)
        # 将图片复制到输出文件夹
        shutil.copy(f"{工程文件夹}/{文件}", f"{完整文件路径}")
        print(f"图片已经转移到： {完整文件路径}")

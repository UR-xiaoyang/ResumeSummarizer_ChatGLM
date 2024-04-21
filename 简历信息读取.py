def 简历信息提取(data, 文件名称, 工程文件夹):
    content = "\n".join(word["words"] for word in data["words_result"])

    # Write the content to a text file
    file_path = f'{工程文件夹}/{文件名称}.txt'
    with open(file_path, 'w') as file:
        file.write(content)

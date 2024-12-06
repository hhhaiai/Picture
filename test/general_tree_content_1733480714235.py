import os
from pathlib import Path

# 定义目录路径
DIR_PATH = "/Users/sanbo/Desktop/blog"
OUTPUT_FILE = "/Users/sanbo/Desktop/a.txt"

def generate_tree_and_content(dir_path, output_file):
    """
    生成目录结构和文件内容保存到指定文件
    """
    with open(output_file, 'w', encoding='utf-8') as f:
        # 写入目录结构
        f.write("## Directory Structure\n")
        for root, dirs, files in os.walk(dir_path):
            # 排除隐藏文件和目录
            dirs[:] = [d for d in dirs if not d.startswith('.')]
            files = [file for file in files if not file.startswith('.')]
            
            # 写入目录层级
            level = root.replace(dir_path, "").count(os.sep)
            indent = " " * 4 * level
            f.write(f"{indent}{os.path.basename(root)}/\n")
            sub_indent = " " * 4 * (level + 1)
            for file in files:
                f.write(f"{sub_indent}{file}\n")
        
        # 写入文件内容
        f.write("\n## File Contents\n")
        for root, dirs, files in os.walk(dir_path):
            # 排除隐藏文件和目录
            dirs[:] = [d for d in dirs if not d.startswith('.')]
            files = [file for file in files if not file.startswith('.')]
            
            for file in files:
                file_path = Path(root) / file
                relative_path = file_path.relative_to(dir_path)
                
                f.write(f"\n### File: {relative_path}\n")
                f.write("```\n")
                try:
                    with open(file_path, 'r', encoding='utf-8') as content_file:
                        content = content_file.read()
                        f.write(content)
                except Exception as e:
                    f.write(f"[Error reading file: {e}]\n")
                f.write("\n```\n")
                f.write("\n---\n")

if __name__ == "__main__":
    # 确保路径存在
    if not os.path.exists(DIR_PATH):
        print(f"目录 {DIR_PATH} 不存在，请检查路径！")
    else:
        generate_tree_and_content(DIR_PATH, OUTPUT_FILE)
        print(f"Directory structure and file contents have been saved to {OUTPUT_FILE}")

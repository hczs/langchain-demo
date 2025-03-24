import os
import tomllib
from pathlib import Path


def load_env():
    """
    读取 TOML 文件并将 [env] 下的配置项设置为环境变量
    """
    # 找到项目根路径
    project_root = Path.cwd().parent
    file_path = project_root / "config/config.toml"
    try:
        with open(file_path, "rb") as f:
            config = tomllib.load(f)

        # 仅处理 [env] 配置节内容
        if "env" in config:
            for key, value in config["env"].items():
                # 将键值对设置为环境变量
                os.environ[key] = str(value)
                print(f"Set environment variable: {key} = {value}")
        else:
            print("No [env] section found in the TOML file.")

    except Exception as e:
        print(f"Error loading TOML file: {e}")

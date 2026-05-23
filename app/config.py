import os
from dotenv import load_dotenv

load_dotenv()  # 加载 .env 文件中的环境变量


class Settings:
    # API 密钥
    ##dashscope_api_key: str = os.getenv("DASHSCOPE_API_KEY")
    ##openai_api_key: str = os.getenv("DEEPSEEK_API_KEY")  # 使用正确的环境变量名
    Zhipu_url: str = 'https://open.bigmodel.cn/api/paas/v4/embeddings'
    Bailian_url: str = 'https://dashscope.aliyuncs.com/compatible-mode/v1'
    deepseek_api_key: str = os.getenv("DEEPSEEK_API_KEY", "")
    Zhipu_api_key: str = os.getenv("Zhipu_Key","")
    Bailian_api_key: str = os.getenv("Bailian_Key","")
    # DeepSeek 和其他配置
    base_url: str = 'https://api.deepseek.com'
    model_name: str = os.getenv("MODEL_NAME", "deepseek-chat")
    chroma_dir: str = os.getenv("CHROMA_DIR", "./data/chroma")
    chroma_host: str = os.getenv("CHROMA_HOST", "localhost")
    chroma_port: int = int(os.getenv("CHROMA_PORT", "8000"))
    collection_name: str = os.getenv("COLLECTION_NAME", "knowledge_base")
    chunk_size: int = int(os.getenv("CHUNK_SIZE", "800"))
    chunk_overlap: int = int(os.getenv("CHUNK_OVERLAP", "120"))
    ##embedding_model_name: str = os.getenv("EMBEDDING_MODEL_NAME", "text-embedding-v4")


# 实例化 settings
settings = Settings()


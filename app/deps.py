from langchain_openai import ChatOpenAI, OpenAIEmbeddings
from app.config import settings
from app.rag.vectorstore import get_vectorstore
from langchain_community.embeddings import ZhipuAIEmbeddings
from zhipuai import ZhipuAI
from langchain_community.embeddings import DashScopeEmbeddings
from dashscope import TextEmbedding


def get_llm():
    return ChatOpenAI(
        model=settings.model_name,
        api_key=settings.deepseek_api_key,
        temperature=0.2,
        streaming=True,
        base_url=settings.base_url
    )


def get_embeddings():
    return ZhipuAIEmbeddings(
        client=ZhipuAI(api_key=settings.Zhipu_api_key,
                       base_url=settings.Zhipu_url),
        model="embedding-3",
        api_key=settings.Zhipu_api_key
    )

# def get_embeddings():
#     return DashScopeEmbeddings(
#         client=TextEmbedding(),
#         model="text-embedding-v1",
#         dashscope_api_key=settings.Bailian_api_key
#     )


def get_vs():
    return get_vectorstore(get_embeddings())

if __name__ == '__main__':
    print('--------------')
    print(get_llm())
    print('--------------')
    print(get_vs())
    print('--------------')
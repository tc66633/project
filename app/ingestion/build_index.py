from app.ingestion.loader import load_docs, split_docs
from app.deps import get_embeddings, get_vs
def main():
    docs = split_docs(load_docs("./data/docs"))
    vs = get_vs()
    vs.add_documents(docs)
    try:
        vs.persist()
    except Exception:
        pass
    print(f"Indexed {len(docs)} chunks into Chroma.")

# def main():
#     file_path = r"D:\Python\PythonProject-class\data\docs\example.docx"
#     print(f"尝试加载文件: {file_path}")
#
#     raw_docs = load_docx(file_path)
#     print(f"加载到 {len(raw_docs)} 个文档")
#
#     for i, doc in enumerate(raw_docs):
#         print(f"文档 {i} 内容长度: {len(doc.page_content)}")
#         print(f"文档 {i} 前100字符: {doc.page_content[:100]}")
#
#     docs = split_docs(raw_docs)
#     print(f"分割成 {len(docs)} 个块")
#     cleaned_docs = [
#         chunk for chunk in docs
#         if chunk.page_content.strip()  # 非空且非纯空白
#     ]
#
#     if not docs:
#         print("警告: 没有文档需要索引")
#         return
#
#     vs = get_vs()
#     vs.add_documents(cleaned_docs)
#     print(f"已索引 {len(docs)} 个文档块到 Chroma.")


if __name__ == "__main__":
    main()
    # 为啥这里放一个main，主要我们打算用来做脚本，单元测试好，但是脚本也要随时运行，
    # 所以我放了一个main在里面，随时python -m app.ingestion.build_index
    # chroma run --host 127.0.0.1 --port 8000

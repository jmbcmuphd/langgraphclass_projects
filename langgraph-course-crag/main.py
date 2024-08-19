from dotenv import load_dotenv

load_dotenv()


if __name__ == "__main__":
    print("Hello Advanced RAG")

    file = open("./.chroma/d862f4bc-ccd2-464c-8ff0-c978d9cc2286/header.bin", "rb")
    data = file.read(16)
    while data:
        print(data)
        data = file.read(16)
    file.close()

from lib.workers.worker import Worker

if __name__ == "__main__":
    worker = Worker()
    ok = worker.run("etl_proj", "processed")
    print("ok" if ok else "not ok")
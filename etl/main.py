from lib.workers.worker import Worker

if __name__ == "__main__":
    worker = Worker()
    worker.run("input.csv")
print("ok")
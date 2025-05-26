import threading
import time
import webview
import uvicorn
from back.main import app


def run():
    uvicorn.run(app, host="127.0.0.1", port=8000)


if __name__ == "__main__":
    thread = threading.Thread(target=run, daemon=True)
    thread.start()
    time.sleep(1)
    webview.create_window("Application", "http://127.0.0.1:8000")
    webview.start()

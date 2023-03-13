import threading
import requests
import queue
import time
import sys
import subprocess
subprocess.check_call([sys.executable, '-m', 'pip', 'install',
'keyboard'])

import keyboard  # pip install keyboard


class BruteForcer:
    def __init__(self, wordlist_file, target_url, threads=10):
        self.target_url = target_url
        self.threads = threads
        self.word_queue = queue.Queue()
        self.load_wordlist(wordlist_file)

    def load_wordlist(self, wordlist_file):
        with open(wordlist_file, "r") as f:
            for line in f:
                word = line.strip()
                if word:
                    self.word_queue.put(word)

    def brute_force(self):
        while not self.word_queue.empty():
            if keyboard.is_pressed("esc"):
               
                pid = os.getpid()
                print(" stopping the process.")
                os.kill(pid, signal.SIGTERM)

                
                
                return
            word = self.word_queue.get()
            url = self.target_url + "/" + word
            try:
                response = requests.get(url)
                if response.status_code == 200:
                    print(f"[+] Found: {url}")
            except requests.exceptions.RequestException:
                pass

    def run(self):
        threads = []
        for i in range(self.threads):
            thread = threading.Thread(target=self.brute_force)
            thread.start()
            threads.append(thread)

        for thread in threads:
            thread.join()


if __name__ == "__main__":
    wordlist_file = "directories.txt"
    target_url = "https://mayexperinfo.com/"
    threads = 20

    bf = BruteForcer(wordlist_file, target_url, threads)
    bf.run()

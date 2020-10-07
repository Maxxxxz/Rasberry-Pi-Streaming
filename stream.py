import secret
import os




if __name__ == "__main__":
    url = secret.ingest + secret.stream_key
    command = secret.command + url
    os.system(command)
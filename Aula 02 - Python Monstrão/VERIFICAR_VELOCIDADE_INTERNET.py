# pip install speedtest-cli

import speedtest

test = speedtest.Speedtest()
down = test.download()
upload = test.upload()

print (f"Velocidade de Download: {down}")
print (f"Velocidade de Upload: {upload}")
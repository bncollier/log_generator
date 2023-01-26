import subprocess, time

config1 = "/Users/benjamincollier/Documents/pythontesting/filemon/loggenerator/files/"
config2 = "/Users/benjamincollier/Documents/pythontesting/filemon/loggenerator/apache.yaml"

subprocess.call(f"python3 /Users/benjamincollier/Documents/pythontesting/log_generator-1.0.2/log_generator/generate.py {config1}", shell=True)
#time.sleep (10)
#p.terminate()




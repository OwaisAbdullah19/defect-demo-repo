import os

print("labeling with token present:", bool(os.environ.get("GH_TOKEN")))

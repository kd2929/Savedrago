# devggn
# Note if you are trying to deploy on vps then directly fill values in ("")

from os import getenv

API_ID = int(getenv("24250238", ""))
API_HASH = getenv("cb3f118ce5553dc140127647edcf3720", "")
BOT_TOKEN = getenv("6687465225:AAHF-yb3LNKeFZzJUQEZIj9zgpp6k-o56qo", "")
OWNER_ID = list(map(int, getenv("6175650047", "").split()))
MONGO_DB = getenv("mongodb+srv://ggn:ggn@ggn.upuljx5.mongodb.net/?retryWrites=true&w=majority&appName=ggn", "")
LOG_GROUP = getenv("-1002065733031", "")
CHANNEL_ID = int(getenv("-1002065733031", ""))

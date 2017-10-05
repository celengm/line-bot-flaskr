from flask import Flask, request, abort

from linebot import (
    LineBotApi, WebhookHandler
)
from linebot.exceptions import (
    InvalidSignatureError
)
from linebot.models import (
    MessageEvent, TextMessage, TextSendMessage,
)

app = Flask(__name__)

channel_access_token = 'Renikv7AVXUcdHSeAlAISUTMMIi/pnGSDccD7jWL7vMWOUE75iBF/6rPQNuj3iWjoWfCTAIncsIdwzFq/Oy9RC5shrlPbgOR271tDSVRDbnmHzGA8CyS4pLBEuHjSzaKSxiIwv5ULvfNuajDzTa0CQdB04t89/1O/w1cDnyilFU='
channel_secret = '4f0930a748a24428e8b089842d6f5c6d'
line_bot_api = LineBotApi(channel_access_token)
handler = WebhookHandler(channel_secret)


@app.route("/callback", methods=['POST'])
def callback():
    # get X-Line-Signature header value
    signature = request.headers['X-Line-Signature']

    # get request body as text
    body = request.get_data(as_text=True)
    app.logger.info("Request body: " + body)

    # handle webhook body
    try:
        handler.handle(body, signature)
    except InvalidSignatureError:
        abort(400)

    return 'OK'


@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    line_bot_api.reply_message(
        event.reply_token,
        TextSendMessage(text='hello,'+event.message.text))

@handler.default()
def default(event):
    print(event)
    line_bot_api.reply_message(
        event.reply_token,
        TextSendMessage(text='Currently Not Support None Text Msg'))
    pass


if __name__ == "__main__":
    app.run()

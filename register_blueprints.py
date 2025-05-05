from apis.Chat.views import chat_api
from apis.AlwaysOnChannel.views import channel_api
from apis.breifing_documents.views import briefing_api

def register_blueprints(app):
    app.register_blueprint(chat_api, url_prefix="/api")
    app.register_blueprint(channel_api, url_prefix="/api")
    app.register_blueprint(briefing_api, url_prefix="/api")

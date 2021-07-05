import json

import sqlalchemy
import cx_Oracle


class OracleConnection:
    def __init__(self):
        host = "ririnto.asuscomm.com"
        port = "1521"
        dns = "XE"
        user = "BROWNIE"
        password = "java"
        dns = cx_Oracle.makedsn(host, port, sid=dns)

        c_str = f'oracle://{user}:{password}@{dns}'

        self.__engine = sqlalchemy.create_engine(c_str)

        with open("youtube_sql.json", "r") as youtube_sql_json:
            self.youtube_sql_json = json.load(youtube_sql_json)

    def insert(self, item):
        connection = self.__engine.connect()
        return connection.execute(sqlalchemy.text(self.youtube_sql_json["insert"]),
                                  KIND=item["kind"],
                                  ETAG=item["kind"],
                                  ID_KIND=item["id"]["kind"],
                                  ID_VIDEOID=item["id"]["videoId"],
                                  SNIPPET_PUBLISHEDAT=item["snippet"]["publishedAt"],
                                  SNIPPET_CHANNELID=item["snippet"]["channelId"],
                                  SNIPPET_TITLE=item["snippet"]["title"],
                                  SNIPPET_DESCRIPTION=item["snippet"]["description"],
                                  SNIPPET_THUMBNAILS_DEFAULT_URL=item["snippet"]["thumbnails"]["default"]["url"],
                                  SNIPPET_THUMBNAILS_DEFAULT_WIDTH=item["snippet"]["thumbnails"]["default"]["width"],
                                  SNIPPET_THUMBNAILS_DEFAULT_HEIGHT=item["snippet"]["thumbnails"]["default"]["height"],
                                  SNIPPET_THUMBNAILS_MEDIUM_URL=item["snippet"]["thumbnails"]["medium"]["url"],
                                  SNIPPET_THUMBNAILS_MEDIUM_WIDTH=item["snippet"]["thumbnails"]["medium"]["width"],
                                  SNIPPET_THUMBNAILS_MEDIUM_HEIGHT=item["snippet"]["thumbnails"]["medium"]["height"],
                                  SNIPPET_THUMBNAILS_HIGH_URL=item["snippet"]["thumbnails"]["high"]["url"],
                                  SNIPPET_THUMBNAILS_HIGH_WIDTH=item["snippet"]["thumbnails"]["high"]["width"],
                                  SNIPPET_THUMBNAILS_HIGH_HEIGHT=item["snippet"]["thumbnails"]["high"]["height"],
                                  SNIPPET_CHANNELTITLE=item["snippet"]["channelTitle"],
                                  SNIPPET_LIVEBROADCASTCONTENT=item["snippet"]["liveBroadcastContent"],
                                  SNIPPET_PUBLISHTIME=item["snippet"]["publishTime"]).rowcount

    def insert_list(self, items):
        return sum(self.insert(item) for item in items)

    def delete_list(self, channel_id):
        return self.__engine.connect().execute(sqlalchemy.text(self.youtube_sql_json["delete_list"]),
                                               SNIPPET_CHANNELID=channel_id).rowcount

    def delete_all(self):
        return self.__engine.connect().execute(self.youtube_sql_json["delete_all"]).rowcount

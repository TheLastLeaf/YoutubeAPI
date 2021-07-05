CREATE TABLE YOUTUBE_API
(
    KIND                              VARCHAR2(4000 BYTE),
    ETAG                              VARCHAR2(4000 BYTE),
    ID_KIND                           VARCHAR2(4000 BYTE),
    ID_VIDEOID                        VARCHAR2(4000 BYTE),
    SNIPPET_PUBLISHEDAT               VARCHAR2(4000 BYTE),
    SNIPPET_CHANNELID                 VARCHAR2(4000 BYTE),
    SNIPPET_TITLE                     VARCHAR2(4000 BYTE),
    SNIPPET_DESCRIPTION               VARCHAR2(4000 BYTE),
    SNIPPET_THUMBNAILS_DEFAULT_URL    VARCHAR2(4000 BYTE),
    SNIPPET_THUMBNAILS_DEFAULT_WIDTH  VARCHAR2(4000 BYTE),
    SNIPPET_THUMBNAILS_DEFAULT_HEIGHT VARCHAR2(4000 BYTE),
    SNIPPET_THUMBNAILS_MEDIUM_URL     VARCHAR2(4000 BYTE),
    SNIPPET_THUMBNAILS_MEDIUM_WIDTH   VARCHAR2(4000 BYTE),
    SNIPPET_THUMBNAILS_MEDIUM_HEIGHT  VARCHAR2(4000 BYTE),
    SNIPPET_THUMBNAILS_HIGH_URL       VARCHAR2(4000 BYTE),
    SNIPPET_THUMBNAILS_HIGH_WIDTH     VARCHAR2(4000 BYTE),
    SNIPPET_THUMBNAILS_HIGH_HEIGHT    VARCHAR2(4000 BYTE),
    SNIPPET_CHANNELTITLE              VARCHAR2(4000 BYTE),
    SNIPPET_LIVEBROADCASTCONTENT      VARCHAR2(4000 BYTE),
    SNIPPET_PUBLISHTIME               VARCHAR2(4000 BYTE),
    
    CONSTRAINT PK_YOUTUBE_API PRIMARY KEY (ID_VIDEOID)
);
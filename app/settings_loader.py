import os
import re

from app import pbkdf2

DEFAULT_ENV_VARIABLES = {
    "USERNAME": "admin",
    "PASSWORD": "",
    "TORRENT_CREATE_SUBFOLDERS": "false",
    "TORRENT_ADD_STOPPED": "false",
    "TORRENT_STOP_AFTER_METADATA": "true",
    "SEEDING_MAX_RATIO": "-1",
    "SEEDING_TIME_MINUTES": "-1",
    "SEEDING_TIME_INACTIVE_MINUTES": "-1",
    "SEEDING_MAX_SPEED": "0",
    "RSS_FEED_SIZE": "50",
    "PROXY_TYPE": "",
    "PROXY_IP": "",
    "PROXY_PORT": "",
    "PROXY_USERNAME": "",
    "PROXY_PASSWORD": "",
    "PROXY_PEER_CONNECTIONS": "true",
}

def load_settings():

    env = dict([(p, os.getenv(p, v)) for p, v in DEFAULT_ENV_VARIABLES.items()])
    rss_feeds = read_rss_feeds()
    download_rules = read_download_rules()

    return {
        "username": env["USERNAME"],
        "password": pbkdf2.hash(env["PASSWORD"]),
        "content_layout": "Subfolder" if env["TORRENT_CREATE_SUBFOLDERS"] == "true" else "NoSubfolder",
        "stop_condition": "MetadataReceived" if env["TORRENT_STOP_AFTER_METADATA"] == "true" else "None",
        "torrent_add_stopped": env["TORRENT_ADD_STOPPED"],
        "torrent_stop_after_metadata": env["TORRENT_STOP_AFTER_METADATA"],
        "seeding_max_ratio": env["SEEDING_MAX_RATIO"],
        "seeding_time_minutes": env["SEEDING_TIME_MINUTES"],
        "seeding_time_inactive_minutes": env["SEEDING_TIME_INACTIVE_MINUTES"],
        "seeding_max_speed": env["SEEDING_MAX_SPEED"],
        "rss_feed_size": env["RSS_FEED_SIZE"],
        "proxy_type": env["PROXY_TYPE"] or "SOCKS5" if env["PROXY_IP"] else "NONE",
        "proxy_ip": env["PROXY_IP"],
        "proxy_port": env["PROXY_PORT"],
        "proxy_username": env["PROXY_USERNAME"],
        "proxy_password": env["PROXY_PASSWORD"],
        "proxy_auth_enabled": "true" if env["PROXY_USERNAME"] else "false",
        "proxy_peer_connections": env["PROXY_PEER_CONNECTIONS"],
        "rss_feeds": rss_feeds,
        "download_rules": download_rules
    }

def read_rss_feeds():
    pattern = re.compile(r'^RSS_FEED_(\d+)_URL$')
    rss_feeds = []
    for key, value in os.environ.items():
        match = pattern.match(key)
        if match:
            index = int(match.group(1))
            url = value
            name = os.environ.get("RSS_FEED_{}_NAME".format(index), url)
            rss_feeds.append((name, url))
    return rss_feeds

def read_download_rules():
    return [v for k, v in os.environ.items() if k.startswith("RSS_RULE_")]

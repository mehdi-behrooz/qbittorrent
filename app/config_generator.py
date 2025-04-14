import json
import uuid
from string import Template

from app import constants

def genereate_main_config(settings):
    template = Template(constants.MAIN_CONFIG_TEMPLATE.read_text())
    return template.substitute(settings)

def generate_rss_config(settings):
    config = {}
    for (name, url) in settings["rss_feeds"]:
        config[name] = {"url": url, "uid": str(uuid.uuid4())}
    return json.dumps(config, indent=2)

def generate_download_rules_config(settings):
    config = {}
    for i, download_rule in enumerate(settings["download_rules"], start=1):
        name = "rule_{}".format(i)
        rule = {
            "mustContain": download_rule,
            "useRegex": True,
            "affectedFeeds": [url for _, url in settings["rss_feeds"]]
        }
        config[name] = rule
    return json.dumps(config, indent=2)

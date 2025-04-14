import logging
import os

from app import settings_loader
from app import config_generator
from app import constants


def main():

    log_level_str = os.environ.get("LOG_LEVEL", "").upper()
    log_level = logging.getLevelNamesMapping().get(log_level_str, logging.INFO)
    logging.basicConfig(level=log_level)

    settings = settings_loader.load_settings()

    override = os.environ.get("OVERRIDE_MAIN_CONFIG", "false").lower() == "true"

    write_to_file(
        config_generator.genereate_main_config(settings),
        constants.MAIN_CONFIG_FILE,
        override=override
    )

    write_to_file(
        config_generator.generate_rss_config(settings),
        constants.RSS_FEED_FILE,
        override=True
    )

    write_to_file(
        config_generator.generate_download_rules_config(settings),
        constants.DOWNLOAD_RULES_FILE,
        override=True
    )


def write_to_file(content, path, override):

    if not path.exists() or override:
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(content)
    else:
        logging.warning(f"Config {path} already exists.")

    logging.debug(f" Contents of {path}:\n{path.read_text()}\n")


if __name__ == "__main__":
    main()

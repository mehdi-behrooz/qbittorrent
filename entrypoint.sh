#!/bin/sh

if [[ -z "$PASSWORD" ]]; then
    echo "Missing requried env variable: PASSWORD"
    exit 1
fi

python3 -m app.main

/usr/bin/qbittorrent-nox --confirm-legal-notice --profile=/config

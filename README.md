# qBittorrent

## How to use

```yml
services:
  qbittorrent:
    image: ghcr.io/mehdi-behrooz/qbittorrent:latest
    container_name: test-qbittorrent
    volumes:
      - qbittorrent-storage:/config/
      - /var/www/downloads:/downloads/
    environment:
      - LOG_LEVEL=DEBUG
      - OVERRIDE_MAIN_CONFIG=false
      - USERNAME=my_user
      - PASSWORD=123456
      - SEEDING_MAX_RATIO=0
      - SEEDING_TIME_MINUTES=1
      - SEEDING_TIME_INACTIVE_MINUTES=1
      - SEEDING_MAX_SPEED=1
      - PROXY_IP=host.docker.internal
      - PROXY_PORT=10801
      - RSS_FEED_SIZE=500
      - RSS_FEED_1_NAME=myjackett-feed-1
      - RSS_FEED_1_URL=${DEV_JACKASS_FEED_1}
      - RSS_FEED_2_URL=${DEV_JACKASS_FEED_2}
      - RSS_RULE_1=.*show|tv.*
      - RSS_RULE_2=.*movie.*
      - RSS_RULE_3=.*book.*
    ports:
      - 8080:8080
      - 6881:6881
    extra_hosts:
      - "host.docker.internal:host-gateway"

volumes:
  qbittorrent-storage:
```


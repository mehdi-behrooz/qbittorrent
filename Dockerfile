# syntax=docker/dockerfile:1

FROM alpine:3

RUN apk update && apk add --no-cache qbittorrent-nox tini python3

# RUN addgroup --system --gid 33 qb && \
#     adduser --system --uid 33 --disabled-password --ingroup qb qb && \
#     mkdir -p /config/ /downloads/ && \
#     chown -R qb:qb /config /downloads/

RUN adduser --system --uid 33 --disabled-password --ingroup www-data www-data && \
    mkdir -p /config/ /downloads/ && \
    chown -R www-data:www-data /config /downloads/

COPY --chmod=755 entrypoint.sh /usr/bin/
COPY app/ /app/
COPY templates/ /templates/

EXPOSE 8080 6881 6881/udp
USER www-data
WORKDIR /
VOLUME ["/config"]
VOLUME ["/downloads"]
ENTRYPOINT ["/sbin/tini", "-g", "--", "/usr/bin/entrypoint.sh"]

HEALTHCHECK --interval=5m \
    --start-period=5m \
    --start-interval=10s \
    CMD pgrep /usr/bin/qbittorrent-nox \
    && nc -z 127.0.0.1 8080 \
    || exit 1

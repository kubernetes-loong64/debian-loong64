# debian for LoongArch64

<p align="center"><a href="README.md">English</a> | <a href="README-zh.md">中文</a></p>

<p align="center"><img src="https://img.shields.io/badge/debian%20LoongArch64%20%E9%BE%99%E8%8A%AF%E6%9E%B6%E6%9E%84%E5%8F%91%E8%A1%8C%E7%89%88-blue?logo=debian&logoColor=white" alt="debian LoongArch64 龙芯架构发行版"></p>

Sync [Debian](https://www.debian.org/) container images from `lcr.loongnix.cn/debian` to Docker Hub for the
**LoongArch64 (loong64)** architecture via CI/CD.

## How it works

A GitHub Actions workflow pulls the specified Debian image from `lcr.loongnix.cn/debian`, compares its digest with the
existing image on Docker Hub, and pushes it only when the images differ. Only for image tags that have never been synced before (i.e., tags that were updated),
a date-stamped tag (`<tag>-YYYYMMDD`) is published alongside the regular tag.

## Docker Images

Images are published to Docker Hub under
[`kubernetesloong64/debian-loong64`](https://hub.docker.com/r/kubernetesloong64/debian-loong64).

[![kubernetesloong64/debian-loong64](https://img.shields.io/docker/v/kubernetesloong64/debian-loong64?arch=loong64&logo=docker&label=kubernetesloong64%2Fdebian-loong64&sort=semver)](https://hub.docker.com/r/kubernetesloong64/debian-loong64/tags)

### Available tags

| Tag           | Description               |
|---------------|---------------------------|
| `13`          | Debian 13 (Trixie) — full |
| `13-slim`     | Debian 13 (Trixie) — slim |
| `trixie`      | Debian Trixie — full      |
| `trixie-slim` | Debian Trixie — slim      |
| `14`          | Debian 14 (Forky) — full  |
| `14-slim`     | Debian 14 (Forky) — slim  |
| `forky`       | Debian Forky — full       |
| `forky-slim`  | Debian Forky — slim       |

Image tags that have never been synced before (i.e., tags that were updated) also receive a date-stamped tag
(`<tag>-YYYYMMDD`) for reproducible builds. Images that have already been synced only update the regular tag
when the upstream digest changes.

### Pull images

```shell
docker pull kubernetesloong64/debian-loong64:13
docker pull kubernetesloong64/debian-loong64:13-slim
docker pull kubernetesloong64/debian-loong64:14
docker pull kubernetesloong64/debian-loong64:14-slim
```

## Source

- [lcr.loongnix.cn/debian](https://lcr.loongnix.cn/debian) — upstream Debian images for LoongArch64

## License

[Apache License 2.0](LICENSE)

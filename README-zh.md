# debian for LoongArch64

<p align="center"><a href="README.md">English</a> | <a href="README-zh.md">中文</a></p>

<p align="center"><img src="https://img.shields.io/badge/debian%20LoongArch64%20%E9%BE%99%E8%8A%AF%E6%9E%B6%E6%9E%84%E5%8F%91%E8%A1%8C%E7%89%88-blue?logo=debian&logoColor=white" alt="debian LoongArch64 龙芯架构发行版"></p>

通过 CI/CD 将 [Debian](https://www.debian.org/) 容器镜像从 `lcr.loongnix.cn/debian` 同步到 Docker Hub，目标架构为
**LoongArch64 (loong64)**。

## 工作原理

GitHub Actions 工作流从 `lcr.loongnix.cn/debian` 拉取指定的 Debian 镜像，与 Docker Hub 上已有镜像的 digest 进行对比，
仅当镜像不同时才推送。只有从未同步过的镜像标签（即更新过的标签），才会额外发布一个带日期戳的标签（`<tag>-YYYYMMDD`）。

## Docker 镜像

镜像发布在 Docker Hub 的
[`kubernetesloong64/debian-loong64`](https://hub.docker.com/r/kubernetesloong64/debian-loong64)。

[![kubernetesloong64/debian-loong64](https://img.shields.io/docker/v/kubernetesloong64/debian-loong64?arch=loong64&logo=docker&label=kubernetesloong64%2Fdebian-loong64&sort=semver)](https://hub.docker.com/r/kubernetesloong64/debian-loong64/tags)

### 可用标签

| 标签            | 描述                       |
|---------------|--------------------------|
| `13`          | Debian 13 (Trixie) — 完整版 |
| `13-slim`     | Debian 13 (Trixie) — 精简版 |
| `trixie`      | Debian Trixie — 完整版      |
| `trixie-slim` | Debian Trixie — 精简版      |
| `14`          | Debian 14 (Forky) — 完整版  |
| `14-slim`     | Debian 14 (Forky) — 精简版  |
| `forky`       | Debian Forky — 完整版       |
| `forky-slim`  | Debian Forky — 精简版       |

从未同步过的镜像标签（即更新过的标签）还会额外获得一个带日期戳的标签（`<tag>-YYYYMMDD`），用于可重复构建。已同步过的镜像仅在上游 digest
变化时更新常规标签。

### 拉取镜像

```shell
docker pull kubernetesloong64/debian-loong64:13
docker pull kubernetesloong64/debian-loong64:13-slim
docker pull kubernetesloong64/debian-loong64:14
docker pull kubernetesloong64/debian-loong64:14-slim
```

## 源

- [lcr.loongnix.cn/debian](https://lcr.loongnix.cn/debian) — LoongArch64 上游 Debian 镜像

## 许可证

[Apache License 2.0](LICENSE)

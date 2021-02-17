# Internal docker python test

Internal test

## deploy on docker hub

```bash
docker build -t pytest -t pytest:1.0.0 .
docker push --all-tags
```

### run image locally

```bash
docker run -it -e IOHUB_MSG="IOhub rocks!" pytest
```

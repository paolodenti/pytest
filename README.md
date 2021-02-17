# Internal docker python test

Internal test

## build image locally

```bash
docker build -t paolodenti/pytest .
```

## run image locally

```bash
docker run -it -e IOHUB_MSG="IOhub rocks!" paolodenti/pytest
```

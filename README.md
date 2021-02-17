# Internal docker python test

Internal test

## deploy on docker hub

```bash
docker build -t paolodenti/pytest -t paolodenti/pytest:1.0.0 .
docker push --all-tags paolodenti/pytest
```

### run image locally

```bash
docker run -it -e IOHUB_MSG="IOhub rocks!" paolodenti/pytest
```

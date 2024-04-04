```sh
docker login --username kaminski-pawel --password-stdin XXX ghcr.io
docker build . -t ghcr.io/kaminski-pawel/ecs-task-example:latest
docker push ghcr.io/kaminski-pawel/ecs-task-example:latest
```


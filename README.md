# [GL DevOps ProCam] Entry task

The script prints basic information about your OS to console output.

## Usage 

Get the Docker image:
```sh
docker pull miletskiy/devops_camp:metric
```


> Getting info about CPU:
```sh
docker run --rm miletskiy/devops_camp:metric cpu
```

> Getting info about memory:
```sh
docker run --rm miletskiy/devops_camp:metric mem
```

To simplify the command input can be used next commands:

> Get CPU info
```sh
make cpu
``` 
> Get memory info
```sh
make mem
``` 

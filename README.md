# slack-sentiment

An example of running sentiment analysis on a slack channel.

## Getting Started

This project required [Python](https://www.python.org). Ideally 3.9 or above.

Packages are managed with [pipenv](https://packaging.python.org/tutorials/managing-dependencies/#managing-dependencies).


### Install dependencies

```bash
pipenv sync --dev
```

### Run notebook

```bash
pipenv run notebook
```

## Deploying a Model with Flask and Docker

Assuming you have created a model by running through the [notebook](https://github.com/ruarfff/slack-sentiment/blob/main/Slack%20Sentiment%20Analysis.ipynb), these instructions will show you how to take that model and expose it as a web service deployed using a docker image.

### Build the image

```
docker build -t slack-sentiment .
```

### Run the container

```
docker run -it --rm -p 5000:5000 slack-sentiment
```

If you want to leave the container running in the background instead use:

```
docker run -d -p 5000:5000 slack-sentiment
```

### Test the model

```
$ curl -d "text='Hello! Have a wonderful day.'" -X POST http://localhost:5000/

That text appears to be positive :)
```

```
$ curl -d "text='Boo. This sucks!'" -X POST http://localhost:5000/

That text appears to be negative :(
```






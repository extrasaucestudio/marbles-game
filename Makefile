install:
	docker-compose build

run:
	docker-compose up --force-recreate

test:
	docker-compose run service sh -c ' \
	    flake8 --docstring-convention google service && \
	    mypy --ignore-missing-imports service && \
	    APPLICATION_STAGE=test py.test -vv --failed-first --cov=service \
	    --cov-report=html --durations=10 $(test)'

pytest:
	docker-compose run --no-deps service sh -c ' \
	    APPLICATION_STAGE=test py.test -vv --failed-first --cov=service \
	    --cov-report=html --durations=10 $(test)'

analyse:
	docker-compose run service sh -c 'pylint --ignore tests --exit-zero service'


#!/bin/sh
set -e

alembic upgrade head

pytest --cov=app --cov-report=term-missing
# Support Inbox OpenEnv

Simulates real-world customer support handling.

## Tasks
- Easy: refund
- Medium: complaint
- Hard: billing issue

## Run
docker build -t support-env .
docker run -p 8000:8000 support-env

## Validate
openenv validate

## Inference
python inference.py
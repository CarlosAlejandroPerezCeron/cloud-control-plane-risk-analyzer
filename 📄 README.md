# Cloud Control Plane Risk Analyzer

IAM privilege escalation detection engine for AWS and Kubernetes control planes.

## What It Does

- Parses IAM policies
- Detects privilege escalation paths
- Builds privilege graph
- Calculates risk score
- Provides REST API

## Why It Matters

Control plane compromise equals total environment compromise.

This tool models escalation paths before an attacker does.

## Run

docker-compose up --build

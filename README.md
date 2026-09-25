# REPAIR-X

**AI Software Maintenance Engineer — Fix it. Test it. Prove it.**

REPAIR-X is a hackathon MVP that demonstrates an evidence-based software repair workflow:

Bug Report → Investigation → Reproduction → Root Cause → Fix Proposal → Human Approval → Patch → Tests → Proof-of-Fix.

## MVP
This repository contains the initial working foundation and a deterministic demo repository. The next implementation stages add the repair workflow and Proof-of-Fix dashboard.

## Stack
- Backend: Python + FastAPI
- Frontend: React + TypeScript + Vite
- Database: SQLite
- Testing: Pytest
- Repository: Git/GitHub
- Containerization: Docker

## Important
REPAIR-X must never claim a repair is verified unless the relevant tests actually execute successfully.

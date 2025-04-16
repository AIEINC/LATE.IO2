#!/bin/bash
# GPG-sign all release artifacts
gpg --armor --detach-sign agentic-deployment-v5.0.zip
cosign sign-blob --key cosign.key agentic-deployment-v5.0.zip

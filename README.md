# Norman Objects

Norman Objects are the typed, structured data models used across the Norman SDK, Core SDK, and cloud services.
They define the shape of everything in the system — models, invocations, files, events, users, and more.

This repo provides shared object definitions that guarantee consistent behavior across:

- Norman SDK (Python)
- Norman Core SDK (Python)
- Cloud microservice
- Storage & file-handling pipelines

If you’re working on internal services or extending Norman, this is the source of truth.

# Why Norman Objects Exist

Modern AI platforms rely on dozens of interacting components.
Without strict shared types, systems drift apart, and integrations become fragile.

Norman Objects solve this by standardizing:

- how models are described
- how invocations are represented
- how files are stored and retrieved
- how events and statuses are tracked
- how errors and logs are transported
- how compute results are packaged
- Every service speaks the same language.
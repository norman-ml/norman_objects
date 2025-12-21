# Norman Objects

`norman-objects` is a shared Python library that defines the **core domain models, contracts, and primitives** used across the Norman AI platform. It acts as the *language of the system*, ensuring consistency between SDKs, services, workers, and infrastructure components.

---

## Purpose

Norman Objects exists to:

* Provide **canonical data models** shared across services
* Enforce **strong typing and validation** at boundaries
* Standardize **invocation, messaging, and execution semantics**
* Reduce duplication and drift between microservices
* Serve as the foundation for the Norman SDKs and runtime

If two services communicate in Norman, they should speak using objects from this package.

---

## Usage

This package is intended to be used as a **dependency**, not a standalone service.

---

## Who Should Use This

* Norman SDK maintainers
* Backend service developers
* Runtime / worker implementations
* Infrastructure and orchestration layers

If you are defining a new cross-service contract, it probably belongs here.

## What Does *Not* Belong Here

* Business logic
* Service-specific behavior
* Infrastructure provisioning
* UI / presentation logic

Norman Objects should remain **pure, stable, and boring**.

---

## License

Internal Norman AI project. Usage governed by internal policies.

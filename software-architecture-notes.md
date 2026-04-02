# architectural patterns
## monolith
- one massive program
- might be well organised, but is generally a horrible mess
- difficult to make changes without unexpected side effects

## microkernel (plugin)
- kernel to handle core features
- other functionality plugs in to the core services of the kernel
- e.g. shop. inventory + orders would be the kernel, and email and invoicing as plugins
- might use messaging/api to communicate between kernel and plugins
- plugins are largely independent from other plugins, avoiding the ball of mud that is the monolith
- plugins are indirectly coupled to each other through the kernel, so a plugin might affect whether another plugin can work correctly
- APIs to the kernel are delicate - changes could mean all plugins need rewriting

## Message based
- Takes the notion of a microkernel one step further, by formalising the communication paths between elements and isolating them even further
- Can enable systems not designed to work together, to work as a single system
- Works like a job queue, the "broker"
- No network involved - use shared memory space
- All communication runs through the broker so agents don't need to know about each other
- Publish/subscribe model also goes through a broker
- Independence makes modules way easier to maintain than the monolith, and solves the dependency problems of a microkernel system
- Messaging systems can be slow, and quickly become very complex, and have the problem of storing the messages

## Microservices and miniservices
- Cloud of independent services cooperate as peers to get work done
- Could be spread across a network
- Are resilient systems
- Microservices are independently deployable and fully autonomous (have own databases)
- Hides implementation details
- Can use messaging POST API
- Good for agile as independent and quick to deploy
- Design and runtime complexity, and are network services are slow

## Reactive systems
- Synchronous service can broadcast an event that other systems react to e.g. order placed, and billing, warehouse, and email services can pick that up and act on it.
- Faster than a declarative approach as things can happen in parallel
- Also makes it easy to maintain due to decoupling of the systems.

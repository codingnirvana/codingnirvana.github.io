---
title: "Microservices: What Are They and Why Should You Care?"
date: 2015-03-03
topic: indix
original_url: "https://web.archive.org/web/2016/http://www.indix.com/blog/developer/microservices-what-are-they/"
---

*Over the last year, Microservices has emerged as a “new” approach to building large scale distributed systems. This is an introductory article that provides background on Microservices, their evolution, the pros and cons and the state of the art as it exists today.*

You recently joined a brand new client project as a lead developer/architect. You’re sitting in a meeting room and after having heard the client’s requirements, you are now contemplating the right architecture and technology stack for the project.

Your client wants you to build an ecommerce application for consumers. They want to support multiple clients including browsers on desktop, and mobile including native mobile applications. In those cases, your system receives an HTTP request in either JSON or XML, it executes business logic, accesses database and sends back response in JSON or XML. At the same time, the system should also expose an API to integrate with third party applications.

“This sounds like a typical layered architecture”, you say to yourself. You have built a couple of such systems in the past, so you decide to use tried and tested architecture that you are comfortable with. The different layers of your architecture are divided into Presentation, Business and Database components. For the technology stack, you have a choice between Rails, Java, Scala, Node.js, and .NET. It really does not matter what you use as this architecture pattern is language or platform agnostic. However, your client wants you to release an MVP of the product within the next six months. In the end, you choose a technology stack that a majority of your team of four developers is at ease with.

Fast forward by six months. You are at a team party to celebrate the success of the MVP which was delivered on time. The team celebrates the success but also reflects on what a small team of six (you added two developers mid-way during the MVP) accomplished in a short time.
The team is thankful to you for choosing the familiar technology stack. The layered architecture also provided multiple benefits. It was very easy to make a change as all the code was in a single source code repository.  For the same reason, it was easy for the two new developers to ramp up and set up the entire application on their laptop, build it and run it locally within a couple of hours. The release was also painless given that there was a single deployment pipeline that would take the build from the CI server and deploy it on a couple of load balanced production boxes.

Fast forward to two years later. After the success of the MVP and a few minor pivots later, the customer base of the product has grown. Your client also boosted its sales team in the last two years to aid the growth. And your team has grown to 20 developers. However, the product is not able to scale and evolve with the customer base. You realize that the application feels like a big ship that’s very hard to steer. The application has grown to thousands of lines of code. The ramping up of new developers is taking weeks instead of days. And you are finding it hard to track down developers who can work on your “legacy” codebase. As a result of all these factors, you are not able to deliver as fast as earlier to keep up with the business requirements.

Let’s try to understand what’s wrong with the application that you built. Let’s give it a name first. The term that is used to describe an application like the one above is- “Monolith”.

Below are some of the challenges associated with a large monolithic application.

- Scaling issues – On the one hand, a monolithic application can be scaled horizontally by running multiple copies behind a load balancer. But on the other hand, each component has its own scaling requirements as some components are heavy on I/O and some on memory and hence have different resourcing requirements. With a monolithic application, you have no choice but to provide the same (higher) resources to the entire application, potentially increasing infrastructure costs.

- Technology changes and evolution – Certain problems are best solved with certain technologies. The technology choices you made when you built the monolith may or may not be the perfect fit when your application evolves at a later stage. You might want to move to a different technology stack or replace individual pieces of the architecture. It could be for scaling needs or for better developer productivity. For e.g., JVM vs C++, SQL vs NoSQL. With a monolithic application, you are married to a technology stack for a long time.

- Multiple teams – Your teams are organized as UI, Services and Database layers. Performing any cross cutting features takes time and also needs approval for the right prioritization. Ideally, you want to organize teams around business capability to reduce the communication barriers so that an individual team can take things end to end without a lot of overheads. And if the teams are across locations or time zones, it adds another level of complexity.

- Continuous delivery – Continuous delivery is about reducing the time it takes for a commitment made by a developer to hit production. It’s hard to follow continuous delivery practices when you have a single large codebase. The cycle time will be longer because the entire application has to be built, tested and deployed for any change. In addition, each of these deployments are high risk deployments.

- Ramping up new members – A large monolithic project is intimidating for new developers as it can take a long time to set up, build and run locally.

### Is there a solution?

Yes. Microservices – small autonomous services that work together, can be scaled and released independently with different teams potentially using different languages across different locations.

### So, how do we describe a Microservice?

- Autonomous – Each service can be built using the appropriate tool for the job. Multiple teams of developers can independently deliver functionality in this model. Each microservice can have its own data storage using [polyglot persistence](http://martinfowler.com/bliki/PolyglotPersistence.html).

- Modeled around the business domain – Microservices should be vertically aligned with business capability to provide faster delivery of business goals and outcomes.

- Small, does one thing, and does it well – Where size is a disadvantage for a monolith, it’s an advantage for a microservice. It should also follow the Single Responsibility Principle (SRP) and should strive towards loose coupling and high cohesion that are hallmarks of well-designed components.

- Owning build and deployment – A microservice should be standalone and should be able to run independently from other systems and services.

- Integrates via well-known interfaces – If the microservices expose and talk using well-known interfaces, open protocols and standards, it provides technology heterogeneity, thereby allowing teams to use the technology stack that they are comfortable with or one that is best suited for the problem at hand.

### What’s with the term “Microservices”?

I heard the term “Microservices” for the first time when Fred George spoke about it in his talk at [YOW 2012 – Brazil](https://www.youtube.com/watch?v=2rKEveL55TY). Ronald Kuhn, the tech lead on Akka, thinks that Microservices as a term is too ambiguous and likes to call it [Uniservices](https://twitter.com/rolandkuhn/status/472024650990772224) instead, given what it does.

Netflix used to call its implementation of Microservices as cloud native architecture and fine grained SOA but they have also started to use the term Microservices since that has become most widely accepted.

### How is this different from Service Oriented Architecture (SOA)?

At the heart of it, both Microservices and SOA try to combat the challenges associated with large monolithic applications. SOA’s approach used protocols like SOAP, RPC, and a complex middleware called ESB that meant different things to different people. It had sound principles but there was a lack of consensus on how to do SOA. Moreover, implementation of SOA itself was monolithic where dumb services were integrated with a smart ESB. Proponents of Microservices look at it as a specific approach to SOA in the same way that XP or Scrum are different approaches for Agile software development.

### Why now?

There was always a desire to build systems this way (even in the SOA era) but the recent advances and maturity in the areas of Cloud, DevOps and Continuous Delivery have made it easier to build them right with Microservices being the building blocks.

### Moving towards Microservices

One has to delve into several design aspects and weigh the pros and cons of various approaches while moving towards microservices.

- Splitting the monolith – The first consideration is around splitting the monolith. And the challenge here is to identify the appropriate service boundaries. In this context, [Domain Driven Design](http://en.wikipedia.org/wiki/Domain-driven_design) (DDD) is a nice model to help break your system into [Bounded Contexts](http://martinfowler.com/bliki/BoundedContext.html) that allow you to set logical and physical boundaries between your services. Another challenge will be around splitting the state. For most applications that state will be the database. You should refactor your existing databases to de-normalize into one data source per table. You should also think about modeling foreign key relationships and transactions across two microservices.

- Inter-services Communication – You will have to decide the approaches for communication between microservices. REST over HTTP is a sensible default choice for both synchronous and asynchronous communication. For the payloads, you have a choice of using JSON, XML or Binary Protocols. Prefer using JSON payloads for both external and internal service communication because of its readability and integration across languages. Consider using Binary protocols like Thrift, Avro or Protobuff if performance is a consideration for your internal services.

- Testing – Start with integration tests to make sure that implicit contracts between services are codified. However, these kind of tests are hard to write and tend to be brittle when you have more than a handful of services. Use [consumer driven contract tests](http://martinfowler.com/articles/consumerDrivenContracts.html) in those cases to detect contract breakages. Testing should also be done in post-production environments by running fake requests and asserting on the responses. Consider using a tool like [Shadow](https://github.com/twilio/shadow) from Twilio while rolling out a newer version of a service to compare its responses with the existing service.

- Deployment – Each of the services should be independently deployable for which you should prefer a single repository for each service. Follow Continuous Delivery principles ensuring that every change within the service is built and tested including integration tests as part of a Continuous Integration (CI) pipeline. Upstream dependencies should trigger the contract tests pipeline. Once these go green, the changes should be deployed in staging environments using a deploy pipeline. Use Continuous Delivery practices like [Feature Flags](http://martinfowler.com/bliki/FeatureToggle.html) and [Canary Releasing](http://martinfowler.com/bliki/CanaryRelease.html) to reduce the risk of new features and to roll back problematic code if required. Use [Blue Green Deployments](http://martinfowler.com/bliki/BlueGreenDeployment.html) to ensure zero-downtime for your services. Investigate using container technologies like [Docker](http://www.docker.com/) with orchestration systems like [Marathon](https://github.com/mesosphere/marathon) to help manage complex deployment workflows and to auto scale based on load.

&nbsp;

- Failure Isolation – Failures are common when you have more than a handful of services. If Service A calls Service B which in turn calls Service C, a problem in Service C can cause service disruption to end users. Use Patterns like Timeouts, [Circuit Breaker](http://martinfowler.com/bliki/CircuitBreaker.html), [Bulk Heads](http://skife.org/architecture/fault-tolerance/2009/12/31/bulkheads.html) and Backpressure to isolate failures. In case of cascading failures, consider gracefully degrading the service rather than failing completely. The book [Release It](http://www.amazon.com/Release-It-Production-Ready-Pragmatic-Programmers/dp/0978739213) has a chapter on Stability Patterns that offers a good introduction to this topic.

- Service Discovery – This is the equivalent of the Service Registry problem in SOA. When you have multiple services, you need a way to discover other services that you are dependent on. DNS with a Load Balancer (LB) works for most cases, but is unable to scale in a dynamic environment where nodes are overloaded and are timing out and need to be removed from the LB, or in cases where one needs to auto scale elastically according to load. [Zookeeper](http://zookeeper.apache.org/) has been a great choice in this area for some time as it provides the primitives to build a service discovery solution. [Consul](https://consul.io/) is emerging as an alternative that gives you all the things required for service discovery out of the box.

- Monitoring – When you have multiple services talking to each other, you need tools that can aid in understanding the system behavior and diagnose performance issues. Aggregation becomes very important to provide a unified view of various systems and metrics. Consider using a single tool like [Logstash](http://logstash.net/) or [Splunk](http://www.splunk.com/) to query and aggregate logs from various Microservices. Distributed request tracing provides you the visibility necessary from an end to end perspective when multiple services are involved. Use correlation IDs across various microservices to track the flow of interaction between services and tie them back to the original request. Consider using [Zipkin](https://blog.twitter.com/2012/distributed-systems-tracing-with-zipkin) from Twitter, an open source solution inspired by [Dapper](http://research.google.com/pubs/pub36356.html) from Google.

- Documentation – If one does not know what your service does, it’s likely that no one will use it. Use [Swagger](http://swagger.io/) or [Postman Collections](https://www.getpostman.com/docs/collections) to document your RESTful APIs.

- API Gateway – If your clients need to orchestrate data from multiple microservices, the API Gateway provides a way to handle cross cutting concerns like authentication, quota management, rate limiting, basic analytics etc. You can also provide a different granularity for end users by composing one or two microservices using the API Gateway.  [Zuul](http://techblog.netflix.com/2013/06/announcing-zuul-edge-service-in-cloud.html) from Netflix is an open source alternative and [3scale](http://www.3scale.net/), [Apigee](http://apigee.com/) and [Mashery](http://www.mashery.com/) are commercial solutions.

### Microservices OSS Stack

Let’s talk about some OSS that’s available to help migrate towards Microservices.

- Netflix – Netflix has a fully functional microservices stack that they have been using internally for a few years. They have open sourced several key pieces of their stack in recent times. Some notable libraries include

  - Hystrix – Fault Tolerant library

  - Eureka – Service Registration and Discovery

If you are using Spring, the [Spring Cloud Netflix](http://cloud.spring.io/spring-cloud-netflix/) project integrates these libraries into the Spring ecosystem.

- Twitter – All of Twitter’s traffic until the end of 2012 was served by a single monolithic rails application, internally called “MonoRail”. Since then, they have moved to using Twitter Server for building their microservices, which is built on top of Finagle. Finatra and Finch are noteworthy frameworks from Twitter. SoundCloud and Tapas are examples of companies that are successfully using the Twitter Microservices stack in production.

- Typesafe – Typesafe’s reactive platform provides the building blocks to build a microservices platform. You can use Spray (to be superseded by Akka-HTTP), Akka-Camel, Akka-Streams to build your own microservices stack on top of the Typesafe platform. Bench.co is a company that’s using the Typesafe stack to build their microservices platform.

- Dropwizard is a JVM based microcontainer that pulls together battle tested libraries for configuration, metrics, and logging to create RESTful microservices.

- Roll Your Own – Of course, you could also roll your own stack by using various pieces from existing stacks and building on top of them.

The above list is not comprehensive and is focused on the JVM platform as majority of the Microservices at Indix run on the JVM. We are currently using Dropwizard and the Typesafe stack but are also actively evaluating the Neflix and Twitter stacks. We also have non-JVM microservices where we are using Bottle and Flask for Python, Express for Node.JS and Sinatra for Ruby.

### What are the disadvantages?

The rosy picture I painted after the initial gloom might make you believe that Microservices would solve all your architectural problems. Sorry to break your heart, but like everything else in software, Microservices are not a silver bullet. It’s an architecture style that is still maturing and has its own share of challenges.

- When you are running multiple microservices, it becomes extremely important to manage the operational complexity associated with it. You need to make sure that you have the right tools in place in order to visualize and orchestrate your deployment and also ensure that you are able to monitor the complex interactions between these systems. You need to build the right set of tools as well as the skill set within your teams to handle this complexity.

- If your team is using multiple language and technology stacks to build their services, lack of standardization might slow you down especially when debugging failures.

- As you work with implicit interfaces across microservices, you will need to worry about backward compatibility and versioning. It needs co-ordination across teams and the solution to this may or may not be technical.

### Should I move to a Microservice architecture?

This is one of those questions that has an YMMV (Your Mileage May Vary) answer.

At Indix, we started with a monolith (but modular) application which was built over the course of the last three years. As I write this article, we are migrating to microservices across all our teams. The reasons for us to move to microservices are captured in the section describing the problems with the monolith. In hindsight, starting with a monolith and breaking it down into microservices with the team growing and the system getting complex, seems like the right approach.

To provide a different perspective, I would refer to [Go-CD](http://www.go.cd/) – an open source build and release management tool. I worked on the team about three years back. Right now, it’s a six+ year old project and the codebase is still a monolith. I think the reason why it’s stayed so is because there were not more than ten developers at any given point of time. The team is co-located and would ramp up only two or three new developers every year. The team uses techniques like [Branch by Abstraction](http://martinfowler.com/bliki/BranchByAbstraction.html) and [Strangler Approach](http://www.martinfowler.com/bliki/StranglerApplication.html) to evolve with changing technological trends. It will be interesting to see if the community decides to split Go-CD into multiple Microservices at some point.

If you want to move towards a Microservices architecture, you should read Martin Fowler’s article on “[Pre-requisites for Microservices](http://martinfowler.com/bliki/MicroservicePrerequisites.html)”.

### Summary

Microservices is an important tool in the arsenal of an evolutionary architect. Microservices themselves have evolved out of the hard earned lessons of engineers building large scale systems. When systems and teams scale, breaking them down into Microservices decouples your systems and gives more options and choices to evolve them independently. Like any other tool, it is important to know when and how to use it. Hopefully, this article has provided you enough context to decide on both.

### Further Reading

If you are really interested in diving deeper into building Microservices, I suggest ordering a copy of the excellent book by Sam Newman called *Building Microservices*.

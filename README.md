<p align="center">
  <img alt="locust" src="https://miro.medium.com/max/1149/1*8RGtKlAWyEiEhiG3-aHt_g.jpeg" width="250px" float="center"/>
</p>

<p align="center">
  <img alt="locust" src="docs/GitHub.png" width="125px" float="center"/>
</p>

<h1 align="center">Welcome to Locust Playground repository</h1>

> A gentle introduction to Locust

## Menu

<p align="left">
  <a href="#description">Description</a>&nbsp;&nbsp;&nbsp;|&nbsp;&nbsp;&nbsp;
  <a href="#how-to-contribute">How to contribute</a>
</p>

## Getting Started

If you want use this repository you need to make a **git clone**:

>
> 1. git clone --depth 1 https://github.com/lpmatos/locust-playground.git -b master
>

This will give access on your **local machine**.

## Description

#### What is Locust?

From locust.io:

>
> Locust is an easy-to-use, distributed, user load testing tool. Intended for load testing web sites (or other systems) and figuring out how many concurrent users a system can handle.
>

#### Why Locust?

* Load testing is hard to do on small projects - Locust makes it way easier, and it's written for Python 2.7, which you already have on your machine (you don't have to mess around with the JDK). Not currently python 3 compatible (🐍 3️⃣ 👎).

* POPO Philosophy. Very little procedural code, and minimal boilerplate. Everything is a Python class or Dict.

* Loose coupling of testing infrastructure with codebases (one set of tests can be used against multiple web services).

* Very scaleable - can run in a local mode on your machine or distributed mode with an arbitrary number of master and slave servers.

* Efficient CLI or pretty Web UI for interpreting results. Take your pick.

#### Why NOT Locust?

* Locust is not a replacement for unit and integration testing. It doesn't do much to help you trace errors beyond logging the HTTP response statuses and any messages in the body. It's a specialist tool.

* Can be frustrating to implement complex API scenarios because there's little abstraction over the HTTP calls themselves in Locust's native interface.

* Much better at testing RESTful than stateful APIs (you're not writing stateful APIs, right? It's 2016.).

#### Making a locustfile.py

A locustfile must minimally define two objects. A client class (HttpLocust), that manages interactions with the API and a TaskSet class that defines the types of behaviors to test against the API.

## How to contribute

>
> 1. Make a **Fork**.
> 2. Follow the project organization.
> 3. Add the file to the appropriate level folder - If the folder does not exist, create according to the standard.
> 4. Make the **Commit**.
> 5. Open a **Pull Request**.
> 6. Wait for your pull request to be accepted.. 🚀
>

Remember: There is no bad code, there are different views/versions of solving the same problem. 😊

## Add to git and push

You must send the project to your GitHub after the modifications

>
> 1. git add -f .
> 2. git commit -m "Added - Fixing somethings"
> 3. git push origin master
>

## Buy me a coffee

<p align="left">
  <img alt="locust" src="docs/By me a Coffe.png" width="150px" float="center"/>
</p>

## Author

👤 **Lucca Pessoa**

## Show your support

Give a ⭐️ if this project helped you!

---

_This README was generated with ❤️ by [glabby](https://github.com/lpmatos/glabby.git)_

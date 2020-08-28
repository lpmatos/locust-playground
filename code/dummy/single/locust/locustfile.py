from locust import HttpUser, TaskSet, task, between

class UserTasks(TaskSet):

  @task
  def index(self):
    self.client.get("/")

class WebsiteUser(HttpUser):
  tasks = [UserTasks]
  min_wait = 1000
  max_wait = 2000

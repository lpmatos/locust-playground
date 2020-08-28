from locust import HttpUser, TaskSet, task, between

CREDENTIALS = {
  "email": "eve.holt@reqres.in",
  "password": "cityslicka"
}

class UserTasks(TaskSet):

  def on_start(self):
    self.client.post("/api/login", CREDENTIALS)

  @task(2)
  def list_users(self):
    self.client.get("/api/users?page=2")

  @task(1)
  def single_user(self):
    self.client.get("/api/users/2")

class WebsiteUser(HttpUser):
  tasks = [UserTasks]
  wait_time = between(5, 15)

from locust import HttpUser, TaskSet, task, between

class UserTasks(TaskSet):

  # The method on_start is called when a Locust start before any task is scheduled
  def on_start(self):
    self.login()

  def login(self):
    self.client.post("/login", json={"username":"admin", "password":"admin"})

  @task
  def index(self):
    self.client.get("/")

  @task(3)
  def profile(self):
    self.client.get("/profile")

class WebsiteUser(HttpUser):
  """    
  Locust user class that does requests to the locust web server running on localhost    
  """
  tasks = [UserTasks]
  wait_time = between(2, 5)

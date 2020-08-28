import logging
from config import Config
from typing import NoReturn
from locust import HttpUser, SequentialTaskSet, TaskSet, task, between, events

# ==============================================================================
# GLOBAL
# ==============================================================================

config = Config()

CREDENTIALS = {
  "email": config.get_env("CREDENTIALS_USER") if config.get_env("CREDENTIALS_USER") else "eve.holt@reqres.in",
  "password": config.get_env("CREDENTIALS_PASSWORD") if config.get_env("CREDENTIALS_PASSWORD") else "cityslicka"
}

LIST_CREDENTIALS = [
  {
    "email": "eve.holt@reqres.in",
    "password": "cityslicka"
  },
  {
    "email": "tobias.funke@reqres.in",
    "password": "pistol"
  },
  {
    "email": "michael.lawson@reqres.in",
    "password": "432432"
  }
]

# ==============================================================================
# LOGGING
# ==============================================================================

logging.basicConfig(
  level=logging.INFO,
  format="%(asctime)s  %(levelname)-10s %(processName)s  %(name)s %(message)s",
  datefmt="%Y-%m-%d-%H-%M-%S"
)

# ==============================================================================
# LOCUST EVENTS
# ==============================================================================

@events.test_start.add_listener
def on_test_start(**kwargs):
  print("A new Load Test with Locust is starting")

@events.test_stop.add_listener
def on_test_stop(**kwargs):
  print("Load Test with Locust is ending")

@events.request_success.add_listener
def my_success_handler(request_type, name, response_time, response_length, **kw):
  print("Successfully made a request to: %s" % name)

from locust import events

@events.quitting.add_listener
def _(environment, **kw):
  if environment.stats.total.fail_ratio > 0.01:
    logging.error("Test failed due to failure ratio > 1%")
    environment.process_exit_code = 1
  else:
      environment.process_exit_code = 0

# ==============================================================================
# FUNCTIONS
# ==============================================================================

def get_list_users(taskset):
  with taskset.client.get("/api/users?page=2") as response:
    logging.info(response.text)

# ==============================================================================
# LOCUST - CONFIG TASKS FOR A USER
# ==============================================================================

class ListUserTasks(TaskSet):

  def on_start(self) -> NoReturn:
    self.login()

  def login(self) -> NoReturn:
    for index, user in enumerate(LIST_CREDENTIALS):
      email = user["email"]
      logging.info(f"User {email} - Position User {index}")
      with self.client.post("/api/login", user) as response:
        if response.status_code != 200:
          logging.error("Falha ao logar")

  tasks = {get_list_users: 3}

  @task(5)
  def get_single_user(self) -> NoReturn:
    self.client.get("/api/users/2")

class UserTasks(SequentialTaskSet):

  def on_start(self) -> NoReturn:
    self.register()

  def register(self) -> NoReturn:
    with self.client.post("/api/register", CREDENTIALS) as response:
      if response.status_code != 200:
        logging.error("Falha ao registrar")

  @task
  def login(self) -> NoReturn:
    with self.client.post("/api/login", CREDENTIALS) as response:
      if response.status_code != 200:
        logging.error("Falha ao logar")

  tasks = [get_list_users]

  @task
  def get_single_user(self) -> NoReturn:
    self.client.get("/api/users/2")

# ==============================================================================
# LOCUST - REPRESENT A REAL USER
# ==============================================================================

class WebsiteUser(HttpUser):
  tasks = [UserTasks]
  wait_time = between(5, 15)

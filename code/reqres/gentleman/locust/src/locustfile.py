import logging
from config import Config
from typing import NoReturn
from locust import HttpUser, SequentialTaskSet, TaskSet, task, between

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
      with self.client.post("/api/login", user) as response:
        if response.status_code == 200:
          logging.info(f"Logado com sucesso! - Position {index}")
        else:
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
      if response.status_code == 200:
        logging.info("Registrado com sucesso!")
      else:
        logging.error("Falha ao registrar")

  @task
  def login(self) -> NoReturn:
    with self.client.post("/api/login", CREDENTIALS) as response:
      if response.status_code == 200:
        logging.info("Logado com sucesso!")
      else:
        logging.error("Falha ao logar")

  tasks = [get_list_users]

  @task
  def get_single_user(self) -> NoReturn:
    self.client.get("/api/users/2")

# ==============================================================================
# LOCUST - REPRESENT A REAL USER
# ==============================================================================

class WebsiteUser(HttpUser):
  tasks = [ListUserTasks]
  wait_time = between(5, 15)

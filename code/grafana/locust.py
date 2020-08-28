from locust import HttpUser, TaskSet, task, between

"""
Locust - User:
  * Represents a single user.
  * Locust will spwan one instance of the class ofr each user being simulated.

tasks:
  * Points to a TaskSet class thar defines the behavior of the user.

min_wait and max_wait:
  * The minimum and maximum time a user may wait between requests, reandomized.
"""

"""
TaskSet

* Methods decorated with @task are executed.
* Providing a number to @task will weight it.
* on_start is called when a simulated user starts the TaskSet.
"""

class UserTasks(TaskSet):

  @task
  def index(self):
    self.client.get("/")

class WebsiteUser(HttpUser):
  """    
  Locust user class that does requests to the locust web server running on localhost    
  """
  tasks = [UserTasks]
  wait_time = between(2, 5)

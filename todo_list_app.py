# from status import Status       # Remember to import status and priority from the provided files
# from priority import Priority
from flask import Flask, render_template, redirect, url_for, request

app = Flask(__name__)

# task lists

tasklists = {
    1: {
        "name": "Python list",
        "last_updated": "2012-04-23T18:25:43.511Z",
        "created_at": "2012-04-23T18:25:43.511Z",
        "tasks": [
            1,
            2,
            3
        ],
        },
    2: {
        "name": "Home list",
        "last_updated": "2012-04-23T18:25:43.511Z",
        "created_at": "2012-04-23T18:25:43.511Z",
        "tasks": [
            4,
            5
        ],
    }
}

# tasks

tasks = {
    1: {
        "name": "learn flask blueprints",
        "last_updated": "2020-04-23",
        "created_at": "2020-04-23",
        # "status": Status.DONE,
        # "priority": Priority.HIGH,
        "description": "Etiam sit amet massa nec urna hendrerit gravida et sed ipsum."
    },
    2: {
        "name": "learn Python enums",
        "last_updated": "2012-04-20",
        "created_at": "2012-04-20",
        # "status": Status.IN_PROGRESS,
        # "priority": Priority.MEDIUM,
        "description": """Lorem ipsum dolor sit amet,
         consectetur adipiscing elit."""

    },
    3:  {
        "name": "revise OOP concepts",
        "last_updated": "2020-04-25",
        "created_at": "2020-04-25",
        # "status": Status.DONE,
        # "priority": Priority.HIGH,
        "description": "Ut eget elit interdum neque faucibus viverra."
    },
    4:  {
        "name": "clean keyboard",
        "last_updated": "2020-04-25",
        "created_at": "2020-04-25",
        # "status": Status.DONE,
        # "priority": Priority.HIGH,
        "description": "Donec fermentum lacus ultrices mauris pretium, sit amet placerat felis dictum."
    },
    5:  {
        "name": "water plants",
        "last_updated": "2020-04-25",
        "created_at": "2020-04-25",
        # "status": Status.DONE,
        # "priority": Priority.HIGH,
        "description": "Nam imperdiet ligula quis ligula rhoncus, et vehicula sem consectetur."
    }
}

# tasklist routing
@app.route("/")
def task_lists():
    return render_template("tasklists.html", tasklists = tasklists)

@app.route("/editname")
def edit_tasklist_name():
    return render_template("edit_name.html")

@app.route("/deletetasklist")
def delete_tasklist():
    return redirect(url_for("tasklists"))

@app.route("/createtasklist")
def create_tasklist():
    return render_template("create_tasklist.html")



# task routing
@app.route("/tasks")
def tasks_():
    return render_template("tasks.html", tasks = tasks)

@app.route("/edittask")
def edit_task():
    return render_template("edit_task.html")

@app.route("/deletetask")
def delete_task():
    return redirect(url_for("tasks"))

@app.route("/createtask")
def create_task():
    return render_template("create_task.html")




if __name__ == "__main__":
    app.run(debug=True)
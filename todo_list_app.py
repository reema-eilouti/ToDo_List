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
        "description": "Etiam"
    },
    2: {
        "name": "learn Python enums",
        "last_updated": "2012-04-20",
        "created_at": "2012-04-20",
        # "status": Status.IN_PROGRESS,
        # "priority": Priority.MEDIUM,
        "description": "hello"

    },
    3:  {
        "name": "revise OOP concepts",
        "last_updated": "2020-04-25",
        "created_at": "2020-04-25",
        # "status": Status.DONE,
        # "priority": Priority.HIGH,
        "description": "Ut "
    },
    4:  {
        "name": "clean keyboard",
        "last_updated": "2020-04-25",
        "created_at": "2020-04-25",
        # "status": Status.DONE,
        # "priority": Priority.HIGH,
        "description": "Donec"
    },
    5:  {
        "name": "water plants",
        "last_updated": "2020-04-25",
        "created_at": "2020-04-25",
        # "status": Status.DONE,
        # "priority": Priority.HIGH,
        "description": "Nam "
    }
}

# tasklist routing
@app.route("/")
def task_lists():
    return render_template("tasklists.html", tasklists = tasklists)

@app.route("/editname/<int:index>" , methods=["POST" , "GET"])
def edit_tasklist_name(index):
    if request.method == "GET":
        return render_template("edit_name.html")

    else:
        new_name=request.form["name"]
        tasklists[index].update({'name': new_name})
        return redirect(url_for('task_lists'))



@app.route("/deletetasklist/<int:index>")
def delete_tasklist(index):
    tasklists.pop(index)
    return redirect(url_for("task_lists"))



@app.route("/createtasklist")
def create_tasklist():
    return render_template("create_tasklist.html")



# task routing
@app.route("/tasks")
def tasks_():
    return render_template("tasks.html", tasks = tasks)



@app.route("/edittask/<int:index>", methods=["POST" , "GET"])
def edit_task(index):

    if request.method == "GET":
        return render_template("edit_task.html")

    else:
        new_name=request.form["name"]
        new_description=request.form["description"]
        tasks[index].update({'name': new_name , 'description' : new_description})
        return redirect(url_for('tasks_'))

    



@app.route("/deletetask/<int:index>")
def delete_task(index):
    tasks.pop(index)
    return redirect(url_for("tasks_"))

@app.route("/createtask")
def create_task():
    return render_template("create_task.html")




if __name__ == "__main__":
    app.run(debug=True)
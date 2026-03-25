let tasks = JSON.parse(localStorage.getItem("tasks")) || [];
let currentFilter = "all";
let debounceTimer;

function addTask() {
    let name = document.getElementById("taskInput").value;
    let priority = document.getElementById("priority").value;
    let deadline = document.getElementById("deadline").value;

    if (name === "") {
        alert("Enter task name");
        return;
    }

    let task = {
        id: Date.now(),
        name,
        priority,
        deadline,
        completed: false
    };

    tasks.push(task);
    saveTasks();
    renderTasks();
}

function saveTasks() {
    localStorage.setItem("tasks", JSON.stringify(tasks));
}
function renderTasks() {
    let list = document.getElementById("taskList");
    list.innerHTML = "";

    let filtered = tasks.filter(task => {
        if (currentFilter === "completed") return task.completed;
        if (currentFilter === "pending") return !task.completed;
        return true;
    });

    filtered.forEach(task => {
        let card = document.createElement("div");
        card.className = "card mb-2 p-2";

        let badgeColor = "bg-success";
        if (task.priority === "Medium") badgeColor = "bg-warning";
        if (task.priority === "High") badgeColor = "bg-danger";

        card.innerHTML = `
            <div class="d-flex justify-content-between align-items-center">
                <div class="${task.completed ? 'completed' : ''}">
                    <strong>${task.name}</strong>
                    <span class="badge ${badgeColor}">${task.priority}</span>
                    <br>
                    <small>${task.deadline}</small>
                </div>

                <div>
                    <button class="btn btn-sm btn-success" onclick="toggleTask(${task.id})">✔</button>
                    <button class="btn btn-sm btn-danger" onclick="deleteTask(${task.id})">X</button>
                </div>
            </div>
        `;

        list.appendChild(card);
    });

    updateCounter();
}

function toggleTask(id) {
    tasks = tasks.map(task => {
        if (task.id === id) {
            task.completed = !task.completed;
        }
        return task;
    });

    saveTasks();
    renderTasks();
}

function deleteTask(id) {
    tasks = tasks.filter(task => task.id !== id);
    saveTasks();
    renderTasks();
}

function debounceFilter(type) {
    clearTimeout(debounceTimer);

    debounceTimer = setTimeout(() => {
        currentFilter = type;
        renderTasks();
    }, 300);
}

function sortTasks(type) {
    if (type === "priority") {
        let order = { High: 3, Medium: 2, Low: 1 };
        tasks.sort((a, b) => order[b.priority] - order[a.priority]);
    }

    if (type === "deadline") {
        tasks.sort((a, b) => new Date(a.deadline) - new Date(b.deadline));
    }

    saveTasks();
    renderTasks();
}

function updateCounter() {
    document.getElementById("total").innerText = tasks.length;

    let completed = tasks.filter(t => t.completed).length;
    let pending = tasks.length - completed;

    document.getElementById("completed").innerText = completed;
    document.getElementById("pending").innerText = pending;
}


renderTasks();
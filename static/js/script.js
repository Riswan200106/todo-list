document.getElementById('add-task-btn').addEventListener('click', function() {
    const taskInput = document.getElementById('task-input');
    const task = taskInput.value.trim();

    if (task) {
        const taskItem = document.createElement('div');
        taskItem.classList.add('task-item');
        taskItem.textContent = task;

        const tasks = document.querySelector('.tasks');
        tasks.appendChild(taskItem);

        taskInput.value = '';
    }
});

document.getElementById('delete-finished-btn').addEventListener('click', function() {
    const tasks = document.querySelectorAll('.task-item');
    tasks.forEach(task => {
        if (task.style.textDecoration === 'line-through') {
            task.remove();
        }
    });
});
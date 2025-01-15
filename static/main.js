document.addEventListener('DOMContentLoaded', function() {
    const taskInput = document.querySelector('textarea[name="task"]');
    const executeButton = document.getElementById('executeButton');
    
    taskInput.addEventListener('input', function() {
        if (taskInput.value.trim() !== '') {
            executeButton.disabled = false;
        } else {
            executeButton.disabled = true;
        }
    });
});

function setButtonLoadingState() {
    var button = document.getElementById('executeButton');
    button.innerHTML = '<span class="spinner-border spinner-border-sm" role="status" aria-hidden="true"></span> 実行中...';
    button.disabled = true;
}

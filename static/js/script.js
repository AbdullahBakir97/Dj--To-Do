document.addEventListener('DOMContentLoaded', () => {
    const checkboxes = document.querySelectorAll('.todo-item input[type="checkbox"]');
    checkboxes.forEach(checkbox => {
        checkbox.addEventListener('change', () => {
            checkbox.closest('form').submit();
        });
    });
});
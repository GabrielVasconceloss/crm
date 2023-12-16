function showForm() {
    document.getElementById('myForm').style.display = 'block';
    document.querySelector('.bnt-add-status').style.display = 'none';
    formDiv.style.display = 'block';
    formDiv.classList.add('div-form-add-status');
    addButton.classList.add('hidden');
    formDiv.addEventListener('animationend', function() {
        addButton.style.display = 'none';
    });
}


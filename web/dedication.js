window.onload = function() {
    let name = localStorage.getItem('player-name');
    if(name) {
        document.querySelector('#player-name').textContent = name;
    } else {
        alert('Name not found!');
    }
};
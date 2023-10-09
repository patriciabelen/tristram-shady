document.querySelector('form').addEventListener('submit', (e) =>{
    e.preventDefault()

    let name = document.querySelector('.fname').value

    localStorage.setItem('player-name', name)

    window.location.href = "01_dedication.html"
})
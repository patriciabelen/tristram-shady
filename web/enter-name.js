document.querySelector('form').addEventListener('submit', (e) =>{
    e.preventDefault()

    // Capture the name from the input field
    let name = document.querySelector('.fname').value

    // Store the name in local storage
    localStorage.setItem('player-name', name)

    // Redirect to the next page
    window.location.href = "01_dedication.html"
})
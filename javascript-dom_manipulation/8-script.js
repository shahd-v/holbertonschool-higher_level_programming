document.querySelector('#btn_translate').addEventListener('click', () => {
  const language = document.querySelector('#language_code').value
  fetch(`https://www.fourtonfish.com/hellosalut/?lang=${language}`)
    .then(response => response.json())
    .then(data => {
      document.querySelector('#hello').textContent = data.hello
    })
})

document.getElementById("form").addEventListener("submit", function(event) {
    event.preventDefault(); // Previne o comportamento padrão do formulário (recarregar a página)

    const nome = document.getElementById("nome").value
    const email = document.getElementById("email").value
    const msg = document.getElementById("msg").value
    const envios = document.getElementById("dados")
    envios.innerHTML=
    `<h3>Dados Enviados:</h3>
    <p><strong>Nome:</strong> ${nome}</p>
    <p><strong>Email:</strong> ${email}</p>
    <p><strong>Mensagem:</strong> ${msg}</p>`
})

const content = document.querySelector(".content")
const inputSearch = document.querySelector("input[type='search']")

let itens = [];

inputSearch.oninput = () => {
    content.innerHTML = ""

    itens
    .filter((item) =>
        item.toLowerCase().includes(inputSearch.value.toLowerCase())
        )
        .forEach((item) => addHTML(item))
}

function addHTML(item) {
    const div = document.createElement("div")
    div.innerHTML = item
    content.append(div)
}

fetch("https://jsonplaceholder.typicode.com/users")
.then((data) => data.json())
.then((users) => {
    users.forEach(user => {
        addHTML(user.name);  // Adiciona o nome de cada usuário ao conteúdo
        itens.push(user.name);  // Adiciona os nomes à lista de itens para pesquisa
    });
})
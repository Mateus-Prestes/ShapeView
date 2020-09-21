var nome= document.querySelector(".nome")
var senha= document.querySelector(".senha")

function acesso() {

    const lsUsers = localStorage.getItem('USERS');

    if (!lsUsers) {
        alert("Não existem usuários cadastrados");
        return;
    }

    const users = JSON.parse(lsUsers);

    const user = users?.filter(user => user?.name === nome?.value);

    if (user.lenght <= 0) {
        alert("Usuário não encontrado");
        return;
    }

    console.log(`usuário atual`, user[0], users);

    if (user[0].name === nome.value && user[0].password === senha.value ) {
        window.location.href = "./acesso.html";
    } else {
        alert("dados incorretos")
        return;
    }
}


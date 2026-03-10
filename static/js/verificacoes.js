//let nome= prompt("Como você se chama?")

//if (nome == null) {
  //  alert("Recarregue a página")
//} else {
    //let correto = confirm("Você se chama " + nome + "?")
//if (correto) {
   // alert(nome + " Bem vindo ao site de cursos")
//} else
   // alert("Recague a página")
//}

document.addEventListener("DOMContentLoaded", function (){
    const formLogin = document.getElementById('form-login')
    formLogin.addEventListener("submit", function (event){
        const inputEmail = document.getElementById('input-email')
        const inputSenha = document.getElementById('input-senha')
        let temErro = False
        //verificar se os input estão vazios

        if (inputEmail.value === '') {
            inputEmail.classList.add('is-invalid')
            temErro = true
          } else {
            inputEmail.classList.remove('is-invalid')
        }

        if (inputSenha.value === '') {
            inputSenha.classList.add('is-invalid')
            temErro = true
        } else {
            inputSenha.classList.remove('is-invalid')
        }

        if (temErro){
            //evita de enviar o formulario
            event.preventDefault()
            alert("Preencha todos os campos")
        }
    })
})

function limpaInputslogin(){
    const inputEmail = document.getElementById('input-email')
    const inputSenha = document.getElementById('input-senha')

    inputEmail.value = ''
    inputSenha.value = ''
}
 nnn

document.addEventListener("DOMContentLoaded", function (){
    const formLogin = document.getElementById('form-cadastro')
    formLogin.addEventListener("submit", function (event){
        const inputNome = document.getElementById('input-nome')
        const inputEmail = document.getElementById('input-email')
        const inputSenha = document.getElementById('input-senha')
        let temErro = False
        //verificar se os input estão vazios

        if (inputNome.value === '') {
            inputNome.classList.add('is-invalid')
            temErro = true
          } else {
            inputNome.classList.remove('is-invalid')
        }

        if (inputEmail.value === '') {
            inputEmail.classList.add('is-invalid')
            temErro = true
          } else {
            inputEmail.classList.remove('is-invalid')
        }

        if (inputSenha.value === '') {
            inputSenha.classList.add('is-invalid')
            temErro = true
        } else {
            inputSenha.classList.remove('is-invalid')
        }

        if (temErro){
            //evita de enviar o formulario
            event.preventDefault()
            alert("Preencha todos os campos")
        }
    })
})


function limpaInputscadastro(){
    const inputNome = document.getElementById('input-nome')
    const inputEmail = document.getElementById('input-email')
    const inputSenha = document.getElementById('input-senha')

    inputNome.value = ''
    inputEmail.value = ''
    inputSenha.value = ''
}

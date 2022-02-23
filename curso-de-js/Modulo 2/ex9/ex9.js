let agora = new Date()
let hora = agora.getHours()
let texto = window.document.querySelector('h2#h2')
let imagem = window.document.querySelector('img#img')
let corpo = window.document.getElementsByTagName('body')[0]
let texto2 = window.document.querySelector('h3#h3')
if(hora >= 6 && hora < 12){
    corpo.style.backgroundColor = 'yellow'
    texto.innerHTML = 'Olá bom dia'
    imagem.src = 'manha.png'
    texto2.innerHTML = `Agora são ${hora} horas`
}
else if(hora >= 12 && hora < 18){
    corpo.style.backgroundColor = 'orange'
    texto.innerHTML = 'Olá boa tarde'
    imagem.src = 'tarde.png'
    texto2.innerHTML = `Agora são ${hora} horas`
}
else if(hora >= 18 && hora < 30 || hora >= 0 && hora < 6){
    corpo.style.backgroundColor = 'darkblue'
    texto.innerHTML = 'Olá boa noite'
    imagem.src = 'noite.png'
    texto2.innerHTML = `Agora são ${hora} horas`
}











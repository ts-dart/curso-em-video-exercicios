function clicar(){
    let paisDeOrigemJs = window.document.querySelector('input#paisDeOrigem').value
    let paisAtualJs = window.document.querySelector('input#paisAtual').value
    let resJs = window.document.querySelector('div#res')
    if(paisDeOrigemJs == paisAtualJs){
        resJs.innerHTML = 'Voce esta em seu pais de origem'
    }
    else{
        resJs.innerHTML = 'Voce esta em um pais estrangeiro'
    }
}